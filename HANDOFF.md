# HANDOFF — live board for the Riot Stars translation

Read this first. Update it after every step (rules: `CLAUDE.md` §7). A fresh session resumes
from this file plus the open PR list; nothing else is required.

## Run configuration — READ BEFORE BRANCHING
**The integration branch for this run is `claude/workflow-translation-iterate-uzlkns`, not
`main`.** The session that owns this run may only push there. It starts at the same commit as
`origin/main` (`dabdeae`), so the tree is identical. Everywhere `CLAUDE.md`, the `translate`
skill and the agent files say `main`, read `claude/workflow-translation-iterate-uzlkns`:

- translators: `git fetch origin claude/workflow-translation-iterate-uzlkns` and branch from it;
- PRs: `base = claude/workflow-translation-iterate-uzlkns`;
- reviewer: `git push origin integrate:claude/workflow-translation-iterate-uzlkns`.

The human fast-forwards `main` from this branch when the run is done. Nothing else changes.

## ⚠️ OWED: wave-1 audit findings — dispatch as a follow-up unit
**`audits/wave-1-audit.md`** (committed `aee737a`) is the independent post-merge reading review of
wave 1, run because wave 1's coordinator had no `Task` tool and reviewed its own four PRs.

**Verdict: no must-fix on any translated line.** The translations are sound — nothing invented,
nothing dropped, gates clean, no regressions from the rework rounds, zero unspaced `，` left in
`tl/`, zero divergent duplicate keys.

**But 1 must-fix and 6 should-fix are outstanding**, and they are owed by a wave session as a
follow-up unit — translator → PR → reviewer like anything else. The doc corrections (findings 1,
2, 6, 7) are reviewer/integrator work and can ride an integration commit; the line edits (3, 4, 5)
need a translator and a PR. Do not apply them from a session that is not running a wave.

The sharpest one, because it shows what self-review costs: **`FLAGS.md` §J1 justified accepting
batch 004's 2.23× compression with arithmetic that PR #4's own Flag 3 contradicted on the same
page.** True cost of restoring the dropped clause is 192 bytes, not 252; bank 40 would land at
**317 free, not negative**; **nothing would have been parked**. The "seven Japanese holes in a
table" justification was false, and §J1 also wrongly states the PR failed to flag the departure.

## NEXT ACTION — always current, always a literal instruction
> **Wave 2 is IN FLIGHT. Its session — `session_01JDoA8KzwUVk3ZjiBw8Qkf3`, "Riot Stars — wave 2" —
> owns the repository and is the active driver. Preflight passed 2026-09-08: `check` green, zero
> open PRs, zero stale worktrees.**
>
> The literal next act is: **wait for the four translators, hold the wave barrier, then review one
> PR at a time in unit order** (chunk 4 → 6 → 9 → script 005). See **In flight** for live state.
>
> Wave 2 has `Task`: it is running the proper three-role split (translator / reviewer subagents),
> so wave 1's spawn constraint below does **not** apply to it.
>
> **When wave 2 closes it opens wave 3's session itself** (SKILL.md §6a; `create_session` needs
> **both** `source_url` and `source_revision`). If this session is dead or stalled — check by
> listing open PRs against this branch and reading In flight — the chain is broken and whoever
> notices should re-open the wave. The chain ends only on one of CLAUDE.md §8's four conditions.

## Last updated
2026-09-08 · by: **wave-2 coordinator** (`session_01JDoA8KzwUVk3ZjiBw8Qkf3`) ·
wave: **2 DISPATCHED, 4 units, 0 returned** · queue: **fresh (survey ran 2026-09-08)**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 13 | 44 | 0, **1**, **2**, **3**, 7, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 8,692 | 43,161 | **20.1%** |
| Script unique lines | 185 | 1,430 | `tl/script/batch_001–004.tsv` |
| Script message instances | 4,013 | 7,931 | **50.6%** |

`check`: **All checks passed** on the integration branch. Tightest banks (`bankmeasure`, measured
after batch 004): **41 → 353 free, 40 → 509, 5 → 3,419**, 2 → 7,543, 33 → 9,353; every other bank
≥ 10,300. Bank 40 is spent — see `FLAGS.md` §J2.

## In flight — WAVE 2, dispatched 2026-09-08

Four translators, all `run_in_background`, each in its own worktree, branching from
`claude/workflow-translation-iterate-uzlkns`. **Wave barrier: review nothing until all four have
an open PR.** Review order when the barrier is met: chunk 4 → chunk 6 → chunk 9 → script 005.

| Unit | Branch | Tier / budget | Round | PR | State |
|---|---|---|---|---|---|
| battle chunk 4 | `tl/battle-004` | D, 642 JP ch, ratio 5.08 | 1 | — | dispatched |
| battle chunk 6 | `tl/battle-006` | C, 1,014 JP ch, ratio 3.09 | 1 | — | dispatched |
| battle chunk 9 | `tl/battle-009` | D, 686 JP ch, ratio 4.93 | 1 | — | dispatched |
| script batch 005 | `tl/script-005` | 26 lines / 26 inst, 1,770 JP ch | 1 | — | dispatched |

**Measured at dispatch (corrections to the wave-2 plan as written by wave 1):**
1. **Batch 005 spans banks 29, 30 and 31 — not 30 and 31.** Lines 984–988 (the five tutorial
   boxes) are resident in **bank 29**, 989–1001 in bank 30, 1040–1047 in bank 31. Free:
   **29 → 27,323 · 30 → 36,671 · 31 → 35,581**. All roomy; at the measured 2.10× growth the batch
   needs ~3,700 bytes spread over three banks. No bank pressure.
2. **The corrected range is confirmed clean**: 26 lines, 1,770 JP characters, 26 instances (all
   1-instance), and `grep -E 'フラグ|：新曲|^[０-９]{2}：|鑑賞モード'` over it returns **nothing**.
   The 89 debug lines are excluded as planned.
3. **No re-seeding was needed.** Every proper noun in all four units is already fixed by
   `glossary.md` — §1/§2 for the decided ones, §9 "Wave 2 seeds" for the rest. Checked all 20.

**Three cross-unit decisions routed to the translators, to be ratified by the reviewer:**
- **`ファリーナ` is a PLACE** (§1 files it under People). Chunk 6 `ファリーナの南、カペラの村`;
  script 1046–1047 `ファリーナの復興`, `ファリーナで発見された`. The rendering `Farina` is
  unchanged — only the classification is wrong. Both PRs flag it; the reviewer moves the row.
- **Fernando's title** (glossary §10 open question 2). `隊長` → captain is fixed (§2) and chunk 2
  shipped `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ`; script 992 reads `２軍のフェルナンド将軍`. Batch
  005's translator is instructed to render `将軍` → **`Ｇｅｎｅｒａｌ`** (two distinct ranks, the
  higher fitting the man who leads the 2nd Royal Army) and to flag it as settling §10.2.
- **`リオン` → `Ｌｅｏｎ`** (§9 wave-2 seed) settles **§10.1**, and also makes the stale
  "unresolved — Lion or Leon" row in §1 wrong. Chunk 6's PR flags both for the reviewer.

### ✅ DONE: the wave-1 reading-review audit — **the four units stand as merged**

`CLAUDE.md` §8, as amended by wave 1's session in commit `16c179e`, required an **independent
post-merge audit of the reading review** for wave 1's four self-reviewed units before the next
wave dispatches. **Wave 2 ran it** — a read-only subagent, in parallel with the wave, writing
nothing to the repo and returning findings. Full report: **`audits/wave1-reading-review.md`**.

**Verdict: chunks 1, 2, 3 and script batch 004 stand as merged. No correction commit is required
before wave 3 dispatches. The requirement is satisfied.** Nothing found changes a plot fact, drops
a clause, mixes a tic, breaks a gate, or renders identical Japanese two ways. Gates were re-run
independently and all pass. The audit's duplicate scan across all 13 shipped battle chunks found
**zero divergences inside the audited units**.

Wave 1's session claimed an audit was "running" but was IDLE, and any subagent of it reports into
*its* context, not this one — so wave 2 ran its own rather than trusting silence as evidence.

**Backlog this created — housekeeping, none of it blocking:**
- **8 proposed file edits** (MINOR: one pragmatic mistranslation, two dropped modifiers, a
  garden-path break, a compound-noun split, three idiom fixes). All verified to fit — every row
  ≤ 23 columns; the four `batch_004` edits cost 38 bytes total in bank 40 (509 → **471** free).
- **6 glossary/FLAGS rulings that are the durable half.** Three are **live in wave 2 right now**:
  `しかし` (no entry, two shipped forms, one of which — `Ｓｔｉｌｌ，` — is §19.1's fixed form for
  それにしても; **chunk 6 ×1 and chunk 9 ×2, verified by this coordinator**), `助かった`
  (chunk 4 ×1), and `愛用` (13 instances still untranslated, three shapes shipped).
- **One live `CLAUDE.md` §3 violation in *earlier* shipped work**, independently verified:
  `村が襲われました。` (13 dump instances) is `ｉｓ　ｕｎｄｅｒ　ａｔｔａｃｋ` in `chunk_007` but
  `ｈａｓ　ｂｅｅｎ　ａｔｔａｃｋｅｄ` in `chunk_034`. Predates wave 1. Cheap fix: change
  chunk 34 (6,601 slack) to chunk 7's wording; chunk 7 has only 399 slack, leave it alone.

**Who acts:** the **reviewer** rules on the glossary items in its integration commits — `しかし` in
particular is a genuine tradeoff (chunk 3 also ships でも → `Ｂｕｔ`, and chunks 4/6/9 each carry
でも ×2, so collapsing them is a deliberate choice), which is the reviewer's call under §6, not the
coordinator's. **The coordinator deliberately did NOT interrupt the four live translators over it**
— the risk of destabilising four healthy mid-draft units outweighed pre-empting a divergence the
reviewer catches anyway, and rework rounds exist for exactly this. The 8 file edits and the
chunk-34 fix ride in one housekeeping commit at wave close or later.

> ## ⏰ A WATCHDOG TIMER MUST BE ARMED AT ALL TIMES
> The main session wakes only on a notification or a human message. Wave 1 stalled once because a
> turn ended with nothing scheduled. **Before ending any turn with work in flight, arm a
> `send_later` watchdog (10–15 min) and re-arm it on every wake** — CLAUDE.md's second banner and
> SKILL.md §6b. Handing the wave to an `orchestrator` subagent is *additional* to the timer, never
> instead of it. A subagent whose notification never arrives is **lost, not finished**:
> `ListAgents` is the authority, silence is not evidence.

### ⚠️ The spawn constraint — read before planning any wave

The session that ran wave 1 had **no `Task` tool** and no `ListAgents`: it could not spawn a
translator, a reviewer, or a successor orchestrator. Discovered mid-wave, when the first reviewer
dispatch was refused.

**What was done, and why.** CLAUDE.md §8 lists four stop conditions and "cannot spawn subagents"
is not one of them. So that session ran all four reviews itself under the identical §6 contract —
a real checkout, every mechanical gate executed and its output pasted into the PR review, the full
line-by-line reading against the Japanese, one PR at a time, integration commits serialised. **What
was lost is reviewer independence, not gate coverage**: the agent that routed the wave also judged
it. Recorded rather than quietly absorbed.

**If your session has `Task`, go back to the three-role split** — it is the better arrangement and
wave 2's session should use it. The wave-boundary chain does *not* depend on `Task`: it uses
`create_session` (SKILL.md §6a).

### Four tooling facts established in wave 1 — carry these into every future wave
1. **Neither `REQUEST_CHANGES` nor `APPROVE` is possible on these PRs.** GitHub refuses both on a
   PR opened by the same account (`Can not approve your own pull request`), which is every PR here.
   **Every** decision — MERGE, CHANGES, PARK — goes as a **COMMENT** review. Do not retry either.
2. **Squash-merging via the GitHub MCP works** — `merge_pull_request`, `merge_method: "squash"`,
   with `expectedHeadSha`. Put the true post-rework figure in `commit_title`: a PR title written
   before a rework is stale, and the squash title is what lands in history.
3. **The proxy blocks branch deletion** (`git push origin --delete` → HTTP 403). Normal pushes are
   unaffected. The four wave-1 branches are merged but still exist on the remote; harmless, and a
   human can delete them in the GitHub UI. **Do not treat this as the §8 "cannot push" condition.**
4. **`translation_prompt.md` §3.2's "add a `{FCC0}`" escape does not exist for a translator.**
   `assemble.py check` fails with `tag stream changed` — `tag_parity` exempts only `{FFFE}`. A
   translator at the 4-row wall has re-flow and §2.1 only.

## Next up — WAVE 2, ready to dispatch

**Battle: chunks 4 (D 5.08), 6 (C 3.09), 9 (D 4.93).** Chapter order, all tier C/D, no byte
pressure. Glossary seeds for all three are already in **§9, "Wave 2 seeds"** — `Ｌｅｏｎ`
(which settles §10.1), `Ｃａｐｅｌｌａ`, `Ｋａｚａｒｏｖ`, `Ｍａｒｔｉｎ`, `Ｐｅｒｃｉｖａｌ`,
`Ｄｉｅｌ` Empire, `Ｗａｒｗｉｃｋ`, 弓使い.

**⚠️ Script batch 005 — the surveyed range was wrong and is CORRECTED here.**

`Next up` previously read "unique lines 1035–1100 (66 lines, one scene, bank 31)". **It is not one
scene.** Measured line by line: of lines 984–1100, **89 are developer debug scaffolding** — a
sound-test / music-appreciation menu (`０１：インターミッション`, `０７：マップの音楽１`,
`５０：新曲１`…) and a flag editor (`フラグ４をＯＮにします。２章でキエーザ城に入れるように
なります。`) — and only **28 are player-facing**.

**Batch 005 is therefore: unique lines 984–1001 and 1040–1047 — 26–28 player-facing lines,
~1,777 JP characters.** Two coherent groups:

| lines | what | bank |
|---|---|---|
| 984–988 | five tutorial boxes: ZOC, front/rear unit composition, `『ＧＵＥＳＴ　ＵＮＩＴ』`, `「ＥＮＴＥＲ」` points, neutral units and `『説得』` | 30 |
| 989–1001 | fortress-guard and rumour dialogue: the Princess's disappearance, Bernard's church, the Carline–Empire alliance, Helfer's plot | 30 |
| 1040–1047 | the church scene — the priest Batou, Farina's reconstruction, the legend of the **Reese civilisation** and Bishop Creus | 31 |

Both banks are roomy (30 → 36,671 free, 31 → 35,581), so there is no bank pressure either way.

**Do NOT queue the 89 debug lines.** The player never reaches them, they are 1-instance each, and
they would spend bank 30/31 on a sound test. If someone later wants them for completeness they are
a deliberate, separate decision — not wave 2's.

**Do NOT queue more of the item-description table**: bank 40 is spent at 509 free, measured
(`FLAGS.md` §J2). Lines 185–225 must be parked until bank 40 is repointed.

### ⚠️ A survey defect this exposed, which affects every future script wave
`tools/queue.py` groups script lines by **bank residency and adjacency only**. It has no notion of
whether a line is player-facing, so a contiguous run of debug menu text looks exactly like a scene
and is 76% of this neighbourhood. **Every future script batch must be eyeballed for debug
scaffolding before dispatch** — grep the candidate range for `フラグ`, `：新曲`, `^[０-９]{2}：`
and `鑑賞モード`. Worth fixing in `queue.py` as a filter; recorded in `FLAGS.md`.

## Remaining (dispatchable) — measured by `python3 tools/queue.py battle`, 2026-09-08
Battle, **27 chunks / 29,980 JP characters** after wave 1, in chapter order (tier, budget ratio):
4 (D 5.08), 6 (C 3.09), 8 (B 2.32), 9 (D 4.93), 13 (C 3.41),
15 (D 6.13), 17 (C 3.19), 18 (D 6.28), 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59),
23 (C 2.80), 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 27 (D 5.54), 28 (D 4.76), 29 (D 6.04),
30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 39 (D 6.20), 41 (E 6.54),
42 (D 5.46).

Script, from `python3 tools/queue.py script` (growth modelled at **2.10× JP characters — the
measured aggregate of the 151 lines already shipped**, 9,595 EN / 4,482 JP; 500 bytes reserved
per bank):

| | unique lines | instances |
|---|---|---|
| untranslated | 1,279 | 4,632 |
| **fit the banks** (greedy scarcity-weighted allocation) | **903** | **1,631** |
| bank-blocked → `pending/script/` | 376 | 3,001 |

The dispatchable script work in instance order is the **item / equipment description table**
(unique lines 127–330, 21 instances each — every map bank carries a copy). Bank 40 (1,771 free)
is the ceiling on it: about 40–45 such lines in total, so it is being spent deliberately, highest
instance yield first. After that the pool is the 1-instance story text in the roomy banks
(518–1,413, ~53,000 JP characters).

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
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. **Chunk 5 dump artifact** (FLAGS §D1): dumper fix plus re-dump; needs `original/`.

## Decisions this run
- 2026-09-08: workflow bootstrapped — `CLAUDE.md`, agents, `/translate`, PR template, this file.
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns` (see the Run
  configuration section). `main` is untouched and identical to this branch's base.
- 2026-09-08: **survey ran.** Added `tools/queue.py` (planning only; it imports `assemble` and
  `bankmeasure` read-only and changes neither). Battle: 30 dispatchable, 2 newly confirmed
  blocked (16 at 1.59, 32 at 1.61 — both under the 1.64× floor). Script: per-bank greedy
  allocation replaces the blanket "any pressured bank blocks the line" rule, which was costing
  545 shippable instances.
- 2026-09-08: growth factor for script planning set to **2.10×**, measured on shipped work, not
  the 2.0× assumed in the skill. 2.0× was optimistic.
- 2026-09-08: **all three wave-1 cross-PR conflicts settled by the PR #2 reviewer** — ノロ →
  `，　ｎｙｏｒｏ．` (glossary §5 corrected, decided on `riotfont.py`'s comma glyph), おお →
  `Ｏｈ！`, サイクス → `Ｓｙｋｅｓ`. Full reasoning in `glossary.md` §18; it binds every later unit.
- 2026-09-08: **`tl/battle/chunk_000.txt` corrected twice** (`Ｕｇｈ．．．` → `Ｔｃｈ．．．`,
  `Ｙｅｓ．` → `Ｙｅａｈ．`). The first closed a live CLAUDE.md §3 violation against shipped
  `chunk_007.txt`. Chunk 0 is now 8,165 / 8,192 — **27 bytes of slack, the tightest file in the
  project**; see `FLAGS.md` §G1 before any further correction lands on it.
- 2026-09-08: **PR #2 decided CHANGES** (round 1). All eight gates passed; the two findings are
  the two rulings above landing on that PR. 11 respellings, no re-flow.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 10 → 13 / 44 (13.8% → 20.1% of JP chars); script 151 → 185 unique lines, 3,299 → 4,013 instances (41.6% → **50.6%**) |

**Wave 1 detail.** All four merged, none parked, no unit past round 2.
`#2` battle chunk 1 — 3,517 / 8,192, slack 4,675, round 2 (`dddf0ae`).
`#3` battle chunk 2 — 5,839 / 8,192, slack 2,353, round 2 (`f298fe1`).
`#1` battle chunk 3 — 4,601 / 8,192, slack 3,591, round 1 (`1491ccd`).
`#4` script batch 004 — 34 lines / 714 instances, bank 40 → 509 free, round 1 (`b3b2abb`).
Glossary grew by four sections (§19–§22) and 13 seeds were promoted out of §9. `FLAGS.md` grew by
three sections (§H, §I, §J). Every unit's gates were re-run in a real checkout on the moved base.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION at the top says literally what to do next**; list open PRs and
   reconcile the In flight table with reality.
3. `/translate` — preflight, then do what NEXT ACTION says. The queue is fresh.
4. The run is recursive: each wave's `orchestrator` subagent spawns the next wave's orchestrator
   before it returns, so it continues unattended. If NEXT ACTION names a spawn that never
   happened, the chain broke — spawn it yourself and carry on. The only four reasons to stop are
   in CLAUDE.md §8.
