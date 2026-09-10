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
> **WAVE 8 IS CLOSED — 5 of 5 merged, 0 parked, `check` green. Battle 32/44 (64.3%), script 57.4%.**
> The next act is to **OPEN WAVE 9'S SESSION**, which wave 8's coordinator does in the same turn.
>
> ```
> create_session(                                   # mcp__Claude_Code_Remote__create_session
>   title:           "Riot Stars — wave 9",
>   tags:            ["riotstars-translation", "wave-9"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-9 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit.
>
> ⚠️ **WAVE 9 IS SCRIPT-ONLY. BATTLE WORK IS FINISHED** until a human clears Blocked **0** or **0a**.
> ⚠️ **The run is NOT complete** — see Remaining. Do not report it complete.
>
> If this line still says "open wave 9" and no wave-9 session exists, the chain broke: open it.

## Last updated
2026-09-10 · by: **wave-8 coordinator** (`session_01GMZPvT2GCVmRBd8pwHPGED`) ·
wave: **8 CLOSED — 5 merged, 0 parked, 4 rework rounds across 3 units** · queue: **wave 9's script
batch must be RECOMPUTED against bank 40 = 75, not inherited**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | 0–4, 6–14, 18–22, 24, 25, 26, 30, 31, 33–35, **37**, **38**, 40, **41**, **42** |
| Battle JP characters | **27,763** | 43,161 | **64.3%** (was 56.5% at wave-8 start) |
| Script unique lines | **461** | 1,430 | `tl/script/batch_001–010.tsv` |
| Script message instances | **4,552** | 7,931 | **57.4%** (was 53.7%) |

`check`: **All checks passed** at `965ee18`. ⚠️ **Tightest banks after wave 8: 40 → 75, 41 → 353,
5 → 1,635, 2 → 2,993.** ⚠️ **Bank 40 and bank 5 are effectively CLOSED to further item-table work** —
every count-21 item line spends its growth in **all 21** of its banks, bank 40 included. **117 item
lines / 2,457 instances are stranded behind bank 40's 75 bytes.**
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact, Blocked 0),
**36** (charset gate, Blocked 0a).

## In flight
**Nothing. Wave 8 is closed and no PR is open.** Wave 9's session dispatches its own units.

## Next up — WAVE 9 (⚠️ SCRIPT-ONLY)
**Seed the glossary BEFORE dispatching.** Sections currently end at **glossary §51** and **FLAGS
§AM** — ⚠️ take the next number by **READING both files at commit time**, never by reserving.

**COMPUTE THE BATCH YOURSELF; DO NOT INHERIT ONE.** Re-run `python3 tools/queue.py script` against
the figures above, check feasibility **by INSTANCES not lines**, and hand the translator an explicit
**DATA line list** (state the convention: DATA = 1-based index among non-blank non-comment lines of
`dumps/script_unique.txt`; **FILE = DATA + 5**).
⚠️ **A line whose clause is ALREADY SHIPPED elsewhere costs the SHIPPED form's bytes**, not a fresh
optimal rendering's — §3 forces the byte-identical English. That is why wave 8's bank-40 estimate ran
14 bytes low (DATA 193/194 were already in `batch_003`). **Check each candidate line's clause against
shipped work before estimating.**
⚠️ **`軍神ヘルメス` / DATA 281 stays LIVE** (21 instances) and needs a **`魔法防御`** form nothing
fixes — but it lands in bank 40, so it may now be **unshippable**. **`ピクシー`** (DATA 817),
**`マーシュ`** (FILE 870, 1330, 1379) and **`小隊`** (FILE 524, 1389) also stay live.
**§4.3 debts for a corrections unit, none budget-blocked (all byte-negative):** `batch_007.tsv:31`
ships `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, the only capitalised bare plural in `tl/`; merged `chunk_000` ×3,
`chunk_008`, `chunk_031` still ship `Ｈｅｙ，` against §32.3's `Ｏｉ，` (four plain + one stammer).

## Remaining
**Battle: 0 dispatchable.** 8 chunks remain and **all are blocked** — 15, 23, 27, 28, 29, 39 by
§D1's dump artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's
measured **1.64×**).
⚠️ **`queue.py battle` will report "dispatchable 11" and is WRONG ON BOTH COUNTS**: its tier-A cutoff
is hardcoded **1.6** (§B2's floor is 1.64), and it knows **nothing** about §D1.

**Script: 969 unique lines / 3,379 instances untranslated**, of which **603 lines / 628 instances are
bank-FEASIBLE now** — about **12 more batches**. So CLAUDE.md §8's "no dispatchable unit left" does
**NOT** hold and the run continues. The other 366 lines (2,751 instances) are bank-blocked; **117 of
them are 21-instance item-table rows** held solely by bank 40.

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
⚠️ **RULINGS LIVE IN THEIR HOMES, NOT HERE** — `glossary.md` §23–**§51**, `FLAGS.md` §K–**§AM**,
`findings.md` §24, `pending/README.md`. Section numbers are taken by **READING both files at commit
time**, never reserved.

**Standing (waves 4–8).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×** (realised 2.118 over 408 lines). Seed the glossary
**before** dispatching. A **parked unit still gets the full reading review**. Name script batches by
**DATA line list**, never a `queue.py` position. A term is "in the glossary" only if a row **fixes an
English form**. A glossary row's **Alt column records REJECTED options**. `{FCC0}` is forbidden by
`assemble.py:tag_parity`, **not** by `rowcheck.py` (§Q2 — never patch it, never a finding).

**Wave 8 — the method findings. These are the wave's real product.**
- ⚠️ **GATE 7 MUST BE RUN FROM THE GLOSSARY SIDE, KEY BY KEY**, with controls in **both** directions
  (plant a key that IS present and one that is NOT). It was **5-for-5** at catching what every other
  gate passed. **THREE units failed on a glossary row whose own census NAMES THE EXACT LINE** (c37
  `やはり`, c42 `ははっ`, batch_010 `実権`). ⚠️ **But it cannot surface a word the glossary never
  recorded** — that is how `くそ` survived two rounds. **5-for-5 is not complete.**
- ⚠️ **§AG6's MIRROR (FLAGS §AL1/§AM3): "I measured the rejected alternative and never looked for the
  incumbent."** Before reaching for a new word, **search for the English the SOURCE WORD already
  has**. Operationalised as a sweep of every non-glossary kanji/katakana run against translated rows;
  on batch_010 it ran 33 runs, found no divergence, and **withdrew a wrong correction**.
- ⚠️ **GATE 6 PAIRS WHOLE MESSAGES AND MATCHES EXACT JAPANESE.** A unique row string, or a kana
  variant (`クソッ`/`くそっ`), is **structurally invisible** to it — demonstrated by negative controls
  that stayed silent while reverting real defects. **A clean gate 6 is not evidence of terminology
  consistency.** ⚠️ **Plant controls INSIDE the checker's coverage set** — one PR's control was
  planted where its checker never looked and proved nothing.
- ⚠️ **MEASURE THE REJECTED OPTION IN MORE THAN ONE WORD ORDER.** Two false impossibilities this
  wave; the first nearly parked a shippable unit. **An order-independent PACKING proof beats
  enumeration, and A TOTAL NEVER RESCUES A PACKING CLAIM** (89–92 columns against a 92 budget can
  still need five rows). **§AG6 also covers the PR body's own prose**, not just rejected options.
- ⚠️ **FIVE WRONG CORRECTIONS THIS WAVE, ONE OF THEM MINE, ONE DECLINED.** The traps: a **numbering
  convention** (DATA vs FILE, twice); a **correction note** — §48.3 reads 21 *plus a note that it
  once read 22*, and **a record documenting its own former error reads as though it still contains
  it**; **re-asserting a round-1 reading after the base moved** (§AL4); and **mine** — see below. The
  declined one: a reviewer nearly forced `復興` to the nominal form, then found `batch_009.tsv:72`
  already renders the bare noun **verbally**, so forcing it would have put the unit *out* of step.
- ⚠️ **A SHAPE CENSUS NEEDS ITS SPLITTER *AND* ITS DUMP.** I claimed `.TTTT.` "is not zero"; it **is**
  zero. §45.2 is a **battle-dump** census under `rowcheck`'s boundary set
  (`{FCC0}|{FC30}|{FC51}|{FC50}|{FFFF}`), where all five figures reproduce exactly — `.TTTT` 182,
  `.TTTT.` **0**, `TTTT` 389, `TTT` 115, `TT` 262. My `{FCC0}`-only split gave 126/3/133; the same
  `rowcheck` splitter over the **script** dump gives 325/1, and that single `.TTTT.` is a **menu
  choice-block**, not a text page. **Three right answers to three different questions.**
- **INFRASTRUCTURE (§AK6): worktree branch names are NOT per-agent and collide** — two worktrees held
  branch `review` at one commit, and one was rewritten between its own reviewer's rounds. ✅ **No gate
  needs a working tree**: `merge-tree --write-tree` for gate 2, a `git archive` extraction for the
  rest, `commit-tree` with a temporary index for integration. Four reviewers used it.
- **A reviewer can merge AND push `integrate:` while still showing "running"**, and a reviewer killed
  mid-run leaves **no trace in git**. **Never infer merge state from an agent's status.** A rejected
  non-fast-forward push is the mid-integration signal: **hold, re-export from the new head, re-apply,
  push — never force.**

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
| 8 | battle 37, 38, 41, 42 + script 010 | **5** | 0 | battle **32/44 (64.3%)**; script **461 (57.4%)** |

**Wave 8 detail.** PRs #29–#33, full three-role split, five separate reviewers, **5 merged / 0
parked** — the run's first clean sweep. Chunk 38 (5,577 / 8,192) and chunk 41 (3,035 / 8,192) took
one rework round; chunk 37 (5,037) and chunk 42 (3,627) took **three**; script `batch_010` (53 lines
/ **293 instances**, bank 40 447 → 75) took one. A **weekly rate-limit outage** (2026-09-09 16:30Z →
2026-09-10 18:00Z) killed one reviewer mid-run and cost ~26 hours; nothing was lost. Detail lives in
`glossary.md` §47–§51 and `FLAGS.md` §AI–§AM, not here.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (a plain
   `checkout` lands on a stale ref — see Run configuration), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; `ListAgents`, then reconcile
   open PRs (`git ls-remote --heads origin 'tl/*'`; ⚠️ `list_pull_requests` returns oversized bodies).
3. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8, and **"nothing dispatchable" does NOT hold** — see Remaining.
