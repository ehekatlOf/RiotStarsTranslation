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
> **WAVE 4 IS RUNNING.** Coordinator: `session_013mqnLaJCts7hGduLSmsuak`. Glossary seeded
> (`e324d6c`, 15 rows in §9). Four units dispatched — see **In flight**.
>
> **If that session died mid-wave:** do NOT restart the wave. Run preflight, reconcile the open
> PR list against **In flight** below, re-dispatch only units with no PR and no live translator
> (`ListAgents` first — silence is not death), then review behind the barrier as usual.
>
> **When wave 4 closes**, its coordinator opens wave 5's session in the same turn:
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 5",
>   tags:            ["riotstars-translation", "wave-5"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-5 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Wave 5's units are in **Next up**.

## Last updated
2026-09-08 · by: **wave-4 coordinator** (`session_013mqnLaJCts7hGduLSmsuak`) ·
wave: **4 IN FLIGHT — 4 dispatched** · queue: **fresh**


## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **18** | 44 | 0, 1, 2, 3, 4, 6, 7, **8**, 9, 10, 11, 12, **13**, 14, 33, 34, 35, 40 |
| Battle JP characters | **13,914** | 43,161 | **32.2%** (was 26.3% at wave-3 start) |
| Script unique lines | 211 | 1,430 | `tl/script/batch_001–005.tsv` |
| Script message instances | 4,039 | 7,931 | **50.9%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353 free,
40 → 471, 5 → 3,381**, 2 → 7,505, 33 → 9,315. Bank 40 lost 38 bytes to PR #9's item-table edits.
Parked and translated: chunks **5, 43** (tier-A budget) and **17** (dump artifact).

## In flight — WAVE 4 (dispatched 2026-09-08)
Barrier: **review nothing until all four have an open PR.** Base branch for every unit and PR is
`claude/workflow-translation-iterate-uzlkns`.

| Unit | Branch | File | Budget | PR | Status |
|---|---|---|---|---|---|
| battle chunk 18 | `tl/battle-018` | `tl/battle/chunk_018.txt` | 611 JP, tier D (6.28) | **#13** | ✅ **PR open** — 3,035 / 8,192 (5,157 slack); 14 glossary rows proposed, none changing an existing entry; 2 judgement calls left for the reviewer (Flags 4 and 6) |
| battle chunk 19 | `tl/battle-019` | `tl/battle/chunk_019.txt` | 1,567 JP, tier B (**1.94 — tight**) | — | dispatched |
| battle chunk 20 | `tl/battle-020` | `tl/battle/chunk_020.txt` | 732 JP, tier D (4.75) | **#14** | ✅ **PR open** — 4,265 / 8,192 (3,927 slack); 25 glossary rows, 5 open questions for the reviewer (see below) |
| script batch pos. 2 | `tl/script-006` | **`tl/script/batch_006.tsv`** | 50 lines / 53 inst, 1,147 JP, banks 12–15 | — | dispatched |

⚠️ **The script unit is `queue.py` batch POSITION 2, written to `batch_006.tsv`** — `batch_002.tsv`
already exists and is merged. Do not let the position number become the filename.

⚠️ **A FIFTH CROSS-UNIT TERM, missed by the wave-4 seed and found by chunk 20's translator:
`宝石` / `宝`.** Re-counted in the dump and confirmed: c19 has 宝石 ×1 and 宝 ×4 (incl. 財宝 ×1),
c20 has 宝石 ×4 and 宝 ×7 (incl. お宝 ×2); c31 ×1 is untranslated. **Chunk 20 ships `宝石` →
`ｇｅｍｓｔｏｎｅｓ`, `宝`/`お宝` → `ｔｒｅａｓｕｒｅ`/`ｔｈｅ　ｔｒｅａｓｕｒｅ`**, rejecting lowercase
`ｊｅｗｅｌｓ` because §3 fixes ジュエル → `Ｊｅｗｅｌ` and ジェム → `Ｇｅｍ` and `Ｇｅｍ` already appears
**147×** across `tl/`. Relayed to chunk 19's translator mid-flight with the counts; chunk 19 is
tier B and holds the casting vote on width, and chunk 20 can be moved to match at no cost.

**Chunk 20's five open questions for its reviewer** (from PR #14, in its priority order):
1. `あら？` → `Ｍｙ？` (§28.3, the later ratified rule) **vs shipped `chunk_014.txt` L3's `Ｏｈ？`** —
   and it is the **same speaker** (portrait 02) in both. §28.3 exists precisely because `Ｏｈ` was
   already spent on おや (§24.4). §3 is not engaged (different messages), so nothing shipped needs
   re-cutting either way — but `あら` has **16 further occurrences**, so this needs one written
   ruling rather than a third drift.
2. `宝石` / `宝` reconciliation with chunk 19 (above).
3. `火の水晶`: chunk 20 took the long `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ`; −6 bytes and no re-flow to
   follow chunk 19 to the short form.
4. `おかしらぁ！` → `Ｂｏｓｓｓ！` or `Ｂｏｓｓ！！`. 0 bytes either way.
5. `勲章` → `ｍｅｄａｌ` now **shares its English with §3's racetrack `メダル`** → `ｍｅｄａｌ`, shipped
   in `batch_002.tsv`. The seed did not mention it; ruled acceptable on §25.3's co-occurrence test
   (never in one scene), but it should be recorded rather than rediscovered.

⚠️ **Chunks 19 and 20 share four terms** (`火の水晶`, `アリエス`, `カバラ`, `ヒューゴー`). Both
translators were seeded with the same forms (`glossary.md` §9, wave-4 block); CLAUDE.md §3 requires
byte-identical English. The seed row is struck by the **second** of the two reviewers to merge.

## Next up — WAVE 5
**Battle chunks 21 (D 4.28), 22 (D 4.59), 24 (C 2.99)** — chapter order, all artifact-free.
⚠️ **Skip 23** as well as 15: both carry the §D1 dump artifact (Blocked item 0).

**One script batch — `queue.py script` position 1**, unique lines **318, 421–469** (50 lines /
52 instances, 3,056 JP chars, banks 2–3): recruitment and shop dialogue, vetted clean by wave 3.
⚠️ **Write it as `tl/script/batch_007.tsv`** — the position number is not the filename; wave 4
took `batch_006.tsv`.

| `queue.py script` position | Lines | Banks | Verdict |
|---|---|---|---|
| **1** — 318, 421–469 | 50 / 52 inst, 3,056 JP | 2, 3 | ✅ **clean — wave 5's pick** |
| ~~2~~ — 319, 335, 599–646 | 50 / 53 inst | 12–15 | ⏳ taken by wave 4 → `batch_006.tsv` |
| ~~3~~ — 320, 1073–1121 | 50 / 52 inst | 31–34 | ⛔ **28/50 DEBUG SCAFFOLDING** — BGM sound-test menu (`５０：新曲１`) and a flag screen (`どのフラグを操作しますか？`). **Never dispatch.** |
| 4 — 326–328, 470–516 | 50 / 53 inst, 1,638 JP | 4, 5, 7 | ✅ clean — ノロ village + towns. ⚠️ bank 5 has 3,381 free |

⚠️ **Vetting method, or the check silently passes everything:** `script_unique.txt` rows are
`<instance count>\t<text>`, so the scaffolding regex `フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must
match the **text field**. Against the raw line the anchored `^[０-９]{2}：` never fires and position
3 scores 18/50 instead of its true 28/50 — a vet that looks like it passed.

**Seed the glossary BEFORE dispatching.** It moved four times during wave 3; wave 4 seeded 15 rows
up front and told every reviewer to re-run gate 7 against the *current* glossary.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **21 open chunks** after wave 3, but ⚠️ **6 of them carry the §D1 dump artifact (Blocked
item 0) and will park exactly as chunk 17 did — 15, 23, 27, 28, 29, 39.** Until a human fixes
`riotbattle.tokenise`, only **15 chunks are truly dispatchable**, in chapter order (tier, ratio):
18 (D 6.28), 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59), 24 (C 2.99), 25 (C 3.48),
26 (C 3.36), 30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 41 (E 6.54),
42 (D 5.46).

Script: 1,219 unique lines / ~3,892 instances untranslated. The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is down to 471 free** —
lines 185–225 stay parked until it is repointed. After that the 1-instance story text in the roomy
banks (518–1,413) is what remains dispatchable; `queue.py script` offers batches 1, 2 and 4 clean.

## Blocked — needs a human
0. 🔧 **THE `riotbattle.tokenise` DUMP ARTIFACT — new 2026-09-08 (PR #12), and it is now the
   highest-leverage item on this list.** `FLAGS.md` **§D1, §R**. The dumper prefers a Shift-JIS
   text run over a control tag whenever an argument byte happens to be a valid lead byte, so an
   item id plus the *next tag's* lead byte decodes as a kanji. **24 occurrences across 10 chunks**
   — `{FC70}` in 5, 16, 17, 23, 39 and `{FCA8}` in 15, 27, 28, 29, 32 — and every one of them makes
   `assemble.py check` unsatisfiable for that chunk: the dump form passes tag parity and fails
   charset, and every re-tokenised form does the reverse. **Chunk 17 is already finished, faithful,
   format-clean and 2,335 bytes UNDER its slot, and is parked for this reason alone.**
   Fix: teach `tokenise` the argument lengths of `{FC70}` and `{FCA8}` (or stop an argument byte
   from ever starting a text run), then `assemble.py refresh`. Chunk 17 then unparks with a
   `git mv` plus a **0-byte** re-tokenisation of one tail. ⚠️ **This needs no disc, no EXE and no
   emulator — unlike everything else on this list — and it unblocks ten chunks at once.**
   ⚠️ **Chunk 15 is on wave 4's list and carries it at message line 11**, so it will park the same
   way unless this is done first (`FLAGS.md` §R3).
1. **Tier A battle chunks 5, 16, 32, 43.** Measured budget ratios 1.53 / 1.59 / 1.61 / 1.23, all
   below the **1.64× floor measured in FLAGS §B2**; no faithful translation fits 8,192 bytes.
   5 and 43 are translated and parked in `pending/`. Fix: the engine patch in
   `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script
   buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends settling
   KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (FLAGS §F2). Translating everything that remains needs
   +30,534 bytes in bank 41 (353 free), +20,924 in bank 40 (**471**), +14,720 in bank 5 (**3,381**),
   +12,798 in bank 2 (**7,505**) and +11,492 in bank 33 (**9,315**) — about **66 KB short**. Every
   other bank has room. 376 unique lines / 3,001 instances are therefore unshippable until a
   MAIN1.EXE repoint or bank-spill scheme exists.

   **Worst cases:** unique 1160–1354 (195 lines) are resident in **bank 40 alone** (471 free,
   needs ~19,000); unique 1355–1387 (33 lines, 14,607 JP chars) in **bank 41 alone** (353 free,
   needs ~29,000). Neither late chapter can be shipped even partially in a way worth playing.

   **Policy this run:** bank 40's spendable budget goes to the 21-instance item-description table
   (~40 lines ≈ 840 instances), not to bank 40's own story text (~25 of 195 lines ≈ 25 instances,
   leaving that chapter 90% Japanese). Reversible — a choice, not a fact — but the arithmetic is
   not close.
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
6. ~~**Chunk 5 dump artifact**~~ — **subsumed by item 0**, which is the same defect measured across all
   10 affected chunks. One fix closes both.

## Decisions this run
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured, not the skill's assumed 2.0×.
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not bank 40's own
  story text. Reversible; the arithmetic is not close.
- 2026-09-08: **seed the glossary BEFORE dispatching a wave.** Wave 3 did; its four round-1 CHANGES
  had unrelated causes, against wave 2's three from a moving glossary.
- 2026-09-08: **a parked unit gets the full reading review before it is parked** (PR #12). It ships
  *unchanged* after a `git mv` and nobody re-reads `pending/`, so defects found later are inherited.

- 2026-09-08 (wave 4 preflight): ⚠️ **a fresh container clones SHALLOW and carries a STALE local
  `claude/workflow-translation-iterate-uzlkns` ref** (wave-1 state, *no merge base* with origin).
  The container starts detached at the right commit, so `git checkout <branch>` silently moves you
  backwards 51 commits and `git pull --ff-only` then aborts. Fix: `git reset --hard
  origin/claude/workflow-translation-iterate-uzlkns` after fetching. Verify with `git log -1`
  before trusting the tree — no work is lost, the local ref is a container artifact.
- 2026-09-08: **the `queue.py` batch POSITION is not the filename.** Wave 4's unit was position 2
  and became `batch_006.tsv`; `batch_002.tsv` has been merged since wave 1.

**Rulings live in their homes, not here**: `glossary.md` §23–§30, `FLAGS.md` §K–§R,
`findings.md` §24, `pending/README.md`. Wave 3 added §27–§30 and §O–§R.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections/audit-wave1 + battle 8, 13, 17 | **3** | **1** | battle **18/44 (32.2%)**; script unchanged |

**Wave 3 detail.** PRs #9–#12, full three-role split. `#9` corrections (12 edits, 5 files) closed
the live CLAUDE.md §3 violation — `tl/battle/` now holds 0 divergent duplicate renderings. `#11`
chunk 8 — 7,437 / 8,192, round 2. `#10` chunk 13 — 5,417 / 8,192, round 1, zero blocking findings.
`#12` chunk 17 — **PARKED**, translated and 2,335 bytes under its slot, blocked solely by the §D1
dump artifact. **The wave's pattern was findings being verified rather than obeyed, in both
directions** — translators disproved a finding's premise and improved on a proposed fix, two
reviewers withdrew findings after measuring, one demoted a ruling it had been asked to ratify, and
translators corrected three coordinator errors. Detail lives in `glossary.md` §27–§30 and
`FLAGS.md` §O–§R.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
