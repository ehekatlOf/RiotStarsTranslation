# pending/ — finished translations that cannot ship yet

Files here are **finished, format-clean translations** that `assemble.py` **must not** pick up.
The directory name deliberately does not match `tl/battle/chunk_NNN.txt`, so `check`, `merge` and
`build` ignore it and the patch stays buildable with those chapters falling through to Japanese
(prompt §0.5).

⚠️ **Nothing here is unfinished work, and there are now THREE reasons a file is parked.** Read the
reason before assuming a file needs translating again:

| Reason | Files | What lifts it |
|---|---|---|
| **Over the 8,192-byte slot** | `chunk_043.txt`, `chunk_043_abridged.txt`, `chunk_005.txt` | the slot extension (`pending/slot-extension.md`, `findings.md` §23) |
| **Tooling — the `FLAGS.md` §D1 dump artifact** | **`chunk_017.txt`** (and `chunk_005.txt`, which has it *as well as* being over slot) | a `riotbattle.tokenise` fix + re-dump (`FLAGS.md` §R4) |
| **Tooling — the `FLAGS.md` §AF1 charset gate on PRESERVED SOURCE** ⚠️ **NEW 2026-09-09, and NOT the same thing as §D1** | **`chunk_036.txt`** | **one function in `assemble.py`** — skip the charset check on runs byte-identical to the dump. **No disc, no EXE, no re-dump, no dumper change.** Then a `git mv` and nothing else (`FLAGS.md` §AF1) |

Move a file into `tl/battle/` only once the constraint named in its row below has been lifted.

## ⚠️ Lines these files must adopt on re-cut

Parked files do not ship, so a divergence from shipped work is not a CLAUDE.md §3 violation
**today** — but it becomes one the moment the slot patch lands and the file moves into
`tl/battle/`. Every line below was ruled on at review against a form that has already shipped.
**Re-cutting one of these files without applying its rows creates the violation.**

| File | Line | Now | Must become | Cost | Ruled |
|---|---|---|---|---|---|
| `chunk_005.txt` | 13 | `Ｔｈｉｓ　ｃａｎ’ｔ　ｂｅ．．．` | `Ｔｈａｔ　ｃａｎｎｏｔ　ｂｅ．．．` | 16 → 17 cols, **+2 B** | PR #7 review; `そんな・・・` now shipped in chunk 6, and Cavia takes no contractions (§14.6) |
| `chunk_005.txt` | 32 | `Ｑｕｉｔｅ　ｓｏ．` | `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` | 9 → 13 cols, **+8 B** | PR #6 review, glossary §23.2; `そうそう。` shipped in chunk 4 |
| `chunk_043.txt` | 14 | `Ｗ‐ｗａｉｔ！` | `Ｗ，　Ｗａｉｔ！` | 9 → 8 cols, **−2 B** | PR #7 review, glossary §24.3; the comma form follows shipped `chunk_007`'s `Ｉｍ，　Ｉｍｐｏｓｓｉｂｌｅ．．．` |
| `chunk_005.txt` | 19 | `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ　ａｔｔａｃｋｅｄ．` | `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．` | 24 cols on one row → **14 / 13**, **+8 B** (+1 `{FFFE}`) | PR #18 review, `FLAGS.md` §X2; glossary **§27.2** is the binding entry and chunks 7 ×2, 13, 17, 21 and 34 all carry it byte-identically. ⚠️ **The only message-level divergence in the whole corpus**, found by the positional sweep at that review |

| `chunk_005.txt` | 21 (`ごめんなさい。そう言って`) | `Ｉ’ｍ　ｓｏｒｒｙ．` | `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` | 10 → 13 cols, **+6 B** | PR #25 review, glossary **§34.1**, which fixes `ごめんなさい。` → `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` and postdates chunk 5. ⚠️ **Two faults, not one**: it breaks §34.1 *and* it spends `Ｉ’ｍ　ｓｏｒｒｙ．`, which **§30.3 fixes on `ごめんね。`** — so chunk 5 currently puts two source strings on one form while the correct form sits unused. `pending/chunk_036.txt`, `tl/script/batch_006.tsv` L49 and `tl/battle/chunk_010.txt` L10 (`ごめんなさいね。`) all agree with §34.1 byte-for-byte; chunk 5 is the only outlier. The §23.2 `そうそう。` shape exactly |

| `chunk_005.txt` | **28** (file line 29) | `ｔｈｅ　ｃｒｏｗｎ’ｓ．　Ｓｅｒｖｉｎｇ` | a form built on **`ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ`** | ⚠️ **RE-FLOW, not a word swap — measured at review** | PR #23 review, glossary **§41.5**; `王家` → `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ` (15) is fixed by chunk 25, which renders it twice. ⚠️ **Substituting in place does not work**: the row is `ｔｈｅ　ｃｒｏｗｎ’ｓ．　Ｓｅｒｖｉｎｇ` (20) and `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ’ｓ．　Ｓｅｒｖｉｎｇ` measures **26**, over the 24 hard limit. A three-row shape fits — `Ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ` (14) / `ｂｅｌｏｎｇｓ　ｔｏ　ｔｈｅ` (14) / `ｒｏｙａｌ　ｈｏｕｓｅ．` (12) — but the exact cut is the re-cutter's, not the reviewer's. ⚠️ **Also note this message carries `王家` TWICE** (`宮廷軍は王家のもの。` and `王家の人間のために`) and the current English renders the second only as `Ｓｅｒｖｉｎｇ　ｉｔ　ｉｓ　ｉｔｓ　ｄｕｔｙ．`, i.e. not as a `王家` at all; the re-cut should restore both |

Net effect on `chunk_005.txt`: **+18 bytes** (the three rows above the `王家` one), so 8,679 → 8,697
against its 8,192-byte slot; the `王家` row's cost is a re-flow and is measured at the re-cut. It is
487 over already; this does not change its feasibility, and it must not be traded against the
budget — the file needs the slot extension either way. `chunk_043.txt` gains 2 bytes back.

⚠️ **The village row above is the reason this table matters.** `assemble.py` reads only `tl/`, so a
divergence parked here is invisible to `check`, to `rowcheck` and to any duplicate sweep scoped to
`tl/` — which is exactly how glossary §27.2 came to say "`tl/battle/` is free of divergent duplicate
renderings" (true, and true only of `tl/`) while this row sat in `pending/`. **Sweep both trees and
say which one a hit is in** (`FLAGS.md` §X3).

| File | Bytes | Slot | Notes |
|---|---|---|---|
| `chunk_043.txt` | 11,181 | 8,192 | faithful translation, 1.86x. Needs a ~12 KB slot. **Ship this one.** |
| `chunk_043_abridged.txt` | 8,941 | 8,192 | evidence only, 1.41x, 13 sentences already deleted — still 749 over. Do not ship. |
| `chunk_005.txt` | 8,679 | 8,192 | faithful and fully compressed, 1.64x — 487 over. See `FLAGS.md` §2–4. Needs a slot extension, same as 43. **Also carries the §D1 artifact** (line 17), so it needs the dumper fix too. |
| **`chunk_017.txt`** | **5,857** | 8,192 | ⚠️ **NOT a budget park — 2,335 bytes UNDER its slot.** PR #12, merged at round 2 (squash `2e0790d`), reviewed line by line and glossary-integrated at §30. **This is finished translation waiting on a tooling fix, not unfinished work.** 1,144 JP → 2,472 EN = 2.16x against a 3.19x ceiling; 154 rows, widest 23, none at 24; no page over 4 text rows; `{FCC0}` untouched. It is here **only** because message line 19's item-grant tail carries the `FLAGS.md` §D1 dump artifact (`{FC70}{=00}入{=A300020000}`, where `入` is item id `0x93` plus the next tag's `0xFC` lead byte decoded as Shift-JIS) and `assemble.py`'s charset and tag-parity gates cannot both be satisfied — all four candidate encodings emit the **byte-identical** stream, so nothing is lost by waiting. **`FLAGS.md` §R** has the proof, the 24-occurrence / 10-chunk scope and the fix. |

| **`chunk_036.txt`** | **2,887** | 8,192 | ⚠️ **NOT a budget park — 5,305 bytes UNDER its slot, 31.4 % of budget spent.** PR #25, PARKED 2026-09-09 (squash `018af11`), reviewed line by line and glossary-integrated at **§44**. **This is finished translation waiting on a tooling fix, not unfinished work.** 986 JP → 1,213 EN against a 3.92× ceiling; widest run **22**, none at 23 or 24; **0 column problems**; no page over 4 text rows the source did not already exceed (45 and 33, both byte-identical to a pristine extraction, both already in `FLAGS.md` §D2); `{FCC0}` 2 → 2 untouched; `{FFFE}` 104 → 107, all three on body line 5. ⚠️ **The chunk is mostly NOT dialogue** — only **174 of 986** source characters are; the rest is a full-width MIPS assembly listing, English machine output and a garbage block, **all preserved byte-for-byte** (verified at review: 9 of 10 body lines byte-identical, 23 replaced runs on the tenth, every one Japanese on the source side, 1,154 characters carried through unchanged). It is here **only** because `assemble.py:validate_body` applies its charset whitelist to that preserved source: **38 illegal-char problems, not one on a translated run** (`＄`×14 `＞`×10 `＿`×4 `＃`×4 `｜`×3 `ケ` `あ` `「`), 0 tag-parity, 0 column, 0 byte. **The pristine chunk raises 193 — no chunk 36 file of any kind can pass `check` today.** ⚠️ **This is NOT §D1** — different function, no re-dump, no disc. **`FLAGS.md` §AF1** has the proof and the fix. |

The chunk 43 pair passes every other `assemble.py check` rule: tag parity, charset, 24 columns,
4 rows, line count and `{PAD}` identity. The byte budget is the only failure.

⚠️ **`chunk_036.txt` passes every rule but one, and the one is not about its text.** Tag parity,
columns, rows, line count, `{PAD}` identity and the byte budget are all green; the charset gate
fails on 38 characters of **source machine text the unit was required to preserve**. Unparking is
`git mv pending/chunk_036.txt tl/battle/chunk_036.txt` and nothing else — no re-translation, no
re-cut, no re-dump. See `FLAGS.md` §AF1.

`chunk_005.txt` passes tag parity, columns, line count and `{PAD}` identity, but has **two
further defects that are not translation problems** and would need handling even at budget:
its line 17 carries a dump artifact (`{FC70}{=00}逓{=20000E}`, where lines 14/16 have the clean
`{FC70}{=0062}{FC20}{=000E}` — the dumper decoded argument bytes ~~0x9276~~ **`0x92FC`** as text),
which trips the charset check; and its source line 10 contains a 7-row and a 5-row page, the first
pages over 4 rows encountered in any chunk worked so far.

⚠️ **Correction, 2026-09-08 (PR #12 review, `FLAGS.md` §R5):** the byte pair above read `0x9276`
and that is wrong — `逓` encodes to **`92 FC`**. The line number (17) and the diagnosis were both
right; only the value was mistyped. **That artifact is the same one that parks `chunk_017.txt`**,
and it is now enumerated project-wide: **24 occurrences across 10 chunks** (5, 15, 16, 17, 23, 27,
28, 29, 32, 39). One `riotbattle.tokenise` fix plus a re-dump clears all ten — see `FLAGS.md` §R.

---

## HEXMAP.BIN inspection (2026-08-05) — the space exists, in chunk 43 only

Measured directly on the retail `TACTICS/HEXMAP.BIN` (8,040,448 bytes, 46 × 0x2A800 chunks
plus a 0x8000 tail).

**Chunk 43 has 18,483 contiguous zero bytes immediately below its script slot:**
`chunk+0x207CD .. chunk+0x25000`, i.e. file `0x743FCD..0x748800`. Nothing sits between that
run and the script. The unit/deployment table at `+0x27000` is not involved — the slot would
grow *downward*, away from it.

Recommended new geometry for chunk 43: **start `chunk+0x23000` (sector 70), length 0x4000 =
16,384 bytes**, ending at the existing `+0x27000` boundary. Sector-aligned, entirely inside the
verified zero run, 5,203 bytes of slack over the 11,181-byte translation.

**This cannot be done globally.** Across the 44 script-bearing chunks the byte immediately
below the slot is free in only three of them (24, 28, 43); the other 41 carry a variable-length
structure that runs as late as `+0x24F15`, and every one of the 41 has a lone `0xFF` sentinel at
exactly `+0x24F18`. A uniform "script starts earlier" change buys **3 bytes** and corrupts 41
maps. The loader change must be conditional on the map index.

Rejected alternatives, for the record:

- **Chunks 44 and 45 are not map chunks** and cannot be borrowed. They have no TIM at any
  0x8800 boundary (all real map chunks have three, at +0, +0x8800, +0x11000) and their
  `+0x25000` regions hold non-script data — chunk 44's is 3,799 non-zero bytes.
- **The 32,768-byte file tail** (`0x7A3000..0x7AB000`) is zero but for one stray `0xFF`.
  Usable as a relocation target only if the loader can be given an arbitrary LBA, which is a
  larger change than the conditional offset above and buys nothing extra for this chunk.

Blocked on `KOUSEI.EXE` to locate the `0x25000` / sector-74 constant and, more importantly, to
size the destination RAM buffer — a 16 KB read into an 8 KB buffer is the one way this fix
fails silently.

## Separate finding: chunk 33 is missing from the dump

`tools/riotbattle.py::find_script_bounds` returns `None` unless `\xfc\x51` appears in the slot.
**Chunk 33 opens every message with `{FC50}` and never uses `{FC51}`**, so it is silently
dropped: `dumps/battle_dump.txt` holds 43 chunks (0–32, 34–43) but the file has **44**
script-bearing chunks.

Chunk 33 is 1,413 bytes of real dialogue — the sorceress guarding the 聖堂, the
`『知識の書』` (Book of Knowledge), the 魔術師 → ウィザード class-change trial, plus the
deployment restriction notice (`このマップでは、魔術師がリーダーのユニット以外は配置することは
できません。`). Headroom 6,779 bytes, so it is an easy chunk once it is dumped.

Fix: relax the detector to `\xfc\x51` **or** `\xfc\x50`, re-dump, and add chunk 33 to the queue.
