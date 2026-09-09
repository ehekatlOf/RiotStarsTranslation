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
> **WAVE 5 IS CLOSED — 4 of 4 merged, 0 parked. `check` green. Battle 23/44 (43.2%), script 52.5%.**
> The next act is to **OPEN WAVE 6'S SESSION**, which wave 5's coordinator does in the same turn.
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 6",
>   tags:            ["riotstars-translation", "wave-6"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-6 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Units: **battle chunks 24, 25, 26 + the
> 47-line script batch (unique 470–516)** — see **Next up**.
>
> If this line still says "open wave 6" and no wave-6 session exists, the chain broke: open it.

## Last updated
2026-09-09 · by: **wave-5 coordinator** (`session_0126GVzUTXdEP5VpVWWJXBCU`) ·
wave: **5 CLOSED — 4 merged, 0 parked** · queue: **fresh, wave-6 batch pre-vetted**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **23** | 44 | 0–4, 6–14, 18–22, 33, 34, 35, 40 |
| Battle JP characters | **18,664** | 43,161 | **43.2%** (was 39.4% at wave-5 start) |
| Script unique lines | **311** | 1,430 | `tl/script/batch_001–007.tsv` |
| Script message instances | **4,162** | 7,931 | **52.5%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353, 40 → 447,
5 → 3,357, 2 → 3,365** (bank 2 fell from 7,505 this wave and has joined the tight group),
33 → 9,291. Parked and translated: chunks **5, 43** (tier-A budget) and **17** (dump artifact).

## In flight
**Nothing. Wave 5 is closed and no PR is open.** Wave 6's session dispatches its own units.

## Next up — WAVE 6
**Four units. Seed the glossary BEFORE dispatching.** Sections currently end at **glossary §38** and
**FLAGS §Z** — ⚠️ take the next number by **READING both files at commit time**, never by reserving.

**1–3. Battle chunks 24 (C 2.99), 25 (C 3.48), 26 (C 3.36)** — chapter order, all artifact-free.

**4. Script batch → `tl/script/batch_008.tsv` — ALREADY COMPUTED AND VETTED at the wave-5 close.**
**Take `queue.py script` position 3 MINUS unique 326, 327, 328 → 47 lines, unique 470–516.**
- 0/47 scaffolding, vetted on the **text field**. Banks 3/4/5 only: bank 3 **+448 → 7,665**,
  bank 4 **+2,037 → 9,768**, bank 5 **+741 → 2,640**. **Bank 40 untouched at 447.**
- ⚠️ **326/327/328 MUST be excluded.** Each has **count 3** and all three instances land in
  **bank 40**: **+816 bytes against 447 free → bank 40 goes NEGATIVE by 369.** They are 3-instance
  gossip lines (Batou; Limrose's casino; the hobbit village) and wait for the bank-40 repoint.
- ⚠️ **Position 4 (329–332, 521–566) is NOT dispatchable** despite being scaffolding-clean: it puts
  **3,351 JP chars into bank 5** (3,357 free) → **−3,991**. Clean of scaffolding, fatal on banks.
- ⚠️ **Position 2 (320, 1073–1121) is the debug batch — NEVER dispatch** (28/50 scaffolding).
- ⚠️ **The recorded vetting regex is broken TWICE, not once.** Matching the **text field** (rows are
  `<count>\t<text>`) is necessary but **not sufficient**: `^[０-９]{2}：` fires **ZERO** times even
  there, because the text begins with `{FB01}` tags, not digits. Use **unanchored `[０-９]{2}：`**
  on the text field — that is what yields position 2's 28/50.

⚠️ **Chunk 37 (a later wave) inherits `FLAGS.md` §Y6:** Cress's gender is fixed nowhere in
`glossary.md` and rendered nowhere in `tl/` (chunks 8, 13, 22 are first-person, vocative or
subject-less). A third-person line forces the pronoun; getting it wrong is a §4.3 correction
reaching three shipped files.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **21 open chunks**, but ⚠️ **6 carry the §D1 dump artifact (Blocked item 0) and will park
exactly as chunk 17 did — 15, 23, 27, 28, 29, 39.** Until a human fixes `riotbattle.tokenise` only
**10 are dispatchable**, in chapter order: 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 30 (B 2.43),
31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 41 (E 6.54), 42 (D 5.46). **About three waves.**

Script: **1,119 unique lines / 3,769 instances untranslated.** The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is down to 447 free** —
lines 185–225 stay parked until it is repointed. After that the 1-instance story text in the roomy
banks (518–1,413) is what remains. ⚠️ **Bank 2 is now tight (3,365)** and cannot take a second batch
the size of 007.

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
**Rulings live in their homes, not here**: `glossary.md` §23–§38, `FLAGS.md` §K–§Z, `findings.md`
§24, `pending/README.md`. ⚠️ **Section numbers are taken by READING both files at commit time,
never reserved** — wave 4 had a reserved §32 claimed mid-wave.
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured (wave 4 came in at 1.89×, wave 5 at
  2.09×).
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not its story text.
- 2026-09-08: **seed the glossary BEFORE dispatching a wave**; **a parked unit still gets the full
  reading review**; **the `queue.py` batch POSITION is not the filename**.
- 2026-09-09: **a term is "in the glossary" only if a row FIXES AN ENGLISH FORM** — `grep -c` on the
  Japanese string is not that test.
- 2026-09-09: **findings are proposals to be verified in BOTH directions.** Wave 5's evidence: three
  translators and two reviewers corrected the coordinator; one reviewer corrected another reviewer's
  correction; three units had PR figures corrected by their reviewer **while still merging**, none
  costing a byte.
- 2026-09-09: **compute cross-unit terms MECHANICALLY** (`FLAGS.md` §Y2) — intersect the ≥2-char
  kanji/katakana runs of the two sources. The coordinator asserted five terms; four were wrong and a
  fifth (`つるん`) was missing. The true set was **eight, and all eight agreed**.
- 2026-09-09: **a "verified free" reach claim goes STALE when a sibling merges** (`FLAGS.md` §Y3).
  Re-verify against the tree at review time, not at drafting time.
- 2026-09-09: **a reviewer should PATCH a measured documentation error in place, not merely record
  it.** §29.5 measured §2's rank widths in wave 3 and only recorded them; the wrong figure then
  travelled two waves into the wave-5 seed. PR #18's reviewer patched §1 and §2.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle **23/44 (43.2%)**; script **311 lines (52.5%)** |

**Wave 5 detail.** PRs #17–#20, full three-role split, **four separate reviewers, all four merged at
round 1, no rework** — no independence audit is owed. The corrections unit found a **fifth** `あら`
outlier its own ruling table had dropped (§32.4 named chunk 8 in its census sentence and omitted it
from its table). Chunk 21 and 22 agreed byte-for-byte on all **eight** shared terms. PR #19 accepted
the project's first possessive on the `{FC00}` insert on the evidence that 48 rows already bind a
character to it. Detail lives in `glossary.md` §35–§38 and `FLAGS.md` §W–§Z.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (see Run
   configuration — a plain `checkout` lands on a stale ref), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8.
