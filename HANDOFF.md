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
> ✅ **WAVE 9 IS CLOSED — 3 of 3 merged, 0 parked, `check` green. Script 640/1,430 lines, 59.7%.**
>
> ✅ **WAVE 10 OPENS AS A GENUINE TOP-LEVEL SESSION, FROM THE RUN'S ROOT SESSION. THE DEPTH-8 CHAIN
> IS RETIRED.** `session_018YepyHo7ky7emoUMicnUcL` — the run's original runner, **lineage depth 0**,
> outside the cap that stopped wave 9 — is opening it. Verified against the session record, not
> taken on the message alone: web origin, **no parent session**, created 2026-09-08 before wave 1,
> same environment and branch. A wave 10 opened from there is **depth 1**, so it has a full tool
> surface: its own translators, its own **independent reviewer**, its own watchdog, and it can open
> wave 11. **The three-role split is intact and no human action is required.**
>
> ⛔ **THE §7.2 SUBAGENT FALLBACK WAS STOOD DOWN, AND IT MERGED NOTHING.** Wave 9's coordinator
> spawned an `orchestrator` subagent when `create_session` failed, then stopped it on the root
> session's instruction. **It got as far as preflight and survey and pushed one `HANDOFF.md` commit
> (`8fb09ad`); it created no branch, opened no PR, and wrote nothing to `tl/`, `glossary.md` or
> `FLAGS.md`.** Verified from `git log`, `git status`, `git ls-remote` and `git diff --stat`, not
> from the agent's own report. **Therefore NO unit is SELF-REVIEWED and NO audit debt exists.**
> `check` is green at that commit.
>
> ⭐ **ONE FACT THAT SUBAGENT ESTABLISHED EMPIRICALLY, worth keeping: a subagent really does have NO
> spawn tool.** It tested its own surface rather than assuming — `SendMessage`, `Monitor`, `TaskStop`
> and **no `Task`**. CLAUDE.md's claim that "subagents cannot spawn subagents" is now verified rather
> than inherited, which is exactly why the §7.2 fallback costs review independence and why a real
> session is worth waiting for.
>
> **Wave 10's coordinator: compute your own units.** The stood-down subagent's survey proposed
> batches **014/015/016 = DATA 707–856** and recomputed the feasible queue at **424 lines / 447
> instances**. ⚠️ **That is a LEAD, NOT A QUEUE — re-derive it.** It is close to wave 9's own close
> figure (427/450) but was measured by an agent that did not finish; and every dispatch in this run
> warns against inheriting a line list.
>
> ⚠️ **WAVE 10 IS SCRIPT-ONLY.** Both battle blockers were re-tested **twice** on 2026-09-11 — at
> wave 9's close and again at the subagent's preflight — and **both are still unfixed**:
> `grep -n "FC70\|FCA8" tools/riotbattle.py` returns no hits; `riotscript.tokenise_stream` still
> tests `is_sjis_lead` before the tag branch with no argument-length table; and
> `assemble.py:validate_body` still applies its charset whitelist with no dump-identical exemption.
> All 8 remaining battle chunks stay blocked.
>
> ⚠️ **The run is NOT complete** — ~424–427 lines stay bank-feasible, roughly 8–9 batches.

## Last updated
2026-09-11 · by: **wave-9 coordinator** (`session_01DFhp3iVua6qbKN4QhBJvPP`) ·
wave: **9 CLOSED — 3 of 3 merged, 0 parked, 0 lost, 0 re-dispatches** ·
**wave 10 handed to the ROOT session as a top-level spawn; the §7.2 subagent was stood down having
merged nothing** · queue: **424–427 lines / 447–450 instances bank-feasible — re-derive, do not inherit**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — battle is blocked, not idle |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **640** | 1,430 | `tl/script/batch_001–013.tsv` (was 461) |
| Script message instances | **4,733** | 7,931 | **59.7%** (was 57.4%) |

`check`: **All checks passed** at `2648372`. glossary ends **§54**, FLAGS ends **§AP**.
⚠️ **TIGHTEST BANKS: 40 → 75, 41 → 353, 2 → 1,607, 5 → 1,635.** ⚠️ **BANK 2 IS NEW TO THIS LIST** —
it was 2,993 before wave 9 and `batch_012` spent 1,386 of it. It is now the **third**-tightest bank
in the game and is no longer comfortable. Banks 40 and 41 still have a spendable budget of **zero**
(free < the 500-byte reserve), so any line touching either remains blocked outright.
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight
**Nothing. Wave 9 is closed (3 of 3 merged, 0 parked) and wave 10 has not started.**
No PR is open, no unit branch is unmerged, and no coordinator is working this repo.
⚠️ **Exactly one coordinator works the repo at a time (CLAUDE.md §4).** Wave 9's coordinator has
ended; wave 10's top-level session is the next and only writer.

## Next up — WAVE 10 (⚠️ STILL SCRIPT-ONLY unless a human clears Blocked 0 / 0a)
**Seed the glossary BEFORE dispatching.** Sections end at **glossary §54** and **FLAGS §AP** —
⚠️ take the next number by **READING both files at commit time**, never by reserving. Wave 9's own
seeds went into **§9 PROVISIONAL**; the ones its units spent are struck.

**COMPUTE YOUR OWN BATCHES. This table is a starting point, not a queue** — it was measured at
wave 9's close (2026-09-11) and the bank figures move with every merge.

**790 lines / 3,198 instances untranslated. 427 lines / 450 instances are bank-feasible**; of those,
**six are GIANT single lines** worth checking before batching:

| DATA | Growth | Bank | Verdict |
|---|---|---|---|
| 518, 519, 520 | 2,722 / 1,713 / 1,954 B | 5 | ⛔ **NOT shippable** — 6,389 B against bank 5's 1,135 spendable. These three are the *sole* reason bank 5 shows as over budget. |
| 744 | 1,391 B | 19 | ✅ feasible — bank 19 has room |
| 863 | 2,935 B | 23 | ✅ feasible — and it carries `『獅子の勲章』`, whose glossary row is **held live** for it |
| 865 | 1,476 B | 23 | ✅ feasible |

**Clusters of the remaining 421 workable lines:**

| DATA | Lines | Banks | Growth | What it is |
|---|---|---|---|---|
| 707–879 | **170** | 18–25 | ~18,183 B | **continues wave 9's `batch_011` scene** — town, shops, NPCs. The obvious next 3 batches. |
| 1043–1159 | 117 | 31–39 | ~9,756 B | ⚠️ **1043–1105 is a DEVELOPER DEBUG MENU** (sound test, flag toggles); **1106–1159 is real dialogue**. **Split it; do not batch them together.** |
| 1388–1430 | 42 | 42, 43 | ~2,978 B | casino: slots, medal exchange, prizes — player-facing |
| 997–1034 | 38 | 30 | ~795 B | ⚠️ debug flag/sound test again — near-zero player value |
| 326–345 | 19 | 18 banks | ~2,156 B | ⚠️ **38 instances from 19 lines across 18 banks** — pays its growth in every one |
| 584–598 · 521–533 · 465–469 | 15 · 13 · 5 | 12 · 6,7 · 3 | small | leftovers, good for topping a batch to 40–60 |

**Terms already owed to later units** (from wave 9's merged rows, so they are BINDING, not proposals):
`『獅子の勲章』` → `“Ｍｅｄａｌ　ｏｆ　ｔｈｅ　Ｌｉｏｎ”` (DATA 863) · `クーデター` → `ｃｏｕｐ` (863, 1373) ·
`ブラックジャック` → `Ｂｌａｃｋｊａｃｋ` (1390, 1395, 1416) · `スリ` → `ｐｉｃｋｐｏｃｋｅｔ` (286, 518, 520,
714) · `工房` → `ｗｏｒｋｓｈｏｐ` (744, 788, 1346, 1364, 1365) · `行商` → `ｐｅｄｌａｒ` (806) · `町長` →
`ｔｏｗｎ　ｅｌｄｅｒ` (1102) · `ベルナール教会` → `Ｂｅｒｎａｒｄ’ｓ　ｃｈｕｒｃｈ` (910) · `ピクシー` →
`Ｐｉｘｉｅ` (DATA 817 — **inside 707–879**, so wave 10 probably discharges it) · `マーシュ` (FILE 870,
1330, 1379) · `小隊` (FILE 524, 1389).

**A corrections unit is now worth a slot.** §4.3 debt in **merged** work, all byte-negative or free:
**FLAGS §AP5** — `chunk_000.txt` ships three hyphen stutters (`Ｗｈ‐ｗｈａｔ`, `Ｎ‐ｎｏｗ`, `Ｔｈ‐ｔｈｉｓ`)
against §23.2's comma convention (census **19 : 3**); **§AP7** — `品` → `ｇｏｏｄｓ` at DATA 376 against
§34.1's `ａｒｔｉｃｌｅ`, fix measured at +6 B into a bank with 31,431 free; **§AP9** — a stale §9
`トリフ` row four merged units already render; `batch_007.tsv:31`'s `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, the only
capitalised bare plural in `tl/`; and merged `chunk_000` ×3, `chunk_008`, `chunk_031` shipping
`Ｈｅｙ，` against §32.3's `Ｏｉ，`.

## Remaining
**Battle: 0 dispatchable.** 8 chunks remain, **all blocked** — 15, 23, 27, 28, 29, 39 by §D1's dump
artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's 1.64×).
⚠️ **`queue.py battle` reports "dispatchable 11" and is WRONG ON BOTH COUNTS** — its tier-A cutoff is
hardcoded **1.6**, and it knows **nothing** about §D1.

**Script: 790 unique lines / 3,198 instances untranslated**, of which **427 lines / 450 instances are
bank-feasible** (421 after setting aside the three unshippable bank-5 giants) — roughly **8–9 more
batches**. CLAUDE.md §8's "no dispatchable unit left" does **NOT** hold; the run continues.
The other 363 lines (2,748 instances) are bank-blocked, **117 of them 21-instance item-table rows
held solely by bank 40's 75 free bytes**.

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
⚠️ **RULINGS LIVE IN THEIR HOMES, NOT HERE** — `glossary.md` §23–**§51** plus the **§9 PROVISIONAL**
seed tables, `FLAGS.md` §K–**§AM**, `findings.md` §24, `pending/README.md`. Section numbers are
taken by **READING both files at commit time**, never reserved.

**Standing (waves 4–9).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×** (realised 2.118 over 408 lines). Seed the glossary
**before** dispatching. A **parked unit still gets the full reading review**. Name script batches by
**DATA line list**, never a `queue.py` position. A term is "in the glossary" only if a row **fixes an
English form**. A glossary row's **Alt column records REJECTED options**. `{FCC0}` is forbidden by
`assemble.py:tag_parity`, **not** by `rowcheck.py` (§Q2 — never patch it, never a finding).

**⚠️ WAVE 9's OWN FINDING — MY DISPATCH TABLE PRODUCED A FALSE POSITIVE. Carry this into every
future dispatch.** I gave all three translators a "shipped clause" table built by splitting shipped
pairs on `{FFFE}`/`{FCC0}`/`{FC30}`/`{FC51}`/`{FC50}` and aligning clauses **positionally**. On
`いらっしゃいませ！！` it asserted a corpus distinction (`Ｃｏｍｅ　ｉｎ！！` vs `Ｗｅｌｃｏｍｅ！`) that
**does not exist**. `batch_011`'s translator rejected it by reading; PR #34's reviewer then proved
it independently: the form occurs **twice in the whole corpus** — bank 16 (this unit) and bank 26
(`batch_010` D885) — and D885 is exactly the message §34.5's **reserve** covers, licensed only
because `カジノへ　ようこそ！` sits on the adjacent row. **The table learned a rule from a sample of
one, and the real conditioning variable was the bank.** The cause is **generic**: positional
alignment infers a rule from whichever instances happen to be translated, and a term whose only
shipped instance sits under a documented reserve will look like a fixed distinction.
✅ **The mitigation worked** — every dispatch labelled the table "a LEAD TO VERIFY BY READING, never
a ruling", and that is exactly what the translator did. **Keep that framing, and additionally mark
any row backed by a SINGLE shipped instance as such.**

⭐ **WAVE 9's BEST PROCESS ARTIFACT — A NEW GATE THAT CLOSES A REAL HOLE IN GATE 6. Put it in
every future dispatch.** Gate 6 pairs whole messages on exact Japanese, so **two units coining
different English for the same `『…』` item name are structurally invisible to it** — which is
exactly how `『進化の木の実』` shipped as `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”` in `batch_011` and
`“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”` in `batch_013`, caught only by a reviewer **after the first had merged**.
`batch_013` then built the missing check: **pair every `『…』` in a message with the `“…”` spans in
that same message, and compare those pairings ACROSS FILES.** On its own unit: 17 names, 4 shared
with other files, 0 divergences. **Cheap, mechanical, and it would have caught this before delivery.**

⚠️ **GATE 8's "`{FFFF}` last on every message" IS A BATTLE-STORE RULE AND DOES NOT APPLY TO SCRIPT
UNITS** — my dispatches mis-scoped it onto all three. Verified: `dumps/script_unique.txt` contains
**0** `{FFFF}` (the dump has 8,760; the unique keys omit the trailing one, per CLAUDE.md §4 step 1),
and `batch_003`/`004`/`005` each carry the line *"Japanese keys are copied byte-for-byte from
script_unique.txt, i.e. without `{FFFF}`"* — **the repo documents this in three places.** PR #35's
reviewer caught it as its own instrument being wrong and said so rather than reporting a failure.

⚠️ **WAVE 9's SEVEN WRONG FIGURES — THE FULL TALLY, WITH ATTRIBUTION, EACH VERIFIED BY ME.**
Recorded because a later summary of this run attributed them **4 translators / 3 reviewers**, and
that is not what the record shows. The verified breakdown is **1 coordinator, 2 translators,
4 reviewers**:
| # | Figure | Source | Caught by |
|---|---|---|---|
| 1 | the `いらっしゃいませ！！` clause-alignment table (a rule inferred from a sample of one) | **coordinator (mine)** | the translator, by reading |
| 2 | `バニシュジュエル` 13 / 15 (true: **12 / 14**) | translator | coordinator |
| 3 | the `ベルナール教会` "promotion" — a row that was never provisional | **reviewer** | the translator, by declining |
| 4 | `こおりのゆびわ` "corrected" 10 → 12 (true: **10**) | translator | coordinator |
| 5 | the `で、` census run with a "starts with" matcher, returning the opposite of the truth | **reviewer** | itself, by re-censusing whole rows |
| 6 | net "+4 bytes" (true: **+2**) | **reviewer** | the translator |
| 7 | the stutter census "21 : 0" (true: **19 : 3**) | **reviewer** | the translator, by reading all 45 hits |
⚠️ **The source shifted across the wave: the early errors were translators', the last three were
reviewers'.** **Quality control here is NOT one-directional, and review dispatches must stop
implying it is.** A reviewer's finding is not privileged over a translator's evidence — #3 would have
written a fabricated entry into `glossary.md` had the translator complied instead of checking.

⚠️ **ALL SEVEN SHARE ONE SHAPE: someone measured ONE SIDE of a comparison and inferred the other.**
The clause table measured shipped English without counting how many instances backed it; the `で、`
census matched one way; the `バニシュジュエル` fix re-measured the source but not the replacement;
the `こおりのゆびわ` fix re-measured the value it corrected *from*, not *to*. **The operational rule
is mechanical, not a counsel of care: `len()` BOTH values and PRINT BOTH before asserting either is
wrong.** I hand-counted `Ｌｅｃｔｕｒｅ` as 8 letters (it is 7) while checking a translator's figure,
and only measuring stopped an eighth error being mine.

**Method findings (wave 8, still binding — these are what the dispatches carry).**
- ⚠️ **GATE 7 RUNS FROM THE GLOSSARY SIDE, KEY BY KEY**, with controls in **both** directions.
  **5-for-5** at catching what every other gate passed; **three units failed on a glossary row whose
  own census NAMES THE EXACT LINE**. Require the **key count** as evidence — "no findings" is not
  evidence. ⚠️ **It cannot surface a word the glossary never recorded** (how `くそ` survived twice).
- ⚠️ **§AG6's MIRROR: "I measured the rejected alternative and never looked for the incumbent."**
  Before reaching for a new word, **search for the English the SOURCE WORD already has**. Wave 9's
  seeding hit this twice: `ウエイト` already ships as `Ｗａｉｔ　ｔｉｍｅ` in `chunk_000`, and a drafted
  `素早さ` → `Ａｇｉｌｉｔｙ` would have contradicted **five shipped class rows** reading `ｓｐｅｅｄ` /
  `ｓｗｉｆｔ`. Both were caught before commit; the row was dropped.
- ⚠️ **GATE 6 PAIRS WHOLE MESSAGES AND MATCHES EXACT JAPANESE.** A unique row string or a kana
  variant (`クソッ`/`くそっ`) is **structurally invisible** to it. **A clean gate 6 is not evidence of
  terminology consistency.** Plant controls **inside** the checker's coverage set and **state the
  coverage**. Battle `tl/` holds no Japanese (grep is a null check); **script TSVs keep Japanese in
  column 2, so a column-2 comparison IS valid there.**
- ⚠️ **MEASURE THE REJECTED OPTION IN MORE THAN ONE WORD ORDER.** Two false impossibilities in wave
  8; the first nearly parked a shippable unit. **An order-independent PACKING proof beats
  enumeration, and A TOTAL NEVER RESCUES A PACKING CLAIM.** §AG6 covers the PR body's own prose too.
- ⚠️ **VERIFY CORRECTIONS IN BOTH DIRECTIONS — a wrong correction enters the record as fact.** Five
  in wave 8. The traps that fired: a **numbering convention** (DATA vs FILE, twice); a **correction
  note** (a record documenting its own former error reads as though it still contains it);
  **re-asserting a round-1 reading after the base moved**; and **a shape census quoted without its
  corpus** — a census needs its **SPLITTER *and* its DUMP**.
- **INFRASTRUCTURE (§AK6): worktree branch names are NOT per-agent and collide.** ✅ **No gate needs
  a working tree:** `git merge-tree --write-tree` for gate 2, a `git archive` extraction for the
  rest, `commit-tree` with a temporary index for integration. **Say which tree you gated and how.**
- **Never infer merge state from an agent's status.** A reviewer can merge *and* push `integrate:`
  while still showing "running"; one killed mid-run leaves **no trace in git**. A rejected
  non-fast-forward push is the mid-integration signal: **hold, re-export, re-apply, push — never
  force.** (Hit once in wave 9, on the seed commit: wave 8's coordinator had pushed a HANDOFF line
  after opening this session. Rebased, verified only `glossary.md` moved, pushed.)

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
