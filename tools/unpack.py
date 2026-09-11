#!/usr/bin/env python3
"""
unpack.py  --  rebuild original/ from the split archive committed on main

The disc's file tree was uploaded to main on 2026-09-11 as riotstars.zip.001, .002, .003
(store-only zip, split at 24,000,000 bytes: concatenating the parts gives the archive).
original/ stays gitignored; this script recreates it in any clone:

    python3 tools/unpack.py          # the five files below into original/
    python3 tools/unpack.py --all    # additionally the whole tree into original/disc/

Every extracted file is checked against a pinned size and sha256, measured from the upload
the day `assemble.py refresh` reproduced dumps/ byte-for-byte (FLAGS.md §BB4). A mismatch
exits non-zero and leaves the file in place for inspection: do not run refresh on it.
"""
import sys, os, io, glob, re, zipfile, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(ROOT, 'original')
PART_GLOB = os.path.join(ROOT, 'riotstars.zip.*')

# name in original/ : (member in the archive, size, sha256)
PINNED = {
    'SCRIPT.BIN':  ('riotstars/IMDATA/SCRIPT.BIN',    1802240, 'ba517b7479308027623f06702e169ee6f24ebedfd961b3b2cf52dd45be3bf80e'),
    'HEXMAP.BIN':  ('riotstars/TACTICS/HEXMAP.BIN',   8040448, '690f061b002348786861ec2afb91e6835c28e977514b93c53d9570821e7bcc1d'),
    'KOUSEI.EXE':  ('riotstars/KOUSEI.EXE',           1073152, '7ec69c54f5bcddf564e694bd6c0004aa9df8b88d0a7269ce422ab12bc0df2c4f'),
    'SLPS_008.29': ('riotstars/SLPS_008.29',           448512, '7eca4794904c28f1bf59c53e5ee6078cea65dadfcc23c5ad254c528ae3e54a41'),
    'MAIN1.EXE':   ('riotstars/MAIN1.EXE',             569344, '288dec61f123155d7481e55f883542ed6651666db3371c2aa305b3035c850076'),
}


def parts():
    ps = glob.glob(PART_GLOB)
    ps = [p for p in ps if re.fullmatch(r'riotstars\.zip\.\d{3}', os.path.basename(p))]
    if not ps:
        raise SystemExit('no riotstars.zip.NNN parts at the repo root — is this a clone of main?')
    return sorted(ps, key=lambda p: int(p.rsplit('.', 1)[1]))


def open_archive():
    ps = parts()
    buf = io.BytesIO()
    for p in ps:
        with open(p, 'rb') as f:
            buf.write(f.read())
    print('joined %d parts, %d bytes' % (len(ps), buf.tell()))
    buf.seek(0)
    try:
        z = zipfile.ZipFile(buf)
    except zipfile.BadZipFile as e:
        raise SystemExit('joined parts are not a zip archive (%s) — a part is missing or damaged' % e)
    bad = z.testzip()
    if bad is not None:
        raise SystemExit('archive CRC failure at member %s' % bad)
    return z


def main(argv):
    everything = '--all' in argv
    z = open_archive()
    os.makedirs(ORIG, exist_ok=True)
    ok = True
    for name, (member, size, sha) in PINNED.items():
        data = z.read(member)
        dst = os.path.join(ORIG, name)
        with open(dst, 'wb') as f:
            f.write(data)
        got = hashlib.sha256(data).hexdigest()
        good = (len(data) == size and got == sha)
        ok &= good
        print('  %-12s %9d bytes  sha256 %s  %s' % (name, len(data), got[:16], 'OK' if good else '!! MISMATCH'))
    if everything:
        z.extractall(os.path.join(ORIG, 'disc'))
        print('  full tree -> original/disc/riotstars/')
    if not ok:
        print('!! at least one file does not match its pin. Do NOT run refresh; look first.')
        return 1
    print('original/ rebuilt. Next: python3 tools/assemble.py refresh  (must leave dumps/ unchanged)')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
