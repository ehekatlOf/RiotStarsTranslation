# Riot Stars — English fan translation (Hect, PS1, SLPS-00829)

This file is the contract for every Claude session and subagent working in this repo. Read it,
then read `HANDOFF.md` (the live board), before doing anything else. The translation rules
themselves live in `translation_prompt.md` and `glossary.md`; this file does not repeat them. It
says how the work is split, gated, merged and handed over.

## 1. The repo in one screen

Text is dumped from two game files, translated in pieces, and spliced back by `tools/assemble.py`.
Whatever is finished can be built and played at any moment; untranslated text falls through to
the original Japanese. **`main` must pass `check` after every commit.**

| Store | Source dump | Unit of work | Where it goes | Hard limits |
|---|---|---|---|---|
| Battle script `HEXMAP.BIN`, 44 chunks | `dumps/battle_dump.txt` | one whole chunk | `tl/battle/chunk_NNN.txt` | 8,192 bytes per chunk; 24 columns × 4 rows |
| Main script `SCRIPT.BIN`, 44 banks | `dumps/script_unique.txt` (1,430 unique lines) | 40–60 unique lines | `tl/script/batch_NNN.tsv` | 0xA000 per bank; banks 41, 40, 5, 2 are nearly full (FLAGS §F2) |

Work that cannot fit is parked, never shipped: battle in `pending/chunk_NNN.txt`, script in
`pending/script/batch_NNN.tsv`. `assemble.py` reads only `tl/`, so parked work never breaks a build.

Mandatory reading before translating or reviewing: **all** of `translation_prompt.md` (budget
maths §0.2, format §1–§3, policy §2, output §6, self-check §7) and **all** of `glossary.md`.
`FLAGS.md` is the open-issue list; `findings.md` is engine reverse-engineering (engine questions
only); `pending/README.md` explains the parked chunks. Chunk order is chapter order.

## 2. Commands (repo root; no game files needed)

```
python3 tools/assemble.py status                       progress, slack per finished chunk
python3 tools/assemble.py check                        THE gate — must end "All checks passed"
python3 tools/assemble.py merge                        writes build/*_dump_merged.txt
python3 tools/rowcheck.py N tl/battle/chunk_NNN.txt    4-row check + per-line {FFFE} diff (battle)
python3 tools/rowcheck.py script                       same for the main script (after merge)
python3 tools/bankmeasure.py                           real per-bank bytes (after merge) — the only bank figure that counts
```

Start a battle translation file from the pristine dump (only the readable text may then change):

```
N=19; python3 -c "import sys; sys.path.insert(0,'tools'); import assemble as a
_,ch,_=a.split_battle(a.read('dumps/battle_dump.txt')); h,b=ch[$N]
open('tl/battle/chunk_%03d.txt'%$N,'w',encoding='utf-8').write('\n'.join([h]+b))"
```

`original/` (the game binaries) is gitignored and absent from clones, so `build` cannot write
`.BIN` files here and `riotbattle.py checkedit` cannot run. That is expected, not a defect.
Agents gate on `check`, `rowcheck` and `bankmeasure`; binaries, disc rebuilds and in-game tests
are the human's job (HANDOFF.md → "Blocked — needs a human"). Do not hunt for the disc or EXEs.

## 3. Rules that bind every agent

- Never edit `dumps/`. Never hand-edit `build/`. Never commit `build/` from a translator branch
  (`git checkout -- build/` before committing).
- Never delete a sentence, a speaker turn or a plot fact to fit a budget. If §2.1 steps 1–6 of
  the prompt do not get a unit under budget, park it with the measured figure and say so.
- Full-width Latin only (§3.1). ASCII does not render. `’` not `'`; `．．．` not `…`.
- Never change `assemble.py`, `riotbattle.py` or `riotscript.py` to make a check pass. A tool
  bug is a flag for a human, not a translator's problem.
- On a translator branch touch only your unit file. Glossary additions and flags go in the PR
  body; the reviewer integrates them into `glossary.md` and `FLAGS.md` on `main`.
- Never merge your own PR. Only the reviewer merges, and only after every gate in §6.
- Identical Japanese gets byte-identical English, across files. Grep before you write.
- After every step, update `HANDOFF.md` per §7. If you cannot (you are a translator on a
  branch), put the same content in your PR body and in your return message.
- Do not read whole dumps into context; grep or use Python. Context is a budget too.

## 4. The autonomous workflow

Three roles, all Opus at maximum effort (`.claude/settings.json`, agent frontmatter). Start the
loop with `/translate` in the main session; that session is the orchestrator.

| Role | Runs as | Does | Never does |
|---|---|---|---|
| **Orchestrator** | main session, `.claude/skills/translate/SKILL.md` | survey, queue, glossary seeds, dispatch, review routing, wave close, HANDOFF | translate, merge, edit `tl/` |
| **Translator** | subagent `translator`, own worktree, several in parallel | one unit → one branch → one PR | touch other files, merge, edit HANDOFF/glossary/FLAGS |
| **Reviewer** | subagent `reviewer`, own worktree, **one at a time** | gates + line-by-line reading → MERGE / CHANGES / PARK; integrates glossary, flags, HANDOFF | translate, waive a gate, merge from a diff read alone |

### The loop

0. **Preflight** (every start and resume): `git checkout main && git pull --ff-only`; `check`
   must pass; read `HANDOFF.md`; list open PRs and reconcile them with HANDOFF (unknown PR → add
   it; in-flight unit with no branch → mark lost, re-queue); remove finished worktrees.
1. **Survey** (first run, and whenever HANDOFF says the queue is stale): `status`, `merge`,
   `bankmeasure`, `rowcheck script`; read FLAGS §B and §F2 and `pending/README.md`. Queue every
   battle chunk not in `tl/battle/` or `pending/` with JP chars, headroom and ratio (§0.2); ratio
   < 1.6 is **blocked** (tier A: 5, 16, 32, 43). Map every untranslated unique script line to the
   banks it lands in (`=== BANK n` headers in `dumps/script_dump.txt`; dump lines carry a trailing
   `{FFFF}` the unique keys omit); a line is **blocked** if any of its banks cannot absorb its
   growth at 2.0× JP chars plus breaks. Group the rest into batches of 40–60, highest count
   first, same scene together. Write Next up / Remaining / Blocked into HANDOFF. Commit, push.
2. **Seed the glossary** for the wave: names and terms in the wave's source that are missing from
   `glossary.md` go into §9 PROVISIONAL with a proposed form in the existing conventions (or the
   alternatives listed if genuinely open). One direct commit to `main`:
   `glossary: provisional seeds for wave N`. This is the orchestrator's only glossary write.
3. **Dispatch** 3–4 units in parallel, one translator each (`run_in_background: true`), with the
   dispatch template from the skill. Battle units in chunk order (chapter order: voices and names
   accumulate); one script batch per wave. Record each unit in HANDOFF → In flight. Commit, push.
4. **Review**, one PR at a time, reviewer in the foreground (`run_in_background: false`). HANDOFF
   is committed and pushed before the reviewer starts; after it returns, `git pull --ff-only` (it
   pushed an integration commit to `main`). Record the decision.
5. **Rework**: on CHANGES, send the reviewer's numbered findings verbatim to the **same**
   translator (SendMessage keeps its context), wait for its push, review again. Three rounds
   maximum; then PARK with the reason, or hand the unit once to a fresh translator.
6. **Wave close**: all wave units merged or parked → `check` on `main`; `merge` and commit
   `build/*_dump_merged.txt` if changed; refresh the README status table from `status`; prune
   worktrees; HANDOFF gets the wave summary and the next wave. Commit, push. Back to step 2.
7. **Stop** when no dispatchable unit remains. Final HANDOFF: done, parked and why, and exactly
   what the human must do next with pointers. Never loop on blocked items.

## 5. Branch and PR contract

- Branch from fresh `origin/main`: `tl/battle-019`, `tl/script-004`, `park/battle-016`. The
  orchestrator assigns batch numbers at dispatch so parallel translators never collide.
- One PR = one unit = exactly one new or changed file under `tl/` (or `pending/` when parking).
- The commit title carries the figure: `tl: battle chunk 019 — 7,912 / 8,192 (280 slack)`;
  `tl: script batch 004 — shop lines, 52 lines / 410 instances`; `park: battle chunk 016 — 8,6xx / 8,192, floor 1.6x`.
- `git push -u origin <branch>`. Open the PR with `gh pr create` if `gh` exists, else the GitHub
  MCP `create_pull_request` tool; if neither works, push and report the branch and the
  orchestrator opens it. Fill every section of `.github/pull_request_template.md`.
- The reviewer merges with squash and deletes the branch.

## 6. Review gates — mechanical ones first, all must pass, evidence pasted in the review

1. Paths: `git diff --name-only origin/main...HEAD` is exactly the unit file.
2. Merges cleanly onto current `origin/main`.
3. `python3 tools/assemble.py check` → All checks passed.
4. Battle: bytes ≤ 8,192 with ≥ 50 slack (less only when ratio < 2.5, and flagged);
   `rowcheck.py N file` shows no page over 4 rows the source did not already exceed; every
   `{FFFE}`/`{FCC0}` change appears in the PR's Flags.
5. Script: `merge` then `bankmeasure.py` → no bank negative; any bank under 2,000 free named in
   the review; `rowcheck.py script` → nothing non-inherited over 4 rows; `merge` prints no
   "never matched the dump" (Japanese keys byte-identical to `script_unique.txt`).
6. Duplicates: every JP message in the unit that recurs anywhere in `tl/` has byte-identical EN.
7. Glossary: every term matches `glossary.md`; new terms are in the PR's Glossary additions; no
   existing entry changed silently.
8. Structure: `{FFFF}` last on every message; `===`, `{PAD}`, `{HDR:}` verbatim; menu options keep
   the leading `　`; ellipsis dot counts match; no `…` `・` `○` or ASCII anywhere.

Then the reading review, every line, Japanese beside English: literal-then-tight (§2), register
per glossary §7 and tics §5, nothing invented, nothing dropped, breaks at word or clause
boundaries, ≤ 23 columns preferred, inserts where English wants them, speaker channels straight.

The decision is a PR review: `DECISION: MERGE | CHANGES | PARK`, the gate table, then numbered
findings each naming the line and the fix. MERGE and PARK are followed by the reviewer's
integration commit on `main` (glossary section "Added by chunk NNN (PR #k)", FLAGS entry dated
today, `pending/README.md` row when parking, HANDOFF row updated), pushed as `integrate:main`.

## 7. HANDOFF.md — the live board, updated after every step

`HANDOFF.md` at the repo root, on `main`, is the single source of truth for what is going on,
what comes next and what is left. A fresh session must be able to resume from it plus the open
PR list, nothing else. It is committed and pushed after **every** step: survey done, wave
planned, unit dispatched, PR opened, review decided, rework sent, wave closed, run stopped.

- Writers: the orchestrator (main checkout) and the reviewer (its integration commit). They never
  write concurrently: the orchestrator pushes before spawning the reviewer and pulls after it.
- Translators never edit it (parallel branches would conflict). Their handoff is the PR body's
  Handoff section plus their return message; the orchestrator copies it in on receipt.
- Sections, in order: Last updated · Progress · In flight · Next up · Remaining · Blocked —
  needs a human · Decisions this run · Wave history · How to resume. Keep it under ~150 lines;
  finished waves collapse to one line each in Wave history.
- Every row says what was done, what is left on that unit, and who acts next.

## 8. Stop and safety conditions

- No dispatchable unit left → final handoff, stop. Blocked units need a human (engine patches,
  binaries, in-game checks); no amount of retranslation unblocks them.
- `check` red on `main` → stop dispatching; revert the breaking merge if needed; fix; resume.
- Cannot push or open PRs after retries → record it in HANDOFF and stop.
- A unit fails three review rounds → PARK with the measured reason; move on.
- Unattended runs rely on the allowlist in `.claude/settings.json` (or `--permission-mode
  acceptEdits`). Nothing here ever needs credentials, the disc image or network beyond GitHub.
