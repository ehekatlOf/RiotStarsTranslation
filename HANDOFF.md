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
2026-09-09 · by: **PR #29's reviewer** (integration commit; chunk 37 MERGED at round 3, squash
`5659d03`, glossary **§48**, FLAGS **§AJ**) · previously: **PR #33's reviewer** (chunk 38 MERGED,
squash `7bd8e76`, glossary §47, FLAGS §AI) ·
wave: **8 — 2 of 5 merged, 3 units still open (#30, #31, #32)** · queue: **script batch computed
fresh this wave, by line list, not by a `queue.py` position**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **30** | 44 | 0–4, 6–14, 18–22, 24, 25, 26, 30, 31, 33, 34, 35, **37**, **38**, 40 |
| Battle JP characters | **26,472** | 43,161 | **61.3%** (was 56.5% at wave-8 start) |
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
| battle chunk 37 | `tl/battle-037` | `tl/battle/chunk_037.txt` | **5,037 / 8,192 — 3,155 slack** (verified by the reviewer at round 3) | ✅ **PR #29 MERGED at round 3** — squash `5659d03`; integrated at glossary **§48**, `FLAGS.md` **§AJ**. Three rounds, five findings, **three of them gate-7 failures** (`やはり`, `始末`, `おい、`). ⚠️ **Leaves two live cross-unit obligations: `掌握` → `ｓｅｉｚｅ` (PR #30 must change `ｔｏ　ｇｒａｓｐ`; zero-cost, both words 5 columns) and `決着をつけてやる` → `ｓｅｔｔｌｅ` at chunk 41 `rowcheck` L8.** Nothing left on this unit |
| battle chunk 38 | `tl/battle-038` | `tl/battle/chunk_038.txt` | **5,577 / 8,192 — 2,615 slack** (verified by the reviewer) | ✅ **PR #33 MERGED at round 2** — squash `7bd8e76`; integrated at glossary **§47**, `FLAGS.md` **§AI**. **THE WAVE'S FIRST MERGE.** Nothing left on this unit |
| battle chunk 41 | `tl/battle-041` | `tl/battle/chunk_041.txt` | **3,033 / 8,192 — 5,159 slack** | **PR #30 OPEN**, awaiting reviewer |
| battle chunk 42 | `tl/battle-042` | `tl/battle/chunk_042.txt` | **3,629 / 8,192 — 4,563 slack** | **PR #31 OPEN**, awaiting reviewer |
| script batch 010 | `tl/script-010` | `tl/script/batch_010.tsv` | **53 lines / 293 instances**; bank 40 **447 → 75** | **PR #32 OPEN**, awaiting reviewer |

**THREE CELLS OF MINE REFUTED BY PR #32's MEASUREMENT — I re-verified all three; the PR is right.**
1. ⚠️ **`軍神ヘルメス` is NOT exhausted and its §9 row must stay LIVE.** My seed implied DATA 300
   closed it. **DATA 281** (`軍神ヘルメスの愛用したブーツ。{FFFE}防御力＋１　魔法防御＋１`) is a
   second untranslated **21-instance** line. ⚠️ It also needs a **`魔法防御`** form, which nothing
   fixes yet — and it lands in **bank 40**, which has only **75 bytes** left after this wave, so it
   may now be effectively unshippable. (The `石版` row **does** discharge: DATA 300 was its last
   untranslated instance — verified.)
2. **My dispatch said the prose window lands in "banks 20–29 with 25,000–40,000 free each". Wrong
   twice**: it lands in banks **25–28**, and **bank 25 has 12,891 free**, not 25,000+. No
   consequence — 12,891 still absorbs 41 prose lines — but the figure was wrong.
3. **My bank-40 estimate was 358; the true spend is 372** (still inside the 380 cap I set, leaving
   75 of 447). ⚠️ **The cause is a modelling lesson for wave 9's batch computation:** DATA 193/194's
   description clause is **already shipped in `batch_003`** as a two-row rendering, so CLAUDE.md §3
   forces that byte-identical English (+40 each) instead of a fresh, shorter one (~+24). **A line
   whose clause already exists elsewhere costs what the shipped form costs, not what an optimal new
   rendering would.** My growth model does not know this; a future batch estimate should check
   whether each line's clause is already rendered.

⚠️ **BANK 40 (75 free) AND BANK 5 (1,635) ARE EFFECTIVELY CLOSED after this wave.** Every remaining
count-21 item line spends its growth in **all 21** of its banks, bank 40 included. That is what
holds the 117 remaining item lines (2,457 instances) — see the run-status section above.

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

✅ **PR #33 (chunk 38) MERGED — the wave's first.** Squash `7bd8e76`, integration `1eaf370`,
re-verified green from a fresh checkout. **Battle 29/44, 25,487/43,161 JP chars (59.1%).**
Glossary **§47**, FLAGS **§AI**. `マラナ` promoted to §1 and struck from §9 — ⚠️ **its gender is
recorded as UNFIXED, not decided**, which is the right correction to my seed's wrong assertion.
⚠️ **The reviewer RATIFIED the translator's refusal of its own prescription** (`Ｂａｄ，` over
`Ｂａｄ！`) and recorded why it was wrong at §AI2: *"I prepended `ｔｈｅ` to the existing `Ｂａｄ！`
without re-reading the result."* All three forms measure 23, so width decided nothing.
⚠️ **§AI carries the sharpened §AG6 lesson: MEASURE THE REJECTED OPTION IN MORE THAN ONE WORD
ORDER.** A greedy row count is a proven minimum **only for the ordering it was given**, and six
correct measurements of six near-identical orderings produced a **false impossibility that nearly
parked a shippable unit**.
✅ **Gate 7 run glossary-key-first, as this wave's method finding requires: 1,097 keys enumerated,
27 occur in chunk 38's source, all 27 conform.** Recorded as the recommended sweep at **§AI4**. It
independently rediscovered the §28.3 `はっ` substring problem.
✅ **TWO THINGS IT DECLINED TO INTEGRATE, both correct:** PR #33's Flag 4 "correction" is itself
wrong (the clause is on the `鎮圧` row and is true) — filed as an addition, matching my own
independent finding; and Flag 5's `pending/chunk_005` item was **already recorded** at
`pending/README.md` line 31 from PR #18's review, so **no duplicate row was added** — and its
"L18" vs the README's "19" is the **DATA/FILE trap again** (file line 19 = body line 18, both
right), correctly left uncorrected in either direction.

### Review round 2 — PR #29: **CHANGES** again, ONE finding. Round 3 sent (the maximum).
All gates re-run from scratch on `dfa9771` against the moved base, re-positive-controlled on the
round-2 file. Figure **5,039 / 8,192** confirmed — the coincidence with round 1 is real, `git diff`
shows exactly four changed body lines (2, 4, 6, 18). Fixes 3 and 4 confirmed correct, and the
reviewer recorded its own round-1 error: it had read §37's scoped `始末する` row as general.
**Finding:** `おい、` ships `Ｈｅｙ，` where §32.3 (`glossary.md:2580`) fixes **`Ｏｉ，`**, and
`Ｈｅｙ，` is recorded *spent* on `よう、` (lines 2579, 3111). ⚠️ **Live across this wave — PR #33
already ships `Ｏｉ，`**, so merging #29 as-is would ship two renderings of one source word out of
one wave. Fix `Ｏｉ，　ｃａｌｌ　ｆｏｒ　ａｉｄ！！`, 19 → 18 columns, −2 bytes → **5,037 / 8,192**.
⚠️ **§4.3 DEBT, not this PR's:** `おい、` → `Ｈｅｙ，` is shipped in **merged** `chunk_000` (×3),
`chunk_008` (×1) and `chunk_031` — five instances predating or slipping past §32.3. A corrections
unit's job; every re-cut is byte-negative, so none is budget-blocked.

⚠️ **GATE 7 MUST BE RUN FROM THE GLOSSARY SIDE, KEY BY KEY — this is the wave's method finding.**
Round 1 asked "do the terms I noticed match?" and passed. Round 2 enumerated **all 44 glossary keys
occurring in chunk 37's source** and caught `おい、` — a three-character particle phrase that **no
content-word sweep reaches**, which is why the translator's own Japanese-side sweep missed it too.
**Gate 6 passed cleanly at round 1 while FOUR terms were wrong** (`全滅`, `始末`, `やはり`, `おい、`).
The sub-message sweep must be **glossary-KEY-driven, not term-noticed-driven.**

⚠️ **TWO GATE DEFECTS FOUND BY CHUNK 37's REWORK — THESE BIND EVERY FUTURE WAVE, NOT JUST THIS PR.**
Round 1 passed **gates 6 and 7 cleanly while three terms were wrong.** Both defects are structural.
1. ⚠️ **GATE 6 IS BLIND TO SUB-MESSAGE TERM RECURRENCE.** It pairs whole **messages**, so a term
   recurring inside *differently worded* messages is invisible to it. That is exactly what `全滅`,
   `始末` and `やはり` were. **A clean gate 6 is not evidence that terminology is consistent.**
   The missing check is a **Japanese-side sub-message sweep**, which is **not in CLAUDE.md §6** at
   all. Chunk 37's translator wrote one (`c037_terms.py`) and it immediately caught two more.
2. ⚠️ **GATE 7 CAN PASS WHILE A GLOSSARY ROW THAT NAMES THE EXACT SOURCE STRING IS VIOLATED.**
   Verified by me: `glossary.md` §37's `やはり、` row lists **`やはり反乱軍の`** among the five
   instances it fixes — that is chunk 37 L6 — and the unit shipped a loose `Ｓｏ　…`. Both the
   translator's self-check and the **reviewer's gate 7** passed it in round 1. Fixed at +8 bytes.
   **Gate 7 needs to be run as "for each glossary row, does any instance list name a line in this
   unit?", not as "do the terms I noticed match?"**
Also found: `始末する` — §37's row is scoped "a hapax in this sense" (chunk 22's political
euphemism); the **battle** sense ships as `ｆｉｎｉｓｈ` (merged c9, c19). §37 is not wrong; the unit
was reading a scoped row as general. **Same error class as the `全滅` finding: censusing the ENGLISH
and never the Japanese** (§Y2/§AC1).

**c38 round 2 pushed @ `41f8f37`.** All three findings fixed; figure **5,577 / 8,192, 2,615 slack**,
matching the reviewer's simulation exactly. `{FFFE}` unchanged in round 2 (still lines 1, 20, 22).
**One flagged deviation for the reviewer to ratify:** it ships `Ｂａｄ，　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ
ｍｅｎ！！` where the finding prescribed `Ｂａｄ！　ｔｈｅ…`. All three candidate forms measure **23**,
so width decides nothing; the source's own mark is `、`, and lower-case `ｔｈｅ` after `！` is
ungrammatical. A one-character change either way.
**A further gate-7 trap it found while adopting the ruling:** the participial keeping
`ｒｅｍｎａｎｔ　ｓｏｌｄｉｅｒｓ` needs **five** rows at both 23 and 24 (95 columns), and the only
four-row packing that keeps that noun goes through `ｏｆ　ｏｌｄ　Ｃａｒｌｉｎｅ　Ｋｉｎｇｄｏｍ`, which
**breaks §2's fixed `カーライン王国` → `Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ`** (glossary line 71). So
the shorter `ｒｅｍｎａｎｔｓ` is **forced**, not preferred, and the 残兵 row changes with it.

### ✅ Review 2 of 5, ROUND 2 — PR #33 (chunk 38): **MERGED.** Squash `7bd8e76`. THE WAVE'S FIRST MERGE.
All nine gates re-run on the round-2 file with **all-new** positive controls (structure, geometry and
duplicate checkers each re-planted at new sites; all fired). **5,577 / 8,192, 2,615 slack** — byte
cost re-derived from an independent implementation, matching the round-1 simulation to the byte.
`{FFFE}` 105→108 (lines 1, 20, 22 only); `{FCC0}` 12→12; 135 text rows, widest 23, **none at 24**.
Integrated at glossary **§47** and `FLAGS.md` **§AI**. Battle now **29/44, 25,487/43,161 JP (59.1%)**.

⚠️ **GATE 7 WAS RUN FROM THE GLOSSARY SIDE, KEY BY KEY — adopt this everywhere.** 1,097 Japanese
keys enumerated from every glossary table row, intersected with the chunk's source: **27 occur here,
all 27 conform.** Two fired as false positives and were adjudicated, not passed over (`はっ` only as
a substring of `はははっっ`; `だって`, whose row is scoped in its own text to *causal,
sentence-initial*). ✅ **`おい、` → `Ｏｉ，` confirmed correct in this unit** — and the method is what
reaches a three-character particle phrase at all. Now recorded as the recommended sweep at §AI4.

⚠️ **TWO ROLE-CORRECTIONS THIS ROUND, BOTH GOOD, BOTH RECORDED (§AI2, §AI3).** ① **The reviewer's own
prescribed fix was wrong by one character and the translator refused it.** Round 1 prescribed
`Ｂａｄ！　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ！！` — ungrammatical, a lowercase word after a full-stop-strength
`！`, because `ｔｈｅ` was prepended to the old `Ｂａｄ！` without re-reading the result. Shipped
`Ｂａｄ，　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ！！`: all three candidates measure **23**, so width decided
nothing, and the source's own mark is `、`. **Ratified.** ② **`残兵` → `ｒｅｍｎａｎｔｓ` is FORCED by a
gate, not preferred** — every §2-conformant wording keeping `ｒｅｍｎａｎｔ　ｓｏｌｄｉｅｒｓ` needs five
rows (98/100/95 cols), and the only four-row packing that keeps it breaks §2's fixed `カーライン王国`
→ `Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ`. **Confirmed.** (One figure corrected without effect: the *95*
is the possessive variant; the participial is **98**.)

⚠️ **TWO ITEMS THAT DID *NOT* GO INTO THE RECORD, AND THAT IS THE POINT (§AI6, §AI7).**
① **PR #33's Flag 4 "correction" to §37.1 was itself wrong** — the quoted "2 battle / 0 script —
closed" clause belongs to the **`鎮圧` row above it (line 3639), where it is TRUE**; the `反乱 (bare)`
row (3640) carries **no count at all**. Filed the measurement as an **addition** plus a §38.3 scoping
note, not as a §4.3 correction. ② **Flag 5's `pending/chunk_005.txt` village line is ALREADY
recorded** — `pending/README.md` line 31, from PR #18's review — so **no duplicate row was added**.
⚠️ Its "L18" vs the README's "19" is **not a discrepancy**: the line is **file line 19 = body line
18**, both right, the DATA/FILE trap in a new file. **A wrong correction is worse than a wrong
figure; verify a quotation by reading the line, even when the quoting agent has been right about
everything else — as this one had.**

**Already-accepted round-1 corrections are integrated:** §9's `マラナ` gender note corrected in place
and the row promoted to §1 and struck (exhausted; gender **recorded as unfixed**, the §Y6 shape a
second time); §28.3's `ははっ` list struck of chunk 38 (a `はははっ` substring; the four genuine
assents stand, and §29's `うん` argument was checked and is undisturbed).

### Review 2 of 5 — PR #33 (chunk 38): **CHANGES**, round 1. Rework sent.
Eight of nine gates pass, independently re-derived (byte cost reimplemented from scratch; full tag
stream diffed; gates 4, 6 and 8 positive-controlled). **Gate 7 fails**: `帝国軍` shipped without the
article, where §20.4 fixes two forms and **11 of 11** shipped instances carry it. Fix
`ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ` (23 cols, +6 bytes). Post-fix simulated: **5,577 / 8,192, 2,615 slack.**

⚠️ **RULING — `反旗を翻す`: THE BANNER FORM WINS. PR #33 MOVES; PR #31 DOES NOT. CHUNK 38 IS NOT
PARKED.** ⚠️ **Chunk 38's geometric argument was REFUTED BY MEASUREMENT — and this is the payoff for
telling the reviewer to verify it rather than accept it.** #33 measured six wordings and concluded
"every one needs a fifth row"; **it only ever tested orderings where `ｔｈｅ　ｂａｎｎｅｒ　ｏｆ`
precedes `ｒｅｖｏｌｔ．．．．．` on the same row.** Moving `ｂａｎｎｅｒ　ｏｆ` down gives
`Ａ　ｆｅｗ　ｒｅｍｎａｎｔｓ　ｏｆ　ｔｈｅ` / `ｏｌｄ　Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ` /
`ｏｐｐｏｓｅｄ　ｉｔ，　ｒａｉｓｉｎｇ　ｔｈｅ` / `ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ．．．．．` — **four rows
≤23, all four content elements kept, 王国 intact, +6 bytes.** A "no wording fits" claim is a claim
about a **search**, not a measurement, and §AG6 says nothing ever checks the rejected option.
**Binding on PR #30 (chunk 41):** the unbroken `アイテムを奪われました。` is genuinely a different key
— broken form exactly 7 (c3, c9×3, c28, c29, c30, matching §21.3), unbroken form 4 (c38 L22, c39 L9,
**c41 L10 and L12**). Chunk 41 must render it byte-identically to chunk 38's, with the one forced
`{FFFE}` (28 columns unbroken).

### Review 1 of 5 — PR #29 (chunk 37): **CHANGES**, round 1. Rework sent to the same translator.
All nine gates passed and were **independently re-measured** (gate 6 positive-controlled with two
planted corruptions; L14's 8 rows proved inherited from a pristine extraction). Two reading
findings, both single-segment word swaps: a lowercase sentence-start (`ｏｕｒ` → `Ｏｕｒ`), and
`全滅` → `ａｎｎｉｈｉｌａｔｅ` diverging from the `ｗｉｐｅ(ｄ)　ｏｕｔ` of merged chunks 2, 9, 19 **and
of open PR #33**. Post-fix figure simulated by the reviewer: **5,035 / 8,192, 3,157 slack**.

⚠️ **RULING — `掌握` → `ｓｅｉｚｅ` WINS. PR #29 does NOT move; PR #30 (chunk 41) DOES.**
`ｔｏ　ｇｒａｓｐ` → `ｔｏ　ｓｅｉｚｅ`: both 5 columns, row 22 either way — **zero bytes, zero re-flow**.
⚠️ **The reviewer corrected MY framing, and it is right:** I said #29's `ｓｅｉｚｅｄ` "appears to
create a §25.3 collision". **§25.3's test is CO-OCCURRENCE, not spend.** `ｓｅｉｚｅ`'s existing sets
(`取り押さえ` c6/c22, `捕まえ` c21) and `掌握`'s (c37, c41, script FILE 870) are **disjoint — no
chunk, bank or line holds two** — the same licence §28.3 used for `Ｙｅｓ，`. And
`ｇｒａｓｐ　Ｉｍｐｅｒｉａｌ　ｓｔｒｅｎｇｔｈ` is not idiomatic English. Glossary row goes in live,
struck at chunk 41's merge (`ルート` precedent, §29.1/§30.1).
✅ **§Y6 settled and its premise refuted — Cress is FEMALE** (reviewer re-verified by reading chunk
13, not the citation). ✅ **L14's 8 segments kept** — index safety under §L2 is the right branch
while Blocked 4 is open.
**Counts corrected:** `小隊` is 2 script lines / 3 instances (FILE 524, 1389); `マーシュ` is 3 lines
/ 4 instances (FILE 870, 1330, 1379) and **FILE 1379 establishes Marsh is the ship's captain**;
`マザロー` hapax confirmed → struck.
✅ **The reviewer independently confirmed my DATA/FILE handling**: HANDOFF's DATA 1378/1380 and PR
#30's FILE 1383/1385 for `決着` are **both right, two conventions** — correctly NOT recorded as an
error either way.

✅ **WAVE BARRIER MET 14:43Z — all five units have an open PR (#29, #30, #31, #32, #33).**
Review order: **37 → 38 → 41 → 42 → script 010**, one reviewer at a time, foreground.

⚠️ **A SEED CELL OF MINE IS WRONG AND PR #33 CAUGHT IT — I RE-VERIFIED AND THE PR IS RIGHT.**
My §9 wave-8 seed says `マラナ`'s `〜わ` marks her **FEMALE**. **It does not.** Verified by me over
the pristine dump: sentence-final `わ` occurs **40** times and at least four speakers are
unambiguously male — c16 `このワシが始末してくれるわ！` (**ワシ**), c39 `一人残らず始末してくれるわ！`
(**Doctor Crimea**, §1/§25.1), c42 `俺様が始末してやるわ！` (**俺様**), c43 `目にもの見せてくれるわ。`
(**Helfer**). Marana's own chunk-38 particles are masculine-leaning (`ぞ`, `〜おって`), and Seti calls
the opponent `おっさん`, whose fixed English is `ｇｅｅｚｅｒ` (§24.2). **No rendering turns on it** —
she is first-person throughout and PR #33 added no gendered pronoun. **The §9 note must be corrected,
not the file.** ⚠️ This is the §Y6 (Cress) shape a second time: a seeded gender assertion that the
corpus does not carry.

⚠️ **THE ONE DIVERGENCE THE REVIEWER MUST RULE — `反旗を翻す`, PR #33 vs PR #31.**
- **#33 (chunk 38)**: `ｒｏｓｅ　ｉｎ　ｒｅｖｏｌｔ．．．．．`
- **#31 (chunk 42)**: `ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ`
- **#33 measured six wordings of #31's form into its own L18 page 2 and every one that keeps all
  four content elements needs a FIFTH row** on a page already at the 4-row wall with a **leading**
  (unfillable) blank — and `{FCC0}` is forbidden. The only wording that fits **deletes 王国**, which
  CLAUDE.md §3 forbids. So if the reviewer rules for the banner form, **chunk 38 must be PARKED or
  chunk 42 changed instead** — a re-cut of that page is not available.
- ✅ The other two shared terms **already agree** with no change: `おのれ` → `Ｃｕｒｓｅ` and
  `刃を向ける` → `ｔｕｒｎ　ａ　ｂｌａｄｅ　ｏｎ` (#33 and #30 arrived at both independently).

**PR #33 also raises three corrections to EXISTING glossary/FLAGS rows** (reviewer to integrate):
§28.3's `ははっ` list wrongly counts chunk 38 — that instance is `はははっっ`, a **laugh** by Marana
answering no one, caught as a **substring** false positive; the four genuine assents stand.
⚠️ ~~§37.1's bare `反乱` "closed" claim is wrong~~ — **STRUCK. I PROPAGATED A MISQUOTE.** PR #33's
Flag 4 attributed the "2 battle / 0 script — closed" clause to the `反乱 (bare)` row and I recorded
it here without reading the row. **Verified by me now: `glossary.md` line 3639 is the `鎮圧` row and
carries that clause; line 3640, `反乱 (bare)`, carries NO count at all — and 鎮圧's own claim is
TRUE (chunks 22, 43). Nothing in the glossary needs correcting.** PR #33's underlying measurement of
`反乱` goes in as an addition, not a §4.3 correction. ⚠️ **This is the SECOND figure I passed on
unverified this wave** (after "chunk 41 L7"), and both were caught by the next role.
`pending/chunk_005.txt` L18 does diverge from §27.2's village line — parked, nothing broken today.

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
