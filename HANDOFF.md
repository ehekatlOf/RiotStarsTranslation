## Run configuration — READ BEFORE BRANCHING
**The integration branch for this run is `claude/workflow-translation-iterate-uzlkns`, not `main`.**
Everywhere `CLAUDE.md`, the `translate` skill and the agent files say `main`, read this branch:
translators branch from it, PRs use it as base, reviewer integration pushes go to
`integrate:claude/workflow-translation-iterate-uzlkns`. The human fast-forwards `main` when the run
is done.

⚠️ **A fresh container clones SHALLOW and carries a STALE local ref of that branch** (wave-1 state,
*no merge base* with origin). It starts detached at the right commit, so `git checkout <branch>`
moves you **backwards** and `git pull --ff-only` then aborts. **All four wave-4 reviewers hit this.**
Fix: `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns`, verify with
`git log -1`. No work is lost; the stale local ref is a container artifact.

## NEXT ACTION — always current, always a literal instruction
> **WAVE 7 IS RUNNING — REVIEWING, 1 of 4 decided.** Coordinator: `session_01N1VxX55Vw79fxNr6nTELcs`.
> Seeds pushed (`f62dadb`). Units: **battle 30 ✅ MERGED, 31, 36 (park), script `batch_009`**.
> **Next reviewer: PR #26, battle chunk 31.** Then #25 (chunk 36 park), then #28 (script batch_009).
> `git pull --ff-only` before dispatching it — PR #27's integration commit is on the branch.
>
> If this line still says "running" and `ListAgents` shows nothing alive: the wave died mid-flight.
> Reconcile open PRs (`git ls-remote --heads origin 'tl/*'`) against In flight, re-dispatch what is
> missing, and carry on from **Review** below. Do **not** restart finished units.
>
> When the wave closes, the close commit is `handoff: wave 7 closed` and the next act is to
> **OPEN WAVE 8'S SESSION** in the same turn (`create_session`, BOTH `source_url` and
> `source_revision` — SKILL.md §6a).

## Last updated
2026-09-09 · by: **wave-7 reviewer, PR #27 integration** ·
wave: **7 REVIEWING — 1 of 4 decided (chunk 30 MERGED); 31, 36, script batch_009 still to review** ·
queue: **fresh; wave-7 batch re-verified, see Decisions**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **27** | 44 | 0–4, 6–14, 18–22, 24, 25, 26, **30**, 33, 34, 35, 40 |
| Battle JP characters | **23,356** | 43,161 | **54.1%** (was 51.0% before chunk 30) |
| Script unique lines | **358** | 1,430 | `tl/script/batch_001–008.tsv` |
| Script message instances | **4,209** | 7,931 | **53.1%** |

`check`: **All checks passed** at `2bac521`. ⚠️ **Tightest banks: 41 → 353, 40 → 447, 5 → 2,007
(was 3,357 — batch 008 spent 1,350), 2 → 3,365**, 3 → 8,113, 33 → 9,291. Parked and translated:
chunks **5, 43** (tier-A budget) and **17** (dump artifact). ⭐ **The dumper is STILL unfixed** —
re-verified at the wave-6 close: `grep -n "FC70\|FCA8" tools/riotbattle.py` returns nothing.

## In flight
| Unit | Branch / file | PR | State |
|---|---|---|---|
| ~~battle chunk 30~~ | `tl/battle/chunk_030.txt` | **#27** | ✅ **MERGED 2026-09-09 — squash `9548e73`; integration commit `integrate: chunk 030 — glossary §43, FLAGS §AE, handoff`.** 7,615 / 8,192, **slack 577**; 183 rows, widest 23, none at 24; both over-4 pages verified inherited against a pristine extraction; `{FFFE}` changed on 7 lines, all itemised. All 8 gates passed, no findings. Glossary **§43** (12 terms + 4 rulings), FLAGS **§AE** |
| battle chunk 31 | `tl/battle-031` → `tl/battle/chunk_031.txt` | **#26** | **delivered — awaiting reviewer** (5,355 / 8,192, slack 2,837) |
| battle chunk 36 | `tl/battle-036` → **`pending/chunk_036.txt`** | **#25** | **PARK proposed — awaiting reviewer** |
| script batch 009 | `tl/script-009` → `tl/script/batch_009.tsv` | **#28** | **delivered — awaiting reviewer** (+6,026 bytes, 2.034×) |

✅ **WAVE BARRIER MET — 4 of 4 PRs open: #27 chunk 30, #26 chunk 31, #25 chunk 36 (park), #28
script batch_009.** Reviewing now, ONE reviewer at a time, foreground, in unit order 30 → 31 → 36
→ script. Push HANDOFF before each reviewer; `git pull --ff-only` after each (it pushes an
integration commit). Never two reviewers at once. A translator still working is not a
failure; wave-6 translators took 37–60 min. A translator that returned/died with no PR gets ONE
fresh re-dispatch (two max), then the unit parks and the barrier closes on the rest.

**PR #25 (chunk 36) is a PARK, and its reason is a NEW tooling blocker — verified by this
coordinator, not taken on trust.** 2,887 / 8,192 bytes, slack 5,305; translation finished, faithful
and format-clean; 0 column problems. It cannot enter `tl/` because **`assemble.py:validate_body`
applies its charset whitelist to preserved SOURCE machine text**: chunk 36 is largely a full-width
MIPS listing, and with `jp_ok=False` (the mode for translated files) **38 characters are rejected —
`＞`×10 `＄`×14 `＿`×4 `｜`×3 `＃`×4 `ケ` `あ` `「` — and NOT ONE of them is on a translated run.**
Re-measured here: pristine chunk 36 raises **193** problems; the delivered file raises **38** with
`jp_ok=False` and **0** with `jp_ok=True`. ⚠️ **This is NOT the §D1 dumper artifact** — §D1 is
`{FC70}`/`{FCA8}` tokenisation; this is the charset whitelist, a different fix in a different
function. Reviewer: record it as its own `FLAGS.md` entry, a Blocked row and a `pending/README.md`
row. Fix is one function in `assemble.py` (skip charset on runs byte-identical to the dump; merely
widening `ALLOWED` is **insufficient** — the garbage block contains kana). **Needs no disc, no EXE
and no dumper change, and after it unparking is a `git mv` and nothing else.**

## Next up — WAVE 7 (in flight; figures RE-VERIFIED by this coordinator)
**Battle 30** (tier B, 1,358 JP, headroom 3,897, ratio **2.43** — tightest, expect a re-cut pass),
**31** (tier C, 1,051 JP, ratio **3.46**), **36** (tier C, 986 JP, ratio **3.92** — ⚠️ **mostly a
full-width MIPS assembly listing that must survive VERBATIM**; only ~154 JP chars are dialogue).

**Script `tl/script/batch_009.tsv` = unique 534–583**, contiguous, **50 lines / 50 instances /
2,913 JP chars**, **0/50 already translated, 0/50 scaffolding** — all re-measured, all exact.
Banks **7, 8, 9, 10, 11, 12 only**; after: b7 **12,978**, b8 **10,621**, b9 **12,150**,
b10 **33,597**, b11 **39,308**, b12 **8,541**. **None of the four tight banks (41, 40, 5, 2) is
touched.** Scene: town troop-recruitment and NPC dialogue across several courts.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **15 open chunks.** ⚠️ **6 carry the §D1 dump artifact and will park exactly as chunk 17 did
— 15, 23, 27, 28, 29, 39**; **16 and 32 are tier-A blocked**. So only **7 are dispatchable**, in
chapter order: **30, 31, 36, 37, 38, 41, 42** — about **two more waves**, and then battle work stops
until a human fixes the dumper or the slot budget.

Script: **1,072 unique lines / 3,722 instances** untranslated. ⚠️ **Bank capacity, not the queue, is
now the binding constraint** — only queue position 6 fits. ⚠️ **Chunk 37 (a later wave) inherits
`FLAGS.md` §Y6**: Cress's gender is fixed nowhere and rendered nowhere in `tl/`.

## Blocked — needs a human
0. 🔧 **THE `riotbattle.tokenise` DUMP ARTIFACT — the highest-leverage item here.** `FLAGS.md`
   **§D1, §R**. The dumper prefers a Shift-JIS text run over a control tag whenever an argument byte
   is a valid lead byte, so an item id plus the *next tag's* lead byte decodes as a kanji.
   **24 occurrences across 10 chunks** — `{FC70}` in 5, 16, 17, 23, 39 and `{FCA8}` in 15, 27, 28,
   29, 32 — and each makes `check` unsatisfiable for that chunk: the dump form passes tag parity and
   fails charset; every re-tokenised form does the reverse. **Chunk 17 is finished, faithful,
   format-clean and 2,335 bytes UNDER its slot, parked for this reason alone.** Fix: teach
   `tokenise` the argument lengths of `{FC70}` and `{FCA8}`, then `assemble.py refresh`; chunk 17
   unparks with a `git mv` plus a **0-byte** re-tokenisation of one tail. ⚠️ **Needs no disc, no EXE
   and no emulator — unlike everything else here — and it unblocks ten chunks at once.**
1. **Tier A battle chunks 5, 16, 32, 43.** Ratios 1.53 / 1.59 / 1.61 / 1.23, all below the **1.64×
   floor** (FLAGS §B2); no faithful translation fits 8,192 bytes. 5 and 43 are translated and parked.
   Fix: the engine patch in `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate
   the 8 KB RAM script buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends
   settling KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (`FLAGS.md` §F2, figures refreshed §Z6). About **66 KB short**:
   bank 41 needs +30,534 with **353** free, bank 40 +20,924 with **447**, bank 5 +14,720 with
   **3,357**, bank 2 +12,798 with **3,365**, bank 33 +11,492 with **9,291**. **376 unique lines /
   3,001 instances are unshippable** until a MAIN1.EXE repoint or bank-spill scheme exists. Worst
   cases: unique 1160–1354 live in **bank 40 alone**, 1355–1387 in **bank 41 alone** — neither can
   be shipped even partially in a way worth playing. **Policy this run:** bank 40's spendable budget
   goes to the 21-instance item table (~840 instances), not its own story text (~25 instances).
   Reversible — but the arithmetic is not close.
3. **Main-script box not yet widened** (MAIN1.EXE). Translate to 24 columns anyway;
   `riotfont.py rewrap` re-flows later.
4. **In-game checks** — `FLAGS.md` §D2/§D3, §D4, §F6, `findings.md` menus and name-entry. Two are
   worth doing first, and they share one visit:
   ⭐ **`FLAGS.md` §L2 / `findings.md` §24.** Eight lines carry **no `{FC50}`/`{FC51}` at all** yet
   exceed four text rows — chunk 6 L9 (15) and L21 (11), chunk 7 L23/L24 (5 and 6, already shipped),
   chunk 30 L23 (8), **chunk 32 L31 (59)**, chunk 37 L14 (8), chunk 42 L11 (16). A 59-row page
   cannot exist, so the prediction is **pools of independently-selected strings** with `{FC03}` as
   selector. **One visit to the chapter 5 church map and chapter 6 settles it, and §D3 with it.**
   ⭐ **`FLAGS.md` §C4 + §Y1 — one shop visit settles both.** ⚠️ **§C4's scope was OVERSTATED and is
   corrected (PR #20):** `assemble.py:validate_body` substitutes `{FFEC}{=00}{=00}` with **7
   placeholder characters** and `rowcheck` does the same via `SCRIPT_NAME`, so **the player-name
   insert IS counted, at 7 columns** — that fix is DONE. Only the **other** insert forms
   (`{=00}{=01}` price, `{=00}{=03}`/`{=00}{=04}` item and unit names) are gate-blind: 12 rows in
   `batch_006` and 6 in `batch_007`, each **bounded** at insert+8 against the Japanese's insert+0..+7.
   A bound, not a measurement. **Also look at what `{FC00}` actually renders as, and whether it is
   padded to 7 characters** — **49 rows across 15 files** now put a character straight after it
   (`，` mostly, plus `．` `？` `！` `　` and, new in chunk 22, `’ｓ`). Enter the **longest legal
   7-character name** and visit a shop with the game's longest item name.
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run `python3 tools/assemble.py
   all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. 📄 **`SKILL.md` §3 edit (small):** scratch-file namespacing must bind **every** role, not just
   translators. A **reviewer's** script was overwritten mid-task in wave 4 and caught only because
   the output was visibly the wrong unit's data — that is gate evidence underpinning a merge
   decision. Add: every agent namespaces every scratch file (`r015_dupes.py`), and no agent trusts a
   scratch script it did not write in the same turn.
7. 🖥️ **The three `『』` UI screen labels need one look at the Formation screen.** `FLAGS.md` §Z1.
   `batch_007.tsv` unique 431/437 ship `“Ｆｏｒｍａｔｉｏｎ”`, `“Ｃｈａｒａｃｔｅｒ　Ｇｒｏｗｔｈ”` and
   `“Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ”` as **instructions to find those menus on screen** — but **the menu
   strings are in NEITHER dump**, so no label here can be checked against what the screen shows, and
   if the menus stay Japanese the instruction misdirects the player. Nothing is defective: the widths
   are right and `『…』` → `“…”` follows glossary §12. **Open Formation in-game and read the three
   entries.** If still Japanese, either re-cut the labels to describe rather than name the menus, or
   translate the menu strings too. Glossary §9's UI-label row **stays live** until settled.

## Decisions this run
**Rulings live in their homes**: `glossary.md` §23–**§43**, `FLAGS.md` §K–**§AE**, `findings.md` §24,
`pending/README.md`. ⚠️ **Section numbers are taken by READING both files at commit time.**
- 2026-09-09 (wave 7, PR #27 review): **`ああ` splits on REGISTER** — §6's `Ｙｅａｈ` is conditioned
  to casual, contraction-taking speakers; Rimul's assent is `Ｉ　ｄｏ．` (glossary §43.1; 13 of 13
  shipped `Ｙｅａｈ` verified casual, the §41.4 precedent extended to a second interjection).
  **`争い` → `ｓｔｒｉｆｅ` is §38's FIXED entry, `ｃｏｎｆｌｉｃｔ` refused** (§43.4) — and
  **`batch_008.tsv` L55's `ｗａｒ` diverges from it and owes a re-cut** (`FLAGS.md` §AE2; 争い and
  戦乱 **co-occur in bank 3**, so §25.3 FAILS for that pair). **Sentence-final `ブヒ` takes §5's
  ノロ mechanism**, sentence-initial keeps §19.1's capital (§43.3). ⚠️ **Two reach counts in the PR
  were wrong and BOTH came from counting the battle dump only**: `クロイツェル` is **not** a hapax
  (bank 41 / unique 1391) so its §9 row **stays live** (§43.5), and `どうかご無事で` does **not**
  recur in chunk 23 (§43.2). **Widths were exact everywhere** — §AC3's discipline has reached
  widths but not yet reaches. **Gate 6 needs a positive control and a planted violation every
  time**: this reviewer's first checker keyed on tag-bearing messages, matched nothing, and read as
  a clean pass (`FLAGS.md` §AE7).
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×**; **bank 40's budget goes to the 21-instance
  item table**, not its story text; **seed the glossary BEFORE dispatching**; **a parked unit still
  gets the full reading review**; **the `queue.py` batch POSITION is not the filename**.
- 2026-09-09 (wave 6): **a term is "in the glossary" only if a row FIXES AN ENGLISH FORM**; findings
  are **proposals to verify in BOTH directions** (5 coordinator figures wrong, 3 reviewer refusals
  upheld, 2 agent claims refuted); **mechanical term search has 4 blind spots** (mixed script,
  maximal runs, katakana register transforms, kana variants — `FLAGS.md` §Y2/§AC1); **a glossary
  row's Alt column records REJECTED options, not a menu**; **measure every width with `len()`**
  (§AC3 — the only systematic error three waves running); **`{FCC0}` is forbidden by
  `assemble.py:tag_parity`, NOT by `rowcheck.py`**; **serialised review is worth its wall-clock**.
- 2026-09-09 (wave 7): ⚠️ **THE WAVE-7 SEED'S LABEL WAS WRONG AND ITS FIGURES WERE RIGHT.** The unit
  was handed over as "`queue.py script` **position 6**". It is **not**: position 6 is unique 340–342
  + 702–748 (banks 18–21). Unique **534–583 is a hand-cut contiguous range straddling queue batches
  3 and 4** and must be named by its line list, never by a queue position. **Every figure attached
  to it re-measured EXACT** (50/50/2,913, six banks, all six after-figures, 0 done, 0 scaffolding).
- 2026-09-09 (wave 7): ⚠️ **"Positions 1–5 are ALL bank-negative" does NOT reproduce** — all six
  current positions fit. The seed chunked *all* untranslated lines in order; `queue.py`'s allocator
  reports the *feasible* set, and by construction everything in it fits. **Two different questions;
  say which one a bank claim answers.** 534–583 was kept anyway: contiguous, one scene, and it
  touches none of the four tight banks.
- 2026-09-09 (wave 7): **8 of the batch's 50 rows carry a sibling binding, not the 1 handed over.**
  535↔505, 578↔984, 579↔985, 581↔988 are **already SHIPPED** (reuse the visible English exactly);
  556↔557 and 582↔583 are **in-batch pairs**; 582/583↔691 is outside and untranslated. ⚠️ **The
  bound rows' TAGS DIFFER** — match the visible English, keep your own tags, or tag parity breaks.
- 2026-09-09 (wave 7): ⚠️ **A LIVE §25.3 COLLISION IS INSIDE THIS BATCH.** `Ｉ　ｓｅｅ．` already
  renders `そうか`, `そうですか`, `なるほど` and `そうかい`. This batch puts **`そうか` (550, 553, 554)
  AND `なるほど` (556, 557) BOTH IN BANK 8** — §25.3's "no chunk and no bank holds two" fails
  outright, exactly as §42.4 predicted. It is the batch-009 translator's ruling to make and the
  reviewer's to test; `Ｅｘａｃｔｌｙ．` stays reserved for `そのとおり`/`そうそう`.

- 2026-09-09 (wave 7): ⚠️ **A COORDINATOR DISPATCH INSTRUCTION WAS IMPOSSIBLE, AND THE TRANSLATOR
  WAS RIGHT TO REFUSE IT.** I told chunk 31 to reproduce its two Latin incantations "EXACTLY,
  character for character". **`・` (U+30FB) is not in `assemble.py:ALLOWED` and is not in the
  full-width Latin/digit ranges, so it is rejected outright** — verified here. The instruction was
  unsatisfiable as written. The translator mapped the three `・` by existing rules instead
  (separator → `　` per §1's `ゼファー・クリッペン`; trailing `・・` → `．．` per §3.1) and kept every
  letter and its case byte-identical. **Third wave running that an agent has correctly refused a
  coordinator instruction on measurement.** ⚠️ The same trap applies to chunk 36's preserved machine
  text and to any future unit carrying source Latin — **`・` can never be "preserved verbatim".**
- 2026-09-09 (wave 7): **two glossary figures corrected by measurement, both confirmed here.**
  (a) **`ｇｅｍｓｔｏｎｅ` is 8 columns and `ｇｅｍｓｔｏｎｅｓ` 9** — §32.1 states "9 / 10" and §33.5
  states "9"; both are one too high. No rendering changes; the form is 1 column *cheaper* than the
  glossary believes. (b) **§32.7's `ふふ` census counts SUBSTRINGS, not laughs** — chunk 31 has
  **3** ふ-runs (`ふふふ`, `ふふふふ`, `ふふふふふ`), whose non-overlapping `ふふ` substring count is
  **5**, which is the "31 ×5" the row records. The §35.2 shape in a new place.

- 2026-09-09 (wave 7): **the kana/mixed-script blind spot bit THREE times in one chunk.** The
  coordinator's brief caught `うらみ`/`恨み`; chunk 30's translator then found the same shape at
  `まちがいない`/`間違いありません` and `じゃま`/`邪魔だて` by searching **both** scripts unprompted.
  §Y2/§AC1's rule is not "check the one term you were warned about" — it is **search both scripts
  for every term**.
- 2026-09-09 (wave 7): ⚠️ **`石版` → `ｔａｂｌｅｔ` MUST STAY LIVE in §9 at every merge this wave.**
  Reach re-measured by chunk 30's translator: **5 battle (chunks 30, 36) + 25 script instances
  across 21 banks**, including unique 574/576. Chunk 36 being PARKED does not discharge it —
  script 569/571 still render it. `クロイツェル` and `遠征軍` ARE exhausted by chunk 30 and may be
  struck outright.

- 2026-09-09 (wave 7): ⚠️ **A FOURTH COORDINATOR ERROR, caught by `batch_009` and verified here.**
  My dispatch told it `Ｉ　ｓｅｅ．` renders "`そうかい` (batch 008)". **Both halves are wrong**:
  `そうかい` is in **`batch_007.tsv:27`** (§38.2, banks 2/3), and **`batch_008` L64/L67 render
  `そうか。`**. The correction *strengthens* the §25.3 ruling rather than weakening it, because it
  puts a shipped `そうか` → `Ｉ　ｓｅｅ．` one bank over in the same town skeleton.
  **Running total this wave: four coordinator figures/claims wrong, every one found by an agent
  measuring.** The dispatch line "your measurement wins and my cell is the error" is doing real
  work — keep writing it, and keep meaning it.
- 2026-09-09 (wave 7): **§25.3 COLLISION RULED by `batch_009` (reviewer must test it):
  `なるほど` → `Ｉｎｄｅｅｄ．` where it shares a bank with `そうか`; `そうか` keeps `Ｉ　ｓｅｅ．`.**
  Census: the two share banks **5, 8 and 33**, and this unit translates bank 8's instances of both.
  `なるほど` moves because it is the 2-row side, because `そうか` → `Ｉ　ｓｅｅ．` is shipped one bank
  over in the same skeleton, and because `なるほど`'s only shipped instances are chunk 33 and parked
  chunk 17. **`Ｅｘａｃｔｌｙ．` re-verified free and left reserved**; next reserve named as
  `Ｑｕｉｔｅ　ｒｉｇｈｔ．`
- 2026-09-09 (wave 7): **all six of my projected bank figures were CONSERVATIVE by 27–330 bytes** —
  measured by moving the file aside, re-merging and re-running `bankmeasure` rather than projecting.
  Actual: b7 13,095 · b8 10,727 · b9 12,205 · b10 33,921 · b11 39,345 · b12 8,559. **None of the
  four tight banks moved by a byte** (41 → 353, 40 → 447, 5 → 2,007, 2 → 3,365). Erring
  conservative is the right direction, but the projection is not the measurement.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle 23/44 (43.2%); script 311 (52.5%) |
| 6 | battle 24, 25, 26 + script 008 | **4** | 0 | battle **26/44 (51.0%)**; script **358 (53.1%)** |

Waves 5 and 6 both ran the full three-role split with a separate reviewer per unit and no
independence debt. Wave 6: PRs #21–#24, three merged at round 1, chunk 25 took one rework round
(`フフ` → the shipped `Ｆｕｆｕ`; bare `そして、` → `Ａｎｄ，`). Detail lives in `glossary.md`
§35–§42 and `FLAGS.md` §W–§AD, not here.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (a plain
   `checkout` lands on a stale ref — see Run configuration), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; `ListAgents`, then reconcile
   open PRs (`git ls-remote --heads origin 'tl/*'`; ⚠️ `list_pull_requests` returns oversized bodies).
3. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8.
