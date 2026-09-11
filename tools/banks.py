"""SCRIPT.BIN bank layout — ONE table shared by riotscript.py, bankmeasure.py, assemble.py and
bankext.py (the MAIN1.EXE patch).

Retail SCRIPT.BIN: 44 banks × 0xA000 = 20 sectors each, 1,802,240 bytes, bank n at sector n*20.
MAIN1.EXE `load_bank` (0x80037B00, FLAGS §BD1) reads 20 sectors at bank*20 into a 0xA000 RAM
buffer. Four banks cannot hold their translation in 0xA000 (FLAGS §F2: 41, 40, 5, 2, and 33 is
next): the fix gives those banks more sectors, keeps every bank in order and contiguous, and
makes the loader take (start sector, count) from a per-bank table (bankext.py) instead of
computing bank*20 / 20.

Growth per tight bank, from §F2's need at 1.9× the untranslated Japanese plus what was free
(2026-09-11): bank 41 +30,534 → +16 sectors (32,768); 40 +20,924 → +11 (22,528); 5 +14,720 → +8
(16,384); 2 +12,798 → +7 (14,336); 33 +11,492 → +6 (12,288). Everything else stays at 20.

The extended layout is OPT-IN (`--layout`) until the boot test passes: dumps, verify, refresh and
the default `check` keep the retail layout.
"""

SECTOR = 2048
NBANKS = 44
RETAIL_SECTORS = 20                       # 0xA000 per bank
RETAIL_BANK = RETAIL_SECTORS * SECTOR
RETAIL_SIZE = NBANKS * RETAIL_BANK        # 1,802,240

EXTRA = {41: 16, 40: 11, 5: 8, 2: 7, 33: 6}     # extra sectors per bank (extended layout)


def count(bank, extended=True):
    """Sectors of `bank` under the layout."""
    return RETAIL_SECTORS + (EXTRA.get(bank, 0) if extended else 0)


def size(bank, extended=True):
    return count(bank, extended) * SECTOR


def start(bank, extended=True):
    """First sector of `bank` (relative to the file start)."""
    return sum(count(b, extended) for b in range(bank))


def offset(bank, extended=True):
    return start(bank, extended) * SECTOR


def total_size(extended=True):
    return sum(size(b, extended) for b in range(NBANKS))


def max_count(extended=True):
    return max(count(b, extended) for b in range(NBANKS))


def table(extended=True):
    """44 × (start sector, count) — what the MAIN1.EXE table holds."""
    return [(start(b, extended), count(b, extended)) for b in range(NBANKS)]


assert start(NBANKS - 1, False) == (NBANKS - 1) * RETAIL_SECTORS
assert total_size(False) == RETAIL_SIZE

if __name__ == '__main__':
    for b in range(NBANKS):
        if b in EXTRA:
            print('bank %2d  start %4d  count %2d  size 0x%05X  (+%d bytes)' % (b, start(b), count(b), size(b), EXTRA[b] * SECTOR))
    print('extended SCRIPT.BIN: %d bytes = %d sectors (retail %d = %d); buffer needs %d sectors = %d bytes'
          % (total_size(), total_size() // SECTOR, RETAIL_SIZE, RETAIL_SIZE // SECTOR, max_count(), max_count() * SECTOR))
