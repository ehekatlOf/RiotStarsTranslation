# Extending the tier-A script slots to 16,384 bytes — appended slots (revised 2026-09-11)

Traced in `KOUSEI.EXE` (1,073,152 bytes, `PS-X EXE`, `t_addr 0x80010000`, `t_size 0x105800`,
`pc0 0x800BD4AC`). File offset = `addr - 0x80010000 + 0x800`. Retail `TACTICS/HEXMAP.BIN` is
8,040,448 bytes = 46 × 0x2A800 + 0x8000 = 3,926 sectors.

**Status: built and simulated, NOT yet booted.** `tools/slotext.py` applies it, `tools/slots.py`
is the one table the EXE stub and the file tools share, `riotbattle.py`/`assemble.py --extended`
build the file. The retail layout stays the default everywhere until the boot test in §5 passes.

## 1. How a map chunk is actually loaded

`map_load(a0 = map index)` at **`0x8006365C`**. The index becomes a sector base at
`0x80063680`–`0x8006368C`: `v0 = idx*5`, `v1 = v0<<4`, `s2 = v0+v1` → **`s2 = idx * 85`**.
85 sectors × 2,048 = `0x2A800`, the chunk stride.

Every read goes through `read(record, sector, count)` at **`0x80064C48`**: it adds `sector` to the
file's start position (BCD minute/second/frame at record+0x104, converted with carries at
`0x80064D48`), `CdlSetloc`s it and `CdRead`s `count` sectors to the pointer at record+0x100. There
is no size check against the file: any sector after the file start is readable, which is what the
appended slots rely on (the rebuilt disc must store HEXMAP.BIN contiguously — every ISO tool does).

| Call site | Sector | Count | Chunk range | Consumer |
|---|---|---|---|---|
| `0x800636EC` | `s2+0x00` | 0x11 | `0x00000..0x08800` | TIM → VRAM |
| `0x8006375C` | `s2+0x11` | 0x11 | `0x08800..0x11000` | TIM → VRAM |
| `0x800637C8` | `s2+0x22` | 0x11 | `0x11000..0x19800` | TIM → VRAM |
| `0x80063834` | `s2+0x33` | 0x17 | `0x19800..0x25000` | map data, below |
| **`0x80063914`** | **`s2+0x4A`** | **4** | **`0x25000..0x27000`** | **script** |
| `0x80063978` | `s2+0x4E` | 4 | `0x27000..0x29000` | unit / deployment |
| `0x800639CC` | `s2+0x52` | 3 | `0x29000..0x2A800` | CLUT loop → `0x80191858` |

### Why the slot cannot grow inside the chunk — measured on the retail file (FLAGS §BC1)

The earlier draft of this document put a 16 KB slot at `chunk+0x23000`, on the reading that the
fourth read's consumers stop at `0x22F68`. The file says otherwise. The map data at `+0x1F000` is a
header (`w`, `h` at +4/+5) followed by **three planes**: two bytes per cell (the copy at
`0x8006389C`, `w*h/2` words) and then **one byte per cell**, which the copy does not take:

| map size | chunks | plane 2 ends | plane 3 ends | last non-zero byte below the slot |
|---|---|---|---|---|
| 104 × 78 | every chunk but three | `0x22F68` | **`0x24F18`** | `0x24F18` |
| 52 × 39 | 24, 28, 43 | `0x1FFE0` | `0x207CC` | `0x207CC` |

So `0x23000..0x25000` holds the third plane in every large map, chunks 5, 16 and 32 included.
Whether the engine reads that plane in place from the staging buffer was not settled and does not
need to be: the unit table is identical in extent in all 44 chunks (last byte `0x28E78`), the CLUT
region runs to `0x2A708`, and the three TIM slots have 1,504 dead bytes each, non-contiguous. There
is no in-chunk room in a large map. The slots are appended instead, and nothing inside any chunk
moves.

## 2. The RAM buffer is the real constraint — 8,192 bytes, hard

`0x8006551C` runs immediately after the script read:

```
8006551C  a1 = 0x801C0DDC              ; staging buffer
80065528  t0 = 0x80154F40              ; destination
80065530  a3 = 0x80154F41
80065538  loop: dst[i*2]=src[1], dst[i*2+1]=src[0]   ; byte-swap to RAM order
80065560  slti v0,a2,0x1000            ; 4,096 halfwords = 8,192 bytes
80065578  sw v0, 0x801DC784            ; table[0] = script base
8006559C  loop: scan for 0xFFFF (skip 0xFCA6 +6), table[k] = pointer after the k-th
80065598  a3 = 0x32                    ; 50 entry slots
800655D8  slti v0,a2,0x1000
```

`0x80154F40` is BSS. **The next code-referenced address above it is `0x80156F4C` — 12 bytes past
the end of the 8,192-byte buffer.** Reading 16 KB into it corrupts a variable with 12 references,
silently. Relocation target: **`0x80180000`**, inside the BSS region `findings.md` §16.3 validated
as unwritten across savestates from three scenes, 32 KB clear of the relocated char buffer at
`0x80178000`.

**The scanner does not stop at zeros.** It walks all `0x1000` (now `0x2000`) halfwords and records
every `0xFFFF`. With the copy widened to 16 KB, a normal map would copy 8 KB of stale staging data
behind its script and could register phantom entries. The stub therefore zeroes the staging
buffer's second 8 KB before every retail-slot read, so the copied tail is zero and the entry table
is exactly what the retail code produced.

## 3. The patch set (`tools/slotext.py apply`)

### 3a. Layout (`tools/slots.py`)

| chunk | key (`idx*85`) | appended slot sector | file offset |
|---|---|---|---|
| 5 | `0x01A9` | 3926 (`0xF56`) | `0x7AB000` |
| 16 | `0x0550` | 3934 (`0xF5E`) | `0x7AF000` |
| 32 | `0x0AA0` | 3942 (`0xF66`) | `0x7B3000` |
| 43 | `0x0E47` | 3950 (`0xF6E`) | `0x7B7000` |

Extended file: 8,105,984 bytes = 3,958 sectors. The retail slot of each of the four chunks is left
byte-identical and is never read.

### 3b. Stub — 132 bytes at `0x800F3ECC` (file `0x0E46CC`), the execution-proven 520-byte run

```
800F3ECC  addiu sp,sp,-8
800F3ED0  sw    ra,0(sp)
800F3ED4  ori   v0,zero,0x1A9      ; chunk 5
800F3ED8  beq   a1,v0,hit
800F3EDC  ori   v1,zero,0xF56      ;   delay slot: its slot sector
          ... same three words for 0x550/0xF5E, 0xAA0/0xF66, 0xE47/0xF6E ...
800F3F04  lui   v0,0x801C          ; normal map: zero staging+0x2000..+0x4000
800F3F08  addiu v0,v0,0x2DDC
800F3F0C  addiu v1,v0,0x2000
800F3F10  sw    zero,0(v0)
800F3F14  addiu v0,v0,4
800F3F18  bne   v0,v1,0x800F3F10
800F3F1C  nop
800F3F20  addiu a1,a1,0x4A         ; retail sector
800F3F24  j     call
800F3F28  ori   a2,zero,4          ;   delay slot: retail count
800F3F2C  hit:  addu a1,v1,zero    ; appended sector
800F3F30  ori   a2,zero,8
800F3F34  call: jal 0x80064C48     ; read(record, a1, a2)
800F3F38  nop
800F3F3C  lw    ra,0(sp)
800F3F40  nop                      ; load delay slot
800F3F44  addiu sp,sp,8
800F3F48  jr    ra
800F3F4C  nop
```

`v0`/`v1` are dead at the call site (the retail code calls `read()` there, which clobbers them);
`s2` survives. The font hook's compact payload lives at `0x80105448` and does not touch this run.

### 3c. Call site

| Addr | Was | Now | Instruction |
|---|---|---|---|
| `0x80063910` | `2645004A` | `0C03CFB3` | `jal 0x800F3ECC` |
| `0x80063914` | `0C019312` | `02402821` | `addu a1,s2,zero` (delay) |
| `0x80063918` | `34060004` | `00000000` | `nop` |

### 3d. RAM buffer relocation and length (unchanged from the first draft)

| Addr | Was | Now | Instruction |
|---|---|---|---|
| `0x80065528` | `3C088015` | `3C088018` | `lui t0,0x8018` |
| `0x8006552C` | `25084F40` | `25080000` | `addiu t0,t0,0` |
| `0x80065530` | `3C078015` | `3C078018` | `lui a3,0x8018` |
| `0x80065534` | `24E74F41` | `24E70001` | `addiu a3,a3,1` |
| `0x80065560` | `28C21000` | `28C22000` | `slti v0,a2,0x2000` |
| `0x8006556C` | `3C028015` | `3C028018` | `lui v0,0x8018` |
| `0x80065570` | `24424F40` | `24420000` | `addiu v0,v0,0` |
| `0x800655D8` | `28C21000` | `28C22000` | `slti v0,a2,0x2000` |

### 3e. Tooling

`tools/slots.py` — the table above; `tools/slotext.py apply|simulate|show`; `riotbattle.py insert
--extended` writes the four scripts to the appended slots and `checkedit --extended` proves the
retail region differs only inside retail slots of non-extended chunks and that the four retail slots
are pristine; `assemble.py --extended` budgets the four chunks at 16,384, takes their parked
`pending/chunk_NNN.txt` files along, writes `build/battle_dump_merged.ext.txt` (gitignored) and
passes the flag through `build`. `dump`, `verify` and `refresh` never change: the pristine dumps are
the retail layout by definition.

## 4. Verified before trusting (2026-09-11, no emulator)

1. `slotext.py simulate` on the patched EXE runs the call site for all 46 map indexes on the
   repo's R3000 interpreter (load-delay hazards enforced): maps 5/16/32/43 call
   `read(record, 3926/3934/3942/3950, 8)`, every other map calls `read(record, idx*85+0x4A, 4)`
   after exactly 2,048 zero-word stores to `0x801C2DDC..0x801C4DDC`, `sp` is restored, no
   hazard, no stray write. The retail EXE under the same harness gives the retail calls.
2. The byte-swap/scan routine on a synthetic 40-message slot: retail copies 8,192 bytes to
   `0x80154F40` and finds the 27 messages inside; patched copies 16,384 to `0x80180000`, the copy
   is identical to the swapped source, and all 40 entries land, all inside the buffer.
3. `riotfont.py simcheck` on the final EXE (font hook + half-width + renderer + this): PASS.
4. `apply --revert` on the patched file is byte-identical to the retail EXE.
5. `riotbattle.py checkedit --extended` on the built HEXMAP.BIN: retail region unchanged outside
   retail script slots, the four retail slots pristine, chunks 5 and 43 in their appended slots.

## 5. The boot test (human, emulator) — what must be true before the layout becomes the default

1. **A normal map loads and plays**: start a new game, fight the first battle (chunk 0, 8,163 /
   8,192 bytes — the tightest translated chunk). Dialogue must appear in the 24-column box.
2. **Chunk 5's battle** (early game, large map, 8,679 bytes in the appended slot): every message
   plays, no black screen at map load, units and terrain look right (the third plane is untouched
   by design, this checks the retail path was not disturbed).
3. **Chunk 43** if a save near the end is available; otherwise it waits.
4. Capture a DuckStation savestate in a battle and one on the name-entry screen: they let
   `riotfont.py liveness` re-validate `0x80105448` and `0x800F3ECC`, and `gridsim` the boot EXE.
5. Rebuild the disc with `TACTICS/HEXMAP.BIN` as the **last** file in the image so nothing else
   moves (it grows by 65,536 bytes; `ZDATA.BIN` is not referenced by name anywhere and may be read
   by sector). Path-based loading makes HEXMAP's own position irrelevant.

If step 2 black-screens, the first suspects in order: the appended sectors not contiguous in the
image (check the ISO), the `0x80180000` buffer (write-breakpoint it), the staging-buffer zeroing
(revert the stub's normal path to the plain retail read with `--revert` and re-test step 1).
