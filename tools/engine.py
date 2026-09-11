#!/usr/bin/env python3
"""
engine.py  --  build the patched executables from original/ into build/, and verify them

    python3 tools/engine.py build     KOUSEI.EXE: hookfont -> halfwidth --glyph-only -> renderer -> slotext apply
                                      SLPS_008.29: namegrid -> menutext -> prompttext
    python3 tools/engine.py verify    riotfont simcheck + slotext simulate on build/KOUSEI.EXE (both must PASS),
                                      slpsmap on build/SLPS_008.29, bankext simulate on build/MAIN1.EXE if present
    --main1-buffer 0xADDR             also build MAIN1.EXE (tools/bankext.py: per-bank SCRIPT.BIN layout, bank
                                      buffer relocated to ADDR). ADDR needs savestate evidence: FLAGS §BD3/§BD5.

The chains are findings.md §18 and §22 plus pending/slot-extension.md §3 (FLAGS §BC3). The font
payload goes to 0x80105448, the run the compact build has shipped in since 2026-07-30 (Appendix B:
xref-clean; validated by one savestate). Re-validate placement with
    python3 tools/riotfont.py liveness build/KOUSEI.EXE STATE.sav
whenever a DuckStation savestate is available. Then the game files:
    python3 tools/assemble.py build --extended      # HEXMAP.BIN with the appended tier-A slots
"""
import sys, os, subprocess, tempfile, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, 'tools')
ORIG = os.path.join(ROOT, 'original')
BUILD = os.path.join(ROOT, 'build')
FONT_ADDR = '0x80105448'


def run(args, must=None):
    cmd = [sys.executable, os.path.join(TOOLS, args[0])] + list(args[1:])
    print('  $ ' + ' '.join(os.path.relpath(c, ROOT) if os.path.isabs(c) else c for c in cmd[1:]))
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).rstrip()
    for line in out.split('\n')[-4:]:
        if line.strip():
            print('    ' + line)
    if r.returncode != 0:
        raise SystemExit('FAILED: %s' % ' '.join(args))
    if must and must not in out:
        raise SystemExit('FAILED: %r not in the output of %s' % (must, ' '.join(args)))
    return out


def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]


def build(main1_buffer=None):
    for f in ('KOUSEI.EXE', 'SLPS_008.29') + (('MAIN1.EXE',) if main1_buffer else ()):
        if not os.path.exists(os.path.join(ORIG, f)):
            raise SystemExit('original/%s missing — run python3 tools/unpack.py first' % f)
    os.makedirs(BUILD, exist_ok=True)
    t = tempfile.mkdtemp()
    k = lambda n: os.path.join(t, n)
    print('KOUSEI.EXE')
    run(['riotfont.py', 'hookfont', os.path.join(ORIG, 'KOUSEI.EXE'), k('s1.EXE'), '--addr', FONT_ADDR, '--style', 'half'],
        must='size preserved')
    run(['riotfont.py', 'halfwidth', k('s1.EXE'), k('s2.EXE'), '--glyph-only'], must='2 word(s) changed')
    run(['riotfont.py', 'renderer', k('s2.EXE'), k('s3.EXE')], must='size preserved')
    run(['slotext.py', 'apply', k('s3.EXE'), os.path.join(BUILD, 'KOUSEI.EXE')], must='11 words written')
    print('SLPS_008.29')
    run(['riotfont.py', 'namegrid', os.path.join(ORIG, 'SLPS_008.29'), k('p1.29')], must='size preserved')
    run(['riotfont.py', 'menutext', k('p1.29'), k('p2.29')], must='size preserved')
    run(['riotfont.py', 'prompttext', k('p2.29'), os.path.join(BUILD, 'SLPS_008.29')], must='size preserved')
    if main1_buffer:
        print('MAIN1.EXE')
        run(['bankext.py', 'apply', os.path.join(ORIG, 'MAIN1.EXE'), os.path.join(BUILD, 'MAIN1.EXE'),
             '--buffer', '0x%08X' % main1_buffer], must='words written')
    for f in ('KOUSEI.EXE', 'SLPS_008.29') + (('MAIN1.EXE',) if main1_buffer else ()):
        p = os.path.join(BUILD, f)
        print('  build/%-12s %9d bytes  sha256 %s' % (f, os.path.getsize(p), sha(p)))
    return verify()


def verify():
    print('verify')
    run(['riotfont.py', 'simcheck', os.path.join(BUILD, 'KOUSEI.EXE')], must='RESULT: PASS')
    run(['slotext.py', 'simulate', os.path.join(BUILD, 'KOUSEI.EXE')], must='RESULT: PASS')
    out = run(['riotfont.py', 'slpsmap', os.path.join(BUILD, 'SLPS_008.29')])
    if 'ＮＥＷ　ＧＡＭＥ' not in out:
        raise SystemExit('FAILED: build/SLPS_008.29 does not carry the English menu')
    print('  build/SLPS_008.29 carries the English menu, prompts and Latin name grid')
    if os.path.exists(os.path.join(BUILD, 'MAIN1.EXE')):
        run(['bankext.py', 'simulate', os.path.join(BUILD, 'MAIN1.EXE')], must='RESULT: PASS')
    print('ENGINE BUILD OK — not booted: see pending/slot-extension.md §5 and FLAGS §BD5')
    return True


if __name__ == '__main__':
    argv = sys.argv[1:]
    mb = None
    if '--main1-buffer' in argv:
        mb = int(argv[argv.index('--main1-buffer') + 1], 16)
        del argv[argv.index('--main1-buffer'):argv.index('--main1-buffer') + 2]
    if not argv or argv[0] not in ('build', 'verify'):
        print(__doc__); raise SystemExit(2)
    raise SystemExit(0 if (build(mb) if argv[0] == 'build' else verify()) else 1)
