"""Battle-script slot layout — ONE table shared by riotbattle.py, assemble.py and slotext.py.

Retail HEXMAP.BIN: 46 chunks x 0x2A800 plus a 0x8000 tail = 8,040,448 bytes = 3,926 sectors.
Every map chunk's event script lives in an 8,192-byte slot at chunk+0x25000 (sector 74 of the
chunk's 85), read by KOUSEI.EXE `map_load` as `read(record, idx*85 + 0x4A, 4)` and byte-swapped
into an 8,192-byte RAM buffer (findings.md §23, pending/slot-extension.md).

Four chunks cannot hold a faithful translation in 8,192 bytes (tier A: 5, 16, 32, 43). The chunk
is completely full — sectors 0..84 are all read — and in every large map (104x78 cells) the map
data's third plane runs to chunk+0x24F18, so there is no in-chunk room either (only the three
small maps 24, 28, 43 are zero above +0x207CC; measured 2026-09-11, FLAGS §BC). The extension
therefore APPENDS one 16,384-byte slot per tier-A chunk after the retail file, and a stub in
KOUSEI.EXE (slotext.py) redirects the script read of exactly those four maps to their appended
slot with count 8. Nothing inside any chunk moves; the retail slot of a tier-A chunk stays
byte-identical to the original and is simply never read.

Layout, in chunk order:
    chunk 5  -> sector 3926 (0xF56), file 0x7AB000
    chunk 16 -> sector 3934 (0xF5E), file 0x7AF000
    chunk 32 -> sector 3942 (0xF66), file 0x7B3000
    chunk 43 -> sector 3950 (0xF6E), file 0x7B7000
    extended file size 8,105,984 bytes = 3,958 sectors

The extended layout is OPT-IN (`--extended`) everywhere until the boot test passes: dumps stay
retail, `verify`/`refresh` stay retail, and `check` on main keeps the 8,192-byte budget.
"""

SECTOR = 2048
CHUNK = 0x2A800
SECTORS_PER_CHUNK = CHUNK // SECTOR           # 85
RETAIL_SIZE = 8_040_448
RETAIL_SECTORS = RETAIL_SIZE // SECTOR        # 3926

SCRIPT_LO = 0x25000                           # retail slot, every chunk
SCRIPT_HI = 0x27000
SCRIPT_SLOT = SCRIPT_HI - SCRIPT_LO           # 8192
SCRIPT_SECTOR = SCRIPT_LO // SECTOR           # 0x4A
SCRIPT_COUNT = SCRIPT_SLOT // SECTOR          # 4

EXT_SLOT = 16384                              # bytes per appended slot
EXT_COUNT = EXT_SLOT // SECTOR                # 8 sectors
EXTENDED = (5, 16, 32, 43)                    # tier-A chunks, appended in this order

assert RETAIL_SIZE % SECTOR == 0


def ext_index(chunk):
    """0-based position of `chunk` in the appended region, or None."""
    return EXTENDED.index(chunk) if chunk in EXTENDED else None


def ext_sector(chunk):
    """First sector (relative to the file start) of the chunk's appended slot."""
    return RETAIL_SECTORS + EXT_COUNT * ext_index(chunk)


def ext_offset(chunk):
    """File offset of the chunk's appended slot."""
    return ext_sector(chunk) * SECTOR


def ext_size():
    """Size of the extended HEXMAP.BIN."""
    return RETAIL_SIZE + EXT_SLOT * len(EXTENDED)


def slot_bytes(chunk, extended):
    """Byte budget of a chunk's script under the given layout."""
    return EXT_SLOT if (extended and chunk in EXTENDED) else SCRIPT_SLOT


def stub_table():
    """(key, sector) pairs the KOUSEI.EXE stub compares `idx*85` against."""
    return [(c * SECTORS_PER_CHUNK, ext_sector(c)) for c in EXTENDED]


if __name__ == '__main__':
    for c in EXTENDED:
        print('chunk %2d  key 0x%04X  sector %d (0x%X)  file 0x%06X' %
              (c, c * SECTORS_PER_CHUNK, ext_sector(c), ext_sector(c), ext_offset(c)))
    print('extended size %d bytes = %d sectors' % (ext_size(), ext_size() // SECTOR))
