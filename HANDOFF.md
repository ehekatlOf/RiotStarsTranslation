## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main`
is at the close commit (`CLAUDE.md` top banner). **This block used to redirect the run to
`claude/workflow-translation-iterate-uzlkns` and told every agent to read `main` as that branch —
twelve waves merged there while `main` sat untouched and a human was told nothing had been done.**
`main` was fast-forwarded to the branch tip on 2026-09-11 (284 commits, 54 translated units); the
old branch is kept identical to `main` as a mirror and has no authority.

⚠️ **A fresh container clones SHALLOW and may carry a STALE local ref of `main`.** If `git checkout
main` lands you on an old commit or `git pull --ff-only` aborts: `git fetch && git reset --hard
origin/main`, verify with `git log -1`.

## NEXT ACTION — always current, always a literal instruction
> # ✅ THE RUN'S AUTOMATED TRANSLATION WORK IS COMPLETE. THERE IS NOTHING LEFT FOR AN AGENT TO DISPATCH.
> **WAVE 12 CLOSED — 4 of 4 MERGED, ALL AT ROUND 1, 0 PARKED, 0 LOST, 0 RE-DISPATCHES.**
> **Script 63.6% → 65.3%. Battle unchanged at 64.3% (blocked, not idle).**
>
> ## ⛔ I DID NOT OPEN A WAVE 13, AND THAT IS A MEASURED DECISION, NOT AN OMISSION.
> **CLAUDE.md §8's first stop condition — "No dispatchable unit left → final handoff, stop" — now
> holds, and I verified it rather than assumed it.** Re-running the feasibility census on the closed
> branch: **366 unique lines / 2,751 instances remain and FEASIBLE = 0 lines, 0 instances.**
> Wave 12 consumed **all 116** bank-feasible lines that existed at its open.
> **Opening a session whose only possible finding is "there is nothing to do" would burn a context to
> re-derive this number.** The root runner session's own watchdog independently reached the same
> conclusion. **If you want the run resumed, the unblocking tasks below are the work — not another wave.**
>
> ### ⚠️ ONE HONEST QUALIFICATION, so nobody reads "0" as more absolute than it is
> **0 is measured at this run's standing planning rate — 2.10× growth with a 500-byte safety reserve.**
> Two lines are **marginal** rather than impossible: **D519 (745 JP chars) and D520 (850)** each fail
> at 2.10× and each *would* fit **only by spending bank 5's entire remaining 1,595 bytes**, and only if
> the translation realised ~1.87× (wave 12's actual rate). **At most ONE of the two could ever fit**
> — together they need 2,762 B. **D518 (1,184 chars) cannot fit either way.** All three are enormous
> pooled multi-scene rows (D518 even opens with a `１２３４５６７８９０１２` ruler string), i.e. FLAGS
> §L2's independently-selected string pools. **Spending the last safety reserve in a tight bank on one
> pooled row is a policy decision for a human, not a dispatchable unit** — and it is the same trade
> §F2 already resolved the other way for bank 40 (budget goes to the 21-instance item table, not to
> one-instance story text).

## Last updated
2026-09-11 · by: **wave-12 coordinator** (`session_01UMK4VSo7m2SaC6uqaJKCdX`, top-level) ·
**wave 12 CLOSED — 4 of 4 merged (PRs #43, #44, #45, #46), all at round 1, 0 parked** ·
**THIS IS THE RUN'S FINAL HANDOFF** · every figure below measured by me on the closed branch

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — **blocked, not idle**; 0 dispatchable |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **1,064** | 1,430 | `tl/script/batch_001–022.tsv` (was 948) |
| Script message instances | **5,180** | 7,931 | **65.3%** (was 63.6%) |

`check`: **All checks passed** at `a19e7d2`. **glossary ends §64 · FLAGS ends §AZ** — ⚠️ **always take
the next number by READING both files at commit time, never by reserving.**
`build/*_dump_merged.txt` regenerated at this close. README status table refreshed. **All worktrees
pruned — `git worktree list` shows only the main checkout.** **No open PR, no live agent.**
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE, and WHICH ONE IT HIDES IS NOT STABLE** — it
hid bank 5 before wave 12 and hides **bank 2** now. **Quote the table, never that line.**
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight
**Nothing. The run is complete.** No open PR, no unmerged unit branch, no live agent, no worktree.
⚠️ **Every `tl/*` branch from waves 1–12 is MERGED but still on origin** — deletion returns **HTTP 403**
from the agent container (**FLAGS §AQ9**), every wave. **"Branch gone = merged" is an INVALID signal in
this repo; use the PR's `merged: true` and the squash SHA in the committed record.**

## Next up
**NOTHING DISPATCHABLE — MEASURED, NOT ASSUMED.** See NEXT ACTION for the census and its one
qualification. The work that remains is the human list below, in that order.

## Remaining — 366 unique lines / 2,751 instances, and the binding constraint for every one
**Battle: 0 dispatchable.** 8 chunks remain, **all blocked** — 15, 23, 27, 28, 29, 39 by §D1's dump
artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's 1.64×).
⚠️ **`queue.py battle` reports "dispatchable 11" and is WRONG ON BOTH COUNTS** — its tier-A cutoff is
hardcoded **1.6**, and it knows **nothing** about §D1.

**Script: 366 unique lines / 2,751 instances**, and I measured the binding bank for each:
| Binding bank | Lines | Instances | Free | Note |
|---|---|---|---|---|
| **bank 40** | **330** | **2,715** | **75** | the item/armour description tables, ~21 instances per line |
| **bank 41** | **33** | **33** | **353** | unique 1355–1387, story text, bank 41 alone |
| bank 5 | **3** | 3 | 1,595 | D518/D519/D520 — the pooled rows in NEXT ACTION's qualification |

⭐ **So 363 of 366 lines and 2,748 of 2,751 instances — 99.9% of what is left — sit behind the ONE
task at the top of the human list: the §F2 bank-40/41 repoint.** Everything else is rounding.

## Blocked — needs a human, IN PRIORITY ORDER
### 1. 🔧 THE `tokenise` ARGUMENT-LENGTH TABLE — cheapest real win, repo-only, unblocks 10 chunks
`FLAGS.md` **§D1, §R, §AP2, §AY2**. Needs **no disc, no EXE, no emulator** — unlike everything below.
The dumper prefers a Shift-JIS text run over a control tag whenever an argument byte is a valid lead
byte, so an item id plus the *next tag's* lead byte decodes as a kanji. **24 occurrences across 10
chunks** — `{FC70}` in 5, 16, 17, 23, 39 and `{FCA8}` in 15, 27, 28, 29, 32 — and each makes `check`
**unsatisfiable** for that chunk: the dump form passes tag parity and fails charset; every re-tokenised
form does the reverse. **Chunk 17 is finished, faithful, format-clean and 2,335 bytes UNDER its slot,
parked for this reason alone.**
⚠️ **THE BUG IS IN BOTH TOOLS AND HAS TWO DISTINCT SYMPTOMS — established across waves 10 and 12:**
- `riotbattle.py` and **`riotscript.py:tokenise_stream` (lines 61–83)** both test `is_sjis_lead(c)`
  **before** the tag branch and **have no argument-length table.** A fix to one leaves the other.
- **§R4/§AP2's script instance (D367) is the SJIS-LEAD branch.** **§AY2's `{FF00}` at D1003 is the
  CONTROL-TAG branch** — `is_sjis_lead` **excludes `0xFF`**, so after `{FFF3}` the loop meets `0xFF` in
  the `0xfb <= c <= 0xff` branch and emits `{FF00}` from an **argument byte**. Census 1 unique / 6 dump
  / 0 battle; **zero shipping impact**, proved from the encoder's grammar.
- ⚠️⚠️ **THEREFORE A LEAD-BYTE REORDER FIXES NEITHER SYMPTOM. It must be an ARGUMENT-LENGTH TABLE —
  and ONE table serves both branches in both tools.**
Then `assemble.py refresh`; chunk 17 unparks with a `git mv` plus a **0-byte** re-tokenisation of one tail.

### 2. ⭐⭐ THE BANK-40/41 REPOINT (§F2) — by far the biggest lever left
`FLAGS.md` **§F2**, figures refreshed **§Z6**. About **66 KB short**: bank 41 needs +30,534 with **353**
free, bank 40 +20,924 with **75**, bank 5 +14,720 with **1,595**, bank 2 +12,798 with **1,607**, bank 33
+11,492. **Unblocks 363 unique lines / 2,748 instances — 99.9% of everything still untranslated.**
Needs a MAIN1.EXE repoint or a bank-spill scheme. **Policy this run:** bank 40's spendable budget goes
to the 21-instance item table (~840 instances), not its own story text (~25 instances). Reversible, but
the arithmetic is not close.
⚠️ **THREE THINGS COME DUE THE MOMENT BANK 40/41 OPENS, and each is written down so nothing is lost:**
- **D1169 `音楽のＯＮ・ＯＦＦを切り替えます` contains `・`, which §3.1 FORBIDS** (§AY5/§AZ7). **No existing
  precedent covers it** — wave 12 ruled `・` → `，` only for *apposition* (§64/§AZ), which does **not**
  reach `ＯＮ・ＯＦＦ`. **First known case of illegal source punctuation inside still-blocked text.**
- **D1332 is readable-identical to the shipped D320** and **D1384 must take §37.1's script-store
  `ｒｅｂｅｌｌｉｏｎ`**, not the battle store's `ｒｅｖｏｌｔ`. Both differ from their shipped twins only in
  tag stream, **so gate 6 is blind to them** — reuse the shipped English byte-for-byte.
- **§42.5's forward-binding table still holds two live rows: `505` → D535 and `506` → D403.**

### 3. 🔧 `assemble.py:validate_body` CHARSET WHITELIST — chunk 36, repo-only
`FLAGS.md` **§AF1**. The charset whitelist is applied to **preserved SOURCE machine text**. Chunk 36 is
mostly a full-width MIPS listing, English machine output and a garbage block, all of which must survive
byte-for-byte; **38 characters are rejected** (`＄`×14 `＞`×10 `＿`×4 `＃`×4 `｜`×3 `ケ` `あ` `「`) and **not
one is on a translated run.** Measured at the PR #25 review: pristine chunk raises **193** problems, the
delivered translation **38**, all charset, **0 tag-parity / 0 column / 0 byte**. `pending/chunk_036.txt`
is finished and **5,305 bytes UNDER its slot**. Fix: **one function** — skip the charset check on runs
byte-identical to the dump. ⚠️ **Widening `ALLOWED` alone is INSUFFICIENT — the garbage block contains
kana** (`ケ`, `あ`), and blanket-allowing kana would disable the gate that catches untranslated Japanese.
Afterwards, unparking is `git mv pending/chunk_036.txt tl/battle/chunk_036.txt` and nothing else.
**986 JP characters — 2.3% of the battle script — are finished and waiting on it.**

### 4. Tier-A battle chunks 5, 16, 32, 43 — needs EXE + disc + emulator
Ratios 1.53 / 1.59 / 1.61 / 1.23, all below the **1.64× floor** (§B2); no faithful translation fits
8,192 bytes. **5 and 43 are translated and parked.** Fix: the engine patch in
`pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script buffer).
**§B3 recommends settling KOUSEI.EXE first and confirming the floor on ONE of 16 or 32, not both.**

### 5. 🎮 Two in-game visits that settle four open questions between them
- **The nine tutorial screens** (Blocked 8, §AO1–AO3). `batch_013.tsv` adds one `{FFFE}` to each of
  DATA 958–963, 968, 969, 970 because `assemble.py`'s column model does not split on `{FFFA}`/`{FFF7}`/
  `{FFF6}`. **Open the tavern tutor, walk lectures 1–6, look for a blank first row or a misaligned
  cursor gutter.** ✅ **Jump targets are NOT at risk** — `{FFF6}` arguments are **message indices within
  the bank**, not byte offsets (verified at review). **If it looks wrong the fix is one regex and zero
  bytes.**
- **The Formation screen** (§Z1 / Blocked 7) and **one shop visit** (§C4 / §Y1). `batch_007` ships three
  `『』` UI labels as instructions to find menus whose strings are **in neither dump**. ⚠️ **Wave 12
  established that §AQ5's `編成` "inconsistency" was a FALSE POSITIVE of its own gate and closed it —
  but that answers only the consistency question, NOT whether the labels match the screen. §Z1 stays
  open.** At the shop, enter the **longest legal 7-character name** and buy the longest-named item:
  `{=00}{=01}` price and `{=00}{=03}`/`{=00}{=04}` name inserts are **gate-blind** (12 rows in
  `batch_006`, 6 in `batch_007`, each **bounded** at insert+8), and **49 rows across 15 files** put a
  character straight after `{FC00}`.
- ⭐ **`FLAGS.md` §L2 / `findings.md` §24** — eight lines carry **no `{FC50}`/`{FC51}`** yet exceed four
  text rows, worst **chunk 32 L31 at 59 rows**. A 59-row page cannot exist, so the prediction is **pools
  of independently-selected strings** with `{FC03}` as selector. **One visit to the chapter 5 church map
  and chapter 6 settles it, and §D3 with it.** ⭐ **Wave 12 found direct corroboration in the script
  store: D518/D519/D520 are exactly such pooled rows** (1,184 / 745 / 850 JP chars, multi-scene, one
  opening with a ruler string).

### 6. Binaries and play-test
Put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run `python3 tools/assemble.py all` (real `checkedit`),
rebuild the disc, play-test. **`original/` is gitignored and absent from clones, so `build` cannot write
`.BIN` files and `riotbattle.py checkedit` cannot run in an agent container. That is expected, not a defect.**

### 7. Enable "Automatically delete head branches" — kills a permanent false signal
Branch deletion returns **HTTP 403** from every agent container (§AQ9), so ~45 merged `tl/*` branches
linger and "branch still exists" has been a misleading signal for twelve waves.

### 7b. 🖥️ The main-script text box is NOT yet widened (MAIN1.EXE) — a standing note, not a blocker
Translate to **24 columns anyway**; `riotfont.py rewrap` re-flows later if the box is widened. This has
been true and harmless for twelve waves; it is recorded so nobody "discovers" it as a defect.

### 7c. ⚠️ If the run RESUMES, watch the session lineage cap — it killed the chain once
`FLAGS.md` **§Z/Blocked 0b (waves 9–10).** Every wave ran as a child session of the previous one and the
platform caps that at **lineage depth 8**. At the cap, `send_later`, `create_trigger` and `create_session`
all return `caller session is at lineage depth 8 (limit 8)`, so that wave ran **without a watchdog and
could not open its successor.** ✅ **Fixed by a human opening the next wave as a fresh TOP-LEVEL session**,
which resets depth to 0. ⚠️ **The in-run fallback — an `orchestrator` subagent — WORKS BUT IS DEGRADED:
subagents cannot spawn subagents, so such a coordinator has no reviewer and self-reviews its own merges
(wave 1's failure, four merges).** **Prefer the human action; it is strictly better and nearly free.**
**Wave 12 ran as a top-level session and hit none of this** — `Task`, `send_later` and `create_session`
all worked, and the three-role split held for all four units.

### 8. 📄 `SKILL.md` §3 edit (small)
Scratch-file namespacing must bind **every** role, not just translators — a **reviewer's** script was
overwritten mid-task in wave 4 and caught only because the output was visibly the wrong unit's data.
Add: every agent namespaces every scratch file, and no agent trusts a scratch script it did not write
in the same turn.

## Decisions this run
### ⭐⭐ WAVE 12's LESSONS — the gate-7 hole is now fully mapped, and it has THREE faces
**Detail lives in `glossary.md` §61–§64 and `FLAGS.md` §AW–§AZ, not here.**
1. ⭐⭐ **GATE 7 HAS THREE FACES AND ALL THREE ARE NOW MANDATORY.** **(a) key cells** · **(b) NOTE
   cells** — wave 11's `さ、` had **0 first-column keys and 2 note-cell mentions**, so a key-first gate 7
   saw 0 of 2 and only the reading review caught a real collapse · **(c) ⭐ NEW: forms SHIPPED IN `tl/`
   THAT THE GLOSSARY NEVER RECORDED AT ALL** — **`その他` had 0 mentions of any kind, key or note, yet
   shipped 7× in `batch_013`.** **Face (c) defeats any glossary-side harvester however good, so gate 7
   needs a `tl/` COLUMN-2 PASS.** ⚠️ **It paid for itself on first use:** at PR #45 a pass over 2,893
   aligned JP→EN segment pairs found that `立ち寄る` → `ｃａｌｌ　ｉｎ` **over-reached and would have
   invalidated shipped work** (`batch_014.tsv:36` already ships `ｄｒｏｐ　ｉｎ`; §25.3 met on disjoint
   banks, so both stand and the key was narrowed). PR #46's pass covered **3,573 pairs / 2,949 distinct
   JP segments, 71 hits, 0 divergences**, and found `「古びた館」` → `“Ｏｌｄ　Ｍａｎｓｉｏｎ”` standing
   beside a shipped lowercase `ａｎ　ｏｌｄ　ｍａｎｓｉｏｎ` — **nothing else could have.**
   `その他` is now a first-column row (§64).
2. ⭐⭐ **HOW TO HAND-MEASURE COLUMNS — `assemble.py:106` SPLITS RUNS ON `{FCC0|FC30|FC51|FC50|FFFF}` AS
   WELL AS `{FFFE}`.** **A `{FFFE}`-only split CAN OVERSTATE COLUMNS.** PR #43's reviewer caught its own
   near-miss exactly that way: **27 columns reported, true rows 14 / 15**, because a `{FCC0}` sat inside
   the segment. ⚠️ **Also `rowcheck.py:_script_cols` expands only `{FFEC}{=00}{=00}` and `{FC00}` (to 7)
   and strips EVERY other insert to ZERO columns** — insert-bearing rows are **bounded, not measured**.
3. ⭐⭐ **ASSUME EVERY REACH FIGURE IN THIS REPO IS A RAW SUBSTRING COUNT UNTIL SHOWN OTHERWISE.** Three
   substring false positives in one wave: §34.1's `品` (inflated by `商品`/`景品`/`作品` — bare noun is
   **8 instances / 5 banks**, not 44 / 23) · `ｍｏｂ` (inside `ｍｏｂｉｌｅ`/`ｍｏｂｉｌｉｔｙ`) · `ＯＰ`
   (inside `＞ＯＰＥＲＡＴＩＯＮ`). Plus five more reach figures re-run and corrected at PR #44.
4. ⭐ **READ EVERY `{FFFE}` SEGMENT OF A POOLED ROW.** Two findings this wave came only from doing it —
   `品` in **segment 16** of a 25-segment row, and a `マップクリアー` incumbent in **segment 19** of a
   29-segment row. **I made the opposite mistake and it cost a false "no defect here".**
5. ⭐ **CITATION ADDRESSING — FIVE FACES NOW, AND THREE CONVENTIONS COEXIST IN `glossary.md` TODAY.**
   0-based vs 1-based; body index vs file line; and ⭐ **NEW: a line citation goes STALE THE MOMENT THE
   FILE ABOVE IT IS EDITED** — my own 65-line seed insert at line 866 silently moved every citation
   below it (`:6815`→`:6880`, `:4525`→`:4590`, `:3883`→`:3948`). **CITE BY SECTION, NOT BY LINE.** State
   for every number whether it is a 0-based index or a 1-based file line.
6. ⭐ **QUOTE DELTAS, NOT ABSOLUTES, IN A PR BODY THAT MAY SIT THROUGH ANOTHER MERGE.** Both debug PRs'
   absolute bank figures went stale by 28 bytes between authoring and review; **both deltas were exact.**
7. ⚠️ **EIGHT COORDINATOR ERRORS, ALL MINE, ALL CAUGHT BY TRANSLATORS AND REVIEWERS.** Miscounted
   `ｒｅｂｅｌｌｉｏｎ` as 10 columns (it is **9**, and my "+8 / 21→25 / needs a re-wrap" was wrong on all
   three counts) · a **case-sensitive** `Ｈｅｙ，` grep that wrongly cleared a chunk carrying lowercase
   `ｈｅｙ，`, "correcting" an inherited citation that was right · judged a **pooled 25-segment row from
   its head** · a `てーこく` cell wrong in **all three** figures whose "sets precedent" claim was false
   (wave 2 set it) · named **three** near-duplicate traps when §42.5 already held a **fourth** · a
   `フラグ`/`その他` attribution backwards · a **0-based body index that propagated into a translator's
   flag** · and ⭐ **relayed another agent's width table verbatim — wrong on 18 of 22 rows.**
   ⚠️⚠️ **THE SHARPEST LESSON OF THE WAVE: `batch_021`'s PROSE REPORT and its COMMITTED FILE disagreed
   on a width (23 vs 21). I relayed the report. THE FILE IS THE AUTHORITY — a relayed measurement is not
   a measurement, and a *reported* measurement is not one either.** ⚠️ **I also diagnosed the stale-line
   -citation bug mid-wave and then left the broken pointers in my own seed until a translator found them.
   Diagnosing a defect and not applying the fix to your own text is worse than not noticing it.**
8. ✅ **QUALITY CONTROL RAN IN BOTH DIRECTIONS, AS IT MUST.** Every one of my eight errors was caught by
   a subordinate agent. Reviewers corrected translators' figures (three of `batch_021`'s, five of
   `batch_022`'s) and translators corrected mine; **`batch_022` withdrew its own title-case draft** when
   its counter-evidence pointed at the other answer; **PR #43's reviewer disclosed a near-miss of its
   own**; PR #45's translator **disclosed that nine glossary sections were covered by key sweep rather
   than by eyes.** ⭐ **Better solutions than the ones I briefed came back twice:** the `反乱` fix took
   its article from an already-shipped sibling instead of inventing a third wording, and `batch_022`
   abbreviated only the menu row where I had said the full form must go.
9. **Rulings made this wave, all one-per-wave and binding:** ⭐⭐ **descriptive labels take SENTENCE
   CASE, title case only for a named thing or a §9-seeded label form** (§63.1/§AY3) — decided on §56.2's
   **eight sentence-case gutter menu labels**, which put §17.1's "capitalised throughout or not at all"
   back where it belongs (the class-name table) · **§AQ5's `編成` closed as a FALSE POSITIVE of its own
   gate**, for free and without the disc · **`Ｏ，　Ｏｉ，` stands** — §AJ3 argued lowercase by analogy to
   a *word doubling* when this is a *fragment stutter* (**23 : 6 capitalised** vs **7 : 0 lowercase**) ·
   the single **24-column** run ships (§64.3/§AZ3) · **`・` → `，` for apposition only**, which does
   **not** reach D1169's `ＯＮ・ＯＦＦ`.

**Standing (waves 4–12).** Integration branch is **`main`** — it was `claude/workflow-translation-iterate-uzlkns`
with `main` untouched until 2026-09-11, which hid the whole run; see the top of this file and `CLAUDE.md`. Script growth for planning **2.10×**; ⚠️ **realised across wave 12 was 1.66×–1.98×, so quote
the planning bound and the realised figure as TWO numbers, never one.** Seed the glossary **before**
dispatching. A **parked unit still gets the full reading review**. Name script batches by **DATA line
list**. A term is "in the glossary" only if a row **fixes an English form**. Section numbers are taken by
**READING both files at commit time**, never reserved. **Runtime name/unit inserts take singular *they***
(§58/§AT4). **Battle `tl/` holds NO Japanese, so grepping it is a null check** — pair the battle dump
positionally (⚠️ **I made this mistake myself in wave 12 while checking a battle citation**). **Gate 6
pairs whole messages on exact Japanese**, so a kana variant, a sub-message term or a sibling differing
only in a tag argument is **structurally invisible** — wave 12's twin units shared **30 readable strings**
differing only in a trailing `{FFF8}` argument and **gate 6 reported clean while seeing nothing.**
**`{FCC0}` is forbidden by `assemble.py:tag_parity`, not `rowcheck.py`** (§Q2). **No gate needs a working
tree**; **pin the merge base to an explicit SHA** and **never reuse an author's `merge-tree` result** —
by wave 12's last review the base had moved through three merges. **Never infer merge state from an
agent's status**: reviewers merge *and* push `integrate:` while still showing "running", and **branch
deletion returns HTTP 403** (§AQ9). A rejected non-fast-forward push is the **mid-integration signal**:
hold, re-fetch, re-apply, **never force**. **`build/*_dump_merged.txt` is committed at WAVE CLOSE only** —
pushing it mid-review risks colliding with a reviewer's integration push. **GitHub REFUSES
`REQUEST_CHANGES` in this repo** (§AQ1): reviewers post a COMMENT review with `DECISION:` on line 1, and
an absent REQUEST_CHANGES is **never** approval. **Settled conventions, never findings:** DATA vs FILE ·
0-based vs 1-based · the gutter census · §45.2's `.TTTT.` is BATTLE-scoped · **breaks vs segments** are
two conventions over identical data · gate-7 key counts vary with splitter and struck-row handling —
**state your corpus.**

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle 23/44 (43.2%); script 311 (52.5%) |
| 6 | battle 24, 25, 26 + script 008 | **4** | 0 | battle 26/44 (51.0%); script 358 (53.1%) |
| 7 | battle 30, 31, 36 + script 009 | **3** | **1** | battle 28/44 (56.5%); script 408 (53.7%) |
| 8 | battle 37, 38, 41, 42 + script 010 | **5** | 0 | battle **32/44 (64.3%)**; script 461 (57.4%) |
| 9 | script 011, 012, 013 (**script-only — battle exhausted**) | **3** | 0 | battle 32/44; script 640 (59.7%) |
| 10 | script 014, 015, 016 (DATA 707–869) | **3** | 0 | battle 32/44; script 803 (61.7%) |
| 11 | script 017, 018, 019 (DATA 1100–1159, 1388–1430, 465–879) | **3** | 0 | battle 32/44; script 948 (63.6%) |
| **12** | **script 020, 021, 022 + corrections** (DATA 318/320/326–345, 997–1034, 1043–1099) | **4** | **0** | battle 32/44 (64.3%); script **1,064 (65.3%)** — ⭐ **ALL FOUR MERGED AT ROUND 1; the run's feasible queue is now EMPTY** |

**Wave 12 detail.** PRs #43–#46, **4 merged / 0 parked / 0 lost / 0 re-dispatches**, and — a first for
the run — **all four merged at ROUND 1 with no must-change finding.** Four separate reviewers, the
three-role split intact throughout, so **no unit is SELF-REVIEWED and there is NO audit debt.** Realised
growth **1.66×–1.98×** against the 2.10× plan, so every unit came in **under** its bound (bank 30 **456**
vs 782; bank 31 **1,724** vs 2,185; bank 5 **40** vs 94). Translators ran 27–53 min, reviewers 33–39 min.
**Four flags retired (§AJ3, §AP5, §AP7, §AQ5) and one closed as a false positive of its own gate.**
Detail lives in `glossary.md` §61–§64 and `FLAGS.md` §AW–§AZ.

## How to resume
1. `git fetch && git reset --hard origin/main` (a plain `checkout` can land on a stale shallow ref —
   see the top of this file), then `python3 tools/assemble.py check`.
2. ⛔ **DO NOT open another wave to look for translation work — there is none, and NEXT ACTION shows the
   measurement.** The queue is empty at the run's standing 2.10× planning rate; the only qualification is
   the two marginal pooled rows named there, which are a policy call, not a unit.
3. **The work is the human list under "Blocked — needs a human", in that order.** Items **1** and **3**
   need **nothing but the repository** — no disc, no EXE, no emulator — and between them unblock **11
   battle chunks**. Item **2** unblocks **99.9% of all remaining script text.**
4. **When a blocker clears, the loop still works**: start a fresh session on this branch and run
   `/translate`. The chain, the wave barrier, the three-role split and every gate are unchanged — the
   only thing that stopped is the supply of feasible units.
