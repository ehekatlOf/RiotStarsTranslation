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
> **WAVE 6 IS CLOSED — 4 of 4 merged, 0 parked. `check` green. Battle 26/44 (51.0%), script 53.1%.**
> The next act is to **OPEN WAVE 7'S SESSION**, which wave 6's coordinator does in the same turn.
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 7",
>   tags:            ["riotstars-translation", "wave-7"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-7 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Units: **battle chunks 30, 31, 36 + script
> `batch_009.tsv` = unique 534–583** — see **Next up**.
>
> If this line still says "open wave 7" and no wave-7 session exists, the chain broke: open it.

## Last updated
2026-09-09 · by: **wave-6 coordinator** (`session_013hHmA6EJT3rCC5wAiX6fwt`) ·
wave: **6 CLOSED — 4 merged, 0 parked, 1 rework round** · queue: **fresh, wave-7 batch pre-vetted**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **26** | 44 | 0–4, 6–14, 18–22, 24, 25, 26, 33, 34, 35, 40 |
| Battle JP characters | **21,998** | 43,161 | **51.0%** (was 43.2% at wave-6 start) |
| Script unique lines | **358** | 1,430 | `tl/script/batch_001–008.tsv` |
| Script message instances | **4,209** | 7,931 | **53.1%** |

`check`: **All checks passed** at `2bac521`. ⚠️ **Tightest banks: 41 → 353, 40 → 447, 5 → 2,007
(was 3,357 — batch 008 spent 1,350), 2 → 3,365**, 3 → 8,113, 33 → 9,291. Parked and translated:
chunks **5, 43** (tier-A budget) and **17** (dump artifact). ⭐ **The dumper is STILL unfixed** —
re-verified at the wave-6 close: `grep -n "FC70\|FCA8" tools/riotbattle.py` returns nothing.

## In flight
**Nothing. Wave 6 is closed and no PR is open.** Wave 7's session dispatches its own units.

## Next up — WAVE 7
**Four units. Seed the glossary BEFORE dispatching.** Sections currently end at **glossary §42** and
**FLAGS §AD** — ⚠️ FLAGS is on the **double-letter scheme**; take the next number by **READING both
files at commit time**, never by reserving.

**1–3. Battle chunks 30 (B 2.43), 31 (C 3.46), 36 (C 3.92)** — chapter order, all artifact-free.

**4. Script batch → `tl/script/batch_009.tsv` — COMPUTED AND VERIFIED at the wave-6 close, but
VERIFY IT YOURSELF ANYWAY (see Decisions).** `queue.py script` **position 6** = **unique 534–583**,
contiguous, **50 lines / 50 instances / 2,913 JP chars**.
- **0/50 scaffolding** (unanchored `[０-９]{2}：` on the **text** field). None already translated.
- **Banks 7, 8, 9, 10, 11, 12 ONLY** — it touches **none of the four tight banks**. After:
  b7 **12,978**, b8 **10,621**, b9 **12,150**, b10 **33,597**, b11 **39,308**, b12 **8,541**.
- ⚠️ **Positions 1–5 are ALL bank-negative** and must not be substituted: pos 1 (b5 −221, b40 −1,781),
  pos 2 (b5 −754, b40 −2,314), pos 3 (b40 −3,519), pos 4 (b40 −843), pos 5 (b5 −4,382). Position 6
  is the **first** viable batch. The item-description table (unique 127–313, 21 instances each) is
  still the highest-yield pool and still bank-40-blocked.
- ⚠️ **DATA 535 carries a forward binding** (FLAGS §AD): a sibling unique row with identical visible
  Japanese and a different key. Also at DATA 326, 329/330/394/400/412 and 403.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **15 open chunks.** ⚠️ **6 carry the §D1 dump artifact and will park exactly as chunk 17 did
— 15, 23, 27, 28, 29, 39**; **16 and 32 are tier-A blocked**. So only **7 are dispatchable**, in
chapter order: **30, 31, 36, 37, 38, 41, 42** — about **two more waves**, and then battle work stops
until a human fixes the dumper or the slot budget.

Script: **1,072 unique lines / 3,722 instances** untranslated. ⚠️ **Bank capacity, not the queue, is
now the binding constraint** — only queue position 6 fits. ⚠️ **Chunk 37 (a later wave) inherits
`FLAGS.md` §Y6**: Cress's gender is fixed nowhere and rendered nowhere in `tl/`.

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
**Rulings live in their homes**: `glossary.md` §23–§42, `FLAGS.md` §K–§AD, `findings.md` §24,
`pending/README.md`. ⚠️ **Section numbers are taken by READING both files at commit time, never
reserved.**
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured (waves 4–6 came in at 1.89×, 2.09×, 1.94×).
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not its story text.
- 2026-09-08: **seed the glossary BEFORE dispatching**; **a parked unit still gets the full reading
  review**; **the `queue.py` batch POSITION is not the filename**.
- 2026-09-09: **a term is "in the glossary" only if a row FIXES AN ENGLISH FORM.** A shared term and
  a strikeable §9 row are different things — wave 6 briefed `場所` as a cross-unit pairing when no
  row for it ever existed.
- 2026-09-09: **findings are proposals to verify in BOTH directions, and the verification is what
  works.** Wave 6: **five** coordinator seed figures were wrong and agents caught every one;
  **three reviewers refused an instruction of the coordinator's on measurement and were right each
  time**; and **two agent claims were wrong the other way** (`ｄｅｓｃｅｎｄａｎｔ` = 11, withdrawn by
  its own author; PR #24's faction row widths) and were refuted by measuring.
- 2026-09-09: ⚠️ **MECHANICAL TERM SEARCH HAS FOUR KNOWN BLIND SPOTS** (`FLAGS.md` §Y2, §AC1) —
  **mixed script** (`末えい`, `恨み`), **maximal runs** (`王位継承` never matches bare `王位`; `司教様`
  never matches `司教`), **full-katakana register transforms** (`マツエイ` for `末えい`), and
  **kana-script variants** (`フフ` vs `ふふ`). Search all scripts before calling a form new.
- 2026-09-09: **a glossary row's "Alt" column records REJECTED options, not a menu.** Chunk 25
  proposed `Ｈｅｈ　ｈｅｈ` for `フフ`; §12.3's own row already listed it as rejected.
- 2026-09-09: ⚠️ **MEASURE EVERY WIDTH WITH `len()`** (`FLAGS.md` §AC3). Hand-counted widths are the
  **only systematic error three waves running**: 14 of PR #23's 37 figures were wrong (13 one high,
  one — `Ｐｒｉｎｃｅ　Ｈｏａｇ` — one *low* in §9 and *wrong in three places at once*). **Every figure
  either party actually argued from was exact**; it is the unargued table cells that drift.
- 2026-09-09: **`{FCC0}` is forbidden by `assemble.py:tag_parity`, NOT by `rowcheck.py`** (which
  splits on it as a page boundary). The rule is unchanged; the coordinator misstated the cause in
  all five wave-6 dispatches. `FLAGS.md` §Q2 was already correct and was rightly not patched.
- 2026-09-09: **verify a handed-down batch's arithmetic even when told "already vetted".** Not
  re-deriving the *unit* and not re-checking its *figures* are different things.
- 2026-09-09: **serialised review is worth its wall-clock.** The `どうやら` register ruling stood at
  6 of 6 when made; chunk 26 merged during a rework and supplied an **eighth** instance landing
  exactly as predicted, from an independent unit and reviewer with no knowledge of the question.

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
| 6 | battle 24, 25, 26 + script 008 | **4** | 0 | battle **26/44 (51.0%)**; script **358 lines (53.1%)** |

**Wave 6 detail.** PRs #21–#24, full three-role split, four separate reviewers. **Three merged at
round 1; chunk 25 took one rework round** (`フフ` → the already-shipped `Ｆｕｆｕ`; bare `そして、` →
`Ａｎｄ，`), fixed in one line and landing at the reviewer's predicted byte exactly. Chunk 26 was the
**first unit of the run needing no figure correction at merge**. Detail lives in `glossary.md`
§39–§42 and `FLAGS.md` §AA–§AD.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (a plain
   `checkout` lands on a stale ref — see Run configuration), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; `ListAgents`, then reconcile
   open PRs (`git ls-remote --heads origin 'tl/*'`; ⚠️ `list_pull_requests` returns oversized bodies).
3. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8.
