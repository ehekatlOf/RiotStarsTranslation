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
> ### ✅ WAVE 11 IS CLOSED — 3 of 3 MERGED, 0 PARKED, 0 LOST, 0 RE-DISPATCHES. Script **61.7% → 63.6%**.
> **▶ WAVE 12'S SESSION IS BEING OPENED NOW by wave 11's coordinator (`session_012m7kST3Y5f2ag1jqg6pX8y`),
> in the same turn as this commit** (CLAUDE.md §4 step 7).
>
> ⚠️ **IF YOU ARE READING THIS AND NO WAVE-12 SESSION EXISTS, THE CHAIN BROKE — OPEN IT YOURSELF.**
> `create_session`, ⚠️ **`source_url` https://github.com/ehekatlOf/RiotStarsTranslation is REQUIRED
> alongside `source_revision` `claude/workflow-translation-iterate-uzlkns`** (it errors without it),
> prompt = the wave number + "read `HANDOFF.md` first" + the Next up list below. Nothing else is
> outstanding: **no open PR, no unmerged branch, no live agent, worktrees pruned, `check` green.**
>
> ✅ **NO UNIT IS SELF-REVIEWED AND THERE IS NO AUDIT DEBT.** Three units, three separate reviewers,
> none reviewing work it translated. The three-role split held throughout.
>
> ⚠️ **THE RUN IS NEAR ITS TRANSLATION END, AND WAVE 12 SHOULD SAY SO PLAINLY.** Only **116 of the
> 482 remaining lines are bank-feasible**, and **95 of those 116 are DEVELOPER DEBUG MENUS**. The
> other **366 lines / 2,751 instances — 95% of the remaining message instances — are BLOCKED behind
> the §F2 bank repoint**, which is a human task. After wave 12 there is essentially nothing left to
> translate that a player will ever see.

## Last updated
2026-09-11 · by: **wave-11 coordinator** (`session_012m7kST3Y5f2ag1jqg6pX8y`, depth 2) ·
wave: **11 CLOSED — 3 of 3 merged (PRs #42, #41, #40), 0 parked, 0 lost, 0 re-dispatches** ·
**wave 12 opened in the same turn** · queue below **re-derived by me after the merges, not inherited**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — battle is blocked, not idle |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **948** | 1,430 | `tl/script/batch_001–019.tsv` (was 803) |
| Script message instances | **5,041** | 7,931 | **63.6%** (was 61.7%) |

`check`: **All checks passed** at `c5f0d5b`. glossary ends **§60**, FLAGS ends **§AV** — both re-read
at commit time, never reserved. `build/*_dump_merged.txt` regenerated at the close (it had gone
**147 lines stale**; `assemble.py` reads only `tl/`, so no build was ever broken).
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 2 → 1,607 · 5 → 1,635.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE, so bank 5 is invisible to anyone quoting it.**
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight
**Nothing. Wave 11 is closed.** No open PR, no unmerged unit branch, no live agent. **Worktrees pruned
— all five removed, `git worktree list` shows only the main checkout.**
⚠️ **`tl/script-017`, `-018`, `-019` are MERGED but still on origin** — branch deletion returns
**HTTP 403** from the agent container (**FLAGS §AQ9**), as it has every wave. **"Branch gone = merged"
is an INVALID signal in this repo; use the `integrate:` commit and the PR's merged state.** Human fix:
enable *Automatically delete head branches*.

## Next up — WAVE 12 (⚠️ still script-only; battle stays blocked on Blocked 0 / 0a)
**COMPUTE YOUR OWN BATCHES.** Every figure here I re-derived at wave 11's close from
`script_unique.txt` + `script_dump.txt` + a fresh `merge`/`bankmeasure` — **482 unique lines /
2,890 instances remain untranslated** (was 627 / 3,035). Feasibility is per-line at 2.10× growth
with a 500-byte reserve: a line is feasible only if **every** bank it lands in can pay its growth.

| DATA | Lines | Inst | Banks | Verdict |
|---|---|---|---|---|
| **1043–1099** | **57** | 57 | 31 only (34,745 free, needs ~2,254) | ⚠️ **FEASIBLE — but a DEVELOPER DEBUG MENU.** Flag-toggle screens (`フラグ４をＯＮにします`). Near-zero player value. **Never batch with real dialogue.** |
| **997–1034** | **38** | 38 | 30 only (35,119 free, needs ~795) | ⚠️ **FEASIBLE — debug flag / sound test.** Same caution |
| **326–345** | **19** | **38** | 4,5,6,7,8,9,12,14,18 (tightest bank 5: 1,635 free, needs ~98) | ✅ **FEASIBLE and CHEAP.** ⚠️ **The inherited "pays its growth in every one of 18 banks" was WRONG — re-derived, it is 8–9 banks and ~98 bytes in the tightest.** Real item/UI table text |
| 318, 320 | 2 | 6 | 3, 32, 34 | ✅ feasible, leftovers to top a batch |
| **1160–1354** | **195** | 195 | **40 only** — needs ~11,073 against **75 free** | ⛔ **BLOCKED** |
| **1355–1387** | **33** | 33 | **41 only** — needs ~33,573 against **353 free** | ⛔ **BLOCKED** |
| 138 more | 138 | **2,523** | **135 blocked by bank 40, 3 by bank 5** | ⛔ **BLOCKED** — the item/armour description tables, 21 instances per line |

⚠️ **THE ARITHMETIC OF WHAT IS LEFT, AND IT IS THE HEADLINE:**
**116 of 482 lines are bank-feasible (139 instances). 366 lines / 2,751 instances are BLOCKED** —
that is **95% of the remaining message instances**, all behind the **§F2 bank repoint (Blocked 2)**.
And **95 of the 116 feasible lines are developer debug menus.** So wave 12's honest options are:
1. **the corrections unit** (below) — real quality gain, byte-negative, no new blockers;
2. **326–345 + 318/320** — 21 lines, 44 instances, the last genuinely player-facing text;
3. **the two debug-menu units** — completeness, near-zero player value;
4. **a final handoff** under CLAUDE.md §8 once 1–3 are done.
**§8's "no dispatchable unit left" does NOT hold yet** — but it is one or two waves away, and wave 12
should say so plainly in its own close rather than let a later wave discover it.

**A corrections unit is still worth a slot.** §4.3 debt in merged work, all byte-negative or free:
**§AP5** `chunk_000`'s three hyphen stutters (census 19 : 3) · **§AP7** `品` → `ｇｏｏｄｓ` at DATA 376 ·
**§AP9** a stale `トリフ` row, `batch_007.tsv:31`'s `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, and `Ｈｅｙ，` against
§32.3's `Ｏｉ，` in `chunk_000` ×3 / `chunk_008` / `chunk_031` · **§AQ5** `batch_007` renders `編成` as
BOTH `Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ` and `Ｆｏｒｍａｔｉｏｎ` · `batch_010` D897 ships `ｒｅｖｏｌｔ` for bare
`反乱` against §38.3's `ｒｅｂｅｌｌｉｏｎ`.

⚠️ **§9 / glossary ROWS THAT STAY LIVE AFTER WAVE 11** — each verified by a `tl/` grep at integration,
not by a reach census: `炎ノ雨`/`炎の雨` (**24 instances outstanding**, D223 alone ×21) · `兵器`
(D220, D221, D518, D520) · `貼り紙がしてある・・・` (**D333, D338 — never named before**) · `材料`
(D304, D305, D308) · `武器や防具` (D1354) · `店を出る` (**D339 ×2 — §7 named only two of three lines**) ·
`ほこら` (D324, bank 40) · `魔道書` (**D293 — 21 of its 23 instances, reaching 21 banks**) ·
`生き返りの秘法` (D324) · `親衛隊` (D1330, bank 40) · `マーシュ` · `クーデター` · `腕力` · `慰霊金` · `命中率`.
✅ **Discharged and exhausted by wave 11:** `また　どうぞ` · `いらっしゃいませ` · `荷物` · `体力` · `景品` ·
`ｃｏｉｎ`/`コイン` · `かじ屋` · `クロイ馬ノ騎士` · `ムーン` · `エウロス` · `部隊章` · `禁断のアンデッド` ·
`『フォースシールド』` · `『すごい魔術師に…なれる本』` · `『ようせいのケーキ』` · the casino terms.

## Remaining
**Battle: 0 dispatchable.** 8 chunks remain, **all blocked** — 15, 23, 27, 28, 29, 39 by §D1's dump
artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's 1.64×).
⚠️ **`queue.py battle` reports "dispatchable 11" and is WRONG ON BOTH COUNTS** — its tier-A cutoff is
hardcoded **1.6**, and it knows **nothing** about §D1.

**Script: 482 unique lines / 2,890 instances untranslated** after wave 11 (was 627 / 3,035).
**Feasible: 116 lines / 139 instances** — and 95 of those are debug menus. **Blocked: 366 lines /
2,751 instances**, i.e. **95% of the remaining instances**, behind the §F2 repoint. See Next up.

## Blocked — needs a human
8. 🎮 **NEW 2026-09-11 — NINE TUTORIAL SCREENS NEED EYES ON THE GAME (PR #36, FLAGS §AO1–AO3).**
   `tl/script/batch_013.tsv` adds one `{FFFE}` to each of **DATA 958–963, 968, 969, 970** because
   `assemble.py`'s column model does not split on the menu tags `{FFFA}`/`{FFF7}`/`{FFF6}`, so the last
   menu option and the text after the dispatch are measured as one 42-column row and `check` fails. The
   break sits at `{FB01}{FFFE}`, i.e. at the head of the fresh window. ⚠️ **The engine's own script never
   uses that position — 0 of 160 dispatch sites** (the alternative, `{FFFE}` *before* the dispatch, is
   5 of 160, so **neither placement is well attested** and the corpus cannot settle it). **What a human
   must do: open the tavern tutor, walk lectures 1–6, and look for a blank first row or a misaligned
   cursor gutter on those nine menu screens.** ✅ **Jump targets are NOT at risk** — verified at review:
   `{FFF6}` arguments are **message indices within the bank**, not byte offsets (five option→target pairs
   each land on exactly the lecture their label names), so inserting bytes moves nothing.
   **If it looks wrong the fix is one regex and zero bytes**: move each `{FFFE}` from after the dispatch
   to before it — measured at review to keep `check` green with byte-identical bank figures.
   ⚠️ **Needs the disc and an emulator, nothing else. Does not block any further translation.**
0b. ⛔ **NEW 2026-09-10 — THE RUN'S AUTOMATION IS OUT OF ROAD, AND THIS IS THE CHEAPEST FIX ON
   THIS LIST.** Every wave has run as a child session of the previous wave, and the platform caps
   that at **lineage depth 8**. Wave 9 is at the cap. `send_later` and `create_trigger` were both
   called and both returned `caller session is at lineage depth 8 (limit 8); cannot spawn or re-arm
   further child sessions`; `create_session` uses the same mechanism. **So wave 9 runs without a
   watchdog and cannot open wave 10 as a session.** ⚠️ **Nothing is wrong with the repository, the
   translations or the tools** — `check` is green and every gate still works. **Fix: a human opens
   wave 10 as a fresh top-level session** (any new Claude Code session on
   `claude/workflow-translation-iterate-uzlkns`), which resets the depth to 0 and restores both the
   chain and the three-role split. **Takes one action and needs no disc, EXE or emulator.** ⚠️ **The
   in-run fallback — an `orchestrator` subagent — WORKS BUT IS DEGRADED**: subagents cannot spawn
   subagents, so such a coordinator has no reviewer and self-reviews its own merges (wave 1's
   failure, four merges). **Prefer the human action; it is strictly better and nearly free.**
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
0. 🔧 **THE `tokenise` DUMP ARTIFACT — the highest-leverage item here.** `FLAGS.md` **§D1, §R**.
   ⚠️ **WIDENED 2026-09-10 (PR #35 review): THE SAME BUG IS IN `tools/riotscript.py` TOO, NOT ONLY
   `riotbattle`.** `riotscript.tokenise_stream` (lines 61–83) tests `is_sjis_lead(c)` **before** the
   tag branch and **has no argument-length table** — verbatim §R4's cause, in a second file. Verified
   directly, not inferred. **A fix that patches only `riotbattle` leaves this unfixed.** Census by
   signature detector, calibrated by reproducing §R2's recorded figure exactly: **24 in the battle
   dump, 1 in the script dump** (script DATA 367, `{FFED}{=03}閧{=A8}` = `FF ED 03 E8 82 A8`, where
   `E8` is a valid SJIS lead so two argument bytes decoded as text). ⚠️ **The script instance has NO
   SHIPPING IMPACT** — both JP and EN re-encode to the identical byte prefix, so nothing renders
   wrongly; it is dump-representation only. **So fix `riotbattle` first — that is what unblocks 8
   chunks — and `riotscript` alongside it, since it is the same three-line change.** The dumper prefers a Shift-JIS text run over a control tag whenever an argument byte
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

### ⭐ WAVE 11's LESSONS — three new method findings, all earned against real defects
**Detail lives in `glossary.md` §58–§60 and `FLAGS.md` §AT–§AV, not here.**

1. ⭐⭐ **GATE 7 IS BLIND TO NOTE CELLS — a NEW structural hole, and it let a real defect through.**
   `batch_018` rendered **`さ、` as `Ｎｏｗ，`**, which is **`さあ、`'s** settled English, putting two
   source strings on one English *inside one file*. `glossary.md` **does** hold them apart — but
   **`さ、` has 0 first-column keys and lives only in two Note cells** (measured: `grep -cE '^\| *`?さ、'`
   = **0**, `grep -c` = **2**), so a key-first gate 7 **saw 0 of 2 and could not find it**. Only the
   reading review caught it, from a shipped battle line carrying both in one speech. ⚠️ **This is
   sharper than §48.5's "a word the glossary never recorded": the glossary DID record it, in a cell
   the gate does not read.** Fix, both halves: **(1) extract `X` → `Y` pairs from NOTE CELLS as well
   as key cells; (2) promote such rulings to real first-column rows.** Done for `さ、` at §59.1.
2. ⭐ **"RE-DERIVING A REACH IS NOT RE-DERIVING A STATUS."** Coined by `batch_017`'s translator about
   its own error: it censused `体力`'s reach correctly (2 unique) and then asserted D834's *shipped*
   status **without ever grepping `tl/`**. There are **three** distinct questions — *where does it
   occur*, *where is it translated*, *has THIS instance shipped* — and each needs its own grep. The
   018 and 019 reviewers adopted it and it immediately caught two live rows about to be struck
   (`荷物`, and `店を出る`'s **D339, which §7 never listed**).
3. ⚠️ **CITATION ADDRESSING IS A TRAP, AND IT BIT TWICE.** A 0-based body index printed as a file line
   cost the 017 reviewer **three** wrong citations; the 018 reviewer then **sprang the same trap in
   the very review that cited it**. **State whether a number is a 0-based index or a 1-based file
   line, and check it against the file before writing it into `glossary.md`.**

⚠️ **FOUR COORDINATOR ERRORS, ALL MINE, ALL IN SEEDS OR DISPATCHES, ALL CAUGHT BY TRANSLATORS.**
`帝国`/`帝国軍` conflated · `炎ノ雨` censused in **katakana only** (`炎の雨` is 5 unique / 25 instances
and already shipped lowercase) · `的中確率`'s reason false (`命中率` is **same-store** and already
ships `ｈｉｔ　ｒａｔｅ`) · `ほこら` wrong **in both directions** (named D1105, which does not contain
the word; missed D1086/D1095). **Three of the four would have struck or mis-justified a glossary row
that must stay live.** ⚠️ **ALL FOUR ARE ONE SHAPE: I asserted one side of a comparison without
censusing the other** — the same shape wave 10 recorded thirteen times. **The seeding step needs the
same discipline the translating step has: census every reach cell in BOTH spellings and BOTH stores,
and mark an unverified cell unverified.** ⚠️ **The `イチバン` "0 battle, exhausted" cell in
`batch_019` was the identical katakana-only error, committed by a translator in the very PR that
caught mine** — `一番` ships `Ｓｔｒｏｎｇｅｓｔ　ｉｓ　ｈｉｇｈｅｓｔ．` in `chunk_010`. **The shape is
not personal; build the check into the method.**

✅ **QUALITY CONTROL RAN IN BOTH DIRECTIONS, AS IT MUST.** Translators corrected reviewers as often as
the reverse: the 017 translator fixed a wrong citation (and the reviewer found two more of its own);
the 018 translator corrected two widths and **its reviewer conceded the translator's string was
better than its own**, because the reviewer's `ｓｈａｌｌ` would have collapsed a §5 split its own
round-1 close had endorsed. **A reviewer's finding is never privileged over a translator's evidence.**

**Standing (waves 4–11).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×** (wave 11 realised **2.038** over 1,299 JP chars).
Seed the glossary **before** dispatching. A **parked unit still gets the full reading review**. Name
script batches by **DATA line list**, never a `queue.py` position. A term is "in the glossary" only if
a row **fixes an English form**; a row's Alt column records **REJECTED** options. Section numbers are
taken by **READING both files at commit time**, never reserved. **Runtime name/unit inserts take
singular *they***, never `ｈｅ`/`ｈｉｍ` (§58, §AT4) — the roster has women and the Japanese has no
pronoun. **Battle `tl/` holds NO Japanese, so grepping it is a null check** — pair the battle dump
positionally. **Gate 6 pairs whole messages on exact Japanese**, so a kana variant or a sub-message
term is structurally invisible; **a clean gate 6 is not evidence of terminology consistency.**
**`rowcheck.py:_script_cols` strips number/name inserts to ZERO columns** — hand-measure those rows
(§AQ8, corrected this wave to **68 rows, max +17** at D1420). **`{FCC0}` is forbidden by
`assemble.py:tag_parity`, not `rowcheck.py`** (§Q2 — never patch it, never a finding). **No gate needs
a working tree**; **pin the merge base to an explicit SHA** — the branch moved under the 017 reviewer
between two consecutive `merge-tree` calls. **Never infer merge state from an agent's status**: a
reviewer merges *and* pushes `integrate:` while still showing "running" (seen on all three units this
wave), and **branch deletion returns HTTP 403** (§AQ9), so a surviving branch proves nothing. A
rejected non-fast-forward push is the **mid-integration signal**: hold, re-fetch, re-apply, **never
force**. **Settled conventions, never findings:** DATA vs FILE · 0-based vs 1-based · the gutter
census · §45.2's `.TTTT.` is BATTLE-scoped · **breaks vs segments** are two conventions over identical
data · gate-7 key counts vary with splitter and struck-row handling — **state your corpus**.

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
| 9 | script 011, 012, 013 (**script-only — battle exhausted**) | **3** | 0 | battle 32/44 (64.3%); script **640 (59.7%)** |
| 10 | script 014, 015, 016 (**script-only**, DATA 707–869) | **3** | 0 | battle 32/44 (64.3%); script **803 (61.7%)** |
| 11 | script 017, 018, 019 (**script-only**; DATA 1100–1159, 1388–1430, 465–879 leftovers) | **3** | 0 | battle 32/44 (64.3%); script **948 (63.6%)** |

**Wave 9 detail.** PRs #34–#36, **3 merged / 0 parked**, the run's second clean sweep and the
first for a script-only wave. Five separate reviewers, three-role split intact throughout — **wave 10
owes NO independence audit.** `batch_013` merged on **round 1**; `batch_011` took 2 rounds;
`batch_012` took **all 3 permitted rounds** and merged on the last. +179 unique lines, +181 instances.
Translators ran 52 min – 1 h 34 m, reviewers 29–43 min, reworks 4–20 min. Nothing was lost to a dead
agent and no unit needed re-dispatching. ⚠️ **The wave ran WITHOUT A WATCHDOG** — `send_later` and
`create_trigger` are both refused at lineage depth 8 (Blocked 0b); background-subagent completion
notifications carried the whole run and none was missed. Detail lives in `glossary.md` §52–§54 and
`FLAGS.md` §AN–§AP, not here.

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

¹ 1,299 = all readable characters after tag-strip. The dispatch said 1,109 (kana+kanji only).
Both are true of their own corpus; growth is calibrated on 1,299. Not an error — state the convention.
