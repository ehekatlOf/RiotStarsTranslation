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

## NEXT ACTION — always current, always a literal instruction
> **Wave 1 is in flight** (battle chunks 1, 2, 3 + script batch 004; four translators dispatched
> 2026-09-08). As each translator returns: record its PR here, commit, push — then **check the
> whole wave against the open PR list. Review nothing until all four units have an open PR**
> (CLAUDE.md §4 step 4, the wave barrier). A unit whose translator returned, died or could not
> push gets a fresh translator for that unit and the barrier waits again; two re-dispatches, then
> park it. Once the barrier is met, run the `reviewer` subagent one PR at a time, in unit order.
>
> **When wave 1 closes, spawn the wave-2 `orchestrator` subagent immediately**
> (`subagent_type: "orchestrator"`, `run_in_background: true`) — units: battle chunks 4, 6, 9 +
> script batch 005 (unique lines 1035–1100, bank 31). Template: `.claude/skills/translate/SKILL.md`
> §6a. Do not stop to ask; CLAUDE.md's top banner and §8 list the only four reasons to stop.
> Every wave orchestrator spawns the next one itself — this line must always name the next spawn.

## Last updated
2026-09-08 · by: orchestrator · wave: 1 dispatched · queue: **fresh (survey ran 2026-09-08)**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 10 | 44 | 0, 7, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 5,963 | 43,161 | 13.8% |
| Script unique lines | 151 | 1,430 | `tl/script/batch_001–003.tsv` |
| Script message instances | 3,299 | 7,931 | 41.6% |

`check`: All checks passed. Tightest banks (`bankmeasure`): 41 → 353 free, 40 → 1,771,
5 → 4,681, 2 → 8,805; every other bank ≥ 8,800.

## In flight
| Unit | Tier / ratio | Agent | Branch | PR | Status | Round | Next actor |
|---|---|---|---|---|---|---|---|
| battle chunk 1 | D 5.28 | translator-1 | `tl/battle-001` | — | dispatched | 1 | translator |
| battle chunk 2 | C 3.15 | translator-2 | `tl/battle-002` | — | dispatched | 1 | translator |
| battle chunk 3 | D 4.23 | translator-3 | `tl/battle-003` | — | dispatched | 1 | translator |
| script batch 004 | — | translator-4 | `tl/script-004` | — | dispatched | 1 | translator |

## Next up (wave 2, provisional)
battle chunks 4 (D 5.08), 6 (C 3.09), 9 (D 4.93) + **script batch 005 = unique lines 1035–1100**
(66 lines, one scene, resident in **bank 31 alone**, 1,372 JP chars, 35,581 bytes free — no bank
pressure at all).

**Correction to the wave-1 note: batch 005 must NOT be more of the description table.** Batch 004
spends about 1,028 of bank 40's 1,771 free bytes; with the 500-byte reserve that leaves roughly
240 bytes, i.e. ~8 more table lines. The item-description table is effectively finished for this
run once batch 004 merges.

Script batches after that, each a single scene resident in a single roomy bank (`queue.py`
groups them; tightest bank free in brackets):

| lines | count | JP chars | bank |
|---|---|---|---|
| 984–1034 | 51 | 1,098 | 30 [36,671] |
| 888–922 | 35 | 2,034 | 28 [34,841] |
| 815–838 | 24 | 1,173 | 21 [36,819] |
| 747–814 | 68 | 3,671 | 20 [29,489] — split into two batches |
| 923–983 | 61 | 4,977 | 29 [27,323] — split into two batches |
| 582–632 | 51 | 1,323 | 12 [11,621] |
| 1104–1138 | 35 | 1,925 | 33 [10,615] — watch bank 33 |

## Remaining (dispatchable) — measured by `python3 tools/queue.py battle`, 2026-09-08
Battle, **30 chunks / 32,709 JP characters**, in chapter order (tier, budget ratio):
1 (D 5.28), 2 (C 3.15), 3 (D 4.23), 4 (D 5.08), 6 (C 3.09), 8 (B 2.32), 9 (D 4.93), 13 (C 3.41),
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

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | — | — | in flight |

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION at the top says literally what to do next**; list open PRs and
   reconcile the In flight table with reality.
3. `/translate` — preflight, then do what NEXT ACTION says. The queue is fresh.
4. The run is recursive: each wave's `orchestrator` subagent spawns the next wave's orchestrator
   before it returns, so it continues unattended. If NEXT ACTION names a spawn that never
   happened, the chain broke — spawn it yourself and carry on. The only four reasons to stop are
   in CLAUDE.md §8.
