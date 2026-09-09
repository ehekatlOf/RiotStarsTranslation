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
> **WAVE 7 IS CLOSED — 3 merged, 1 parked, `check` green. Battle 28/44 (56.5%), script 53.7%.**
> The next act is to **OPEN WAVE 8'S SESSION**, which wave 7's coordinator does in the same turn.
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 8",
>   tags:            ["riotstars-translation", "wave-8"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-8 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Units: **battle 37, 38, 41, 42 + one script
> batch computed fresh** — see **Next up**.
>
> ⚠️ **WAVE 8 IS THE LAST BATTLE WAVE.** It spends the final four dispatchable chunks; after it,
> battle work **STOPS** until a human clears Blocked **0** or **0a**.
>
> If this line still says "open wave 8" and no wave-8 session exists, the chain broke: open it.

## Last updated
2026-09-09 · by: **wave-7 coordinator** (`session_01N1VxX55Vw79fxNr6nTELcs`) ·
wave: **7 CLOSED — 3 merged, 1 parked, 1 rework round** · queue: **fresh; wave-8 script batch must
be recomputed against the figures below, NOT inherited**

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

## In flight
**Nothing. Wave 7 is closed and no PR is open.** Wave 8's session dispatches its own units.

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
⚠️ **NEW, AND IT BINDS EVERY TRANSLATOR FROM NOW ON (glossary §45.2 / FLAGS §AG1).** **A page's
source-blank TRAILING segment MAY carry text** — where no tag is added, moved or deleted and the
resulting shape is attested in the pristine dump. It buys a text row for **0 bytes** against
`{FFFE}`'s 2. A 44-chunk census settles it: `TTTT` 389, `TT` 262, `.TTTT` **182**, `TTT` 115 — and
**`.TTTT.` 0**. ⚠️ **§3.2's warning is about `.TTTT.` ONLY** (leading blank *and* trailing blank
*and* four text rows) and does **not** reach `.TTTT`; filling a trailing blank moves *away* from the
never-attested shape. Misreading this cost chunk 31 a review round — it compressed a line for a
constraint that does not exist, in a chunk with 2,837 bytes of slack.
⚠️ **§AC3 EXTENDED (FLAGS §AG6): measure the option you argue AGAINST, not only the one you ship.**
Chunk 31 `len()`-measured every row that entered the file and got all of them right; the *rejected*
alternative quoted in its flag never entered the file, was hand-counted, and was wrong — and it was
the number the whole argument rested on. No gate can catch that one.

⚠️ **RULINGS LIVE IN THEIR HOMES, NOT HERE** — `glossary.md` §23–**§45**, `FLAGS.md` §K–**§AG**,
`findings.md` §24, `pending/README.md`. Section numbers are taken by **READING both files at commit
time**, never reserved. This section keeps only what does not belong to a single unit.

**Standing (waves 4–6).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×**. Bank 40's budget goes to the 21-instance item
table, not its story text. Seed the glossary **before** dispatching. A **parked unit still gets the
full reading review**. The `queue.py` batch **position is not the filename**. A term is "in the
glossary" only if a row **fixes an English form**. Mechanical term search has **four blind spots**
(mixed script, maximal runs, katakana register transforms, kana variants — §Y2/§AC1). A glossary
row's **Alt column records REJECTED options, not a menu**. `{FCC0}` is forbidden by
`assemble.py:tag_parity`, **not** by `rowcheck.py` (§Q2, already correct — never patch it).

**Wave 7 — measurement discipline. This is the section that earns its space.**
- ⚠️ **EIGHT coordinator/inherited figures were refuted by measurement this wave, and every single
  one was caught by an agent I had told to check me.** Mine: the batch's "queue position 6" label
  (it is a hand-cut line range); "positions 1–5 are all bank-negative" (does not reproduce); an
  instruction to reproduce Latin "character for character" (**impossible** — `・` U+30FB is rejected
  by the charset gate); `そうかい` attributed to `batch_008` (it is `batch_007.tsv:27`). Inherited
  from a PR and repeated by me without measuring: `クロイツェル` called exhausted (it is not — 1
  battle + 1 script, bank 41); the second bad `ｇｅｍｓｔｏｎｅ` cell placed in §33.5 (it is at
  **line 2804 inside §33's promotions table**; §33.5 carries no figure). **Write "your measurement
  wins and my cell is the error" into every dispatch, and mean it.**
- ⚠️ **AND VERIFY IN BOTH DIRECTIONS — two "corrections" TO me were themselves wrong.** PR #27's
  reviewer "corrected" `石版` DATA 569/571 to FILE 574/576 and it was written into `FLAGS.md` §AE5
  and glossary §9 as though 569/571 were an error. **They are the same lines in two conventions**
  (FILE = DATA + 5). Chunk 36's reviewer withdrew it (§AF3, glossary §44.5). §AE5's real finding —
  a third `石版` at **DATA 300, 21 instances across 21 banks** — stands.
- ⚠️ **STATE YOUR NUMBERING CONVENTION on every line-number claim, and cite a location by READING
  it, not by copying a citation.** Seven conventions exist in this repo (`batch_008.tsv` counts
  DATA, `batch_007.tsv` counts FILE, `rowcheck` line N = `validate_body` body line N−1). Numbering
  has now cost real attention twice in one wave, and §AD5 flagged the same clash a wave earlier.
- ⚠️ **MEASURE THE OPTION YOU ARGUE AGAINST, not only the one you ship** (§AC3's new hiding place).
  Chunk 31's only wrong figure was its own **rejected** alternative — hand-counted because it never
  entered the file, so nothing ever checked it. Reserves, alternatives and "this would have been"
  figures are where hand-counting survives.
- ⚠️ **A GATE-6 CHECKER THAT MATCHES NOTHING REPORTS A CLEAN PASS** (`FLAGS.md` §AE7). PR #27's
  reviewer's first checker matched **zero** pairs and passed; only a positive control caught it.
  **Plant a corruption, prove the checker fails on it, then trust its output.** Battle `tl/` files
  hold no Japanese (grep is a null check — use the positional method); script TSVs keep Japanese in
  column 2, so a column-2 grep is valid there.
- **A CENSUS BEATS A PLAUSIBLE READING OF THE STYLE GUIDE.** Chunk 31 compressed a line believing
  §3.2 forbade a 4th text row under a leading blank; a census of all 44 pristine chunks found that
  shape (`.TTTT.`) occurs **0** times and `.TTTT` **182**. Premise gone, compression unlicensed.
- **SERIALISED REVIEW PAID OFF AGAIN — §41.4 now predicts 11 of 11.** `chunk_030` merged *between*
  chunk 31's two review rounds and supplied three more `どうやら` instances, all formal, all
  matching, from an independent unit and agent. Second wave running this has happened.
- **A wrong figure travels.** Three of the eight above originated in a PR, passed through my
  briefing unmeasured, and were caught only by the third role. The three-role split is doing work.

- ⚠️ **A NINTH FIGURE OF MINE WRONG — AND WRONG IN BOTH DIRECTIONS AT ONCE.** I told chunk 31's
  reviewer "§41.4 now predicts 11 of 11". It is **13 of 13**: the reviewer censused the whole battle
  dump (**19 `どうやら`, 13 rendered, 6 untranslated** — chunks 15 ×3, 16, 23 ×2) and found
  **§41.4's own table listed 8 and missed `chunk_008` line 14**, so the rule was 9 of 9 when
  written, not 8 of 8. My number was too low AND the source table it came from was too low.
  Glossary §45.4. ⚠️ **§41.4's "with no exceptions" is STILL wrong** — the census was battle-only,
  and `batch_005.tsv` puts a plainly casual speaker (`俺たち`, `ラッキーだぜ`, `ｈａｓｎ’ｔ`) on the
  `ｉｔ　ｓｅｅｍｓ` side. Pre-existing and shipped; no rendering changes.

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
