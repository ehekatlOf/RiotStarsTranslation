# HANDOFF — live board for the Riot Stars translation

Read this first. Update it after every step (rules: `CLAUDE.md` §7). A fresh session resumes
from this file plus the open PR list; nothing else is required.

## Last updated
2026-09-08 · by: workflow bootstrap (no translation done) · wave: none yet ·
queue: **stale — the survey pass has not run.** First action for the orchestrator: `/translate`.

## Progress (`python3 tools/assemble.py status`, 2026-09-08)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 10 | 44 | 0, 7, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 5,963 | 43,161 | 13.8% |
| Script unique lines | 151 | 1,430 | `tl/script/batch_001–003.tsv` |
| Script message instances | 3,299 | 7,931 | 41.6% |

`check`: All checks passed. Tightest banks (`bankmeasure`): 41 → 353 free, 40 → 1,771,
5 → 4,681, 2 → 8,805; every other bank ≥ 10,000 free.

## In flight
| Unit | Tier / ratio | Agent | Branch | PR | Status | Round | Next actor |
|---|---|---|---|---|---|---|---|
| (none) | | | | | | | |

## Next up (proposed wave 1 — confirm in the survey pass)
| Unit | Tier | JP chars | Headroom | Ratio | Note |
|---|---|---|---|---|---|
| battle chunk 1 | D | 719 | 6,151 | 5.28 | chapter after chunk 0; geometry, not bytes, is the constraint |
| battle chunk 2 | C | 1,140 | 4,911 | 3.15 | |
| battle chunk 3 | D | 870 | 5,617 | 4.23 | |
| script batch 004 | — | — | — | — | highest-count untranslated lines whose banks have room; the orchestrator assigns the exact `script_unique.txt` line list |

## Remaining (dispatchable) — figures from `translation_prompt.md` §0.3; re-verify against the dump
Battle, 30 chunks, in chapter order (tier, ratio):
1 (D 5.28), 2 (C 3.15), 3 (D 4.23), 4 (D 5.08), 6 (C 3.09), 8 (B 2.32), 9 (D 4.93), 13 (C 3.41),
15 (D 6.13), 17 (C 3.19), 18 (D 6.28), 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59),
23 (C 2.80), 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 27 (D 5.54), 28 (D 4.76), 29 (D 6.03),
30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 39 (D 6.20), 41 (D 6.53), 42 (D 5.46).

Script: 1,279 untranslated unique lines (4,632 message instances). Bank membership is **not yet
computed** — the survey pass must map each line to its banks and mark bank-blocked lines
(FLAGS §F2 projects banks 41, 40, 5 and 2 about 66 KB short in total).

## Blocked — needs a human
1. **Tier A battle chunks 5, 16, 32, 43** (ratio < 1.6) do not fit 8,192 bytes at any faithful
   density (FLAGS §B; measured floor 1.64×). 43 and 5 are translated and parked in `pending/`.
   The fix is an engine patch: `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words plus
   relocating the 8 KB RAM script buffer) gives chunk 43 a 16 KB slot. Only chunks 24, 28 and 43
   have free space below their slot, so 5, 16 and 32 need a further decision. Needs the EXE, the
   disc image and an emulator.
2. **Main-script bank capacity** (FLAGS §F2): banks 41, 40, 5, 2 cannot hold a complete
   translation. Lines landing in a full bank are parked in `pending/script/` until a MAIN1.EXE
   repoint or bank-spill scheme exists.
3. **Main-script box not yet widened** (MAIN1.EXE side). Translate to 24 columns anyway;
   `riotfont.py rewrap` re-flows later.
4. **In-game checks**: FLAGS §D2/§D3 (pages over 4 rows), §D4 (is line 1234 reachable), §F6
   (description window 3 or 4 rows), §C4 (`{FFEC}` variant widths), `findings.md` menus and
   name-entry first test.
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. **Chunk 5 dump artifact** (FLAGS §D1): dumper fix plus re-dump; needs `original/`.

## Decisions this run
- 2026-09-08: workflow bootstrapped — `CLAUDE.md`, `.claude/agents/translator.md`,
  `.claude/agents/reviewer.md`, `/translate` skill, `.github/pull_request_template.md`, this file.
  No translation was produced or changed.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| — | | | | |

## How to resume
1. `git checkout main && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file; list open PRs; reconcile the In flight table with reality.
3. `/translate` — runs preflight, then the survey if the queue is stale, then the loop.
