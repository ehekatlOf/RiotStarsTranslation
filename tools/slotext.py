#!/usr/bin/env python3
"""
slotext.py  --  KOUSEI.EXE patch: 16 KB script slots for the tier-A battle chunks

    python3 tools/slotext.py apply    KOUSEI.EXE OUT [--revert]   # verify every word, then write
    python3 tools/slotext.py simulate KOUSEI.EXE                  # R3000 simulation of the patched paths
    python3 tools/slotext.py show                                 # the stub, assembled and disassembled

What it changes (pending/slot-extension.md §3, revised 2026-09-11 — FLAGS §BC):

  1. A stub in the execution-proven 520-byte zero run at 0x800F3ECC. `map_load` calls it instead
     of `read()` for the script sector. For the four chunks in slots.EXTENDED it reads 8 sectors
     from the chunk's APPENDED slot (slots.py); for every other map it zeroes the second 8 KB of
     the staging buffer and reads the retail 4 sectors exactly as before. The zeroing matters:
     the byte-swap below now copies 16 KB, and the entry scanner walks all of it — stale staging
     data there would register phantom message entries.
  2. Call site 0x80063910: `jal stub` with `addu a1,s2,zero` in the delay slot (a1 = idx*85).
  3. The script RAM buffer moves 0x80154F40 -> 0x80180000 (16 KB; the retail buffer has 12 bytes
     of clearance, findings §23.2) and both loop bounds go 0x1000 -> 0x2000 halfwords.

Every original word is verified before anything is written (riotfont._apply_set); the stub
region must be all zero. --revert restores every word and zeroes the stub.
"""
import sys, os, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from riotfont import load_exe, psx_to_file, _apply_set, R3000, HDR
import slots

STUB_PSX   = 0x800F3ECC          # findings Appendix B: safe, execution-proven (520 B)
STUB_ROOM  = 520
CALL_SITE  = 0x80063910          # addiu a1,s2,0x4A ; jal read ; ori a2,zero,4
READ_FN    = 0x80064C48          # read(record, sector, count)
SWAP_FN    = 0x8006551C          # byte-swap staging -> script buffer, then scan for entries
STAGING    = 0x801C0DDC
OLD_BUF    = 0x80154F40
NEW_BUF    = 0x80180000
TABLE      = 0x801DC784          # entry table: [0] = buffer base, [k] = after k-th {FFFF}
CALL_RET   = CALL_SITE + 0xC     # 0x8006391C: jal byte-swap, unchanged

# ---------------------------------------------------------------- a very small assembler
R = dict(zero=0, at=1, v0=2, v1=3, a0=4, a1=5, a2=6, a3=7, t0=8, t1=9, t2=10, sp=29, ra=31)


def _i(op, rs, rt, imm):
    return (op << 26) | (R[rs] << 21) | (R[rt] << 16) | (imm & 0xFFFF)


def assemble(prog, base):
    """prog: list of (mnemonic, args...) or ('label', name). Two passes; returns bytes."""
    labels, pc = {}, base
    for ins in prog:
        if ins[0] == 'label':
            labels[ins[1]] = pc
        else:
            pc += 4
    out, pc = [], base
    for ins in prog:
        m = ins[0]
        if m == 'label':
            continue
        a = ins[1:]
        if m == 'nop':     w = 0
        elif m == 'addiu': w = _i(0x09, a[1], a[0], a[2])
        elif m == 'ori':   w = _i(0x0D, a[1], a[0], a[2])
        elif m == 'lui':   w = (0x0F << 26) | (R[a[0]] << 16) | (a[1] & 0xFFFF)
        elif m == 'sw':    w = _i(0x2B, a[2], a[0], a[1])
        elif m == 'lw':    w = _i(0x23, a[2], a[0], a[1])
        elif m in ('beq', 'bne'):
            off = (labels[a[2]] - (pc + 4)) >> 2
            w = _i(0x04 if m == 'beq' else 0x05, a[0], a[1], off)
        elif m in ('j', 'jal'):
            t = labels[a[0]] if isinstance(a[0], str) else a[0]
            w = ((0x02 if m == 'j' else 0x03) << 26) | ((t & 0x0FFFFFFF) >> 2)
        elif m == 'jr':    w = (R[a[0]] << 21) | 0x08
        elif m == 'addu':  w = (R[a[1]] << 21) | (R[a[2]] << 16) | (R[a[0]] << 11) | 0x21
        else: raise ValueError(m)
        out.append(w); pc += 4
    return b''.join(struct.pack('<I', w) for w in out)


def stub_program():
    p = [('addiu', 'sp', 'sp', -8),
         ('sw', 'ra', 0, 'sp')]
    for key, sector in slots.stub_table():
        p += [('ori', 'v0', 'zero', key),
              ('beq', 'a1', 'v0', 'hit'),
              ('ori', 'v1', 'zero', sector)]          # delay slot: candidate sector
    lo = STAGING + slots.SCRIPT_SLOT                    # second 8 KB of the staging buffer
    p += [('label', 'normal'),
          ('lui', 'v0', lo >> 16),
          ('addiu', 'v0', 'v0', lo & 0xFFFF),
          ('addiu', 'v1', 'v0', slots.SCRIPT_SLOT),
          ('label', 'zl'),
          ('sw', 'zero', 0, 'v0'),
          ('addiu', 'v0', 'v0', 4),
          ('bne', 'v0', 'v1', 'zl'),
          ('nop',),
          ('addiu', 'a1', 'a1', slots.SCRIPT_SECTOR),
          ('j', 'call'),
          ('ori', 'a2', 'zero', slots.SCRIPT_COUNT),   # delay slot
          ('label', 'hit'),
          ('addu', 'a1', 'v1', 'zero'),
          ('ori', 'a2', 'zero', slots.EXT_COUNT),
          ('label', 'call'),
          ('jal', READ_FN),
          ('nop',),
          ('lw', 'ra', 0, 'sp'),
          ('nop',),                                    # load delay slot (findings §14.8 #1)
          ('addiu', 'sp', 'sp', 8),
          ('jr', 'ra'),
          ('nop',)]
    assert (lo & 0xFFFF) < 0x8000, 'staging low half must not sign-extend'
    return p


STUB = assemble(stub_program(), STUB_PSX)
assert len(STUB) <= STUB_ROOM

JAL_STUB = 0x0C000000 | ((STUB_PSX & 0x0FFFFFFF) >> 2)
hi, lo = NEW_BUF >> 16, NEW_BUF & 0xFFFF

WORDS = [
    # call site (plan §3b)
    (CALL_SITE + 0, 0x2645004A, JAL_STUB,   'jal stub (was addiu a1,s2,0x4A)'),
    (CALL_SITE + 4, 0x0C019312, 0x02402821, 'addu a1,s2,zero in the delay slot (was jal read)'),
    (CALL_SITE + 8, 0x34060004, 0x00000000, 'nop (was ori a2,zero,4)'),
    # RAM buffer relocation and length (plan §3c)
    (0x80065528, 0x3C088015, 0x3C080000 | hi, 'lui t0,hi(buffer)'),
    (0x8006552C, 0x25084F40, 0x25080000 | lo, 'addiu t0,lo(buffer)'),
    (0x80065530, 0x3C078015, 0x3C070000 | hi, 'lui a3,hi(buffer)'),
    (0x80065534, 0x24E74F41, 0x24E70000 | (lo + 1), 'addiu a3,lo(buffer)+1'),
    (0x80065560, 0x28C21000, 0x28C22000, 'slti v0,a2,0x2000 (byte-swap bound)'),
    (0x8006556C, 0x3C028015, 0x3C020000 | hi, 'lui v0,hi(buffer)'),
    (0x80065570, 0x24424F40, 0x24420000 | lo, 'addiu v0,lo(buffer)'),
    (0x800655D8, 0x28C21000, 0x28C22000, 'slti v0,a2,0x2000 (entry-scan bound)'),
]
assert lo + 1 < 0x8000 and lo < 0x8000


def cmd_show():
    print('stub at 0x%08X, %d bytes (%d instructions), room %d' % (STUB_PSX, len(STUB), len(STUB) // 4, STUB_ROOM))
    try:
        from capstone import Cs, CS_ARCH_MIPS, CS_MODE_MIPS32, CS_MODE_LITTLE_ENDIAN
        md = Cs(CS_ARCH_MIPS, CS_MODE_MIPS32 | CS_MODE_LITTLE_ENDIAN)
        for i in md.disasm(STUB, STUB_PSX):
            print('  %08X  %08X  %-6s %s' % (i.address, struct.unpack_from('<I', STUB, i.address - STUB_PSX)[0], i.mnemonic, i.op_str))
    except ImportError:
        for k in range(0, len(STUB), 4):
            print('  %08X  %08X' % (STUB_PSX + k, struct.unpack_from('<I', STUB, k)[0]))
    print('words:')
    for psx, was, now, why in WORDS:
        print('  %08X  %08X -> %08X  %s' % (psx, was, now, why))


def cmd_apply(path, out_path, revert=False):
    data, t_addr, t_size, _ = load_exe(path)
    off = psx_to_file(STUB_PSX, t_addr)
    region = bytes(data[off:off + STUB_ROOM])
    if not revert:
        if any(region):
            if region[:len(STUB)] == STUB and all(w == 0 for w in region[len(STUB):]):
                print('stub already present')
            else:
                raise SystemExit('ABORT: stub region 0x%08X is not zero — another patch lives there. '
                                 'Nothing written.' % STUB_PSX)
    else:
        if region[:len(STUB)] != STUB:
            raise SystemExit('ABORT: stub region does not hold this stub. Nothing written.')
    plan, already = _apply_set(data, t_addr, WORDS, revert=revert)
    if revert:
        data[off:off + len(STUB)] = b'\x00' * len(STUB)
    else:
        data[off:off + len(STUB)] = STUB
    open(out_path, 'wb').write(bytes(data))
    print('%s: %d words %s, %d already, stub %s at 0x%08X (%d B); size preserved (%d bytes) -> %s'
          % ('REVERT' if revert else 'slotext', len(plan), 'restored' if revert else 'written',
             already, 'zeroed' if revert else 'written', STUB_PSX, len(STUB), len(data), out_path))


def _cpu(path):
    data, t_addr, t_size, _ = load_exe(path)
    return R3000(bytes(data), t_addr, t_size)


def sim_callsite(path, idx, patched):
    """Run map_load's script read for map `idx` from the (patched) call site to CALL_RET."""
    cpu = _cpu(path)
    sp0, ra0, rec = 0x801FFF00, 0xDEAD0000, 0x800F4660
    cpu.r[18] = idx * slots.SECTORS_PER_CHUNK      # s2
    cpu.r[4] = rec; cpu.r[29] = sp0; cpu.r[31] = ra0
    cpu.intercept = {READ_FN}
    cpu.run(CALL_SITE, {CALL_RET}, max_steps=50000)      # retail: addiu a1 ; jal ; ori a2
    return cpu, sp0


def sim_swap(path, nmsg=40, msglen=300):
    """Run the byte-swap + entry scan on a synthetic slot of nmsg messages, msglen bytes each."""
    cpu = _cpu(path)
    msg = (b'\x82\xa0' * ((msglen - 8) // 2)) + b'\xfc\xa6' + b'\x00\x00\x00\x00' + b'\xff\xff'
    slot = (msg * nmsg)[:slots.EXT_SLOT]
    slot += b'\x00' * (slots.EXT_SLOT - len(slot))
    for i, v in enumerate(slot):
        cpu.wb(STAGING + i, v)
    cpu.r[29] = 0x801FFF00; cpu.r[31] = 0xDEAD0000
    cpu.run(SWAP_FN, {0xDEAD0000}, max_steps=600000)
    base = cpu.rw(TABLE)
    entries = [cpu.rw(TABLE + 4 * k) for k in range(50)]
    n = 1
    while n < 50 and entries[n] != 0:
        n += 1
    # what the swap should have produced
    swapped = bytes(b for i in range(0, len(slot), 2) for b in (slot[i + 1], slot[i]))
    copied = bytes(cpu._rb(base + i) for i in range(slots.EXT_SLOT))
    return base, entries[:n], copied, swapped, len(msg)


def cmd_simulate(path):
    data, t_addr, _, _ = load_exe(path)
    patched = struct.unpack_from('<I', data, psx_to_file(CALL_SITE, t_addr))[0] == JAL_STUB
    print('%s: %s' % (path, 'PATCHED' if patched else 'retail'))
    ok = True
    lo, hi = STAGING + slots.SCRIPT_SLOT, STAGING + 2 * slots.SCRIPT_SLOT
    for idx in range(46):
        cpu, sp0 = sim_callsite(path, idx, patched)
        ext = patched and idx in slots.EXTENDED
        want = (READ_FN, 0x800F4660,
                slots.ext_sector(idx) if ext else idx * slots.SECTORS_PER_CHUNK + slots.SCRIPT_SECTOR,
                slots.EXT_COUNT if ext else slots.SCRIPT_COUNT)
        got = cpu.calls[0][:4] if cpu.calls else None
        zeroed = sorted(a for a, v, n in cpu.writes if lo <= a < hi)
        z_ok = (not patched) or (ext and not zeroed) or \
               (not ext and len(zeroed) == slots.SCRIPT_SLOT // 4 and zeroed[0] == lo and zeroed[-1] == hi - 4
                and all(v == 0 for a, v, n in cpu.writes if lo <= a < hi))
        stray = [a for a, v, n in cpu.writes if not (lo <= a < hi) and not (sp0 - 8 <= a < sp0)]
        good = (got == want and cpu.r[29] == sp0 and not cpu.hazards and z_ok and not stray
                and len(cpu.calls) == 1)
        ok &= good
        if idx in (0, 5, 16, 32, 42, 43, 44, 45) or not good:
            print('  map %2d  read(sector %4d, count %d)  %s  sp %s  hazards %d  zeroed %5d words  stray %d  %s'
                  % (idx, got[2] if got else -1, got[3] if got else -1,
                     'as expected' if got == want else 'WRONG (want sector %d count %d)' % (want[2], want[3]),
                     'restored' if cpu.r[29] == sp0 else 'BROKEN', len(cpu.hazards), len(zeroed), len(stray),
                     'OK' if good else '!! FAIL'))
    base, entries, copied, swapped, mlen = sim_swap(path)
    reach = slots.EXT_SLOT if patched else slots.SCRIPT_SLOT
    want_base = NEW_BUF if patched else OLD_BUF
    n_want = min(49, 40, reach // mlen)    # messages (of the 40 synthetic) whose {FFFF} lies inside the copied bytes
    copy_ok = copied[:reach] == swapped[:reach]
    ptr_ok = all(base < e <= base + reach for e in entries[1:])
    print('  byte-swap: base 0x%08X (%s), copied %d bytes %s, entries %d (%s, want %d), all inside buffer: %s'
          % (base, 'as expected' if base == want_base else 'WRONG', reach,
             'identical to swapped source' if copy_ok else 'MISMATCH', len(entries) - 1,
             'ok' if len(entries) - 1 == n_want else 'WRONG', n_want, ptr_ok))
    ok &= (base == want_base and copy_ok and ptr_ok and len(entries) - 1 == n_want)
    print('RESULT: %s' % ('PASS' if ok else 'FAIL'))
    return ok


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    cmd = argv[1]
    if cmd == 'show':
        cmd_show(); return 0
    if cmd == 'apply':
        cmd_apply(argv[2], argv[3], revert='--revert' in argv); return 0
    if cmd == 'simulate':
        return 0 if cmd_simulate(argv[2]) else 1
    print('unknown command', cmd); return 2


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
