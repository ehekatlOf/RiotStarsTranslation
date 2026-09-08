## Run configuration — READ BEFORE BRANCHING
**The integration branch for this run is `claude/workflow-translation-iterate-uzlkns`, not
`main`.** The session that owns this run may only push there. It starts at the same commit as
`origin/main` (`dabdeae`), so the tree is identical. Everywhere `CLAUDE.md`, the `translate`
skill and the agent files say `main`, read `claude/workflow-translation-iterate-uzlkns`:

- translators: `git fetch origin claude/workflow-translation-iterate-uzlkns` and branch from it;
- PRs: `base = claude/workflow-translation-iterate-uzlkns`;
- reviewer: `git push origin integrate:claude/workflow-translation-iterate-uzlkns`.

The human fast-forwards `main` from this branch when the run is done. Nothing else changes.

## NEXT ACTION — always current, always a literal instruction
> **WAVE 3 IS RUNNING** in `session_0126mzDCZDEoby12pU5qXegc`. Glossary seeded (`19a0391`),
> four units dispatched. The coordinator closes the wave and then opens wave 4's session.
>
> If this line still says "wave 3 is running" and no agent is alive (`ListAgents`) and no PR has
> moved for an hour, the chain broke: reconcile open PRs against **In flight**, re-dispatch what
> is lost, finish the wave, then open wave 4 with `create_session` (BOTH `source_url` and
> `source_revision` = `claude/workflow-translation-iterate-uzlkns`).

## Last updated
2026-09-08 · by: **wave-3 reviewer** (integration commit for PR #9) ·
wave: **3 running — 1 of 4 merged, 3 in review** · queue: **fresh**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 16 | 44 | 0, 1, 2, 3, **4**, **6**, 7, **9**, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 11,351 | 43,161 | **26.3%** (was 20.1% at wave-2 start) |
| Script unique lines | 211 | 1,430 | `tl/script/batch_001–005.tsv` |
| Script message instances | 4,039 | 7,931 | **50.9%** |

`check`: **All checks passed** on the integration branch. Tightest banks after PR #9: **41 → 353
free (unchanged), 40 → 471, 5 → 3,381**, 2 → 7,505, 33 → 9,315. Bank 40 is spent (`FLAGS.md` §J2,
**superseded on these figures by §O1** — make the next bank-40 decision against **471, not 509**).
Wave 2's units touched banks 29/30/31 only, which remain roomy (25,589 / 35,119 / 34,827 free).

PR #9 edits already-shipped files, so no Done count above moves; what changed is byte figures.

## In flight — WAVE 3 (4 units, dispatched 2026-09-08)
Barrier: ✅ **MET 2026-09-08** — all four units have an open PR. Review order: **#9, #11, #10, #12**.

| Unit | Branch | Round | PR | State |
|---|---|---|---|---|
| corrections/audit-wave1 (**12** edits) | `tl/corrections-audit-wave1` | 1 | **[#9](https://github.com/ehekatlOf/RiotStarsTranslation/pull/9)** | ✅ **MERGED round 1** — squash `9965c64`; integration = the commit immediately after it, `integrate: corrections/audit-wave1 (PR #9)`. Reviewer acts next: **#11** |
| battle chunk 8 (B 2.32) | `tl/battle-008` | 1 | **[#11](https://github.com/ehekatlOf/RiotStarsTranslation/pull/11)** | ⚠️ **CHANGES round 1** — rework sent to the same translator; re-review after its push |
| battle chunk 13 (C 3.41) | `tl/battle-013` | 1 | **[#10](https://github.com/ehekatlOf/RiotStarsTranslation/pull/10)** | 🔍 **IN REVIEW** (reviewer 3 of 4) — runs alongside chunk 8's rework; still one reviewer at a time |
| battle chunk 17 (C 3.19) | `tl/battle-017` | 1 | **[#12](https://github.com/ehekatlOf/RiotStarsTranslation/pull/12)** | **PR open — PARK proposed** (dump artifact, not budget) — queued, reviewer 4 |

**PR #9 (corrections) — ✅ MERGED round 1, all eight gates green, findings were proposals only.**
Twelve edits across five files (the dispatch's eleven and HANDOFF's eleven were *different*
elevens; the unit applied the union and reported it). Every figure re-derived at review: chunk 1
**3,519** · chunk 2 **5,855** · chunk 3 **4,605** · chunk 34 **1,587 (−4)**; chunks 0 and 7
byte-for-byte untouched (identical blob hashes); `batch_004` **+38 B in each of 21 banks**, bank
40 **471** free, bank 41 unchanged at 353, no bank negative; **tag stream byte-identical to the
base on every line of all four chunks**. Two dispatch errors the unit caught were both correct
(the declined edit-5 re-flow, and `chunk_002` file **L14** not L15) — `FLAGS.md` §O8.

**✅ The live CLAUDE.md §3 violation is closed. `tl/battle/` now has ZERO divergent duplicate
renderings** — verified independently at review by positional pairing against the dump at two
granularities: 1 divergent before, 0 after. `村が襲われました。` is binding as
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．` (`glossary.md` **§27.2**), 13 dump
instances, **ten still untranslated** (chunks 5, 13, 15, 16 ×2, 17, 21, 23, 38, 39).
**Flag 6's deadline is discharged**: `tl/battle/chunk_013.txt` L8 (#10) and
`pending/chunk_017.txt` L21 (#12) were checked on their branches and both carry it byte-for-word.

**Integrated at review** (`glossary.md` §27, `FLAGS.md` §O): the 7 glossary rows, with the `愛用`
count corrected to **9 unique lines remaining, not 13**; a §4.3 correction to **§22.1**'s 火炎剣
gloss, which edit 2 superseded (§27.3); the §24.6 correction, which is **worse than reported** —
the spaced/unspaced conflation is one of *three* errors in that clause (§27.4); bank 40 recorded
at 471 in §O1, with §J1/§J2 marked superseded.

⚠️ **Wave-1 audit finding 7 is STILL OPEN and is carried forward, not discharged** — `FLAGS.md`
**§O7** now lists all five entries with their shipped renderings and corpus counts. Four and a
half are genuinely unfixed (`ヘビー`, `洞窟`/`赤い屋根`, bare `隊`, the `謹慎` noun forms; `さあ`
only partially, via §24.5/§24.6 with no table row — **16 battle + 10 script occurrences**). It has
survived two waves. **Whoever owns the next glossary integration writes these rows or records the
rejection in terms.**

**PR #10 (chunk 13) — key facts for the reviewer.** 5,417 / 8,192, **2,775 slack**; 132 rows,
widest 23, no page over 4 text rows. The binding `村が襲われました。` wording was verified against the
dump and applied (L7), byte-identical to chunk 7's break placement. Four lines re-flowed (L1 +1,
L4 −1, L7 +1, L8 −1), no `{FCC0}` added or removed anywhere.
- ⚠️ **My seed's column figure for `アーバイン様` was wrong and the translator caught it.**
  `Ｌｏｒｄ　Ｉｒｖｉｎｅ` is **11** columns and `Ｉｒｖｉｎｅ` **6**, not the seed's 12 and 7 —
  re-measured and confirmed. The reviewer should fix the §9 row at integration. The rendering
  itself is unchanged, so nothing translated is affected.
- **Two more §9 descriptions are wrong, same shape as the メルザリオ / ファリーナ corrections:**
  `ルクレール` and `レバーク` are **kingdoms**, not "a castle" and "a castle Maya has left" — each
  has a king (`我がルクレール国王`, `予は　レバーク王`), its own soldiers and a *castle*
  (`ルクレール城`, `レバーク城`), plus `誉れ高き国、ルクレールよ！` and `東南の王国、レバークを解放した`.
  **Neither rendering changes**; only the notes.
- **24 glossary additions** — the largest set of the wave. Three bind well beyond this unit and
  want deliberate ratification rather than inheritance: `レバーク` → `Ｌｅｖｅｒｋ` (a first-use
  promotion of a §9 row that offered two readings, **10 script occurrences** in a later scene —
  after this merges it is a §4.3 correction); `あら、` → `Ｍｙ，` (**16 further occurrences**, chosen
  only because §24.4 has spent `Ｏｈ` on おお / ほう / おや); `指揮下に入る` → `ｓｅｒｖｅ　ｕｎｄｅｒ`
  (**6 battle occurrences**, all squad members joining the player).
- Flag 8 asks the reviewer to sanity-check one speaker read: portrait 09 as Cress across L1/L2/L4.
  If that read is wrong her four pages need **re-registering, not re-cutting**.
- Flag 11 declares, rather than hides, that `さんざんいたぶった後` / `上玉` is a threat of sexual
  menace rendered at the source's own temperature.

**PR #11 (chunk 8) — key facts for the reviewer.** 7,437 / 8,192, **755 slack**; 20 lines, widest
row 23, no page over 4 text rows. All five wave-3 §9 seeds used **exactly as seeded**. Four lines
re-flowed (L4 −1, L5 +1, L9 −3, L15 −1); `{FCC0}` count unchanged on every line. 19 glossary rows
proposed.

⚠️ **Flag 3 is the finding that outlives this PR, and it is REAL — verified independently by the
coordinator against the source, not taken from the PR.** `translation_prompt.md` tells a translator
to add a `{FCC0}` page break in **four** places — line 248 ("You may add one when English overruns
the visible rows"), 361 ("If English needs a fifth line, insert a `{FCC0}`"), 373 ("Four rows is the
wall… add a `{FCC0}` rather than cutting sense") and 520, which asks the translator to *report*
"lines that needed an added `{FCC0}`". **Both gates reject it**: `tools/assemble.py:125-126` and
`tools/rowcheck.py:93-94` build the parity list as
`[t for t in re.findall(r'\{[^}]*\}', a) if t != '{FFFE}']` — only `{FFFE}` is exempt, so an added
`{FCC0}` fails as "tag stream changed". This translator's first draft added two, `check` failed on
exactly those lines, and it **re-cut to the source's page structure instead of touching the tools**
(CLAUDE.md §3) — the right call.

**Consequence, which is the part that matters:** every battle chunk is silently constrained to the
source's own page count, a tighter constraint than the prompt describes, and it changed two
speeches in this unit. This is a **documentation/tooling defect for a human** — `FLAGS.md` and the
prompt, not a translator's problem, and **not grounds for a finding against any PR**. The
run-configuration briefing already knew the escape does not exist; what is new is the measurement of
what it costs and that the prompt still asks for it in four places.

Also from PR #11, for the reviewer to rule on rather than inherit:
- **Flag 5 — the first genuine `Ｒｉｇｈｔ，` collision in one segment.** §24.3 fixes `よし、` →
  `Ｒｉｇｈｔ，` and §6 fixes `分かった` → `Ｒｉｇｈｔ，`; chunk 8 has **both in one segment**, which
  §25.3 says forces a split but names no reserve form for. The translator took
  `Ｒｉｇｈｔ，　ｕｎｄｅｒｓｔｏｏｄ．` (18 of 23 columns — the row has room if the reviewer prefers
  another form, and nothing re-flows). Whatever is decided belongs in §24.3 or §25.3.
- **Flag 9 — a source typo:** `大減棒` (L14) is almost certainly `大減俸`, a pay cut. Rendered for
  the meaning; a `FLAGS.md` note, not a translation change.
- **Flag 11 lists 12 segments that recur in chunks nobody has translated yet** — not §3 violations
  today, but whoever takes chunks 5, 16, 17, 19, 21, 24, 27 and 43 must match rather than reinvent.
- `ルート`'s §9 row is rendered by **both** chunk 8 and chunk 17 this wave — strike it once, at
  whichever merges second.

**PR #12 (chunk 17) — PARK proposed, and the reason is NOT budget.** The translation is complete
at **5,873 / 8,192 (2,319 slack)**, widest row 23, no page over 4 rows, all seven §9 seeds used
exactly as seeded (`クロスリー` promoted — this is the wave that first renders it). It is parked to
`pending/chunk_017.txt` because message **L19** carries the `FLAGS.md` §D1 dump artifact.

**Verified independently by the coordinator against `dumps/battle_dump.txt`, not taken from the
PR — the translator's mechanism and its scope figures are both exactly right.** The dump contains
`{FC70}{=00}入{=A300020000}`: that `入` is not text, it is **item id 0x93 followed by 0xFC, the lead
byte of the next `{FCA3}` tag**, decoded as Shift-JIS (`入` = 93 FC, and it is the *only* character
that encodes to those bytes). Chunk 39 L8 has the identical shape with id 0x8C → `向` (8C FC).
A full scan confirms **24 occurrences across 10 chunks**: `{FC70}` in **5, 16, 17, 23, 39** and
`{FCA8}` in **15, 27, 28, 29, 32**.

**Why it cannot ship to `tl/`:** the two gates are unsatisfiable together. Left as dumped, the file
contains a Japanese character and fails the charset gate; re-tokenised into the true byte run, the
tag stream changes and fails tag parity (`assemble.py:125`). All candidate forms produce
byte-identical game output, so nothing is lost by parking. Chunk 17 is the **first chunk where this
artifact is the only blocker** — the others are also budget-blocked or untranslated.

**For a human:** fixing the dumper unblocks 10 chunks and unparks this one with a `git mv` plus one
0-byte re-tokenisation. Needs `original/`. This is `FLAGS.md` §D1 and Blocked item 6.

Reviewer also to rule on: `Ｃａｎｙｏｎ` vs `Ｇｏｒｇｅ` for `バージェス峡谷` (reversible at no cost),
and whether chunk 4's dying girl is Femina. ⚠️ Its gate-6 comparison against `chunk_034.txt` will
show a divergence on the village line **that resolves when PR #9 merges** — #9 is first in the
review order for that reason.

**PR #11 (chunk 8) — CHANGES round 1, 2026-09-08.** All eight gates pass and **every figure the
PR claimed is true when re-derived**; gate 6 was run as positional pairing at four granularities,
extended across PR #10's and #12's branches — **624 page keys, zero divergent renderings anywhere**.
The reviewer records that the translator was **right on every contested measurement it made**,
including the `{FCC0}` conflict, the 26-column `ｒｅｔｒｅａｔ　ａｎｄ　ｓｕｐｐｌｙ　ｒｏｕｔｅｓ．`, and the
glossary's 18-column figure for `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` (it is **17** — a §4.3 correction the
integration commit owes). What holds the merge is **one reading defect the gates cannot see**:
- **Finding 1 (blocking):** L10's `{FCC0}` clears the box **between `ｔｈｅ` and `ｆｏｒｅｓｔ`**. Of the
  10 mid-sentence English page breaks in `tl/`, nine are inherited; this is the only one where the
  source's break follows a sentence-final `。` and the English carries a phrase across it, and the
  only one splitting a determiner from its head noun. Measured fix costs ~2 bytes of 755.
- **Finding 2:** L4's `南から、帝国軍よ！` reverses source clause order, unforced and unflagged;
  source order is the same 33 characters in the same two rows. Restore **or** flag as a fourth
  step-6 reorder — the translator picks, with reasons.
- **Finding 3 (record only):** Flag 2's L9 breakdown is +2/−5, not +1/−4 (net −3 is right).

**Rulings the reviewer made rather than deferring** (this is the §25.3 gap being closed properly):
`Ｒｉｇｈｔ，　ｕｎｄｅｒｓｔｏｏｄ．` **stands** for chunk 8 — chunk 8 has no `了解`, so §25.3's test is met.
But **chunk 19 contains both**, so the reserve is fixed **now, before a unit needs it**: `了解` keeps
`Ｕｎｄｅｒｓｔｏｏｄ`, a co-occurring `わかった` takes **`Ａｇｒｅｅｄ．`** (7 columns, verified free —
`Ｉ　ｓｅｅ．` and `Ｖｅｒｙ　ｗｅｌｌ` are spent, `Ｅｘａｃｔｌｙ．` reserved). Goes into §28.
`大減棒` ruled a source typo (hapax; `減俸` is the word) — rendering stands, `FLAGS.md` note.
Two findings **withdrawn after measuring** and recorded so they are not re-raised: rows ending on
`ｔｈｅ` (29 shipped instances) and on a lone `Ｉ` (1) are settled house practice.

**No integration commit** — glossary §28, the FLAGS entries and the two §4.3 corrections are drafted
and held until the rework lands and the same reviewer re-reviews.

⚠️ **Glossary section numbering — two reviewers now hold drafts.** `glossary.md` ends at **§27**
(PR #9). PR #11's reviewer has **§28 drafted but unpushed**, held until chunk 8's rework lands. PR
#10's reviewer is told to take **the next free number at the moment it commits** — so if #10
integrates first it takes §28 and PR #11's held draft becomes §29 on its round-2 pass. Whichever
commits second must re-read the file rather than trusting a number reserved earlier.

**No script batch this wave.** Four units is CLAUDE.md §4 step 3's ceiling and the corrections
unit takes the fourth slot. A vetted script range for wave 4 is in **Next up**.

## Next up

**Wave 3's unit specs live in the dispatch messages and in `audits/`** — enough to re-dispatch any
unit from here:

- **corrections/audit-wave1** — apply the wave-1 audit's measured edits to already-shipped files.
  `audits/wave1-reading-review.md` §"table of 8" (**file** line numbers) + `audits/wave-1-audit.md`
  items 3–5 (**message** line numbers — the two docs number differently and mean the same lines),
  plus the §3 violation in that doc's §9. **Eleven** translated-line edits: `batch_004` L12/L17/
  L29/L42, `chunk_003` L6 (×2) and L17, `chunk_002` L15, `chunk_001` L2 and msg-L14, `chunk_034` L8.
  ⚠️ The audit's proposed `しかし` → `Ｂｕｔ` is **superseded** by §23.3 (`Ｂｕｔ` is でも's) → use
  `Ｈｏｗｅｖｅｒ，` and re-measure. ⚠️ `chunk_000.txt` (27 B slack) is **out of scope**.
- **battle chunks 8 / 13 / 17** — `python3 tools/queue.py battle` for figures; seeds in glossary §9.

**Wave 4 candidates**, in this order:
1. Any wave-3 unit that parked.
2. Battle chunks **15 (D 6.13), 18 (D 6.28), 19 (B 1.94)** — next in chapter order.
3. **One script batch — ALREADY VETTED by the wave-3 coordinator, take one of these:**

   | `queue.py script` batch | Lines | Banks | Verdict |
   |---|---|---|---|
   | **batch 1** — 318, 421–469 | 50 / 52 inst, 3,056 JP | 2, 3 | ✅ **CLEAN** — recruitment & shop dialogue |
   | **batch 2** — 319, 335, 599–646 | 50 / 53 inst, 1,332 JP | 12–15 | ✅ **CLEAN** — shop lines, roomy banks |
   | ~~batch 3~~ — 320, 1073–1121 | 50 / 52 inst | 31–34 | ⛔ **28 of 50 are DEBUG SCAFFOLDING** — a BGM sound-test menu (`５０：新曲１`, `１６：バトル（ザコ戦）`) and a flag-manipulation screen (`どのフラグを操作しますか？`). **Do not dispatch.** |
   | **batch 4** — 326–328, 470–516 | 50 / 53 inst, 1,638 JP | 4, 5, 7 | ✅ **CLEAN** — ノロ village + town descriptions. ⚠️ bank 5 has only 3,419 free |

   **Batch 2 is the pick** — cleanest, roomiest banks, lowest JP count.
   ⚠️ **Method note, or the vet silently passes everything:** `script_unique.txt` lines are
   `<instance count>\t<text>`, so the scaffolding regex `フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must be
   matched against the **text field**, not the raw line — anchored `^[０-９]{2}：` never fires on the
   raw line and batch 3 scores 18/50 instead of its true 28/50.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle, **24 dispatchable chunks** after wave 2 (`queue.py` reports 26 open — the other two are
tier-A 16 and 32, blocked below), in chapter order (tier, budget ratio):
8 (B 2.32), 13 (C 3.41), 15 (D 6.13), 17 (C 3.19), 18 (D 6.28), 19 (B 1.94), 20 (D 4.75),
21 (D 4.28), 22 (D 4.59), 23 (C 2.80), 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 27 (D 5.54),
28 (D 4.76), 29 (D 6.04), 30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37),
39 (D 6.20), 41 (E 6.54), 42 (D 5.46).

Script: 1,219 unique lines / ~4,606 instances untranslated. The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is spent at 509 free**
— lines 185–225 stay parked until it is repointed. After that, the 1-instance story text in the
roomy banks (518–1,413, ~53,000 JP chars) is what remains dispatchable.

## Blocked — needs a human
1. **Tier A battle chunks 5, 16, 32, 43.** Measured budget ratios 1.53 / 1.59 / 1.61 / 1.23, all
   below the **1.64× floor measured in FLAGS §B2**; no faithful translation fits 8,192 bytes.
   5 and 43 are translated and parked in `pending/`. Fix: the engine patch in
   `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script
   buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends settling
   KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (FLAGS §F2). Translating everything that remains needs
   +30,534 bytes in bank 41 (353 free), +20,924 in bank 40 (1,771), +14,720 in bank 5 (4,681),
   +12,798 in bank 2 (8,805) and +11,492 in bank 33 (10,615) — about **66 KB short**. Every
   other bank has room. 376 unique lines / 3,001 instances are therefore unshippable until a
   MAIN1.EXE repoint or bank-spill scheme exists.

   **The two worst cases are whole late chapters, and they are the clearest statement of the
   problem yet:** unique lines **1160–1354** (195 lines, 4,836 JP chars) are resident in **bank 40
   alone**, which has 1,771 bytes free and would need about 19,000; unique lines **1355–1387**
   (33 lines, **14,607 JP chars**) are resident in **bank 41 alone**, which has 353 bytes free and
   would need about 29,000. Neither chapter can be shipped even partially in a way worth playing.

   **Policy this run, with the numbers that decide it:** bank 40's spendable budget goes to the
   21-instance item-description table (~40 lines ≈ 840 instances) rather than to bank 40's own
   story text (~25 of 195 lines ≈ 25 instances, leaving that chapter 90% Japanese). A complete,
   coherent table beats a tenth of a chapter. Reversible — it is a choice, not a fact — but the
   arithmetic is not close.
3. **Main-script box not yet widened** (MAIN1.EXE side). Translate to 24 columns anyway;
   `riotfont.py rewrap` re-flows later.
4. **In-game checks**: FLAGS §D2/§D3 (pages over 4 rows), §D4 (is line 1234 reachable), §F6
   (description window 3 or 4 rows), §C4 (`{FFEC}` variant widths), `findings.md` menus and
   name-entry first test.
   ⭐ **The highest-value one is now `FLAGS.md` §L2 / `findings.md` §24 — do this one first.**
   Eight lines in `battle_dump.txt` carry **no `{FC50}`/`{FC51}` at all** and still exceed four
   text rows: chunk 6 L9 (15 rows) and L21 (11, tags are only `{FFFE}`/`{FFFF}`), chunk 7 L23/L24
   (5 and 6, already shipped — this is §D3), chunk 30 L23 (8), **chunk 32 L31 (59)**, chunk 37 L14
   (8), chunk 42 L11 (16). A 59-row page cannot exist, so the prediction is that these are **pools
   of independently-selected strings**, with `{FC03}` (32 occurrences, battle-only, zero in the
   script dump) as the selector. **One visit to the chapter 5 church map and chapter 6 settles it,
   and settles §D3 with it.** If the prediction holds, `rowcheck`'s `> 4 rows` warning is
   meaningless on all eight and a translator may re-flow freely inside such a line — but must
   never merge two entries. If it fails, chunk 7 L24 is already broken in shipped work.
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. **Chunk 5 dump artifact** (FLAGS §D1): dumper fix plus re-dump; needs `original/`.

## Decisions this run
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured, not the skill's assumed 2.0×.
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not bank 40's own
  story text (~40 lines ≈ 840 instances vs ~25 of 195 lines ≈ 25 instances). Reversible.
- 2026-09-08: **wave 3 seeds the glossary BEFORE dispatch** (`19a0391`, 10 §9 rows). Wave 2's three
  round-1 CHANGES all came from the glossary moving under a draft mid-wave.

**Wave-2 rulings are no longer duplicated here** — they are written into their homes and that is
where they bind: `glossary.md` §23–§26 (`しかし`→`Ｈｏｗｅｖｅｒ，`, `クリミア` is a person, 将軍→General,
`様`≠さん, 弓使い→bowman), `FLAGS.md` §K–§N (§I1/§N2 quoted-token capitalisation, §J1's corrected
arithmetic), `findings.md` §24 (`{FC03}`), `translator.md` `06353c7` (the null gate-6 grep).

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines / 4,013 instances (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle **16/44 (26.3%)**; script **211 lines / 4,039 instances (50.9%)** |

**Wave 2 detail.** Four merged, none parked, none past round 2, run as a full three-role split
(translator / reviewer subagents) — the first wave with independent review.
`#6` chunk 4 — 3,849 / 8,192, slack 4,343, round 1, **zero findings**; the project's first
zero-re-flow unit (tag stream byte-identical on all 25 lines). `#7` chunk 6 — 5,899 / 8,192,
slack 2,293, round 2. `#5` chunk 9 — 3,973 / 8,192, slack 4,219, round 2. `#8` script batch 005 —
26 lines / 26 instances, 4,040 B into banks 29/30/31, round 2.
Glossary grew by four sections (§23–§26), `FLAGS.md` by four (§K, §L, §M, §N), `findings.md` by
one (§24, the `{FC03}` investigation). **Three of the four round-1 CHANGES were caused by the
glossary moving under a draft mid-wave** — a merged unit's integration commit adding rulings that
name a sibling unit's lines. Wave 3 should seed the glossary before dispatching, not after.
**Twice a translator overturned a reviewer's proposed replacement on evidence**, and both times the
reviewer withdrew its finding: chunk 6's `Ｎｏｗ，` over `Ｃｏｍｅ　ｏｎ，`, and chunk 9's three-row
`Ｈｏｗｅｖｅｒ，` split over a two-row form that ended a row on the article `ａ`.
An **independent post-merge audit of wave 1's four self-reviewed units** also ran this wave
(`audits/`): the units stand as merged, with eight minor edits queued above.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
