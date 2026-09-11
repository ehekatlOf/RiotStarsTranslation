#!/usr/bin/env python3
"""
bankext.py  --  MAIN1.EXE patch: per-bank SCRIPT.BIN layout (tools/banks.py) and a bigger bank buffer

    python3 tools/bankext.py apply    MAIN1.EXE OUT --buffer 0xADDR [--revert]
    python3 tools/bankext.py simulate MAIN1.EXE [--buffer 0xADDR]
    python3 tools/bankext.py show     [--buffer 0xADDR]

What it changes (FLAGS §BD, findings-style addresses, retail MAIN1.EXE t_addr 0x80010000):

  1. The image grows by one 0x800 sector (t_size 0x8A800 -> 0x8B000). The new page at 0x8009A800
     holds the 44-entry table of (u16 start sector, u16 count) from banks.py. No lui/addiu or
     gp-relative reference lands in 0x8009A800..0x8009C000 (measured 2026-09-11), and the crt0
     zero-fill start moves from 0x8009A20C to 0x8009B000 so the page survives boot. Every byte the
     crt0 no longer clears is inside the loaded image and is zero in the file, so nothing changes
     for the variables there, on first boot or on re-entry from KOUSEI/CASINO/KEIBA.
  2. `load_bank` (0x80037B00): the 17-word tail from 0x80037B60 is rewritten in place — table
     lookup instead of bank*20 / 20, the count parked at sp+0x14 across `advance` and reloaded
     four instructions before `read`, the loc pointer built as gp+0x254 (one word, frees the
     slot), the read destination = --buffer. Same number of words, no stub, no load-delay hazard.
  3. The bank buffer moves from 0x800D8068 (0xA000, zero clearance: the event record table starts
     at 0x800E2068) to --buffer, 36 sectors = 73,728 bytes: the loader's dest, the CD record's
     dest word at 0x8007F7CC, and the eight lui/addiu (or lui/sh) pairs that build the base or
     base+0x384 (FLAGS §BD2).

--buffer has NO default. The static candidates (0x800A8000, 0x800F1000, 0x80170020, 0x801C0040)
are exactly where pointer-addressed load buffers would live; a DuckStation savestate from a town
scene must show the region unwritten (`riotfont.py liveness`) before a build goes to the human.
Every original word is verified before anything is written; --revert restores the retail file
byte for byte (including the size).
"""
import sys, os, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from riotfont import load_exe, psx_to_file, _apply_set, R3000, HDR
import banks

T_ADDR      = 0x80010000
OLD_TSIZE   = 0x8A800
NEW_TSIZE   = 0x8B000
TABLE       = 0x8009A800                 # in the appended page
LOAD_BANK   = 0x80037B00
TAIL        = 0x80037B60                 # first rewritten word
ADVANCE     = 0x80012AC0
READ        = 0x80012988
LOC         = 0x8009A334                 # CdlLOC scratch (gp+0x254)
REC_LOC     = 0x8007F7D0                 # SCRIPT.BIN CD record: CdlLOC of the file start
REC_DEST    = 0x8007F7CC                 # ... and its destination pointer (data word)
OLD_BUF     = 0x800D8068
BODY        = 0x384
GP          = 0x8009A0E0
CRT0_WORD   = 0x800456B4                 # addiu v0,v0,lo(bss start) in the zero-fill setup
CLEAR_OLD   = 0x8009A20C
CLEAR_NEW   = 0x8009B000
BUF_SECTORS = banks.max_count()          # 36


def split(addr):
    """(hi, lo) for lui + sign-extended 16-bit immediate."""
    lo = addr & 0xFFFF
    hi = (addr >> 16) + (1 if lo & 0x8000 else 0)
    return hi, lo


def enc_lui(rt, addr):      return (0x0F << 26) | (rt << 16) | split(addr)[0]
def enc_addiu(rt, rs, imm): return (0x09 << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)
def enc_lhu(rt, rs, imm):   return (0x25 << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)
def enc_lw(rt, rs, imm):    return (0x23 << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)
def enc_sw(rt, rs, imm):    return (0x2B << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)
def enc_sh(rt, rs, imm):    return (0x29 << 26) | (rs << 21) | (rt << 16) | (imm & 0xFFFF)
def enc_sll(rd, rt, sa):    return (rt << 16) | (rd << 11) | (sa << 6)
def enc_addu(rd, rs, rt):   return (rs << 21) | (rt << 16) | (rd << 11) | 0x21
def enc_jal(t):             return 0x0C000000 | ((t & 0x0FFFFFFF) >> 2)
V0, V1, A0, A1, A2, SP, RA, AT, S4, GP_REG = 2, 3, 4, 5, 6, 29, 31, 1, 20, 28
assert GP + 0x254 == LOC

RETAIL_TAIL = [0x10A00004, 0x00001021, 0x00051080, 0x00451021, 0x00021080, 0x0C004AB0, 0x3044FFFF,
               0x3C04800A, 0x2484A334, 0x3C05800E, 0x24A58068, 0x0C004A62, 0x34060014,
               0x8FBF0010, 0x27BD0018, 0x03E00008, 0x00000000]


def new_tail(buf):
    thi, tlo = split(TABLE)
    tlo_s = tlo - 0x10000 if tlo & 0x8000 else tlo
    bhi, blo = split(buf)
    return [enc_lui(V0, TABLE),                 # lui   v0,hi(table)
            enc_sll(V1, A1, 2),                 # sll   v1,a1,2          bank*4
            enc_addu(V0, V0, V1),               # addu  v0,v0,v1
            enc_lhu(A0, V0, tlo_s),             # lhu   a0,lo(table)(v0)   start sector
            enc_lhu(V1, V0, tlo_s + 2),         # lhu   v1,lo+2(v0)        count
            enc_jal(ADVANCE),                   # jal   advance
            enc_sw(V1, SP, 0x14),               #   sw  v1,0x14(sp)        (delay slot)
            enc_lw(A2, SP, 0x14),               # lw    a2,0x14(sp)        count (4 instructions before the call)
            enc_addiu(A0, GP_REG, 0x254),       # addiu a0,gp,0x254        loc scratch (retail used lui/addiu)
            enc_lui(A1, buf), enc_addiu(A1, A1, blo),   # a1 = buffer
            enc_jal(READ),                      # jal   read
            0x00000000,                         #   nop                    (delay slot)
            0x8FBF0010, 0x27BD0018, 0x03E00008, 0x00000000]   # epilogue (retail words)


# the buffer references outside the loader: (lui psx, lo-carrying psx, register, extra, lo opcode)
REFS = [(0x800133CC, 0x800133D0, V0, 0,    'addiu'),
        (0x80031C20, 0x80031C24, V0, 0,    'addiu'),
        (0x80031C04, 0x80031C08, V0, BODY, 'addiu'),
        (0x80033FF0, 0x80033FF4, V0, BODY, 'addiu'),
        (0x80031CCC, 0x80031CD0, S4, 0,    'addiu'),
        (0x8003BF60, 0x8003BF64, S4, 0,    'addiu'),
        (0x8003BEF0, 0x8003BEF8, AT, 0,    'sh')]


def word_set(buf):
    """(psx, was, now, why) for everything except the tail and the table page."""
    ws = []
    for lui_psx, lo_psx, reg, extra, kind in REFS:
        old_addr, new_addr = OLD_BUF + extra, buf + extra
        ohi, olo = split(old_addr); nhi, nlo = split(new_addr)
        ws.append((lui_psx, (0x0F << 26) | (reg << 16) | ohi, (0x0F << 26) | (reg << 16) | nhi,
                   'lui base%s hi @%08X' % ('+0x384' if extra else '', lui_psx)))
        if kind == 'addiu':
            ws.append((lo_psx, enc_addiu(reg, reg, olo), enc_addiu(reg, reg, nlo), 'addiu lo'))
        else:   # sh v0, lo(at)
            ws.append((lo_psx, enc_sh(V0, AT, olo), enc_sh(V0, AT, nlo), 'sh v0,lo(at)'))
    ws.append((REC_DEST, OLD_BUF, buf, 'CD record 7 dest pointer (data)'))
    ws.append((CRT0_WORD, enc_addiu(V0, V0, split(CLEAR_OLD)[1]), enc_addiu(V0, V0, split(CLEAR_NEW)[1]),
               'crt0 zero-fill start 0x%08X -> 0x%08X' % (CLEAR_OLD, CLEAR_NEW)))
    for i, (old, new) in enumerate(zip(RETAIL_TAIL, new_tail(buf))):
        ws.append((TAIL + 4 * i, old, new, 'load_bank tail +%d' % (4 * i)))
    return ws


def table_bytes():
    return b''.join(struct.pack('<HH', s, c) for s, c in banks.table(True))


def parse_buffer(argv):
    if '--buffer' in argv:
        v = int(argv[argv.index('--buffer') + 1], 16)
        if v & 0xF or not (0x80000000 <= v < 0x80200000):
            raise SystemExit('--buffer must be a 16-byte-aligned PSX RAM address')
        return v
    return None


def cmd_show(buf):
    print('table: 44 x (start, count) at 0x%08X, %d bytes; buffer 0x%s, %d sectors = %d bytes'
          % (TABLE, len(table_bytes()), '%08X' % buf if buf else 'UNSET', BUF_SECTORS, BUF_SECTORS * 2048))
    for psx, was, now, why in word_set(buf or OLD_BUF):
        print('  %08X  %08X -> %08X  %s' % (psx, was, now, why))


def cmd_apply(path, out_path, buf, revert=False):
    data, t_addr, t_size, _ = load_exe(path)
    if t_addr != T_ADDR:
        raise SystemExit('not MAIN1.EXE (t_addr 0x%08X)' % t_addr)
    if not revert:
        if buf is None:
            raise SystemExit('--buffer is required: no default until a town savestate proves the region (FLAGS §BD3)')
        if buf + BUF_SECTORS * 2048 > 0x80200000 or buf < t_addr + NEW_TSIZE:
            raise SystemExit('--buffer must lie in BSS above the extended image and below the end of RAM')
        if t_size != OLD_TSIZE or len(data) != HDR + OLD_TSIZE:
            raise SystemExit('expected the retail image (t_size 0x%X, %d bytes)' % (OLD_TSIZE, HDR + OLD_TSIZE))
        plan, already = _apply_set(data, t_addr, word_set(buf))
        data += b'\x00' * (NEW_TSIZE - OLD_TSIZE)
        struct.pack_into('<I', data, 0x1C, NEW_TSIZE)
        off = psx_to_file(TABLE, t_addr)
        data[off:off + len(table_bytes())] = table_bytes()
    else:
        if t_size != NEW_TSIZE:
            raise SystemExit('not a bankext-patched image (t_size 0x%X)' % t_size)
        # recover the buffer address from the loader's a1 words
        w_hi = struct.unpack_from('<I', data, psx_to_file(TAIL + 4 * 9, t_addr))[0]
        w_lo = struct.unpack_from('<I', data, psx_to_file(TAIL + 4 * 10, t_addr))[0]
        lo = w_lo & 0xFFFF; lo = lo - 0x10000 if lo & 0x8000 else lo
        buf = ((w_hi & 0xFFFF) << 16) + lo
        plan, already = _apply_set(data, t_addr, word_set(buf), revert=True)
        off = psx_to_file(TABLE, t_addr)
        if bytes(data[off:off + len(table_bytes())]) != table_bytes():
            raise SystemExit('ABORT: the table page does not hold this layout; nothing written')
        del data[HDR + OLD_TSIZE:]
        struct.pack_into('<I', data, 0x1C, OLD_TSIZE)
    open(out_path, 'wb').write(bytes(data))
    print('%s: %d words %s, %d already; t_size 0x%X; buffer 0x%08X; %d bytes -> %s'
          % ('REVERT' if revert else 'bankext', len(plan), 'restored' if revert else 'written', already,
             struct.unpack_from('<I', data, 0x1C)[0], buf, len(data), out_path))


def sim_bank(path, bank):
    data, t_addr, t_size, _ = load_exe(path)
    cpu = R3000(bytes(data), t_addr, t_size)
    sp0, ra0 = 0x801FFF00, 0xDEAD0000
    cpu.r[4] = bank; cpu.r[28] = GP; cpu.r[29] = sp0; cpu.r[31] = ra0
    cpu.store(GP + 0x2A0, 0xFFFF, 2)                        # current bank != bank
    for i, v in enumerate((0x02, 0x30, 0x10, 0x00)):        # a plausible file-start CdlLOC in the record
        cpu.wb(REC_LOC + i, v)
    cpu.intercept = {ADVANCE, READ}
    cpu.run(LOAD_BANK, {ra0}, max_steps=20000)
    loc = [cpu._rb(LOC + i) for i in range(4)]
    return cpu, sp0, loc


def cmd_simulate(path, buf):
    data, t_addr, t_size, _ = load_exe(path)
    patched = t_size == NEW_TSIZE
    if patched and buf is None:
        w_hi = struct.unpack_from('<I', data, psx_to_file(TAIL + 36, t_addr))[0]
        w_lo = struct.unpack_from('<I', data, psx_to_file(TAIL + 40, t_addr))[0]
        lo = w_lo & 0xFFFF; lo = lo - 0x10000 if lo & 0x8000 else lo
        buf = ((w_hi & 0xFFFF) << 16) + lo
    print('%s: %s%s' % (path, 'PATCHED' if patched else 'retail', ', buffer 0x%08X' % buf if patched else ''))
    ok = True
    for bank in range(banks.NBANKS):
        cpu, sp0, loc = sim_bank(path, bank)
        want = [(ADVANCE, banks.start(bank, patched)),
                (READ, LOC, buf if patched else OLD_BUF, banks.count(bank, patched))]
        got = [(c[0], c[1]) if c[0] == ADVANCE else (c[0], c[1], c[2], c[3]) for c in cpu.calls]
        cur = cpu.rh(GP + 0x2A0)
        good = (got == want and cur == bank and cpu.r[29] == sp0 and not cpu.hazards
                and loc == [0x02, 0x30, 0x10, 0x00])
        ok &= good
        if bank in (0, 2, 5, 33, 40, 41, 43) or not good:
            print('  bank %2d  advance(%4d)  read(loc, 0x%08X, %2d)  current=%d  sp %s  hazards %d  loc copied %s  %s'
                  % (bank, got[0][1] if got else -1, got[1][2] if len(got) > 1 else 0, got[1][3] if len(got) > 1 else -1,
                     cur, 'restored' if cpu.r[29] == sp0 else 'BROKEN', len(cpu.hazards),
                     loc == [0x02, 0x30, 0x10, 0x00], 'OK' if good else '!! FAIL (want %s)' % (want,)))
    if patched:
        # crt0 zero-fill: first stores must start at CLEAR_NEW, and the table page must be intact
        cpu = R3000(bytes(data), t_addr, t_size)
        cpu.r[29] = 0x801FFF00
        try:
            cpu.run(0x800456B0, {0x800456D4}, max_steps=200)  # a few iterations are enough for the start
        except SystemExit:
            pass                                              # step limit inside the zero-fill loop, expected
        first = min(a for a, v, n in cpu.writes)
        tb = bytes(cpu._rb(TABLE + i) for i in range(len(table_bytes())))
        print('  crt0 zero-fill starts at 0x%08X (want 0x%08X); table page readable from the image: %s'
              % (first, CLEAR_NEW, tb == table_bytes()))
        ok &= (first == CLEAR_NEW and tb == table_bytes())
    print('RESULT: %s' % ('PASS' if ok else 'FAIL'))
    return ok


def main(argv):
    buf = parse_buffer(argv)
    args = [a for a in argv if a not in ('--revert',) and not a.startswith('--buffer')]
    if buf is not None:
        args = [a for a in args if a != '0x%X' % buf and a != argv[argv.index('--buffer') + 1]]
    if len(args) < 2:
        print(__doc__); return 2
    cmd = args[1]
    if cmd == 'show':
        cmd_show(buf); return 0
    if cmd == 'apply':
        cmd_apply(args[2], args[3], buf, revert='--revert' in argv); return 0
    if cmd == 'simulate':
        return 0 if cmd_simulate(args[2], buf) else 1
    print('unknown command', cmd); return 2


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
