# FLAGS.md — open issues carried forward

Everything here needs a human decision, a tool fix, or an in-game look. Nothing here is
resolved by translating more chunks. Items are grouped by what blocks them.

Session of 2026-08-06 delivered `tl/battle/chunk_007.txt` (7,793 / 8,192, 399 slack) and
parked `pending/chunk_005.txt` (8,679 / 8,192, 487 over).

Second session of 2026-08-06 delivered `tl/script/batch_002.tsv` (script lines 1234 and 8604).
**`check` reports PROBLEMS (0) and `build` writes output for the first time in the project.**
§A1, §A2 and §A3 are resolved below; §C1 is partly resolved; §D4, §D5, §C4 and §C5 are new.

Third session of 2026-08-06 delivered `tl/script/batch_003.tsv` (the 102-entry description table,
**14.6% → 41.6% of message instances**), re-flowed `batch_001`, fixed §C4 and the carried-over
`chunk_035` edit. `check` still reports **PROBLEMS (0)** and `build` still writes both dumps.
**§C4 and §E's `ほう` line are resolved; §F is new and §F2 is the most important thing here.**

---

## A. Blocking the build right now

### A1. ~~`build` refuses to write~~ — RESOLVED 2026-08-06

`python3 tools/assemble.py check` → **All checks passed** (PROBLEMS: 0).
`python3 tools/assemble.py build` → writes `build/battle_dump_merged.txt` and
`build/script_dump_merged.txt`. The patch is buildable for the first time.

`build/battle_dump_merged.txt` **was** stale, exactly as this flag said: re-merging changed it by
87 insertions / 60 deletions, i.e. it had never contained chunks 7 or 33. It is now fresh, and
verified to differ from `dumps/battle_dump.txt` in precisely the ten chunks that have a
`tl/battle/` file — no other chunk touched, no line-count drift in any chunk.

⚠️ **One step of `build` still cannot run in a fresh clone**, and this is not a defect:
`original/SCRIPT.BIN` and `original/HEXMAP.BIN` are `.gitignore`d game data, so the reinsertion
half prints `-- skipping HEXMAP.BIN (original or merged dump missing)` and produces no `.BIN`.
Whoever has the disc image should drop the two files into `original/` and re-run `build` to
confirm the binaries. See §C5 for why `checkedit` cannot stand in for that.

### A2. ~~Root cause — exactly two untranslated messages~~ — RESOLVED 2026-08-06

Both are translated in `tl/script/batch_002.tsv`. The diagnosis in this flag was correct: nothing
but these two fall-through Japanese messages was blocking the build.

| Source line | Bank | Was | Now | Note |
|---|---|---|---|---|
| `script_dump.txt:1234` | 5 | 1,182 bytes, one 39-column segment | 2,570 bytes, longest run 23 columns | see **§D4** — it is not linear dialogue |
| `script_dump.txt:8604` | 43 | 894 bytes, contains `×` | 1,870 bytes, tag stream byte-identical | `×` → `Ｃｒｏｓｓ　ｂｕｔｔｏｎ` |

Bank pressure was never a factor, as predicted. Real figures, measured through
`riotscript._emit_bytes_from_body` (which counts the 900-byte `{HDR:}` block that
`assemble.py`'s `cost()` charges as 0, so these run ~900 higher than `check` implies):

- **bank 5**: 26,523 → 30,959 / 40,960 — **10,001 bytes still free**
- **bank 43**: 19,641 → 23,665 / 40,960 — **17,295 bytes still free**
- worst bank anywhere after the merge is bank 41 at 40,607 / 40,960, i.e. its 353 free bytes
  (§3.3) are untouched — no regression there.

All 44 banks re-encode to bytes cleanly, which is the reinsertion round trip minus the binaries.

**`{FFFE}` / `{FCC0}` counts, per line, before → after:**

| Line | `{FFFE}` | `{FCC0}` | Note |
|---|---|---|---|
| 1234 | **61 → 76** | 0 → 0 | +15, every one forced by the 24-column rule, on source segments 0, 1, 9 (+2), 13 (+4), 16, 17, 33, 35, 39, 45 and 53. Segment 13 is the 39-column one and needs five rows. No `{FCC0}` added — see §D4 for why |
| 8604 | **41 → 41** | 11 → 11 | Unchanged. The English fits the source's own page structure segment for segment, so the tag stream is byte-identical to the source apart from the text itself |

### A3. ~~`×` is a button glyph, not punctuation~~ — RESOLVED 2026-08-06

**`×ボタン` → `Ｃｒｏｓｓ　ｂｕｔｔｏｎ`.** Reasoning recorded in full in `glossary.md` §16;
the entry itself is in `glossary.md` §3, alongside a prospective △ → `Ｔｒｉａｎｇｌｅ　ｂｕｔｔｏｎ`
so the fourth button cannot drift.

Two findings from `riotfont.py` worth keeping whichever way this is revisited:

1. **The font is not full.** 88 codes in `SJIS_TO_ASCII`, ~1,232 bytes of payload inside an
   8,704-byte `AUTO_WINDOW`; one more glyph costs 14 bytes. §A3 had assumed fullness might kill
   option 2 — it does not.
2. **There is nonetheless no ✗ available.** Every glyph comes from `font8x8(ch)`, a 95-entry
   ASCII bitmap indexed `ord(ch) - 0x20`. SJIS `0x817E` is absent from the map and the pipeline
   cannot express a glyph that is not an ASCII character. Adding ✗ needs a hand-drawn bitmap plus
   changes to `SJIS_TO_ASCII` / `font8_rows_msb`, then a hardware re-proof. It would not have
   round-tripped today, which is the test the session prompt set for option 2.


---

## B. Blocking tier A chunks

### B1. Chunk 5 is infeasible in 8,192 bytes

Three passes: natural 1.97x → disciplined 1.74x → maximum compression short of deleting
content **1.64x**. The budget requires **1.53x**. Final: 8,679 bytes, **487 over**.
Parked in `pending/`.

### B2. 1.64x is a floor, not slack — measured, not asserted

Achieved ratios on chunks already shipped:

| chunk | budget ratio | **achieved** ratio |
|---|---|---|
| 0 | 1.74 | **1.73** |
| 10 | 8.39 | 1.88 |
| 12 | 8.49 | 2.10 |
| 33 | 9.52 | 1.93 |

Chunk 5 at 1.64x is **tighter than anything the project has shipped** and still misses.
The remaining sanctioned lever (§2.1 step 2, merging segments to delete `{FFFE}`) was measured
exhaustively: 29 mergeable pairs, **58 bytes**, against 487 needed. Closing the rest requires
deleting sentences, which §2.1 forbids.

### B3. Tier A is probably dead as a whole — decide before spending two more sessions

Chunk 16 (budget 1.59x) and chunk 32 (budget 1.61x) both sit **below** the measured 1.64x floor.
Chunk 43 (1.23x) is already parked. If the floor holds, all four tier-A chunks need the
`pending/slot-extension.md` work rather than more translation passes. Recommend settling the
`KOUSEI.EXE` question first and confirming the floor on one of 16 or 32, not both.

---

## C. Tooling defects

### C1. `assemble.py` does not implement the row check Appendix A claims

`validate_body` (lines 88–112) does charset and columns only. There is no page/row logic
anywhere in the file, so pages exceeding 4 text rows pass silently.

`tools/rowcheck.py` (added this session) mirrors `assemble.py`'s cost, column, charset and
tag-parity semantics and adds the missing row check plus per-line `{FFFE}` before→after diffing.
Usage: `python3 tools/rowcheck.py <chunk_num> <path_to_tl_file>`. It was calibrated against the
shipped byte figures for chunks 10, 11, 12 and 33 (exact match) and falsification-tested against
four planted violations: an overlong run, ASCII characters, a dropped tag, and `…`.

**Extended 2026-08-06** with a second mode, `python3 tools/rowcheck.py script [merged_dump]`,
which does the same row check for the **main script** and additionally counts the script-side
name insert at its true width (see §C4). It diffs each translated line's pages against the
pristine dump so that source breakage is reported as `INHERITED` rather than blamed on the
translation. `ROOT` is now derived from the file's own location instead of being hard-coded.
Battle mode is unchanged and re-verified against chunks 7 and 33.

Current output: columns clean across all 1,305 translated script lines; two pages over four text
rows, **both inherited** — line 1234 (source 61 rows, English 76; see §D4) and line 8194 (source
and English both 11 rows, from `batch_001`).

`assemble.py` itself still has no row check. It is a stand-in, not clearance (§0.6) —
`assemble.py check` remains the authority.

### C2. `riotbattle.py checkedit` has a bare `argv[3]` index

Running it with one argument raises `IndexError` instead of printing usage. Correct form is
`checkedit <original> <edited>`. One-line fix in `main`.

### C4. `assemble.py`'s column check is blind to the main-script name insert

`validate_body` substitutes `{FC00}{=0000}` with 7 placeholder characters before counting
columns, then strips all remaining tags. That is right for the battle script. **The main script
does not use `{FC00}` at all** — there are zero occurrences in `script_dump.txt`. It uses
`{FFEC}{=00}{=00}`, 113 occurrences, and the contexts put it beyond doubt that it is the same
player-name insert: `９軍隊長の{FFEC}{=00}{=00}だな？`, and `さん` / `君` / `殿` suffixed forms
throughout banks 0, 1, 5, 42 and 43.

`assemble.py` strips it to **0 columns**, so a main-script line can be up to 7 columns over the
limit and pass `check` silently. `batch_002` was laid out by hand against the true cost of 7 and
verified with the new `rowcheck.py script` mode; nothing in `batch_001` or `batch_002` is over.

Fix belongs in `assemble.py`: extend the substitution to `\{FFEC\}\{=00\}\{=00\}`.
**DONE 2026-08-06 (batch 003 session).** One line added to `validate_body`, immediately after the
`{FC00}` substitution. `check` was then re-run over the whole tree as the session prompt required:
it surfaced **nothing** — PROBLEMS (0) still — so no existing line was relying on the insert
costing 0 columns, in `batch_001`, `batch_002`, `batch_003` or any fall-through Japanese line. The other `{FFEC}`
variants (`{=01}` a number, `{=03}` an item name, and `{=02}` / `{=04}` / `{=05}` / `{=06}`,
which are undocumented) have **no known width bound** and want an in-game look before anyone
gives them a number.

### C5. `riotbattle.py checkedit` takes binaries, not dumps

The session prompt's verification step 3 asked for
`checkedit dumps/battle_dump.txt build/battle_dump_merged.txt`. That cannot pass and did not:
`checkedit` reads both arguments as `HEXMAP.BIN` images, slices them into fixed `0x2A800` chunks
and proves nothing outside `+0x25000`–`+0x27000` moved. Handed two text dumps it fails at the
first line — `FAIL: size changed 247339 -> 263662` — because an English dump is simply longer
than a Japanese one. The correct call is the one `assemble.py cmd_build` already makes:
`checkedit original/HEXMAP.BIN build/HEXMAP.BIN`, and it needs the binaries (§A1).

The equivalent proof was done at dump level instead and passes: the merged battle dump differs
from the pristine dump in exactly the ten translated chunks and nowhere else, with per-chunk line
counts identical. Anyone with the disc image should still run the real `checkedit` on the `.BIN`.

### C3. Chunk 33 dumper bug — recorded in `pending/README.md`, still open

`find_script_bounds` requires `\xfc\x51`; chunk 33 uses only `{FC50}`. Already documented; noted
here so it is not lost.

---

## D. Source defects (do not "fix" silently)

### D1. Dump artifact in chunk 5 line 17

`{FC70}{=00}逓{=20000E}` where lines 14 and 16 have the clean `{FC70}{=0062}{FC20}{=000E}`.
The dumper decoded argument bytes 0x9276 as Shift-JIS text. Preserved verbatim in the
translation. **Chunk 5 could not have passed `check` even at budget**, because this trips the
charset rule. Fix belongs in the dumper, not the translation.

### D2. Source pages exceeding 4 text rows are real

14 of them, across chunks 5, 6, 7, 30, 32, 36, 37 and 42. Worst is chunk 32 line 31 at
**59 rows**. None of the nine chunks shipped before this session contained one, which is why
this has not come up.

Chunk 5 source line 10 has a 7-row and a 5-row page. Chunk 7 line 23 has 5 rows. In both cases
source structure was preserved rather than inserting `{FCC0}`, because the text looks like
auto-advancing cutscene narration where a page break would be wrong. **Needs an in-game look
to confirm.**

### D4. Script line 1234 is a scrap/variant pool, NOT linear dialogue — CONFIRMED

The session prompt's working hypothesis was right, and the evidence is stronger than
"branching variants". Line 1234 is an **earlier draft** of the war-council scene that shipped as
line **1236**, left in the bank. Six independent findings:

1. **1234, 1235 and 1236 share a byte-identical 40-byte header prefix**
   (`{FFC2}{=00}{=13}` … `{FFD2}{=00}{=14}`). They are three siblings of one event.
2. **1236 is the playable version**: 21 `{FC50}` speaker channels, 19 `{FC30}` waits,
   12 `{FCC0}` page breaks, 17 `{FCB0}` transitions.
3. **1234 has none of those.** 61 `{FFFE}` and *zero* `{FC30}`, `{FC50}`, `{FC51}`, `{FCC0}`.
   Only **two** messages in the entire 7,931-message dump have ≥8 `{FFFE}` and no `{FCC0}`, and
   the other one (8239) is visibly a pool of unrelated NPC lines too. With no `{FC30}` anywhere
   the box never waits for input, so 503 characters could not be read even if it were reached.
4. **The sentences recur in 1236 with small edits** — `これでてめえも` / `体面が保てるんだ` vs
   1236's `体面が保てるな`; `いくぞ、本当の作戦会議の開始だ` vs 1236's `いくぞ、作戦会議だ`;
   `こんな無茶な遠征を` / `計画しといて、` / `よく言うぜ。` identical in both.
5. **The 39-column segment is a symptom.** `７軍の後ろを…９軍はまだ戦力が残ってるようだな。`
   restates segment 11's `９軍はまだ`, with segments 10 and 12 (`そういえば、` / `おおかた、`)
   reading as two alternative openings for one sentence. It is an unwrapped draft line, not a
   wrapping bug in a live message.
6. **The neighbour proves the register.** Line **1235** — same header, same shape, 1,184
   characters, zero `{FC30}` — contains the literal string **`１２３４５６７８９０１２`** three
   times. That is a developer's 12-column ruler. It also carries the same sentence twice in two
   registers (`…手薄になります。` polite / `…手薄になるってことだ。` plain) and the
   奴らに悟られずに / 敵に悟られずに pair. This is a scratch pool.

**What was done.** Translated **fragment by fragment**, each `{FFFE}` segment standing alone, as
the prompt directed for the confirmed case. Longest run is 23 columns. **The tag stream is
preserved exactly and no `{FCC0}` was added**, against the prompt's general licence to add them,
because a page break without a `{FC30}` does not pause and would only clear the box mid-flow;
and because if the data is addressed as a pool, inserted bytes could shift what indexes it. This
follows the §D2 precedent of preserving source structure where the text is not a normal textbox.
The page therefore still reports 61 → 76 text rows, correctly, as `INHERITED`.

**What is still needed.** An in-game look at the war council to confirm 1236 is what plays and
1234 is unreachable. If 1234 *is* reachable, it is broken in Japanese too and the fix is a
dumper/engine question, not a translation one.

### D5. `お前らは　したらしいな。` has a hole in it — preserved, not patched

Segment 27 of line 1234. The verb `した` is present; the **object is missing**, and the source
leaves a full-width space where it should be — compare 1236's
`お前たちで要塞を落として…`. Rendered `Ｙｏｕ　ｌｏｔ　　ｄｉｄ，　ｉｔ　ｓｅｅｍｓ．`,
keeping the double space so the hole stays visible on screen and nothing is invented to fill it.
Consistent with §D4: a draft line, never finished.

### D3. Chunk 7 line 24 — the one place in shipped work that needs eyes

`{FFFE}` went 6 → 8. Both additions are forced: source segments 3 and 5 are 16 and 20 JP chars
and overflow 24 columns in any English rendering. But this pushes an already-out-of-spec page
from 6 rows to 8. Everything else in chunk 7 is within spec. Check this textbox in game before
considering chunk 7 final.

Other `{FFFE}` changes in chunk 7: lines 25 and 26, 0 → 1 each (splitting
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ　ｕｎｄｅｒ　ａｔｔａｃｋ．` off the 24-column limit).

---

## E. Naming and translation decisions that could be revisited

All are entered in `glossary.md` §14 and cross-referenced from §13.

| Item | Decision | Why it might change |
|---|---|---|
| `キャビア` → Cavia | §14.1 | kana are exactly the loanword *caviar*; the pun may be deliberate (§13.14) |
| `ナコール` → Nacol | §14.1 | no in-game romanisation; alt *Nakor*, *Nacoll* (§13.15) |
| `ティータ` → Tita | §14.1 | **hapax** — one occurrence in the battle dump, zero in the script dump. Not a typo for ティミー: in ch.5 line 10 Fei is *surprised* by Timmy's arrival, so she was not calling her in line 1. Possibly Fei's beast, since Fei is a 獣使い, or a cut character (§13.16) |
| `ベルナール` → Bernard | §14.2 | alt *Bernal* |
| `オーク` → orc (lowercase) | §14.3 | class-table form still open (§10.2, §13.17) |
| `ほう` → **Ｏｈ** (was `Ｈｏｈ`) | §6, §10.6 | **Closed 2026-08-06.** `tl/battle/chunk_035.txt` now reads `Ｏｈ，`; the chunk went 557 → 555 bytes. No `Ｈｏｈ` remains anywhere in `tl/` |
| `クレス` → Cress | glossary §1 | alt *Kress*, *Cres*; no in-game romanisation |
| `ウエストバリー` → Westbury | glossary §2 | alt *Westbarry* |
| `ゼファー・クリッペン` → Zephyr Krippen | glossary §1 | name taken from the session prompt; alt *Zepher*, *Crippen*, *Klippen*. Appears **once** in either dump, so nothing corroborates the reading |
| `穀潰し` → freeloaders | glossary §2 | recurs in line 1236, so it will be re-used before it can be revisited cheaply |

### E1. Deviations from literal (§2.1 steps 5–6)

**Chunk 7:** 敵さん、大勢で → *Look at them all* (implication for the count);
傭兵あがりの若造ども → *Mercenary upstarts* (drops the youth sense);
王女の命、いただいたぞ → *Her life is mine*;
世話んなったじいさん → *the old man who raised her*;
お父様たちも → *your father* (drops the plural);
エチュード → *etude* (no `é` in charset).

**Script batch 002 (line 1234):** `わかったんだよ、` → `Ｗｅ’ｖｅ　ｆｏｕｎｄ　ｏｕｔ：` — the
source's `、` became `：` so that the three fragments after it (`薬の持ち主が。` / `薬の在処が。`
/ `黒幕が。`) read correctly whether they follow it or stand alone, which §D4 requires;
`かなり` → *very* rather than *quite*, purely for columns; `黒幕が。` → *Who is behind it.* as a
clause rather than the noun *mastermind*, because the fragment stands alone.

**Script batch 002 (line 8604):** `がんがん当てちゃおうね！！` →
`ｌｅｔ’ｓ　ｐｉｃｋ　ｐｌｅｎｔｙ　ｏｆ　ｗｉｎｎｅｒｓ！！` (implication for `がんがん`);
`ゆーことを示すの` → plain *means* — the casual spelling has no English equivalent that is not
an eye-dialect the §3.1 charset cannot carry.

**Chunk 5:** 橋の前にもオークが drops も; 王女様だけじゃなく → *not only her*;
自分たちで守る → *guarded our own*; Cavia given `ｃａｎ’ｔ` in her exhausted opening line,
against her otherwise uncontracted register (§14.6) — the one deliberate exception.

---

## F. Script batch 003 — the description table (2026-08-06)

### F1. The byte figure, measured the real way

**Bank 40: 39,189 / 40,960 used — 1,771 bytes free.** Measured through
`riotscript._emit_bytes_from_body`, i.e. counting the 900-byte `{HDR:}` block that `assemble.py`'s
`cost()` charges as 0. `check` will report this bank ~900 lighter; the figure above is the one the
inserter sees, and it is the one that decides overflow.

Every bank, before → after this session:

| Bank | before | after | free | note |
|---|---|---|---|---|
| **40** | 33,869 | **39,189** | **1,771** | the binding constraint, as predicted |
| 5 | 30,959 | 36,279 | 4,681 | |
| 2 | 26,835 | 32,155 | 8,805 | |
| 41 | 40,607 | 40,607 | 353 | **untouched** — no description line lives in bank 41 |
| the other 18 of the 21 | | | ≥ 10,000 | |

Growth is 5,320 bytes per bank: 5,130 from characters (EN 5,131 vs JP 2,530) and 190 from the
95 added `{FFFE}` breaks. One line of the block lives in bank 29 alone, not in the 21.

**Ratio hit: 2.03x.** The prompt asked for ≤ 1.8x and ~2,000 bytes of slack; I hit 2.03x and 1,771,
and here is why 1.8 is not reachable on this material rather than an excuse:

- The `Ｇｅｍ　Ｔｙｐｅ：<colour>` row is **fixed by §3 and unvarying**. It is 12–15 characters
  against the source's 8–10, i.e. **1.63x on its own**, and it is 1,371 of the 5,131 characters in
  the batch. The descriptions would have to come in at 1.72x to drag the whole to 1.8.
- `batch_001`, the same table by the same rules, shipped at **2.31x**. This batch is 12% tighter
  than the work it has to sit beside, which is as far as it can go without the entries reading
  differently from their neighbours in a list the player scans side by side.
- What is left is not fat. The ceiling is geometry, not bytes: 2 description rows × ≤23 columns
  is 46 characters, and 42 of the 101 descriptions are within 6 characters of that wall.

### F2. Bank 40 cannot hold a complete translation — and neither can 41, 5 or 2

This is the finding that matters, and it is not about this batch. I measured every bank's
**remaining untranslated Japanese** and projected it at 1.9x, a ratio no shipped work has beaten
(§B2's floor is 1.64x under maximum compression; real achieved ratios are 1.73–2.31):

| Bank | free now | untranslated JP chars | growth needed @1.9x | verdict |
|---|---|---|---|---|
| **41** | 353 | 14,607 | 26,292 | **short by 25,939** |
| **40** | 1,771 | 12,514 | 22,525 | **short by 20,754** |
| **5** | 4,681 | 9,573 | 17,231 | **short by 12,550** |
| **2** | 8,805 | 8,657 | 15,582 | **short by 6,777** |
| all other 40 banks | | | | fit, most with room to spare |

**~66,000 bytes short in total.** SCRIPT.BIN is "69% free" in aggregate (§3.3) and that aggregate
is misleading: the free space is in banks 10, 11, 21–27 and 34–39, which hold almost no text,
while the four banks that carry the bulk of it are full. Bank 41's 353 free bytes were always
known (§3.3); the other three were not.

Consequences, in order:

1. **The main script needs the same treatment as chunk 43** — repointing, or a bank-spill scheme —
   and it needs it before roughly a third of the remaining script can ship. This is the
   `pending/slot-extension.md` question again, on the `MAIN1.EXE` side. It should be settled
   before many more script sessions, for the same reason §B3 says to settle `KOUSEI.EXE` first:
   otherwise sessions are spent producing text that cannot be inserted.
2. **The "keep ~2,000 bytes of slack" instruction is moot** and I have not distorted the
   translation to satisfy it. Reserving 2,000 bytes against a 20,754-byte shortfall buys nothing;
   what buys something is writing tight, which is why this batch is at 2.03x and not at 2.31x.
3. **Nothing overflows today.** No bank exceeds 0xA000, `insert` would not raise, and `check`
   passes. The failure is in the future, not in this build.
4. Worth re-measuring with `tools/bankmeasure.py` (added this session) at the start of every
   script session. It is the only tool that reports the figure the inserter actually uses.

### F3. Scope — the block is 101 lines, not 102

The session prompt's count of "102 remaining unique lines ending `ジェムタイプ：<colour>`" includes
**`script_unique.txt` line 979**, which is not a description-table line: it is the 404-character
`『ジェム』` tutorial, and it merely *contains* the word `ジェムタイプ` in prose. Filtering on
lines that actually **end** `ジェムタイプ：<colour>`, as the prompt's own wording says, gives
**101**. Line 979 is untranslated and out of scope; it belongs with the §7 tutorial boxes.

The prompt's 2,929-character figure is inflated the same way. The block as translated is
**2,525 Japanese characters over 101 lines** (25.0 average, not 28.7), plus the `クラス７０`
placeholder at 5 — **2,530 in 102 entries**, which is the denominator of the 2.03x above.

Not a defect in the prompt's conclusion: 101 lines × 21 occurrences is still 2,121 instances and
still by far the biggest block available. `assemble.py status` now reports **41.6%** of message
instances translated, up from 14.6%.

### F4. `{FFFE}` counts, per line

Uniform, so a table of 102 rows would be noise:

| Change | Lines | Why |
|---|---|---|
| **1 → 2** | 95 | the source puts the whole description on one row (16 JP columns) and lets `ジェムタイプ` share the second; English needs two description rows plus the Gem Type row on its own |
| 1 → 1 | 6 | lines 79, 117, 119, 120, 142, 174 — the description fits one row, so the source's single break is all that is needed |
| 0 → 0 | 1 | the `クラス７０` placeholder |

**No entry exceeds three text rows**, i.e. two description rows plus `Ｇｅｍ　Ｔｙｐｅ`, per
§10.3 and the prompt's ceiling. Verified mechanically, not by eye: `rowcheck.py script` reports
columns clean across all 3,405 translated lines and no page over four text rows that the source
did not already exceed (the two inherited ones, lines 1234 and 8194, are unchanged — no third one
was introduced).

### F5. `batch_001` re-flow — 20 segments at 24 columns, now 3

Done as the prompt invited, and it **saves** 34 characters (68 bytes per bank), so it cost the
budget nothing. Sixteen entries changed; the Japanese keys are untouched and `check`/`rowcheck`
were re-run over the whole tree afterwards.

Representative changes: `Ａ　ｓｗｏｒｄ　ｗａｒｒｉｏｒ　ｏｆ　ｇｒｅａｔ` / `ｓｐｅｅｄ　ａｎｄ　ｓｋｉｌｌ．`
→ `Ａ　ｓｗｏｒｄ　ｗａｒｒｉｏｒ，　ｇｒｅａｔ` / `ｉｎ　ｓｐｅｅｄ　ａｎｄ　ｓｋｉｌｌ．`;
`ｗｈｏ　ｋｉｌｌｓ　ｗｉｔｈ　ｏｎｅ　ｂｌｏｗ．` → `ｋｉｌｌｉｎｇ　ｗｉｔｈ　ｏｎｅ　ｂｌｏｗ．`
(§4's *kills with one blow* survives intact); `ｗｈｏ　ｒｏａｍｓ　ｔｈｅ　ｗｏｏｄｌａｎｄｓ．`
→ `ｒｏａｍｉｎｇ　ｔｈｅ　ｗｏｏｄｌａｎｄｓ．`.

Three word changes worth naming, all in already-shipped text:

- 神の使いといわれる → `Ａ　ｓｗｏｒｄｓｗｏｍａｎ　ｃａｌｌｅｄ` (was *said to be*), which also
  matches how 異名を持つ / と言われる are rendered throughout `batch_003`.
- 遠隔戦闘の経験を積んだ → `ｗｅｌｌ　ｖｅｒｓｅｄ　ａｔ　ｒａｎｇｅ` (was *in ranged combat*) —
  one character short of fitting, and *ranged combat* survives in the neighbouring entry.
- 乗馬と戦闘の技術を極めた → `Ａ　ｋｎｉｇｈｔ，　ｍａｓｔｅｒ　ｏｆ` drops *both*.

**Three segments could not be brought under 24 and are unchanged**, because every arrangement
either drops a word or needs a third description row:

1. `ｓｗｏｒｄｓｍａｎ　ｉｎ　ｌｉｇｈｔ　ｇｅａｒ．` (素早さと技に優れた軽装の男剣士) — its
   partner row is fixed, at 21.
2. `Ａｎ　ａｒｍｏｕｒｅｄ　ｓｗｏｒｄｓｍａｎ　ｏｆ` and 3. `ｈｉｇｈ　ａｔｔａｃｋ　ａｎｄ　ｄｅｆｅｎｃｅ．`
   (高い攻撃力と防御力を持つ鎧剣士) — 48 characters of content against a 46-character ceiling.
   `ｏｆ　ｈｉｇｈ　ａｔｔａｃｋ　ａｎｄ　ｄｅｆｅｎｃｅ．` is 27 and `ｈｉｇｈ　ａｔｔａｃｋ　ａｎｄ　ｄｅｆｅｎｃｅ．`
   is exactly 24, so the break has nowhere to go.

### F6. `batch_001` has five entries that render four text rows

Not introduced here, but it is the one place where existing work depends on the unconfirmed §10.3
window being four rows rather than three: 高い戦闘力を持つ上級の天馬騎士, 長射程の炎・雷の単体魔法…,
モンスターを操り、氷魔法を使う…, 仲間の能力を引き出して戦うことを…, and 炎・雷・光魔法を使う最上級の….
Each is three description rows plus `Ｇｅｍ　Ｔｙｐｅ`. **Every one of the 102 entries in
`batch_003` is three rows**, so if the in-game check comes back "three rows", only these five need
re-cutting.

### F7. `Ａｔｋ＋ＮＮ`, and why the weapon stat row is not `Ａｔｔａｃｋ`

Fourteen weapon entries carry a second field: `攻撃力＋ＮＮ　ジェムタイプ：色`.
`Ａｔｔａｃｋ＋１０　Ｇｅｍ　Ｔｙｐｅ：Ｇｒｅｅｎ` is **exactly 24 columns**, and `Ｇｅｍ　Ｔｙｐｅ：`
cannot be shortened (§3, 2,964 occurrences). Rather than create the one fragile row the prompt
told me not to create, the stat label is **`Ａｔｋ＋ＮＮ`**, which holds every stat row at ≤ 21.
Prose keeps *attack power* (§4) — this is a mechanical stat field, and the source itself uses a
compressed label there.

**Swap it back to `Ａｔｔａｃｋ＋ＮＮ` the moment the description window is confirmed wider than 24**,
or if a reviewer would rather have the full word and accept 24 columns on the single Green weapon
(line 171 — the only Green one in the table, so it is exactly one row, once).

### F8. Deviations from literal (§2.1 steps 5–6)

- 古の種族、ダークエルフの血を引く → *Ａ　ｍａｇｅ　ｏｆ　ａｎｃｉｅｎｔ　ｄａｒｋ　ｅｌｆ　ｂｌｏｏｄ．*
  — 古の種族 (*an ancient race*) folded into *ancient*; both rows are within 3 of the wall.
- 鋭い爪を持ち、鋭敏な動きをする暗殺猫 → *Ａ　ｓｗｉｆｔ　ａｓｓａｓｓｉｎ　ｃａｔ　/　ｗｉｔｈ　ｓｈａｒｐ　ｃｌａｗｓ．*
  — 鋭敏な動き carried by *swift* rather than a clause.
- 帝国の量産型機械兵試作機 → *Ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｐｒｏｔｏｔｙｐｅ　/　ｍａｃｈｉｎｅ　ｓｏｌｄｉｅｒ．*
  and クリミアの量産型機械兵２号機改良型 → *Ｃｒｉｍｅａ’ｓ　ｉｍｐｒｏｖｅｄ　…* — **量産型 is
  dropped in the derived entries only**. It is carried in full by the entry each derives from
  (`Ｍａｓｓ‐ｐｒｏｄｕｃｅｄ　ｍａｃｈｉｎｅ　ｓｏｌｄｉｅｒ　Ｕｎｉｔ　１`,
  `Ｃｒｉｍｅａ’ｓ　ｍａｓｓ‐ｐｒｏｄｕｃｅｄ　…`), which sits directly beside it in the list.
- さく裂弾を放つ長射程の無人砲台 / 火炎弾を放つ… → *Ａ　ｌｏｎｇ‐ｒａｎｇｅ　ｔｕｒｒｅｔ　…* —
  無人 (*unmanned*) dropped; *turret* carries it and 砲台 has no shorter English.
- 他のユニットを乗せて運搬できる機構車両 → *Ａ　ｖｅｈｉｃｌｅ　ａｂｌｅ　ｔｏ　ｃａｒｒｙ　/　ｏｔｈｅｒ　ｕｎｉｔｓ．*
  — 機構 (*mechanical*) dropped for width.
- 最強の攻撃能力を持つオリジナル４号機 → *…　ｏｆ　ｔｈｅ　/　ｓｔｒｏｎｇｅｓｔ　ａｔｔａｃｋ．* — 能力 dropped.
- 天をも支える怪力無双の巨人 → *Ａ　ｇｉａｎｔ　ｗｈｏｓｅ　ｍａｔｃｈｌｅｓｓ　/　ｍｉｇｈｔ　ｕｐｈｏｌｄｓ　ｔｈｅ　ｓｋｙ．*
  — reordered so the relative clause takes the break (§2.1 step 6).
- 幸運を運ぶと言われる → *ｓａｉｄ　ｔｏ　ｂｒｉｎｇ　ｌｕｃｋ．* — *good fortune* would not fit.

### F9. Readings with a defensible alternative

| Kana | Chosen | Alternative | Why it might change |
|---|---|---|---|
| ネルガリ | `Ｎｅｒｇａｌｉ` | **`Ｎｅｒｇａｌ`** | The kana are one vowel off the Babylonian death-god ネルガル, and the class is a dark elemental, so the god is very probably the source. Plain transliteration chosen because nothing in either dump corroborates it. Appears twice, both in this table |
| 水蛇 | `ｓｅａ　ｓｎａｋｅ` | *water serpent* | The literal *water serpent* is 4 columns longer and does not fit the row; *hydra* was rejected as a different creature |
| トクロフ | `Ｔｏｋｒｏｆ` | *Tokurofu*, *Tocroph* | One occurrence in either dump. A tree, apparently |
| ルシファ | `Ｌｕｃｉｆｅｒ` | *Lucifa* | Strict transliteration is *Lucifa*; the European form matches the Bauer / Carline / Helfer naming already fixed |
| 悪鬼 | `ｆｉｅｎｄ` | *demon* | §9 already glossed it *fiend*, and 豚顔 (pig-faced) is in the same sentence, so *fiend* keeps 鬼 → *ogre* free for the sibling entries |
| 魔術戦士 | `ｍａｇｅ　ｗａｒｒｉｏｒ` | *spell warrior*, *sorcerous warrior* | Must stay distinct from 魔法戦士 → *magic warrior* (§4); the chosen form uses the 魔術/魔法 split the glossary already draws |

### F10. Suspected source oddities, preserved

- **`子供のドラゴン。成長すれば・・？`** — two dots, not three, and a `？`. Reproduced exactly as
  `．．？` per §3.1's match-the-dot-count rule. It is the only entry in the table with a question
  mark, and reads like a designer's note left in.
- **`自走砲１です！` / `自走砲２です！` / `固定砲３です！`** — three entries written as sentences
  with `です！` where every other entry is a noun phrase. They are unfinished, like `ダミーぶきです`,
  and are translated the same way rather than tidied into the table's voice.
- **`量産型機械兵１号機。`** has no owner where its neighbours name the Empire, Crimea or Seneca.
  Left as it is.

---

## G. Wave 1 review — battle chunk 1 / PR #2 (2026-09-08)

Raised by the reviewer of PR #2. The rulings themselves are in `glossary.md` §18; only the items
that still need a human or a later check are recorded here.

### G1. `tl/battle/chunk_000.txt` now has 27 bytes of slack — the tightest file in the project

Two corrections were applied to chunk 0 this session (glossary §18.3): `くっ・・・` `Ｕｇｈ．．．` →
`Ｔｃｈ．．．` (0 bytes) and `ああ。` `Ｙｅｓ．` → `Ｙｅａｈ．` (**+2 bytes**). Chunk 0 goes
**8,163 → 8,165 / 8,192, slack 29 → 27**. `assemble.py check` passes.

`translation_prompt.md` §3.3 already called 29 "uncomfortably close". At 27 there is effectively no
room left: **the next glossary correction that lands on chunk 0 and is not width-neutral will force
a re-cut of the chunk**, not a one-line edit. Chunk 0's ratio is 1.74 (tier B), so a re-cut is real
work. Worth a deliberate decision by a human: either re-cut chunk 0 once now to buy back ~200 bytes
of headroom, or accept that it is frozen.

### G2. The ノロ tic now costs 2 bytes per instance, ~77 instances still to come

Glossary §18.1 corrects the tic to the spaced form `，　ｎｙｏｒｏ．`. That is +1 full-width
character = **+2 bytes per occurrence** against the unspaced spelling. Roughly **70 further `ノロ`
lines in `script_unique.txt` and 7 more in `battle_dump.txt`** carry it, so about **150 bytes**
project-wide. Immaterial in the roomy banks; **worth watching if a `ノロ` line ever lands in bank 41
(353 free) or bank 40 (509 free after batch 004)**. No shipped file is affected — the tic had never
been rendered when the ruling was made.

### G3. In-game checks requested by chunk 1

- Five pages sit at exactly 4 text rows on dump lines 2, 6, 7, 9 and 15 — the same shape §D2/§D3
  already ask about. Chunk 1 introduces no page the source did not already fill.
- Two sentences run across a `{FCC0}` page break and keep a lowercase first word on the far side
  (`ｂａｔｔｌｅ，　ｂｕｔ` → break → `ｉｆ　ｅｖｅｎ　ｏｎｅ　ｓｕｒｖｉｖｅｓ`, and
  `ｒｅａｃｈｅｄ　０　ＨＰ，` → break → `ｙｏｕ　ｃａｎ　ｎｏ　ｌｏｎｇｅｒ　ｓａｖｅ`). This follows
  chunk 0's shipped tutorial. If glossary §10.4's leading `{FCC0}{FFFE}` blank row turns out to be
  wasted, these two joins are where it will read worst.
- Does the pig-faced fiend's `Ｏｉｎｋｋｋｋ．` read as intended in the box?

### G4. Speakers in chunk 1 are inferred from portrait ids, and no name appears

`{FCB0}` portraits: 0005 the hobbit chief (the `ノロ` speaker), 0001 the veteran, 0000 the newcomer,
0004 the anxious one, 0002 the sarcastic one, 0006 the fiend, 0003 the tutorial speaker. Battle
chunk 2 carries the same anxious voice and names ティミー and サイクス, and chunk 3 identifies the
confined 9th Army member as シャスタ, but **nothing in chunk 1 names anyone**, so no name is
asserted there. Worth an in-game look; if a later chunk names these portraits, chunk 1's registers
want re-checking (cf. §10.11, §13.13).

### G5. Suspected source typo — `９軍ってのは` vs `９軍てのは`

Dump lines 6 and 7 are two alternate takes of one scene, of which the player sees only one. They
differ by a single `っ` in the same clause. Both take `ｔｈｅ　９ｔｈ　Ａｒｍｙ，`. Same species of
authoring slip as `訊ねたい` / `尋ねたい` in chunk 0 (glossary §10.10). Nothing to do; recorded so
it is not "fixed".

### G6. `Ｎｕｍｅｒａｌｓ` — the ch.12 precedent held again, and is now consistent enough to fix

Glossary §10.8 is still open. Chunk 1 spells `あと１隊` and `１人でも` as *one* while keeping `９`
(`９ｔｈ　Ａｒｍｙ`, fixed by §2) and `０` (an HP value). That is exactly the split §15.1 drew for
the racing table: **digits stay full-width where they are data, prose spells small numbers out.**
Three sessions have now independently landed on it. Someone should promote it from an open question
to a rule in §3 rather than leave each translator to rediscover it.

## H. Wave 1 review — battle chunk 2 / PR #3 (2026-09-08)

### H1. The `{FCB0}` portrait-id → character map is still guesswork, and chunk 2 is where it bites

Chunk 2 names only **Fernando** (self-identified, id 5), **Albert** (addressed by name, id 6),
**Timmy** and **Sykes** (addressed together by id 10). Ids 0, 1, 2, 3 and 9 are unnamed:

- **id 1** is the casual, tactically-minded speaker who addresses the player by name. He is written
  to §7's Kain register — contractions throughout — but the chunk never names him. **If an in-game
  check shows id 1 is not Kain, his contractions need revisiting.**
- **id 3** is the young voice that calls Fernando `いばってる` and is addressed in the same breath as
  `ティミー、サイクス` by id 10, so id 3 is probably Timmy or Sykes — the chunk never says which.
- **id 9** is the 重剣士 who speaks with `僕`.
- **id 0B is a second Melzario hobbit who does NOT use the `ノロ` tic** and speaks plain polite
  Japanese. That is the source's own distinction and it was preserved. Do not "fix" it later.

Same species of question as §G4 (chunk 1) and glossary §10.11 / §13.13. Only settleable in-game.

### H2. `帝国軍` — chunk 7 took the width fallback where the default would have fitted

Glossary §2 makes `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` the default and `ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ` the
fallback for when 24 columns will not take it. Chunk 2 uses the default twice, at 21 columns.
Shipped `chunk_007.txt` uses the fallback in a row that measures 22 columns with the default —
i.e. it would have fitted.

**Not to be acted on.** The Japanese messages differ, so CLAUDE.md §3's identical-JP rule is not
engaged, and `chunk_007.txt` has only **399 bytes of slack**: swapping in the longer form costs
bytes for no correctness gain. Recorded so nobody "discovers" the divergence later and re-cuts a
tight file over it. Glossary §20.4 states the default explicitly so later units do not drift.

### H3. In-game check requested by chunk 2

The two coda variants (file lines 14 and 20) are mutually exclusive — the player sees one. Both
were translated and both are gated, but **which one fires, and on what condition, is unknown**.
Worth confirming that the line-20 variant is reachable at all; cf. §D4, the same question about
script line 1234.

## I. Wave 1 review — battle chunk 3 / PR #1 (2026-09-08)

### I1. ~~Quoted UI tokens: capitalised or not?~~ ✅ **RESOLVED 2026-09-08 (PR #8 review) — see §N2**

> **Settled: a quoted token naming something the game DISPLAYS — a command, menu option, map
> label, item or skill — is capitalised (verbatim where the source already supplies full-width
> Latin); a quoted phrase that merely describes stays lowercase.** The tie-breaker §I1 lacked is
> that chunk 3's source is `「入る」` (Japanese) while script 987's is `「ＥＮＴＥＲ」` (already
> Latin, i.e. a quotation of what is on screen). **One shipped line moves** — `chunk_003.txt` L5,
> `“ｅｎｔｅｒ”` → `“ＥＮＴＥＲ”`, 0 bytes, queued on the wave-3 corrections unit's existing
> `chunk_003:5` row. The analysis below is kept as the record of why it stayed open so long.

`「…」` → `“…”` is settled (§3, §15.1). **Whether the quoted text is capitalised is not.** Measured
across every quoted token in `tl/` as of chunk 3's merge:

| Capitalised | Lowercase |
|---|---|
| `“Ｇｅｍｓ”`, `“Ｐｏｗｅｒ　Ｓｔｏｎｅ”` (chunk 0) | `“ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”`, `“ｐａｓｔ　ｐｌａｃｉｎｇｓ”`, `“ｆｏｒｍ　ｔｏｄａｙ”`, `“ｆｏｒｍ”` (`batch_002`) |
| `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”` (chunk 33) | `“ｄｅｍｏｎ　ｂｌａｄｅ”` (`batch_003`) |
| `“Ｒｉｂｂｉｔ”` (chunk 10) | `“ｅｎｔｅｒ”` (chunk 3) |
| `“Ｖｉｌｌａｇｅ”`, `“Ｗａｉｔ”` (chunk 1) | |

**Two candidate rules, and neither survives the corpus:**

- *"Names capitalised, descriptions lowercase"* — plausible, and it explains most rows, but it puts
  chunk 1's `“Ｗａｉｔ”` (a menu verb) and chunk 3's `“ｅｎｔｅｒ”` (a menu verb) on the same side,
  and they are shipped on opposite sides.
- *"Sentence-initial capitalised, mid-sentence lowercase"* — fails too: `batch_002` ships
  `ｈｏｒｓｅ’ｓ{FFFE}“ｆｏｒｍ”` lowercase mid-sentence while chunk 1 ships `ｃｈｏｏｓｅ　“Ｗａｉｔ”`
  capitalised mid-sentence. `batch_002` even carries the same token both ways
  (`“Ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”` and `“ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”`).

**Not treated as a defect in chunk 3, deliberately.** `“ｅｎｔｅｒ”` matches `batch_002`'s shipped
practice as squarely as `“Ｗａｉｔ”` matches chunk 0's, so there was no decided rule to enforce, and
deciding it by holding one PR would have set project-wide policy from a two-entry sample written
during the same wave. Glossary §19.2's note has been narrowed accordingly so it no longer reads as
a general rule.

**To settle it**, someone should pick one rule and sweep all of `tl/` in a single §4.3 correction,
the way the `×` button was settled in glossary §16. Every candidate fix is width-neutral (a case
change costs 0 bytes and 0 columns), so this can be done at any time and is **not** blocking. The
one place it is *not* free is `chunk_000.txt`, which has 27 bytes of slack (§G1) — but a case
change costs nothing there either.

### I2. `アイテムを{FFFE}奪われました。` is now fixed for seven instances

Chunk 3 establishes `Ａｎ　ｉｔｅｍ　ｗａｓ{FFFE}ｓｔｏｌｅｎ　ｆｒｏｍ　ｙｏｕ．`. Recounted against
`battle_dump.txt`: the string occurs in **chunks 3, 9 (×3), 28, 29 and 30** — seven instances, five
chunks. (The earlier note listing chunks 38, 39 and 41 was wrong; they do not carry this string.)
Recorded in glossary §21.3. Later translators must copy it byte-for-byte, not re-render it.

### I3. Chunk 3 discharges chunk 1's Flag 12

Chunk 1 read `謹慎処分を受けてる` as singular and masculine (`ｓｏ　ｈｅ’ｓ　ｃｏｎｆｉｎｅｄ．`) and
flagged a 2-byte edit if a later chunk disagreed. Chunk 3 names the man — **Shasta**, who
self-references with `僕`. No edit needed. Closed.

## J. Wave 1 review — script batch 004 / PR #4 (2026-09-08)

### J1. The description table now ships at two registers of tightness — 2.60× and 2.23×

Re-measured on the merged files, taking the description clause as the text before each entry's
final `{FFFE}`:

| | description clause | |
|---|---|---|
| `batch_003`, weapon rows | 198 JP → 515 EN | **2.60×** |
| `batch_003`, whole batch | 1,478 JP → 3,647 EN | 2.47× |
| **`batch_004`** | 491 JP → 1,095 EN | **2.23×** |

Batch 004 is about **14% tighter** than the shipped standard, and the tightness is concentrated in
one repeated frame rather than spread: **six rows sit at 1.40×** —
`持つ者に炎の守護をもたらす剣／槍。` → `Ａ　ｆｉｒｅ‐ｗａｒｄｉｎｇ　ｓｗｏｒｄ／ｓｐｅａｒ．`, which drops
`持つ者に` ("to the one who bears it") entirely. It is a **§2.1 step 5 departure**.

> ⚠️ **CORRECTED 2026-09-08 by the PR #6 reviewer, verified against PR #4's body. Two statements
> in the original text of this flag were false and are struck below.**
>
> 1. ~~"the PR did not flag it; recorded here instead"~~ — **PR #4 flagged it explicitly.** Its
>    **Flag 3** reads: *"§2.1 step 5 — 持つ者に…をもたらす implied, lines 146–148 and 170–172…
>    Fits one row, which is what makes the six of them affordable (12 bytes each instead of 44)."*
>    By rule number and by line number. Two independent audits reached this conclusion; the PR
>    body was re-read to confirm it.
> 2. ~~"+42 bytes per entry × 6 = +252 bytes" … "parking about 7 of the 34 lines" … "seven
>    Japanese holes in a table"~~ — **the arithmetic is wrong.** PR #4's Flag 3 gives the one-row
>    form as **12 bytes each instead of 44**, so the restore delta is **32 bytes/entry × 6 =
>    192 bytes**, not 252. Bank 40 would land at **509 − 192 = 317 free**, and at §J2's measured
>    ~37 bytes/line net growth that is **~5 lines** of parking, not seven.
>
> **The conclusion survives both corrections and is NOT reopened.** 317 free is still 183 bytes
> below the project's 500-byte reserve, so the restore remains unaffordable without parking real
> lines, and the departure stays accepted. What changes is the record: PR #4 did its job, and the
> cost of the alternative is smaller than this flag claimed.

**Accepted deliberately at review, with this arithmetic.** The row is 21 columns, so columns are
not the constraint — bank 40 is. Restoring `持つ者に` needs a second row, **+32 bytes per
entry × 6 = +192 bytes** (corrected above). Bank 40 has **509 free against the project's 500-byte
reserve — 9 bytes of margin** (⚠️ **now 471, see §O1** — the restore lands at **279**, and the
margin against the 500-byte reserve is gone) — and net growth in bank 40 runs 1,262 ÷ 34 ≈ **37 bytes per line**,
so 192 bytes means parking **about 5 of the 34 lines**. Five weapon descriptions left in Japanese,
visible as holes in a table the player reads side by side, to lengthen six entries. The partial
option is worse: ~3 parked lines buys ~111 bytes, enough for three or four of the six, which would
break the seed's requirement that all six be identical.

**What is actually lost** is not accuracy — every distinguishing feature survives on every row
(fire, cold, thunder god, Tyr, Odin, blue dragon scales, moonlight, meteors, jet-black, rusted),
and a player can tell all 34 weapons apart. What is lost is **uniformity across the table**: a
batch-003 sword and a batch-004 sword read at noticeably different lengths side by side.

**If bank 40 is ever repointed**, these six entries are the first thing to loosen — they are
cheap, self-contained, and the seed already fixes what the fuller form must say.

### J2. Bank 40 is spent, and bank 5 is now the one to watch

Measured before/after by removing `batch_004.tsv` and re-merging. Every affected bank spends
**exactly 1,262 bytes** — the 21-map-bank replication:

| bank | before | after |
|---|---|---|
| **40** | 1,771 | **509** |
| 5 | 4,681 | **3,419** |
| 2 | 8,805 | 7,543 |
| 33 | 10,615 | 9,353 |
| 12 | 11,621 | 10,359 |
| 3 | 11,891 | 10,629 |
| 41 | 353 | **353 — untouched**, the table does not land there |

> ⚠️ **SUPERSEDED for banks 40, 5, 2 and 33 by §O1 (PR #9, 2026-09-08).** The wave-1 corrections
> unit spends a further **38 bytes in each of these 21 banks**: **bank 40 is now 471 free, not
> 509**; bank 5 **3,381**; bank 2 **7,505**; bank 33 **9,315**. Bank 41 is still 353 and still
> untouched. **Make the next bank-40 decision against 471.** §J1's corrected 192-byte restore
> therefore lands at **279 free, not 317** — still affordable, with a thinner margin.

Two consequences for planning, both measured rather than projected:

1. **The item/equipment description table is finished for this run.** Lines 185–225 (clubs, axes,
   bows, machine-soldier arms) land in the same 21 banks and must go to `pending/script/` until
   bank 40 is repointed. This confirms §F2's projection exactly.
2. **Bank 5 lost 27% of its remaining headroom to one batch** and is now the third-tightest bank
   at 3,419 free. It is not yet blocking, but any future batch resident in bank 5 needs
   `bankmeasure` run before dispatch, not after.

---

## K. Wave 2 review — battle chunk 4 / PR #6 (2026-09-08)

Merged round 1, MERGE, all eight gates green. Rulings and glossary additions in `glossary.md` §23.

### K1. The byte figure, and the first zero-re-flow unit in the project

**chunk 4: 3,849 / 8,192 bytes — 4,343 bytes slack.** Widest run **23 columns**, nothing at 24; no
page over 4 text rows *at all*, not merely none beyond the source's own. No `{FC00}` name insert in
this chunk.

**The tag stream is byte-identical to `dumps/battle_dump.txt` on all 25 lines, including every
`{FFFE}`** — verified at review by extracting the pristine chunk and diffing per-line tag lists
(`lines with ANY tag diff: 0`). **Zero breaks added, deleted or moved; no `{FCC0}` touched; no
insert repositioned.** This is the first unit to ship that way, and it is worth recording as an
existence proof: at ratio 5.08 the source's own 12-column break structure was already right for a
24-column box, segment for segment, exactly as `translation_prompt.md` §3.2 predicts. The source's
`{FCC0}{FFFE}` leading-blank pages (lines 3, 10, 13, 21) and trailing empty segments (lines 4, 7,
10 ×2, 21) are preserved untouched, per §3.2 and glossary §10.4.

Punctuation was measured rather than asserted: `？` 11 → 12 (**+1**, the one flagged `。` → `？` on
`どうして…解隊されちゃうんだろ。`), `！` 15 → 15 (**+0**), and all **10** ellipsis runs match the
source dot for dot (`[3, 3, 3, 4, 5, 4, 4, 3, 3, 4]` both sides).

### K2. `辺境` → *frontier*, and why `chunk_000.txt` is deliberately left alone

Ruled at review; the entry and the full reasoning are in `glossary.md` §23.1. Recorded here because
it is the second instance of the §20.4 pattern and the pattern is now a rule rather than a one-off:

> A **phrase-level** rendering in an earlier shipped file does not bind a later unit's **word-level**
> choice, provided the Japanese *messages* differ. Record the variant; do not re-cut.

`chunk_000.txt` line 4 carries `こんな辺境` **twice**, both `ｓｕｃｈ　ａ　ｒｅｍｏｔｅ　ｐｌａｃｅ`.
Chunk 4 uses *frontier* three times. Nothing is re-cut. Note for anyone tempted later: chunk 0 has
**27 bytes of slack** (§G1) and §18.3 records that the next correction there forces a full re-cut,
so this file is now effectively frozen against non-mandatory edits.

### K3. In-game check — is the portrait-`04` girl Princess Cavia?

Chapter 5's rescued girl. She is alone, hunting the fairy forest, refuses an escort and says
`また会いましょ`. Chunk 5's parked text has the party thanked for saving `王女様とフェイ` at that
forest, and glossary §14.1 dates the Princess's name to ch.5. **Plausibly Cavia travelling
incognito.**

**No glossary entry was made and no §14.1 cross-reference was added** — deliberately. §14.1 is a
table of decided entries; writing an inference into it is how §9's `メルザリオ` row came to be
wrong. The English is safe either way: all 13 of her segments are contraction-free §14.6 Cavia
register, verified at review.

**What would settle it:** an in-game look at whether portrait `04` in chunk 4 is the same portrait
the Princess uses in ch.5/ch.7. If confirmed, §14.1 gains the cross-reference and **no line in
`chunk_004.txt` needs to change**.

### K4. In-game check — the portrait-`06` map, and the line-21 watcher

Chunk 4's coda (line 21) is a lone speaker weighing whether to keep tailing the 9th Army: he had
*heard about* them, and he goes hungry unless they slip up. The `{FCB0}` arguments:

```
line  3 {FCB0} args: ['00060001', '00080000']    <- Ridge speaks on portrait 0006, channel 1
line 21 {FCB0} args: ['00060000']                <- the watcher is portrait 0006, channel 0
```

**Same portrait id 06**, differing only in the channel byte — so the portrait table points at
Ridge. And that agrees with, rather than contradicts, the "hired outsider" reading: glossary §9's
wave-2 seed records `リオン`/`Ｌｅｏｎ` as *"a man who sent Ridge to help and wants to stay
anonymous"* (ch.6). A Ridge hired to attach himself to the squad is exactly the speaker of line 21,
and it explains why he is the one telling everyone in line 3 to relax about being disbanded.

The English names nobody and works under either reading, so **nothing needs to change**. This is
recorded beside §H1 (the `{FCB0}` portrait-id map is still guesswork) because chunk 4 gives §H1 its
first case where the id map would actually decide a reading.

### K5. Two shipped lines need a translator, both from rulings made at this review

Neither is applied here: the reviewer's remit is `glossary.md`, `FLAGS.md`, `pending/README.md` and
`HANDOFF.md`, and `HANDOFF.md` already queues line edits of this kind in the wave-3
`corrections/audit-wave1` unit. Both are measured so nobody re-derives them.

| File | Line | Was | Becomes | Cost |
|---|---|---|---|---|
| `tl/battle/chunk_003.txt` | 5 | `Ｓｔｉｌｌ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` | `Ｈｏｗｅｖｅｒ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` | 19 → 21 cols, **+4 bytes**; chunk 3 slack 3,591 → 3,587 |
| `tl/battle/chunk_001.txt` | 14 | `ｙｏｕ　ｓａｖｅｄ　ｕｓ，　ｎｙｏｒｏ．` | `ｗｅ　ａｒｅ　ｓａｖｅｄ，　ｎｙｏｒｏ．` | 20 → 20 cols, **0 bytes** |

The first is the `しかし` ruling (glossary §23.3) — `Ｓｔｉｌｌ，` is §19.1's fixed form for
`それにしても` and cannot also serve `しかし`. It was already queued for wave 3 by both wave-1
audits; the ruling now names the replacement.

**The second is new and neither wave-1 audit caught it** (glossary §23.4): `chunk_001:14`
`いやいや、助かったノロ。` is active while `chunk_003:7` `助かったノロ、` is passive — two hobbits
thanking the party, in source strings that differ only in their final mark, which §5's mechanism
says should be the *only* difference. Zero-byte fix.

### K6. `ファリーナ` reclassified — moved once, for the whole wave

Moved from `glossary.md` §1 (People) to §2 (places), with the dump evidence recorded in the row.
Verified against both dumps before moving, not taken from a report: `ファリーナという国も昔は
栄えとった`, `ファリーナ城`, `ファリーナの南、カペラの村`, `ファリーナを占領した`, `ファリーナ出身`,
and three people identified *by* it (`ファリーナの司教、クレウス`, `ファリーナの衛兵隊長、ウルフ`,
`ファリーナの自治官フェリクス`). **No instance in either dump uses it as a personal name.**

`Ｆａｒｉｎａ` is unchanged, so **nothing translated needs revisiting.** PRs #7 and #8 both flag
this; it is done, and their reviewers must not move it again.

⚠️ **`クリミア` (PR #5 Flag 4) is the same shape and was deliberately NOT moved here.** Chunk 4
does not touch it and this reviewer has not seen the evidence; moving a fixed row on an unverified
claim is precisely what §4.3 forbids. **PR #5's reviewer makes that call.**

### K7. PR-body verification claims need to name real source strings

Not blocking, and PR #6's *conclusion* was correct — but four of the nine citations in its Flag 8
duplicate list do not survive checking, and were caught only because the gate was re-run from the
dumps rather than read off the PR:

- `助けて` attributed to chunk 0. **Chunk 0 contains no `助けて`** — its `Ｈｅｌｐ　ｍｅ．．．` renders
  `たすけて・・・`, the kana spelling, a different source string.
- `あのまま` attributed to `pending/chunk_043`. **`あのまま` occurs only in chunk 4**, in the whole
  battle dump.
- `マズい` attributed to `pending/chunk_043`. Chunk 43 has `マズい、自爆装置だ！！`; chunk 4 has
  `マズいな。` — different strings.
- `いえ、` attributed to `pending/chunk_005`. Chunk 5 has `いえ、これくらいは`; the bare `いえ、`
  segment belongs to chunks 4 and 26.

Chunk 0's two `何` renderings were also quoted without their stutters (`な、何事だ！？` →
`Ｗｈ‐ｗｈａｔ　ｉｓ　ｔｈｉｓ！？`, not `Ｗｈａｔ　ｉｓ　ｔｈｉｓ！？`), and `こんな辺境` in chunk 0 was
reported once where it occurs twice.

**For future units:** a duplicate-check claim should name the exact source string and the file and
line it was aligned against. Segment-count alignment against the non-`{FFFE}` tag skeleton is the
cheap way to do it and is what this review used.

---

## L. Wave 2 review — battle chunk 6 / PR #7 (2026-09-08)

Merged at round 2, squash `dd406d0`. Round-1 findings 1–6 all verified fixed against the file;
finding 3 was fixed with a **different and better replacement than the reviewer proposed**, and
the finding was withdrawn (see §L5).

### L1. The byte figure

**chunk 6: 5,899 / 8,192 — 2,293 bytes slack.** Ratio 3.09 (tier C); the slot never bound.
Geometry was the constraint, as the dispatch predicted: **151 rows, widest 23, 0 rows at exactly
24, 0 over.** `{FFFE}` changed on four lines — 6, 17, 18 (each 1 → 2, tutorial boxes that will not
hold `Ｅｎｅｍｙ　ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ` / `Ｙｏｕ　ｈａｖｅ　ｎｏｔ　ｄｅｆｅａｔｅｄ` on one row) and 21
(11 → 12, from a single 23-character source segment). No `{FCC0}` added anywhere. No bank is
touched — this is a battle unit, and `FLAGS.md` §F2's bank figures are unchanged.

⚠️ **The PR title and body still carry the round-1 figure (5,897 / 2,295).** The true round-2
figure is in the rework comment and in the squash commit. Not blocking, but a stale PR body is
what a later audit will read first.

### L2. `{FC03}`, and eight lines in the dump with no speaker channel at all — needs an in-game look

Raised as the unit's Flag 7/8 and **measured at review rather than left as a guess.** This is the
highest-value in-game check outstanding on the battle script, because it decides whether the
`> 4 text rows` warnings on eight lines mean anything at all.

`{FC03}` occurs **32 times in `battle_dump.txt` and zero times in `script_dump.txt`** — it is
battle-only. It carries a small argument (`{=0000}` … `{=003F}`), sometimes with an `FA10…` /
`FA11…` blob appended, and appears in 11 chunks: 0 (×2), 2, 5, **6 (×6)**, 12 (×3), 16 (×10),
25 (×2), 26 (×2), 28 (×2), 29 (×2), 42.

The related and more important shape: **eight lines in the whole dump carry no `{FC50}` or
`{FC51}` anywhere and still exceed four text rows.**

| Chunk | Line | Text rows | `{FC03}` | Status |
|---|---|---|---|---|
| 6 | 9 | 15 | 2 | shipped (PR #7); every segment given exactly one English row |
| 6 | 21 | 11 → 12 | 0 | shipped (PR #7); tags are **only** `{FFFE}` and `{FFFF}` |
| 7 | 23 | 5 | 0 | shipped — see §D3 |
| 7 | 24 | 6 → 8 | 0 | shipped — **§D3 already asks for eyes on this one** |
| 30 | 23 | 8 | 0 | not yet translated |
| 32 | 31 | **59** | 0 | not yet translated (tier A, blocked) |
| 37 | 14 | 8 | 0 | not yet translated |
| 42 | 11 | 16 | 0 | not yet translated |

**Chunk 32 line 31 is 59 text rows.** No 24×4 box displays 59 rows, and no conversation is 59
rows without a single page break or speaker change. That is strong evidence these lines are
**pools of independently-selected messages** — the engine picking one string per event — rather
than one long page. If that is right, then the `> 4 rows` warning on all eight is meaningless and
`rowcheck` should learn to recognise the shape; if it is wrong, chunk 7 line 24 is already broken
in shipped work and chunk 6 lines 9 and 21 would be too.

**What to check in game:** enter chapter 5 (church map) and chapter 6, and see whether the
line-9 and line-21 strings appear one at a time (pool) or run on as a single scrolling exchange
(page). §D3's chunk 7 line 24 is the same question and the same visit can settle both.
Recorded in `findings.md` §24 with the measurement method.

### L3. Two parked files owe an adopt-on-re-cut, both from rulings made at this review

Neither ships today; both would **create** a CLAUDE.md §3 violation the day the slot patch lands
if they are re-cut without adopting the shipped form. Rows added to `pending/README.md`.

| File | Line | Now | Must become | Cost |
|---|---|---|---|---|
| `pending/chunk_005.txt` | 13 | `Ｔｈｉｓ　ｃａｎ’ｔ　ｂｅ．．．` | `Ｔｈａｔ　ｃａｎｎｏｔ　ｂｅ．．．` | 16 → 17 columns, **+2 bytes** |
| `pending/chunk_043.txt` | 14 | `Ｗ‐ｗａｉｔ！` | `Ｗ，　Ｗａｉｔ！` | 9 → 8 columns, **−2 bytes** |

`chunk_005` is 487 bytes over its slot already, so the +2 makes a bad number marginally worse and
changes nothing about its feasibility. This joins glossary §23.2's `そうそう。` row on the same
list — three lines chunk 5's eventual re-cut must adopt.

### L4. `glossary.md` §18.2 was factually wrong about the mechanism, and is corrected

§18.2 held that `おお`, `ほう`/`ほお`, `おや` and `あ、` are kept apart **by their punctuation**
rather than by four different words. Counted across both dumps at this review: `おお、` occurs
**40** times against `おお！` **7**, and `ほう、`/`ほお、` **5** — so the majority form of おお takes
`Ｏｈ，`, which is exactly what `ほう、` takes. The split separates おや and あ、 and does **not**
separate おお from ほう. It only looked as though it did because chunk 1's single instance was
`おお！`.

Corrected in glossary §24.4 as a deliberate, accepted collapse on the ふっ/フンッ → `Ｈｍｐｈ`
principle. **No shipped byte changes** — every instance in `tl/` already renders `Ｏｈ` plus the
source's own stop. What changed is a sentence that would have misled the next translator into
thinking `Ｏｈ，` was reserved.

### L5. A null duplicate check ran on every battle unit before this review — and what replaces it

Disclosed by chunk 6's translator against its own round-1 work, and confirmed here. **Battle
`tl/*.txt` files contain zero Japanese characters** (measured: chunks 0, 1, 2, 3 = 0 each;
`tl/script/batch_001.tsv` = 964, because script TSVs keep the Japanese in column 2). So the gate-6
method of *grepping the unit's Japanese against `tl/`* **could never match for a battle unit** and
silently returned “no hits” every time. It worked only on the script side. That is why two of
chunk 6's round-1 findings existed at all.

**The method that works** — and that this review used — is **positional row-pairing**: split both
the dump line and the rendered line on the non-`{FFFE}` tag skeleton, pair the `{FFFE}`-separated
rows inside each cell by index, and compare the English every Japanese row receives. Applied
across all 15 rendered battle files, both `pending/` files and the four script TSVs, that is 2,181
paired rows and it runs in under a second.

⚠️ **Two traps it must be used with**, both hit during this review:

1. **A row containing a `{FC00}{=0000}` name insert is not the bare row.** `chunk_003.txt` line 4
   is `さあ、{FC00}{=0000}、` → `Ｃｏｍｅ　ｏｎ，　{FC00}{=0000}，`, and `chunk_000.txt` line 3 is
   `よし、{FC00}{=0000}。` → `Ｇｏｏｄ，　{FC00}{=0000}．`. A splitter that breaks at tags reports
   both as bare-segment divergences against chunk 6. **Neither is one**, and the round-1 finding
   that rested on the first of them was withdrawn.
2. **An added `{FFFE}` shifts every later row index inside its cell.** Chunk 6 line 21 goes
   11 → 12 rows, so its `・・・` → `．．．` pair reports as a mismatch until the shift is accounted
   for. Compare per cell, and treat an index shift as “re-flowed”, not “divergent”.

This is now written into `.claude/agents/translator.md` gate 6 (commit `06353c7`). §K7 asked for
duplicate claims to name the exact source string, file and line; this is the mechanism that makes
that cheap.

### L6. Speakers on chunk 6 lines 9 and 21 are inference, not tags

A consequence of §L2: neither line carries a portrait or channel tag, so who speaks is read from
content. Line 9 is taken as a Ridge/Sykes reunion; line 21 as the Black Knight leader retreating
from Sykes, then a warning about Ridge, then a party member asking Sykes who he is. The reading is
internally consistent with the named cast, but `甘く見ない方がいいぞ。` / `あいつが本気になったら、`
/ `こんなもんじゃない。` could be Ridge boasting about himself **or** Sykes warning the Knights,
and the English is deliberately neutral between the two. Same in-game visit as §L2 settles it.
Cf. §G4 and §H1, which are the same class of problem on portrait ids.

## M. Wave 2 review — battle chunk 9 / PR #5 (2026-09-08)

Merged at round 2, squash `5f3e714`. Decision recorded as a **COMMENT** review: GitHub refuses both
APPROVE and REQUEST_CHANGES on this repository, so every wave-2 decision is a comment.

### M1. The byte figure

**chunk 9: 3,973 / 8,192 — 4,219 bytes slack.** 95 non-empty rows, **widest 23, zero rows at 24,
zero over 24**. Line count 21 vs 21. The tag stream is byte-identical to the dump except `{FFFE}`
on two lines (line 8: 3 → 4, line 9: 16 → 18), both in the PR's Flags — which also proves
mechanically that **no `{FCC0}` was added, moved or dropped**, since `assemble.py`'s tag-parity
check excludes `{FFFE}` and nothing else.

Page shapes were computed for all 21 lines, source against rendered: **only the two flagged pages
change**, and every other page keeps the source's exact (lead, rows, trail). No page over 4 text
rows. The four dump-wide shape counts the PR quotes were recounted from `battle_dump.txt` and all
four are exact: `(False,3,False)` = **115**, `(False,2,False)` = **262**, `(True,4,False)` = **182**,
`(False,4,True)` = **1**, and the leading-blank-plus-four-rows-plus-trailing-blank shape that
glossary §10.4 worries about = **0**.

### M2. Finding 1 — the translator overturned the reviewer's prescribed wording, correctly

Recorded because this is the second time in wave 2 that a translator's counter-form beat the
reviewer's (chunk 6's `Ｎｏｗ，` over `Ｃｏｍｅ　ｏｎ，` was the first), and both times the
translator's evidence was measured and the reviewer's was not.

Round 1 asked for `しかし恐ろしい兵器だ。` to be split two rows as
`Ｈｏｗｅｖｅｒ，　ｗｈａｔ　ａ` / `ｔｅｒｒｉｂｌｅ　ｗｅａｐｏｎ　ｉｔ　ｉｓ．`. The translator shipped a
three-row form instead — `Ｈｏｗｅｖｅｒ，` / `ｗｈａｔ　ａ　ｔｅｒｒｉｂｌｅ　ｗｅａｐｏｎ` / `ｉｔ　ｉｓ．`
at 8 / 22 / 6 — and it is right. Measured at this review, independently:

| 2-row split of that wording | cols | verdict |
|---|---|---|
| `Ｈｏｗｅｖｅｒ，　ｗｈａｔ　ａ　ｔｅｒｒｉｂｌｅ` / `ｗｅａｐｏｎ　ｉｔ　ｉｓ．` | 24 / 13 | row 1 at the hard limit |
| `Ｈｏｗｅｖｅｒ，　ｗｈａｔ` / `ａ　ｔｅｒｒｉｂｌｅ　ｗｅａｐｏｎ　ｉｔ　ｉｓ．` | 13 / 24 | row 2 at the hard limit |
| `Ｈｏｗｅｖｅｒ，　ｗｈａｔ　ａ` / `ｔｅｒｒｉｂｌｅ　ｗｅａｐｏｎ　ｉｔ　ｉｓ．` (the review's) | 15 / 22 | **row 1 ends on the article `ａ`** |
| `Ｈｏｗｅｖｅｒ，　ｗｈａｔ　ａ　ｔｅｒｒｉｂｌｅ　ｗｅａｐｏｎ` / `ｉｔ　ｉｓ．` | 31 / 6 | illegal |

**Every two-row split either puts a row at exactly 24 or ends a row on a lone article.** The
three-row form is the only shape with every row ≤ 23 and no short-word row-end, and it costs the
same bytes: 2×37 + 2 = **76** = 2×36 + 4. The file measures 3,973 either way.

⚠️ **One correction to the PR's reasoning, which matters for the next unit.** It says
`Ｈｏｗｅｖｅｒ，　ｗｈａｔ　ａ　ｔｅｒｒｉｂｌｅ` (24 columns) means `ｔｅｒｒｉｂｌｅ` **cannot** join row 1.
It can — 24 is the hard limit and it would pass `check`. It **must not**, which is the stronger
and correct claim: `translation_prompt.md` §3.2 says "aim for ≤ 23, not ≤ 24", chunk 9 holds all 95
of its rows to ≤ 23, and chunk 6 shipped 151 rows with none at 24. **No shipped battle row in the
project sits at 24.** Worth stating plainly so nobody reads "≤ 24" as a target.

The review's own finding 2 had ordered a short-word row-end removed from line 10, so taking its
finding-1 wording verbatim would have fixed one §3.2 defect and introduced another. The three
short-word row-ends that remain (`…ｈｅａｄ　ｔｏ`, `…ｓｅｃｒｅｔ　ｉｓ　ｔｏ`, `…ｓｏｌｄｉｅｒ，　ｗｅ`)
were re-checked and are still forced: each sits on a 4-row page at the wall, and the only
repacking available severs `Ｄｏｃｔｏｒ` from `Ｃｒｉｍｅａ` or pushes a row to 24.

### M3. ⚠️ A CLAUDE.md §3 violation in already-merged work, found by this review's gate 6

**Not chunk 9's** — chunk 9 contains no instance, and nothing here blocked its merge. Recorded so
it is not lost, and queued for the wave-3 corrections unit exactly as glossary §23.3 and §23.4
queued theirs. Not applied here: the reviewer's remit is `glossary.md`, `FLAGS.md`,
`pending/README.md` and `HANDOFF.md`, not `tl/`.

The tutorial box `村が襲われました。` (`{=FA1000300030}`, **13 instances in `battle_dump.txt`**) is
rendered two ways across merged files — byte-identical Japanese, divergent English:

| File | Line | English | rows |
|---|---|---|---|
| `tl/battle/chunk_007.txt` | 25, 26 | `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．` | 14 / 13 |
| `tl/battle/chunk_034.txt` | 7 | `Ｔｈｅ　ｖｉｌｌａｇｅ　ｈａｓ　ｂｅｅｎ{FFFE}ａｔｔａｃｋｅｄ．` | 20 / 9 |

`tl/battle/chunk_006.txt` line 14's `Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．` (23 columns) is
**not** part of the violation and must not be swept into the fix: its source is
`村が　襲われました。` **with an internal full-width space**, a different string, so §3 is not
engaged on it — the §20.4 / §23.1 / §24.5 shape again.

**Measured both directions, so whoever takes it does not re-derive them:**

- adopt chunk 34's form in chunk 7 → **+4 bytes per instance × 2 = +8**; chunk 7 has **399** bytes
  of slack, so it fits, but chunk 7 is the second-tightest file in the project.
- adopt chunk 7's form in chunk 34 → **−4 bytes**, one instance; chunk 34 has **6,601** bytes of
  slack.

**Recommendation, not a ruling** (the corrections unit's reviewer decides): chunk 34's passive
tracks the source's `襲われました` and matches both §21.3's shipped stolen-item box
(`Ａｎ　ｉｔｅｍ　ｗａｓ　ｓｔｏｌｅｎ　ｆｒｏｍ　ｙｏｕ．`, passive) and chunk 6's neighbouring
`Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．`, whereas `ｉｓ　ｕｎｄｅｒ　ａｔｔａｃｋ` is a paraphrase.
But it is the direction that costs bytes in the tighter file, and it changes 2 instances to fix 1.

⚠️ Also note: glossary §24.6 cites this box as "§21.3's shipped `村が襲われました。` →
`Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．`". Two things in that citation are loose — §21.3 is the
**stolen-item** message, not this one, and the form quoted is chunk 6's, which renders the
**spaced** source string. Left as written (it is a register note and its point stands), but the
corrections unit should not read it as authority for which form wins.

### M4. Gate 6 re-run with the positional method, and the figures that supersede round 1's

§L5 replaced the null grep-Japanese-against-`tl/` check with positional row-pairing. Run here
across **all 16** shipped battle chunks: **873 paired rows, 132 paired messages.**

- **Chunk 9 is clean.** Its only recurring message, `アイテムを{FFFE}奪われました。` (×3), is
  byte-identical to `chunk_003.txt`'s §21.3 form — 1 distinct English on both rows. **0
  message-level divergences involve chunk 9.**
- **6 row-level divergences exist corpus-wide, none of them chunk 9's**, and §24.5 rules that §3
  engages on the message, not the row. Two are documented (`帝国軍が` §20.4, `ファリーナの南、`
  §24.5); three more (`ありがとうございます。`, `こいつは`, `『知識の書』を`) are row-index
  artefacts of the §L5 trap 2 kind — equal row counts, non-corresponding content — and are not
  divergences at all.
- **`隊長！` is confirmed as exactly the false positive §24.5 predicts**, and the PR has the
  assignment right: `chunk_007.txt` line 2 is the bare `Ｃａｐｔａｉｎ！`; `chunk_014.txt` line 3 is
  the row carrying `{FC00}{=0000}`. **No action — do not chase it again.**
- **Script side checked too**, which the PR did not do: 10 of chunk 9's 88 distinct Japanese
  segments occur in `script_unique.txt` (`いや・・・`, `お前も`, `しかしながら、`, `それでも`,
  `ところで`, `ないんだ。`, `アイテムを`, `ウエストバリーの`, `カーラインの奴らに`, `フン、`), and
  only `それでも` appears in translated script work — as `お前はそれでも、` in `batch_002`, a
  different source string. No conflict.

### M5. Three column figures in the PR body are wrong, and are corrected in the glossary

None of them is a gate failure — they are figures quoted in prose, and the **file itself** measures
correctly (widest row 23, verified). But glossary §25 records the remeasured values, because a
wrong column count in a glossary note is what makes the *next* translator's row arithmetic fail.

| Term | PR said | Actually |
|---|---|---|
| `Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ．` | 19 | **18** |
| `ｔａｋｅ　ｂａｔｔｌｅ　ｓｔａｔｉｏｎｓ` | 22 | **20** |
| `Ｙｏｕ　ｌｏｏｋ　ｄｏｗｎｃａｓｔ．` | 19 | **18** |

This is §K7's ask still not fully landed. The PR's *measured* claims — bytes, row widths, page
shapes, dump-wide occurrence counts, the finding-1 and line-12 split tables — were all checked and
were all **exact**; it is the incidental column counts in the additions table that drifted.

### M6. One glossary addition was missing from the PR body entirely

`それでも` → `Ｅｖｅｎ　ｓｏ，` is rendered on chunk 9 line 12 and appears in neither the PR's
Glossary additions table nor its "used exactly as already fixed" list. It is a **fourth**
adversative alongside でも → `Ｂｕｔ，`, それにしても → `Ｓｔｉｌｌ，` and しかし → `Ｈｏｗｅｖｅｒ，`,
so it is exactly the kind of term that drifts if it is not written down. Added at §25.2;
`Ｅｖｅｎ　ｓｏ` occurs nowhere else in `tl/`, so the form is free and nothing is re-cut.

### M7. `クリミア` reclassified — the call `FLAGS.md` §K6 deferred to this reviewer

**`クリミア` is a PERSON**, moved from glossary §2 (places) to §1 (People), with the evidence in the
row. Verified against both dumps at this review, not taken from the PR: **5 battle + 64 script
occurrences, not one of them a place.** He self-refers in the third person
(`この砦は、このクリミアにお任せ下さい。`, `またこのクリミアの新型機械兵`), is addressed vocatively
twice (`クリミア博士、反乱軍です・・・！！`, `クリミア博士、事は計画通り進んで`), is located *inside*
a place (`クロスリーにいるクリミア博士`), and the script's machine-soldier table credits him as their
designer (`クリミアの量産型機械兵２号機`). `Ｃｒｉｍｅａ` is unchanged, so **no shipped line is
re-cut** — the same shape as メルザリオ (§20.1) and ファリーナ (§K6).

**`クロスリー` is the place**, and it is a new §9 seed candidate (`Ｃｒｏｓｓｌｅｙ`, 8 columns) — 8
battle + 2 script occurrences, all locational. It is **not** chunk 9's business; chunk 9 does not
render it. Promote in the wave that first does.

### M8. Both wave-2 seeds this chunk consumed are promoted, used exactly as seeded

`ディール帝国` → the `Ｄｉｅｌ` Empire and `ワーウィック` → `Ｗａｒｗｉｃｋ`, both to glossary §25.1,
with their §9 rows struck. Counts confirmed at review: ディール 2 battle / 0 script (the other is
`ディール帝国紅の騎士団の将`, which agrees that it is the Empire's proper name); ワーウィック 2
battle / 6 script, every occurrence locational, which is the seed's own figure.

### M9. Rulings this review makes that bind later units

1. **`Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` serving both `そうそう。` and `そのとおりだ。` stands** — glossary
   §25.3. Decided on a corpus count, not taste: `そのとおり` occurs **once in the whole project**
   and **no chunk or bank contains both strings**, so the collision can never be seen in one
   scene. Reserve forms if that ever changes: `Ｅｘａｃｔｌｙ．` (8) preferred, `Ｑｕｉｔｅ　ｒｉｇｈｔ．`
   (12).
2. **`Ｆａｔｈｅｒ` carries both the priest (§24.1) and the parent** — glossary §25.4. Confirmed
   rather than split, and chunk 9 introduces nothing: `pending/chunk_005.txt` line 13 already
   renders `お父様・・・・` as `Ｆａｔｈｅｒ．．．．`, byte-identical, and
   `pending/chunk_043_abridged.txt` lines 41–42 render a parent's notes as `Ｆａｔｈｅｒ’ｓ`.
3. **`甘くない` of an institution → `ｈａｒｄｅｒ　ｔｈａｎ　…　ｔｈｉｎｋ`** — glossary §25.1. A negated
   comparison rendered as a positive one, accepted because the two are the same proposition on one
   scale and every literal split either ends a row on `ａｓ` / `ｓｏ` or measures exactly 24.

## N. Wave 2 review — script batch 005 / PR #8 (2026-09-08)

Merged at **round 2**, squash `38c18bc`. All eight §6 gates re-run on head `19769cf` with round-1
evidence discarded, and every figure in the PR body re-derived rather than read off it.

### N1. The byte figure, and the banks

**4,040 bytes**, net **+4** on round 1's 4,036 (finding 1 +8, finding 2 +12, finding 3 −16). 26
unique lines, 1 instance each, **26 message instances**. 1,980 JP → 4,004 EN characters, **2.02×**.

| bank | before | after | spent |
|---|---|---|---|
| 29 (984–988) | 27,323 free | **25,589 free** | 1,734 |
| 30 (989–1001) | 36,671 free | **35,119 free** | 1,552 |
| 31 (1040–1047) | 35,581 free | **34,827 free** | 754 |

**The two banks under 2,000 free are 41 (353) and 40 (509), and this unit touches neither** — not
asserted, proved: `merge` + `bankmeasure` were run twice, once with `batch_005.tsv` in place and
once with it moved aside, and the diff between the two runs is exactly three lines, banks 29/30/31.
Bank 5 (3,419) is likewise untouched. Every bank in this unit has 25,000+ free, so **any later
correction to `batch_005` is free**.

Geometry, re-measured independently of `rowcheck`: **widest row 23, none at 24, none over 24, no
page over 4 text rows**; 72 rows sit at 22–23. `{FFFE}` changed on 13 lines, net **−4**; `{FCC0}`
counts identical to the source on all 26 lines, none added or moved; excluding `{FFFE}`, the tag
stream is byte-identical to the source on all 26 lines. `rowcheck.py script` warns only on the two
pre-existing INHERITED pages (1234 page 0, 8194 page 26), neither of which is in this unit.

Gate 6 was run positionally, the §L5 method: each of the 26 Japanese messages occurs **once** in
`script_dump.txt`, **zero** times in `battle_dump.txt`, and **zero** times in any of the other 23
files under `tl/` and `pending/`. The one internal repeat, `あなた方に　神の恵みの{FFFE}あらんことを。`
in 1040 and 1041, is byte-identical in both.

### N2. §I1 IS SETTLED — quoted UI tokens are capitalised, descriptive quoted phrases are not

**§I1 has been open since chunk 3's review and is closed here.** The rule:

> **A quoted token that names something the game itself displays — a command, a menu option, a map
> label, an item, a skill — is CAPITALISED.** Where the source already supplies full-width Latin,
> reproduce it verbatim and do not re-case it. Where the source supplies Japanese, capitalise the
> English. **A quoted phrase that merely describes rather than names stays lowercase.**

**What settles it is a source fact §I1 did not have.** §I1 got stuck because chunk 1's `“Ｗａｉｔ”`
and chunk 3's `“ｅｎｔｅｒ”` are both menu verbs shipped on opposite sides, so "names vs
descriptions" and "sentence-initial vs mid-sentence" both failed. The tie-breaker is that **the two
source strings are not alike at all**: chunk 3's is `「入る」` — Japanese, one occurrence in
`battle_dump.txt` — while script 987's is `「ＥＮＴＥＲ」`, **already full-width Latin**, two
occurrences in `script_dump.txt`. The game displays `ＥＮＴＥＲ` on the map in Latin caps. So
`“ＥＮＴＥＲ”` is not a translator's casing choice at all; it is a quotation of what is on screen,
and chunk 3's `“ｅｎｔｅｒ”` is the one row that has to move.

Every previously-shipped row the rule now explains, with no other change: `“Ｇｅｍｓ”`,
`“Ｐｏｗｅｒ　Ｓｔｏｎｅ”` (chunk 0), `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”` (chunk 33),
`“Ｖｉｌｌａｇｅ”` / `“Ｗａｉｔ”` (chunk 1) — all displayed names, capitalised ✅.
`“ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”`, `“ｐａｓｔ　ｐｌａｃｉｎｇｓ”`, `“ｆｏｒｍ　ｔｏｄａｙ”`, `“ｆｏｒｍ”`
(`batch_002`) — descriptive column headings the guide is explaining, lowercase ✅.
`“ｄｅｍｏｎ　ｂｌａｄｅ”` (`batch_003`, the 妖刀 epithet) and `“Ｒｉｂｂｉｔ”` (chunk 10, a quoted
utterance) are neither, and are unaffected. `batch_002`'s own two-way
`“Ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”` / `“ｒｕｎｎｉｎｇ　ｓｔｙｌｅ”` is the heading versus the running text and
is left as shipped.

**batch 005 already obeys it, unprompted, and is the strongest evidence for it** — the source draws
the same line inside a single message and the translation preserves it: `『支援効果』` →
`“Ｓｕｐｐｏｒｔ　Ｅｆｆｅｃｔ”` against unquoted 包囲効果 → `ｔｈｅ　ｅｎｃｉｒｃｌｉｎｇ　ｅｆｆｅｃｔ`
two sentences later; `『説得』` → `“Ｐｅｒｓｕａｄｅ”` against the bare verb 説得する → `ｐｅｒｓｕａｄｅ`;
`「ＥＮＴＥＲ」` → `“ＥＮＴＥＲ”` against `ＥＮＴＥＲ地点` → `ＥＮＴＥＲ　ｐｏｉｎｔ`; the label
`“ＧＵＥＳＴ　ＵＮＩＴ”` against prose `ゲスト` → `ｇｕｅｓｔ`.

**Lines this affects (§4.3): exactly one.** `tl/battle/chunk_003.txt` **L5**, `“ｅｎｔｅｒ”　ｃａｖｅｓ`
→ `“ＥＮＴＥＲ”　ｃａｖｅｓ`. A case change costs **0 bytes and 0 columns**. **Not applied at this
review** — a reviewer's remit is `glossary.md`, `FLAGS.md`, `pending/README.md` and `HANDOFF.md`,
not `tl/`. ⚠️ **It lands on the row the wave-3 corrections unit is already editing**: that unit
carries `chunk_003:5` for glossary §23.3's `しかし` → `Ｈｏｗｅｖｅｒ，` (+4 B). **Both edits are on
the same message line and must be made in one pass**; combined cost +4 B, chunk 3 slack
3,591 → 3,587.

### N3. The JP-char-count defect is the coordinator's regex ONLY — `tools/queue.py` is CLEAN

`HANDOFF.md` asked whether `tools/queue.py` shares the count defect, and warned that if it does,
"every ratio in Remaining is optimistic". **Checked at this review. It does not, and they are not.**

- The coordinator's figure is reproducible: a kana+kanji-only regex `[぀-ヿ一-鿿]` over this
  batch's 26 keys returns **exactly 1,770**, against the true **1,980** — a 210-character, **10.6%**
  under-count, and it is **entirely** 66 `。`, 53 `、`, 40 `　` and the full-width Latin and digits
  (`ＺＯＣ`, `ＥＮＴＥＲ`, `９`), every one of which costs 2 bytes and 1 column like any other
  character.
- **`tools/queue.py` uses `len(re.sub(r'\{[^}]*\}', '', …))` at lines 46, 124, 199 and 219** — the
  strip-tags-and-count method, which returns 1,980. Every JP-char figure and every budget ratio
  `queue.py` prints, for both the battle queue and the script batching, is computed the correct way.

**Wave 3 does not owe this check — it is discharged here.** The Remaining table is sound. The
lesson that survives is narrower and still worth keeping: **never count Japanese characters with a
kana/kanji class.** Full-width punctuation and layout spaces are 8–12% of a typical line and cost
exactly what letters cost.

### N4. Deviations from literal (§2.1 steps 5–6) — the complete list

Flag 6 lists three step-6 clause reorders (988 p3, 999, 984 p3) and they are correct as written.
Flag 7 lists eight step-5 implications. **Two more of the same pattern were found at review and are
recorded here rather than sent back for a third round**, on the §M5 / §M6 practice — the
translations are right and the rule is already stated in Flag 7 item 5; only the itemisation was
short. **Ten in total:**

| Line | Japanese | English | What is elided |
|---|---|---|---|
| 985 p3 | `キャラを有用にするも無用にするも使い方次第じゃな` | `Ｕｓｅｆｕｌ　ｏｒ　ｕｓｅｌｅｓｓ　ｉｓ　ｕｐ　ｔｏ　ｙｏｕ．` | the subject *a character*, established two pages earlier |
| 985 p2 | `前衛に重剣士、後衛に魔術師` | `ａ　ｈｅａｖｙ　ｓｗｏｒｄｓｍａｎ　ｉｎ　ｆｒｏｎｔ　ａｎｄ　ａ　ｍａｇｅ　ｂｅｈｉｎｄ` | the fixed *front line* / *rear line*; `ａ　ｍａｇｅ　ｔｏ　ｔｈｅ　ｒｅａｒ　ｃｏｖｅｒｓ` is 25 columns |
| 985 p2 | `魔術師の弓に弱いという欠点` | `ｉｔｓ　ｗｅａｋｎｅｓｓ　ｔｏ　ｂｏｗｓ` | the repeated *the mage's* → *its*; 欠点 carried by *weakness* |
| 990 | `さっさと任務についたらどうだ？` | `ｗｈｙ　ｎｏｔ　ｒｅｐｏｒｔ　ｔｏ　ｙｏｕｒ　ｐｏｓｔｓ？` | さっさと, carried by the brusque question |
| 994 p3 | `どうやら…らしい` | `ｉｔ　ｓｅｅｍｓ` | one of two stacked hedges — English has one slot |
| 994 p4 | `今のうちに、早く　逃げよう。` | `Ｌｅｔ’ｓ　ｇｅｔ　ｏｕｔ　ｗｈｉｌｅ　ｗｅ　ｃａｎ．` | 早く, carried by *while we can* |
| 995 | `全滅させられたらしい` | `ｆｅｌｌ　ｔｏ　ｔｈｅ　ｒｅｂｅｌｓ` | 全滅 and the causative-passive compressed; the page is 2.18× at the 4-row wall |
| 995 | `全く、イヤな話だよ。` | `Ｒｅａｌｌｙ，　ｆｏｕｌ．` | 話; §6's まったく → `Ｒｅａｌｌｙ，` kept in full |
| **1000** | **`何でも、…らしいぜ`** | **`Ｗｏｒｄ　ｉｓ　…`** | **ADDED AT REVIEW.** The same stacked sentence-initial adverb + sentence-final evidential as 994 p3, collapsed into one hedge |
| **1001** | **`何でも、…だとか言ってたから`** | **`Ｈｅ　ｓａｉｄ　…`** | **ADDED AT REVIEW.** Same collapse, with the reported-speech frame doing the work |

Two further judgements accepted at review without a flag, recorded so nobody re-opens them:
**992's `誘拐した` → `ｔｏｏｋ`** (the crime is carried by `ｃｕｌｐｒｉｔ` and `ｈｏｌｅｄ　ｕｐ`;
`ａｂｄｕｃｔｅｄ` would in fact have fitted at 17 / 21 / 19, so this is a choice, not a forced cut —
it is idiomatic English for an abduction and drops no plot fact), and **987's `逆もしかりじゃ、` →
`Ｔｈｅ　ｒｅｖｅｒｓｅ　ｈｏｌｄｓ　ｔｏｏ：`** (a `、` rendered as `：`, which is §3.1-legal; the
source's punctuation is otherwise followed throughout, and the dot-count rule governs ellipses).

### N5. One arithmetic claim in the PR body is wrong — the rendering is not

Same shape as §M5. The finding-2 row says `ａｎｄ　ｒｅｂｕｉｌｄ` "would put row 3 at exactly 24".
Re-measured: `Ｆａｔｈｅｒ　Ｂａｔｏｕ’ｓ　ｗｉｌｌ　ａｎｄ` is **23** and `ｒｅｂｕｉｌｄ　ｔｈｉｓ　ｃｈｕｒｃｈ．`
is **21**, so `ａｎｄ` would have fitted. **The `ｂｙ` stands on its merits regardless**: `ついで` is a
て-form of means, and `ｂｙ　ｒｅｂｕｉｌｄｉｎｇ` renders that subordination where the coordinate
`ａｎｄ` would flatten it. Only the justification is corrected. Every other figure in the PR body was
re-derived and is exact, including the two corrections the translator made to this reviewer's own
round-1 estimates (+10 → **+8**, +14 → **+12**), which are right.

### N6. Two English hearsay frames for one Japanese evidential

Recorded in glossary §26.6; not a §3 violation, because §3 engages on the message and all four
messages differ (§20.4, §23.1, §24.5). `ｔｈｅｙ　ｓａｙ` is the default and is also §25.2's fixed form
for `〜ってウワサだ`; `Ｗｏｒｄ　ｉｓ` is the sentence-initial variant. Fixed now so it cannot drift.

### N7. In-game checks requested by this unit

1. **Script 987 page 2 ends mid-sentence** (`…ユニットには、`) with the predicate arriving on page 3
   after the `{FCC0}`. Preserved verbatim — a translator cannot move a `{FCC0}` — but it looks like
   a source authoring slip. Worth an eye alongside §D2.
2. **`バカとハサミは使いよう` → `Ｉｔ　ｉｓ　ａ　ｐｏｏｒ　ｗｏｒｋｍａｎ　ｔｈａｔ　ｂｌａｍｅｓ　ｈｉｓ　ｔｏｏｌｓ`**
   (glossary §26.4) is the loosest of this batch's three proverbs: both locate the outcome in the
   user rather than the tool, but the Japanese encourages where the English chides. Accepted
   because the page is at the 4-row wall (21 / 23 / 20 / 23) and the following sentence restores
   the constructive sense. If it reads wrong on screen, the fix needs a re-cut of the page, not a
   word swap.
3. **The old tutor (984–988) is never named or given a portrait in these five messages.** The
   register row in glossary §26.7 keys on his speech (`じゃ` / `のじゃ` / `じゃろ`). If a later unit
   names him, re-check it — cf. §G4, §H1, §L6.

### N8. Rulings this review makes that bind later units

1. **`将軍` → `Ｇｅｎｅｒａｌ`** (glossary §26.2). Discharges §9's correction 2 on a corpus count of
   17 against 2, with all three shipped `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ` traced to `隊長` sources.
   Bare `２軍` → `２ｎｄ　Ａｒｍｙ`, not §20.1's `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ`. **Note: §10 question 2,
   the class/unit name table, is a different item and is still open.**
2. **`バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ`** (glossary §26.1). §24.1 is **applied, not amended**;
   §21.2's drop-the-honorific rule reaches `〜さん` on a personal name and nothing else. The `様`
   and `さん` patterns stay separate.
3. **`砦` → `ｆｏｒｔ`** (glossary §26.4), leaving 要塞 / 大要塞 / 空中要塞 as three other words.
   `tl/battle/chunk_040.txt` already ships both `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` and `ｔｈｅ　Ｆｏｒｔ`.
4. **`助かりました` → `Ｙｏｕ　ｓａｖｅｄ　…`** as a third row of §23.4 (glossary §26.8), governing
   9 occurrences across both dumps. `chunk_001` line 14's queued correction is unaffected.
5. **`リース文明` ≠ `古代ハイランド`** — zero lines in either dump contain both. Both rows stay.
6. **`アップミーズ` → `Ａｐｕｍｉｚｕ`, a town.** Two new §9 seeds fell out of verifying it, on the
   `クロスリー` precedent: **`ホアグ王子` → Prince `Ｈｏａｇ`** (6 battle + 16 script; Cavia's elder
   brother, who built Apumizu) and **`トリフ` → `Ｔｏｒｉｆ`** (9 battle + 6 script; his younger
   brother, Helfer's preferred heir). Neither was in `glossary.md` at all; neither is rendered yet.
7. **`ファリーナ` was NOT moved again.** Flag 2 asked for it; §9's correction 1 is already struck
   ✅ DISCHARGED by PR #6's review, with the standing instruction that PRs #7 and #8 must not move
   it a second time. The row sits in §2, `Ｆａｒｉｎａ` is unchanged, and this unit uses it correctly.
   §K6's "moved once, for the whole wave" held for all three units that flagged it.
8. **glossary §11.2's `フェリスランド` note was factually wrong** and is corrected in place —
   13 occurrences, not zero. Rendering unchanged, nothing revisited.

---

## O. Wave 3 review — corrections/audit-wave1 / PR #9 (2026-09-08)

Merged round 1, **MERGE**, all eight gates green on evidence re-derived at review rather than
inherited from the PR body. Glossary rows and two §4.3 corrections in `glossary.md` §27.

### O1. The byte figures, and the banks

**chunk 1: 3,519 / 8,192 — 4,673 slack. chunk 2: 5,855 / 8,192 — 2,337. chunk 3: 4,605 / 8,192 —
3,587. chunk 34: 1,587 / 8,192 — 6,605 (−4).** Widest row in the unit **23**, none at 24.

**`chunk_000.txt` and `chunk_007.txt` are byte-for-byte untouched** — identical blob hashes on
both sides of the diff (`845870f…`, `6aff068…`). Chunk 0 stays at **27 bytes of slack** (§G1) and
chunk 7 at **399**.

**⚠️ `batch_004` spends 38 bytes in each of 21 banks. Bank 40 is now at 471 free, not 509.**
Verified by diffing `bankmeasure` between the base tree and the merged tree: exactly 21 banks
moved (2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 25, 33, 40, 42, 43), each by
exactly **−38**, no bank negative.

| bank | §J2 recorded | **now** |
|---|---|---|
| **40** | 509 | **471** |
| 41 | 353 | **353 — still untouched**, the table does not land there |
| 5 | 3,419 | **3,381** |
| 2 | 7,543 | 7,505 |
| 33 | 9,353 | 9,315 |

**§J2's table is superseded by this one** for banks 40, 5, 2 and 33. **§J1's corrected arithmetic
still fits, with a thinner margin:** restoring `持つ者に` on all six `〜守護をもたらす` entries
costs 192 bytes at the corrected 32 B/entry, leaving bank 40 at **279 free** rather than 317.
Both this PR and that restoration remain affordable together, but little else is, and §J2 already
declares bank 40 closed to further batches. **The next bank-40 decision must be made against 471.**

### O2. The tag stream did not move, and this is the second zero-re-flow unit

`rowcheck` run against the working tree and against the base blobs prints **identical
`{FFFE} changed:` lists** for all four chunks, differing only in the byte figure. No break was
added, deleted or moved; no `{FCC0}` was touched; no insert repositioned. Gate 4's
`{FFFE}`/`{FCC0}` clause is genuinely vacuous for this unit, which is what makes a twelve-edit
correction pass across four merged files cheap to verify.

### O3. `tl/battle/` is free of divergent duplicate renderings for the first time

The live CLAUDE.md §3 violation the wave-1 reading review found in §9 is **closed**. Method and
figures, re-derived at review by pairing each shipped chunk positionally against
`dumps/battle_dump.txt` (equal line counts by construction, split at `{FC30}`, tags stripped), run
at two granularities as a cross-check:

```
BEFORE  [{FC30}-turn] distinct=354 recurring=13 DIVERGENT=1
        [whole-line ] distinct=123 recurring=6  DIVERGENT=1
           JP: 村が襲われました。
             chunk 007 L26 / L27  Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ // ｕｎｄｅｒ　ａｔｔａｃｋ．
             chunk 034 L8         Ｔｈｅ　ｖｉｌｌａｇｅ　ｈａｓ　ｂｅｅｎ // ａｔｔａｃｋｅｄ．
AFTER   [{FC30}-turn] distinct=354 recurring=13 DIVERGENT=0
        [whole-line ] distinct=123 recurring=6  DIVERGENT=0
```

Script side: **211 unique JP keys across all five TSVs, 0 duplicated keys, 0 divergent.**

The binding rendering is `glossary.md` **§27.2** — `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　
ａｔｔａｃｋ．`, 13 dump instances, **ten still untranslated** (chunks 5, 13, 15, 16 ×2, 17, 21, 23,
38, 39). ✅ Both wave-3 siblings already carry it byte-for-byte, checked on their branches at this
review: `tl/battle/chunk_013.txt` L8 (PR #10) and `pending/chunk_017.txt` L21 (PR #12).

⚠️ **`chunk_006.txt` L15 is NOT a fourth instance** — its source is `村が　襲われました。` with a
full-width space, a hapax, and `glossary.md` §24.6 wrongly called it the same string. Corrected in
**§27.4**; no rendering changes. Anyone re-running a duplicate check by eye, or with a tool that
normalises whitespace, will hit this.

### O4. Gate 6's method note, restated because §L5 is still recent

A battle `tl/chunk_NNN.txt` holds **zero Japanese**, so grepping a unit's Japanese against `tl/`
returns "clean" unconditionally — that is the null check §L5 records. Positional pairing against
the dump is the replacement and is what ran here. The script check *is* a key comparison, which is
valid only because the TSVs keep the Japanese in column 2.

### O5. `glossary.md` §22.1's 火炎剣 gloss was superseded, and the PR said nothing was

PR #9's Glossary-additions table proposed `焼き尽くす` → `ｂｕｒｎ　…　ｔｏ　ａｓｈ` with its reason,
so the change was not silent and gate 7 passes — but the body's "Nothing existing was changed" is
inaccurate: §22.1's `火炎剣` row documents `すべてを焼き尽くす` → *burning all up*, which edit 2
replaces. Written out as a §4.3 correction in **§27.3**, with the single affected line named.
Verified complete at review: `焼き尽く` occurs **1 battle (chunk 15, untranslated) / 21 script
(one unique line × 21)**, so `batch_004` L17 is the only rendering in `tl/`.

Related, and corrected when copying the row into the glossary: the PR body and
`audits/wave1-reading-review.md` both say "**13 occurrences** of 愛用 remain untranslated". 13 is
the **total** number of unique lines containing 愛用 (273 dump instances ÷ 21); four are now
rendered, so **9 remain — 189 message instances**. §27.1 carries the corrected figure and names
the nine.

### O6. A break placement in `batch_004` L12 — a proposal, deliberately NOT applied

`Ａ　ｃｏｍｍｏｎ　ｓｗｏｒｄ　ｍａｎｙ{FFFE}ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ．` (19 / 16) splits the noun
phrase `ｍａｎｙ　ｓｏｌｄｉｅｒｓ`, so row 1 ends on a bare quantifier. That is the same class of
defect edits 4, 7+8 and 10 of this very unit exist to remove, and
`Ａ　ｃｏｍｍｏｎ　ｓｗｏｒｄ{FFFE}ｍａｎｙ　ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ．` is **14 / 21 at identical
bytes**.

**Not applied, and not asked of the translator.** The shipped form is
`audits/wave1-reading-review.md` item 3's own verbatim proposal; §3.2's two *hard* rules (break at
a word boundary; no row ending in a lone one- or two-letter word) are both satisfied, and only the
"prefer clause boundaries" preference is at stake; and §J2 closes bank 40 to further batches, so
the row will not be reopened soon. Recorded here for whoever next touches `batch_004` — if the
column-width table is ever re-cut after a bank-40 repoint, take this with it.

For contrast, the dangling `ｔｈｅ` at the end of row 1 on L29 and L42 is **forced, not a choice**:
moving it down puts row 2 at 26 columns. Those two stand as shipped.

### O7. ⚠️ Wave-1 audit finding 7 is STILL OPEN — carried forward with evidence, not discharged

`audits/wave-1-audit.md` finding 7: five entries PR #1 proposed for glossary §21 were dropped at
integration with no note of rejection. **Checked against the current `glossary.md` at this review.
Four and a half are still open**; all five are rendered in shipped work and fixed nowhere.

| Entry | Status | Shipped as | Corpus |
|---|---|---|---|
| `ヘビー` → `ｈｅａｖｙ` | **absent** | `ａ　ｂｉｔ　ｈｅａｖｙ`, `chunk_003` file L6 | 1 battle / 0 script |
| `洞窟` / `赤い屋根の家` / `赤い屋根の建物` | **absent** | `ｃａｖｅｓ` / `ｒｅｄ‐ｒｏｏｆｅｄ　ｈｏｕｓｅｓ` / `ｒｅｄ‐ｒｏｏｆｅｄ　ｂｕｉｌｄｉｎｇｓ`, all `chunk_003` file L6 | 洞窟 5 battle, 赤い屋根 2 battle |
| bare `隊` → squad | **absent** | — | — |
| `謹慎中` → `ｕｎｄｅｒ　ｃｏｎｆｉｎｅｍｅｎｔ`, `謹慎がとける` → `ｃｏｎｆｉｎｅｍｅｎｔ　ｅｎｄｅｄ` | **half open** — §19.2 records only the adjective `ｃｏｎｆｉｎｅｄ` | `ｕｎｄｅｒ　ｃｏｎｆｉｎｅｍｅｎｔ` and `ｍｙ　ｃｏｎｆｉｎｅｍｅｎｔ｜ｅｎｄｅｄ`, `chunk_003` file L5; `ｃｏｎｆｉｎｅｄ`, `chunk_001` L6/L7 | 4 battle / 1 script |
| `さあ` → `Ｃｏｍｅ　ｏｎ，` | **partially discharged**, by §24.5's note and §24.6's Fernando row (`さあ、` → `Ｎｏｗ，`), but with **no table entry** | `Ｎｏｗ，` in `chunk_006` L13 and `chunk_033` L21; `Ｃｏｍｅ　ｏｎ，` still on `chunk_003` L4's `さあ、{FC00}{=0000}、` row | **16 battle / 10 script** |

**Not this unit's remit and not a defect in it** — PR #9 flagged the item explicitly (its Flag 9)
rather than letting it lapse, which is why it is still visible. **Whoever owns the next glossary
integration should either write these five rows or record the rejection in terms.** It has now
survived two waves; the third time it disappears it will be gone for good, and `さあ、` alone is
26 occurrences of drift risk.

### O8. Two dispatch errors the translator caught, both correctly

Recorded because both are the shape §M2 and CLAUDE.md's "findings are proposals" rule exist for.

1. **The dispatch's re-flow instruction for edit 5 was wrong and was declined with a
   measurement.** `Ｈｏｗｅｖｅｒ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` lands at **21 columns** (from 19), inside
   the ≤ 23 preference, page still 4 rows (21 / 20 / 22 / 12). Re-measured at review: correct.
   Re-flowing would have churned the tag stream for nothing and forfeited §O2. The dispatch
   generalised from wave 2's chunk 9, where the word landed on a page already at the 4-row wall.
2. **A line number in the dispatch was wrong.** Edit 9 is `chunk_002` **file line 14**, not 15 —
   file line 14 is the one carrying `すみません。{FFFE}ありがとうございます。`, and
   `audits/wave1-reading-review.md` item 1 says L14 too. Located by content, as instructed. No
   other target was off. ⚠️ **The two audits and the glossary number these lines three different
   ways** (raw file lines, message lines = file − 1, and glossary §23.3/§23.4's message lines).
   Any future unit acting on them must locate by content.

### O9. Scope was widened by one edit and it was reported, not slipped in

The dispatch's eleven and `HANDOFF.md`'s eleven were **different elevens**; PR #9 applied the
**union, twelve**, and said so in its own body before anyone asked. The twelfth is
`chunk_001.txt` file L15 (glossary §23.4's `助かった` correction, **0 bytes**), whose warrant is
§23.4's own sentence *"Added to the wave-3 corrections unit; not applied at review"* rather than
the dispatch. Accepted at review: it is in a file the unit already opens, gate 1's five-path list
is unchanged either way, and the alternative was to leave a glossary ruling unapplied with no
owner. The unit also offered edits 2/3/4 as separately parkable (leaving `batch_004` at +14 B/bank)
and edit 12 as separately revertible; neither lever was used.

---

## P. Wave 3 review — battle chunk 13 / PR #10 (2026-09-08)

Merged **round 1**, **MERGE**, all eight gates green on evidence re-derived at review rather than
inherited from the PR body. Glossary rows, three §9 description/width corrections and the
discharge of §O7 are in `glossary.md` **§28**.

⚠️ **Line numbers below are MESSAGE lines** (dump body index, 1-based) = `tl/` file line − 1,
because the `=== CHUNK` header is kept. `HANDOFF.md` called the village-attack line L8; it is
message line **7**. Same row. Third numbering convention in this repo (§O8) — locate by content.

### P1. The byte figure

**chunk 13: 5,417 / 8,192 — 2,775 slack.** 132 text rows, **widest 23, none at 24**, no page over
4 text rows. Ratio 3.41, so §3.3's ≥ 50-byte floor is never in play; the binding constraint was
geometry, and the PR is right about that — 1,092 JP characters became 2,353 English columns,
**2.15×** against a 3.41 ceiling.

Column and row figures were re-derived independently of `rowcheck`, splitting rows at `{FFFE}`
**and** at `{FCC0}`/`{FC30}`/`{FC51}`/`{FC50}`/`{FFFF}` with the name insert counted as 7:

```
TOTAL TEXT ROWS: 132   widths 4..23   max 23   rows at 23: 11   rows at 24+: 0
```

### P2. The tag stream — and a correction to the PR's own Flag 2

`{FCC0}`: **dump 19 → file 19, unchanged.** No page break added or removed anywhere, as claimed.
The four `{FFFE}` deltas are exactly as flagged (L1 12→13, L4 37→36, L7 0→1, L8 24→23), and each
is justified by geometry I could reproduce.

⚠️ **Flag 2 says "L2, L5 and L6 are byte-for-byte unchanged in their tag streams". That is right
for L5 and L6 and wrong for L2.** L2's `{FFFE}` **count** is unchanged at 12 — which is all
`rowcheck` reports, since it diffs counts — but one break moved **out of** page 2 (`情報では、
カーライン軍は…` goes 4 rows → 3) and one moved **into** page 6 (`あれは、９軍？…` goes 2 → 3), so
its full tag *order* differs from the dump. Comparing complete tag sequences line by line, the
lines genuinely byte-identical to the dump are **L3, L5, L6, L9, L10, L11**.

**The re-flow itself is correct and legal; only the claim is off.** Recorded because §27.2's
reviewer verified this branch by reading it and the next auditor will too — and because a
count-only check cannot see a moved break. A reviewer who wants position identity must compare
the whole tag list, not `rowcheck`'s `{FFFE} changed:` line.

### P3. Gate 6 — the method, and the §27.4 trap sprung in practice

Battle `tl/` files hold **zero** Japanese, so grepping a JP string against `tl/` is a null check,
not a pass. Each shipped chunk was paired positionally against `dumps/battle_dump.txt` (equal line
counts by construction) at two granularities:

```
MESSAGE granularity: 129 distinct JP keys, 0 divergent
PAGE    granularity: 517 distinct JP keys, 0 divergent
```

**Page granularity is the load-bearing one for this unit**, because it is stable under `{FFFE}`
re-flow and sub-page granularity is not: chunk 13 re-flows L1, L4, L7 and L8, and a segment-level
scan mispairs every row after a moved break. It produced a spurious `はっ！` → `Ｈｏｗｅｖｅｒ，`
mapping on L2 before the method was corrected. **Any future duplicate check on a re-flowed unit
must split at page boundaries, or skip the re-flowed lines and say so.**

⚠️ **§27.4's predicted false positive occurred, exactly as written.** The first page-level pass
normalised `　` out of the JP key and reported one divergence — chunk 6's **spaced**
`村が　襲われました。` collapsing onto the unspaced string that §27.2 governs. With exact keys the
count is **0**. §27.4 is correct, chunk 6 stands, and the warning has now been vindicated by an
actual tool rather than anticipated.

Chunk 13's two recurring pages, both byte-identical to shipped work:

| JP | EN | where |
|---|---|---|
| `村が襲われました。` | `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．` | c7 L25, c7 L26, **c13 L7**, c34 L7 |
| `くっ・・・` | `Ｔｃｈ．．．` | c0 L19, c7 L11, **c13 L1** |

All five sub-page reuses in the PR's own gate-6 table verified true, including the one that looked
false: `いいか、` **is** in `chunk_000.txt` L3 and **does** ship `Ｌｉｓｔｅｎ，`; the segments
mispair there because chunk 0 L3 is itself re-flowed.

**Cross-PR**, against the live sibling branches `tl/battle-008` (#11) and `tl/battle-017` (#12) at
page granularity: **0 divergences.** `村が襲われました。` matches c17 L20; `はっ！` → `Ｓｉｒ！`
matches c8 L10 and c17 L6. None of chunk 13's 24 new terms collides with anything either sibling
renders, and `ｒｏｕｔｅ` (the shared wave-3 seed) does not occur in chunk 13 at all.

**Both King's-speech variants are byte-identical** — 365 characters including tags, and the JP
source is identical too. (The PR body's "383 characters" is the only figure in it I could not
reproduce; the substance holds.)

### P4. ⚠️ `指揮下` — the one proposal that would have caused real drift

`glossary.md` §28.2 carries the corrected entry. In short: the PR proposed
`指揮下に入る` → `ｓｅｒｖｅ　ｕｎｄｅｒ` with "**6 battle occurrences** … this binds forward".
Counted at review, `指揮下` is 6 but `指揮下に入る` is **one** — chunk 13's own line — and **two of
the six are already shipped, both rendering `ｃｏｍｍａｎｄ`**:

| where | JP | shipped EN |
|---|---|---|
| `chunk_007.txt` L11 | `黒の騎士団の指揮下だ。` | `ｕｎｄｅｒ　ｏｕｒ　ｃｏｍｍａｎｄ．` |
| `chunk_014.txt` L3 | `第９軍の指揮下に` / `入ります。` | `ｕｎｄｅｒ　ｔｈｅ　ｃｏｍｍａｎｄ　ｏｆ` / `ｔｈｅ　９ｔｈ　Ａｒｍｙ．` |
| **`chunk_013.txt` L8** | `君の指揮下に入ろう。` | `Ｉ　ｗｉｌｌ　ｓｅｒｖｅ　ｕｎｄｅｒ　ｙｏｕ．` |

Chunk 7's is also the **enemy's** chain of command, not "a squad member joining the player".
**CLAUDE.md §3 is not engaged** — three different source strings in three different messages
(§20.4, §23.1, §24.5, §27.4) — so **nothing is re-cut**, and chunk 13's rendering is width-forced:
`ｃｏｍｅ　ｕｎｄｅｒ　ｙｏｕｒ　ｃｏｍｍａｎｄ．` measures **24** columns (the PR body's 26 is two over,
remeasured here) on a page already at 10 / 22 / 11 / 23. All three share `ｕｎｄｅｒ`, so the family
reads as one.

**Recorded as one default plus one stated variant, the §26.6 `らしい` shape.** Left as the PR wrote
it, chunk 19's translator would read "this binds forward", render `ｓｅｒｖｅ　ｕｎｄｅｒ` three times
for `では、俺たちの指揮下に入ってもらう`, and fork the word against two shipped files in a chunk
that has room for `ｃｏｍｍａｎｄ`. **Chunk 19 should use `ｃｏｍｍａｎｄ`.**

### P5. Two English forms shared with shipped work, both accepted under §25.3

Neither is a CLAUDE.md §3 violation and neither changes a rendering; both are recorded so they
cannot drift, because in each case the PR's own note asserted a distinctness that does not hold.

| chunk 13 | shares its English with | verdict |
|---|---|---|
| `何っ！？` → `Ｗｈａｔ！？` | `chunk_007.txt` L2's **katakana** `何ッ！？` → `Ｗｈａｔ！？` | **Accepted.** One full-width character apart, so different lookup keys — the §24.5 / §27.4 shape. And it is the *documented* collapse: one word, two kana spellings, which §6 already does for 何だと？ / なんだと？. §25.3's test is met — `何ッ！？` is chunk 7 only, `何っ！？` is chunks 13 and 18, **no chunk holds both**. The PR's "a sixth member … all held apart" is corrected in §28.3; chunk 7 has first use |
| `あいにく` → `Ｓｏｒｒｙ，` | `chunk_010.txt` L10 and L12's `ごめんね、トカゲさん。` → `Ｓｏｒｒｙ，　Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ．` | **Accepted.** Two different source words, §25.3's test met (chunks 10 and 13 never meet), and the alternative is width-blocked: `Ｕｎｆｏｒｔｕｎａｔｅｌｙ，` is 16 and puts that row at 28. The PR's note held `あいにく` apart only from 残念ながら; recorded in §28.3 |

### P6. Corpus counts remeasured — five slips, none affecting a rendering

| entry | PR body | remeasured at review |
|---|---|---|
| `指揮下に入る` | 6 battle | **1** battle (`指揮下` is 6) — §P4 |
| `レバーク` | 1 battle + 10 script | 1 battle + **13** script-unique |
| `ルクレール` | 1 battle + 4 script | **2** battle + 4 script-unique |
| `国王` | 4 battle + 10 script | **6** battle + **21** script-unique |
| `アーバイン様` (§9 seed, not the PR) | 7 bare / 12 with title | **6** bare / **11** with title |

`ははっ` at 5 battle + 1 script-unique is **correct as written** when read as the tic under §5's
word-plus-source-punctuation mechanism (`ははっ・・・・！！` ch 16, `ははっ！！` ch 37,
`はははっっ！！` ch 38, `ははっ・・・・` ch 42); the exact string `ははっ！` is 2 battle. Counts
matter here because two of them (`レバーク`, `指揮下`) are the reach figures a future translator
would act on, and in both cases the true figure argues *more* strongly for the decision taken.

### P7. ⚠️ The `アーバイン様` seed was the orchestrator's and it was wrong

`glossary.md` §9's wave-3 seed said "**7 columns bare, 12 with the title**". Both are one too many:
`Ｉｒｖｉｎｅ` is **6** and `Ｌｏｒｄ　Ｉｒｖｉｎｅ` is **11**. The translator caught it in its own
additions table; remeasured at review on the shipped row (`Ｌｏｒｄ　Ｉｒｖｉｎｅ！` = 12 with the
mark) and confirmed. **The rendering is unchanged and nothing is re-cut** — only the width figure
was wrong, and it would have mattered the first time someone tried to put the title on a shared
row. §9's row is struck and corrected; §28.1 carries the right figures.

**This is the second wave-3 seed error the translator caught** (`ルクレール` and `レバーク`
described as castles when both are kingdoms — §28.1). Seeds are written fast by the orchestrator
against a grep; treat their *widths and descriptions* as provisional even where the *form* is
sound, which is what §9's own preamble already says.

### P8. Ten pages carry a leading blank plus four text rows — glossary §10.4 again

Chunk 13 has **ten** pages shaped `{FCC0}{FFFE}` + 4 text rows. `glossary.md` §10.4 records that
whether the leading break wastes a top row is unconfirmed, and §3.2 of the prompt says a page with
a leading blank *and* four text rows *and* a trailing blank "has never appeared in the source and
may not fit". None of chunk 13's ten has a trailing blank as well, so none is the untested shape —
but ten instances in one chunk is the largest concentration so far, and **this chunk is a good
candidate for the in-game check §10.4 has been waiting for.** Every one of the ten is inherited
from the source's own page division: gate 3's tag parity excludes only `{FFFE}`, so a `{FCC0}`
cannot be added even where §3.2 invites one, and every page had to fit the division the dump
already had. Message line 8 pages 3, 5 and 6 (41, 43 and 40 JP characters in four rows) set the
tightness of the whole unit.

### P9. The King is unnamed and his kingdom unstated — the English commits to neither

The rescued King says only `私は、この国の国王です`. Message line 8 establishes that the map is
Leclerc and that its King is a captive, so the likeliest reading is that this is the same King
after the rescue — **but the chunk never says so, and Cress leaves for `Ｌｅｖｅｒｋ`, a different
kingdom.** `ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｉｓ　ｌａｎｄ` and `ｏｕｒ　Ｋｉｎｇ　ｏｆ　Ｌｅｃｌｅｒｃ` each render
exactly what their own line says and nothing more, which is the right call for an ambiguity the
source declines to resolve. **Worth an in-game look on the same pass as §P8 and the other map
checks.** If a later chunk names him, the two lines are 21 and 20 columns and both have room.

### P10. `さんざんいたぶった後` / `上玉` — sexual menace, rendered at the source's temperature

Message line 1 page 4. Recorded in `glossary.md` §28.4. The PR raised it itself rather than
leaving the decision silent, and the decision is ratified: neither softened nor sharpened, with
`上玉` → `ｔｈｅ　ｐｒｉｚｅ` chosen to keep the objectification the scene turns on. Flagged here so
that anyone who meets the line later finds a decision rather than an accident.

### P11. One line of finding withdrawn on measurement

The review opened a finding on rows ending in a short function word — `Ｗｈｏｓｅ　ｓｏｌｄｉｅｒ　Ｉ
ａｍ　ｉｓ`, `ｈｅｌｄ　ｃａｐｔｉｖｅ，　ｗｉｌｌ　ｂｅ`, `Ｔｒｕｌｙ，　ｗｈａｔ　ｙｏｕ　ｓａｙ　ｉｓ` — against
§3.2's "do not leave a line ending in a lone one- or two-letter word if it can be avoided". Each
had a free zero-byte re-split. **Withdrawn after counting the corpus**: it is unanimous house
practice, not a chunk-13 defect.

```
short (<=3 letter) row-final words, per shipped chunk
  c0 68   c7 55   c6 47   c13 44   c2 43   c1 30   c3 30   c4 30   c9 29
  c14 18  c10 14  c33 12  c12 10   c11 7   c34 7   c35 3   c40 1
```

31–33% of rows in **every** substantial file, and §27.2's own binding message
(`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．`) ends a row on `ｉｓ`. Chunk 13's 44 in 132 is
mid-distribution. **§3.2's "if it can be avoided" is read in this project as "where it does not
cost a worse break", and that reading is now recorded** so the next reviewer does not re-open it
per-chunk. A finding here would have put one file out of step with sixteen.

### P12. §O7 is DISCHARGED

`FLAGS.md` §O7 handed five dropped wave-1 glossary rows to "whoever owns the next glossary
integration". That was this integration, and chunk 13 renders one of them, which is what settled
it. Four rows are written in `glossary.md` **§28.8** (`さあ、` → `Ｎｏｗ，`; `ヘビー`; `洞窟`;
`赤い屋根の家` / `赤い屋根の建物`; `謹慎中` / `謹慎がとける`), and the fifth — bare `隊` → squad —
is **rejected in terms**, as §O7 allowed: it has no shipped rendering and no occurrence to point
at, so there is nothing to fix.

**`さあ、` → `Ｎｏｗ，` is the one that mattered**: 16 battle + 10 script-unique occurrences, and
chunk 13 is the **third** shipped file to agree (`chunk_006` L12, `chunk_033` L20). The two
row-level variants stand and are **not** re-cut — `chunk_011` L3's `さあ、私のかわいい` →
`Ｎｏｗ　ｔｈｅｎ，　ｍｙ　ｄａｒｌｉｎｇ`, and `chunk_003` L4's `さあ、{FC00}{=0000}、` →
`Ｃｏｍｅ　ｏｎ，　{FC00}{=0000}，`, which §24.5 already rules is a different row.

### P13. No source typos

The PR checked this programmatically per segment rather than by eye and reports none; re-derived
at review. `{PAD 5269}`, `{=FF}` and the `=== CHUNK 13 @ 0x228800  script 0x24D800..0x24E36B
headroom 5269` header are byte-identical to the dump; every message ends with `{FFFF}`; every
ellipsis run matches the source's own mark count, paired run by run rather than by totals — L1
3→3, L2 3,3→3,3, L4 7,4,3,5→7,4,3,5, L5 5→5, L8 5→5. Zero characters outside §3.1, zero ASCII,
no `…` `・` `○` `'` `"`. No menu options in this chunk, so no `　` gutter to preserve.

---

## Q. Wave 3 review — battle chunk 8 / PR #11 (2026-09-08)

Merged at **round 2**, **MERGE**, all eight gates green on evidence re-derived at review rather
than inherited from the PR body. Round 1 was **CHANGES** on two reading findings, both applied;
the rework was **byte-neutral**. Glossary rows, the `Ｒｉｇｈｔ，` collision ruling, four §9
promotions and a §4.3 column correction are in `glossary.md` **§29**.

⚠️ **Line numbers below are `rowcheck` line numbers** — the `tl/` file index counting the
`=== CHUNK` header as line 0, i.e. the convention `rowcheck.py 8` prints. That is a **fourth**
numbering scheme in this repo (§O8, §P): chunk 13's message lines are this minus one. Locate by
content, not by number.

### Q1. The byte figure

**chunk 8: 7,437 / 8,192 — 755 slack**, unchanged across the rework. 185 text rows, **widest 23,
twenty at 23, none at 24**, no page over 4 text rows. Ratio 2.32 (tier B), so §3.3's ≥ 50-byte
floor was never in play; **every compression in this unit was forced by 24 columns × 4 rows, not
by the slot** — which is the same verdict tier E reached and the reason §0.2's warning about high
ratios applies here too.

The rework cost nothing: the added `{FFFE}` on L10 is +2 bytes and the inter-sentence space that
became a row boundary is −2. `{FCC0}` is **unchanged on every line** (L4 3, L9 4, L10 4, L14 1,
L15 3; whole-chunk total 15 → 15); `{FFFE}` moved on five lines only — L4 35→34, L5 3→4,
L9 54→51, L10 29→30, L15 25→24. Every non-`{FFFE}` tag is identical element for element on all
20 lines.

### Q2. ⚠️ TOOLING DEFECT FOR A HUMAN — `translation_prompt.md` tells translators to add a `{FCC0}`, and both gates reject it

**This is the finding that outlives the PR, and it is not a defect in the PR.** Verified
independently at review against the source, not taken from the PR body.

The prompt licenses adding a page break in **four** places:

- **line 248** — “`{FCC0}` … You may add one when English overruns the visible rows”;
- **line 361** — “If English needs a fifth line, insert a `{FCC0}` page break”;
- **line 373** — “Four rows is the wall. When four rows of 23 will not hold the page, add a
  `{FCC0}` rather than cutting sense”;
- **line 520** — the FLAGS template asks the translator to report “lines that needed an added
  `{FCC0}`”.

**Both gates reject it.** `tools/assemble.py:125-126` and `tools/rowcheck.py:93-94` build the tag
parity list as

```python
ta = [t for t in re.findall(r'\{[^}]*\}', a) if t != '{FFFE}']
```

— **only `{FFFE}` is exempt**, so any added `{FCC0}` fails as “tag stream changed”. Chunk 8's
first draft added two (the Alfred briefing on L4, the battle plan on L10), `check` failed on
exactly those two lines, and the translator **re-cut both speeches to the source's page structure
instead of touching the tools** (CLAUDE.md §3). That was the right call and the shipped file adds
none.

**The consequence is the part that matters for the rest of the project:** every battle chunk is
silently constrained to the source's own page count, which is a **tighter constraint than the
prompt describes**, and in this unit it changed two speeches and forced the §2.1 step-5
compression in Q3. Someone with authority over both files has to decide which is wrong — widen the
exemption to `{FCC0}`, or delete the licence from the prompt's four places. Until then translators
will keep hitting it. Related: §C, and the several existing notes that a unit “preserved the source
structure rather than inserting `{FCC0}`” (§D4, §M) were each hitting this same wall without
naming it.

### Q3. The one §2.1 step-5 compression, and why it is forced

`退路・補給路の確保だ。` → `ｏｕｒ　ｒｅｔｒｅａｔ　ａｎｄ　ｓｕｐｐｌｙ．` (L4) — the `路`
(“routes / lines”) is implicit. Flagged by the translator; **verified forced at review, twice
over**:

- `ｒｅｔｒｅａｔ　ａｎｄ　ｓｕｐｐｌｙ　ｒｏｕｔｅｓ．` measures **26** and cannot be a row;
- the whole sentence with `ｌｉｎｅｓ` restored measures **93 characters against the 92 that four
  rows of 23 can hold**, so it does not fit at *any* split, and `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ`
  occupies a whole row on its own (17 columns, see glossary §29.5).

A fifth row needs the `{FCC0}` **Q2 forbids**. Both nouns survive and “secure our retreat and
supply” is ordinary military English.

### Q4. ⚠️ SOURCE DEFECT — `大減棒` is a typo for `大減俸`

`く〜っ、こりゃ、{FFFE}大減棒ものだな。` (L14). **`減棒` is not a word; `減俸` (げんぽう, a cut in
pay or stipend) is**, they are homophonous, and a pay cut is what the scene requires — an escort
officer who has just lost the prisoner he was guarding. Counted at review: **1 occurrence in
`dumps/battle_dump.txt`** (this line) and **0 in `dumps/script_unique.txt`**, so it is a hapax and
no other line is affected. Rendered for the meaning as `ａ　ｂｉｇ　ｐａｙ　ｃｕｔ`; **no translation
change is wanted.** Filed here with §D's other source defects so nobody “fixes” the dump. Glossary
§29.2 carries the row.

### Q5. Round-1 findings, and how they were settled

**Finding 1 — the `{FCC0}` cleared the box between `ｔｈｅ` and `ｆｏｒｅｓｔ` (L10). Applied.**
The evidence that made it a finding rather than a preference, counted across the whole shipped
corpus at review: **`tl/` holds 10 English page breaks that fall mid-sentence, and nine of them are
inherited** — the source's own `{FCC0}` there follows a `、`, so the English had no choice (chunk 0
L10 ×4, chunk 1 L8 ×2, chunk 3 L5 ×2, chunk 12 L16), and every one lands after a comma or a
coordinating `and` / `but` / `so`. **Chunk 8 L10 was the only case in the project where the source's
`{FCC0}` follows a sentence-final `。` and the English carried a phrase across it**, and the only one
that split a determiner from its head noun.

The translator tested the finding's premise before applying it — checking whether the break could be
*removed* rather than moved — and the answer is no: the two order-sentences measure **118 columns
against the 92** that page B's four rows hold, and the first two need **5 rows against 4**. **Exactly
one mid-sentence page break is unavoidable here without the `{FCC0}` Q2 forbids**, so only its
*site* was ever open. The re-cut moved two rows back into the preceding page (which had two free
rows) and now breaks after `ｔｈｅ　ｆｏｒｅｓｔ　ａｎｄ` — a coordinating conjunction, the shape chunks
0 and 1 already ship — and after `ｈｉｔｓ　ｔｈｅｉｒ　ｆｌａｎｋ．`, a **full sentence boundary**, which
is better than the reviewer's own proposal and puts the Procyon sentence whole on its own page.

**Finding 2 — `南から、帝国軍よ！` reversed the source's clause order, unforced and unflagged.
Reverted.** Both orders measure identically — `Ｆｒｏｍ　ｔｈｅ　ｓｏｕｔｈ，` (15) /
`ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ！` (18) against `Ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ，` (18) /
`ｆｒｏｍ　ｔｈｅ　ｓｏｕｔｈ！` (15), same 33 characters, same two rows — so the reorder bought nothing
and §2's literal default governs. The PR's step-6 reorder count drops from three to two, and both
survivors were verified forced (`ｃｏｍｐｏｓｉｔｉｏｎ　ａｎｄ　ｍｏｂｉｌｉｔｙ` is **exactly 24**;
`ｆｏｒｅｓｔ，　Ｃａｒｌｉｎｅ’ｓ　ａｒｍｙ！` in source order is **25**).

**Finding 3 — the PR's own L9 break accounting was incomplete.** Re-derived per turn: **+2 / −5**,
not +1 / −4 (net −3 either way, which is what 54→51 says). The missing addition is
`一緒に行こう、セネカ。`, which needs two rows because one would be 26; the missing deletion is
`挟撃を受ける` + `危険性があるぞ。` merging into `ｃａｕｇｈｔ　ｉｎ　ａ　ｐｉｎｃｅｒ．`. Corrected in the
PR body at round 2. **Not a gate failure** — the per-line figures were always right and complete.

### Q6. Two candidate findings WITHDRAWN at review, and why they are recorded

Both were raised, then measured against the corpus and dropped. They are written down so the next
reviewer does not spend the round re-deriving them:

- **`Ｈｅｒｅ　ｔｈｅｙ　ｃｏｍｅ，　ｔｈｅ` / `Ｉｍｐｅｒｉａｌ　ａｒｍｙ！` (L5)** ends a row on an article
  and splits a noun phrase, and a free alternative exists.
- **`Ｗｅｓｔｂｕｒｙ．　Ｂｕｔ　ａｌｏｎｅ　Ｉ` (L9)** ends a row on a lone one-letter word, which
  prompt §3.2 names explicitly, and a free alternative exists.

**Counted across all shipped `tl/battle/`: 29 rows end on `ｔｈｅ`, 17 on `ｉｓ`, 13 on `ｔｏ`, 8 each
on `ａ` / `ｉｎ` / `ｓｏ` / `ｂｅ`, 7 on `ｏｆ`, and `chunk_007.txt` L19 already ships a row ending on a
lone `Ｉ`.** That is settled house practice across sixteen chunks and four reviewers, so holding one
unit to a stricter standard would be the reviewer imposing taste. **Both withdrawn.** If the project
ever wants the stricter rule, it is a project-wide decision and a re-cut of thirty-odd shipped rows,
not a PR finding.

### Q7. Cross-PR and duplicate verification

Gate 6 by **positional pairing against `dumps/battle_dump.txt`**, not by grepping Japanese against
`tl/` — battle files hold zero Japanese, so that grep is a null check (`translator.md` `06353c7`
already records this). Four granularities: whole message with tags, whole message text-only, turns
split at `{FC30}`, pages split at `{FC30}`/`{FCC0}`/`{FC50}`/`{FC51}`. Run at round 2 over **19
chunks** — the 17 shipped, including chunk 13 which merged between the rounds, plus PR #12's
`pending/chunk_017.txt`:

```
A whole message (tags incl)  keys=163  divergent=0
B whole message (text only)  keys=154  divergent=0
C turns @FC30                keys=457  divergent=0
D pages                      keys=624  divergent=0
```

**Zero divergent renderings**, so `tl/battle/` remains free of divergent duplicates (the state §O
first reached) and chunk 8 does not disturb it. Cross-PR spot checks: `ルート` → `ｒｏｕｔｅ`
lowercase in both chunk 8 and chunk 17 L3/L4; chunk 13 L8 keeps bare `わかった・・・・。` as
`Ｒｉｇｈｔ．．．．．`; chunk 17 L6 renders `了解！よし、` as `Ｕｎｄｅｒｓｔｏｏｄ！Ｒｉｇｈｔ，` — three
units, three source strings, no clash. See glossary §29.4.

### Q8. Forward list — 12 segments that recur in chunks nobody has translated yet

Not §3 violations today, since nothing is shipped on the other side. **Whoever takes these chunks
must match chunk 8 rather than reinvent**, and the renderings are in `glossary.md` §29:

| Segment | Recurs in |
|---|---|
| `アルフレッド、` | ch.16 |
| `よりによって、` | ch.19 |
| `よさそうだな。` | ch.19, ch.27 |
| `こんなところで` | ch.24 |
| `何がなんでも、` | ch.24 |
| `そ、それが、` | ch.24 |
| `それでは、` | ch.5, ch.43 |
| `俺たちは、` | ch.21 |
| `どうした。` | ch.43 |
| `それに、` | ch.43 |
| `何？` | ch.17 |
| `君、` | ch.24 |

⚠️ **`ルート` is live this wave**: chunk 17 (PR #12) renders it too. Its §9 PROVISIONAL row is
**deliberately left unstruck** at this integration — the wave's rule is that a cross-unit seed is
struck once, by whichever unit merges second, and that is #12. Glossary §29.1 says so on the row.

### Q9. Two glossary figures corrected under §4.3, with nothing re-cut

Written out in `glossary.md` §29.5 rather than patched in place, per §4.3 and CLAUDE.md §6.7:

1. **`少尉` → `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` is 17 columns, not §1/§2's 18** (Second 6 + space +
   Lieutenant 10). Caught by the translator in Flag 4, remeasured at review. The knock-on is that
   **`Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ` is 23 and would fit one row**, so §1's “never on one
   row” is false as written — it is the vocative comma that makes it **24**, and the vocative is
   the only shape either dump renders. Chunk 8's split stands; **no shipped line changes.** §2's
   `中尉` → `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ` “17” is the same error (it is **16**), flagged not changed
   because nothing renders it yet. **This is the third seeding/measurement figure this wave to be
   one or two columns out** — after §M's three remeasurements and §P's `アーバイン様` 7/12 → 6/11.
   Column figures in seeds and PR bodies should be treated as claims to check, not data.
2. **`うん、` → `Ｙｅｓ，` is right, but the PR's stated licence is not.** §18.3 freed `Ｙｅｓ` from
   `ああ` **only**. `Ｙｅｓ` already carries `ええ。` (`chunk_007` L19), `そうだ、` (`chunk_000` L3)
   and, since PR #10, `ははっ！` → `Ｙｅｓ，　ｓｉｒ！` (glossary §28.3). What licenses a fourth is
   §25.3's co-occurrence test, and it passes: `うん` in chunks 8, 20, 43; `ええ` in 7, 19, 32;
   `そうだ、` in 0, 5, 24, 39; `ははっ` in 13, 16, 37, 38, 42 — **no chunk contains うん with any of
   the other three.** Recorded with that reason in §29.3.

### Q10. Bank figures at this integration

Unmoved by a battle unit, recorded because gate 5 requires naming any bank under 2,000 free:
**bank 41 → 353 free**, **bank 40 → 471 free**, then 5 → 3,381, 2 → 7,505, 33 → 9,315. No bank
negative. `merge` prints no “never matched the dump”; `rowcheck script` reports only the two known
INHERITED over-4-row pages (lines 1234 and 8194). §F2 and §O1 are unchanged.

---

## R. Wave 3 review — battle chunk 17 / PR #12 (2026-09-08)

**PARKED at round 2, squash `2e0790d`.** `pending/chunk_017.txt` — **5,857 / 8,192 bytes, slack
2,335**; JP 1,144 → EN 2,472 = **2.16×** against a 3.19× ceiling; 154 rows, widest **23**, none at
24; no page over 4 text rows; tag stream identical to the dump but for **7 added `{FFFE}` (120 →
127, none deleted)**; **`{FCC0}` 12 → 12, untouched**; header and `{PAD 5005}` byte-identical.
Every figure re-derived at review with **both** `cost()` and the true Shift-JIS encoder
`riotbattle.bytes_from_body`, which agree to the byte. Glossary §30.

**No script bank is touched** (battle unit), so `bankmeasure` was correctly not run and the
standing tightest banks are unchanged: **41 → 353 free, 40 → 471, 5 → 3,381**, 2 → 7,505
(`FLAGS.md` §O1). No bank under 2,000 free is newly at risk from this unit.

### R1. ⚠️ THE PARK REASON — the §D1 dump artifact, and it is the highest-leverage item on the human's list

**This is not a budget park.** The unit is 2,335 bytes *under* its slot and needed no compression
at all. It cannot ship because **`assemble.py`'s charset and tag-parity gates are unsatisfiable
together** on message line 19's item-grant tail. Re-derived from `dumps/battle_dump.txt` at review
rather than taken from the PR:

- The dump reads `…{FC30}{FC70}{=00}入{=A300020000}{FFFF}`. Every clean `{FC70}` reads
  `{FC70}{=00XX}{FCA3}{=00NN0000}`. Here the item id is **0x93**, and `93 FC` — the id byte plus
  the **lead byte of the following tag** — is a valid Shift-JIS sequence, so `riotbattle.tokenise`
  decoded it as the character **入**.
- **`入` is the only character in the Shift-JIS repertoire encoding to `93 FC`** — enumerated over
  the BMP at review, not argued. Chunk 39 message 8 is the identical shape with id `0x8C` → `向`
  (`8C FC`), which confirms the diagnosis outright.
- **All four candidate encodings produce the byte-identical stream `FC70 0093 FCA3 00020000`**, so
  **parking costs nothing** — the game output is the same whichever form is written. Verified:

| Form | `tag_parity` | charset |
|---|---|---|
| `{FC70}{=00}入{=A300020000}` (the dump form) | **PASS** | **FAIL** — illegal char 入 |
| `{FC70}{=0093}{FCA3}{=00020000}` | **FAIL** — tag stream changed | PASS |
| `{FC70}{=00}{=93FC}{=A300020000}` | **FAIL** | PASS |
| `{FC70}{=0093FC}{=A300020000}` | **FAIL** | PASS |

  Each was run through `assemble.tag_parity` and `assemble.validate_body` at review. **There is no
  fifth form**: keeping the dump's three tags in order with no text between them loses the `93 FC`
  bytes, and widening the charset means editing `assemble.py`, which CLAUDE.md §3 forbids.
- **The artifact is inherent to the chunk, not introduced by the translation.** The pristine dump
  chunk placed in `tl/battle/` raises 998 charset problems, three of them `入`. **No chunk 17 file
  of any kind can pass `check` today**, translated or not.
- Shipped, the reworked file gives exactly one problem:
  `!! chunk 17 line 18: illegal char '入' (U+5165)`. Nothing else in the project fails.

**Chunk 17 is the first chunk whose ONLY blocker is this**, which is what makes the dumper fix
worth a human's time now: 1,144 JP characters — **2.7% of the battle script** — finished, faithful,
format-clean and 2,335 bytes under its slot, held up by one character.

### R2. Scope — 24 occurrences, 10 chunks, and the swallowed byte is NOT always `0xFC`

Enumerated across the whole dump at review. Two corrections to PR #12's account, both accepted by
the translator:

- The PR's prose says *"Five of those ten (15, 16, 23, 27, 28, 29, 32, 39)"*. That list has **eight**
  entries, and **eight is the right number**: of the ten chunks, 5 is already parked and 17 is this
  unit, so **eight chunks still meet this the moment they are translated**.
- ⚠️ **The swallowed lead byte is `0xFA` in ten of the twenty-four cases, not always `0xFC`.** The
  character's *trail* byte is whatever the next tag's lead byte happens to be. **This widens the
  diagnosis and it changes the fix**: the dumper repair must be about **argument lengths in
  general**, not about `{FCA3}` or about `0xFC`.

| Chunk | Msg line(s) | Tag | Char | SJIS | Swallowed lead |
|---|---|---|---|---|---|
| **5** | 17 | `{FC70}` | `逓` | `92FC` | `0xFC` |
| **15** | 11 | `{FCA8}` | `諦` | `92FA` | `0xFA` |
| **16** | 5 | `{FC70}` | `改` | `89FC` | `0xFC` |
| **17** | 19 | `{FC70}` | `入` | `93FC` | `0xFC` |
| **23** | 7 | `{FC70}` | `蔭` | `88FC` | `0xFC` |
| **27** | 3, 4 ×2, 5 ×2 | `{FCA8}` | `奧` | `9AFA` | `0xFA` |
| **27** | 4, 6, 7 ×2 | `{FCA8}` | `哄` | `99FA` | `0xFA` |
| **28** | 18, 23 | `{FCA8}` | `咨` | `99FC` | `0xFC` |
| **29** | 10 | `{FCA8}` | `奩` | `9AFC` | `0xFC` |
| **29** | 20 | `{FCA8}` | `奧` | `9AFA` | `0xFA` |
| **32** | 12, 14 ×2 | `{FCA8}` | `哄` | `99FA` | `0xFA` |
| **32** | 13, 14 | `{FCA8}` | `奧` | `9AFA` | `0xFA` |
| **39** | 8 | `{FC70}` | `向` | `8CFC` | `0xFC` |

Totals: **24 occurrences, 10 chunks; trail `FC` ×8, trail `FA` ×16.** `{FC70}` in **5, 16, 17, 23,
39**; `{FCA8}` in **15, 27, 28, 29, 32**. Note the `FC`/`FA` split does **not** line up with the
`{FC70}`/`{FCA8}` split — chunk 29 has one of each — which is further evidence the cause is
argument length, not a particular tag pair.

### R3. ⚠️ FOR WAVE 4 — chunk 15 carries this and will park the same way

**Chunk 15 is on wave 4's list and its artifact is at message line 11 (file line 12):**
`{FCA8}{=01}諦{=1000000000}`, `諦` = **`92 FA`** — one of the `FA` cases. Tier D, ratio 6.13, so it
is otherwise an easy chunk. **Unless the dumper is fixed first, chunk 15 will translate cleanly and
then be unable to ship, exactly as chunk 17 was.** Whoever plans wave 4 should either fix the dumper
first or dispatch chunk 15 knowing it parks. Chunks 16, 23, 27, 28, 29, 32 and 39 are in the same
position whenever they are reached.

### R4. The unpark recipe — one tooling change, ten chunks

**Not proposed as a translator change** (CLAUDE.md §3 — a tool bug is a human's call), but the cause
is narrow and the fix is small:

> `riotbattle.tokenise` prefers a Shift-JIS text run over a control tag whenever an argument byte
> happens to be a valid Shift-JIS lead byte. Teach it the **argument lengths** of `{FC70}` and
> `{FCA8}` — or, more generally, stop an argument byte from ever starting a text run — then
> `assemble.py refresh` to re-dump.

Afterwards, chunk 17 unparks with **`git mv pending/chunk_017.txt tl/battle/chunk_017.txt`** plus a
**0-byte** re-tokenisation of that one tail to match whatever the new dump emits. Nothing else in
the file changes; every other gate already passes. **The same fix unblocks the other nine chunks at
once.** This belongs beside §D1 and in `HANDOFF.md` → "Blocked — needs a human".

### R5. CORRECTION to `pending/README.md` (§4.3 style — written out, not patched silently)

`pending/README.md` records chunk 5's instance of this artifact and says the dumper *"decoded
argument bytes **0x9276** as text"*. **That value is wrong.** `逓` encodes to **`92 FC`**, not
`0x9276` — checked at this review. The line number it gives (chunk 5 line 17) **is** right, and the
diagnosis is right; only the byte pair was mistyped. Corrected in that file in this commit, with
this note as the record.

### R6. Flag 6's §2.1 claim is VOID — the line stands on a different reason

PR #12's Flag 6 justified `リムル様、奇襲です！` → `Ｌａｄｙ　Ｒｉｍｕｌ，　ａ　ｒａｉｄ！` as a §2.1
step-6 departure, on the ground that `Ｌａｄｙ　Ｒｉｍｕｌ，　ａ　ｓｕｒｐｒｉｓｅ` and
`ｕｎｄｅｒ　ｓｕｒｐｒｉｓｅ　ａｔｔａｃｋ！` *"measure exactly 24"*. **Both are 22** — remeasured at
review and confirmed by the translator, which had counted `ｓｕｒｐｒｉｓｅ` as 9 and `Ｒｉｍｕｌ，` as 7.
A 4-row layout carrying the full 奇襲 exists (22 / 22 / 20 / 9).

**The line is unchanged and correct**, but for a better reason: 奇襲 *is* "surprise attack; raid",
so `ａ　ｒａｉｄ！` is a dictionary equivalent and **not a §2.1 departure at all**; and the priced
alternative breaks the sentence mid-clause where the shipped form maps the source's four clauses
1:1, which `translation_prompt.md` §3.2 prefers. **Recorded so no later unit inherits a width
constraint that does not exist.** This is the fourth width-miscount in three waves (§28.1, §29.5,
§25.1) — **measure with a tool, never by eye.**

### R7. Other width corrections made at this review

Six figures in PR #12's glossary table were one or more columns out; all are corrected in glossary
§30 and none changes a rendering. `Ｂｕｒｇｅｓｓ` **7** (not 8) · `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` **14**
(not 15, and §9's seed said 15 too) · `Ｉｎｔｅｒｃｅｐｔ　ｓｔａｔｉｏｎｓ` **18** (not 19) ·
`ｓｏｒｔｉｅ！` **7** (not 8) · `ｈａｒｄｗａｒｅ` **8** (not 9) · `ｔｉｍｅ　ｔｏ　ｗｉｔｈｄｒａｗ` **16**
(not 20).

Also corrected: the PR's `{FFFE}` **total** of 132 → 139. The real figures are **120 → 127**;
the +7 delta and the per-line table were always right. Conceded by the translator at round 2.

### R8. Rimul takes no contractions here, and shipped `chunk_000.txt` does not — recorded, not re-cut

Glossary §7 is explicit that Rimul takes no contractions in her own lines, and chunk 17 holds that
across every one of her segments. **Shipped `chunk_000.txt` L14/L18 nevertheless give her `ｃａｎ’ｔ`,
`ｄｏｎ’ｔ`, `ｗｏｎ’ｔ`, `Ｉ’ｌｌ`.** The unit followed the written rule and correctly did **not**
propose a re-cut: different messages, so CLAUDE.md §3 is not engaged (§20.4 / §23.1 / §24.5 shape),
chunk 0 has **27 bytes of slack** (§G1), and §18.3 records that its next correction needs a full
re-cut. **Left alone deliberately.** If chunk 0 is ever re-cut for another reason, these two lines
should be brought into line at the same time.

### R9. Reading findings raised and resolved (round 1 → round 2)

Two rows changed, **−16 bytes**, no re-flow, nothing else touched:

1. `読みが甘かったか。` → `Ｉ　ｒｅａｄ　ｔｈｅｍ　ｔｏｏ　ｓｏｆｔｌｙ．` was not English, and its stated
   parallel with §25.1's 甘くない was false (`chunk_009` ships `ｈａｒｄｅｒ`; `ｓｏｆｔ` was nowhere in
   `tl/`). Now **`Ｉ　ｍｉｓｒｅａｄ　ｔｈｅｍ．`** — and the translator **overturned the reviewer's
   proposed `ｕｎｄｅｒｅｓｔｉｍａｔｅｄ`, correctly**, because three source phrases (`甘く見ない方`,
   `見くびっていた`, `見くびって`) genuinely mean *underestimate*. That word is now **reserved**;
   glossary §30.4.
2. `いや、` → `Ｎｏ．` where §25.2 fixes `Ｎｏ` **plus the source's own punctuation**. Now `Ｎｏ，`,
   23 columns, **0 bytes**. The unit had already used `Ｎｏ，` for `いえ、` twice, so it was an
   outlier against itself as well as against `chunk_004` and `chunk_009`.

### R10. Three sisters in one chunk, all left uncommitted

Femina is confirmed as portrait 02's **妹**, from the tag stream (glossary §30.5). Two further
threads are **deliberately not resolved and no glossary row is proposed for either**: chunk 4's
dying enemy girl cries for her 姉さん (§23.5) and the halves fit, but nothing names her; and the
unnamed enemy of message lines 22–23 has *a third* sword-wielding sister. **A chunk that names any
of them should re-check all three together.**

### R11. Duplicate check — method note for later units

Gate 6 was run by **positional pairing against the dump at message and page granularity across all
19 translated units** (18 shipped + this branch): **15 repeated JP messages / 18 repeated JP pages,
0 divergent.** Grepping Japanese against `tl/battle/*.txt` is a **null check** — those files hold
zero Japanese — and row granularity mispairs on a re-flowed unit (§P3). `村が襲われました。` is
byte-identical **as a whole message** between chunk 17 and `chunk_034.txt`, and the §27.2 wording
matches chunks 7 ×2, 13 and 34 byte-for-byte. After this park: 4 shipped, **1 written and parked
(chunk 17)**, and **8 instances across 7 chunks still to write** (5, 15, 16 ×2, 21, 23, 38, 39).

---

## S. Wave 4 review — battle chunk 18 / PR #13 (2026-09-08)

**MERGED at round 1**, zero blocking findings. `tl/battle/chunk_018.txt` — **3,035 / 8,192 bytes,
slack 5,157; 78 text rows, widest 23, none at 24**, no page over 4 text rows, one `{FFFE}` added
(file line 7, 19 → 20), no `{FCC0}` touched. Every §6 gate re-run in a real checkout and pasted in
the PR review. Rulings live in `glossary.md` **§31**; this section carries what a human should look
at.

### S1. Two judgement calls the translator deliberately left open, both ruled in its favour

Recorded because the PR chose to *ask* rather than decide, and both answers turned on evidence the
PR did not have. See glossary §31.4 and §31.5 for the rulings in full.

1. **`いや、わかった。` → `Ｎｏ．　Ｒｉｇｈｔ．`** — the source's comma promoted to a full stop.
   **Already shipped**: `tl/battle/chunk_014.txt` msg 10 renders `よし、ここまで来たら、` as
   `Ｒｉｇｈｔ．　Ｗｅ’ｖｅ　ｃｏｍｅ　ｔｈｉｓ`, the same promotion for the same reason. The rule written
   at §31.4 — *§5's punctuation mechanism yields to English sentence grammar only where the
   material after the source's comma is a complete independent clause* — is what keeps this from
   contradicting §R / glossary §30.3, which corrected a `Ｎｏ．` to `Ｎｏ，` on a **continuing**
   clause at chunk 17's round 2. **§30.3 is unamended.**
2. **`シナリオ` → `ｓｃｒｉｐｔ`, not `ｐｌａｎ`** — because `ｐｌａｎ` is already spent on 作戦
   (§19.2, shipped in `chunk_001`). ⚠️ **Width does not decide it and the PR implied it did**:
   `Ｅｖｅｒｙｔｈｉｎｇ　ｇｏｅｓ　ｔｏ　ｐｌａｎ．` is 24, but `Ａｌｌ　ｇｏｅｓ　ｔｏ　ｐｌａｎ．` is 17 and
   would have fitted.

### S2. Five figures in the PR body are wrong; every rendering is right

Same class as §P / §Q / §R's remeasurements. Nothing was re-cut.

| PR said | Actual | Where |
|---|---|---|
| 60 text rows | **78** | recounted twice by independent boundary walks: lines 5/7/8/10/12 = 43/22/4/2/7 |
| `Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ` 18 columns | **17** | 18 is the form with a following stop — §25.1's own figure |
| `ｔｈｅ　ｄｅｆｅｎｃｅ` 12 columns | **11** | |
| `Ｎｏｗ　ｔｈｅｎ，` 10 columns | **9** | |
| `シナリオ` "hapax — 1 battle / 0 script" | **3 battle** (c18 ×1, **c23 ×2**), 0 script | see S3 |

### S3. Three strings this unit now binds in still-untranslated chunks

Whoever takes these chunks must copy, not re-invent. All three counted in `dumps/battle_dump.txt`
at review.

- **`かかってくるがいい。` → `Ｙｏｕ　ｍａｙ　ｃｏｍｅ　ａｔ　ｍｅ．`** is byte-identical at **chunk 23
  L15**. 2 battle / 0 script. The sibling `かかってこい。` (chunks 16 ×2, 30) is deliberately left
  free to take `chunk_033`'s shipped `Ｃｏｍｅ　ａｔ　ｍｅ．`, and `かかってきなさい。` (chunk 33) already
  holds it.
- **`シナリオ` → `ｓｃｒｉｐｔ`** reaches **chunk 23 ×2**
  (`俺には、このシナリオがフェルナンドひとりの手で仕組まれたとは思えない。`) — the same staged-affair
  metaphor five chapters later. The **word** is fixed; chunk 23's `このシナリオ` is a different
  construction and takes `ｔｈｉｓ　ｓｃｒｉｐｔ`, not chunk 18's frame.
- **`まさか、` → `Ｓｕｒｅｌｙ`** — see S4.

Two more forms will be reached again and had no stated reach in the PR: **`手駒` → `ｐｉｅｃｅｓ`**
(1 battle + **3 script**) and **`ご奮闘` → `ｓｔｒｕｇｇｌｅ`** (2 battle — this chunk and **chunk 28**).

### S4. `まさか` had been shipped for a whole wave with no glossary row — 28 occurrences riding on it

⚠️ **The largest single drift risk this unit leaves behind, and neither the PR nor wave 3 raised
it.** `pending/chunk_017.txt` msg 4 ships `まさか、奴らは` → `Ｓｕｒｅｌｙ　ｔｈｅｙ　ｄｉｄ　ｎｏｔ`;
chunk 18 uses the same word; **`glossary.md` fixed neither.** Counted at this review: **18 battle
occurrences across 13 chunks (0, 17, 18, 19, 23, 24, 25, 26, 27, 30, 32, 39, 43) + 10 script.**
Fixed now at glossary §31.3 — the §24.3 `よし、` shape, a form shipped repeatedly that the glossary
never wrote down.

⚠️ **Chunks 19 and 23 both carry it, and chunk 19 is live in this wave (PR #16).**

### S5. Three English forms now serve more than one Japanese word, all safe, all recorded

The PR's additions table named none of these. §3 is not engaged in any of them (different
messages), and §25.3's co-occurrence test was run for each.

| English | Japanese words it serves | Test |
|---|---|---|
| `Ｎｏｗ　ｔｈｅｎ` | `さて、` (c33 shipped, c18), `それじゃ、` (c3), `おっと。` (c7, as `Ｎｏｗ　ｔｈｅｎ．`) | `さて、` c18/26/33 · `それじゃ` c3/7/15/32/43 · `おっと` c7/25/43 — **no chunk holds `さて、` with either** ✓ |
| `ｄｅｐｌｏｙ` | 配備につく (c17 noun, c18 verb), 配置する (c33) | 配置 = battle c33 only (+2 script); 配備 = c17, c18 only (+3 script) — **disjoint** ✓ |
| `ｄｅｆｅｎｃｅ` | 守備 bare (c18), 防御力 → *defence power* (`batch_001`, `batch_003`), 正当防衛 → *self‐defence* (`chunk_011`) | compounds of different words; 守備兵 → *garrison* (§2) stays separate ✓ |

⚠️ **`それじゃ` and `おっと` DO co-occur — chunks 7 and 43** — and `chunk_007` ships `おっと。` →
`Ｎｏｗ　ｔｈｅｎ．`. That belongs to the **`おっと` ruling `HANDOFF.md` hands to another reviewer**
(batch_006 / PR #15 raised it, with a second divergent rendering `Ａｈ　ａｈ，` in parked
`chunk_043`), not to this unit. Recorded here so that reviewer inherits the count instead of
recomputing it.

### S6. `ええい、` → `Ｅｎｏｕｇｈ！` is NOT §5's punctuation mechanism — do not "fix" it

⚠️ **A trap for a future duplicate check.** §14.5's entry carries the `！` **as part of the fixed
form**, and the Japanese has `、` in every instance. `chunk_007` msg 2 ships
`ええい、全軍　迎えうてッ！！` → `Ｅｎｏｕｇｈ！` / `Ａｌｌ　ｕｎｉｔｓ，　ｉｎｔｅｒｃｅｐｔ！！`; chunk 18's
`ええい、この非常時に。` → `Ｅｎｏｕｇｈ！　Ｉｎ　ｔｈｉｓ　ｃｒｉｓｉｓ．` matches it byte-for-byte. Anyone
applying §5's *word-plus-source-punctuation* rule mechanically will "correct" both to `Ｅｎｏｕｇｈ，`
and break two shipped files. **Chunk 24 carries a third instance, untranslated.**

Same shape: **chunk 18 renders `いや、` as `Ｎｏ，` and `Ｎｏ．` inside one message** (file line 5,
four pages apart). Correct per §31.4; a positional check will read it as a divergence and it is
not one. Cf. §O8 / §P on numbering, glossary §24.5 and §27.4 on the other two such traps.

### S7. Numbering — a FOURTH convention is now in play in one repo

`glossary.md` §31's line numbers are **`tl/` FILE lines** (the `=== CHUNK` header counted as line
1). §28 and §30 use **message** lines (file line − 1); §29 uses **`rowcheck` lines** (header as
line 0). `HANDOFF.md` has used yet another. **Locate by content, never by number.** This is §O8 and
§P restated because it has now bitten four sections running; a human tidying this repo should pick
one convention and migrate all four.

### S8. Glossary coverage line corrected (not an entry, but recorded anyway)

`glossary.md`'s Status header listed battle chunks **0, 1, 2, 3, 4, 7, 10, 11, 12, 14, 33, 34, 35,
40** — omitting **6, 8, 9, 13 and 17**, all merged or parked in waves 2–3, and it had gone
uncorrected through five integrations. Updated at this integration to the true list plus chunk 18
and the parked 5 / 17 / 43. **No rendering changes and nothing needs revisiting** — it is a
coverage note, not a fixed entry, so §4.3's revisit obligation does not arise. Recorded here
because CLAUDE.md §6.7 forbids silent changes to `glossary.md` of any kind.

### S9. Nothing for a human to unblock in this unit

No `{FCC0}` was attempted (`FLAGS.md` §Q2's documented gate defect was not rediscovered), no
`{FFEC}` / `{FC00}` / `{FFDA}` inserts, no menu options, no `{FC70}` / `{FCA8}` dump artifact
(Blocked item 0 does **not** touch chunk 18), no suspected source typo, no tag whose meaning had to
be guessed. `assemble.py build` and `riotbattle.py checkedit` remain unrun because `original/` is
absent, which CLAUDE.md §2 records as expected.

⚠️ **Portrait 08 is unnamed and the English commits to nothing.** He commands the fortress, holds
Unit 1, and Guilford's soliloquy (`クリッペン司令のご奮闘を拝見させてもらうとしよう`) points hard at
**Commander Krippen** — but no line names him, so no row of his carries a name, per §P's practice
for chunk 13's King. If a later chunk settles it, only his register wants re-checking, not the
text.

---

## T. Wave 4 review — battle chunk 20 / PR #14 (2026-09-09)

**DECISION: MERGE at round 1**, squash-merged as `46b728a`. Every §6 gate run in a real checkout and
pasted in the PR review; **no finding required a change to the unit**. Reviewer 3 of wave 4.

**Figures, all verified here rather than taken from the PR:** `tl/battle/chunk_020.txt` is
**4,265 / 8,192 bytes, slack 3,927**; 732 JP → 1,512 EN characters = **2.07×** against a 4.75×
tier-D ceiling; **94 text rows, widest 23, none at 24** (11 rows at 23). `assemble.py check` →
"All checks passed". `rowcheck.py 20` clean, no page-over-4 warning. An independent token-by-token
skeleton diff against the pristine dump confirms **exactly three `{FFFE}` inserted on two lines
(file line 29: 5→6, file line 48: 13→15), none deleted, no `{FCC0}` added**, and all 48 other body
lines plus `{=FF}` and `{PAD 5493}` byte-identical tag for tag. **Every figure in the PR was
correct as stated** — the first unit this wave for which that is true.

### T1. ~~⚠️ OWED WORK~~ ✅ **DISCHARGED 2026-09-09 by PR #17 — and it was FIVE rows in FOUR files**

> **Discharged at `f25ff14`** (wave-5 `あら` corrections unit). The table below is **incomplete**: it
> omits **`tl/battle/chunk_008.txt` L4** (`あら？` → `Ｏｈ？` → **`Ｍｙ？`**, 3 columns, 0 bytes), which
> glossary §32.4's own census sentence counted and its *Lines this affects* table then dropped — an
> omission §T1 inherited here and the wave-5 dispatch inherited from §T1. PR #17's translator found
> the row by scanning the dump rather than trusting any of the three documents, and fixed it.
> **Five rows, four files, net −6 bytes, zero `{FFFE}` and zero `{FCC0}` changes.** Full record in
> §W below and glossary §35; §32.4's table now carries the chunk 8 row.

**Ruled at this review (glossary §32.4): `あら` takes `Ｍｙ` plus the source's own punctuation.**
§28.3 is upheld and extended; chunk 20 ships `Ｍｙ？` / `Ｍｙ．．．？` and is correct. The decisive
ground is that §24.4 already spent `Ｏｈ？` on おや **outright**, across 29 occurrences, so shipped
`chunk_014`'s `あら？` → `Ｏｈ？` is byte-identical to a different fixed source word.

**This leaves three shipped files as outliers. They are NOT fixed in the integration commit** — PR
#15 (batch 006) is open and unreviewed on the same question from the script side (~30 more
instances) and chunk 19 is mid-rework, so re-cutting shipped files inside a battle-chunk merge was
the wrong blast radius. This is the §27 corrections-unit shape.

| File | Row | Now | Must become | Cost |
|---|---|---|---|---|
| `tl/battle/chunk_007.txt` L19 | `あら・・・・？` | `Ｏｈ．．．．？` (7) | `Ｍｙ．．．．？` (7) | 0 bytes |
| `tl/battle/chunk_007.txt` L24 | `あら、雪・・・？` | `Ｏｈ，　ｓｎｏｗ．．．？` (12) | `Ｍｙ，　ｓｎｏｗ．．．？` (12) | 0 bytes |
| `tl/battle/chunk_011.txt` L3 | `あら、お客様？` | `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` (16) | `Ｍｙ，　ｖｉｓｉｔｏｒｓ？` (13) | −6 bytes |
| `tl/battle/chunk_014.txt` L3 | `あら？` | `Ｏｈ？` (3) | `Ｍｙ？` (3) | 0 bytes |

All four are width-neutral or shorter and re-flow nothing; `chunk_007` has 399 bytes of slack and
`chunk_011` 6,625, so neither re-cut is at risk. **Whoever takes this must re-run
`assemble.py check` and `rowcheck.py` on 7, 11 and 14 afterwards.** Also correct §28.3's sentence
"The alternative `Ｏｈ　ｍｙ，` is also free" — it is **false**, and `chunk_011` L3 ships it **for
`あら、` itself**. Already struck in glossary §32.4.

### T2. ⚠️ LIVE COLLISION — `勲章` and `メダル` share `ｍｅｄａｌ`, and share banks 42 and 43

Chunk 20's `ｍｅｄａｌ` is correct and nothing is re-cut. But the PR (and the §9 seed before it)
discharged the clash with §3's racetrack `メダル` → `ｍｅｄａｌ` on a false premise, and the
discharge is withdrawn — see glossary §32.5.

- `勲章` is **4 battle (chunks 20 ×2, 22 ×2) + 59 in `script_dump.txt` / 39 in `script_unique.txt`**,
  not the seed's and the PR's "2 battle".
- It is the plot item **`獅子の勲章`** (9×) / **`『獅子の勲章』`** (2×) — the King's decoration,
  Fernando's forgery, the coup. Not a trinket.
- §25.3's test, applied as this project states it ("no chunk and no bank contains both"), is **NOT
  met**: `メダル` is in banks **42, 43**; `勲章` is in banks 1–9, 12–19, 23, 25, 32, 33, 40–43;
  **both are in 42 and 43**. **0 messages contain both**, so nothing is unreadable today.

**For whoever takes banks 42–43:** the reserve is `ｔｏｋｅｎ` (5 columns), verified free across `tl/`
and `pending/`, and it is the **racetrack** side that moves — which makes §3's `メダル` row a §4.3
correction naming `tl/script/batch_002.tsv`. Do not silently re-point `勲章`.

### T3. Glossary rows the PR rendered but did not record — added at integration

All correct as shipped; all needed rows so they cannot drift. Written into §32.2 / §32.3:
`ふふっ、` → `Ｆｕｆｕ，` (a new spelling on §12.3, **whose "feminine" gloss is corrected — a male
officer speaks it here**); `ようし、` → `Ｒｉｇｈｔ，` (a distinct source string collapsed onto
§24.3's `よし、`, 1 battle + 2 script); `〜の奴` / `〜の奴ら` (**56 battle + 22 script**, no row until
now, and three prior English forms — `ｆｅｌｌｏｗｓ`, `ｍｅｎ`, and this unit's `ｌｏｔ`, accepted as
register-selected); `おい、` → `Ｏｉ，` (14 battle + 10 script; first **shipping** use — it existed
only in parked `chunk_043`).

⚠️ **`何だ、` → `Ｗｈａｔ，` is NOT a fixed form** and the PR's row called it "an eighth member of the
何 family". It is a clause head English absorbs differently every time, and the corpus already
renders it three ways: `Ｗｈｏ　ａｒｅ　ｙｏｕ？` (`chunk_007` L13), `Ｗｈａｔ　ｉｓ　ｉｔ？` (`batch_002`
L9), and this unit's `Ｗｈａｔ，`. All three are right for their sentences. Rewritten as a row-level
rendering in glossary §32.8 so the next translator does not apply it mechanically.

⚠️ **`ｏｆｆｉｃｅｒ` is not free** — `chunk_001` already ships `ａ　ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ，` for a
different source word. No collision (different message, different collocation), recorded on the
将校 row.

### T4. Small figure corrections, in this wave's established style

- `Ｍｙ．．．？` is **6** columns, not the PR's 7. The `Ｏｈ？` ⇄ `Ｍｙ？` swap is still 0 bytes.
- The PR's Glossary-additions table has **24** rows; the dispatch said 25.
- The `グレイウーズ` → `ｇｒｅｙ　ｏｏｚｅ` precedent is **§17.2**, not §17.4 — the §9 seed mis-cited it
  and the PR inherited the citation. Derivation unaffected.
- `宝` / `お宝` occurs **3** times in this chunk, not the PR's 2.

### T5. Confirmed, not defects — recorded so they are not re-raised

- **Flag 13 CONFIRMED inherited.** The `{FCC0}` page in file line 48 carries a leading blank plus
  four text rows in **the source's own segment structure** (`{FCC0}{FFFE}` + `ねえ、` +
  `アリエスさんも、` + `こっちへ来て、` + `宝石を見なよ。`), reproduced exactly at 4/16/12/22. File
  line 2's `{FCC0}` page likewise reproduces the source's leading blank + 2 rows + `　` row +
  trailing blank. **Neither is `translation_prompt.md` §3.2's untested shape** (leading blank *and*
  trailing blank *and* four text rows). This is glossary §10 question 4, still open for a human and
  neither worsened nor depended on by this unit.
- **§Q2 not re-discovered.** No `{FCC0}` was added anywhere; the documented prompt/gate
  contradiction (`translation_prompt.md` licenses `{FCC0}` at lines 248/361/373/520 while
  `assemble.py:125-126` and `rowcheck.py:93-94` exempt only `{FFFE}`) remains a documentation
  defect for a human and was **not** grounds for any finding.
- **§31.3's known-over-broad `まさか` → `Ｓｕｒｅｌｙ` is inert here**: `まさか` occurs **0 times** in
  chunk 20, counted in the dump body. Chunk 19's re-reviewer still owes the narrowing.
- Three renderings read closely and accepted: `こんなものが。` → `ｔｈｅｒｅ　ｗａｓ　ａｌｓｏ　ｔｈｉｓ．`
  (the *also* is carried by `〜所に`, unflagged); `埋まっていた所に` → `ｗｈｅｒｅ　…　ｌａｙ` against the
  mirror message's `ｗａｓ　ｂｕｒｉｅｄ　ｈｅｒｅ` (§2.1 step 4 width synonym, different source clauses);
  `もんってことさ` → `ｏｕｒｓ　ｎｏｗ．` (mild step-5 implication).

### T6. Bytes and slack after this merge

`chunk_020` ships with **3,927 bytes of slack** — the third-largest margin in `tl/battle/` — so
every reversible call in §32 (`Ｆｉｒｅ　Ｃｒｙｓｔａｌ` if chunk 19 needs it, −6 bytes; any `あら`
respelling) is free here. **No bank is under 2,000 free** as a result of this unit: it touches no
script bank at all, and `bankmeasure.py` was not run because nothing under `tl/script/` changed.

---

## U. Wave 4 review — battle chunk 19 / PR #16 (2026-09-09)

Merged at `aecea69` after **round 2**. **8,065 / 8,192 bytes, slack 127** — 3,325 EN / 1,745 JP =
**1.91×** against a 1.94 ceiling, the tightest unit of the wave and the second tightest shipped
after chunk 0. 200 text rows, widest 23 with 14 at 23, **none at 24**, no page over 4 text rows.
`{FFFE}` 188 → 179 (net −9) on five lines; **`{FCC0}` untouched at 24**; non-break tag stream
byte-identical to the dump on all 28 lines. Glossary entries at **§33**.

### U1. Four findings at round 1, all four accepted, none contested — and every one byte-neutral or better

Recorded because the shape is worth repeating: in the wave's tightest unit, **no finding cost the
budget a byte**. The rework came in at **net 0 characters** and −2 bytes overall.

| # | Finding | Fix | Cost |
|---|---|---|---|
| 1 | `ウルフ` → `Ｗｏｌｆ` collides with shipped `ｗｏｌｆ` (the creature) | → **`Ｕｌｆ`** | **−2 bytes** |
| 2 | Orphaned 4-column `Ｉ　ａｍ` row, against the chunk's own two other renderings of the same formula | repack to `Ｉ　ａｍ　Ｆａｒｉｎａ’ｓ` / `ｇｕａｒｄ　ｃａｐｔａｉｎ，` / `Ｕｌｆ．` | **0 bytes** |
| 3 | Row ends on the lone article `ａ`, orphaning a 5-column `ｌｅａｄ．` — a `translation_prompt.md` §3.2 breach | 4 rows → 3, `…ｈｅ　ｍａｙ　ｋｎｏｗ` / `ｓｏｍｅｔｈｉｎｇ　ｏｆ　ａ　ｌｅａｄ．` | **0 bytes** |
| 4 | A second, undisclosed §2.1 step-6 clause reorder | source order restored (`Ｆｒｏｍ　ｔｈｅ　ｆｏｒｅｓｔ，` / `ｓｏｌｄｉｅｒｓ．．．！`) | **0 bytes** |

**The translator improved on two of them and disclosed both.** Finding 2's repack also removed a
second orphan neither party had claimed (`ａｍ` would have been row-final), and finding 3's page
turned out to carry a **leading blank plus four text rows** — the shape §3.2 says has never
appeared in the source — so the fix moved it away from the wall rather than merely tidying it.

⚠️ **The translator also corrected the reviewer's own evidence on finding 1, and was right.** The
round-1 review said `ｗｏｌｆ` was shipped "three times… a 21-instance row", conflating three
occurrences of the string with one unique line. Recounted: **2 unique lines of `batch_003`
(L39, L40) at 21 instances each = 42 message instances**, and **L40's source key contains the
katakana `ウルフ` itself** (`キラーウルフが進化した狼の怪物。` → `…ｆｒｏｍ　ｔｈｅ　ｋｉｌｌｅｒ　ｗｏｌｆ．`),
so ウルフ → `ｗｏｌｆ` is literally shipped rather than inferred from 狼. The corrected figure is in
§33.3.

### U2. §31.3's `まさか` → `Ｓｕｒｅｌｙ` is over-broad — NARROWED at §33.6, and it was wrong on two facts

⚠️ **This is the item a later unit is most likely to trip on.** §31.3 was written one PR earlier
and named chunk 19 among the 13 chunks it binds. Chunk 19 is the unit that tests it and it does not
hold as written. **No rendering changed; the entry did.** Full working at §33.6; the short form:

- **8 of the 18 battle occurrences are the incredulous use** (`まさか…か？`, bare `まさか・・・`) —
  chunks 0, 17, 18, 19, 25, 27, 39 ×2 — and take `Ｓｕｒｅｌｙ`. Both shipped instances
  (`chunk_018`, `pending/chunk_017`) are of this kind and stand.
- **10 are the exclamative `まさか…とは / とはな`** — chunks 19, 23 ×2, 24, 26, 27, 30, 32 ×2, 43 —
  where `Ｓｕｒｅｌｙ` **inverts the sense**. Chunk 19 renders its one as `ｏｆ　ａｌｌ　ｔｈｉｎｇｓ`.
- **"`Ｓｕｒｅｌｙ` is otherwise free across `tl/`" was false.** Three shipped lowercase `ｓｕｒｅｌｙ`
  render `はずだ` (`chunk_000` L14) and `きっと` (`chunk_007` L20, `chunk_034` L2).
- **§31.3 listed chunk 0, which already ships `まさか、` as `Ｉｔ　ｃａｎ’ｔ　ｂｅ，`** (`chunk_000`
  L14) — contradicted by shipped work at the moment it was written. Chunk 0 stays recorded, not
  re-cut (27 bytes of slack; §18.3).

**Ten chunks inherit the narrowed reading: 23, 24, 26, 27, 30, 32, 43** for the exclamative and
**25, 27, 39** for the incredulous.

### U3. The wave-4 cross-unit rule is DISCHARGED — eight seed rows struck, none re-cut

Chunk 20 merged first and left the four cross-unit rows live; chunk 19 merged second and struck
them, plus the four chunk-19-only seeds — eight in all, **every one used exactly as seeded by both
translators.** ✅ **§9's `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` contingency never fired**: the seed warned that
tier-B chunk 19 might be unable to fit `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` (15) and would drag chunk 20 onto
the short form. Its four rows measure 18 / 18 / 21 / 21 and it shipped with 127 bytes spare, so the
long form stands in both units.

⚠️ **`宝石` was a fifth cross-unit term the seed missed** — 6 battle (19 ×1, 20 ×4, 31 ×1) + 4
unique script lines. Ruled `ｇｅｍｓｔｏｎｅ` at this review (§33.5) and shipped consistently by both
units. **It has no §9 row**, so nothing was struck for it. **Chunk 31 inherits `ｇｅｍｓｔｏｎｅ`**, as
do the three still-untranslated script lines — including the 21-instance
`宝石として珍重する地方もある。`, which is the line that decided it.

### U4. Two duplicate-check traps, both reproduced by the reviewer's own checker

Written into §33.8. Recorded here because they will fire again on any future sweep:

1. **`どうする？` reads DIVERGENT to any index-based row checker** — message 19's deliberate
   step-6 reorder shifts the row index. Chunk 19 does carry `Ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ？`
   byte-identically at message 3. ⚠️ That string is shipped in **five** files (`chunk_000`,
   `chunk_004`, `chunk_008`, `chunk_019`, `pending/chunk_005` ×2) — more entrenched than either
   PR realised, which is precisely what made the reorder worth making.
2. **Ellipsis checkers that STRIP tags rather than SPLIT on them report a false failure at message
   24** — stripping glues `ｌｅｔ’ｓ　ｆｉｇｈｔ．` onto `．．．Ａｇｒｅｅｄ．` and invents a run of four.
   The translator predicted this in its Flag 5 and the reviewer's first checker reproduced it
   exactly. **Split on tags; do not strip them.**

### U5. §29.4's `Ａｇｒｅｅｄ．` reserve is engaged for the first time

Chunk 19 is the unit §29.4 wrote the reserve for: bare `了解。` (message 19) and `・・・わかった。`
(message 24) on one map. 了解 keeps `Ｕｎｄｅｒｓｔｏｏｄ．`, わかった takes `．．．Ａｇｒｅｅｄ．`, and
`Ａｇｒｅｅｄ` was re-verified free across `tl/` and `pending/` — it appears in no translation file
but this one.

⚠️ **The reserve is CONDITIONAL and the next two chunks must not copy it blindly.**
`・・・わかった。` recurs in **chunks 24 and 27**. It takes `．．．Ａｇｒｅｅｄ．` **only** where a
`了解` stands beside it; absent one, §6's `Ｒｉｇｈｔ` governs, as `chunk_013` L8 already ships.
Check the chunk for `了解` before copying.

### U6. Terms fixed at review that neither PR proposed

- **`よりによって` → `ｏｆ　ａｌｌ　…`, complement following the source.** All three battle
  occurrences are now shipped and they differ by design — `Ｏｆ　ａｌｌ　ｐｌａｃｅｓ，` (chunk 19,
  complement is `厄介なところ`), `Ｏｆ　ａｌｌ　ｔｉｍｅｓ，` (chunk 8), `ｔｏ　ｓｅｎｄ　ｍｅ，　ｏｆ　ａｌｌ`
  (chunk 4). The **word** is fixed; the noun follows the source. §3 is not engaged (different
  messages). The phrase is now closed — no further occurrences remain.
- **`どうやら、` → `Ｌｏｏｋｓ　ｌｉｋｅ　…`.** Chunk 19 absorbed it with no standing form and its
  Flag 15 asked for one. **It reaches four more chunks — 23, 25, 30, 31** — so it is fixed now
  rather than invented four times. Held distinct from §26.6's hearsay evidentials: どうやら is the
  speaker's own inference from what he can see, not report of another's word.

### U7. Not raised, so it is not "fixed" later

Three rows end in a one- or two-letter word — `…ｂｕｔ　Ｉ` (message 1), `Ｌｏｏｋｓ　ｌｉｋｅ　ａ`
(message 3), `ｂｕｔ　Ｉ　ｈｅａｒ　ｉｔ　ｉｓ　ａ` (message 23). Each mirrors the source's own break
segment for segment, which §3.2 says should normally be preserved, and **none is compounded by an
orphan row or a page at the four-row wall**. They stand. The one that *was* corrected stacked all
three faults at once.

### U8. Nothing new for a human

No `{FCC0}` was added, so `FLAGS.md` §Q2's documented gate defect was not rediscovered. No tag
required guessing; no source typo suspected. Banks are untouched by this unit — **bank 41 (353
free), bank 40 (471) and bank 5 (3,381) remain the tight three**, unchanged by chunk 19, and no
bank is negative. `python3 tools/assemble.py check` passes on the integration branch after this
commit.

---

## V. Wave 4 review — script batch 006 / PR #15 (2026-09-09)

Merged at **round 1** (squash `13a5ab8`), zero findings requiring a change to the unit. Glossary rows
and every ruling are at **glossary §34**; this section carries what a human or a later unit has to act
on. Section letter read off `FLAGS.md`'s last heading at commit time (`## U`), not reserved.

**Figures, all re-derived at review against a measured baseline** (unit file removed, `merge` re-run,
unit restored) rather than taken from the PR body:

```
BASELINE (batch_006.tsv absent):  script lines replaced: 4039  (unique forms: 211)
WITH UNIT:                        script lines replaced: 4092  (unique forms: 261)
                                  → +53 instances, +50 unique forms — exactly the unit
```

| Bank | Baseline free | With unit | Δ |
|---|---|---|---|
| 12 | 10,321 | **8,639** | −1,682 |
| 13 | 13,449 | **12,727** | −722 |
| 14 | 13,493 | **13,455** | −38 |
| 15 | 13,433 | **13,395** | −38 |

**Total −2,480 bytes; no bank negative.** 1,332 JP → 2,513 EN readable characters = **1.89×**
(planning model 2.10×). Widest row **23**, seven at 23, **none at 24**. One `{FFFE}` added (unique 631,
11 → 12); **no `{FCC0}` change**; the non-break tag stream is **byte-identical on all 50 lines** —
verified mechanically, so Flag 4's insert repositionings changed no tag *order*.

**Banks under 2,000 free, named as CLAUDE.md §6.5 requires: bank 41 → 353, bank 40 → 471.** Both are
**byte-for-byte untouched by this unit** — identical on both sides of the baseline run. Next tightest
is bank 5 at 3,381, then bank 2 at 7,505 and bank 12 at 8,639. `python3 tools/assemble.py check`
passes on the integration branch after this commit.

### V1. ⚠️ NEEDS THE DISC — `{FFEC}` insert widths, and this unit is the first to put twelve rows on §C4

**This is the highest-value item in PR #15 for a human with the disc, and §C4 has been open since it
was written.** `{FFEC}{=00}{=03}` (item name) and `{FFEC}{=00}{=01}` (number / price) have **no known
width bound**, and **both `assemble.py check` and `rowcheck.py script` strip them to 0 columns** — only
`{FFEC}{=00}{=00}`, the player name, is counted, at 7. **The column gate is therefore blind to twelve
rows in this unit and cannot be relied on for any of them.**

The translator's response was correct and is ratified: measure the English overhead carried beside each
insert and hold every row to a stated bound. **Remeasured at review, all six lines, and the bound
holds — maximum insert+8, against the Japanese's own insert+0 to insert+7:**

| Unique | Item row JP → EN | Price row JP → EN |
|---|---|---|
| 600 | +4 → **+8** (`，　ｉｓ　ｉｔ？`) | +4 → **+8** (`Ｔｈａｔ　ｉｓ　`) |
| 606 | +0 → **+1** (`，`) | +5 → **+8** (`　Ｊｅｗｅｌｓ．`) |
| 616 | +4 → **+8** | +7 → **+8** |
| 622 | +0 → **+1** | +5 → **+8** |
| 636 | +0 → **+1** | +4 → **+8** |
| 641 | +0 → **+1** | +5 → **+7** |

**What one visit settles.** If an item name can reach **16** columns these rows are safe. At **20**, the
two insert+8 item rows (600, 616) are one over — **and so is the Japanese** at insert+4 if a name
reaches 20, which is itself evidence the ceiling is lower than 20. **Go to any shop, select the longest
item name in the game, and read the price-confirm box.** That settles §C4 for these twelve rows **and
for all four remaining copies of this shop skeleton** (unique 592–598, 647–655), which are queued behind
it. Until then, no unit should spend a `{FFFE}` on these rows: a break bought with a guess is worse than
a measured bound.

⚠️ **Not grounds for a finding against any unit.** Measuring the overhead and declaring the bound is the
correct response to an unmeasurable gate, and it is what this unit did.

### V2. ⚠️ LIVE COLLISION — bank 41: the recall `そうだ、` must NOT take `Ｓａｙ，`

**§32.3 (PR #14, merged the same day this PR was reviewed) fixed `ねえ、` → `Ｓａｙ，`, shipped in
`chunk_020` L48. PR #15 had already drafted `そうだ、` (recall) → `Ｓａｙ，` and verified it free — which
it was, at drafting time.** Counted at review:

```
ねえ、   battle 4 in chunks [5, 15, 20, 32] | script 16 in banks [0, 18, 20, 28, 40, 41]
そうだ、  battle 4 in chunks [0, 5, 24, 39] | script 2  in banks [12, 41]
SHARED chunks [5]   SHARED banks [41]   messages holding both: 1   → §25.3 NOT MET
```

Ruled at **glossary §34.2** on the §32.5 precedent: `Ｓａｙ，` stays with `ねえ、` (shipped, 20
occurrences); the recall `そうだ、` → `Ｓａｙ，` **stands in `batch_006`** because bank 12 holds no
`ねえ、` at all.

> ⚠️ **WHOEVER TAKES BANK 41: its `そうだ、{FFEC}{=00}{=00}、王女様を探…` takes `Ｙｏｕ　ｋｎｏｗ，`
> (10 columns, verified free across `tl/` and `pending/`), NOT `Ｓａｙ，`.** With the name insert the row
> measures 19 columns. **Bank 41 has 353 bytes free** — the tightest bank in the project — so check the
> figure before spending anything.

The only message holding both is parked `chunk_005` msg 28, and it currently renders **neither** with
`Ｓａｙ，` (`ねえ、あなたたち、` re-flowed away, `そうだ、` dropped and carried by
`Ｆｅｉ，　ｗｏｎ’ｔ　ｙｏｕ　ｃｏｍｅ…`), so **nothing is visible today**. If chunk 5 is ever re-cut — it
already owes §23.2 and §24.3 corrections — apply the reserve there too.

### V3. ⚠️ LIVE COLLISION — bank 26: `いらっしゃいませ` and `ようこそ` in ONE message

`Ｗｅｌｃｏｍｅ` renders both `ようこそ` (shipped `chunk_007` L15) and this unit's three
`いらっしゃい`-family greetings. **PR #15's stated justification was wrong on the facts and is corrected
at glossary §34.5; the collapse stands on other grounds.** Counted at review:

```
ようこそ    battle 1 (chunk 7) | script 3 in banks [4, 26]        (PR said "battle chunk 7 only")
いらっしゃい  battle 4 (chunks 5, 6, 33) | script 21 in banks
            [12,13,15,16,17,18,19,22,25,26,43]                    (PR said "banks 12-15 and 43")
SHARED bank [26]   messages holding both: 1   → §25.3 NOT MET
```

The message is bank 26's casino greeter, both words on adjacent rows:
`いらっしゃいませ！！{FFFE}カジノへ　ようこそ！{FFFE}店の準備があるから、{FFFE}ちょっと待っててね。`

> ⚠️ **WHOEVER TAKES BANK 26** needs two forms in that one message. **The reserve is on the
> `いらっしゃいませ` side — `Ｃｏｍｅ　ｉｎ` (7 columns), verified free** — because
> `Ｗｅｌｃｏｍｅ　ｔｏ　ｔｈｅ　ｃａｓｉｎｏ` is the rendering English cannot avoid for `カジノへようこそ`.

### V4. ⚠️ LIVE COLLISION — bank 19: `あれ？` and `何？` both land on `Ｗｈａｔ？`

Not created by this unit — `chunk_020` L30 already ships `・・・あれ？` → `．．．Ｗｈａｔ？` (§32.3) and
§30.3 fixes `何？` → `Ｗｈａｔ？` (`chunk_008` L10, `pending/chunk_017`). `batch_006` unique 626 conforms
to shipped practice. Counted at review: `あれ？` chunk 20 + banks [1, 12, 16, 17, 19, 23, 41]; `何？`
chunks [7, 8, 17, 28] + bank [19]. **Shared bank 19, no shared chunk, 0 messages hold both.** Live for
bank 19's translator only; no reserve is named because no message forces it yet.

### V5. ⚠️ FORWARD BINDINGS — the four remaining copies of this shop skeleton

`batch_006` translates one of **five** copies of the same shop dialogue. The other four inherit its
wording; they must not re-invent it.

| Unique | What it is | What it inherits |
|---|---|---|
| **598** | the keigo shop's own buy/sell/leave menu — **byte-identical READABLE TEXT to 319 and 614**, different `{FFF6}` jump arguments | **`　Ｂｕｙ　ａｎ　ｉｔｅｍ` / `　Ｓｅｌｌ　ａｎ　ｉｔｅｍ` / `　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ`, byte-for-byte.** Strictly CLAUDE.md §3 does not force it — three different keys — but the player meets one menu in three shops. Leading `　` cursor gutter on all three |
| 592, 596 | `毎度あり！！` (the rough shop's thanks) | `Ｍａｎｙ　ｔｈａｎｋｓ` (§34.1) |
| 597 | `いらっしゃいませ。どんな　ご用でしょうか。` (the keigo greeting) | `Ｗｅｌｃｏｍｅ` + the source's punctuation; the keigo shop's **no-contractions-anywhere** register (§34.10) |
| 647 | the frog shop's copy of the closed-shop notice | The §34.1 notice wording. ⚠️ **Its source differs from 633's in two ways and both are deliberate**: it **has** the `。` before `」` that 633 omits, and its indent is **four** full-width spaces where 633 uses two. Reproduce each exactly |
| 333 | the plain copy of the same notice | Same wording, no tic, four-space indent |
| 648–655 | the frog shop (katakana, `ゲロゲロ`) | `Ｗｅｌｃｏｍｅ`, `ａｒｔｉｃｌｅ`, `　Ｌｅａｖｅ　ｉｔ`, `Ｍａｎｙ　ｔｈａｎｋｓ`. ⚠️ **Unique 652's bare `ゲロゲロ？` takes `Ｒｉｂｂｉｔ？`** — glossary §34.6 rules the parallel bare `ノロ？` → `Ｎｙｏｒｏ？` and that ruling binds it |

### V6. Three duplicate-check traps this unit leaves behind

Written down because each will read as a defect to a checker and is not one.

1. **Unique 319 and 614** are byte-identical readable text with different `{FFF6}` jump arguments
   (`{=03}/{=09}/{=10}` against `{=24}/{=2A}/{=31}`). **Their English is byte-identical** — verified
   mechanically at review: readable text equal, full field correctly unequal.
2. **Unique 601 and 630 carry the byte-identical ROW `ありがとうございます。` and render it differently**
   — `ｐｕｒｃｈａｓｅ．` in 601, `Ｔｈａｎｋ　ｙｏｕ　ｖｅｒｙ　ｍｕｃｈ．` in 630. **Not a divergence**: §3
   engages on the message, not the row (glossary §20.4, §24.5, §27.4, §31.4), and in 601 `お買い上げ`
   sits on the preceding row so the English redistributes across the break. Same class of trap as
   §24.5's `さあ、` before a `{FC00}` and §27.4's spaced / unspaced village line.
3. **Five EN-only leading full-width spaces (unique 606, 616, 622, 636, 641) are NOT stray gutters.**
   They are the separator after the `{FFEC}{=00}{=01}` price insert (`{FFEC}　Ｊｅｗｅｌｓ．`), which
   Japanese does not need and English does. The real gutter check is clean: **19 source segments begin
   with `　` and none lost it.**

### V7. `rowcheck.py script` — two new INHERITED pages, and the `_script_rows` artifact behind them

```
  ~  line 3195 page 2: 5 text rows > 4  (source already 5 — INHERITED)   = unique 606
  ~  line 3564 page 2: 6 text rows > 4  (source already 6 — INHERITED)   = unique 641
  columns OK; no page over 4 text rows that the source did not already exceed
```

**Confirmed at review to be this unit's and genuinely inherited**, by diffing the merged dump against
the committed baseline at those two line numbers — the untranslated source already carries 5 and 6
rows and the English adds none.

⚠️ **They are also a tool artifact and should not be "fixed".** `_script_rows` splits pages on
`{FCC0}` / `{FC30}` / `{FC51}` / `{FC50}` / `{FFFF}` but **not on `{FFFA}`**, so a yes/no menu block is
counted into the preceding text page. Both flagged pages are text page + menu block, not a five- or
six-row wall of prose. Lines 1234 and 8194 in the same listing are pre-existing and unrelated.

### V8. Unique 629 cannot be assigned to a shop

Its register is the rough male of unique 592–596, but its `{FFF8}{=00}{=04}` jump target matches the
**hobbit** block. Rendered in the plain rough-casual register the line itself carries
(`Ｏｏｐｓ，　ｓｏｒｒｙ！` / `Ｔｈａｔ　ｏｎｅ’ｓ　ｓｐｏｋｅｎ　ｆｏｒ．` / `Ｃｏｕｌｄ　ｙｏｕ　ｐｉｃｋ　ａｎｏｔｈｅｒ？`),
which is safe either way. **If a later batch places it, re-check** — if it turns out to be the hobbit's,
it wants the `ノロ` tic, which the source does not give it here.

### V9. Corrections this review makes to earlier work — recorded, none re-cuts a line

| What | Correction |
|---|---|
| **glossary §32.5** | Its reserve line says `ｔｏｋｅｎ` is *"verified free across `tl/` and `pending/`"*. **No longer true** — `batch_006` unique 631 ships `ａ　ｔｏｋｅｎ　ｏｆ　ｍｙ　ｔｈａｎｋｓ` for `感謝のしるし`, its first use anywhere. **The reserve survives**: the idiom sits in bank 12 and §32.5's `勲章`/`メダル` collision is live in banks 42–43, so §25.3's test is met between them. Corrected at glossary §34.7 — the sentence, not the ruling, exactly as §32.4 struck §28.3's "the alternative is free" |
| **`おっと` has three prior renderings, not two** | PR #15 named `chunk_007` L11 → `Ｎｏｗ　ｔｈｅｎ．` and `pending/chunk_043` L6 → `Ａｈ　ａｈ，`. Positional pairing at review found a third: **`chunk_007` L13 `おっと、` → `Ｎｏｔ　ｓｏ　ｆａｓｔ，`** — so one shipped chunk already renders its own two instances two ways. Ruled at glossary §34.3 as the §32.8 `何だ、` shape: a clause head, not a fixed form. **Nothing re-cut** |
| **Six figures in PR #15's body** | `ジュエル` → `Ｊｅｗｅｌｓ` is **7** instances, not 6; `失礼ですが` is byte-identical as a *phrase* but not as a *row* (22 vs 18 columns, and two different source strings); `ようこそ` is **4** occurrences across chunk 7 and banks 4, 26, not "battle chunk 7 only"; `いらっしゃい〜` reaches **11 banks + 3 battle chunks**, not "banks 12–15 and 43"; `ａｌｌ　ｒｉｇｈｔ` shares with **five** shipped/parked files, not two; `ｐａｃｋ` and `ｗｏｒｔｈ` are **not** free (`chunk_007` L13's herd sense, `chunk_012` L15's `ｐｒｏｖｅ　ｍｙ　ｗｏｒｔｈ`) — both harmless, both recorded |

### V10. Still open from earlier waves — untouched by this unit, listed so they are not lost

- **§T1 — the `あら` re-cut** of `chunk_007` L19 + L24, `chunk_011` L3 and `chunk_014` L3 (4 rows, 3
  files, all width-neutral or −6 bytes) is **still owed**. ⚠️ **PR #15 was the open PR §T1 named as a
  reason to defer, and it is now merged**, so the deferral's stated condition is discharged: this is now
  a clean §27-style corrections-unit job with nothing in flight against it. PR #15 **conforms** to
  §32.4 (`あら` ×1 → `Ｍｙ，`), so it adds nothing to the list.
- **§T2 — the `勲章` / `メダル` collision** is still live in banks 42–43, with `ｔｏｋｅｎ` as the reserve.
  See V9 above: the reserve is still usable but is no longer unspent.
- **§C4** — see V1. This unit is the first to put twelve rows on it.

---

## W. Wave 5 review — corrections/`あら` / PR #17 (2026-09-09)

**DECISION: MERGE at round 1**, squash-merged as **`f25ff14`**. Every §6 gate run in a real checkout
and pasted in the PR review; **no finding required a change to the unit**, and **every figure in the
PR body was correct as stated** — the second unit in the project for which that is true, after
chunk 20. Reviewer 1 of wave 5. Not a new unit of text: it applies glossary §32.4's `あら` ruling to
the shipped outliers, the §27 / PR #9 corrections-unit shape.

**Figures, all re-derived here rather than taken from the PR.** `tl/battle/chunk_007.txt`
**7,793 / 8,192, slack 399 (unchanged)** · `chunk_008.txt` **7,437 / 8,192, slack 755 (unchanged)** ·
`chunk_011.txt` **1,561 / 8,192, slack 6,631 (was 6,625 — −6 bytes)** · `chunk_014.txt`
**2,203 / 8,192, slack 5,989 (unchanged)**. Net **−6 bytes**, all in chunk 11. `assemble.py check` →
"All checks passed". An independent token-by-token diff against the pre-edit files confirms **zero
tag-stream changes on every line of all four files**, `{FFFE}` 154/155/34/41 unchanged, `{FCC0}`
9/15/3/4 unchanged, `{FFFF}` unchanged, line counts 34 / 21 / 15 / 14 unchanged, and **exactly five
readable runs changed — every one an `あら` row**. `rowcheck` was re-run on the **base** files and its
output is byte-for-byte identical except chunk 11's byte line, so **every `!!` and every
`{FFFE} changed` line is INHERITED**. Duplicate scan base vs after: **0 message-level divergences on
both sides, the same 19 distinct segment-level keys on both sides**. `bankmeasure.py` not required
(nothing under `tl/script/` changed) but run: **no bank negative**; the banks under 2,000 free are
**41 → 353** and **40 → 471**, both byte-for-byte untouched by this unit.

### W1. ✅ §T1 DISCHARGED — and its table was one row short

**Five rows in four files, not four in three.** `tl/battle/chunk_008.txt` **message line 4** ships
`{FCB0}{=000A0001}{FC51}{FFFD}あら？{FFFE}{FC00}{=0000}、来たわ！` and rendered `Ｏｈ？` — the identical
defect §32.4 names for `chunk_014` L3, on the identical source string, from a female 9th Army
companion (§29.6). Fixed at 3 → 3 columns, 0 bytes, no re-flow, against 755 bytes of slack.

**§32.4 counted chunk 8 and then dropped it.** Its census sentence names "chunks 7, **8**, 11, 13,
14, 16, 20 ×2, 27 and 29"; its *Lines this affects* table listed four rows and none was chunk 8's.
§T1 copied the table, the wave-5 dispatch copied §T1, and the omission travelled three documents
intact. Confirmed at review by an independent census of both dumps (below). `chunk_008` message line
15's `あらかた片付いたな。` is 粗方 and is correctly **excluded**. The dispatch's scope named three
files; its own verification clause ("if you find a fifth outlier … SAY SO and handle it") governs,
and the row is ratified. **Gate 1 passes on exactly four files.**

**After this merge `Ｏｈ　ｍｙ` occurs 0 times in `tl/` and `pending/`** and every `あら` interjection
in either tree renders `Ｍｙ`. Chunks 16, 27 and 29 are untranslated and inherit the form.

### W2. Three §4.3 record corrections applied at integration — all measured here first

Written into glossary §35.1–§35.3 and marked in place on the rows themselves, so nothing is silent.
**None changes a rendering.**

| Where | Was | Is |
|---|---|---|
| §28.3 `あら、` row | "The alternative `Ｏｈ　ｍｙ，` is also free" | **False** — `chunk_011` L3 shipped `Ｏｈ　ｍｙ，` for `あら、` itself. Struck. §32.4 struck it in §32.4's body but left §28.3 unamended, where a translator would actually look |
| §28.3 reach | "16 further (5 battle + 11 script-unique — both figures confirmed)" | **11 battle + 28 script-unique interjection instances = 39** (38 further). Out by >2× |
| §32.4 census | "12 `あら` rows in the battle dump" | **11**; 12 is the substring count. Chunk list unchanged and correct |
| §24.4 table | `おや` **6** battle | **4** interjection (chunks 1, 2, 31, 35); false positives `おやさしい方です。` and `おやすいご用です。` |

```
=== あら, by readable run ===            === おや, by readable run ===
battle: 12 substring / 11 interjection   battle: 6 substring / 4 interjection
        false pos: あらかた (chunk 8 L15)         false pos: おやさしい (ch7 L19), おやすい (ch23)
script: 31 substring / 28 interjection
        false pos: あらんことを ×2, 日を あらためて
```

⚠️ `おやさしい方です。` sits on **chunk 7 message line 19 — the very line carrying `あら・・・・？`**,
so both of §24.4's miscounts meet on a line this unit edits. Coincidence, recorded.

### W3. ⚠️ NEW — a positional duplicate checker can MIS-PAIR a re-flowed line, not merely skip it

PR #17's Flag 11 disclosed that index-aligned duplicate checkers cannot see a line whose `{FFFE}`
count changed, and named it as the likely reason chunk 8's row was missed. **Right in substance;
the mechanism is worse than "skip", and this was reproduced at review on the actual line:**

```
chunk 8, dump body line 4 (tl file line 5) — the fifth outlier's own line
  {FFFE} count               : JP 35  EN 34   -> a {FFFE}-ROW checker SKIPS the line (Flag 11 holds)
  ALL-TAG readable-run count : JP 40  EN 40   -> such a checker does NOT skip it
  it pairs  JP 'あら？'      with EN '，　ｔｈｅｙ’ｒｅ　ｈｅｒｅ！'
  and pairs JP '確かだしな。'  with EN 'Ｍｙ？'
```

A deleted `{FFFE}` and an added insert-adjacent run **cancel**, so the run counts match while the
content is shifted from index 32 onward. **For that checker shape the line is not skipped — it is
silently mis-paired**, which is strictly worse: it returns *wrong* answers rather than *no* answer,
and seeds the duplicate dictionary with garbage keys. Nothing broke here only because
`確かだしな。` and `あら？` are each unique enough that no comparison fired.

**For the next duplicate sweep:** pair on `{FFFE}`-delimited rows *and* on all-tag runs, treat a
line whose `{FFFE}` count differs as **unpairable by index in both shapes**, and fall back to a
content scan. This is the same family as §33.8's and §24.5's recorded traps and belongs beside them.

### W4. ⚠️ NEW — `tl/battle/chunk_001.txt` has no trailing newline, and it costs a sweep a whole chunk

Raised as PR #17's Flag 10 and **reproduced at review**: `chunk_001.txt` is the **only** file under
`tl/battle/` or `pending/` written without a trailing newline. Every other chunk file has one, and
the dump body carries a final empty-string sentinel that the trailing newline reproduces.
Consequence: `read().split('\n')` yields **19 body lines against the dump's 20**, and a positional
checker that guards on length **drops the entire file** — mine did, before I special-cased it.

**Not a defect in any unit and not a build problem** — `assemble.py check` and `rowcheck.py` both
tolerate it, and chunk 1's content is complete. But it is silent, and chunk 1 is the file carrying
ten `ノロ` instances and §23.4's known `助かった` correction, so losing it from a sweep is not cheap.
**Cheapest fix: append one newline** (0 bytes in the slot — the trailing newline is not part of the
chunk body) in whatever corrections unit next touches `tl/battle/`, or normalise in the checker.
Recorded rather than fixed here: this unit's scope is the five `あら` rows.

### W5. ⚠️ Speaker attribution — a PR flag corrected, and a caveat on §32.4's own aside

PR #17's Flag 7 calls `chunk_007` L19's speaker "portrait 02 (§21.4/§25.5/§28.6/§32.9's unnamed
female companion)". **In chunk 7 portrait 02 is Timmy** — the next segment is
`{FCB0}{=00010001}{FC51}{FFFD}どうした、ティミー？` → `Ｗｈａｔ　ｉｓ　ｉｔ，　Ｔｉｍｍｙ？`. **Portrait ids
are per-chunk** (§23.5 has Timmy at 0007 in chunk 4), so §32.4's aside that "the same-speaker
argument (portrait 02 in chunks 7, 14 and 20) is real" does not hold either. **Nothing changes** —
§32.4 says that argument settles *consistency*, not *which form*, and `Ｍｙ` is the fixed form
whatever the speaker. Glossary §35.5. **Registers of all five rows were checked and `Ｍｙ` suits
every one.**

### W6. Confirmed, not defects — recorded so they are not re-raised

- **`ｖｉｓｉｔｏｒｓ` correctly kept** in `chunk_011` L3: §34.1's `お客様` row requires it in terms
  ("§32.4's owed re-cut of `chunk_011` L3 keeps `ｖｉｓｉｔｏｒｓ`"). Only `Ｏｈ　` is removed, so the
  form stays spent and §34.1 needs no amendment.
- **Glossary additions "(none)" is right.** The unit renders no new term and promotes no §9 row.
- **`あれは・・・？` → `Ｉｓ　ｔｈａｔ．．．？`** (`chunk_014` L3) is a **different source string** from
  §21.2's `あれ・・・？` → `Ｗｈａｔ．．．？` and is unchanged by this unit. Not a divergence.
- **§Q2 not re-discovered.** No `{FCC0}` was added anywhere; the documented prompt/gate
  contradiction remains a documentation defect for a human and was not grounds for any finding.
- **Chunk 7's two `> 4 rows` warnings** (lines 23, 24) are the §D3 / §L2 pages carrying no
  `{FC50}`/`{FC51}`, already queued for the in-game check, and **byte-identical to base**.
- **Cross-PR:** none of the three sibling wave-5 units touches these files or this word — `あら` is
  absent from chunks 21 and 22 and from script batch 007's range (unique 318, 421–469, **0 hits**).
- **Branch `tl/corrections-ara` not deleted** — `git push origin --delete` is blocked by the proxy
  (HTTP 403). Harmless; not CLAUDE.md §8's "cannot push" condition.

### W7. Bytes and slack after this merge

Every chunk keeps far more than the 50-byte floor: chunk 7 **399**, chunk 8 **755**, chunk 11
**6,631**, chunk 14 **5,989**. The project is **6 bytes lighter**. **No bank moved** — this unit
touches no script file — so §F2's table is unchanged and banks 41 (353) and 40 (471) are
byte-for-byte as they were.

## X. Wave 5 review — battle chunk 21 / PR #18 (2026-09-09)

**DECISION: MERGE at round 1**, squash-merged as **`6276b4b`**. Every CLAUDE.md §6 gate run in a
real checkout and pasted in the PR review; **no finding required a change to the unit**. Reviewer 2
of wave 5. Three PR-body figures were wrong and are corrected here and in glossary §36.7 — none of
them touches the file, and the per-line `{FFFE}` table that gate 4 actually turns on is complete and
correct.

**Figures, all re-derived here rather than taken from the PR.** `tl/battle/chunk_021.txt`
**4,431 / 8,192, slack 3,761** — 45× the 50-byte floor. 863 JP → 1,809 EN readable characters =
**2.096×** against the **4.280** tier-D ceiling (`tag_bytes` 803, `english_budget` 3,694), **49.0 %**
of the budget spent; 863 / 5,663 / 4.28 all match `translation_prompt.md` §0.3's own table.
`assemble.py check` → "All checks passed". `rowcheck.py 21` prints no `!!` at all — no column over
24, no page over 4 text rows, tag parity clean — and the four `{FFFE} changed` lines it names are
exactly the four in the PR's Flag 2 with exactly the right before → after figures. **105 text rows**
(source 100), widest **23**, none at 24, ten at 23. `{FCC0}` **7 → 7** and none added, so `§Q2` was
not re-discovered. Duplicate sweep: **0 unpairable lines, 246 message keys, 1 divergence** (the
pre-existing `pending/chunk_005` village line, §X2) and chunk 21 on the conforming side of it.
`bankmeasure` not required (nothing under `tl/script/` changed) but run: **no bank negative**; banks
under 2,000 free are **41 → 353** and **40 → 471**, both byte-for-byte untouched, and bank 5 → 3,381.
`rowcheck.py script` → columns OK, only the three INHERITED over-4-row pages.

### X1. ⚠️ NEW — a PR figure that contradicts its own evidence table, and cannot be reproduced

The PR states "**`{FFFE}` 55 → 59 (+4)**". Measured against the dump the totals are **81 → 86, delta
+5**, and **the PR's own per-line table sums to +5** (7→8, 17→19, 0→1, 2→3). Five counting
definitions were probed at review, in case 55 was a defensible alternative measure:

```
definition                              JP     EN   delta
raw {FFFE}                              81     86      +5
text rows (rowcheck's own definition)  100    105      +5
row-separating breaks (rows - pages)    61     66      +5
breaks with text on both sides          61     66      +5
{FFFE} minus trailing-empty             61     66      +5
```

**Every definition gives +5, and no chunk in the battle dump has a source total of 55**, so this is
not §W3's scratch-file mix-up either. The figure is simply wrong and is corrected rather than
rationalised. **Two further figures in the same block are also wrong**: "57 text rows" is **105**,
and "nine rows at 23" is **10**. "Widest 23, none at 24" — the figure the column gate turns on — is
correct.

**Why this was a MERGE and not CHANGES.** Gate 4's requirement is that *every `{FFFE}`/`{FCC0}`
change appears in the PR's Flags*; all four do, per line, with the right numbers, and the required
byte figure is present and correct. What is wrong is a summary line that the gate does not rest on
and that `rowcheck` refutes in one command. Rework would have changed no byte of the unit. This is
the §S / §T / §U precedent — a reviewer correcting a PR's figures while ratifying its calls — and it
is recorded rather than waved through.

**Standing recommendation for future battle PRs:** state the `{FFFE}` total as `rowcheck` reports the
per-line diff, or omit the summary and give only the table. A summary that disagrees with its own
table is worse than no summary, because the table is right and the summary is what gets copied into
`HANDOFF.md`.

### X2. `pending/chunk_005.txt` L19 diverges from §27.2 — pre-existing, now queued in `pending/README.md`

Raised as the PR's Flag 12 and **reproduced independently at review** by the positional sweep:
`pending/chunk_005.txt` file line 19 renders `村が襲われました。` as
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ　ａｔｔａｃｋｅｄ．` against §27.2's binding
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．`, which chunks 7 ×2, 13, 17, 34 and now 21 all carry
byte-identically. **It is the only message-level divergence in the whole corpus** (246 JP keys) and
**chunk 21 is on the conforming side of it.**

**Not introduced by this unit and not live today** — chunk 5 is parked for the tier-A budget and
`assemble.py` reads only `tl/` — but it becomes a live CLAUDE.md §3 violation the day the slot patch
lands, which is exactly the §23.2 `Ｑｕｉｔｅ　ｓｏ．` shape. **Row added to `pending/README.md`'s
"Lines these files must adopt on re-cut" table**, measured at review: the current row is **24 columns
on one row** (at the hard limit, legal), the replacement is **14 / 13** — matching §27.2's own stated
figures — and it costs **+8 bytes**, taking chunk 5's re-cut total from +10 to **+18** (8,679 →
8,697 against 8,192). It does not change that file's feasibility; it needs the slot extension either
way.

⚠️ **§27.2's sentence "`tl/battle/` is free of divergent duplicate renderings for the first time in
the project" is TRUE and stays** — the claim is scoped to `tl/`, and `tl/` is still free. What was
missing is that the sweep behind it never covered `pending/`. §27.2's instance list does name chunk
5 among the thirteen; it simply does not say chunk 5 is already translated and disagrees.

### X3. ⚠️ `pending/` is a blind spot in BOTH directions, and this unit shows the good direction

§W3 and §W4 recorded `pending/` traps that lose information. This unit adds the mirror case, which is
worth having beside them because it looks like a defect and is not:

- **The bad direction** is §X2 — a `tl/`-scoped duplicate sweep does not see a parked divergence.
- **The good direction** is the PR's `相変わらず` row, which says "Free across `tl/`" — literally true
  — when `pending/chunk_005.txt` L29 **already renders the same phrase, and renders it identically**
  (`Ｓａｍｅ　ａｓ　ｅｖｅｒ，`). The row reads as if the form were being coined; it is being matched.
  Likewise `ええっ` → `Ｅｈｈ`, already drafted in `pending/chunk_043.txt` L43 — which that row *does*
  say.

**Both directions have the same fix: sweep `tl/` and `pending/` together and say which tree a hit is
in.** A "free across `tl/`" claim is not a freshness claim. Recorded in glossary §36.7.3.

### X4. Two glossary questions ruled, and one two-wave-old correction finally applied

- **§31.2's `〜め` re-scoped to third-person reference** (glossary §36.3). Its "Recurs as
  `この裏切り者め。` in chunk 21" clause is struck; direct address takes `Ｙｏｕ　〜` on §28.3's
  `馬鹿者！` model. `Ｙｏｕ　ｔｒａｉｔｏｒｓ．` ratified, with evidence the PR did not have — **two
  distinct 9th Army portraits (0000 and 0009) speak on `{FC51}` inside that one message**, so Ryan is
  not addressing one man. Reserve `Ｙｏｕ　ｔｒａｉｔｏｒ．` recorded. **No line changes.**
- **`とにかく` ruled register-selected** (glossary §36.2), on a five-instance trace the PR did not
  run: register predicts 5 of 5 renderings, the source comma predicts 2 of 5. **No line changes**;
  five further battle chunks inherit the row.
- **§1 and §2's rank widths patched IN PLACE** (glossary §36.4): 少尉 **17** not 18, 中尉 **16** not
  17, `Ａｎｓｅｌｍｏ` **7** not 8, `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` **24** not 25.
  ⚠️ **§29.5 measured this in wave 3 and deliberately recorded rather than patched; the wrong figure
  then travelled two waves and was restated in the wave-5 §9 seed as a new discovery.** Three
  independent measurements now agree, so it is applied rather than deferred a third time. **PR #20 is
  the project's first 中尉 rendering and now inherits a correct §2 instead of the trap.** The blanket
  "will not share a line with a name" is false — `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ，` is 23 and
  ships as one row; §29.5's contrary conclusion was reasoned on Cress (5 columns) and holds for
  Cress only. **No rendering anywhere changes.**
- **Glossary §10 question 8 (numerals in prose) CLOSED** (glossary §36.6): cardinals in running prose
  are spelled out; full-width digits stay in fixed names (§2's army numbers) and in tables of numbers
  (§15.1). Chunk 21 carries both sides on adjacent rows, which is why the rule had to be stated in
  that shape.

### X5. ⚠️ A correction against the wave-5 dispatch — four of five "cross-unit" terms are not in chunk 21

The dispatch told this reviewer that chunks 21 and 22 share five seeded terms — `ライアン`,
`クレス隊長`, `リオン将軍`, `ジェイク`, `５軍`. **Counted in chunk 21's source at review:**

```
ライアン 1   ２軍 1   クレス 0   リオン 0   ジェイク 0   ５軍 0   勲章 0   モンスター 0
```

**Only `ライアン` is cross-unit between #18 and #19.** `クレス` is battle chunks 8, 13, 22, 37;
`リオン` is 6, 22, 23; `ジェイク` is 22 only; `５軍` is 8, 13, 22 — none of them in chunk 21, which
therefore renders none of them and promotes none of them. The PR's Glossary-additions table promotes
exactly `ライアン` and `バトウ神父` and is right; the dispatch was wrong. **Consequence:** #18 merged
first, so **only the `ライアン` §9 row is left live** for #19's reviewer to strike, and `バトウ神父` is
promoted and struck here (`バトウ` is battle chunk 21 only, so it is not shared). There was never
anything for this merge to leave live on the other four.

### X6. Confirmed, not defects — recorded so they are not re-raised

- **`か。` rendered with interrogative syntax and a full stop is established practice.** Swept across
  every `か。` in `tl/battle/`: `chunk_002` L15/L21 and `chunk_006` L3/L4 already do it, and chunk 21
  L20's `Ｉｓ　ｔｈｉｓ，　ｔｏｏ，　ｔｈｅ　ｗｉｌｌ　ｏｆ　Ｇｏｄ．` is the fifth instance. The chunk's other
  two `か。` go declarative because they are realisations, not questions — a principled split, and the
  punctuation follows the source in all three. Glossary §36.8.
- **`ｕｎｄｅｒ　ａｔｔａｃｋ` twice in one chunk** — §27.2's village line (L11) and `攻撃を受けてる` (L5).
  Different source strings, §3 not engaged; recorded so a later sweep does not read L5 as a
  fourteenth §27.2 instance.
- **`{FCA8}` appears in this chunk** (L22, `{FCA8}{=01D3}`) but chunk 21 is **not** one of §D1's ten
  affected chunks and `check` passes. Coincidence, recorded so it is not mistaken for the artifact.
- **§Q2 not re-discovered.** No `{FCC0}` was added anywhere; the documented prompt/gate contradiction
  remains a documentation defect for a human and was not grounds for any finding.
- **Branch `tl/battle-021` not deleted** — `git push origin --delete` is blocked by the proxy (HTTP
  403). Harmless; not CLAUDE.md §8's "cannot push" condition.
- **Cross-PR:** #19 (chunk 22) and #20 (script 007) were both still open at this merge, verified in
  the PR list rather than assumed. Chunk 21 contains no `勲章`, no `モンスター`, and its one bare
  `２軍` takes the same `２ｎｄ　Ａｒｍｙ` the mid-wave relay sent to chunk 22, so nothing here
  constrains either.

### X7. Bytes and banks after this merge

Chunk 21 ships at **4,431 / 8,192, 3,761 slack**. The project's tightest battle chunk is still
chunk 19 at **127**. **No bank moved** — this unit touches no script file — so `FLAGS.md` §F2's table
is unchanged and banks 41 (353) and 40 (471) are byte-for-byte as they were.

---

## Y. Wave 5 review — battle chunk 22 / PR #19 (2026-09-09)

**DECISION: MERGE at round 1**, squash-merged as **`6423083`**. Every CLAUDE.md §6 gate run in a real
checkout and pasted in the PR review; **no finding required a change to the unit.** Reviewer 3 of
wave 5. Four PR-body figures and four justifications are corrected here and in glossary §37 — none of
them touches the file, and the per-line `{FFFE}` table that gate 4 actually turns on is complete and
correct.

**Figures, all re-derived here rather than taken from the PR.** `tl/battle/chunk_022.txt`
**4,153 / 8,192, slack 4,039** — 81× the 50-byte floor. 799 JP → 1,643 EN readable characters =
**2.0563×** against the **4.5857** tier-D ceiling (`tag_bytes` 863, `english_budget` 3,664),
**44.8 %** of the budget spent; 799 / 5,731 / 4.59 all match `translation_prompt.md` §0.3's own
table. `assemble.py check` → "All checks passed". `rowcheck.py 22` prints **no `!!` at all** — no
column over 24, no page over 4 text rows, tag parity clean — and the one `{FFFE} changed` line it
names (L05, 52 → 54) is exactly the one in the PR's Flag 2 with the right figures. **108 text rows**
(source 104), widest **23**, **eight at 23**, none at 24. `{FFFE}` **87 → 89 (+2)**, L05 only;
`{FCC0}` **11 → 11**, none added, so §Q2 was not re-discovered. Per-line bytes L01 448→786 ·
L05 1,482→2,544 · L06 290→528 · L07 142→196 — all four exact as stated. Duplicate sweep by the
positional method, 27 files indexed, 0 skipped: **0 whole-message divergences**, 0 page divergences,
7 byte-identical row reuses, 3 row-level differences all in different messages, **0 whole-message
hits in `tl/script/`**. `bankmeasure` **not required** (nothing under `tl/script/` changed) but run:
no bank negative; banks under 2,000 free are **41 → 353** and **40 → 471**, both byte-for-byte
untouched, bank 5 → 3,381. `rowcheck.py script` → columns OK, only the four **INHERITED**
over-4-row pages. `merge` prints **0** "never matched the dump"; `build/` reverted afterwards.

### Y1. ⭐ RULED — a possessive on the `{FC00}` player-name insert is ACCEPTED, and here is what it does and does not settle

`tl/battle/chunk_022.txt` L05 page 27 renders `{FC00}の話、` as
**`{FC00}{=0000}’ｓ　ｓｔｏｒｙ　ｆｉｔｓ`** (20 columns with the insert at 7). The PR raised it as a
project first and supplied a zero-cost alternative; **the possessive ships.** The reasoning, because
this is the same family as §C4 and the next unit will want it:

1. **`translation_prompt.md` §3.1 gives `Ｒｉｍｕｌ’ｓ` — a possessive on a proper name — as its own
   example of correct apostrophe usage.** A possessive on a name is contemplated by the contract.
2. **The only novelty is that the name is engine-substituted, and binding text directly to the
   insert's output is long-established.** Counted at review across `tl/` **and** `pending/`: **48
   rows in 14 files** put a character immediately after `{FC00}{=0000}` — `，` overwhelmingly, and
   also `．` (chunks 0, 2, 3, 8), `？` (chunk 2), `！` (chunks 14, 43) and a bare full-width space
   `　` (chunks 14, 21). `translation_prompt.md` §5's own worked example is `Ｉ’ｍ　{FC00}{=0000}．`
   Chunk 22 adds `’` as the **sixth** following glyph, 43 shipped rows after the first.
3. **`’` (U+2019) is a mapped glyph** — in §3.1's permitted set and in `rowcheck.ALLOWED`, already
   shipping in every contraction in the project — so nothing new is asked of the font hook.
4. **Both gates count the insert at its 7-character maximum** (`assemble.py` and `rowcheck.py`, via
   the `{FC00}{=0000}` → 7-column substitution), so a shorter player name only shortens the row.
   20 columns is the worst case, three under the ≤23 preferred limit.
5. **The one residual risk is not new to this unit.** If the engine pads the substituted name to 7
   characters, `Ｒｉｍｕｌ　　’ｓ` renders badly — **but so do all 48 of those shipped rows**
   (`Ｒｉｍｕｌ　　，`). The possessive therefore introduces **no new risk class**, only a new
   following character.

> **The precedent, for the next unit that wants one:** a possessive, or any other text, may bind
> directly to `{FC00}{=0000}`. **What is still unchecked is the same thing §C4 leaves unchecked** —
> what the insert actually renders as on screen, and in particular whether it is padded. **One visit
> to any map after name entry settles it, and it settles all 49 rows at once, not just this one.**
> Added to "Blocked — needs a human" item 4 as a rider on §C4's shop visit, not as a new trip.

The zero-cost alternative `Ｗｈａｔ　{FC00}{=0000}　ｓａｙｓ　ｆｉｔｓ` (22 columns — measured, the PR's
figure correct) is **not** taken: it costs 2 columns and one of the two `ｓｔｏｒｙ` echoes for no
reduction in risk, since risk 5 is shared with the comma rows either way.

### Y2. ⚠️ NEW — a SECOND cross-unit term between chunks 21 and 22, and why no dispatch would have caught it

The wave-5 dispatch named five cross-unit terms; §X5 corrected it to one (`ライアン`). **Both are
wrong: there are eight**, and the three the machinery missed are ordinary vocabulary rather than
seeded proper nouns. Swept at this review over every kanji/katakana run of ≥2 characters shared by
the two chunk sources, plus the kana-bearing phrase families that filter cannot see:

```
フェルナンド  c21 2  c22 7   Ｆｅｒｎａｎｄｏ            = Ｆｅｒｎａｎｄｏ                    ✓ §1
ライアン     c21 1  c22 1   Ｓｅｃｏｎｄ Ｌｉｅｕｔｅｎａｎｔ Ｒｙａｎ / Ｃａｐｔａｉｎ Ｒｙａｎ   ✓ source rank each
宮廷軍       c21 4  c22 2   Ｒｏｙａｌ Ａｒｍｙ           = Ｒｏｙａｌ Ａｒｍｙ                ✓ §2
将軍         c21 2  c22 2   Ｇｅｎｅｒａｌ               = Ｇｅｎｅｒａｌ                    ✓ §26.2
帝国         c21 1  c22 1   ｔｈｅ Ｅｍｐｉｒｅ            = ｔｈｅ Ｅｍｐｉｒｅ                 ✓ §2
つるむ    ★  c21 1  c22 1   ｉｎ ｌｅａｇｕｅ ｗｉｔｈ ｔｈｅ Ｅｍｐｉｒｅ  (both)               ✓ byte-identical
フン、    ★  c21 1  c22 1   Ｈｍｐｈ，                  = Ｈｍｐｈ，                       ✓ §6 / §36.1
つもりない ★ c21 1  c22 1   Ｗｅ ｈａｖｅ ｎｏ ｉｎｔｅｎｔｉｏｎ …  (same frame)              ✓ independently
```

**Eight shared terms, zero divergences, no re-cut.** Two units drafted in parallel by different
agents agreed on every one.

**The `つるむ` row's "`ｌｅａｇｕｅ` verified free" was TRUE when written** — at 02:37Z both PRs were
open and neither was in `tl/` — and became false when #18 merged an hour before this review.

> **This is §X3's blind spot failing on TIME instead of on tree, and it is structural.** §X3 recorded
> that a `tl/`-scoped freshness claim cannot see `pending/`. This one could not see the **future**: a
> sibling PR's forms enter `tl/` between drafting and review, so **a translator's freshness sweep can
> only ever be a snapshot, and re-running gate 7 against the tree as it stands at merge is the
> reviewer's job.** It cannot be delegated upward to a better dispatch, because no seed list will
> ever contain `つるむ`, `フン` or a `〜つもりはない` frame.
>
> **Recommended, and it cost one script: at the SECOND merge of any wave that ships two battle
> chunks, intersect the ≥2-character kanji/katakana runs of the two sources and compare the English
> on every hit.** It catches exactly the class the seed list cannot.

### Y3. Three reach figures that searched the wrong tree — all three agree anyway

Same mistake three times, and it is §35.3's "a substring grep is not a census" from the other side:
the counts were right, the **trees** were not. **No rendering changes.**

- **`５軍`.** §9's seed said "`tl/script/batch_005.tsv` already carries a `５軍` line, so **grep it
  before writing**". The translator did exactly that and reported honestly. But `５軍`'s five battle
  occurrences are chunks **8, 13 and 22**, and two were already shipped: **`chunk_013` L2 ships bare
  `５軍` → `ｔｈｅ　５ｔｈ　Ａｒｍｙ`, the exact string this unit uses.** A match recorded as a coinage.
- **`ありがとう。`** Flag 12 names `chunk_004` L10 as the one shipped `Ｔｈａｎｋ　ｙｏｕ．` it differs
  from by a capital. There are **seven** — `chunk_004` L10, `chunk_007` L19, `pending/chunk_005` L28,
  `pending/chunk_043` L41+L42, `pending/chunk_043_abridged` L41+L42 — four of them in `pending/`.
- **The duplicate table** names one file per row where several have two: `まったく、` also
  `chunk_012`, `・・・・・` also `chunk_010`, `・・・・` also `chunk_018`, `はっ！` also `chunk_013`.

### Y4. Four PR figures corrected, and one justification replaced while the rendering stands

**None touches the file.** §X1's shape a second time, so its standing recommendation now has two
instances behind it: state a summary as the tool reports it, or omit it and give only the table.

1. **`{FCC0}` "untouched at 8" — the count is 11** (L01 3, L05 6, L06 2). *Untouched* is correct and
   verified per line; only the number is wrong, and it is the number that reaches `HANDOFF.md`.
2. **Flag 2's two rejected three-row splits are 23, not 24** (`Ｅｍｐｉｒｅ` is 6 columns):
   `ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ　Ｅｍｐｉｒｅ？` = 23, `ｔｈｅ　Ｅｍｐｉｒｅ？　Ｉｓ　ｉｔ　ｔｒｕｅ？` = 23.
   A legal three-row split exists (8 / 21 / 23), so the added `{FFFE}` was **elective, not forced**.
   **It stands** on §3.2's own advice to spend free bytes on breaks at high ratio; the shipped
   8 / 19 / 18 / 11 has headroom where the alternative sits on the 23 ceiling.
3. **`ａ　ｍｉｓｕｎｄｅｒｓｔａｎｄｉｎｇ` is 18 columns, not 16.** Conclusion unaffected.
4. **Flag 9's "three-way echo of 話" is two-way** — L05 p01's `という話は` correctly dissolves and
   renders no *story*.

**Flag 7's `ｌｅｄ　ｂｙ　Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ！` = 24 is CORRECT, but `ｕｎｄｅｒ` was not
forced.** A four-row recut of the same page keeps the literal inside 23 (18 / 23 / 23 / 17, no new
`{FFFE}`, no `{FCC0}`). `ｕｎｄｅｒ` **stands** — standard military English for the identical relation,
plot fact intact, and the alternative ends a row on the two-letter `ｂｙ` against §3.2. It is a choice
between two soft constraints, not a forced §2.1 step 4, and glossary §37.6 records it as such.
**Flag 4's `Ｂｅｙｏｎｄ　ａｌｌ　ｂｅｌｉｅｆ，` ratified** (glossary §37.5) with one correction: L01
plays **before** the L05/L06 fork, not "in the other branch", so the `belief` / `believed` echo is
visible in one playthrough — benign, different Japanese, §3 not engaged.

### Y5. ⚠️ Two readings left OPEN rather than hardened into facts

- **The `ライアン` two-title question** (glossary §37.4). §9's seed proposed the promotion reading as
  "likelier" and the PR agreed. **The renderings are ratified; the reading is not.** In chunk 21
  `ライアン少尉` is spoken by **portrait 0000, a 9th Army soldier addressing an officer over him**; in
  chunk 22 `ライアン隊長` is spoken by **portrait 0006, Ryan's own subordinate**. An outsider using
  the substantive rank and his own man using the functional address accounts for both **with no
  promotion at all** — and §2's own 隊長 row already calls 隊長 a function. Neither reading is
  decisive and **nothing rides on it**, because §26.2's source-rank rule is correct either way. The
  test: a scene holding `ライアン少尉` and `ライアン隊長` together, or a third rank. `ライアン` is
  battle 21 and 22 only, so the question may stay open permanently and harmlessly.
- **Flag 10's portrait mechanism.** Every attribution in it is correct. `{FCB0}{=00PP00SS}` assigns
  portrait **PP** to **slot SS**, and `{FC50}` / `{FC51}` speak from slot 0 / slot 1 — which
  *predicts* Cress's move to slot 1 exactly when Jake takes slot 0, and is the only reading that
  covers **L05 p06** (`フェルナンドを？どういうことだ。`), a page carrying **no `{FCB0}` at all**.
  ⚠️ Consistent with §23.5 / §28.7 / §30.7 but **derived inside chunk 22 only** and, per §W5, not
  carried to any other chunk. It is an observation for `findings.md` if a later chunk corroborates
  it, **not** a settled engine fact, and no reviewer should lean on it across a chunk boundary yet.

### Y6. ⚠️ NEW — Cress's gender is unfixed, unrendered, and battle chunk 37 will force it

Glossary §1's `クレス` row states no gender. **This PR's own body uses both** — "he" in the Unit
summary, "her" in the `クレス隊長` glossary row. **No shipped English anywhere genders Cress** —
`chunk_008` L4, `chunk_013` L1/L2 and this unit are all first-person, vocative or subject-less — so
there is **no defect today and nothing to re-cut.**

Raised because **`クレス` occurs in battle chunks 8, 13, 22 and 37**, and 37 is untranslated. A
third-person line there forces the pronoun, and a wrong choice would be a §4.3 correction reaching
three shipped files. What the corpus offers: Cress's speech here is `私` / `お前` / `〜のか` /
`〜てくれ` / `よい`, the neutral-to-masculine officer register of §7 with nothing feminine-marked —
**not enough to fix it.** Whoever takes chunk 37 (or the script lines at `クレス少尉`) settles it and
records the evidence.

### Y7. Confirmed, not defects — recorded so they are not re-raised

- **§Q2 not re-discovered.** No `{FCC0}` was added anywhere; the three pages at the four-row wall
  (L01 p12, L05 p34, L05 p44) were solved inside the source's own page structure. The documented
  prompt/gate contradiction remains a documentation defect for a human and was grounds for nothing.
- **§T2's `メダル` collision untouched.** `勲章` ×2 ships as `ｍｅｄａｌ` (§32.1), matching
  `chunk_020` L47/L48. This chunk is the first place the plot explains the item, but it is a battle
  chunk and reaches **no bank**, so the live banks 42–43 collision is neither worsened nor discharged
  and the `ｔｏｋｅｎ` reserve is unspent.
- **`{FCA8}` appears once** (L07) and chunk 22 is **not** one of §D1's ten affected chunks; `check`
  passes. Same coincidence §36.8 recorded for chunk 21.
- **`ｄｏ　ｎｏｔ　ｐｕｓｈ　ｔｏｏ　ｈａｒｄ．` vs `chunk_008`'s capitalised form**: the source strings
  genuinely differ (`ムチャ` here, `無理` there — verified in the dump), so §3 is not engaged in
  either direction, and `chunk_013`'s third form is correctly untouched.
- **Gate 6's own trap, hit and fixed at this review.** A positional row index that strips
  `{FC00}{=0000}` to nothing rather than to a placeholder **manufactures** a divergence: it paired
  chunk 14 L3's `{FC00}隊長！` → `Ｃａｐｔａｉｎ　{FC00}！` against this chunk's `隊長！` →
  `Ｃａｐｔａｉｎ！` and reported a stray space in shipped work that is not there. **Substitute the
  insert on both sides before comparing**, exactly as `assemble.py` and `rowcheck.py` already do.
  Third entry in the §W3 / §W4 / §X3 checker-trap family.
- **Branch `tl/battle-022` not deleted** — `git push origin --delete` is blocked by the proxy (HTTP
  403). Harmless; not CLAUDE.md §8's "cannot push" condition.
- **Cross-PR:** #20 (script batch 007) was still open at this merge, verified in the PR list rather
  than assumed. Chunk 22 touches no `tl/script/` file and none of its terms is in unique 318 or
  421–469 (`５軍`'s two script lines are 524 and 995, both outside that batch), so nothing here
  constrains #20.

### Y8. Bytes and banks after this merge

Chunk 22 ships at **4,153 / 8,192, 4,039 slack**. The project's tightest battle chunk is still
chunk 19 at **127**. **No bank moved** — this unit touches no script file — so §F2's table is
unchanged and banks 41 (353) and 40 (471) are byte-for-byte as they were.

---

## Z. Wave 5 review — script batch 007 / PR #20 (2026-09-09)

**MERGED at round 1** as `11af9e78`. `tl/script/batch_007.tsv` — `script_unique.txt` file lines 318
and 421–469, 50 unique lines / **70 message instances**, 3,015 JP → 6,306 EN = **2.092×**,
**7,074 bytes** across 21 banks. Every §6 gate run and pasted; full reading review line by line.
**No finding required a change to the unit.** Glossary section **§38**.

### Z1. NEEDS THE DISC — the three `『』` UI screen labels (BLOCKED, needs a human)

⚠️ **This is the item on the Blocked list, and glossary §9 explicitly asked the reviewer to raise it
rather than resolve it.**

`tl/script/batch_007.tsv` unique **431** and **437** tell the player to go and find three menus on
screen:

| Japanese | Shipped English | Columns |
|---|---|---|
| `『編成』` | `“Ｆｏｒｍａｔｉｏｎ”` | 11 |
| `『キャラクター育成』` | `“Ｃｈａｒａｃｔｅｒ　Ｇｒｏｗｔｈ”` | 18 |
| `『キャラを入れる』` | `“Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ”` | 17 |

**The menu strings themselves are in NEITHER dump.** They live in the executable or in a graphics
table, not in `SCRIPT.BIN` or `HEXMAP.BIN`, so an English label here **cannot be verified against
what the screen actually shows** — and if the menus stay Japanese, the instruction sends the player
to a menu whose name does not match. All three widths are correct as remeasured, and `『…』` → `“…”`
follows §12, so **nothing here is a defect**; the risk is a mismatch with a surface this project
does not yet control.

**What the human has to do:** open the Formation screen in-game and read the three menu entries. If
they are still Japanese, either (a) the labels here should be re-cut to describe the menu rather
than name it, or (b) the menu strings need to be found and translated too. Either way it is one
look at one screen.

Note that §26.3's **verbal** 編成 → `form (your units)` is a different thing and is untouched: the
same unit uses it correctly twice in unique 437 where the source is verbal, which is the source's
own split.

### Z2. FORWARD BINDING — this unit fixes the recruiter menu for TEN untranslated lines

⚠️⚠️ **UPDATED 2026-09-09 at `batch_008`'s merge (PR #21), on two counts.**
**(a) Four of the nine are now shipped.** `tl/script/batch_008.tsv` renders this menu **four times**
— its DATA 472, 483, 493, 504, which are **this entry's 477, 488, 498, 509** — byte-for-byte
identical to `batch_007`, gutter included, verified mechanically. **Five remain untranslated:
this entry's 334, 335, 399, 405, 417** (= DATA 329, 330, 394, 400, 412), and **unique 417 is still
the head of the rough human recruiter whose tail `batch_007` renders**. Seven of the twelve rows now
carry the string.
**(b) ⚠️ THE NUMBERS IN THIS ENTRY ARE `script_unique.txt` FILE LINES, and the wave-6 documents
count DATA lines — the two differ by exactly 5.** This entry's 440/450/461 are DATA 435/445/456;
its 334/335/399/405/417/477/488/498/509 are DATA 329/330/394/400/412/472/483/493/504. `HANDOFF.md`
warned that `batch_007` and `batch_008` number differently and glossary §9's wave-6 citations were
corrected to DATA twice; **this is the same clash reaching FLAGS**. Neither convention is wrong —
what is wrong is citing one without saying which. **State the convention beside any line number.**
See glossary §42.5.

Counted mechanically at review across `script_unique.txt`, not taken from the PR.

**The three-option recruiter menu** ` 兵士を　補充したい` / ` 情報を　聞きたい` / ` 何でもない`
→ **` Ｒｅｃｒｕｉｔ　ｓｏｌｄｉｅｒｓ` / ` Ａｓｋ　ｆｏｒ　ｉｎｆｏｒｍａｔｉｏｎ` / ` Ｎｏｔｈｉｎｇ`**
(leading `　` cursor gutter on all three) is **byte-identical readable text at twelve unique lines**.
Three are now shipped — 440, 450, 461 — and **nine remain untranslated: 334, 335, 399, 405, 417,
477, 488, 498, 509.**

**`他に　用はないノロか？` → `Ｎｏｔｈｉｎｇ　ｅｌｓｅ，　ｎｙｏｒｏ？`** binds **unique 470**, the
tenth.

All ten carry different `{FFF8}` jump arguments and are therefore **different keys**, so CLAUDE.md
§3 does not *force* reuse. But the player meets one menu at every recruiter, which is exactly
§34.9's reasoning for unique 598 and the shop menu. **Whoever takes any of those ten lines should
copy the English byte-for-byte and not re-invent it.**

⚠️ **Unique 417 is one of the nine**, and it sits inside the untranslated head (416–420) of the
rough human recruiter whose tail this unit renders at 421–426. So that head inherits **both** the
menu strings *and* the register contrast this unit built: the human says
`Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ` / `ｔｉｍｅ！` where the hobbits say `…ｔｉｍｅ，　ｎｙｏｒｏ．`, and
`Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ` appears in both.

### Z3. FORWARD OBLIGATION — Torif's birth order now lives in exactly two lines

Unique 455 renders `第２王子のトリフ様` as `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ`, per glossary §9's seed, and
**drops the ordinal**. Ruled at review and it stands — see glossary §38.5 — on the measurement that
`第２王子` occurs **exactly once in the entire script dump (that line) and zero times in the battle
dump**, while the same fact is carried **twice more by `弟のトリフ`**.

⚠️ **Those two `弟のトリフ` lines are now the only place in the game where Torif's birth order
survives.** Whoever renders them **must keep the younger-brother fact** — it is what glossary §9's
`ホアグ王子` row turns on (Hoag is Carline's first prince, Torif the pliable younger brother Helfer
prefers as heir). Not a defect today; a thing that becomes one if it is dropped a second time.

### Z4. Six PR-body figures corrected at review, none touching the file

Recorded so they are not inherited. Every **headline** figure in the PR was correct as stated and
re-derived at review — 50 / 70, 2.092×, 7,074 bytes, all 21 bank movements, 367 rows, widest 23,
17 at 23, none at 24, `{FFFE}` +6 on the five named lines, `{FCC0}` untouched.

1. **`兵舎`** — the PR's *correction to glossary §9* is itself wrong. Measured: 4 in
   `script_dump.txt`, 1 of them the unit's own → **3 further, 4 in total**. §9's "4 script" is
   **right**. The PR's 3 is the unique-line count.
2. **`ワイン`** — "35 further" is **41** (44 total − 3 own). §9's "44 script-dump instances" is right;
   its "24 unique" is 18.
3. **`リムローズ`** — "9 further" is **10** (14 − 4 own). Banks [18, 20, 40, 41] and 2 battle in
   chunk 38 are exact.
4. **`上官`** — "used unchanged 3×" is **2×**. Unique 431 carries 上官 three times; the third
   (`貴官の上官となる`) renders the bare `ｙｏｕｒ　ｓｕｐｅｒｉｏｒ，　Ｆｉｒｓｔ`, an unflagged §2.1
   step-3 shortening forced by width (the full form gives 28 columns). Rendering stands.
5. **`ｖｉｓｉｔｏｒ`** — "chunks 11, 33, 35" is **11 and 33**; `chunk_035.txt` has no `ｖｉｓｉｔ`
   in any form.
6. **`おい、`** — "12 battle chunks" is **11** (0, 8, 16, 20, 23, 27, 31, 32, 37, 38, 43; 14
   instances). Banks [5, 41] correct and **not bank 2**, so §25.3's test still passes. `おいおい`
   "twice more (banks 29, 41)" is exact.

⚠️ **A seventh, to a claim rather than a figure: Flag 7's "the unit contains no §2.1 step-6 reorder
at all" is false.** Unique **422** reorders — the source puts the conjecture
(`地殻の変動が激しいのか`) before the main clause (`妙な噂を聞くぜ`) in one sentence; the English
puts the main clause first and the conjecture second, in two. **The rendering stands** (nothing
added or dropped, the page keeps its four rows and its `{FCC0}` in the source's place, and fronting
a Japanese parenthetical `〜のか` is close to forced in English) — but the flag was owed. Glossary
§38.6.

### Z5. §Y3's staleness trap — checked, and it did not fire here

§Y3 records that a translator's "verified free" is only a snapshot, and that `つるむ`'s went stale
between drafting and review because a sibling merged in between. **This PR was written before three
merges** (#17 `f25ff14`, #18 `6276b4b`, #19 `6423083`), so every reach and freedom claim was
re-measured against the **post-merge** tree at review, not accepted on report.

**All of them still hold.** `ｎｕｔ` (only hit *minute*), `ｗｉｎｅ` (only hits *swine*),
`ｂａｒｒａｃｋｓ`, `ｇｒｅｅｄｙ`, `ｒａｎｋｓ`, `ｓｔｒｉｆｅ`, `ａｒｒａｎｇｅ`, `ｗａｎｔｅｄ　ｍｅｎ`,
`ｊｏｉｎｔ　ｏｐｅｒａｔｉｏｎｓ`, `ｐｏｔａｔｏ`, `ｃｉｔｙ　ｆｏｌｋ`, `ｂｕｔｔｅｒ`,
`ｍｏｓｔ　ｗｅｌｃｏｍｅ`, `Ｌｉｍｒｏｓｅ`, `Ｅａｔｏｎ`, `Ｃｈｅｋｏｔ`, `Ｔｏｒｉｆ`, `１ｓｔ　Ａｒｍｙ`
— free on the current tree. `ｒｅｃｒｕｉｔ` correctly **not** free (`chunk_000` L4's noun).

⚠️ **One glossary claim DID go stale, and it is not the PR's.** Glossary **§29.4** says
"`Ａｇｒｅｅｄ` is **verified free across all of `tl/`**". It is not, since PR #16 merged:
`tl/battle/chunk_019.txt` L25 ships `・・・わかった。` → `．．．Ａｇｒｅｅｄ．` — **which is exactly
what §29.4 prescribed for chunk 19**, so the reserve was spent as designed, not violated. **Nothing
is re-cut and no line changes.** But **the わかる family now has no reserve left**: a future unit
that puts `わかった` beside `了解` in one segment will have to fix a new form. Recorded here rather
than patched into §29.4, per §4.3. This unit is unaffected — it renders `わかった。` → `Ｒｉｇｈｔ．`
(§6, the source's own stop) and contains **no `了解`**; 了解 is script bank 5 only, battle chunks
3, 17 and 19.

### Z6. Bytes and banks after this merge

| Bank | before | after | spent |
|---|---|---|---|
| **2** | 7,505 | **3,365** | −4,140 |
| **3** | 10,591 | **8,113** | −2,478 |
| 5 | 3,381 | 3,357 | −24 |
| **40** ⚠️ | 471 | **447** | −24 |
| 4, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 25, 33, 42, 43 | | | −24 each |
| **41** | 353 | **353** | **0 — byte-for-byte untouched** |

**21 banks moved, 7,074 bytes, no bank negative.** Measured by removing the file, re-merging and
re-measuring — **every figure in the PR body is exact.**

⚠️ **§F2's tight list is now: bank 41 at 353 free, bank 40 at 447, bank 5 at 3,357, bank 2 at
3,365.** **Bank 2 has moved into the tight group** — it was the binding bank for this unit
(1,866 of its 3,015 JP characters, a 3.01× ceiling against the 2.09× actually spent) and it is now
the project's fourth-tightest. **Whoever plans the next script batch must check bank 2's headroom
before dispatching**, as this wave's coordinator correctly did.

Unique 318's own cost, which the dispatch asked for: **+24 bytes in each of 21 banks, 504 in
total** — 21 English columns against 9 Japanese characters. Bank 40's ceiling for that one line was
**244 English characters**, so "keep it short" was never binding there; **bank 2 was**.

No battle chunk moved — this unit touches no battle file — so the tightest chunk is still
**chunk 19 at 127 bytes of slack**.

---

## AA. Wave 6 review — battle chunk 24 / PR #24 (2026-09-09)

### ⚠️ AA0. SECTION NUMBERING — single letters are exhausted, and the scheme is now DOUBLE LETTERS

`FLAGS.md` ran `A` … `Z` at one section per review and **§Z was the last single letter**. From this
review the scheme is **double letters: §AA, §AB, §AC, §AD, …**, the ordinary spreadsheet-column
convention, which sorts and reads unambiguously beside the existing single letters. **This review
takes §AA.** As always, the next section is taken by **reading this file at commit time, never by
reservation** — the remaining wave-6 reviewers (PR #23, #22, #21) should each read to the end and
take the next free double letter.

### AA1. Decision and gates

**MERGE.** `paths ✓ merge ✓ check ✓ figures ✓ rows ✓ banks n.a. dupes ✓ glossary ✓ structure ✓`
Squashed as **`f1d1581`**. Reviewed at `origin/tl/battle-024` (`31eefd4`) merged onto the
integration branch at `0f261dd`; the merge took only `HANDOFF.md` and did not conflict.

`git diff --name-only` = `tl/battle/chunk_024.txt` alone. `assemble.py check` → **All checks passed**.
`rowcheck.py 24` prints **no `!!` at all** — no tag-parity, column, row or charset finding — and only
`{FFFE} changed: line 7: 2->3, line 10: 20->21`, both in the PR's Flag 5 with before → after.

**Every figure in the PR body was re-measured and is exact**, except the two labelling errors at
AA2. Independently measured with `rowcheck`'s own algorithm (`NAME_COST=7`, `COLS=24`):

```
chunk 24: 5913 / 8192 bytes  slack 2279
TEXT ROWS  src 155  tl 157      WIDEST tl 23 ; at 23 = 12 ; at 24 = 0 ; over 24 = 0
READABLE chars: src 1210  tl 2478  ratio 2.0479
tag_bytes = 953 ; english_budget = 3619.5 chars ; ceiling = 2.9913
{FCC0} 14 -> 14   {FFFF} 18 -> 18   {FC30} 38 -> 38   {FC50} 22 -> 22   {FC51} 17 -> 17   {FC00} 6 -> 6
```

Ellipsis profile re-measured by **splitting on tags** (§33.8's trap) and counting `・・・。` as a
four-`．` cluster, which is §3.1's own rule: JP `{2:2, 3:17, 4:6, 5:2}` against EN `{2:2, 3:17, 4:6,
5:2}` — **exact match**. The single-stop difference (JP 31, EN 32) is L15's one sentence split.

**No battle chunk moved but this one; the tightest chunk is still chunk 19 at 127 bytes of slack.**
No bank moved — this unit touches no script file.

### AA2. Gate 6 was run by the POSITIONAL method, and chunk 24 introduces zero divergences

A battle `tl/` file holds no Japanese, so grepping one for a source string is a null check. The
checker (`r024_dupes.py`, namespaced per §Y-era practice) pairs dump body line *i* with `tl` line
*i* across **28 files** in `tl/battle/` and `pending/`, strips trailing blanks so `chunk_001`'s
missing trailing newline does not drop the file (§W4), and marks lines whose `{FFFE}` count changed
as row-unpairable (§W3 / §Y7).

```
positional pairs: 633   (row-unpairable lines: 83)
WITHOUT 043_abridged                       divergent whole = 0  divergent rows = 9
WITHOUT 043_abridged AND WITHOUT chunk 24  divergent whole = 0  divergent rows = 9
NEW divergences introduced by chunk 24 (whole): []      (rows): []
```

⚠️ **Two traps this run leaves behind for the next reviewer to reuse.**

1. **`assemble.split_battle` returns a body list with a TRAILING BLANK separator line**, so a naive
   `len(body) == len(tl_lines[1:])` check fails on **every file in the corpus** and the checker
   silently reports zero pairs and therefore zero divergences. It looks exactly like a clean pass.
   Strip trailing `''` from the dump body as well as from the `tl` file.
2. **`pending/chunk_043.txt` and `pending/chunk_043_abridged.txt` are two translations of the SAME
   dump chunk.** Left in, they produce **31 spurious "divergent whole-message renderings"** that
   have nothing to do with the unit under review. Exclude `_abridged` from any corpus-wide
   consistency pass, or attribute every hit before reporting one.

The residual **9 row divergences are pre-existing** and untouched by this unit — short rows such as
`お前は、` and `もう少し` playing different grammatical roles in different sentences.

Chunk 24's only content recurrences are byte-identical to shipped work:
`{FC00}{=0000}、` → `{FC00}{=0000}，` (`chunk_007` 20.1, `chunk_022` 5.7) and `そして、` → `Ａｎｄ，`
(`pending/chunk_043` 13.2). The honorific inserts, which the row key does not pair, were checked
separately: `{FC00}{=0000}君、` → `{FC00}{=0000}，` follows `chunk_020` 47.5, and `chunk_014` 2.13
keeps a **rank** where this drops an **honorific** — English has no *-kun*, it has *Captain*.

### AA3. ⚠️ `様` on an unresolved referent is rendered `ｍｙ　ｌｏｒｄ`, which COMMITS TO A MALE PATRON

`tl/battle/chunk_024.txt` body line 6 (file line 8), Fernando's death line:
`話が違いますぞ、` / `・・ル・・・様・・・` → `ｏｕｒ　ｂａｒｇａｉｎ，` / `．．ｌ．．．　ｍｙ　ｌｏｒｄ．．．`

Fernando dies half-naming the patron who betrayed him. The source gives one middle syllable, `ル`,
which identifies nobody — `ヘル ファー`, `ギル フォード` and `リム ル` all contain it — and the
translation reproduces that with a lowercase `ｌ`, the letter all three romanisations share. The dot
runs are exact (2 / 3 / 3 both sides). **That part is right.**

**What is open:** `様` → **Lord** for a male superior and **Lady** for a female one (`glossary.md`
§1, `ヘルファー様` → `Ｌｏｒｄ　Ｈｅｌｆｅｒ`; `リムル` → `Ｌａｄｙ　Ｒｉｍｕｌ`). `ｍｙ　ｌｏｒｄ` therefore
**commits to a male patron**, and **nothing in the corpus settles it.** Two of the three candidates
are male (`ギルフォード様` → `Ｌｏｒｄ　Ｇｕｉｌｆｏｒｄ`, §32.1) and one is female (`リムル様` →
`Ｌａｄｙ　Ｒｉｍｕｌ`, §1), which is the one that would break the row.

**Action for whoever renders the chunk that names Fernando's backer: re-check this row.** It is 4
columns either way (`ｌｏｒｄ` / `ｌａｄｙ`), so the fix would cost no re-flow and no byte. Chunk 25
(PR #23) puts Helfer at the centre of the conspiracy — `ヘルファーが張本人よ` — which **points at**
`Ｌｏｒｄ　Ｈｅｌｆｅｒ` but does not prove the referent of this fragment. **Left open deliberately;
NOT resolved at this review.**

### AA4. Cross-unit with chunk 25 (PR #23, open, NOT merged) — two agreements, two divergences

Verified byte-for-byte against `origin/tl/battle-025`, which had not merged when this ran.

**Agreeing, and the §9 rows therefore stay LIVE** (the `ルート` precedent, glossary §29.1 / §30.1 —
struck by the **second** of the pair to merge; chunk 24 is the **first**, so nothing was struck):

- `王位` → `ｔｈｅ　ｔｈｒｏｎｅ`. Chunk 24 `王位継承を巡って` → `ｓｕｃｃｅｅｄ　ｔｏ　ｔｈｅ　ｔｈｒｏｎｅ．`;
  chunk 25 `僕は王位なんか狙ってはいない` → `Ｉ　ｈａｖｅ　ｎｏ　ｄｅｓｉｇｎｓ` / `ｏｎ　ｔｈｅ　ｔｈｒｏｎｅ`.
- `恨み` → `ｇｒｕｄｇｅ`. Chunk 24 `一族の恨み` → `Ｔｈｅ　ｇｒｕｄｇｅ　ｏｆ　ｔｈｅ　ｋｉｎ`; chunk 25
  `お前たちに恨みはないが、` → `Ｉ　ｂｅａｒ　ｙｏｕ　ｎｏ　ｇｒｕｄｇｅ，`; parked `chunk_043` 13.3 agrees.

Also agreeing across the two: `Ｔｏｒｉｆ`, `Ａｒｉｅｓ`, `Ｆｅｒｎａｎｄｏ`, `Ｈｅｌｆｅｒ`, `Ｈｏａｇ`,
`Ｃｏｍｍａｎｄｅｒ`, `ｔｈｅ　Ｅｍｐｉｒｅ`, `ｗａｒ`, `Ｐｒｉｎｃｅ`, `ｋｉｎ`, `ｍａｇｉｃ`, `Ｇｕｉｌｆｏｒｄ`,
`Ｒｉｍｕｌ`. `何者` is correctly **not** a fixed form — chunk 24 renders it twice, `ｉｔ　ｓｅｅｍｓ
ｓｏｍｅｏｎｅ` (indefinite) and `ｊｕｓｔ　ｗｈｏ　ｏｎ　ｅａｒｔｈ　ａｒｅ　ｙｏｕ？` (interrogative), which is
the §32.8 shape.

**Diverging — for the chunk 25 reviewer to settle, not chunk 24's defect:**

1. ⚠️ **`そして、` — chunk 24 ships `Ａｎｄ，`, chunk 25 ships `Ａｎｄ　ｔｈｅｎ，`** (line 11, page 31).
   **Chunk 24 matches the earlier shipped work**, `pending/chunk_043.txt` 13.2's `Ａｎｄ，`, so the
   change belongs to chunk 25 — and `Ａｎｄ　ｔｈｅｎ，` adds a temporal sense the `〜のも … 〜のも`
   list does not carry. Not gate-6, because chunk 25 is not in `tl/` yet.
2. ⚠️ **`どけっ` is cross-unit and NEITHER PR nor the dispatch listed it.** Chunk 24 9.7 `どけっ、` →
   `Ｍｏｖｅ！`; chunk 25 11.58 `どけっ！` → `Ｏｕｔ　ｏｆ　ｍｙ　ｗａｙ！`, with `どかないと` → `Ｍｏｖｅ，`
   on the next row — so `Ｍｏｖｅ` does double duty across the pair for two different source words.
   Different source strings, so nothing is gate-bound, and §6's `行くぞ！` → `Ｍｏｖｅ　ｏｕｔ！`
   (`chunk_009`, `chunk_014`) is unaffected. **Wants a ruling.** Chunk 24 also has `そこをどいて！`
   → `Ｓｔａｎｄ　ａｓｉｄｅ！`, a third form of the same act, which is fine as a third source string.

### AA5. ⚠️ A STALE "FREE" CLAIM THAT BELONGS TO PRs #23 AND #21 — `末えい` → `ｄｅｓｃｅｎｄａｎｔ` IS ALREADY SHIPPED

`glossary.md` §9's wave-6 seed proposes `末えい` → `ｄｅｓｃｅｎｄａｎｔ` as a new form at "1 instance
each" (chunk 25 and `batch_008`). **It is neither new nor two instances.** `tl/battle/chunk_010.txt`
12.2 already ships:

```
誇リ高キ　龍人族ノ　マツエイダ。  ->  Ｗｅ　ａｒｅ　ｄｅｓｃｅｎｄａｎｔｓ　ｏｆ / ｔｈｅ　ｐｒｏｕｄ　ｄｒａｇｏｎｆｏｌｋ．
```

— the same word in the lizardmen's **full-katakana** register (§5). **The seed's CHOICE is confirmed
by shipped work**, which is the good news; only the novelty and reach claims were wrong, and §9 is
patched in place accordingly. Chunk 24 does not use the word.

⚠️ **This is a THIRD spelling class past §Y2's blind spot.** §Y2 recommends a ≥2-character run
intersection; wave 5 found it misses **kanji+kana** (`つるむ`, `末えい`); this review finds it also
misses **full katakana** (`マツエイ` for `末えい`), which is a *register* transform, not a spelling
variant, and which no search over the kanji form can ever find. The corpus already has the same
problem recorded for `ウエストバリー` / `ウェストバリー` (§2). **Any cross-unit sweep must normalise
katakana↔kanji↔kana before intersecting**, and must run against the whole of each sibling source
rather than against a seed list — this is the third consecutive wave to be bitten.

### AA6. `しまった` is RULED (glossary §39.4), and its recorded reach was wrong

Flag 12 asked for the ruling and supplied a census that is wrong in three ways: the page indices
(13.0 / 7.0 / 45.0 for what are really 13.1 / 7.1 / 45.1), the case (`Ｄａｍｎ　ｉｔ` where two of the
three ship lowercase `ｄａｍｎ　ｉｔ`), and the reach ("13 battle chunks + 8 script", which counts the
verbal auxiliary `〜てしまった` — five of the 13 battle hits and six of the 7 script hits).

**RULED at glossary §39.4:** line-initial `しまった` → `Ｏｈ　ｎｏ`; after a grunt → `ｄａｍｎ　ｉｔ`,
lowercase, capitalised only where it opens a sentence — §5's mechanism, the word fixed and the
punctuation following the source. **The interjection reaches 8 battle chunks (0, 5, 8, 14, 16, 20,
24, 37) + 1 script line; six are rendered, and the ruling binds the two that are not — chunk 16 L2
and chunk 37 L0, both line-initial, both `Ｏｈ　ｎｏ．．．`.**

### AA7. `{FCC0}` — §Q2 stands, but its stated mechanism is one step off

Not re-raised as a finding, correctly. For the record, the briefing's framing ("both gates reject
it — `assemble.py:125-126` and `rowcheck.py:93-94` exempt only `{FFFE}`") conflates two different
checks:

- **`rowcheck.py` DOES honour `{FCC0}` as a page boundary** — `row_problems` splits on
  `\{(?:FCC0|FC30|FC51|FC50|FFFF)\}` (line 78) and `col_problems` does the same (line 66).
- What forbids it is **`tag_parity`**, in both tools, which requires every tag except `{FFFE}` to
  survive in the same order — so `{FCC0}` may be neither **added** nor **removed**, but a `{FCC0}`
  the source already has is counted as a page break by the row and column checks.

So §Q2's practical rule is right (the prompt tells translators to add one and the gates will fail
them) and its cause is narrower than stated. Chunk 24 has 14 in and 14 out.

### AA8. §9 corrections applied IN PLACE in this integration commit

Per the run's 2026-09-09 "patch in place, do not merely record" decision. **All six verified by the
reviewer before applying**, and the glossary rows carry the correction inline with the date and
PR number, per §4.3.

| # | What was wrong | Corrected to |
|---|---|---|
| 1 | §9 line ~520 read `Ｐｒｉｎｃｅ　Ｔｒｉｆ’ｓ　ｆａｃｔｉｏｎ` | `Ｔｏｒｉｆ` — fixed at §9 line 290, promoted at §38.1, shipped at `batch_007.tsv` L56. `Ｔｒｉｆ` occurs **nowhere** in `tl/` or `pending/` |
| 2 | Same row read "**21 / 21** columns" | **21 / 22** — `Ｔｏｒｉｆ` is 5 columns to `Ｈｏａｇ`'s 4, `len()`-measured |
| 3 | `古代文明` cited as "unique 473" | **DATA line 488** |
| 4 | `魔族` / `末えい` / `司教様` cited as "unique 483" | **DATA line 498** — 483 is a *menu* line, as the block's own FACT 1 says |
| 5 | `ウェストバリー` cited as "unique 505" | **DATA line 515** |
| 6 | "`batch_008` is 47 lines but only **~26** distinct translations" | **32** — 47 − 22 in groups + 7 groups |
| 7 | `ライトエルフ` / `オーラスマッシャー` attributed to **Torif** | **ARIES's** — Gilford says `確かにライトエルフの末えいのようだな` to Aries, who then finds `オーラスマッシャー` useless. Renderings unaffected; only the note was wrong |
| 8 | `末えい` seeded as new, "1 instance each" | Already shipped in `chunk_010` — see AA5 |

⚠️ **The numbering method matters and the dispatch's gloss for it was wrong.** The dispatch said each
bad figure was "exactly `unique − 470`"; it is not (488 − 473 = 15, 498 − 483 = 15, 515 − 505 = 10 —
inconsistent). The real mapping is **`batch_008.tsv`'s own declared convention**: its header reads
*"script_unique.txt DATA lines 470-516 … 'DATA line' = tools/queue.py script_rows() numbering:
1-based over script_unique.txt"*, i.e. **counting data rows only, skipping the file's 3 comment and
2 blank lines**, so **DATA line = FILE line − 5**. Measured: `古代文明` is FILE 493 = DATA 488,
`魔族`/`末えい`/`司教様` FILE 503 = DATA 498, `ウェストバリー` FILE 520 = DATA 515. The corrected
figures are right; the arithmetic offered for them was not. `batch_007.tsv`'s header says **FILE
lines**, so **the two batch files use different conventions** — check the header before citing a
number. This is the seventh numbering convention in the repo (§O8, §P).

❌ **NOT applied, and must not be:** PR #23's Flag 15 says §9's `末えい` → `ｄｅｓｃｅｎｄａｎｔ`
"10 columns" should be 11. `len('ｄｅｓｃｅｎｄａｎｔ')` = **10**. The seed was right and that flag is a
hand-count one high. The §9 row now records the measurement so it is not "corrected" a third time.

### AA9. PR figures corrected without changing a byte (glossary §39.3)

Six, all recorded rather than sent back, on the wave-5 precedent that a measured figure error in a
PR body is fixed by the reviewer at merge:

1. The faction "20 / 18" are **row** widths; the **phrases** are **16 / 17**. Numbers right, label
   wrong. The page is 23 / 22 / 20 / 18, exactly as the PR states.
2. **`ｂｌｏｗ` is not free** — `batch_001.tsv` L10 ships §4's fixed `一撃必殺` →
   `ｋｉｌｌｉｎｇ　ｗｉｔｈ　ｏｎｅ　ｂｌｏｗ．`
3. **`ｂｉｒｔｈ` is not free** — `batch_007.tsv` L31 ships `ｍｙ　ｂｉｒｔｈ　ｖｉｌｌａｇｅ`.
4. **`ｐｌｏｔ` renders three source words, not two** — `batch_005.tsv` L36's `Ｈｅｌｆｅｒ’ｓ　ｐｌｏｔ．`
   was missed by the §25.3 accounting.
5. **`Ｈｍ．`'s census misses `chunk_004` 4.6** (`ん・・・？` → `Ｈｍ．．．？`).
6. **`ｍｙ　ａｐｏｌｏｇｉｅｓ．` ships lowercase**, correctly; the additions table capitalises it.

**All of 2–5 still pass §25.3's co-occurrence test, so not one line changed.** ⚠️ The lesson for the
remaining wave-6 units: **"verified free" is a measurement, and three of this unit's were not
measured.** That is `FLAGS.md` §Y3's failure mode in its other direction — not stale, simply
unchecked — and it is cheap to catch: one grep of `tl/` and `pending/` per claimed-free word.

### AA10. Nothing here needs a human, and nothing is blocked

No `{FCA8}` §D1 artifact tag. `check` green on the integration branch after integration. Chunk 24
is complete and shippable. The one item left open on purpose is **AA3**, the `様` gender commitment,
which needs a later chunk to name Fernando's patron — not a human, and not a blocker.

## AB. Wave 6 review — battle chunk 26 / PR #22 (2026-09-09)

### AB1. Decision and gates

**MERGE**, squash `e96b259`, integration commit `integrate: chunk 026 — glossary, flags, handoff`.
Reviewed at `b3c07da` merged onto `b720967` — i.e. **after chunk 24 landed**, so every corpus claim
in a PR opened against `3ec89d0` was re-measured rather than accepted (§Y3's staleness-by-time).

```
paths ✓   exactly tl/battle/chunk_026.txt (A), nothing else
merge ✓   clean, 'ort', no conflict
check ✓   All checks passed.
figures ✓ 5,325 / 8,192, slack 2,867 — 139 text runs, MAX 23 columns, 0 at 24, 0 over
rows   ✓  0 pages over 4 text rows; {FFFE} +3 (body L11 1→2, L14 58→60), both declared
banks  n.a. (battle unit)
dupes  ✓  positional, 28 files, 0 misaligned; 279 JP messages → 0 divergent
glossary ✓ every term conforms; 12 new rows + register table; no entry changed by the PR
structure ✓ {FFFF} last on all; header/{=FF}/{PAD 5115} verbatim; 0 charset violations;
            18/18 ellipsis dot counts exact; single trailing newline, no CRLF
```

**This is the first unit of the run whose PR figures needed NO correction at merge.** Every reach
count, bank list and column width in the PR body was re-measured and is exact — including the two
that are easy to get wrong: `len('Ｈｕｍａｎｓ　ａｒｅ　ｎｏｔ　ｆｏｒｇｉｖｅｎ！')` = **24** and
`len('Ｈｕｍａｎｓ　ｗｅ　ｎｏｔ　ｆｏｒｇｉｖｅ！')` = **22**, both as claimed.

### AB2. ⚠️ RULING — the `そして、` → `Ａｎｄ，` rule is POSITIONAL, and was briefed too broadly

**This is the finding most likely to cost a later unit a round, and it is a correction to the
dispatch, not to the PR.** Every wave-6 agent was briefed that "`そして、` → `Ａｎｄ，` IS RULED, and
chunk 26 carries it". Chunk 26 carries a `そして`, but **not the construction the rule covers**, and
applying the rule mechanically would have damaged the line.

Measured across every `そして` in the battle dump — the reach figure is otherwise **exact as
briefed**, 10 battle (chunks 5, 16, 24, 25, 26, 39, 43) + 9 script (banks 1, 9, 32, 41):

| Where | Source | Shipped English | Shape |
|---|---|---|---|
| `chunk_024` L15 seg15 | `そして、` **alone on its row** | `Ａｎｄ，` | opens a new sentence |
| `chunk_043` L13 seg2 | `そして、` **alone on its row** | `Ａｎｄ，` | own coordinating row |
| `chunk_005` L15 seg10 | `そして　くれぐれも` | `Ａｎｄ　ａｂｏｖｅ　ａｌｌ，` | **no comma** |
| `chunk_043` L3 seg7 | `そして　ここは、` | `Ａｎｄ　ｔｈｉｓ　ｉｓ　ｔｈｅｉｒ` | **no comma** |
| `chunk_043` L32/33 seg0 | `そして、空に移り住んだ` | `Ａｎｄ　ｔｈｅ　ｌｅａｄｅｒｓ　ｗｈｏ` | **no comma** |
| `chunk_026` L14 row3 | `そして、極めて残忍です。` | `ａｎｄ　ｕｔｔｅｒｌｙ　ｃｒｕｅｌ．` | **list-final, lowercase** |

**The comma in `Ａｎｄ，` is not part of the word — it is the row ending where the source's `、`
ends it.** Chunk 26's `そして、` is the final conjunct of a three-item predicate list opened three
rows earlier by `彼らは、`; `Ａｎｄ，　ｕｔｔｅｒｌｙ　ｃｒｕｅｌ．` would capitalise a conjunction
mid-sentence and put a comma after "And" that no English style permits. Ruling written up at
**glossary §40.4**: alone on its row → `Ａｎｄ，`; continuing into its own clause → lowercase `ａｎｄ`,
no comma. `Ａｎｄ　ｔｈｅｎ` stays reserved for `それから`. **Five of the six shipped instances already
agreed with this;** only the two that stand alone on a row carry the comma.

### AB3. ⚠️ The stutter convention is `Ｘ，　`, measured 8 : 1 — and two shipped/parked outliers

PR #22's gate-6 row table declares **one** row divergence (`まさか、`). There are **two**: the
byte-identical source row `な、何をするっ！？` is rendered two ways.

```
tl/battle/chunk_026.txt L15   Ｗ，　ｗｈａｔ　ａｒｅ　ｙｏｕ　ｄｏｉｎｇ！？   23 cols
pending/chunk_043.txt   L27   Ｗ‐ｗｈａｔ　ａｒｅ　ｙｏｕ　ｄｏｉｎｇ！？    22 cols  (PARKED)
```

All **12** stutter rows in the corpus were surveyed before ruling. `Ｘ，　` is the shipped
convention **8 to 1**: `Ａｈ，　`(c00), `Ｉｍ，　`(c07), `Ｗ，　`(c07), `Ｙ，　`(c07), `Ｗ，　`(c08),
`Ｌ，　`(c14), `Ｗ，　`(c24), `Ｎ，　`(c24), plus chunk 26's own `Ｓ，　Ｓｅｔｉ．．．` and this row.
**The `Ｘ‐` outliers are three: `chunk_000` L2's `Ｔｈ‐ｔｈｉｓ．．．` — which is internally
inconsistent with its own `Ａｈ，　` on the SAME line — and the two in parked `chunk_043`**, which
`assemble.py` never reads. **Chunk 26 was not changed.** ⚠️ **Left OPEN for whoever next touches
`chunk_000` or unparks chunk 43:** align them to `Ｘ，　`, or rule the other way and re-cut the
nine. Not urgent — `chunk_043` is parked and `chunk_000` is one row — but it will keep resurfacing
until someone rules, and the row is not gate-bound because the containing messages differ.

### AB4. ⚠️ RULING — `大歓迎` is context-sensitive; §38.2 CORRECTED IN PLACE; chunk 15 unblocked

PR #22's Flag 7 is **confirmed on both halves**. `glossary.md` §38.2 fixed one form and its own
reach note lists chunk 7, yet **`tl/battle/chunk_007.txt` body L3 (file line 5) already ships
`Ｓｕｃｈ　ａ　ｗａｒｍ　ｗｅｌｃｏｍｅ！`**. Both were verified at review. Reach re-measured: **4 battle
(chunks 7, 15, 26) + 6 script (banks 0, 3)** — exactly as the PR states.

Ruled at **glossary §40.3** and §38.2 **patched in place** (§4.3, dated, with the PR number):
`大歓迎` is ordinary vocabulary, not a coined term, and takes the English its clause needs. The
binding precedent is this run's own `残念だけど` decision — **CLAUDE.md §3 engages on the MESSAGE,
not the phrase** — and the three source messages differ, so **gate 6 is not engaged and neither
chunk 7 nor chunk 26 is re-cut**. Ironic (chunks 7, 26) → a *warm / most welcome* phrasing fitting
the row; sincere (chunk 15) → `Ｍｏｓｔ　ｗｅｌｃｏｍｅ` (12).

⚠️ **For chunk 15's dispatch, and this is the part that would have been expensive later: its two
`大歓迎` instances are ONE sentence.** Dump L11's text is a strict **suffix** of L10's (a scene with
two entry points — measured, not inferred: `len(L10)=547`, `len(L11)=232`, `L10.endswith(L11)` is
true). The two are **not** byte-identical messages, so gate 6 does not bind them, but the shared
sentence `そう言うことなら大歓迎だ！！` must be rendered **byte-identically in both**. Suggested:
`Ｉｎ　ｔｈａｔ　ｃａｓｅ，` (13) / `ｙｏｕ’ｒｅ　ｍｏｓｔ　ｗｅｌｃｏｍｅ！！` (21).

### AB5. ⚠️ `Ｃａｐｔａｉｎ` renders two source words and §25.3 is only HALF met — banks 28 and 41

Re-measured at review, both figures exactly as PR #22 Flag 6 claims:

```
船長  1 battle [26]  + 3 script, banks [23, 28, 41]
隊長  24 battle [1,2,3,6,7,8,13,14,16,19,22,23]  + 10 script, banks [2, 10, 28, 32, 34, 41]
```

**Chunks are disjoint — chunk 26 carries no 隊長 — so nothing shipped is affected and nothing was
re-cut.** But **banks 28 and 41 hold both**, so whoever translates them gets a ship's captain and a
squad captain in one bank. English has no second word that is not a register slip (`ｓｋｉｐｐｅｒ` is
far too colloquial for the scene). **A decision for those banks' translator, recorded now so it is
not a discovery then.** Bank 41 is already one of the four nearly-full banks (§F2).

### AB6. Treize is the L10/L11 dark elf — CONFIRMED on the channel, and portrait ids are SCENE-LOCAL

PR #22's Flag 2 proposed it from the portrait id and called it unproven. Re-tested at review on the
**`{FC50}`/`{FC51}` channel**, as PR #23's ruling requires, and it **strengthens rather than
breaks**: the triple **(id 0006, channel `{FC51}`, selector `FA11`) is constant across L3, L10, L11
and L15**, and in L15 Seti addresses that exact speaker with the vocative `トレーズ、` and it answers
`セ、セティ・・・助けてくれ。` The content chains independently — L11's `この私が、人間などに・・`
is a defeat by humans; L15's `傷だらけになって` / `新しく来た人間どもだ` / `油断して、不覚をとった`
each presuppose it. **Consequence: chunks 27, 28 and 29 inherit a haughty, uncontracted,
human-despising Treize** (glossary §40.2, §40.5).

⚠️ **A general finding that outlives this PR: `{FCB0}` portrait ids are SCENE-LOCAL, not global.**
Chunk 26 proves it internally — **id 0007 on `{FC50}` is the katakana-pidgin mook in L7's scene and
Seti in L15's**, which is coherent with Annette's `あれは魔族の中でも下級の者たち` and is why the two
demon registers are correctly *not* levelled. **This extends §Y2 and PR #23's "portraits are not
speakers" ruling: an id is only comparable within one scene, so identifications must be made on the
(id, channel, scene) triple.** Residual caveat: chunk 26 contains **no `{FB00}` tag at all**, so no
id is tied to an image here; chunks 27–29 can still overturn the identification.

### AB7. Two briefing claims corrected against the tree — measured pushback

Both were checked before acting, and **neither was applied**:

1. **`場所` has NO §9 row.** The dispatch stated that "`魔族` and `場所` pair chunk 26 with batch
   008" and to leave both live. `grep -c 場所 glossary.md` = **0**; `場所` appears nowhere in
   `glossary.md` or `FLAGS.md`. Only `魔族` has a row. **Nothing to strike or leave live for
   `場所`**, and PR #21's reviewer should not hunt for one. Recorded at glossary §40.7.
2. **§Q2 does NOT record the wrong cause, and was NOT patched.** The dispatch asked for §Q2 to be
   patched "if it records the wrong cause". Read at review, §Q2 says: *"Both gates reject it.
   `tools/assemble.py:125-126` and `tools/rowcheck.py:93-94` build the tag parity list as … only
   `{FFFE}` is exempt, so any added `{FCC0}` fails as 'tag stream changed'."* **All four line
   numbers are exactly the `tag_parity` lines in both files** (verified: `assemble.py:125-126`,
   `rowcheck.py:93-94`), and both tools do reject an added `{FCC0}` there. §Q2 never claimed the
   row or column checks reject it — the conflation was in the **briefing**, and **§AA7 (PR #24)
   already records the correction**. Patching §Q2 would have introduced an error. **§Q2 stands
   unchanged; §AA7 remains the place the nuance is recorded.**

### AB8. Cross-unit — chunk 26 is the FIRST of its pair to merge, verified by reading the tree

At merge time `tl/battle/chunk_025.txt` and `tl/script/batch_008.tsv` are both **absent** from
`claude/workflow-translation-iterate-uzlkns` (checked twice: before review, and again after chunk
25's rework commit `8177dbd` landed on the branch, which does **not** merge the unit).

- ⚠️ **`魔族`'s §9 row is LEFT LIVE** and annotated in place. It pairs this unit with `batch_008`
  (PR #21, open). **PR #21's reviewer strikes it**, per the `ルート` precedent (§29.1 / §30.1).
- **`末えい`, `フフ`/`ふふ`, `それから`, `魔物` and `ｄｅｓｃｅｎｄａｎｔ` do not occur in chunk 26.**
  Nothing here propagated PR #23's Flag 15 miscount (`ｄｅｓｃｅｎｄａｎｔ` is **10** columns, and §9
  already carries the measurement), and §12.3 / §32.7's `Ｆｕｆｕ` is not engaged.
- **Bank check: none.** Battle unit; no bank moved. No bank crossed under 2,000 free at this merge.

### AB9. Nothing here needs a human, and nothing is blocked

No source typos found, no tag meanings guessed, no `{FCC0}` added or removed, no byte over budget,
2,867 bytes of slack left in the chunk. `check` passes on the integration branch after this commit.
The three items left open for later units — the `Ｘ，　`/`Ｘ‐` stutter outliers (§AB3), the
`Ｃａｐｔａｉｎ` collision in banks 28 and 41 (§AB5), and confirming Treize's identity from chunk 27
(§AB6) — are all decisions for a translator or reviewer, not for the human.

---

## AC. Wave 6 review — battle chunk 25 / PR #23 (2026-09-09)

Merged at **round 2**, squash `68ba7f4`, after one CHANGES round with two findings. Both were fixed
in one line and one commit, both independently re-verified by the translator against the tree before
pushing, and neither was argued with. Third of wave 6's four units to merge, after chunks 24 and 26.

**Measured at review on `dacd7ab`, merged onto `0ce2df6`:** **5,403 / 8,192 bytes, slack 2,789** —
1,039 JP → 2,220 EN characters = **2.1367×** against a **3.4837** tier-C ceiling, 61.3 % of budget.
**129 text rows** (source 124), widest **23**, **ten** at 23, **none at 24**, no page over four.
`{FFFE}` **101 → 106**, `{FCC0}` **11 → 11**, `{FFFF}` 14, `{FC50}` 27, `{FC51}` 23, `{FC00}` 2,
`{PAD 5161}` — all unchanged, non-`{FFFE}` tag stream byte-identical on all 18 lines. Gate 6 by the
positional method over **29 files and 1,256 indexed source runs** with a live self-test: **0
duplicate obligations**, 0 chunk-25 messages present as `script_unique` keys.

### AC1. ⚠️ THE STANDING FINDING — a kana-script search finds only its own script, and this is now the THIRD distinct search blind spot this run

Finding 1 of round 1 was `フフ・・、` → `Ｈｅｈ　ｈｅｈ．．，` against §12.3's fixed `ふふ` → `Ｆｕｆｕ`.
The translator's own diagnosis at round 2 is the part worth keeping: **it grepped `フフ`, `フッ` and
`フン` — all katakana — and never `ふふ` in hiragana.** The glossary row it needed was there and its
search could not reach it, because a kana search is a *script* search.

**Three distinct classes of term are now known to be invisible to the obvious search, and each cost
a real finding:**

| class | example | what fails | first cost |
|---|---|---|---|
| maximal kanji run | `王位継承` vs bare `王位` | a run intersection never pairs them | §Y2, wave 6 — missed by both units' dispatch lists |
| mixed kanji + kana | `末えい`, `恨み`, `つるん` | a kanji-run sweep drops them entirely | §Y2 / §9, waves 5 and 6 |
| **kana-script variant** | **`フフ` vs `ふふ`; `グフッ` vs `ぐふっ`; `クッ` vs `くっ`** | **a search in one kana script cannot see the other** | **§AC, this review** |

> **Rule, for every agent: search a term in BOTH kana scripts and in the kanji, before concluding a
> form is new.** `フフ` → `ふふ` is a `str.translate` away; there is no excuse for it being manual.
> This matters most for interjections and laughs, which is precisely where the glossary collapses
> spellings onto one English (§17.2 鬼 / オーガ, §11.5 くっ / クッ, §28.3 何っ / 何ッ, §29.3
> くーっ / く〜っ, §30.3 ぐふっ / グフッ, §32.7 ふふ / ふふっ).

⚠️ **A second, sharper point the translator found and the reviewer did not: §12.3's own row already
listed `Ａｌｔ　Ｈｅｈ　ｈｅｈ　—　ｓｅｅ　ＦＬＡＧＳ`.** The shipped form was not merely a new
invention, it was **the alternative that row had already considered and rejected.** A glossary row's
"Alt" column is a record of rejected options, not a menu.

Reach for whoever takes chunk 39: `ふふ` **8 battle** (chunks 20, 28, 31, 33) **+ 1 script**;
`ふふっ` 1 + 1; `フフ` 2 (chunks 25, 39) + 1; `フフッ` 1 (chunk 39) + 1. **All four take `Ｆｕｆｕ`.**

### AC2. `そして、` — the rule, its condition, and the collision it discharged

Finding 2 of round 1 was bare `そして、` → `Ａｎｄ　ｔｈｅｎ，` where merged `chunk_024` and parked
`chunk_043` both ship `Ａｎｄ，` **for the same speaker in the adjacent chapter**. Fixed to `Ａｎｄ，`.

The rule as it now stands, combining this and §40.4 (chunk 26's review, which narrowed it between
this PR's two rounds and **confirms rather than undoes** the finding):

> `そして、` **alone on its display row** — opening a new sentence, or standing as its own
> coordinating row — takes **`Ａｎｄ，`**. A `そして` **continuing into its own clause** takes
> lowercase **`ａｎｄ`** with no comma. **`Ａｎｄ　ｔｈｅｎ` is reserved for `それから`.**

✅ **The `Ａｎｄ　ｔｈｅｎ` collision is DISCHARGED, not merely recorded.** Before the fix, `Ａｎｄ　ｔｈｅｎ`
rendered `それから、` in `pending/chunk_017` **and** `そして、` in chunk 25 — and **chunk 5 holds both
source words**, so §25.3's co-occurrence test *failed*. After the fix `Ａｎｄ　ｔｈｅｎ` occurs
**exactly once in the whole corpus** and the test is met. Reach: `そして` **10 battle** (chunks 5,
16, 24, 25, 26, 39, 43) **+ 9 script** (banks 1, 9, 32, 41); `それから` 6 battle (5, 13, 17, 23, 38)
+ 2 script (banks 2, 43).

### AC3. ⚠️ WIDTH FIGURES — the method rule, replacing another wave of individual corrections

**Fourteen of PR #23's 37 width figures were wrong; thirteen were exactly one too high.** The
translator re-measured all 37 itself at round 2 and formally withdrew its own Flag 15. Two rows of
`glossary.md` were also wrong about one phrase in **opposite** directions and are patched in place:
**§9 had `Ｐｒｉｎｃｅ　Ｈｏａｇ` at 10 (one LOW) and §39.1 at 13 (two HIGH); it is 11.**

**The pattern is the finding.** Across two review rounds and two agents, **every figure either party
argued from was exact** — `Ｐｒｉｎｃｅｓ　Ｈｏａｇ　ａｎｄ　Ｔｏｒｉｆ，` 23, the rejected 26-column
alternative, `Ｒｉｇｈｔ，　ｇｅｔ　ｔｈｅ　ｓｈｉｐ　ｏｕｔ！` 24, `Ｓｕｒｅｌｙ　ｎｏｔ．．．．！？` 16 — **and every
wrong figure was a table cell typed rather than measured.** Three waves running have now spent
reviewer time on this.

> **Rule: every column figure that reaches a PR body, a glossary row or a FLAGS entry is produced by
> `len()`, including the ones that look obvious.** A figure nobody argues about is exactly the one
> nobody checks, and it is the one a later unit will budget a row from. Nothing rendered has ever
> been affected by these errors; the risk is entirely downstream.

### AC4. Portrait id is not speaker — the channel test, and two readings it produced here

Both of chunk 25's long messages put **two speakers under one `{FCB0}` portrait id**, separated only
by the `{FC50}`/`{FC51}` channel byte. §40.5 used the same test on chunk 26's Treize in the same
wave. Two readings this produced that no portrait-level reading would:

- **Portrait 0002 channel 0 is Hoag, not Torif** — Hoag borrows his brother's portrait for
  `何を言ってるんだ、トリフ。`
- **Portrait 0008 channel 0 in the final message is Guilford, not Helfer** — Helfer (ch1) apologises
  to Guilford by name and ch0 answers `なに、かまわん。…私が一人で解いてみせる。`

It also confirmed §9's corrected attribution from inside the chunk: the light-elf descendant and
Aura Smasher are **Aries's** (channel 1), not Torif's. Recorded at glossary §41.2.

### AC5. §33.2's `どうやら` row was over-broad, and a reach count that looks only forward is why

§33.2 fixed `どうやら、` → `Ｌｏｏｋｓ　ｌｉｋｅ　…` and named the four *untranslated* chunks it would
bind — but `chunk_002` (wave 1) and `chunk_014` had already shipped **three** `seem` renderings, and
the row counted none of them. Corrected in place at glossary §41.4: the corpus splits on **register,
8 of 8** (contraction-free formal → `seem`; contracting casual → `Ｌｏｏｋｓ　ｌｉｋｅ`), the §36.2
`とにかく` shape. **No line changes anywhere**; all eight instances were already on the right side.

⚠️ **The general defect: a reach count that enumerates the chunks a term will reach, and not the
files that already render it, is only half a count.** This is §37.3's and §38.6's failure in a new
place, and it is the second half of §Y3 — a claim can be stale because the tree moved *forward*
since it was written, or because it never looked *backward* in the first place.

### AC6. Standing gate-6 trap list — two additions from this review

The list every battle reviewer needs, with the two new entries first:

1. ⚠️ **NEW — an ellipsis checker that counts `・` runs but ignores a closing `。` reports a FALSE
   MISMATCH.** §3.1 counts `・・・。` as **four**. Chunk 25's line 12 has fourteen groups and two of
   them are `・・・。`; a `・`-only checker reports 3-against-4 twice and looks like a real defect.
2. ⚠️ **NEW — a segment-level positional checker SILENTLY DROPS every line whose `{FFFE}` count
   changed.** Chunk 25's 129-row main line indexed **20** segments instead of 123 until the pairing
   was keyed on the surviving tag stream instead of on segment index. The output looks clean; it is
   empty. This is §W3/§Y7's skew in its most dangerous form, because it fails *quietly*.
3. `split_battle` returns a **trailing blank separator line** — strip it from both sides or every
   file mismatches and the checker reports zero pairs, which reads as "no duplicates" (§AA2).
4. `pending/chunk_043.txt` and `pending/chunk_043_abridged.txt` are **two translations of one
   chunk** — exclude `_abridged` or get 31 spurious divergences (§AA2).
5. `tl/battle/chunk_001.txt` has **no trailing newline** (§W4); handle it by stripping trailing
   blanks from both sides rather than popping, or the file drops out of the index entirely.
6. Battle `tl/` files carry a **2-line header offset** from the dump body index.
7. ⚠️ **A checker must exclude the unit under review from its own index**, or every run self-matches.
   Report the count of runs *looked up* separately from the count of matches *found*.
8. **Case matters in a `tl/` grep.** `ｐｕｒｓｕｅｒｓ` looked free across the whole tree until
   `chunk_021` L3's sentence-initial `Ｐｕｒｓｕｅｒｓ？` was found — §36.1's row was right and the
   grep was wrong.

### AC7. Bank pressure — unchanged by this unit

Nothing under `tl/script/` changed, so `bankmeasure` and `rowcheck script` are not engaged and no
bank moved. The tightest banks are as §Z6 / §AB left them: **41 → 353, 40 → 447, 5 → 3,357,
2 → 3,365**, 33 → 9,291. **No bank is under 2,000 free that was not already.**

### AC8. Open, carried forward, not resolved here

1. **§AA3 stays OPEN** — chunk 24's `．．ｌ．．．　ｍｙ　ｌｏｒｄ．．．` commits to a male patron and
   nothing settles the referent. Chunk 25 makes Helfer the conspirator and puts Guilford beside him,
   which is consistent with `Ｌｏｒｄ　Ｈｅｌｆｅｒ` but proves nothing. 4 columns either way, no
   re-flow. Re-check when a chunk names Fernando's backer.
2. **Portraits 01 and 09 of chunk 25 are unnamed on purpose.** 01 knows Rimul by sight, uses blunt
   `お前` to her and polite `ですか` to a 司令官 who is present; Fernando fits and nothing names him.
   The English supplies no name, so nothing needs revisiting if a later chunk settles it.
3. **`王子様` referential is NOT ruled** — only the vocative is (glossary §41.6). The **8 script
   instances** read referential and `batch_008` (PR #21) or a later script unit decides them, on
   §1's `王女様` → *the Princess* precedent.
4. **`pending/chunk_005.txt`'s two `王家` rows are queued for re-cut** in `pending/README.md`
   (`ｔｈｅ　ｃｒｏｗｎ’ｓ` → `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ`, +8 columns), on the §23.2 precedent. Chunk 5 is
   parked for the tier-A budget, so nothing ships until the slot patch lands either way.
5. **Torif's register is fixed for the first time** at glossary §41.3 — formal, `僕`, no
   contractions, `兄さん` → `Ｂｒｏｔｈｅｒ` capitalised as a vocative. **Chunks 26 and 42 carry him.**
6. **`踊り子` → `ｄａｎｃｅｒ` binds 18 script instances** (banks 1, 18, 20, 23, 41) — the largest
   forward obligation this unit creates. `ｆｉｅｌｄ　ｍｉｃｅ` binds chunks 41 and 42 and bank 41;
   `小娘` reaches chunk 31; `封印` reaches chunk 32 and bank 41; `駒` reaches bank 41; `追手` reaches
   chunk 29; `あの世` reaches chunk 41.

---

## AD. Wave 6 review — script batch 008 / PR #21 (2026-09-09)

**DECISION: MERGE at round 1**, squashed as `e8ad8c6`. All nine gates re-run in a real checkout on
the merged tree; **nothing in the file needed to change**, and **five subsidiary figures in the PR
body are wrong and were corrected at merge**, none of them touching a line. The last unit of wave 6.

### AD1. The figures, as the reviewer measured them

`check` → "All checks passed", 4,209 script lines / 358 unique forms. `merge` prints **no** "never
matched the dump". `rowcheck.py script` reports only the four **inherited** pool/shop lines — and
none is this unit's, proven mechanically rather than by eye: its 47 messages occupy **merged-dump
lines 830–1233**, so the flagged line 1234 sits immediately after the last of them.

| | Measured | PR |
|---|---|---|
| bank 4 free | 11,781 → **10,179** (+1,602 used) | exact |
| bank 5 free | 3,357 → **2,007** (+1,350 used) | exact |
| banks 3 / 40 | **byte-for-byte untouched** (8,113 / 447) | exact |
| unique lines / instances | 47 / 47, banks 4 (32) and 5 (15) only, no key elsewhere | exact |
| distinct translations | **32** (47 − 22 + 7) | exact |
| EN visible characters | **3,052** | ❌ 2,932 |
| growth | **1.9353×** | ❌ 1.86× |
| text rows / widest | **190 rows, widest 23, 20 rows at 23, none at 24** | exact |
| `{FFFE}` | **+1, DATA 470 only** | exact |
| `{FCC0}` | **19 → 19, none added** | exact |
| charset | 0 characters outside §3.1 | exact |

Bank movement was measured by **moving the file aside, re-running `merge` and `bankmeasure`, then
restoring it** — not by trusting the PR. ⚠️ The EN-character figure is checkable against those bank
deltas and closes exactly: `(3052 − 1577) × 2 + 2` (the added `{FFFE}`) `= 2,952 = 1,602 + 1,350`.

⚠️ **Banks under 2,000 free, named as CLAUDE.md §6.5 requires: 41 (353) and 40 (447)**, both
pre-existing and untouched here. ⚠️ **Bank 5 now stands at 2,007 — seven bytes above the
threshold, and the third-tightest bank in the project.** The next script unit that touches bank 5
has effectively no room; treat it as full when planning.

### AD2. ⚠️ `ｍｏｎｓｔｅｒｓ` renders 魔物 AND モンスター in one bank, one speaker, two messages apart

**The PR did not raise it; the rendering stands and nothing is re-cut.** Full reasoning and the
reserve are at glossary **§42.3**. Short form: `魔物` is banks [5, 40]; `モンスター` is 24 banks
including 4 and 5, 214 script instances, byte-bound by `batch_001` L33. This unit renders both in
**bank 5, from King Leverk, two gossip lines apart**, so §25.3's test fails *visibly* — the sharpest
instance the project has had. §9's wave-6 seed nevertheless fixed `魔物` → `ｍｏｎｓｔｅｒ` knowing
`モンスター` was already shipped, and one native word plus one loanword for one concept is exactly
§17.2's 鬼 / オーガ collapse. **If a later unit needs the split, `モンスター` cannot move and `魔物`
must; the reserve is `ｃｒｅａｔｕｒｅ` (9 columns), verified free.** Only banks 5 and 40 are affected.

### AD3. ⚠️ LIVE — `Ｉ　ｓｅｅ．` and `なるほど` share bank 5, and §30.3's discharge never tested banks

`Ｉ　ｓｅｅ．` now renders **five** source strings. The **new** one, `そう。` (DATA 481, bank 4),
passes §25.3's stated bank test cleanly — none of `そうか。` [5, 8, 9, 29, 33, 41], `そうですか`
[0, 7, 12, 16, 41], `そうかい` [2, 12, 17, 20, 23, 24] or `なるほど` [1, 5, 8, 33, 36, 40] is in
bank 4. **But this unit puts `そうか。` → `Ｉ　ｓｅｅ．` into bank 5 (DATA 507, 510), and bank 5 also
holds an untranslated `なるほど`** inside two of the big pooled strings.

**The pairing is pre-existing, not created here** — §30.3 fixed `なるほど` and `chunk_004` L11
shipped `そうか` → `Ｉ　ｓｅｅ．` long before — and **§30.3's discharge counted chunks only, never
banks**, which is the gap this merge exposes. Nothing shipped is affected and no line changes. Left
LIVE for whoever translates that pool, on the §T2 / §32.5 pattern. §25.3's `Ｅｘａｃｔｌｙ．` stays
reserved for `そのとおり` / `そうそう`. See glossary §42.4.

### AD4. FORWARD BINDING — four messages have sibling unique rows outside the unit

Measured over all 1,430 unique lines by **visible text** rather than key. Different `{FFF6}` /
`{FFF8}` arguments make them different keys, so §3 does not force reuse — but the player meets one
line, which is §34.9's reasoning for unique 598.

| Shipped here | Japanese | Untranslated siblings (DATA) |
|---|---|---|
| 472 / 483 / 493 / 504 | the recruiter menu | **329, 330, 394, 400, 412** |
| 481 | `そう。疲れたときはいつでもよってね。` | **326** (count 2) |
| 505 | `どれが　よろしいかな？` | **535** |
| 506 | `軍隊にとって兵士は　立派な財産。大切にされよ。` | **403** |

**Copy the English byte-for-byte; do not re-invent it.** ⚠️ DATA 326 is one of the three lines the
wave-6 preflight already had to correct the wave-5 handoff about (`HANDOFF.md`: 326/327/328 are
count-2 shop lines in banks 4 and 5, not count-3 bank-40 gossip). The two records now agree.

### AD5. ⚠️ §Z2 counts FILE lines where the wave-6 documents count DATA lines — a third convention clash

`FLAGS.md` §Z2's menu line numbers are `script_unique.txt` **FILE** lines; `batch_008.tsv`'s header,
glossary §9's corrected wave-6 citations and §34's convention are **DATA** lines, and the two differ
by exactly **5**. §Z2's 440/450/461 are DATA 435/445/456, and four of its "nine untranslated" —
477, 488, 498, 509 — are this unit's own 472, 483, 493, 504. **§Z2 is updated in place at this
merge.** `HANDOFF.md` item 10 already warned that `batch_007` and `batch_008` number differently;
this is the same clash reaching FLAGS, and it is the **seventh** numbering convention now in play in
this repo (§O8, §P; glossary §28, §29, §30, §31, §32, §33, §34). **Neither convention is wrong —
what is wrong is citing one without saying which. State the convention beside any line number.**

### AD6. Five PR figures corrected, and one of them changes an inherited decision

**Every headline figure was exact**, and all three of Flag 5's line-citation corrections were
re-derived independently and confirmed (`古代文明` DATA 488, `魔族`/`末えい`/`司教様` DATA 498,
`ウェストバリー` DATA 515), as was Flag 3's "32, not ~26".

| # | Claim | Measured with `len()` |
|---|---|---|
| 1 | 2,932 EN chars / 1.86× | **3,052 / 1.9353×** |
| 2 | `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` 25, `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ` 20 | **23 and 17** |
| 3 | `Ｗｅｓｔｗａｒｄ，　ａ　ｄｅｓｅｒｔ　ｏｆ` 22 | **21** |
| 4 | `Ｉ’ｍ　ａｆｒａｉｄ，` 10 | **11** (its −6-byte figure is right) |
| 5 | `ｔｈｏｓｅ　ｇｉｆｔｅｄ　ｉｎ　ｗｉｓｄｏｍ` 20 | **22** |

⚠️ **#2 is the one that matters beyond the record.** The PR's `砲台` row tells chunk 15's translator
that the full `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` does not fit. **At 23 it does** — inside the
box, at the ≤23 preferred limit. Corrected in glossary §42.1 so that chunk is not steered away from
it. A wrong width in a *forward* note is worse than a wrong width in a summary, because the next
unit budgets from it.

⚠️ **§AC3's pattern holds a second wave running: every figure either party argued from was exact,
and every wrong one was a table cell typed rather than measured.** The PR caught one of its own
before pushing (Flag 17's `ｄｅｓｅｒｔ` at 24). ❌ **`ｄｅｓｃｅｎｄａｎｔ` is 10 and was not reopened** —
five parties have now measured it.

### AD7. ⚠️ Three dispatch claims that did not survive measurement

Recorded because two of them would have cost a round if acted on.

1. ❌ **`大陸` does NOT owe byte-identity with chunk 25.** The dispatch said "batch 008 must match
   `ｔｈｅ　ｃｏｎｔｉｎｅｎｔ` byte-for-byte". Chunk 25's source is **bare** `大陸`; both of this unit's
   are **`この大陸`** and take `ｔｈｉｓ　ｃｏｎｔｉｎｅｎｔ`. **The fixed word matches; the determiner is
   the source's**, and §3 engages on the message. Forcing `ｔｈｅ` would have put a definite article
   on a demonstrative. Glossary §42.1.
2. ❌ **`王子様` referential is NOT this unit's to rule.** Measured: `王子様` is banks [1, 20, 40, 41]
   + battle chunk 25; `王子` banks [1, 3, 8, 10, 20, 23, 40, 41]. **This unit is banks 4 and 5 and
   contains no `王子` in any form.** §41.6's own standard — "a reviewer does not rule on lines that
   are not in front of him" — applies; the question stays open for a batch in banks 1/20/40/41.
3. ❌ **§AB5's `Ｃａｐｔａｉｎ` question is not engaged either**: `船長` is banks [23, 28, 41], `隊長`
   banks [2, 10, 28, 32, 34, 41]; this unit touches neither term nor either bank.

✅ **Two dispatch claims that were right and were acted on**: the two §9 cross-unit rows (`魔族` from
chunk 26, `末えい` from chunk 25) really were live and are struck here, **after reading the merged
tree** for each; and `場所` really has no §9 row (confirmed a third time).

### AD8. The blind-insert bound grows to 24 rows — §C4 / §Y1 unchanged

Six more rows join it: DATA 474/485/495 each carry `{FFEC}{=00}{=04}` (unit name) and
`{FFEC}{=00}{=01}` (price), neither of which `assemble.py:validate_body` or `rowcheck.py` substitute
— only `{FFEC}{=00}{=00}` (7 columns) and `{FC00}{=0000}` are counted, and **this unit contains
neither**, so the player-name question does not arise here. Measured: each of the six is
**insert + 8** (`，　ｉｓ　ｉｔ？` ×3, `　Ｊｅｗｅｌｓ，` ×3) against the Japanese's insert+2 and
insert+5, so at the §8 unit-name cap the row lands at 16 and overflows only if an insert renders
wider than 16. **`batch_006`'s 12 + `batch_007`'s 6 + these 6 = 24 rows now ride on one shop visit.**
The PR states the mechanism correctly and does **not** claim the blindness is uniform.

### AD9. `キエーザ城` — the promotion answers the reading only in the negative

`キエーザ` → `Ｋｉｅｓａ` is promoted and §9's row struck, but ⚠️ **the `Ｃｈｉｅｓａ` (Italian *church*)
reading is not ruled out — it is merely unsupported by this unit**, which names a swamp and a
direction and gives no religious evidence either way. The question actually lives in **`キエーザ城`
(script 1090 / 1092), still unrendered**. Whoever takes it should look at whether the castle is a
religious site before treating `Ｋｉｅｓａ` as settled for the compound; changing it afterwards is a
§4.3 correction reaching this unit's two rows. Glossary §42.1.

---

## AE. Wave 7 review — battle chunk 30 / PR #27 (2026-09-09)

**MERGED.** `tl/battle/chunk_030.txt`, **7,615 / 8,192 — 577 bytes slack**. Squash `9548e73`.
183 text rows, widest 23, none at 24, none over. Every gate in CLAUDE.md §6 run in a real
checkout; every width re-measured with `len()`.

### AE1. Byte and geometry figures — all confirmed, none corrected

`assemble.py check` → `chunk 30   7615 / 8192 bytes   slack   577`, "All checks passed".
`rowcheck` reports the two over-4 pages at file lines 21 (5 rows) and 23 (8 rows) and **both are
inherited**: a pristine extraction of chunk 30, run through the same tool at review, gives the
same two lines at the same counts (5 in / 5 out, 8 in / 8 out) and `{FFFE} unchanged on every
line`. Nothing introduced. Width histogram reproduced independently and matches the PR exactly:
`{5:4, 6:5, 7:4, 8:5, 9:3, 10:2, 11:11, 12:5, 13:11, 14:3, 15:11, 16:14, 17:6, 18:12, 19:18,
20:24, 21:16, 22:21, 23:8}`.

Tag accounting over the whole chunk: `{FCC0}` 12 → 12 (**no page break added**), `{FFFF}` 26 → 26,
`{FC30}` 53 → 53, `{FC50}` 44 → 44, `{FC51}` 17 → 17, `{FC00}` 4 → 4; **0 lines** with a changed
non-`{FFFE}` tag stream. `{FFFE}` 162 → 166, net **+4**, which is exactly the sum of the seven
per-line deltas the PR itemises. Dots: source `。`+`・` = **132**, translation `．` = **132**, and
the per-line ellipsis-run multisets match on every line (17 runs each side). Zero ASCII, zero
illegal characters, no gutter space lost.

### AE2. ⚠️ `batch_008.tsv` L55 renders 争い as `ｗａｒ`, against §38's fixed entry — A HUMAN / CORRECTIONS UNIT OWES THIS

Found while ruling on PR #27's `争い` question, and **not chargeable to PR #27**, which is correct.

- **`争い` → `ｓｔｒｉｆｅ` is a fixed glossary entry at §38**, which holds it distinct from
  戦乱 → *war* and 戦闘 → *battle* in as many words. It ships at `batch_007.tsv` L67 and
  `chunk_024` L14, and now `chunk_030` L24.
- `tl/script/batch_008.tsv` **L55** renders `知に長けた者と力に長けた者の　争いは` as
  `Ｔｈｅ　ｗａｒ　ｏｆ　ｔｈｅ　ｗｉｓｅ　ａｎｄ` / `ｔｈｅ　ｓｔｒｏｎｇ`. §42 (batch 008's own glossary
  section) registers **no** row for it, so this went in unnoticed.
- ⚠️ **It is live, not harmless.** Counted at this review: **`争い` and `戦乱` co-occur in bank 3**
  — precisely the collision §38 held them apart to avoid. §25.3's disjointness test **FAILS** for
  this pair, so a player can see both in one scene with one English word doing both jobs.
- **Fix:** re-cut `batch_008.tsv` L55 to `ｓｔｒｉｆｅ`. It is a script batch, so there is no byte
  pressure. Not done here — a reviewer does not edit a unit outside the PR in front of him.

### AE3. ⚠️ §9's `クロイツェル` row was going to be struck on a wrong count — CORRECTED, row kept live

PR #27's glossary row said "Hapax — 1 battle (this chunk) + 0 script, so the row is struck
outright". **The reviewer's own dispatch briefing repeated the claim.** Counted at review over
**both** dumps: **1 battle (chunk 30) + 1 script — bank 41, `script_unique` line 1391**, and the
script instance is the same construction (`紅の騎士団の将、リムル・クロイツェルだな？`). The §9 row
**stays live**; it is struck by whichever script unit takes bank 41. Glossary §43.5.

**No rendering is wrong** — `Ｋｒｅｕｔｚｅｌ` (8) and `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ` (14) are correct as
shipped and both widths were re-measured. Only the exhaustion claim was wrong. **This is §41.4's
item 1 in a new place: a reach count that looked at the battle dump and not at the script one.**
The wave's other two seeds were counted over both dumps and are exact.

### AE4. ⚠️ PR #27's `どうかご無事で` row said "recurs in chunk 23" and it does not — CORRECTED

`どうかご無事で` is **battle chunk 30 only, 4 instances, 0 script**. Chunks 5 and 23 carry
`ご無事でしたか` — the **past-tense enquiry** the same row explicitly holds distinct
(`フェルナンド将軍、ご無事でしたか。`, chunk 23). The row contradicted itself and, left as written,
would have pushed chunk 23's translator onto `ｐｌｅａｓｅ　ｂｅ　ｓａｆｅ．` for a construction that is
not the same one. Rewritten at integration; glossary §43.2.

### AE5. `石版` unique-line ids were wrong in two places — corrected, reach confirmed exact

The §9 seed row and PR #27's Handoff both said the script instances are "569 / 571"; PR #27's own
glossary row said "574 / 576". Measured: they are `script_unique` **305, 574 and 576** — 574/576
right, 569/571 wrong, and **305** (`軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`) named by
neither. The **reach itself is exact as the PR states**: 5 battle (chunks 30, 36) + **25 script
instances across 21 banks** (2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 25, 33, 40,
42, 43). Row stays live per §29.1 / §30.1.

### AE6. §L2 is confirmed from inside chunk 30 and still needs its in-game visit

`chunk_030.txt` **file line 23** (dump body 22) carries **no `{FC50}`/`{FC51}` anywhere** and eight
text rows; **file line 21** (body 20) has a page of five with no channel tag after its `{FC30}`,
which puts `リムル・・・。` — plainly the player's line — on Rimul's own channel beside her reply.
Both are inherited exactly and neither was re-flowed to flatter the count. **Nothing here is
translatable-away.** §L2's prediction of independently-selected string pools is consistent with
what the tag stream shows, and chunk 30 is one of the eight lines that question is about. **Still
a human job.**

### AE7. Method notes worth keeping

1. **Gate 6 needs a positive control AND a planted violation, every time.** This reviewer's first
   duplicate checker keyed on tag-bearing messages; portrait and `{FCB0}` tags differ per
   occurrence, so **nothing ever matched and it reported a clean pass**. It was caught only
   because a positive control asserted `recurrences seen > 0`. The working version keys on
   **readable text**, checks at `{FC30}`-utterance and row level, and was proved live by planting
   two corruptions and confirming detection. Corpus size is the cheap sanity check: **911 distinct
   JP utterances / 977 instances, 1,658 distinct rows** across 30 aligned files.
2. **A row-level checker silently drops every line whose `{FFFE}` count changed** — chunk 30
   changed seven. The hole was closed by looking every JP row of those seven lines up in a corpus
   built from the other 29 files. **Exposure was exactly two rows, both already declared in the
   PR** (`ああ。` and `お前は・・・`). Do this explicitly, and say so; a checker that skips a line
   and prints nothing is indistinguishable from one that passes it.
3. **§AC3 holds a third wave running, and it now cuts both ways.** Every width figure in PR #27
   was exact — the translator measured with `len()` and caught one of its own hand-counts
   (`Ｉ　ｗａｎｔ　ｔｏ　ａｓｋ　ｙｏｕ．` = 24, not 23) before pushing. **The two errors this review
   found were both *reach counts*, not widths**, and both came from counting one dump instead of
   two. The discipline has migrated: widths are now measured, reaches still are not always.
4. **A PR can under-count in its own favour.** PR #27 said six shipped `Ｙｅａｈ` instances and
   listed eight; there are **13**, and all 13 are casual speakers, so the argument it was making
   was stronger than it claimed. Verify the evidence even when the conclusion is right.

---

## AF. Wave 7 review — battle chunk 36 / PR #25, PARKED (2026-09-09)

### AF1. ⚠️ NEW BLOCKER — `assemble.py:validate_body` charset-checks PRESERVED SOURCE TEXT

**THIS IS NOT §D1 AND MUST NOT BE FILED UNDER IT.** The two are different functions, different
causes, different fixes and wildly different costs; conflating them buries a cheap fix inside an
expensive one.

| | **§D1 / §R** (chunks 5, 15, 16, 17, 23, 27, 28, 29, 32, 39) | **§AF1** (chunk 36) |
|---|---|---|
| Where | `riotbattle.tokenise` | `assemble.validate_body` |
| What | argument bytes mis-decoded as Shift-JIS (`{FC70}{=00}逓{=20000E}`, `{FC70}{=00}入{=A300020000}`) | the charset whitelist applied to text the translator never wrote |
| The characters | **should never have existed** — a dumper artifact | **genuine authored source bytes that render correctly today** from the ROM font; the player already sees them in the Japanese game |
| Fix | a `tokenise` fix **plus a re-dump** | **one function in `assemble.py`; no re-dump, no disc, no EXE, no dumper change** |
| After the fix | re-dump, re-verify 10 chunks | `git mv pending/chunk_036.txt tl/battle/chunk_036.txt` and nothing else |

**Measured at the PR #25 review, in a real checkout, not taken from the PR:**

| file placed in `tl/battle/` | `check` problems | breakdown |
|---|---|---|
| the **pristine** chunk 36 straight from the dump | **193** | all charset |
| the **delivered translation** | **38** | **all charset — 0 tag-parity, 0 column, 0 byte** |
| the delivered translation with `jp_ok=True` | **0** | — |

**The 38, counted:** `＄`(U+FF04)×14 · `＞`(U+FF1E)×10 · `＿`(U+FF3F)×4 · `＃`(U+FF03)×4 ·
`｜`(U+FF5C)×3 · `ケ`(U+30B1)×1 · `あ`(U+3042)×1 · `「`(U+300C)×1. They sit on body lines 2 (15)
and 5 (23) and **not one of them is on a translated run.** Chunk 36 is largely a full-width MIPS
assembly listing (`ｌｈｕ　ｔ５，＄１８`, `ｊａｌ　ａｉｍ＿ｅｎｅ`, `ｊｒ　ｒａ`), machine output
(`＞ＴＡＲＧＥＴ　ＲＥＣＯＧＮＩＺＥＤ`, `＞ＯＫ`) and a deliberate garbage block.

`assemble.py:192` calls `validate_body(new, 'chunk %d' % idx)` with the default `jp_ok=False` for
every battle chunk; line 280 passes `jp_ok=True` for the main script. **The translation removes
155 of the 193 problems and cannot remove the last 38, because they are not its text. No chunk 36
file of any kind — translated, partially translated or pristine — can pass `check` today.**

**Why the specification did not see this coming.** `translation_prompt.md` §3.1 bans `#`, `$`,
`>`, `|`, `_` as a rule for **what a translator writes**, and Appendix A describes the charset gate
as checking translation. Neither document contemplates a chunk whose *source* is full-width Latin
machine text. The gate is doing exactly what it was specified to do, to text the specification
never had in view.

**Fixes, cheapest first. All are `assemble.py` edits, which CLAUDE.md §3 puts outside a
translator's and a reviewer's remit — this needs a human.**

- **(a) RECOMMENDED — fixes the class, not the case.** Charset-check only the text the translator
  actually changed: diff each translated line's readable runs against the corresponding dump line
  and skip runs that are byte-identical. Preserved source is then never charset-checked, in any
  chunk, and no rule is loosened for real translation. The same diff already exists in the review
  tooling and is cheap.
- **(b) ⚠️ INSUFFICIENT ALONE.** Adding `＄ ＞ ＿ ＃ ｜ 「` (U+FF04, FF1E, FF3F, FF03, FF5C, U+300C)
  to `assemble.ALLOWED` and `rowcheck.ALLOWED` **does not close it** — `ケ` and `あ` are kana inside
  the garbage block, and blanket-allowing kana would disable the very gate that catches
  untranslated Japanese. (b) needs (a), or a per-chunk verbatim allowance beside it.
- **Rejected: legal look-alikes** (`％１８`, `＝ＴＡＲＧＥＴ`, `ａｉｍ‐ｅｎｅ`). They would corrupt a
  MIPS listing the player reads, rewrite source text the unit was told not to touch, and still
  cannot fix `ケ` / `あ`. The `{=8190}` byte-tag route was tested by the translator and fails
  `tag_parity` instead — **the two gates are unsatisfiable together**, the §R1 shape exactly.

**986 Japanese characters — 2.3 % of the battle script — are finished and waiting on this.**

### AF2. Figures — all confirmed, none corrected

`pending/chunk_036.txt`: **2,887 / 8,192 bytes, slack 5,305** (pristine 2,427, +460); widest run
**22**, none at 23 or 24, **0 column problems**; `{FFFE}` **104 → 107**, all three on body line 5
and each itemised in the PR; `{FCC0}` **2 → 2**, none added or moved; `assemble.tag_parity` returns
**no problems**, the only multiset delta anywhere being `{FFFE}: 59 → 62`. Both `>4`-row pages
(45 and 33) are **byte-identical to a pristine `split_battle` extraction** — already enumerated in
§D2, which lists chunk 36 by name.

**The preservation claim was verified, not accepted.** 9 of 10 body lines byte-identical (including
body line 2, the 884-character MIPS listing, in full); body line 5 the only line touched; **23
replaced runs, and the source side of every one contains Japanese** — changed runs with no Japanese
on the source side: **0**; 1,154 characters carried through unchanged on that line; residual
Japanese anywhere in the file: `ケ` and `あ` only.

### AF3. ⚠️ §AE5's `石版` "correction" was a FILE-vs-DATA convention difference — WITHDRAWN

§AE5 recorded that the `石版` script instances are "305, 574 and 576 — 574/576 right, 569/571
wrong". Measured on `dumps/script_unique.txt` at this review: **the first data row is FILE 6, so
FILE = DATA + 5**, and `石版` occurs at **DATA 300 / 569 / 571 = FILE 305 / 574 / 576**.

**569/571 and 574/576 are the same two lines in two conventions. Neither was wrong.** §AE5's real
finding survives and is valuable — **DATA 300 / FILE 305**
(`軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`) is a third instance no row had named. Only
the "wrong" verdict is withdrawn. The reach is unchanged and exact: **5 battle (chunks 30, 36) +
25 script instances across 21 banks**. Glossary §9's two rows now carry explicit convention labels;
see glossary §44.5.

⚠️ **§AD5 flagged this exact convention clash one wave earlier and it recurred immediately, in the
next review.** The rule this file has now earned: **state the convention on every line-number
claim, and never call a numbering difference an error without checking the offset.**

### AF4. ⚠️ `riotbattle.bytes_from_body` cannot cross-check a battle body, and PR #25's Flag 1 overstated

Its signature is `bytes_from_body(body, idx)` and it **raises**
`ValueError: bad tag {PAD 5765} in chunk 36` on this chunk's body — for the pristine chunk and the
translation alike. It cannot be run over a battle body that still contains its `{PAD}` line; the
structural lines must be stripped first, which is what `assemble.py` itself does
(`cost(''.join(l for l in new if not is_structural(l)))`).

**The byte figure is right** — 2,887 / 8,192 is `assemble.py check`'s own arithmetic, which is the
gate. Only the claim that the two implementations "agree to the byte" as run is unsupported as
written. **Nothing in any file changes.** Recorded so the next unit does not repeat the
cross-check and conclude the tool is broken.

### AF5. Method notes worth keeping

1. **A green `check` on a parked unit proves nothing.** `grep -n "pending" tools/assemble.py`
   returns **nothing** — `assemble.py` never reads `pending/`. Any review of a park must say so
   explicitly and must re-run the gate with the file placed in `tl/battle/`, or the tick is
   mistaken for clearance. Done here; the same file that passes in `pending/` raises 38 problems
   in `tl/battle/`.
2. **Numbering conventions differ BETWEEN TOOLS, not only between documents.**
   `rowcheck.py:load_chunk` returns `lines[a:b]` **including** the `=== CHUNK` header, so
   **rowcheck line N = `assemble.validate_body` body line N−1**. rowcheck's "line 3"/"line 6" and
   the charset block's "line 2"/"line 5" name the same two lines. Both sets in PR #25 are correct;
   neither is wrong; a reviewer who does not know the offset will "find" a contradiction.
3. **§AE7's positive control was run again and earned its place.** A synthetic clean/corrupted pair
   was checked **first**: the checker extracted 2 pairs from each and distinguished them, excluding
   the matched-nothing-and-passed failure. Only then was the 3,685-pair, 30-file corpus trusted.
   ⚠️ **`pending/chunk_043_abridged.txt` was excluded** — it is a second translation of chunk 43 and
   would have doubled every chunk-43 row in the corpus.
4. **A reviewer's own finding can be wrong, and a census is how you find out.** Two rows in chunk 36
   end in a lone two-letter word, which §3.2 cautions against and which is avoidable at zero cost.
   The census killed it: **170 such rows exist across 24 of the 27 shipped battle chunks**,
   `chunk_030` included. Holding one PR to a standard no merged unit meets is not review, it is
   inconsistency. **Raised, measured, withdrawn — and recorded so the next reviewer does not
   re-raise it.**
5. **Portrait ids do not survive chunk boundaries, and chunk 36 is the sharpest proof yet.**
   Glossary §23.5 fixes Timmy on **portrait 0007**; in chunk 36 portrait 0007 is **the machine**.
   Carrying the id across would have handed the MIPS listing to Timmy. §41.2 / §AC4's channel test
   is what decides. See glossary §44.3.

### AF6. Bank pressure — unchanged by this unit

Battle unit, nothing under `tl/script/`. Tightest banks are unchanged: **41 → 353, 40 → 447,
5 → 2,007, 2 → 3,365.** No bank is under 2,000 free that was not already.

---

## AG. Wave 7 review — battle chunk 31 / PR #26, MERGED (2026-09-09)

Two review rounds. Round 1 → CHANGES on one finding; round 2 applied it verbatim → MERGE at
`6d2530c`. **5,399 / 8,192 bytes, 2,793 slack.** Longest column run 23, zero at 24, zero over 24,
133 text rows, no page over 4. Tag stream unchanged on every line; no `{FCC0}` added.

### AG1. ⚠️ NEW — a page's source-blank TRAILING segment MAY carry text, and §3.2's warning is narrower than it reads

**Ruled at this review and recorded at `glossary.md` §45.2.** Chunk 31 buys a text row on **seven**
pages by moving text into a trailing segment the Japanese left blank — no tag added, moved or
deleted, slot count per page unchanged, physical row budget identical. A census of page text/blank
shapes across all 44 pristine chunks, run at review, is what settles it:

```
TTTT   389      TT     262      .TTTT  182      TT.     98
TTT.   276      T      251      .TTT.  132      TTT    115      .TTTT.   0
```

**`.TTTT.` — leading blank AND trailing blank AND four text rows — has 0 occurrences, exactly as
§3.2 says.** But `.TTTT` has **182**, and `TTTT` is the commonest page shape in the game at 389.
So filling a trailing blank moves *away* from the never-attested shape rather than toward it, and
§3.2's warning does not reach it.

⚠️ **This distinction cost a review round, and it will cost another unless it is read carefully.**
The PR read §3.2 as barring a fourth text row under a leading blank, and on that basis compressed
`百戦錬磨の将とはいえ、` to `Ａ　ｖｅｔｅｒａｎ　ｇｅｎｅｒａｌ，　ｙｅｔ` as a §2.1 step-4 shorter
synonym — in a chunk with **2,837 bytes of slack**, where §2.1's ladder ("when a chunk is over
budget") does not apply at all. The finding was raised, the census supplied, and round 2 restored
the literal reading at +44 bytes. **No §2.1 compression remains in the file.**

### AG2. ⚠️ OPEN — in-game legibility of the `・` separator inside the two Latin incantations

**A human's question; nothing an agent can settle from the dumps.** `assemble.py`'s charset gate
rejects `・` (U+30FB) and §3.1 states there is no `・`, so the wave dispatch's instruction to
reproduce the incantations "exactly, character for character" **was not satisfiable**. The
translator refused it and said so, which was right. The mapping is forced and every letter and its
case is preserved byte for byte:

| source | shipped | rule |
|---|---|---|
| `ＨＥＫａＳ・ＨＥＫａＳ` | `ＨＥＫａＳ　ＨＥＫａＳ` | separator → `　` (§1, `ゼファー・クリッペン`) |
| `ＥＳＴｉＶｅｂＲＯｉ・・` | `ＥＳＴｉＶｅｂＲＯｉ．．` | trailing `・・` → `．．` (§3.1, count matched) |
| `ＥＬＡＧＬＡ・ＬｉＣＨ！` | `ＥＬＡＧＬＡ　ＬｉＣＨ！` | separator → `　` |

**Someone should look at these two lines on screen once**, since a magic formula's separator reads
differently in a 24-column box than in a text editor. Add to the in-game visit alongside §L2.
See `glossary.md` §45.7.

### AG3. ⚠️ OPEN — stutter capitalisation is UNFIXED and the corpus is split 9 : 5

Counted at this review across `tl/` and `pending/`. Neither form is fixed by any glossary row, and
both are shipped:

- **Capitalised** (9): `Ｗ，　Ｗａｉｔ` (c6), `Ｐ，　Ｐｒｉｎｃｅｓｓ` / `Ｗ，　Ｗｈｙ` (c7),
  `Ｗ，　Ｗｅｌｌ` (c8), `Ｌ，　Ｌａｄｙ` (c14), `Ｉ，　Ｉｔ` (c22), `Ｗ，　Ｗｅｌｌ` / `Ｎ，　Ｎｏｔ` /
  `Ｎ，　Ｎｏ` / `Ｗ，　Ｗｈａｔ` (c24), `Ｓ，　Ｓｅｔｉ` (c26), `Ｉ，　Ｍａｍｕ` (pending/c17).
- **Lowercase** (5): `Ｙ，　ｙｅｓ` (c7), `Ｗ，　ｗａｉｔ` (c11), `Ｉ，　ａｆｔｅｒ` (c25),
  `Ｗ，　ｗｈａｔ` (c26), `Ｃ，　ｃｈｉｅｆ` (`batch_007`).

Chunk 31's `お、おい、` → `Ｈ，　ｈｅｙ，` is on the lowercase side and is **not a defect** — §24.3
and §19.1 fix the *comma form*, not the case. But `chunk_026` ships both conventions in one file,
which is the sort of thing a player sees. **For a future corrections unit**, not for a translator
mid-wave: pick one, and note that the capitalised form is both the majority and the one English
sentence-initial capitalisation would give.

### AG4. Two §4.3 corrections applied in place, and a third to §41.4's census

All three are recorded at `glossary.md` §45.4; **none touches a line of any file.**

1. **`ｇｅｍｓｔｏｎｅ` is 8 columns, `ｇｅｍｓｔｏｎｅｓ` 9** — not 9 and 10. Two cells carried the same
   wrong number and both are patched: §32.1's row and §33.1's row. ⚠️ **The second is in §33.1's
   promotions table, not §33.5's prose** — §33.5 carries no column figure at all, and both the PR
   and the wave dispatch mis-attributed it while getting the line number right. Flagged by the
   translator; confirmed with `len()`.
2. **§32.7's `ふふ` census counts substrings.** Chunk 31 has **3** ふ-runs, whose non-overlapping
   `ふふ` substring count is 5 — the "31 ×5" the row records. The §35.2 shape again.
3. **§41.4's own census was short by one, and the battle side is now 13 of 13.** 19 `どうやら` in
   the battle dump: 13 rendered, 6 untranslated (chunks 15 ×3, 16, 23 ×2). §41.4 listed 8 and
   missed `chunk_008` line 14, so it was 9 of 9 when written. ⚠️ **"With no exceptions" is still
   wrong** — the count was battle-only, and `batch_005.tsv` puts a plainly casual speaker on the
   `ｉｔ　ｓｅｅｍｓ` side. Same forward-not-backward count §41.4 criticised in §33.2 one section
   earlier.

### AG5. ⚠️ LIVE — `何だって？` shares its English with `何だと？` in script banks 5 and 41

`何だって？` → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` is accepted as a third spelling on §6's row. The battle
side is clean (no chunk holds both), but on interjection forms alone — **not** the bare substrings,
which pick up `chunk_013`'s `何だと思っている` — **banks 5 and 41 hold both**, and `batch_002.tsv`
already ships `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` into those pools. **Pre-existing, not created here, no
line changes.** Recorded LIVE on the §42.4 pattern for whoever translates those pools. **Reserve,
verified free: `Ｗｈａｔ　ｄｉｄ　ｙｏｕ　ｓａｙ？` (17).** See `glossary.md` §45.6.

### AG6. §AC3 refinement — measure the option you argue AGAINST, not only the one you ship

**A new hiding place for this project's most persistent bug, diagnosed by the translator itself.**
Every row that entered `chunk_031.txt` was measured with `len()` and every one was right. The
rejected alternative quoted in the PR's Flag 4 **never entered the file**, so it was hand-counted —
23/23/22 against a true 22/22/22 (`hundred` and `battles` are 7 letters; it counted 8). That
unmeasured number was the load-bearing one: it was the whole case for compressing the line.

> **Rule: a width you cite in an argument is a width you must measure, even — especially — when it
> belongs to the option you are rejecting.** `len()` on strings that never reach the file is as
> mandatory as `len()` on the ones that do. Five coordinator claims and three glossary cells have
> been refuted by measurement this wave; this is the first case where the unmeasured string was in
> a *flag* rather than in a file, and no gate would ever have caught it.

### AG7. Bank pressure — unchanged by this unit

Battle unit, nothing under `tl/script/`. Re-measured after `merge`: **41 → 353, 40 → 447,
5 → 2,007, 2 → 3,365.** No bank is under 2,000 free that was not already, and none moved.

### AG8. `石版` and `『かげの石版』` §9 rows STAY LIVE after this merge

Chunk 31 contains **no** `石版` — verified at review — so this unit discharges nothing. **PR #28
(script `batch_009`) is the last unit that renders them** and is still unreviewed; the rows are
struck by that merge, per the `ルート` precedent (§29.1 / §30.1). `クロイツェル` also stays live
(1 battle + 1 script, bank 41, `script_unique` 1391), per §43.5.


## AH. Wave 7 review — script batch 009 / PR #28, MERGED (2026-09-09)

One review round → **MERGE** at `aca5b77`. `script_unique.txt` **DATA 534–583** (FILE 539–588;
FILE = DATA + 5, verified at review by reading `tools/queue.py:script_rows()`), 50 unique lines /
50 instances / 2,913 JP → 5,925 EN visible characters = **2.0340×**, **+6,026 bytes**.
`{FFFE}` 285→286, `{FCC0}` 46→46, non-`{FFFE}` tag stream byte-identical on all 50 lines,
340 text rows, 2 at 24, 26 at 23, none over 24, no page over 4 rows. **Every one of the PR's
figures re-measured at review and every one is exact** — including all twelve bank figures,
which were checked in **both** directions by moving the file aside and re-merging.

Banks after this merge: **7 → 13,095 · 8 → 10,727 · 9 → 12,205 · 10 → 33,921 · 11 → 39,345 ·
12 → 8,559.** No bank negative.

### AH1. ⚠️ Banks under 2,000 free after this merge — unchanged, and NOT touched by this unit

**bank 41 → 353 free · bank 40 → 447 free.** Bank 5 is next at **2,007**, bank 2 at **3,365**.
All four were verified byte-for-byte unchanged across the before/after measurement — `batch_009`
lands only in banks 7–12. **§F2's four tight banks remain the run's real ceiling** and nothing in
wave 7 moved them.

### AH2. ⚠️ §9's `石版` row is STILL LIVE after wave 7 — the wave-7 dispatch said to strike it and was WRONG

The dispatch instructed the reviewer to strike **both** tablet rows if this unit rendered them
consistently. It renders them consistently — but the strike is only half correct, and the
dispatch itself flagged the doubt, which turned out to be justified.

- **`『かげの石版』` IS struck.** Its whole reach is battle chunk 36 (rendered, parked) + script
  **DATA 569** (rendered here). Nothing outstanding.
- **`石版` is NOT struck.** Its reach is script **DATA 300, 569, 571**. This unit renders 569 and
  571. **DATA 300** — `軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`, **count 21 across 21
  banks**, an item description — is in **no** wave-7 unit and is translated in **no**
  `tl/script/*.tsv`. Verified by direct lookup at review, not inferred from the cell.

**Whoever takes DATA 300 strikes the row.** Until then `石版` → `ｔａｂｌｅｔ` (6 columns, bare
lowercase) is binding. Recorded at `glossary.md` §9 and §46.4.

### AH3. ⚠️ NEW — §9's `ビーストショップ` reach cell was INCOMPLETE; the row is held live for DATA 899

The §9 row records the reach as "script 555". **`ビーストショップ` also occurs at script
DATA 899 (bank 28), which is untranslated**:

```
DATA 899 (bank 28): ちょっと変わった仲間が{FFFE}ほしいなら、{FFFE}マーベラスの街へ{FFFE}行ってみなよ。
                    {FCC0}{FFFE}『ビーストショップ』で{FFFE}ドラゴンやゴーレムを{FFFE}売ってくれるぜ。
```

**Neither the wave-7 dispatch nor the PR body caught this.** It was found by recounting the term's
reach over the pristine dump rather than trusting the cell — the same failure mode §AE5/§AF3
already cost this wave once.

⚠️ **DATA 899 is PROSE, not a menu option.** It takes `“Ｂｅａｓｔ　Ｓｈｏｐ”` — §12 quotes for the
source's `『　』`, and **no leading `　` cursor gutter**. The gutter belongs only to DATA 555's two
menu options (`　Ｂｅａｓｔ　Ｓｈｏｐ` 11, `　Ｉｔｅｍ　Ｓｈｏｐ` 10). `アイテムショップ` alone is
exhausted at 555, but the two share one §9 row, so the row is held live for `ビーストショップ`.

### AH4. ⚠️ §25.3's collision test has FAILED for the first time, and the ruling is BANK-scoped — battle chunk 32 is the next place it bites

`glossary.md` §46.3 rules `なるほど` → `Ｉｎｄｅｅｄ．` where it shares a bank with `そうか` (which
keeps `Ｉ　ｓｅｅ．`). The census was recounted independently at review over both pristine dumps
and **reproduces the PR's cell for cell**; `そうか` × `なるほど` share script banks **[5, 8, 33]**,
and bank 8 is where this unit renders both (DATA 550/553/554 vs 556/557, all Prince Hoag).

**The gap: the ruling names *banks*, so it does not reach a battle *chunk*.**

- **Battle chunk 32 holds BOTH `そうか、` and `なるほど`, and is untranslated.**
- Battle `chunk_033` already ships `なるほど` → `Ｉ　ｓｅｅ．` (§30.3).

**Chunk 32's translator will meet this collision with no rule covering it.** The obvious extension
is the chunk-scoped analogue of §46.3 — `なるほど` takes `Ｉｎｄｅｅｄ．` in chunk 32 — but that
puts a second form on a chunk adjacent to `chunk_033`'s shipped `Ｉ　ｓｅｅ．`, so it wants a
decision rather than a default. **Script banks 5 and 33 also hold both members and are
untranslated**; there §46.3 applies directly and needs no new ruling.

⚠️ **Reserves, both re-verified FREE across `tl/` and `pending/` at review:** `Ｅｘａｃｔｌｙ．` (8)
stays reserved for `そのとおり` / `そうそう` per §25.3 and was **not** spent; `Ｑｕｉｔｅ　ｒｉｇｈｔ．`
(12) is the named next reserve for a third member of the family in one bank.

### AH5. ⚠️ NEEDS A HUMAN — is bank 8's town ruled by a King or by Prince Hoag?

`王` and `王子` name the **same portrait** (`0x14`) in bank 8 and the English commits to neither:

- **DATA 542** — a retainer: `王は ただいま外出しておられる` → `Ｔｈｅ　Ｋｉｎｇ　ｉｓ　ａｗａｙ`.
- **DATA 558** — the 9th Army captain calls that portrait `王子` → `ｍｙ　Ｐｒｉｎｃｅ`.
- **DATA 574** fixes the portrait as **Prince Hoag** (`ホアグ王子`, twice), and **576** says his
  father is dead (`父が亡くなって`).

So *King* may be correct in-fiction (Hoag crowned), or 542 may be a generic door line reused
across towns. **Each row renders exactly what its own line says**, which is §28.7's disposition of
chunk 13's unnamed King, so nothing is blocked — but **one in-game visit to that town settles it.**
§41.6's *referential* `王子様` is not reached by this unit and stays open where §41.6 left it.

### AH6. FORWARD BINDING — DATA 691 (bank 17, untranslated) is a twin of 582/583

DATA 691 carries the byte-identical visible text of this unit's **582/583**
(`いらっしゃい！！` / `どんな 用だい？`). A different `{FB00}` portrait and different `{FFF8}`
arguments make it a different key, so §3 does not *force* reuse — but the player meets one shop
greeting. **Whichever batch takes DATA 691 must reuse `Ｗｅｌｃｏｍｅ！！` /
`Ｗｈａｔ’ｓ　ｙｏｕｒ　ｂｕｓｉｎｅｓｓ？` byte-for-byte**, on §34.9's reasoning for unique 598.

### AH7. Gate-6 method note — §AE7's lesson applied, and a checker that was wrong about the FILE

Per §AE7, **no checker was believed at this review until a planted corruption made it fail.** Four
passes were run, each with a positive control that **DETECTED** its planted fault: exact key (0
collisions), visible-text siblings (4 pairs, all shipped, 0 divergences), in-batch whole messages
(2 pairs, 0 divergences), and **page-level sub-sequences across the whole shipped script corpus —
612 pages compared, 54 recurring-page pairs, 0 divergences**, which is the pass a whole-message
comparison cannot see. A script `.tsv` keeps the Japanese in column 2, so a column-2 comparison is
valid here; it would **not** be for a battle chunk.

⚠️ **A worked example of the inverse failure — the checker was wrong, not the file.** A first-pass
ellipsis checker reported DATA 574 as a dot-count mismatch (JP nine runs of 3, EN `3/4/4/4/3/3/3/3/3`).
It was the checker: **three of the source runs are `・・・。` — an ellipsis followed by the source's
own `。` — and `．．．．` is the correct rendering**, while the six bare `・・・` correctly give
`．．．`. Re-run with the `。` accounted for: **0 mismatches on all 12 runs**, control DETECTED.
**Compare a JP `・` run against an EN `．` run only after folding in a following `。`.**

### AH8. Figure corrections to the PR body (no rendering changes; §9's "your measurement wins")

`ａｓｌｅｅｐ　ｉｎ　ｔｈｅ　Ｍｉｒｒｏｒ　Ｔｅｍｐｌｅ．` is **28**, not the PR's 30 ·
`Ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ，` is **14**, not 15 · the unit has **12** ellipsis runs, not 13 ·
Flag 19's "the only non-possessive apostrophe-contraction in bank 10" overlooks
`Ｔｈａｔ’ｓ　ｒｉｇｈｔ，` at 574 — **that rendering is correct**, being §30.3's mandated form for
`そうよ` with the source's own comma, so the claim is imprecise and the translation is not.

**Flag 7's departure was re-tested and IS forced**: with the proper name that page needs **5 rows
against a 4-row limit** even under an optimal greedy wrap, and 4 rows without it.

⚠️ **Flag 20 (`ああ、` at 580) is the one departure that is NOT forced by geometry, and the PR does
not claim it is.** `Ａｌａｓ，　ｔｏ　ｔｈｉｎｋ…` **fits** — 4 rows at 22/20/17/7, measured at review
per §AC3's "measure the option you argue against". The flag argues lexically (the a-family is
spent; the lament rides on the exclamative *To think that…*) and names `Ａｌａｓ，` as a
verified-free reserve. Accepted as a disclosed judgment, with the reserve now on the record.

---

## AI. Wave 8 review — battle chunk 38 / PR #33, MERGED (2026-09-09)

Squash `7bd8e76`, merged at **round 2** (round 1 was CHANGES). Base
`claude/workflow-translation-iterate-uzlkns`. **5,577 / 8,192, 2,615 slack.** All nine gates re-run
on the round-2 file with **all-new** positive controls; glossary integration at **§47**.

⚠️ **Numbering convention: `L<n>` is the `tl/` file index with the `=== CHUNK` header as line 0 —
what `rowcheck.py` prints, i.e. dump body index + 1.**

### AI1. A "geometrically impossible" claim that was not — and it nearly cost a unit

PR #33 shipped `反旗を翻す` → `ｒｏｓｅ　ｉｎ　ｒｅｖｏｌｔ` and argued at length that PR #31's
`ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ` **could not fit** chunk 38's L18 page 2 — shape
`.TTTT`, a leading unfillable blank plus four text rows, at the wall, `{FCC0}` forbidden. It measured
**six** wordings; every one keeping all four content elements needed a fifth row, and the only one
that fitted deleted 王国 (CLAUDE.md §3). The dispatch to the reviewer said in terms that if the
geometry held and the banner form won, **chunk 38 must be PARKED**.

**All six measurements were arithmetically correct. The conclusion was still wrong.** The
obstruction is a property of **one token order**, not of the wording. The reviewer reproduced the
5-row rejection (`rowcheck`: `!! c38 line 18: 5 text rows > 4`), then re-ordered: the tail
`ｒｅｖｏｌｔ．．．．．` is 11 columns, atomic and must end the page, but it **need not be preceded by
`ｔｈｅ　ｂａｎｎｅｒ　ｏｆ`** (13; 13 + 1 + 11 = 25 > 24). Put `ｂａｎｎｅｒ　ｏｆ` on the last row with
it — `ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ．．．．．` = **21** — and it fits **four rows at ≤23** with every
content element kept, by the same §2.1 step-6 clause reorder the PR already claimed for that page.

⚠️ **THE LESSON, and it sharpens §AG6 rather than repeating it. "Measure the option you argue
against" is not enough: MEASURE IT IN MORE THAN ONE WORD ORDER.** A rejected alternative never
enters the file, so no gate ever checks it — and a *greedy* row count is a proven minimum only for
the token order it was given. Six correct measurements of six near-identical orderings produced a
false impossibility. A unit was one review round from being parked on the strength of it.

### AI2. The reviewer's own prescription was wrong by one character, and the translator caught it

Round 1's Finding 1 (`帝国軍` must keep its article, glossary §2 / §20.4 — see §47.5) prescribed
`Ｂａｄ！　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ！！`. That is **ungrammatical**: a lowercase word after a
full-stop-strength `！`. The reviewer had prepended `ｔｈｅ` to the existing `Ｂａｄ！` without
re-reading the result — the defect was invisible at round 1 only because the old wording began with a
capital `Ｉｍｐｅｒｉａｌ`. The translator shipped `Ｂａｄ，　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ！！` and
**flagged the deviation for ratification instead of applying it silently**, which is what let it be
ruled on. Measured: all three candidates are **23 columns**, so width decided nothing; the source's
own mark is `、`, and round 1 had turned it into `！` only as a consequence of the width problem the
article fix removed. **Ratified.**

⚠️ **A prescribed fix is a reviewer's draft, not a gate result. Translators should measure and read
it like any other candidate, and flag rather than obey.** This is the second time in wave 8 that a
role's output was corrected by the next role down; it is the process working.

### AI3. A gate that forced a lexical choice — `残兵` → `ｒｅｍｎａｎｔｓ`

Adopting the banner ruling, the translator found that the shorter noun is **forced, not preferred**.
Every §2-conformant wording keeping `ｒｅｍｎａｎｔ　ｓｏｌｄｉｅｒｓ` needs five rows (participial 98
columns, finite 100, possessive 95 — five rows at both 23 and 24), and the **only** four-row packing
that keeps it routes through `ｏｆ　ｏｌｄ　Ｃａｒｌｉｎｅ　Ｋｉｎｇｄｏｍ`, which breaks §2's fixed
`カーライン王国` → `Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ` (`glossary.md:71`) — **a gate-7 failure, not
an option.** Confirmed by the reviewer. ⚠️ One figure corrected in passing without changing the
conclusion: the coordinator's note gave the *participial* as 95 columns; 95 is the **possessive**
variant, the participial is **98**. Both are five rows.

### AI4. Gate 7 run FROM THE GLOSSARY SIDE — the method, adopted from PR #29's round 2

Rather than "do the terms I noticed match?", the reviewer enumerated **1,097** Japanese keys from
every glossary table row, intersected them with chunk 38's source, and checked each aligned
rendering. **27 keys occur in this chunk; all 27 conform.** Two fired as false positives and were
adjudicated rather than passed over: **`はっ`** (§6 → `Ｓｉｒ`) only as a substring inside
`はははっっ` — the method independently rediscovered §AI5's problem — and **`だって`**
(`glossary.md:5099`), whose row is scoped in its own text to *causal, sentence-initial*, while chunk
38's two instances are an incredulous echo and a concessive.

⚠️ **This is now the recommended way to run gate 6/7's sub-message sweep.** A content-word sweep
cannot reach a three-character particle phrase: `おい、` → `Ｏｉ，` (`glossary.md:2580`, with
`Ｈｅｙ，` spent on `よう、` at 2579) was missed twice in chunk 37 — by a reviewer's gate 7 **and** by
the translator's own Japanese-side sweep — and caught only key-side. **Chunk 38 ships `Ｏｉ，` and is
correct**, confirmed key-side here.

### AI5. Two corrections to existing glossary rows, both raised by the PR and both verified

1. **§28.3's `ははっ` list wrongly counted chunk 38 — struck.** Chunk 38's string is `はははっっ`,
   caught as a *substring*; in context it is **Marana laughing while taunting, answering no one**,
   where `Ｙｅｓ，　ｓｉｒ！！` is nonsense. `はははっ` is battle chunk 38 only, 0 script — a hapax.
   **The four genuine assents (c13 L2, c16 L2, c37 L1, c42 L6) and §28.3's ruling for them are
   untouched.** The §35.2 / §35.3 "a substring count is not a census" failure in a new place.
   ⚠️ **§29's `うん` co-occurrence argument cites the same list and is NOT disturbed** — `うん` is
   chunks 8, 20, 43, so striking 38 creates no overlap. Checked before striking.
2. **The wave-8 §9 seed's `マラナ` gender note was wrong — corrected in place, not merely struck.**
   It read "`〜わ` → **female**". Re-measured independently at review: sentence-final `わ` occurs
   **40** times in `battle_dump.txt` and at least four speakers are unambiguously male (c16 `ワシ`,
   c39 Doctor Crimea, c42 `俺様`, c43 Helfer). Marana's own is `あると思ったわ！！` after a volitional
   — the same masculine emphatic — and `おっさん` → `ｇｅｅｚｅｒ` (c38 L10) points the other way.
   **No rendering turned on it**: she is first person throughout and the translator wrote no gendered
   pronoun, deliberately declining `ｆｅｌｌｏｗ` (§32.2). Gender is **recorded as unfixed**.
   ⚠️ **This is the §Y6 (Cress) shape a second time — a seeded gender assertion the corpus does not
   carry. Seeds should stop asserting gender from a sentence-final particle.**

### AI6. ⚠️ A correction that was itself wrong — caught before it entered the record

PR #33's Flag 4 quoted `glossary.md` §37.1 as reading
`反乱 (bare) | ｒｅｖｏｌｔ | 2 battle / 0 script — both now rendered, so the word is closed`
and offered a §4.3 correction to it. **Read verbatim, that clause belongs to the `鎮圧` row
immediately above (line 3639), not to the `反乱` row (line 3640), which carries no count and no
closure claim at all — and 鎮圧's own claim is TRUE** (2 battle, chunks 22 and 43, 0 script; verified).
Integrating the correction as written would have struck a true statement or corrected a claim never
made. **The underlying measurement is right and went in as an ADDITION**: bare `反乱` is 3 battle
(c22, c38, c43) + 4 script (DATA 443, 785, 896, 1383), with a scoping note against §38.3's
`ｒｅｂｅｌｌｉｏｎ` for the script store. No rendering changed.

⚠️ **This is exactly what §AF3 was written for: a wrong correction is worse than a wrong figure,
because it enters the record as fact.** Verify a quotation by reading the line, not by trusting the
quote — including when the quoting agent has been right about everything else, as it had been here.

### AI7. ⚠️ An "unrecorded" divergence that was already recorded — and a DATA/FILE trap inside it

PR #33's Flag 5 reported that `pending/chunk_005.txt`'s village line diverges from §27.2 and that
"**no section records it**". **It is recorded**: `pending/README.md` line 31 carries exactly that row,
with exactly that fix, from **PR #18's review**. No duplicate row was added — a second entry would
have read as a second, independent finding. The rediscovery is still worth having: an independent
positional sweep reconfirms the row is still open and still the only message-level divergence in the
corpus.

⚠️ **And the line numbers are NOT in conflict.** Flag 5 and the reviewer's gate-6 output say **18**;
`pending/README.md` says **19**. The reviewer opened the file: the line is **file line 19 = body line
18**. **Both are right, two conventions** — the §AE5 / §AF3 DATA-vs-FILE trap in a new file. Neither
was "corrected" into the other.

### AI8. A lookup key that no glossary row recorded — cross-unit with chunk 41

`アイテムを奪われました。` exists in the dump in **two source forms**, and they are different lookup
keys. §21.3 fixes the **broken** form `アイテムを{FFFE}奪われました。` and counts it seven times —
**exact, verified** (c3 L8, c9 L13/14/15, c28 L7, c29 L15, c30 L10). The **unbroken** form is a
separate **4** instances — **c38 L22, c39 L9, c41 L10, c41 L12** — and no row recorded it. Chunk 38
renders it byte-identically to §21.3's English with the one `{FFFE}` added; that break is **forced,
not elective** (unbroken the line measures **28** columns, over the hard 24). Recorded at §47.6.
⚠️ **PR #30 (chunk 41) carries this form twice and must match byte-for-byte** — held to it at that
review. The mirror case is `村が襲われました。`, which is **always unbroken** in the source (13
instances, 0 broken) and also 28 on one row, so §27.2's added break is the only form there has been.

### AI9. Figures, for the record

| | |
|---|---|
| bytes | **5,577 / 8,192 — 2,615 slack**; byte cost re-derived from an independent implementation, not read off `assemble.py` |
| growth | 1,080 JP → 2,333 EN readable characters, **2.16×** against a **3.37×** ceiling |
| rows | **135 text rows** (source 129), widest **23**, twelve at 23, **none at 24** |
| pages | no page over 4 text rows; no never-attested `.TTTT.`; three source-blank **trailing** segments filled at 0 bytes (§45.2) |
| tags | non-`{FFFE}` stream **byte-identical on all 24 body lines**; `{FFFE}` **105 → 108** (lines 1, 20, 22 only); `{FCC0}` **12 → 12** |
| controls | structure, geometry and duplicate checkers each **positive-controlled with planted corruptions at new sites in round 2**, all fired |

## AJ. Wave 8 review — battle chunk 37 / PR #29, MERGED (2026-09-09)

**5,037 / 8,192, 3,155 slack.** Three review rounds, five findings, **three of them gate-7
failures**. Every gate re-run in full each round, with both positive controls **re-planted on the
file under review** rather than replayed — round 3's plants were deliberately different from rounds
1 and 2 (L15's half of the internal duplicate rather than L16's; dots 8 → 9 rather than 8 → 7).

### AJ1. ⚠️ OPEN, for a human — CLAUDE.md §6's gate 6 is structurally blind to term drift

Gate 6 as specified pairs whole **messages**: for every Japanese message of the unit that recurs
elsewhere, compare the English. A term that recurs **inside differently worded messages is invisible
to it**, and nothing in §6 covers that case.

**Gate 6 passed cleanly at this unit's round 1 while FOUR terms were wrong** — `全滅` (against three
merged files), `始末` (a scoped row read as general), `やはり` (a row naming this unit's own line)
and `おい、` (a row saying “the form is fixed from here”). The gate was not at fault; it was doing
exactly what §6 asks.

**The missing check is a Japanese-side sub-message sweep, and §AI4 now records how to run it: from
the GLOSSARY'S KEYS, not from the terms the unit noticed.** This unit is the evidence for why that
distinction is load-bearing rather than stylistic — see §AJ2. **Proposed §6 edit, for a human:** add
a ninth gate, *“every glossary key that occurs in the unit's source is checked against the unit's
rendering”*, and say in gate 6 that message-level pairing does not discharge it.

### AJ2. The three gate-7 failures, and why each escaped the round before

| Round | Term | Row | Caught by | Missed by |
|---|---|---|---|---|
| 2 | `やはり` | §37 — its instance list **names `やはり反乱軍の`**, this unit's L6 | the translator's Japanese-side sweep | the reviewer's gate 7, run as “do the terms I noticed match?” |
| 2 | `始末` | §37 — scoped “a hapax **in this sense**” to chunk 22's political euphemism | the same sweep | the reviewer, who read the scoped row as general and wrote so in round 1 |
| 3 | `おい、` | §32.3 “**the form is fixed from here**”, re-affirmed §34.1; `Ｈｅｙ，` spent on `よう、` | **the reviewer's glossary-key-driven sweep** | gate 7 **twice**, and the translator's own Japanese-side sweep |

⚠️ **`おい、` is the decisive case and the reason §AI4's refinement is not optional: it is a
three-character particle phrase.** A sweep keyed on content words cannot reach it *from either side
of the review*. Only enumerating the glossary's own keys does.

**Round 3's figures: 1,127 keys enumerated (969 unique); 46 occur in chunk 37's source; all 46
adjudicated.** The enumerator was controlled **in both directions** — a planted key present in the
source is reported (47), a planted key absent from it is not (46). Six hits were sweep artifacts and
were adjudicated by reading rather than passed over (`で、` only inside `にまで、`; `でも` only inside
`とでも`; `反乱` only inside `反乱軍`; `って` only inside `ってわけ` / `されたって`; `はっ` only
inside `ははっ` — independently rediscovering §AI5's substring problem; and `ああ`, an artifact of
the splitter stripping `〜` from §32's `あ〜あ`, which is absent from the source). Three more were
**out of scope by their own wording**: §4482's `王子 (bare vocative)`, §1734's `編成` (the UI verb,
not `再編成`), §1727's `同盟` (the noun, against this unit's `同盟国`).

### AJ3. ⚠️ OPEN — a §4.3 debt on `おい、` in three MERGED files: four plain instances plus one stammer

Fixing chunk 37 exposed that §32.3's `おい、` → `Ｏｉ，`, written at chunk 20's merge in wave 4, was
already contradicted by merged work at the moment it was written, and was contradicted again
afterwards without anyone noticing. Paired positionally against the dump at this review:

| File | Source | Shipped | Re-cut | Δ |
|---|---|---|---|---|
| `chunk_000` ×3 (wave 1) | `おい、しっかりしろ。` / `おい、お前。` / `おい、お前！` | `Ｈｅｙ，　…` | plain swap to `Ｏｉ，` | −2 bytes each |
| `chunk_008` ×1 (wave 3) | `おい、いいのか？` | `Ｈｅｙ，　ａｒｅ　ｙｏｕ　ｓｕｒｅ？` | plain swap | −2 bytes |
| `chunk_031` ×1 (wave 7) | **`お、おい、あれ`** | **`Ｈ，　ｈｅｙ，　ｉｓｎ’ｔ　ｔｈａｔ　ａ`** | **`Ｏ，　ｏｉ，`** — a stammer, not a plain swap | −2 bytes |

⚠️ **It is four plain instances plus ONE STAMMER, not five of a kind** — the translator's
measurement, verified here. `chunk_031`'s source is `お、おい、`, and its re-cut composes the way
§34.1 composes `おいおい、` → `Ｏｉ，　ｏｉ，`, which is a separate small decision. ⚠️ **`FLAGS.md`
§AG3 looked at that very line and passed it** — but for its *stutter case*, not its word choice, so
the divergence has never actually been ruled on. **Every re-cut is byte-negative** (`Ｏｉ，` is a
column shorter than `Ｈｅｙ，`), so **none is budget-blocked, including `chunk_000` with its 27 bytes
of slack** (§G1). **For a corrections unit, not for a translator mid-wave.** Chunk 38 ships `Ｏｉ，`
and is correct (§AI4).

### AJ4. ✅ SETTLED — §Y6 is discharged, and §Y6's own premise is REFUTED. Cress is FEMALE

§Y6 asked whoever took chunk 37 to settle Cress's gender, on the stated ground that *“No shipped
English anywhere genders Cress — `chunk_008` L4, `chunk_013` L1/L2 and this unit are all
first-person, vocative or subject-less.”* **The second half of that sentence is false**, and it was
false when it was written.

Read at this review, not taken from a citation: `dumps/battle_dump.txt` chunk 13's **only** `クレス`
line carries `その方、クレスと申したな。` … `女隊長と聞いておったから` … `なかなかの上玉ではないか`
… `ギルフォード将軍に献上してやる`, and **merged `tl/battle/chunk_013.txt` has shipped
`Ｉ　ｈａｄ　ｈｅａｒｄ　ｏｆ　ａ　ｗｏｍａｎ` / `ｃａｐｔａｉｎ` since wave 3**. `chunk_022` body line 0
fixes the referent independently by addressing her as `クレス隊長`.

**The project committed to female in wave 3 and §Y6 did not notice.** Glossary §1's `クレス` row now
states the gender. ⚠️ **No rendering changes anywhere** — no shipped line uses a pronoun for her, and
chunk 37's only `クレス` is `Ｃｒｅｓｓ　ｉｓ　ｗｉｔｈ　ｙｏｕ　ｔｏｏ！！`. The dispatch's expectation
that chunk 37 would “force” the pronoun **did not hold**: every third-person referent in L14 and L18
is Hoag or Rimul. **§Y6 is corrected, not merely closed** — this is the second row this wave whose
seeded assertion the corpus refutes (§AI5's `マラナ` gender note is the other).

### AJ5. Cross-PR ruling — `掌握` → `ｓｅｉｚｅ`; PR #30 moves, not this unit

Full reasoning at `glossary.md` §48.3. In short: `ｓｅｉｚｅ` **is** already spent on three other
source words (`取り押さえ` c6/c22, `捕まえ` c21), and `ｇｒａｓｐ` is free — both facts verified. But
**§25.3's test is co-occurrence, not spend**: those chunk sets and `掌握`'s ({37, 41} + script FILE
870) are **disjoint**, so no player can see the collision in one scene, which is the licence §28.3
used for `Ｙｅｓ，`. And `ｇｒａｓｐ　Ｉｍｐｅｒｉａｌ　ｓｔｒｅｎｇｔｈ` is not idiomatic English.
**The swap in chunk 41 is free — both words are 5 columns and the row is 22 either way.** The
glossary row is left **live** for chunk 41's merge to strike (`ルート` precedent) and for FILE 870.

### AJ6. A correction to a row written five hours earlier — `占拠` was under-scoped, not wrong

§47.3 (chunk 38's merge) fixed `占拠` → `ｔａｋｅｎ` with a census naming chunks 22, **37** and 38 —
the §37-`やはり` shape again, a row naming a unit it could not adjudicate, because chunk 37 was
unmerged. Read at this review: the two `ｔａｋｅｎ` instances are **passive and punctual**; chunk 37's
is **active, progressive and distributed**, and its `ため` clause needs the standing state.
⚠️ **The rejected option was measured in FIVE word orders, per §AI's own new rule** — every one is
over the ≤ 23 preference, against a shipped page whose widest row is 22. Row scoped in place;
**no line needs revisiting**. Full table at `glossary.md` §48.4.

### AJ7. For §L3's adopt-on-re-cut list — parked `pending/chunk_005.txt` diverges from §28.3 THREE times

Raised by the translator, verified by reading the file, and **one instance more than it reported**:

- body L23 — `本当に、` → `Ｔｒｕｌｙ，`
- body L27 — **`確かに、フェイのことは残念でした。` drops the concessive entirely**
  (`Ｗｈａｔ　ｂｅｆｅｌｌ　Ｆｅｉ　ｗａｓ　ａ　ｓｏｒｒｏｗ．`)
- body L28 — `確かに、人間たちは、` → **`Ｔｒｕｅ，　ｈｕｍａｎｓ…`**

§28.3 fixes 確かに、 → `Ｔｒｕｌｙ，`. Chunk 5 predates that ruling and is **parked**, so nothing in
`tl/` is broken and nothing is owed today. ⚠️ Related and measured: `確かに` ∩ `本当に` over the
battle dump is **exactly {5, 37}**, and chunk 5 is parked — so **chunk 37 is the first and only
*shippable* unit where the clash arises**, which is why its `本当に` yields to `ｒｅａｌｌｙ` while the
glossary-fixed `確かに、` keeps `Ｔｒｕｌｙ，`. The four merged files rendering `本当に` as *truly*
(`chunk_003`, `_007`, `_019`, `_026`) contain no `確かに` and never had to choose.

### AJ8. Confirmed, not defects — recorded so they are not re-raised

- **L14 is one of §L2's eight no-`{FC50}` lines (8 text rows) and its segment count was preserved at
  8** — accepted at rounds 1 and 2. Under the pool theory an added break shifts every later selector
  index, and Blocked 4 is open, so preserving the count is the safer branch under **both** theories;
  the 8 rows are inherited either way (pristine baseline re-run each round). The price is one dropped
  adverbial (`ここまでに`), flagged as a §2.1 step-5 loss with its alternatives measured — the closest,
  `Ｔｈｉｓ　ｆａｒ　ｈａｓ　ｄｒａｉｎｅｄ　ｕｓ．`, is **24**.
- **`ａｔ　ｌａｓｔ` renders two source words inside this one file** — L6's `今日こそ` and L18's
  `やっと` — and merged `chunk_030` spends it on a third (`せっかく`). §25.3's test is per *scene* and
  these are two different scenes. The alternatives that fit were measured
  (`Ｔｏｄａｙ　ｔｈｅｎ` 20, `Ｔｏｄａｙ，　ｔｈｅｎ` 21, `Ｔｏｄａｙ　ｉｔ　ｉｓ` 21) and are all **worse**
  renderings of `こそ`'s emphatic focus. Recorded, not passed silently; noted for whoever re-cuts L18.
- **`ｏｕｒ` → `Ｏｕｒ` (L18) was the only genuine lowercase sentence-start in the whole battle
  corpus.** Scanning all shipped files reported seven hits; six were classified by reading and are
  false positives — four follow an ellipsis (`chunk_004`, `_008`, `_019`, `_026`), one follows a
  stripped `{FC00}{=0000}` that supplies the capital in play (`chunk_021`), and `chunk_030` L5 is a
  subordinate clause split by a `{FCC0}`.
- **`{FCA8}` appears once (L15)** and chunk 37 is **not** one of §D1's ten affected chunks — the
  coincidence §36.8 recorded for chunk 21 and §Y7 for chunk 22.
- **`tl/battle/chunk_001.txt` has no trailing newline**, so it holds 19 lines against the dump's 20
  and a naive positional pairing skips it silently. Pre-existing; `check` passes; both this review's
  and the translator's gate-6 tools pad trailing empties so chunk 1 is genuinely compared.
- **Verified in both directions so it is NOT recorded as an error:** `HANDOFF.md` gives `決着`'s two
  script instances as DATA 1378/1380 and PR #30 gives FILE 1383/1385. **Both are correct** — same
  lines, two conventions, FILE = DATA + 5, reproduced by reading the file. The §AE5 / §AF3 trap.
- **A figure that did travel wrong and is now fixed:** PR #29's Flag 4 cited chunk 41's `決着` at
  `rowcheck` **L7**; it is **L8** (L7 is the tag-only `{FCE0}{=0001}{FFFF}`, L9 carries `掌握`).
  `HANDOFF.md`'s correction was right and the PR adopted it.

### AJ9. ⚠️ Evidence for Blocked 6's `SKILL.md` §3 edit, from this review's own working directory

The shared scratchpad this reviewer worked in held **`c037_dupes.py` and `c037_plant.py` written by
this unit's translator** alongside `r029_dupes.py` and `r029_plant.py` written by this reviewer, plus
`b010_*`, `c038_*`, `c041_*`, `c042_*`, `r033_*` and `w8_*` from six other agents — **all in one
directory, all in the same wave.** Namespacing is what kept them apart, and it held only because
every agent happened to observe it. Blocked 6 asks for `SKILL.md` §3 to bind **every** role rather
than translators alone; this is a second, independent instance of the condition that motivates it.

---

## AK. Wave 8 review — battle chunk 41 / PR #30, MERGED (2026-09-10)

Squash `3721e4d`. Merged at **round 2**; round 1 was CHANGES on **two gate-7 failures**, both fixed
verbatim. **3,035 / 8,192, slack 5,157.** Glossary section **§49**. Numbering in this entry:
`rowcheck` lines (the `=== CHUNK 41` header is line 0).

### AK1. ⚠️ LIVE — `陰謀` and `計画` both render `ｐｌｏｔ`, and they SHARE script bank 41

**Raised by the PR (its Flag 8) and confirmed exactly at review**, counted over both dumps:

```
陰謀  battle [41 x2]  script banks {28: 1, 30: 1, 41: 2}
計画  battle [24 x1]  script banks {5: 2, 41: 7}
SHARED BANKS: [41]        script lines holding BOTH: 0
```

§41.1's clearance — *"no shared chunk, no shared bank, no message holds two"* — was run on
**企み vs 計画** and is correct for that pair. It was **never run on 陰謀 vs 計画**, and for that pair
§25.3's stated test **fails on bank 41**. Both renderings are already shipped (`batch_005` L36 and
`chunk_024`), so nothing in chunk 41 could have been the fix, and **no line changes**.

⚠️ **`ｐｌｏｔ` now renders FIVE source words** — 計画 (`chunk_024`), 企み (`chunk_025`), 企てる
(`chunk_037` L18 and `batch_007` L50), 陰謀 (`batch_005` L36 and `chunk_041` ×2). **A future script
batch touching bank 41 has to fork one of them.** Bank 41 has **353 bytes free**, the tightest in the
project, so the fork must be measured before it is chosen. Recorded LIVE, on the §32.5 / §34.2 /
§34.5 / §42.4 / §45.6 pattern.

### AK2. ⚠️ The SECOND false impossibility of wave 8, and the sharpest statement of its shape yet

§AI records that a greedy row count is a proven minimum **only for the ordering it was given**.
Chunk 41's round 1 is the second instance in one wave, after chunk 38's `反旗` (§47.4), and the
translator's own round-2 diagnosis states the mechanism better than §AI1's wording does:

> **"I tested the plural only in the orderings I had already discarded, never in the one I had
> chosen."**

Round 1 argued that §30.1's fixed plural `ｒａｔｓ` could not fit L1 page 3, and **every figure it
gave reproduces**: the rejected literal is **68** columns, the fixed `Ａｌｌ　ｕｎｉｔｓ，　ｔａｋｅ
ｂａｔｔｌｅ　ｓｔａｔｉｏｎｓ！` is **32**, the page is `.TTTT` with an unfillable leading blank, and
32 + 1 + 68 = **101 > 92** — still over at the 96 hard wall. **None of it licensed the conclusion.**
Eleven orderings were measured at review, at 23 and at 24; **four fit**, and the cheapest is the
unit's own shipped sentence with one letter added (22 / 22 / **23** / 21 = 88 of 92, breaks
untouched, +2 bytes).

**Both of this wave's false impossibilities have the identical shape:**

| | claimed impossible | the counterexample |
|---|---|---|
| chunk 38 (§47.4) | `反旗を翻す` in four rows | the same wording with `ｂａｎｎｅｒ　ｏｆ` moved one row down |
| chunk 41 (§AK2) | `ネズミども` plural in four rows | **its own shipped sentence plus one letter** |

> **The rule, restated so it is actionable rather than cautionary: when you reject an option as
> impossible, the LAST ordering you must test is the one you actually chose, minimally edited to
> carry the rejected element.** That is the ordering a greedy search never reaches, because it was
> never a candidate — it was the answer.

⚠️ **And a corollary found at this review, on the `帝国兵` drop of the same unit (§49.7): a total-column
bound does NOT rescue you either.** The shortest wordings keeping 兵 + 力 + も measure **89–92
columns, under the 92 budget**, yet **all ten need five rows** once packed. Totals are necessary,
never sufficient; greedy wrapping wastes columns at row ends. **Pack the candidate, do not total it.**

### AK3. `決着をつけてやる` — the SCRIPT half, which no glossary row carries

The coordinator's mid-task note to chunk 41 named three battle instances. **Measured over both dumps
with tags stripped, and confirmed independently at this review: 4 battle + 2 script.**

```
battle : chunk_030 x2, chunk_037 x1, chunk_041 x1
script : bank 41 x2  —  script_unique 1383 and 1385
                        『事と次第によっては、この場で決着をつけなけりゃならんが。』
```

All four battle instances are now rendered and all four share `ｓｅｔｔｌｅ` (§43's row). **The two
script lines are untranslated, sit in bank 41 — 353 bytes free — and `HANDOFF.md` has unique
1355–1387 as currently unshippable**, but whoever eventually cuts them owes `ｓｅｔｔｌｅ` too, and no
glossary row states it. Recorded here so it is not re-invented.

⚠️ **A naive grep for `決着をつけて` over the raw dump returns chunks 37 and 41 only and misses
`chunk_030`, which writes it `決着を{FFFE}つけて`.** Strip tags before matching. Same tag-split trap
as §33.1's `トレジャー|ハンター`.

### AK4. `野郎` has four collocation-selected renderings and no glossary row

Recorded as a drift risk, not a defect — **nothing is re-cut and §25.3 is met** (chunks 7, 37, 41 and
43 are disjoint; the script side is banks 20, 23, 28).

| Where | Japanese | English |
|---|---|---|
| `chunk_007` L13 | `下衆な野郎は、許さねえ。` | `ｌｏｗ　ｓｗｉｎｅ` (as a unit) |
| `chunk_037` L15 | `野郎、俺がちょっと` | `Ｔｈｅ　ｗｒｅｔｃｈ，` (bare vocative) |
| **`chunk_041` L8** | `口だけは達者な野郎だぜ。` | **no noun at all** — `ｔｈａｔ　ｏｎｅ’ｓ　ａｌｌ　ｔａｌｋ．` |
| parked `chunk_043` L6 | `卑劣な野郎だ・・・。` | `ｃｕｒ` |

Chunk 41 spends **no new noun**, putting the contempt in the demonstrative (§31.2 / §41.1), so it
**cannot collide by construction** — which is why it is the one instance that needs no defence. The
§32.2 `〜の奴` shape: the word is not fixed, the register is.

### AK5. A gate-6 artifact that reads as a divergence and is not — proved with a REVERSE control

`助かりました！！` is reported divergent at SEGMENT level between `chunk_013` and `chunk_041`, and the
PR's own gate-6 output presented it as the `ｍｅ` / `ｕｓ` divergence it was arguing about. **It is
not.** Setting `ｍｅ` → `ｕｓ` at review does **not** clear the report:

```
c013 L04  JP |助かりました！！|   EN |Ｙｏｕ　ｓａｖｅｄ　ｕｓ！！|
c041 L09  JP |助かりました！！|   EN |Ｙｏｕ　ｓａｖｅｄ　ｍｅ！！　Ｉ　ａｍ　ａ|
```

c041's slot carries the **following clause** because the English re-flowed across the break, so its
segment text can never equal c013's whatever the object is. The §33.8 / §34.9 / §31.4 trap family in
a new place. **A positional row checker cannot be read as evidence about a word choice unless the
two slots hold the same clause** — check that first. The ruling stands on the message level
(§49.5), where gate 6 reports **0 divergences**.

⚠️ **A second control lesson from the same unit, and it is about controls rather than about this
row.** The PR's own gate-6 control was planted at sites its checker did not cover — the corrupted
strings recur nowhere else, so nothing was ever compared and the control proved nothing while
appearing to pass. **§AE7 says a control is only evidence for the file and run it was planted in;
this adds: it is only evidence for the SITES the checker actually covers.** State the coverage set
first, then plant inside it. Chunk 41's is small and worth quoting as the shape of the thing: of
**7 message / 20 page / 68 segment** keys, only **1 / 1 / 4** recur in another translated chunk.

### AK6. ⚠️ OPERATIONAL — a review worktree was rewritten between rounds, under a live reviewer

Recorded because it could have corrupted a merge silently and nothing in the board warns of it.
Between chunk 41's round 1 and round 2 the worktree assigned to that reviewer was rewritten: branch
`review` had been reset to track **`origin/tl/battle-042`** at a different merge commit, with staged
changes adding chunk 41 and deleting chunk 42 — **PR #31's review state**, in PR #30's reviewer's
worktree. A reviewer that had run `git checkout` and proceeded would have gated the wrong tree.

**What it did instead, and what should generalise:** gate 2 was verified with
`git merge-tree --write-tree` (a pure object operation that touches no working tree), and **every
other gate was run against an isolated checkout extracted from that exact merged tree** with
`git archive`. The contaminated worktree was left untouched. The integration commit was then built
with a temporary index (`GIT_INDEX_FILE`) and `commit-tree`, so nothing was checked out at all.

> **A reviewer's gates do not need a working tree. When one is unsafe, `merge-tree` + `archive` give
> a provably correct one, and `commit-tree` writes the integration commit without a checkout.**

### AK7. Figures corrected at this review — none touches a line of any file

| # | Claim | Measured |
|---|---|---|
| 1 | glossary §48.3: `ｇｒａｓｐ` / `ｓｅｉｚｅ` rows "both **22** columns" | **21.** Measured with `len()` three times — reviewer at round 1, translator independently at round 2, and again at merge. **Corrected in place at §48.3** |
| 2 | PR body: "English budget ~3,875 chars; **spent ~1,000**" | **1,293** readable EN characters, **33.4 %** of the budget, growth 2.1804× |
| 3 | PR body: `Ｙｏｕ　ｓａｖｅｄ　ｍｅ！！` is "the first singular referent in the corpus" | **Not first** — `chunk_012` ships `助かったぜ、あんちゃん！` → `Ｙｏｕ　ｓａｖｅｄ　ｍｅ，　ｌａｄ！` (§23.4). The correction **favours** the shipped form |
| 4 | PR body: `よくぞ` → "**First rendering anywhere**" | True of よくぞ, **false of the English string**: merged `chunk_037` L15 ships `Ｓｏ　ｙｏｕ　ｈａｖｅ` for `やっと`. Disjoint chunks, §25.3 met. A freeness claim that was not measured (§AC3) |
| 5 | PR body: `ｔｏｋｅｎ` / `ｋｉｌｌｅｒｓ` treated as free | Neither is — `batch_006` unique 631 and `batch_003` respectively. Both survive §25.3; recorded so they cannot drift |

**Everything else in the PR body re-counted at review is exact** — 副官, 番人, 衰弱, 本望, 協力の証,
口だけは達者, 一歩たりとも (chunk-41 hapaxes, 0 script), ともども vs もろとも, ぬぬ, 無念, 掌握,
陰謀 / 計画, and every headline figure. That is a good record.

---

## AL. Wave 8 review — battle chunk 42 / PR #31, MERGED (2026-09-10)

Squash `35944da`. **3,627 / 8,192, 4,565 slack**; JP 698, headroom 6,225, ratio 5.46. Three rounds,
**three findings, none of them visible to gate 6.** Glossary section **§50**.

### AL1. ⚠️ §AG6's MIRROR — measure the rejected alternative, but SEARCH FOR THE INCUMBENT FIRST

The round-3 finding, and the sharpest formulation this wave produced. The unit shipped
`くそっ・・・！！` → `Ｂｌａｓｔ　ｉｔ．．．！！`, having verified `Ｂｌａｓｔ` free and having correctly
established that `Ｄａｍｎ　ｉｔ` was **not** free (§39.4 fixes it for `しまった`-after-a-grunt;
`pending/chunk_005` spends it on `何てこった。`). Every one of those measurements was right.

**What was never asked is what English `くそ` itself already had.** `chunk_012` L11 has shipped
`クソッ、無念だ・・・。` → `Ｄａｍｎ，　ｈｏｗ　ｂｉｔｔｅｒ．．．．` since wave 3. One word, two kana
spellings, two English words in two shipped files.

> **In the translator's own words at round 3:** *"I asked whether `Ｄａｍｎ　ｉｔ` was free, found it
> wasn't, and reached for a new word — without ever asking what English `くそ` itself already had.
> **I measured the rejected alternative and never looked for the incumbent.**"*

**§AG6 / §AC3 say: measure the option you argue against. This adds: before reaching for a new word,
search the corpus for the form the SOURCE WORD already carries** — including its other kana
spelling, which no grep on the exact Japanese will find. Fixed at **glossary §50.1**;
`Ｂｌａｓｔ` now occurs nowhere in `tl/` or `pending/`.

⚠️ **The error sat one question upstream of everything the unit measured, which is exactly why no
gate caught it.** Flag 6's reasoning is correct and is *preserved* by the fix.

### AL2. ⚠️ THREE FINDINGS, AND GATE 6 WAS BLIND TO ALL THREE — measured, not asserted

CLAUDE.md §6 gate 6 pairs whole **messages** on exact Japanese. Every finding in this unit was a
term inside a differently-worded message, so gate 6 passed clean at all three rounds while the
defects stood. **Demonstrated with a reverse control at each round** (§AK5's method): reverting a
fix and re-running gate 6 raises **zero** new problems.

| Round | Term | Governing rule | Why gate 6 could not see it |
|---|---|---|---|
| 1 | `ははっ・・・・` → `Ｓｉｒ．．．．` | §28.3, which **names `c42 L6`** | `ははっ・・・・` is a unique row string in the corpus |
| 1 | `たかが` → `Ｍｅｒｅｌｙ` | §19.1's `ｏｎｌｙ` | different messages in chunks 1, 25, 42 |
| 3 | `くそっ` → `Ｂｌａｓｔ　ｉｔ` | the kana-variant rule | chunk 12's key is `クソッ`, a different string |

This is §48.5 / §AJ1 reproduced three times in one unit. **The key-first gate-7 sweep found the
first two; only a term census found the third**, because `くそ` has no glossary row at all — a
glossary-key sweep cannot surface a word the glossary never recorded. **That is a real limit of the
§AI4 method and it should be written down**: key-first covers everything the glossary knows, and
nothing it does not.

### AL3. ⚠️ THE PAGE-SHAPE CENSUS IS METHOD-SENSITIVE, AND ALL THE PUBLISHED FIGURES ARE CORRECT

Three censuses of `.TTTT` / `.TTTT.` / `TTTT` were in circulation and disagreed (§45.2's
182 / 0 / 389; PR #32's reviewer's 325 / 1; the wave-8 coordinator's 126 / 3 / 133). **Re-run over
all 44 pristine chunks at this review, twice. There is no disagreement about the data — only about
what counts as a page boundary, and both reproduce exactly:**

```
METHOD B — pages split on {FCC0}/{FC30}/{FC51}/{FC50}/{FFFF}   (rowcheck.row_problems' own set)
   TTTT 389   .TTTT 182   TTT. 276   .TTT. 132   TT 262   TTT 115   .TTTT. 0     total 1,874
METHOD A — pages split on {FCC0} only
   TTTT 133   .TTTT 126   TTT.  75   .TTT.  68   TT  57   TTT  27   .TTTT. 3     total   916
```

**Method B reproduces every one of §45.2's seven published figures, `.TTTT.` = 0 included. Method A
reproduces the coordinator's 126 / 3 / 133 exactly.** §45.2's numbers were never wrong: they are
stated in the boundary set used by `rowcheck`, which is the tool that actually gates rows, and its
`.TTTT.` = 0 is **correct as scoped**. `.TTTT.` becomes 3 only under a different definition of
*page*.

> **Ruled: §45.2 and §AG1 stand unchanged** — the ruling needs `.TTTT` to be common and it is under
> either method (182 or 126). **No rendering changes anywhere.**
>
> ⚠️ **A page-shape figure is meaningless without its boundary set. Every published census must
> carry its method or it cannot be reproduced, and three agents will derive three answers from the
> same dump.** Rows: split on `{FFFE}`; a row is *text* if it has non-tag content after stripping;
> structural lines excluded; wholly empty page fragments dropped.

⚠️ **ONE DESCRIPTION STILL DOES NOT REPRODUCE, and the diagnostic is the TOTAL, not the shapes.**
`batch_010`'s reviewer states its method as *"pages on `{FCC0}`, rows on `{FFFE}`, blank = no
non-tag content, `=== CHUNK` headers and `{PAD n}` excluded"* and reports **182 / 0** — but that is
the answer **my Method B** gives, and my implementation of *that stated method* is Method A, which
gives 126 / 3. The wave-8 coordinator attributes the spread to "what counts as structural"; **that
cannot be the cause** — structural lines carry no `{FFFE}` and no text, so excluding them or not
moves the counts by a handful at most.

**The cause is the page-boundary set, and the way to prove it in one step is to compare TOTAL PAGES
COUNTED, not the shape rows**: `{FCC0}`-only yields **916** pages over the 44 chunks; the `rowcheck`
set yields **1,874**. Any two censuses whose totals differ by that factor are not disagreeing about
shapes at all. **Whoever next quotes a page-shape figure should publish the total alongside it** —
it pins the method independently of the thing being argued about.

### AL4. ⚠️ A CORRECTION NOTE BAITED A WRONG CORRECTION — mine, and it is the reviewer's error

At round 1 I read `glossary.md` §48.3 as stating **22** columns for the `掌握` row and flagged it;
it did read 22 then, and PR #30's merge corrected it in place to **21**. **At round 2 I asserted
that it "still reads 22 in the merged base" without re-reading the file at the moved base.** It
does not. The cell reads *"both **21** columns"* followed by
`⚠️ CORRECTED IN PLACE 2026-09-10 (§4.3, PR #30's merge): this cell read 22.`

**§48.3 is correct and is NOT touched.** The transferable part is the trap:

> ⚠️ **A record that documents its own former error still contains the wrong figure.** A
> carried-forward memory — or a grep — reads the correction note's historical value as the live
> one. **Corrections written in place must be read in place**, at the head you are actually
> committing against, and never quoted from a reading of an earlier base.

This is the third §AE5 / §AF3-class wrong correction of wave 8 and the **first baited by a
correction note rather than by a DATA/FILE offset**. My own round-1 review had told the translator
to take section numbers by reading at commit time; I did not do it for this one.

### AL5. ⚠️ §AG6 EXTENDS TO THE PR BODY'S OWN PROSE

Round 1 found **five wrong widths in PR #31's body out of 55 stated**, and **all five were in prose
about rows that are correct as shipped** — `ｂｒｅｔｈｒｅｎ` 9 (is 8), `ｅｘｔｅｒｍｉｎａｔｅ` 13 (11),
`Ｉｎｓｏｌｅｎｃｅ，` 12 (10), bare `Ｗｉｎ　ａｎｄ　ｙｏｕ　ａｒｅ　ｒｉｇｈｔ` 22 (21), `Ｂｕｔ．．．！？` 9
(8). Everything **entering the file** was `len()`-measured; the **write-up** was hand-counted.

> **§AG6 has covered rejected alternatives. It must also cover the write-up**, because those
> figures are what the glossary inherits — a reviewer who copies an additions table copies its
> arithmetic. Corrected at §50.4.

⚠️ **And the reviewer is not exempt**: I hand-counted `Ｓｏ　ｌｏｎｇ　ａｓ　ｏｎｅ　ｈａｓ　ｗｉｔ．` at 22
and nearly issued a correction to a figure the PR had **right** at 23 (`Ｃａｒｌｉｎｅ` is seven
letters, not eight). Caught by measuring before writing.

### AL6. ⚠️ A NUMBERING CONVENTION DECLARED AND THEN NOT APPLIED — 17 citations, all one low

PR #31 declared `rowcheck` numbering (`=== CHUNK` header = line 0) and applied it correctly to its
own file, but its **corpus** citations were 0-based body indices — **17 of them, every one exactly
one low**: `chunk_018` L9 (is **L8**), `chunk_025` L13 (**L12**), `chunk_012` L3 (**L4**),
`chunk_010` L1 (**L2**), `chunk_034` L5 (**L6**), `chunk_013` L7 (**L8**), `chunk_020` L1 (**L2**),
`chunk_000` L4 (**L3**), `chunk_006` L11 (**L12**), `chunk_033` L19 (**L20**),
`pending/chunk_043` L1/L29/L34 (**L2/L30/L35**), `chunk_013` L1 (**L2**), and Flag 7's six `はっ！`
cites. **Root-caused at round 2, not patched**: the scratch helpers printed a 0-based body index and
the conversion was applied at the citation site rather than at the print site. **The helper now
converts where it prints.** The `chunk_018` **L8** in the wave-8 dispatch was right and the PR's L9
was not.

### AL7. Evidence for §L2's pool reading, from a second chunk — `はっ！` is 7 of 7

Carried here for whoever makes the chapter 5/6 in-game visit (**Blocked 4**). Chunk 42 L11 is one of
§L2's eight lines: **no `{FC50}`/`{FC51}` anywhere, 16 text rows in the source, 21 shipped.**

`はっ！` lands **mid-way through a run of Helfer's taunts**, where a subordinate's assent makes no
narrative sense — and CLAUDE.md §3 forces `Ｓｉｒ！` there, because the form is **7 of 7** across
the shipped tree: `chunk_002` L14 and L20, `chunk_008` L10, `chunk_013` L2, `chunk_022` L5,
`chunk_031` L2, `pending/chunk_017` L6. **No exception anywhere.** L11 also carries the soldiers'
`ヘルファー様、万歳！！` beside Helfer's own speech. That is a **second, independent** consistency
argument for pools of independently-selected strings, from a different chunk than §AE6's chunk 30.

⚠️ **The PR counted 6 of 6 and missed `chunk_013`** because that line's English is offset by one —
it compresses JP rows 6–9 into EN rows 6–8 and leaves EN row 9 blank, so from index 10 on
`en[k−1]` answers `jp[k]`. **A positional harvest mispairs `はっ！` with `Ｈｏｗｅｖｅｒ，` and
`しかし、` with the row after it.** Any corpus sweep touching `chunk_013` line 2 must apply that
offset; it also mispairs `ははっ！` (真 `Ｙｅｓ，　ｓｉｒ！`) and `つべこべ言わず` (真
`Ｎｏｗ，　ｎｏ　ｍｏｒｅ　ｔａｌｋ．`).

**§24.2's no-merge property was verified specifically**: 16 source entries, all present in order,
five splits **inside** single entries, **no two entries merged**.

### AL8. Method notes worth keeping

- **No working tree was used for any gate, at any round** (§AK6). Gate 2 by
  `git merge-tree --write-tree`; every other gate on a `git archive` extraction of the resulting
  tree; provenance by `cmp` against `git show <head>:<path>` plus a sha256. **My worktree shared
  branch `review` with another live agent's at `e450094` for the whole review** — the collision
  §AK6 describes is structural, not a one-off, because worktree branch names are not per-agent.
- **Gate 6 controls were re-planted at fresh sites with fresh texts at every round** — round 1 hit
  the second `万歳` cheer and the L11 copies; round 2 the first cheer, the L2 copies and
  `ヘルファー！`; round 3 the third `万歳` instance and third texts throughout. Coverage is only 4
  cross-file and 3 internal keys, so **rotating the text and the copy is what keeps the control
  honest** when the sites are nearly exhausted.
- ⚠️ **Two of the reviewer's own checkers failed a planted control before the file did.** A
  substring test over a whole line passed a corruption because the JP key had a spurious second
  corpus rendering that happened to appear elsewhere in the same line; and a checker harvesting only
  row-aligned lines missed internal duplicates spanning an aligned and an unaligned line. The fix is
  to require the expected English as a **whole `{FFFE}`-delimited row** and to carry the unit's own
  aligned rows forward into its unaligned lines. **§AE7 one level deeper: a control planted inside
  coverage can expose the checker, not only the file.**
- **Gate 7 figures, for the record:** round 1 — 2,261 distinct glossary keys, 103 occurring, 2
  failing; round 3 — **2,329 distinct keys (5,020 occurrences), 109 occurring, all adjudicated,
  0 failing.** Gate 6 corpus grew from 2,163 to **2,225 distinct segment keys / 2,494 aligned rows**
  as chunks 037, 038 and 041 shipped. **Coverage each round: 79 segment keys (75 distinct), 4
  recurring elsewhere, 3 internally; 0 of 25 page keys and 0 of 6 message keys recurring.**

### AL9. Bank pressure — unchanged by this unit

Battle-only; no script file. Tightest banks stand where PR #28 left them: **41 → 353, 40 → 75,
5 → 1,635, 2 → 3,365.**

## AM. Wave 8 review — script batch 010 / PR #32, MERGED (2026-09-10)

Squash `b9ba9d5`. 53 unique lines / 293 message instances. Two rounds; **five findings at round 1,
every one a gate-7 failure, all five fixed at round 2.** Gated with **no working tree at all**
(§AK6): `merge-tree --write-tree` → tree `2e4c77bf` at round 2 (`6ec0bede` at round 1), all gates on
a `git archive` extraction, provenance proved by `cmp` + sha256 + blob id against
`git show bf2f663:tl/script/batch_010.tsv`.

### AM1. Byte figures — the wave's tightest numbers, confirmed on the final tree

Differenced against a `git archive` of the base, not read from the PR, at **both** rounds:

| bank | before | after | spend |
|---|---:|---:|---:|
| **40** | 447 | **75** | **372** |
| **41** | 353 | **353** | **0 — not in the moved set at all** |
| **5** | 2,007 | **1,635** | 372 |
| 25 | 12,891 | 11,829 | 1,062 (372 + prose) |
| 26 / 27 / 28 | — | — | 122 / 120 / 4,104 (prose only) |

**Banks under 2,000 free after this merge: bank 40 (75), bank 41 (353), bank 5 (1,635).** No bank
negative. The item table's growth is **exactly 372, spent in full in each of 21 banks** (2 3 4 5 6 7
8 9 12 13 14 15 16 17 18 19 25 33 40 42 43) — verified by differencing the two `bankmeasure` runs,
not by trusting the PR's table. **Bank 41 is not among them.** The whole cost of round 2's five fixes
was **+6 bytes in bank 28**, which keeps 30,737 free: as predicted, no fix touched bank 40.

⚠️ **Bank 40 should now be treated as CLOSED for item-table work.** Any remaining `script_unique`
line with count 21 spends its growth in all 21 banks including bank 40's 75 free. In particular
**DATA 281** (`軍神ヘルメスの愛用したブーツ。{FFFE}防御力＋１　魔法防御＋１`, count 21, untranslated) may
now be **unshippable**: it needs a `魔法防御` form that nothing fixes yet, beside §51.1's `Ｄｅｆ＋ＮＮ`,
and only a **zero-growth two-stat row** fits. See the live §9 `軍神ヘルメス` row.

`check` **All checks passed** (4,552 replaced / 461 unique; base 4,259 / 408 → Δ **293 / 53**,
confirmed from three independent directions). `rowcheck script` 4,655 lines, nothing non-inherited
over 4 rows. `merge` prints **zero** "never matched the dump" lines. Max English width **23**;
0 segments over 23, 0 over 24. `{FCC0}` 37 in / 37 out; `{FFFE}` count changes on exactly DATA
193/194/300/310, plus one position-only move at DATA 880.

### AM2. §4.3 DEBT IN ALREADY-MERGED WORK — `batch_007.tsv:31` capitalises a bare species plural

Surfaced by round 1's finding 5 and **verified independently at review**: `tl/script/batch_007.tsv`
line 31 ships **`Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ　ｔｅｌｌ　ｌｉｅｓ，　ｎｙｏｒｏ．`** — a capitalised bare plural in
prose, which is exactly what §17.1 (`ホビット | hobbit | lowercase in prose`) and §40.1 (the 魔族 row,
which calls ホビット → hobbit *the canonical lowercase case*) forbid. It is the **only** capitalised
bare instance in `tl/`, against lowercase `ｈｏｂｂｉｔ` in five files. The same line's
`Ｈｏｂｂｉｔ　Ｖｉｌｌａｇｅ` is **correct** — §2 place name — and its `ｈｏｂｂｉｔ　ｖｉｌｌａｇｅ　ｃｈｉｅｆ．`
is correct too.

⚠️ **The mitigating fact, recorded so the corrections unit does not over-read this:** the instance is
**sentence-initial**, so its capital is ambiguous between species capitalisation and ordinary
sentence capitalisation. That ambiguity is why it did not license PR #32's **mid-sentence**
`Ｗｅ　Ｈｏｂｂｉｔｓ`. **One isolated instance, zero-cost to fix (identical width), for a corrections
unit — it was not asked of PR #32.**

### AM3. THE SOURCE-WORD MIRROR SWEEP — §AL1 operationalised, and it is now a gate step

§AL recorded that a glossary-key-first sweep **cannot surface a word the glossary never recorded**
(how `くそ` survived two rounds). PR #32's review ran the mirror of it and it should now be standard:

> **For every kanji run ≥2 and katakana run ≥3 in the unit's source that is NOT a glossary key,
> find whether an already-translated row contains the same run, and read both English sides.**

33 such runs here. **No divergence**, and it produced three results a key-first sweep could not:

- 古代文明 → `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ`, byte-identical to `batch_008.tsv:45`, British `-s-`
  matched. 攻撃魔法 → `ａｔｔａｃｋ　ｍａｇｉｃ`, identical to `batch_003.tsv:27`, `:29`. 戦争 → `ｗａｒ`;
  無事 → `ｓａｆｅ` (four files agree); 兄弟 → `ｂｒｏｔｈｅｒｓ`; 遺跡 → `ｒｕｉｎｓ`; 立派 → `ｆｉｎｅ`.
- 感謝: the shipped family is `ｇｒａｔｅｆｕｌ` / `ｔｈａｎｋｓ` / `ｇｒａｔｉｔｕｄｅ`, and `batch_008.tsv:60`
  ships the **uncontracted** `Ｉ　ａｍ　ｔｒｕｌｙ　ｇｒａｔｅｆｕｌ．`. ⚠️ **This WITHDREW a round-1 register
  nit** against DATA 920's `Ｉ　ａｍ　ｇｒａｔｅｆｕｌ．` — the uncontracted form is the house form. **The
  sweep prevented a wrong correction, which is the point of §AG6's mirror.**
- 軍人 → `ｓｏｌｄｉｅｒｙ` here against `ａ　ｓｏｌｄｉｅｒ　ｏｆ　Ｃａｒｌｉｎｅ` at `batch_002.tsv:9`: same
  root, collective for a plural address, held apart from §30.2's `Ｓｏｌｄｉｅｒｓ，` by register. Fixed
  at §51.2 so the next 軍人 has an incumbent to read.

### AM4. ⚠️ THE PAGE-SHAPE CENSUS — the divergence was the CORPUS, not the splitter, and both prior counts were right about their own dump

This closes the dispute that ran three ways across wave 8. **§45.2's figures are a BATTLE-dump
census.** The giveaway is its own neighbouring figure `5,355 → 5,399 / 8,192` — an 8,192-byte battle
slot. Measured at PR #32's review over `dumps/battle_dump.txt` with `rowcheck`'s own boundary set
`{FCC0}|{FC30}|{FC51}|{FC50}|{FFFF}`, **all five of §45.2's figures reproduce exactly**:

| corpus (splitter = `{FCC0}\|{FC30}\|{FC51}\|{FC50}\|{FFFF}` in both) | pages | `TTTT` | `.TTTT` | `TTT` | `TT` | `.TTTT.` |
|---|---:|---:|---:|---:|---:|---:|
| **`dumps/battle_dump.txt`** — what §45.2 measured | 5,181 | **389** | **182** | **115** | **262** | **0** |
| `dumps/script_dump.txt` — the store `batch_010` lives in | 21,224 | 721 | **325** | 196 | 6,602 | **1** |

So **§45.2 and §AG1 stand unqualified for the battle store**, and the wave-8 coordinator's 325 was
right for the script store. The single script-side `.TTTT.` is `script_dump.txt` line 6899 and is a
**menu choice-block**, not an ordinary text page —
`{FFFE}　はい{FFFE}　いいえ{FFF7}…{FB01}嘘だよ。お前から金を…` — so it is not a counterexample to §3.2's
four-text-row warning either.

> ⚠️ **The durable rule is one notch sharper than §AL3's:** a page-shape census is a property of
> **(corpus, splitter)**, and these two dumps differ by ~2× on the very shape the rule turns on.
> **State the dump AND the boundary set AND the total pages beside any shape figure.** Quoting a
> battle-dump census at a script unit — or the reverse — is how three separate reviewers reached
> three answers while every one of them computed correctly.

**Moot in the safe direction for this PR:** DATA 880 page 2 goes `.TTT.` → `.TTTT`, attested **182**
in the battle dump and **325** in the script dump. It never approaches `.TTTT.`. No tag added, moved
or deleted; slot count per page unchanged. §45.2's liberty applies and the row is safe.

### AM5. Rulings issued at this review — do not re-open

- **DATA 300 keeps 3 rows; `とされる` is NOT restored.** Two independent grounds. (a) The
  impossibility was reproduced **order-independently**: the minimum faithful token set emits **74
  columns against 3 × 24 = 72**, so no word order fits — and it was extended past the PR's own
  argument, because a claimed impossibility had already been false twice this wave: dropping the
  article gives 72 vs 72 and **still does not pack**, and `ｒｅｐｕｔｅｄｌｙ` gives 71 vs 72 and **still
  does not pack**. Impossible in three formulations. (b) Independently of bytes,
  `translation_prompt.md` §3.2 records the description window's row count as **UNKNOWN** and says to
  keep description entries to 2 text lines plus the stat line until it is confirmed. **A 4-row entry
  would breach an open engine question, so the 3-row form is required, not merely affordable.**
- **`復興` — §51.3.** `ざます` — §51.2. `ああ、` (lament) → `Ａｈｈ，` — §51.2. `『してんこうせき』` —
  §51.2. `＜アイテム名＞` → `（ｉｔｅｍ　ｎａｍｅ）`, setting the precedent for DATA 127–130 — §51.2.
- ⚠️ **`ｗｈｏ　ｒｕｌｅｄ　Ｆａｒｉｎａ．` teaches something about how to spend a fix:** the round-1 finding
  could not be met by swapping a word, because the paraphrase had **displaced** the term rather than
  occupying a slot it could drop into. The proposed repack was measured before it was asked for —
  `ａｌｌ　ｔｈｅ　ｋｉｎ` + `ｔｈｅ　ｒｅａｌ　ｐｏｗｅｒ` does **not** pack even at the hard 24 (91 columns of
  content against 96 of capacity — **the total fits and the packing still fails**). **A reviewer
  asking for a fix should verify the fix packs, not merely that it fits by total** (§AK's rule,
  applied in the reviewer's own direction).

### AM6. Open, for whoever takes them

- **DATA 281** — the second `軍神ヘルメス` line, count 21, needs `魔法防御` and may be unshippable
  against bank 40's 75 free. §9 row held live. **AM1.**
- **DATA 817** — the second `ピクシー` line, untranslated; §9 row added and held live.
- **DATA 127–130** — the `＜ダミーデータ＞` rows, whose bracket precedent §51.2 now sets.
- **`お城` → `ｃａｓｔｌｅ` vs `ｃｏｕｒｔ`.** DATA 907 renders `お城では` as `Ａｔ　ｃｏｕｒｔ`; `batch_007.tsv:29`
  ships `ｔｈｅ　ｃａｓｔｌｅ`. **Deliberately not made a finding, and the measurement is why**:
  `Ａｔ　ｔｈｅ　ｃａｓｔｌｅ` on that page needs 87 columns against 4 × 23 = 92 and **no packing exists**,
  and it still does not pack at the hard 24 (87 vs 96) — a clean example of a total that fits while
  the packing fails. The page is `.TTTT` and full; 城 is not a glossary key. Recorded for the next
  unit that renders 城 in prose.

---

## AN. Wave 9 review — script batch 011 / PR #34, MERGED (2026-09-10; review closed 2026-09-11)

Town and shop NPCs, DATA 647–706, banks 14–18. **Round 2, head `a1581f3`, merged `edd6d2d`.**
Round 1 returned CHANGES with one finding; the rework fixed it and nothing else. All eight §6 gates
green at round 2, re-run from scratch on the moved base. Glossary integration at **§52**.

### AN1. ⚠️ THE WAVE-9 DISPATCH TABLE PRODUCED A FALSE POSITIVE, AND THE CAUSE IS GENERIC

The wave-9 coordinator's dispatches carried a "shipped clause" table built by splitting shipped
JP/EN pairs on `{FFFE}` / `{FCC0}` / `{FC30}` / `{FC50}` / `{FC51}` and **aligning the resulting
clauses positionally**. On `いらっしゃいませ` it asserted a corpus distinction that **does not
exist** — `いらっしゃいませ！！` → `Ｃｏｍｅ　ｉｎ！！` against `いらっしゃいませ！` → `Ｗｅｌｃｏｍｅ！`
— and instructed all three translators to preserve it.

Measured at this review, over both dumps and all of `tl/`:

```
§34.1   いらっしゃいませ / いらっしゃい / いらっしゃいノロ -> Ｗｅｌｃｏｍｅ + the source's own punctuation
§34.5   Ｃｏｍｅ　ｉｎ is a RESERVE, scoped to the bank-26 ようこそ collision, and nothing wider
§51.5   batch_010's DATA 885 spends that reserve exactly as reserved;
        "the bank-26 Ｗｅｌｃｏｍｅ collision is now discharged and the reserve is spent"
Ｃｏｍｅ　ｉｎ！！ corpus-wide: 1 instance, bank 26, and it is DATA 885.
```

So the whole evidential base for the "distinction" was **one** shipped message, and that message
sits under a documented reserve. `batch_011`'s translator rejected the instruction by reading and
flagged it as the thing it most wanted checked; both reviewers then proved it independently.

> **The cause is generic and will recur, so state it as a rule.** *Positional clause alignment
> infers a rule from whichever instances happen to be translated. A term whose only shipped
> instance sits under a documented reserve, a width forcing or any other local licence will look
> like a fixed distinction, because the licence is invisible to the alignment.*
>
> **Mitigations, both already partly in place, both now binding.**
> 1. Keep the framing every wave-9 dispatch used — "a LEAD TO VERIFY BY READING, never a ruling".
>    It worked: the translator did exactly that.
> 2. **Additionally mark any row whose evidence is a SINGLE shipped instance as such**, with the
>    count. A one-instance row is a hypothesis; the table gave it the same weight as a 20-instance
>    one.
> 3. Before trusting an aligned pair, check whether the shipped side is covered by a `glossary.md`
>    reserve or width note. Grep the glossary for the English form, not only for the Japanese.

⚠️ **This bug bit a second time inside this very review, in the opposite direction — see AN2.**

### AN2. ⚠️ A POSITIONAL CENSUS NEARLY OVERWROTE A CORRECT RECORD WITH A WRONG ONE

Instructed to correct §42.1's `で、` row, this reviewer's first census matched only segments
*starting* with `で、` and reported `batch_007`'s three rows as `で、森に住むじいさんに` →
`ｆｏｒｅｓｔ，　ｎｙｏｒｏ．　Ａｎ　ｏｌｄ` — i.e. **no `Ｓｏ，` incumbent anywhere**. Had that been
trusted, the review would have recorded that an existing, correct claim was false.

A second, direct census — `grep` for the substring over whole rows, then read every aligned
segment of every hit — found the truth: `batch_007.tsv` L40, L50, L61 each ship
`で、今日はどんな用ノロ？` → `Ｓｏ，　ｗｈａｔ　ｃａｎ　Ｉ　ｄｏ` / `ｔｏｄａｙ，　ｎｙｏｒｏ？`, with
`で、今日は` sitting **mid-segment**, which is why a "starts with" matcher missed all three. Bank
census: `で、今日はどんな用ノロ` = bank 3 (4 instances); `で、どんな` = bank 4 (2); this unit's
`で、今日は何のご用で` = bank 16 (2).

> **Rule: a substring census must match the substring, not the segment. "Starts with" is a
> different query and will silently return zero.** This is the same family as §AL4's
> "re-asserting a round-1 reading after the base moved" and §AG6's "quoted without its corpus" —
> *a census needs its splitter, its dump AND its matcher stated.*

The record fix itself is written out at **glossary §52.3**: `で、` has **two** shipped Englishes —
`Ｎｏｗ，` (bank 4 and siblings, §42.1) and `Ｓｏ，` (bank 3, `batch_007`, since wave 5) — and
`batch_011` takes the latter in bank 16 because §28.8's `さあ、` → `Ｎｏｗ，` already occupies that
bank *inside the same message* (D689 carries both words). **No `tl/` line moves.**

### AN3. PR #34's Flag 3 was incomplete in its own favour, and PR bodies keep doing this

Flag 3 stated that `Ｓｏ，` is "spent elsewhere only on `ダカラ、` in battle chunk 26". True as far
as it went (`chunk_026` L8 `ダカラ、俺タチノ敵！` → `Ｓｏ，　ｙｏｕ　ｏｕｒ　ｅｎｅｍｙ！`, verified), but
it **missed its own strongest evidence** — the three shipped `batch_007` rows above. The effect is
benign here (it turns a coinage into a reuse), but it is the fourth wave running in which a PR's
freeness or spentness sentence has been incomplete. ⚠️ **A "this form is free / spent only on X"
sentence must be produced by a census, and the census command belongs in the PR body.**

Two smaller PR-body defects, both recorded rather than made findings:

- **The body is round 1's and was never refreshed for the rework.** It still says "One commit, one
  file" and its bank table still reads bank 16 → 10,963 free. The true post-rework figure is
  **10,953** (−10 bytes). No template section is missing and no figure is absent, so §6's PR-body
  gate is not failed; the correct figures are in the merge commit title, glossary §52 and HANDOFF.
  ⚠️ **A rework should refresh the body's figures, and a reviewer should not have to carry that.**
- **The "Reuses recorded" list credits two things the source does not contain.** Measured in the
  unit: `妖精` 0, `ジェム` 0, `ｆａｉｒｙ` 0, `Ｇｅｍ` 0 (`ジュエル` 9 → `Ｊｅｗｅｌｓ` 9, 0 bare
  singular). Neither was carried into glossary §52. Same shape as §AM's own note: **a "reuse" is a
  claim about the source and needs the same census as an addition.**

### AN4. ⚠️ CROSS-UNIT AND LIVE — `『進化の木の実』` binds PR #36, which is open and unreviewed

`batch_011` D689 ships `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”` (18). `batch_013` (PR #36) L52 renders the
same named item `“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”` (15). Neither form was in `glossary.md` when either unit
was written, so neither translator overrode a ruling. **Ruled for the long form at glossary §52.5**,
on the corpus's two decided `『Ｘの Ｙ』` precedents (§12 `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”`; §33.1
`“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”`, which records the short compound as considered and **"never
fired"**), and because `batch_011` merged first and is now the shipped work.

**Width decides nothing and both directions were measured with `len()` before ruling:** #36's row
becomes `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”？` = **19** against its current 16 — inside the box, no
re-flow; conversely `ａ　“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”．` would have been 18 here against the shipped 21.
Banks **16 and 29 — disjoint**, so §25.3 is not engaged; this is a naming divergence only.

> ⚠️ **ACTION FOR PR #36's REVIEWER: this is a finding on #36.** One row, no re-flow, no tag change.

### AN5. Two unrecorded incumbents found by §AG6's mirror, and the unit matched both

`不思議` → `ｓｔｒａｎｇｅ` (`chunk_034` L5, aligned to the dump at review) and `またの機会に` →
`Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ　ｔｉｍｅ` (`batch_007` L24/L47/L58/L69). Neither is a glossary key, so
**gate 7 could not have surfaced either** — that is §AG6's standing blind spot, and the mirror is
what caught them. Both are now recorded at glossary §52.2, with `かわいい`'s two-incumbent register
split (`ｄａｒｌｉｎｇ` from `chunk_011` L3 for Maya, `ｃｕｔｅ` from `chunk_013` L5 for the keigo
shop; banks 18 and 16, disjoint).

⚠️ **Method note for the mirror itself:** a first pass searched only `tl/script/*.tsv` and reported
`不思議` as having no incumbent. `tl/battle/*.txt` holds **0 Japanese characters outside tags**
(measured over all 32 files), so the Japanese side has to be taken from `dumps/battle_dump.txt`
**aligned by line index** to the translated chunk — the dump line and the `tl/` line are the same
message. **A mirror that searches only `tl/` is half a mirror.**

### AN6. Bank state after this merge — no change to the tight banks

```
bank 14  28279 / 40960   free  12681      (-378)
bank 15  28373 / 40960   free  12587      (-412)
bank 16  30007 / 40960   free  10953      (-1106, of which -10 is the round-2 rework)
bank 17  27825 / 40960   free  13135      (-288)
bank 18  30627 / 40960   free  10333      (-290)
total growth +2,474 bytes
tightest: bank 40 75 free, bank 41 353 free, bank 5 1635 free   <- byte-for-byte UNCHANGED
```
Every other bank is byte-identical to the pre-merge baseline, verified by diffing two
`bankmeasure.py` runs. **Banks under 2,000 free remain 5, 40 and 41** — all pre-existing §F2, none
touched by this unit, and the §F2 arithmetic is unaffected.

### AN7. Gate method notes worth keeping

- **Gated with no working tree, as §AK6 requires, and this was a genuine second-round hazard.**
  `git merge-tree --write-tree` → tree `452615e`; `git archive` of that tree and of the bare
  integration head (`4504447`) into two scratch dirs, so "free before" was reproduced here rather
  than taken from the PR; provenance by `cmp` + `sha256sum` against `git show a1581f3:…`
  (`e1889a72…`), and `diff -rq` of the two extractions showing the merged tree differs from the
  base by **exactly one added file**. Round 1's evidence was discarded outright: base `0a462db` →
  `4504447` and head `855686e` → `a1581f3`.
- **Gate 6's coverage must be stated, and `tl/battle` is not part of it.** 60 unit keys vs **461**
  shipped keys across 10 files, 0 exact-key collisions, controls fired correctly in both
  directions; a second arm on **tag-stripped visible text** (58 distinct unit texts vs 423
  elsewhere) is what catches messages differing only in a portrait or jump argument, and it found
  the one real cross-file twin — D691 against `batch_009` L77/L78, byte-identical.
- **Gate 7 key count, this review: 2,322 keys enumerated / 131 occurring / 0 failures.** Five
  glossary rows *name this unit's exact lines* (§34.1 on unique 647 and 651, §34.6 on unique 652,
  plus the `いらっしゃいませ` and `ご用` rows) and all five conform — the fourth wave running in which
  the glossary-side sweep's value has come from rows that cite the line numbers under review.
- **§3.1's four-dot case was handled correctly by the unit and by the checker.** D700's
  `静まりかえっている・・・。` → `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ．．．．` — `・・・。` is **four**, not three.
  D647's bare `・・・` is three. Both match. (A round-1 reviewer's own counter got this wrong
  before catching it; the counter used here counts the trailing `。` explicitly.)

### AN8. Still open after this merge, for whoever takes these lines

- **DATA 1348** — the second `メンバーカード` line, untranslated; must take `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ`
  (glossary §52.1).
- **DATA 530** (bank 6) — readable text identical to this unit's D659; must reuse
  `Ｏｔｈｅｒ　ｂｕｓｉｎｅｓｓ？`.
- **DATA 339** (banks 17 and 18 — this unit's own banks) — menu identical to D676; must reuse
  `　Ｂｕｙ　ａ　ｍｏｎｓｔｅｒ` / `　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ`.
- **`ｗｏｎ’ｔ　ｙｏｕ` at D679 is the keigo shop's only contraction** (that scene is otherwise
  `Ｗｅ　ｓｈａｌｌ`, `Ｉ　ａｍ　ａｆｒａｉｄ`, `ｙｏｕ　ｃａｎｎｏｔ`, `Ｉ　ｓｈａｌｌ`, `Ｔｈａｔ　ｉｓ`,
  `Ｍａｙ　Ｉ　ａｓｋ`). **Read and accepted, not a finding**: a negative tag question has no natural
  uncontracted English form, and this shopkeeper is not in glossary §7's register table. Recorded
  so it cannot drift, and so the next unit in these banks knows the profile is deliberate.
- **`当店` → `ｕｓ` at D690** is a width-forced variant of §52.1's `ｏｕｒ　ｓｈｏｐ` on a 23-column row
  where the full form cannot fit (the speaker *is* the shop). Flagged by the PR, accepted, recorded.
- ⚠️ **The squash-merge title carries a literal `&amp;`** where `&` was intended
  (`town &amp; shop NPCs`) — an HTML-escaping artifact of the merge API call, cosmetic only, in
  `edd6d2d`'s subject line. Not worth rewriting history; noted so it is not read as a typo in the
  source data.
