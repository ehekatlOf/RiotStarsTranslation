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
> **WAVE 8 IS IN FLIGHT — 5 units dispatched, glossary seeded at `5402c68`.** The coordinator is
> `session_01GMZPvT2GCVmRBd8pwHPGED`. Nothing is reviewed until **all five** units have an open PR
> (the wave barrier, CLAUDE.md §4 step 4).
>
> If you are resuming and the five PRs are open: review them **one at a time, in unit order**,
> `run_in_background: false`. If a unit has no PR and its translator is gone, re-dispatch that unit
> (two rounds max, then park). If a unit has no PR and its translator is alive, **wait**.
>
> When the wave closes, open **wave 9's session** with `create_session` — BOTH `source_url`
> (`https://github.com/ehekatlOf/RiotStarsTranslation`) and
> `source_revision` (`claude/workflow-translation-iterate-uzlkns`) are required.
>
> ⚠️ **WAVE 8 SPENDS THE LAST FOUR DISPATCHABLE BATTLE CHUNKS.** After it, battle work **STOPS
> ENTIRELY** until a human clears Blocked **0** or **0a**. Both were re-tested at wave 8's preflight
> and **both are still unfixed**. Wave 9 is script-only. Say so in wave 9's seed.

## Last updated
2026-09-09 · by: **wave-8 coordinator** (`session_01GMZPvT2GCVmRBd8pwHPGED`) ·
wave: **8 DISPATCHED — 5 units in flight** · queue: **script batch computed fresh this wave, by
line list, not by a `queue.py` position**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **28** | 44 | 0–4, 6–14, 18–22, 24, 25, 26, **30**, **31**, 33, 34, 35, 40 |
| Battle JP characters | **24,407** | 43,161 | **56.5%** (was 51.0% at wave-7 start) |
| Script unique lines | **408** | 1,430 | `tl/script/batch_001–009.tsv` |
| Script message instances | **4,259** | 7,931 | **53.7%** |

`check`: **All checks passed** at `6d73819`. ⚠️ **Tightest banks, re-measured at PR #28's review:
41 → 353, 40 → 447, 5 → 2,007, 2 → 3,365** — wave 7 moved none of them (`batch_009` spent only
banks 7–12: b7 13,095 · b8 10,727 · b9 12,205 · b10 33,921 · b11 39,345 · b12 8,559).
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact, Blocked 0),
**36** (charset gate, Blocked **0a** — new this wave).

## In flight — WAVE 8 (dispatched 2026-09-09)
Base for every unit: `claude/workflow-translation-iterate-uzlkns` @ `5402c68`. Round 1 for all.

| Unit | Branch | File | Figures at dispatch | State |
|---|---|---|---|---|
| battle chunk 37 | `tl/battle-037` | `tl/battle/chunk_037.txt` | **5,039 / 8,192 — 3,153 slack** | **PR #29 OPEN**, awaiting reviewer |
| battle chunk 38 | `tl/battle-038` | `tl/battle/chunk_038.txt` | JP 1,080, headroom 5,115, ratio **3.37** (tier C) | dispatched |
| battle chunk 41 | `tl/battle-041` | `tl/battle/chunk_041.txt` | **3,033 / 8,192 — 5,159 slack** | **PR #30 OPEN**, awaiting reviewer |
| battle chunk 42 | `tl/battle-042` | `tl/battle/chunk_042.txt` | **3,629 / 8,192 — 4,563 slack** | **PR #31 OPEN**, awaiting reviewer |
| script batch 010 | `tl/script-010` | `tl/script/batch_010.tsv` | **53 lines / 293 instances** / 2,477 JP chars | dispatched |

**CROSS-UNIT TERMS THE REVIEWER MUST CROSS-CHECK BETWEEN OPEN PRs** (all measured by me over the
pristine dump, tags stripped — the source *messages* differ in every case, so **CLAUDE.md §3 is NOT
engaged**; these are §25.3 term-consistency calls):
| Term | Where | Rendering | Note |
|---|---|---|---|
| `掌握` | c37 ×1, c41 ×1 | **#29 `ｓｅｉｚｅｄ` vs #30 `ｇｒａｓｐ`** | ⚠️ **A real divergence — see below** |
| `決着をつけてやる` | c30 ×2 (shipped), c37, c41 | `ｓｅｔｔｌｅ` | Agreed across all three |
| `反旗を翻す` | c38 ×1, c42 ×1 | #31 `ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ` | ⚠️ c38's is **split across a `{FFFE}`** (`反旗を{FFFE}翻した`), so a whole-phrase grep misses it. §25.3 vs §2's 旗印 → `ｂａｎｎｅｒ` (c0, c27) is **met**: disjoint chunk sets |
| `おのれ` | c38 ×1, c41 ×2, c43 ×1 | #30 `Ｃｕｒｓｅ` | Nowhere in `tl/` — first **shipping** use (parked c43 has it) |
| `刃を向け` | c38 ×1, c41 ×1 | #30 `ｔｕｒｎｅｄ　ａ　ｂｌａｄｅ　ｏｎ　ｕｓ` | — |
| `ネズミ` family | 13 battle; c42 ×7, c41 ×2 | #31 spends 5 forms, #30 spends 2 | ⚠️ #31 notes c41's `この野ネズミが` is **grammatically SINGULAR** and §41.1 fixes only the plural `ｆｉｅｌｄ　ｍｉｃｅ`; `ｆｉｅｌｄ　ｍｏｕｓｅ` is unspent |
I sent the last three to chunk 38 mid-flight, as I did `決着` to chunk 41.

**PR #31 (chunk 42) also contributes independent evidence for §L2's pool reading** — worth carrying
into Blocked 4's in-game visit. `はっ！` is forced to `Ｓｉｒ！` by **6 of 6** shipped instances, yet
in L11 it lands mid-way through a run of Helfer's taunts, where a subordinate's assent makes no
narrative sense. That is a **second, independent** consistency argument for pools of
independently-selected strings, from a different chunk than §AE6's chunk 30.

⚠️ **CROSS-PR COLLISION — PRs #29 AND #30 RENDER `掌握` DIFFERENTLY. THE REVIEWER MUST RULE.**
Found by me from both open PRs; the wave barrier is what made it visible before either merged.
- **PR #29 (chunk 37)**, body line 18: `ヘルファーが帝国と手を結び軍を掌握したんだ` →
  `ｓｅｉｚｅｄ　ｔｈｅ　ａｒｍｙ`. Chunk 37 did **not** flag `掌握` at all.
- **PR #30 (chunk 41)**, body line 9: `帝国兵の力も掌握するつもりなのです` → `ｔｏ　ｇｒａｓｐ`.
  Chunk 41 flagged it as cross-unit and offered to be the one that moves.
- **I measured chunk 41's stated reason and it holds**: `ｓｅｉｚｅ` is ALREADY SPENT in three
  **shipped** files — `chunk_006`, `chunk_021`, `chunk_022` — on a different source word
  (`取り押さえろ` and chunk 22's Fernando line). **`ｇｒａｓｐ` occurs nowhere in `tl/` or
  `pending/`.** So PR #29's choice creates a §25.3 co-occurrence collision and PR #30's does not.
- ⚠️ **The two Japanese MESSAGES differ entirely, so CLAUDE.md §3's byte-identical rule is NOT
  engaged.** This is term consistency under §25.3, not a gate failure. Reviewer's call, on the
  evidence above; whichever way it goes, the second PR to merge must match the first.

⚠️ **A FIGURE OF MINE TRAVELLED UNMEASURED AND WAS WRONG — recorded because the board preaches it.**
My mid-flight note to chunk 41 said the line was "chunk 41 L7". I copied that from PR #29's report
without reading it. **It is line 8** (convention: `=== CHUNK` header = line 0, so the first body line
is line 1 — `rowcheck`'s numbering); **line 7 is the tag-only `{FCE0}{=0001}{FFFF}`**, no readable
text. Verified by me in the dump. PR #30 caught it. Exactly the §AE-class failure the Decisions
section describes: a wrong figure travels, and only the next role catches it.

⚠️ **AND THE COUNTER-CASE, so it is NOT recorded as an error: PR #30 cites the two script instances
as `script_unique` 1383 and 1385; I measure them at 1378 and 1380. BOTH ARE RIGHT** — 1383/1385 are
**FILE**, 1378/1380 are **DATA**, and FILE = DATA + 5. Do **not** "correct" either into the other:
this is precisely the §AE5 / §AF3 trap that wave 7 had to withdraw. Substance confirmed by me: both
lines are **bank 41**, count 1, untranslated. So `決着をつけてやる` reaches **4 battle instances
(chunks 30 ×2, 37, 41) + 2 script (DATA 1378, 1380, bank 41)** — larger than the 3 battle my note
claimed. Bank 41 has 353 bytes free, so the script half is unshippable for now regardless.

**PR #29 (chunk 37) carries three things the reviewer must integrate, not just merge:**
1. ⚠️ **`FLAGS.md` §Y6 is SETTLED — Cress is FEMALE — and §Y6's own premise is REFUTED.** §Y6 says
   "no shipped English anywhere genders Cress". That is **false**: merged `tl/battle/chunk_013.txt`
   body line 0 already ships `ａ　ｗｏｍａｎ　ｃａｐｔａｉｎ` addressed to Cress by name, rendering
   the source's `女隊長` (corroborated by `上玉` / `献上してやる`, and `chunk_022` addresses her as
   `クレス隊長`). The project committed to female in **wave 3** and §Y6 did not notice. **No
   rendering changes anywhere.** Record the refutation, not only the answer, and correct glossary
   §1's `クレス` row to state the gender.
2. **Cross-unit, already actioned by me:** `決着をつけてやる` is in chunks 30 (shipped, renders
   `ｓｅｔｔｌｅ`), 37 and **41**. I verified it in the dump and sent chunk 41's translator the
   precedent mid-flight. ⚠️ **Chunk 30 writes it `決着を{FFFE}つけて` — a `{FFFE}` splits the
   phrase, so a naive grep misses chunk 30.** Check chunk 41's PR uses `ｓｅｔｔｌｅ`.
3. **§9 row states:** strike `マザロー` (hapax, exhausted). **Keep `マーシュ` LIVE** — 3 script
   instances remain untranslated (the twin scene at `script_unique` 870, outside batch_010's
   880–920 window). New `小隊` row also stays live (1 script instance, unique 524).

⚠️ **Chunk 37** inherits `FLAGS.md` §Y6 (Cress's gender — unfixed and unrendered anywhere; settle
it with evidence or flag it, never guess silently). ⚠️ **Chunk 42 L11** is one of §L2's no-`{FC50}`
16-row pages — an in-game question (Blocked 4), **not the translator's to solve**.

## Next up — WAVE 8 (⚠️ THE LAST BATTLE WAVE)
**Seed the glossary BEFORE dispatching.** Sections currently end at **glossary §46** and **FLAGS
§AH** — ⚠️ take the next number by **READING both files at commit time**, never by reserving.

**1–4. Battle chunks 37, 38, 41, 42 — the ONLY dispatchable battle chunks left.** From
`queue.py battle`: 37 (JP 985, ratio **3.69**), 38 (1,080, **3.37**), 41 (593, **6.54**),
42 (698, **5.46**) — all comfortable, none tier-A.
⚠️ **Chunk 37 inherits `FLAGS.md` §Y6** — Cress's gender is fixed nowhere and rendered nowhere.
⚠️ **Chunk 42 L11** is one of §L2's no-`{FC50}` 16-row pages (in-game question, Blocked 4).

**5. One script batch — COMPUTE IT YOURSELF, DO NOT INHERIT A POSITION.**
⚠️ **Name the unit by LINE LIST, never by a `queue.py` position** — wave 7 was handed "position 6"
and it was a different range. Re-run `queue.py script` against the figures above, check the batch
is bank-feasible by **INSTANCES not lines**, and verify scaffolding and already-done counts.
⚠️ **`石版` (DATA 300, count 21, 21 banks) and `ビーストショップ／アイテムショップ` (DATA 899, bank 28)
are both still untranslated and both keep a §9 row live** — a batch containing either discharges it.

## ⚠️ THE RUN IS **NOT** COMPLETE AFTER WAVE 8 — MEASURED 2026-09-09, WAVE 8
**"Wave 8 is the last BATTLE wave" is TRUE. "Wave 8 is the FINAL wave" is FALSE.** The two are
being conflated, and acting on the second would end the run with ~12 waves of shippable work left.

Measured by simulating `queue.py`'s own allocator with batch_010 removed from the pool:
| After batch_010 merges | lines | instances |
|---|---|---|
| Untranslated unique | 969 | 3,379 |
| **Bank-FEASIBLE — dispatchable now** | **603** | **628** |
| Bank-blocked (needs a human) | 366 | 2,751 |

**603 feasible unique lines ≈ 12 more script batches at 40–60 lines each.** So CLAUDE.md §8's
"no dispatchable unit left" does **NOT** hold, and **wave 9 MUST be opened — script-only.**
Of the 366 blocked, **117 are 21-instance item-table lines (2,457 instances) held solely by bank
40**, which will have ~89 of its 447 bytes left after this wave. Those need Blocked 2's repoint.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **15 open chunks.** ⚠️ **6 carry the §D1 dump artifact and will park exactly as chunk 17 did
— 15, 23, 27, 28, 29, 39**; **16 and 32 are tier-A blocked**. So only **4 are dispatchable** now
that wave 7 spent 30, 31 and 36: **37, 38, 41, 42** — **one more wave**, and then battle work stops
until a human fixes the dumper (Blocked 0) or the charset gate (Blocked 0a).

Script: **1,022 unique lines / 3,672 instances** untranslated (was 1,072 / 3,722; batch_009 took
50 / 50). ⚠️ **Bank capacity, not the queue, is the binding constraint.** ⚠️ **Do NOT cite a
`queue.py` position for a hand-cut range** — wave 7's batch was dispatched as "position 6" and the
label was wrong (it was the hand-cut DATA 534–583); **cite script batches by their DATA line list,
and state the convention**, per `glossary.md` §44.5 and §46. ⚠️ **Chunk 37 (a later wave) inherits
`FLAGS.md` §Y6**: Cress's gender is fixed nowhere and rendered nowhere in `tl/`.

## Blocked — needs a human
0a. 🔧 **NEW 2026-09-09 — THE CHEAPEST ITEM ON THIS LIST, AND IT IS NOT ITEM 0.** `FLAGS.md`
   **§AF1**. `assemble.py:validate_body` applies its charset whitelist to **preserved SOURCE
   machine text**. Battle chunk 36 is mostly a full-width MIPS assembly listing, English machine
   output and a garbage block, all of which must survive byte-for-byte; **38 characters of it are
   rejected** (`＄`×14 `＞`×10 `＿`×4 `＃`×4 `｜`×3 `ケ` `あ` `「`) and **not one is on a translated
   run**. Measured at the PR #25 review: the pristine chunk raises **193** problems, the delivered
   translation **38**, all charset, **0 tag-parity / 0 column / 0 byte**, and **0** with
   `jp_ok=True`. `pending/chunk_036.txt` is finished, faithful and **5,305 bytes UNDER its slot**.
   ⚠️ **This is NOT item 0 / §D1** — §D1 is `{FC70}`/`{FCA8}` mis-tokenisation in `riotbattle` and
   needs a re-dump; this is the charset whitelist in `assemble.validate_body` and needs **one
   function**: skip the charset check on runs byte-identical to the dump. ⚠️ **Widening `ALLOWED`
   alone is INSUFFICIENT — the garbage block contains kana** (`ケ`, `あ`), and blanket-allowing kana
   would disable the gate that catches untranslated Japanese. **Needs no disc, no EXE, no emulator
   and no dumper change.** Afterwards, unparking is `git mv pending/chunk_036.txt
   tl/battle/chunk_036.txt` and nothing else. **986 JP characters — 2.3 % of the battle script —
   are finished and waiting on it.**
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
⚠️ **RULINGS LIVE IN THEIR HOMES, NOT HERE** — `glossary.md` §23–**§46**, `FLAGS.md` §K–**§AH**,
`findings.md` §24, `pending/README.md`. Section numbers are taken by **READING both files at commit
time**, never reserved. This section keeps only what does not belong to a single unit.

**Standing (waves 4–8).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×** (realised aggregate **2.118**, re-measured wave 8
over 408 shipped lines). Bank 40's budget goes to the 21-instance item table, not its story text.
Seed the glossary **before** dispatching. A **parked unit still gets the full reading review**. The
`queue.py` batch **position is not the filename, and not the unit** — name script batches by their
**DATA line list** and state the convention. A term is "in the glossary" only if a row **fixes an
English form**. Mechanical term search has **four blind spots** (mixed script, maximal runs,
katakana register transforms, kana variants — §Y2/§AC1). A glossary row's **Alt column records
REJECTED options, not a menu**. `{FCC0}` is forbidden by `assemble.py:tag_parity`, **not** by
`rowcheck.py` (§Q2, already correct — never patch it).

**Measurement discipline — the rules that keep earning their space.**
- ⚠️ **"Your measurement wins and my cell is the error" goes in every dispatch.** Wave 7 had **nine**
  coordinator/inherited figures refuted by measurement; wave 8's own briefing then asserted DATA 300
  was "not bank-blocked" when it lands in bank 40 (see Remaining). **A wrong figure travels, and
  only the third role catches it.**
- ⚠️ **VERIFY IN BOTH DIRECTIONS — a wrong correction is worse than a wrong figure**, because it
  enters the record as fact. Wave 7's `石版` DATA 569/571 → "FILE 574/576" correction was itself
  wrong (same lines, two conventions) and had to be withdrawn (§AF3, glossary §44.5).
- ⚠️ **STATE YOUR NUMBERING CONVENTION on every line-number claim** — seven exist in this repo —
  and **cite a location by READING it, not by copying a citation.** Verified wave 8: in
  `script_unique.txt`, **FILE = DATA + 5**, constant offset; `queue.py` uses DATA.
- ⚠️ **MEASURE THE OPTION YOU ARGUE AGAINST** (§AC3 / FLAGS §AG6). A rejected alternative never
  enters the file, so no gate ever checks it — that is where hand-counting survives. Wave 8 caught
  two of its own hand-counted glossary widths this way before committing.
- ⚠️ **A CHECKER THAT MATCHES NOTHING REPORTS A CLEAN PASS** (§AE7). **Plant a corruption, prove the
  checker fails on it, then trust it.** Battle `tl/` files hold no Japanese, so grepping one for a
  source string is a null check — use the positional method; script TSVs keep Japanese in column 2,
  so a column-2 comparison IS valid there.
- **A CENSUS BEATS A PLAUSIBLE READING OF THE STYLE GUIDE** (glossary §45.2 / FLAGS §AG1). A
  page's source-blank **trailing** segment MAY carry text: `.TTTT` is attested **182** times across
  the 44 pristine chunks, `.TTTT.` **0**. §3.2's warning is about `.TTTT.` only. Chunk 31 lost a
  review round compressing for a constraint that does not exist.
- **SERIALISED REVIEW EARNS ITS WALL-CLOCK.** Chunk 30 merged between chunk 31's two review rounds
  and supplied three more `どうやら` instances that confirmed §41.4 (now **13 of 13**, glossary
  §45.4). Never two reviewers at once; a translator reworking does **not** occupy the reviewer slot.
- **A reviewer can finish its merge and integration while still "running".** Do not pull or write
  HANDOFF mid-integration; if one dies after merging but before integrating, do the integration
  yourself — **never re-review a merged PR.**
## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle 23/44 (43.2%); script 311 (52.5%) |
| 6 | battle 24, 25, 26 + script 008 | **4** | 0 | battle 26/44 (51.0%); script 358 (53.1%) |
| 7 | battle 30, 31, 36 + script 009 | **3** | **1** | battle **28/44 (56.5%)**; script **408 (53.7%)** |

**Wave 7 detail.** PRs #25–#28, full three-role split, four separate reviewers. Chunk 30 (7,615 /
8,192) and script `batch_009` (+6,026 bytes, 2.034×) merged at round 1; chunk 31 (5,399 / 8,192)
took one rework round; **chunk 36 PARKED on a NEW tooling blocker** (Blocked **0a**). Detail lives
in `glossary.md` §43–§46 and `FLAGS.md` §AE–§AH, not here. **Nine coordinator/inherited figures were
refuted by measurement and two corrections made TO the coordinator were themselves wrong** — see
Decisions.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (a plain
   `checkout` lands on a stale ref — see Run configuration), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; `ListAgents`, then reconcile
   open PRs (`git ls-remote --heads origin 'tl/*'`; ⚠️ `list_pull_requests` returns oversized bodies).
3. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8.
