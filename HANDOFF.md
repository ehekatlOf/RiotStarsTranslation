## Run configuration — READ BEFORE BRANCHING
**The integration branch for this run is `claude/workflow-translation-iterate-uzlkns`, not
`main`.** Everywhere `CLAUDE.md`, the `translate` skill and the agent files say `main`, read this
branch: translators branch from it, PRs use it as base, reviewer integration pushes go to
`integrate:claude/workflow-translation-iterate-uzlkns`. The human fast-forwards `main` from it when
the run is done.

⚠️ **A fresh container clones SHALLOW and carries a STALE local ref of that branch** (wave-1 state,
*no merge base* with origin). It starts detached at the right commit, so `git checkout <branch>`
silently moves you backwards and `git pull --ff-only` then aborts. **All four wave-4 reviewers hit
this.** Fix: `git fetch` then `git reset --hard origin/claude/workflow-translation-iterate-uzlkns`,
and verify with `git log -1` before trusting the tree. No work is lost; the local ref is a
container artifact.

## NEXT ACTION — always current, always a literal instruction
> **WAVE 4 IS CLOSED — 4 of 4 merged, 0 parked. `check` green. Battle 21/44 (39.4%), script 51.6%.**
> The next act is to **OPEN WAVE 5'S SESSION**, which wave 4's coordinator does in the same turn.
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
> Omit `environment_id` and `model` so both inherit. Units: **the `あら` corrections unit + battle
> chunks 21, 22 + script `batch_007.tsv`** — see **Next up**.
>
> If this line still says "open wave 5" and no wave-5 session exists, the chain broke: open it.

## Last updated
2026-09-09 · by: **wave-4 coordinator** (`session_013mqnLaJCts7hGduLSmsuak`) ·
wave: **4 CLOSED — 4 merged, 0 parked** · queue: **fresh**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **21** | 44 | 0–4, 6–14, **18, 19, 20**, 33, 34, 35, 40 |
| Battle JP characters | **17,002** | 43,161 | **39.4%** (was 32.2% at wave-4 start) |
| Script unique lines | **261** | 1,430 | `tl/script/batch_001–006.tsv` |
| Script message instances | **4,092** | 7,931 | **51.6%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353 free,
40 → 471, 5 → 3,381**, 2 → 7,505, 33 → 9,315. Wave 4 spent only banks 12–15 (−2,480) and left 41
and 40 byte-for-byte untouched. Parked and translated: chunks **5, 43** (tier-A budget) and **17**
(dump artifact).

## In flight
**Nothing. Wave 4 is closed and no PR is open.** Wave 5's session dispatches its own units.

## Next up — WAVE 5
**Four units. Seed the glossary BEFORE dispatching** (it moved four times during wave 3 and three
times *inside* wave 4 — §31, §32, §33 — so every reviewer must be told to rebase and re-run gate 7
against the CURRENT glossary, weighing each difference as "translator error" vs "a ruling that did
not exist when the unit was drafted").

**1. ⭐ The `あら` corrections unit — do this one, it is owed and now unblocked.** `FLAGS.md` §T1.
Chunk 20's reviewer ruled `あら` → `Ｍｙ` + the source's own punctuation (glossary §32.4) and
deliberately did **not** re-cut the outliers, because two sibling PRs were open on the same
question. **Both have since merged and both conform, so that condition is discharged.** Re-cut four
shipped rows, all width-neutral or −6 bytes: `chunk_007` L19 and L24, `chunk_011` L3,
`chunk_014` L3. A §27-style corrections unit, one PR.

**2. Battle chunks 21 (D 4.28) and 22 (D 4.59)** — chapter order, both artifact-free and roomy.
⚠️ **Chunk 21 inherits `この裏切り者め。`**: §31's `〜め` on a personal name → `Ｔｈａｔ　〜` was fixed
by chunk 18. ⚠️ **Chunk 23 is NOT next** despite chapter order — it is artifact-blocked (below).

**3. One script batch — `queue.py script` position 1**: unique **318, 421–469** (50 lines /
52 instances, 3,056 JP chars, banks 2–3), recruitment and shop dialogue, vetted clean.
⚠️ **Write it as `tl/script/batch_007.tsv`** — the queue POSITION is not the filename; wave 4's
position-2 unit became `batch_006.tsv`.
⚠️ **It inherits forward bindings from `batch_006` (`FLAGS.md` §V):** unique **598** must reuse
batch_006's menu strings byte-for-byte (`　Ｂｕｙ　ａｎ　ｉｔｅｍ` / `　Ｓｅｌｌ　ａｎ　ｉｔｅｍ` /
`　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ`), and unique **592–597, 647–655** are two more copies of the same shop
skeleton — they inherit `Ｗｅｌｃｏｍｅ`, `Ｍａｎｙ　ｔｈａｎｋｓ`, `ａｒｔｉｃｌｅ`, `　Ｌｅａｖｅ　ｉｔ` and the
notice wording rather than re-inventing them.

**Battle chunk 24 (C 2.99) moves to wave 6** — four units is the dispatch limit and the corrections
unit takes a slot.

⚠️ **Vetting method for future script batches, or the check silently passes everything:**
`script_unique.txt` rows are `<count>\t<text>`, so the scaffolding regex
`フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must match the **text field**. Against the raw line the
anchored `^[０-９]{2}：` never fires and position 3 scores 18/50 instead of its true 28/50 — a vet
that looks like it passed. **Position 3 (unique 320, 1073–1121) is 28/50 debug scaffolding: never
dispatch it.** Position 4 (326–328, 470–516) is clean but ⚠️ bank 5 has only 3,381 free.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **23 open chunks**, but ⚠️ **6 carry the §D1 dump artifact (Blocked item 0) and will park
exactly as chunk 17 did — 15, 23, 27, 28, 29, 39.** Until a human fixes `riotbattle.tokenise`, only
**12 are truly dispatchable**, in chapter order (tier, ratio): 21 (D 4.28), 22 (D 4.59),
24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69),
38 (C 3.37), 41 (E 6.54), 42 (D 5.46).

Script: **1,169 unique lines / 3,839 instances untranslated.** The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is down to 471 free** —
lines 185–225 stay parked until it is repointed. After that the 1-instance story text in the roomy
banks (518–1,413) is what remains dispatchable.

## Blocked — needs a human
0. 🔧 **THE `riotbattle.tokenise` DUMP ARTIFACT — the highest-leverage item on this list.**
   `FLAGS.md` **§D1, §R**. The dumper prefers a Shift-JIS text run over a control tag whenever an
   argument byte happens to be a valid lead byte, so an item id plus the *next tag's* lead byte
   decodes as a kanji. **24 occurrences across 10 chunks** — `{FC70}` in 5, 16, 17, 23, 39 and
   `{FCA8}` in 15, 27, 28, 29, 32 — and every one makes `assemble.py check` unsatisfiable for that
   chunk: the dump form passes tag parity and fails charset, and every re-tokenised form does the
   reverse. **Chunk 17 is already finished, faithful, format-clean and 2,335 bytes UNDER its slot,
   and is parked for this reason alone.** Fix: teach `tokenise` the argument lengths of `{FC70}`
   and `{FCA8}` (or stop an argument byte from ever starting a text run), then
   `assemble.py refresh`. Chunk 17 then unparks with a `git mv` plus a **0-byte** re-tokenisation
   of one tail. ⚠️ **This needs no disc, no EXE and no emulator — unlike everything else here —
   and it unblocks ten chunks at once.**
1. **Tier A battle chunks 5, 16, 32, 43.** Measured budget ratios 1.53 / 1.59 / 1.61 / 1.23, all
   below the **1.64× floor measured in FLAGS §B2**; no faithful translation fits 8,192 bytes.
   5 and 43 are translated and parked in `pending/`. Fix: the engine patch in
   `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script
   buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends settling
   KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (`FLAGS.md` §F2 has the full table). About **66 KB short**
   overall: bank 41 needs +30,534 with 353 free, bank 40 +20,924 with 471, bank 5 +14,720 with
   3,381, bank 2 +12,798 with 7,505, bank 33 +11,492 with 9,315. Every other bank has room.
   **376 unique lines / 3,001 instances are unshippable** until a MAIN1.EXE repoint or bank-spill
   scheme exists. Two whole late chapters are the worst cases — unique 1160–1354 live in **bank 40
   alone** and 1355–1387 in **bank 41 alone**; neither can be shipped even partially in a way worth
   playing. **Policy this run:** bank 40's spendable budget goes to the 21-instance item table
   (~840 instances), not its own story text (~25 instances, leaving that chapter 90% Japanese).
   Reversible — but the arithmetic is not close.
3. **Main-script box not yet widened** (MAIN1.EXE side). Translate to 24 columns anyway;
   `riotfont.py rewrap` re-flows later.
4. **In-game checks**: `FLAGS.md` §D2/§D3 (pages over 4 rows), §D4 (is line 1234 reachable),
   §F6 (description window 3 or 4 rows), `findings.md` menus and name-entry first test. Two are
   worth doing before the rest:
   ⭐ **`FLAGS.md` §L2 / `findings.md` §24.** Eight lines in `battle_dump.txt` carry **no
   `{FC50}`/`{FC51}` at all** yet exceed four text rows — chunk 6 L9 (15) and L21 (11), chunk 7
   L23/L24 (5 and 6, already shipped — §D3), chunk 30 L23 (8), **chunk 32 L31 (59)**, chunk 37 L14
   (8), chunk 42 L11 (16). A 59-row page cannot exist, so the prediction is that these are **pools
   of independently-selected strings** with `{FC03}` as the selector. **One visit to the chapter 5
   church map and chapter 6 settles it, and §D3 with it.** If it holds, `rowcheck`'s `> 4 rows`
   warning is meaningless on all eight; if it fails, chunk 7 L24 is already broken in shipped work.
   ⚠️ **§C4, promoted by wave 4:** both `check` and `rowcheck` **strip `{FFEC}` inserts to 0
   columns**, so the column gate is *blind* to twelve rows in `batch_006` and to four further
   copies of that shop skeleton. Its translator bounded every row at insert+8 against the
   Japanese's insert+0..+7 — the right response to an unmeasurable gate, but a bound, not a
   measurement. **One visit to any shop with the game's longest item name settles it.**
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. 📄 **`SKILL.md` §3 edit (small, and wave 4 earned it): scratch-file namespacing must bind EVERY
   role, not just translators.** A **reviewer's** script was overwritten mid-task by another agent
   this wave and caught only because the output was visibly the wrong unit's data — that is gate
   evidence underpinning a merge decision. Reviewers run concurrently with reworking translators by
   design, so they collide identically. Add: every agent namespaces every scratch file
   (`r015_dupes.py`), and no agent trusts a scratch script it did not write in the same turn.

## Decisions this run
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured, not the skill's assumed 2.0×.
  (Wave 4's script batch came in at **1.89×**.)
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not its own story
  text. Reversible; the arithmetic is not close.
- 2026-09-08: **seed the glossary BEFORE dispatching a wave.**
- 2026-09-08: **a parked unit gets the full reading review before it is parked** (PR #12).
- 2026-09-08: **the `queue.py` batch POSITION is not the filename.** Wave 4's position-2 unit became
  `batch_006.tsv`; `batch_002.tsv` merged in wave 1.
- 2026-09-09: **a term is "in the glossary" only if a row FIXES an English form.** `grep -c` on the
  Japanese string is not that test — the coordinator called four terms glossary-fixed when they
  appeared only as Japanese quotations inside another row's evidence note, and the translator
  caught it.
- 2026-09-09: **a co-occurrence discharge is only as good as its counts** (`FLAGS.md` §T2). The §9
  seed said `勲章` was "2 battle"; it is **4 battle + 59 script-dump** and a named plot item, and
  §25.3's test **fails** on banks 42–43. The rendering was still right. Count the corpus before
  writing "never in one scene".
- 2026-09-09: **a reviewer may rule a cross-file question without re-cutting the outliers in the
  same commit.** The `あら` ruling bound immediately; the four rows it invalidated were recorded
  with lines and measured costs and left to a corrections unit, because sibling PRs were in flight
  on the same question. Recording with the lines named is what §4.3 requires; applying them
  mid-wave is not.
- 2026-09-09: **findings are proposals to be verified in both directions, and wave 4 is the
  evidence.** Every unit had figures or reasoning corrected by someone downstream: reviewer 1 fixed
  five of a PR's figures while ratifying its calls; reviewer 2 corrected reviewer 1's day-old
  §31.3; chunk 19's translator corrected reviewer 2's own evidence (42 instances, not 21) and the
  reviewer recorded the correction **against itself**; reviewer 4 replaced a PR's justification
  while keeping its rendering; and two translators corrected the coordinator.

**Rulings live in their homes, not here**: `glossary.md` §23–§34, `FLAGS.md` §K–§V,
`findings.md` §24, `pending/README.md`. Wave 4 added glossary §31–§34 and `FLAGS.md` §S–§V.
⚠️ **Section numbers are taken by READING both files at commit time, never reserved in advance** —
wave 4 had one reviewer's reserved §32 claimed by another mid-wave.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle **21/44 (39.4%)**; script **261 lines (51.6%)** |

**Wave 4 detail.** PRs #13–#16, full three-role split, four separate reviewers for four units none
of them translated — **no independence audit is owed**. Three merged at round 1; chunk 19, the
tightest unit in the project so far (**8,065 / 8,192, 127 slack**), merged at round 2 with all four
findings accepted and **not one costing a byte**. Chunk 20 was the first unit whose every PR figure
was correct as stated. The wave settled `あら` (§32.4) — raised independently by two units from
opposite ends of the corpus — and struck a false claim in §28.3; narrowed §31.3's over-broad
`まさか` (§33.6) one hour after it was written; and discharged the five-term cross-unit
coordination between chunks 19 and 20 with **zero divergent renderings** and no re-cut. Detail
lives in `glossary.md` §31–§34 and `FLAGS.md` §S–§V.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (see Run
   configuration — a plain `checkout` lands on a stale ref), then
   `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
