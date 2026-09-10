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
> ⛔ **THE RECURSIVE-SESSION CHAIN HAS HIT ITS CEILING AT WAVE 9. A HUMAN MUST START WAVE 10.**
> **`send_later` AND `create_trigger` BOTH FAIL** from this session with:
> `caller session is at lineage depth 8 (limit 8); cannot spawn or re-arm further child sessions`
> — tested directly 2026-09-10, both tools, not inferred. Each wave has been a child of the last,
> so wave 9 is the 8th descendant and **the last link this design can produce.** Consequences:
> 1. **THERE IS NO WATCHDOG ON WAVE 9.** CLAUDE.md's "the timer is always armed" cannot be
>    satisfied — the tool refuses. Wave 9's only wake mechanism is background-subagent completion
>    notifications, which do work, but have **no backstop** if one is swallowed.
> 2. **WAVE 10 CANNOT BE A NEW SESSION OPENED FROM HERE.** `create_session` is the same lineage
>    mechanism and is expected to fail identically.
>
> **What a human should do: open wave 10 as a FRESH TOP-LEVEL SESSION** (depth 0) from
> `https://github.com/ehekatlOf/RiotStarsTranslation`, `source_revision`
> `claude/workflow-translation-iterate-uzlkns`, seeded per SKILL.md §6a with the units in **Next
> up**. That restores the full chain *and* the three-role split, and costs nothing else.
>
> **What wave 9 does if no human appears:** `.claude/agents/orchestrator.md` §7.2's documented
> fallback — an `orchestrator` **subagent**, `run_in_background: true`. ⚠️ **This is a REAL
> DEGRADATION, not an equivalent:** CLAUDE.md's own banner says a coordinator running as a subagent
> **has no `Task` tool**, so it cannot spawn a reviewer and the three-role split collapses into one
> agent that dispatches, judges and merges its own wave. **That happened in wave 1 and cost the
> independence of four merges.** If that fallback is taken, every unit it merges is **SELF-REVIEWED**
> and owes an independent post-merge audit (CLAUDE.md §8).
>
> ✅ **WAVE 9 ITSELF IS UNAFFECTED.** Its translators are subagents of this session, which *does*
> have `Task`, so the reviewer can be spawned and the three-role split is intact for this wave.
>
> **WAVE 9 IS RUNNING — 3 script batches dispatched, behind the wave barrier (CLAUDE.md §4a).**
> Coordinator: `session_01DFhp3iVua6qbKN4QhBJvPP`. Base `ff3295a` (glossary seeds) on
> `claude/workflow-translation-iterate-uzlkns`.
>
> **Units — computed this wave, not inherited. All three ranges are fully contiguous (no gaps).**
> DATA = 1-based index among non-blank, non-comment lines of `dumps/script_unique.txt`;
> **FILE = DATA + 5** (verified this wave at DATA 1→FILE 6 and DATA 1430→FILE 1435).
>
> | Unit | DATA | Lines / inst | Banks (cost / budget) | Theme |
> |---|---|---|---|---|
> | `batch_011` | 647–706 | 60 / 60 | 14–18, max 14% | town & shop NPCs, the frog merchant |
> | `batch_012` | 355–415 | 61 / 63 | 0,1,2,42,43 — **bank 2 1,597/2,493 = 64%** | main plot (the coup) + casino |
> | `batch_013` | 921–978 | 58 / 58 | 28,29, max 37% | tavern, item shop, tactics lectures |
>
> **Next step: wait for all three PRs (the §4a barrier), then one reviewer at a time in unit order.**
> If a translator returns with no PR, re-dispatch that unit (2 attempts, then park).
>
> ⚠️ **The run is NOT complete** — 603 bank-feasible script lines remain, ~12 batches. See Remaining.
> ⚠️ **Battle is finished until a human clears Blocked 0 or 0a.** Both re-tested at this wave's
> preflight 2026-09-10: **still unfixed** (`grep FC70\|FCA8 tools/riotbattle.py` → no match;
> `assemble.py:validate_body` still charset-checks preserved source text).

## Last updated
2026-09-10 · by: **wave-9 coordinator** (`session_01DFhp3iVua6qbKN4QhBJvPP`) ·
wave: **9 RUNNING — glossary seeded (`ff3295a`), 3 batches dispatched, awaiting the §4a barrier** ·
queue: **recomputed this wave; my bank accounting reproduces `queue.py`'s 603/628 exactly**

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
| Unit | Branch | PR | Round | State |
|---|---|---|---|---|
| `batch_011` — town & shop NPCs, DATA 647–706 | `tl/script-011` @ `855686e` | **[#34](https://github.com/ehekatlOf/RiotStarsTranslation/pull/34)** | **2** | ⚠️ **ROUND 1 → CHANGES, 1 finding. Rework sent to the same translator 2026-09-10.** Every §6 gate green with pasted evidence; every PR figure reproduced under `len()`. Gate 7: **2,269 keys, 110 occurring, 0 failures**, incl. 5 rows whose glossary text names this unit's exact lines. Reviewer gated **no working tree** — `merge-tree --write-tree` → `f6fb779`, `git archive` extraction, provenance by `cmp` + sha256 against `git show`. **The finding:** D689 drops the additive `も` of `当店も大繁盛` that the SAME speaker's near-twin D690 renders `，　ｔｏｏ` four rows later — not budget- or geometry-forced (bank 16 has 10,963 free), and the unit's own practice carries 2 of the 3 additive `も` in its source. Fix is a repack, +10 bytes, no tag or break change. **Flags 1, 2, 3 and 9 were adjudicated IN THE TRANSLATOR'S FAVOUR and need no work.** PR unmerged, integration branch untouched at `0a462db` — verified from `git log`, not from agent status. |
| `batch_012` — main plot + casino, DATA 355–415 | `tl/script-012` @ `b7cb51e` | **[#35](https://github.com/ehekatlOf/RiotStarsTranslation/pull/35)** | 1 | ✅ **PR OPEN**, 1 file / 92 additions (gate 1 pre-verified). 61 lines / 63 inst, 0 parked. **Bank 2 landed at 1,607 free** — growth 1,386 against the 2,493 spendable, realised **2.02×**, under the 2.10× model. Gate 6 **0 failures** (22 pairs + 4 groups, controls both ways); gate 7 **83 keys / 151 key-row pairs, 0 failures**. All wave-9 seeds used **exactly as seeded**; `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` rendered ×4; **DATA 362 names no card, by design** (as dispatched). ⚠️ **Reviewer:** (a) **DATA 367 carries a DUMP ARTIFACT** — `{FFED}{=03}閧{=A8}`, a raw SJIS pair the dumper split, preserved verbatim; **check whether this is a new instance of Blocked 0 / §D1's class** and file it there if so; (b) §46.3's census is **short a cell** — bank 1 holds both `そうか・・・・` (D390) and `なるほど` (D391); (c) §32.5's `勲章`/`メダル` collision is now **realised**, bank 42 carrying a shipped racetrack `ｍｅｄａｌ`; (d) its **reading review caught a defect gate 7 passed** — D391's `王女様` drafted as `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ`, corrected to `Ｐ‐Ｐｒｉｎｃｅｓｓ．．．．！？`; (e) new terms incl. `閣下` → `Ｈｉｓ　Ｅｘｃｅｌｌｅｎｃｙ` (**deliberately NOT collapsed onto §1's `様` → `Ｌｏｒｄ`**), `『獅子の勲章』` → `“Ｍｅｄａｌ　ｏｆ　ｔｈｅ　Ｌｉｏｎ”` (**reach includes untranslated DATA 863**), `政務大臣`, `ホッジス` → `Ｈｏｄｇｅｓ` |
| `batch_013` — tavern + tactics lectures, DATA 921–978 | `tl/script-013` @ `553087f` | **[#36](https://github.com/ehekatlOf/RiotStarsTranslation/pull/36)** | 1 | ✅ **PR OPEN**, 1 file / 86 additions. 58/58 lines, 0 parked. Banks 28 (+246) and 29 (+8,704), 30,491 / 16,885 free. Gate 7 swept glossary-side: **1,094 rulings, 44 applicable, 41 matched, 3 read and dismissed**. Held the three Wait-forms apart and **verified `待機` occurs 0× in its source**, so `“Ｗａｉｔ”` could not have collided. ⚠️ **Reviewer, in this order:** (a) **FLAG 1 — it ADDED NINE `{FFFE}` TO MAKE `check` PASS.** `assemble.py`'s column model does not split on the menu tags `{FFFA}`/`{FFF7}`/`{FFF6}`, so the last menu option and the following prose measure as ONE row — 19/15 columns in Japanese (passes), 42/37 in English (fails). **This is the column-side twin of FLAGS §V7's row-side artifact, but §V7 only warns while this one FAILS THE GATE**, so it could not be left alone. Its safety evidence is unusually good — jump arguments proven to be **message indices, not byte offsets**, and `{FCC0}{FFFE}` occurring 553× vs 208× for `{FCC0}`-then-text, with `{FC50}/{FC51}`-then-`{FFFE}` at **0 of 1,193** as a discriminating negative. **Still wants a human in front of the game** → Blocked list. (b) **FLAG 6 — IT CORRECTED MY SEED, AND IS HALF RIGHT. I RE-MEASURED BOTH DIRECTIONS:** ✅ **its substance is RIGHT** — D946's source **is** `『バニシュジュエル』`, quoted, so my seed's "unquoted in its source" was **my error** and `“Ｖａｎｉｓｈ　Ｊｅｗｅｌ”` is correct; ❌ **its two figures are WRONG** — `len()` gives bare **12** (my seed's figure, right) and quoted **14**, not the 13 / 15 it reports. **Integrate the quoting fix, NOT the widths.** (c) Flag 5, `パワーストーン` unquoted here vs `chunk_000`'s `“Ｐｏｗｅｒ　Ｓｔｏｎｅ”` — **the sources genuinely differ** (`『…』` there, bare here), so §3 is not engaged; a project-level call. (d) Flags 7, 8: two menu-index compressions (`ＨＰ` for `回復`, `ＺＯＣ` for `包囲`) with every alternative measured — note `ｈｅａｌｉｎｇ` was **rejected because it is already bound to `ヒーリング`** in 3 shipped `batch_003` rows |

✅ **BARRIER MET — all 3 PRs open (#34, #35, #36), 0 units parked, 0 re-dispatches needed.**
**Review 1 of 3 done: #34 → CHANGES (1 finding), rework in flight. #36 not yet reviewed.**
⚠️ **DELIBERATE ORDER DEVIATION, recorded rather than silent: #35 is being reviewed WHILE #34
reworks**, instead of idling until #34 finishes. **The invariant CLAUDE.md §4 actually protects is
preserved — exactly ONE reviewer alive at a time**, so `glossary.md` / `FLAGS.md` / `HANDOFF.md`
writes still serialise. Rationale: reworks ran 4–12 min and reviews 12–30 min in wave 8, and **this
wave has no watchdog** (lineage cap, Blocked 0b), so an idle stall is a real risk while a moved base
is not — translators touch only their own `tl/` file, so a `batch_012` merge cannot conflict with
`batch_011`'s rework, and gate 2 re-checks mergeability against the current head anyway. Section
numbers are still taken by **READING at commit time**, which is what makes out-of-order integration
safe. If this proves wrong, the fallback is simply to serialise fully again.
Reviewing now, **one reviewer at a time, `run_in_background: false`, in unit order 011 → 012 → 013**.
Push `HANDOFF.md` before each reviewer; `git pull --ff-only` after it (it pushes an `integrate:`
commit). ⚠️ **Never infer merge state from an agent's status** — check `git log` and the PR.

⚠️ **CROSS-UNIT, FOR THE REVIEWER TO HOLD:** `batch_012` renders `ホッジス` → `Ｈｏｄｇｅｓ` (DATA 398)
as the retired officer to consult **about tactics** — and **`batch_013` IS the tactics-lecture
unit.** Almost certainly the same NPC. **Check `batch_013` names him identically.**

## Next up — WAVE 10 (⚠️ STILL SCRIPT-ONLY unless a human clears Blocked 0 / 0a)
**Seed the glossary BEFORE dispatching.** Sections end at **glossary §51** (wave 9's seeds went into
**§9 PROVISIONAL**, not a new section) and **FLAGS §AM** — ⚠️ take the next number by **READING both
files at commit time**, never by reserving.

**COMPUTE YOUR OWN BATCHES; DO NOT INHERIT THIS TABLE — it is a starting point, not a queue.**
After wave 9 merges, **424 lines / 447 instances** stay bank-feasible. The clusters, measured
2026-09-10 (growth at the 2.10× planning model):

| DATA | Lines | Banks | Growth | What it is |
|---|---|---|---|---|
| 707–879 | 173 | 18–25 | ~23,985 B | **continues wave 9's `batch_011` scene** — town, shops, NPCs |
| 1043–1159 | 117 | 31–39 | ~9,756 B | ⚠️ **1043–1105 is a DEVELOPER DEBUG MENU** (sound test, flag toggles) — lowest player value in the corpus; **1106–1159 is real dialogue** (cake, resurrection, magic-tome shop). **Split it; do not batch them together** |
| 1388–1430 | 42 | 42, 43 | ~2,978 B | casino: slots, medal exchange, prizes — player-facing |
| 997–1034 | 38 | 30 | ~795 B | ⚠️ debug flag/sound test again — tiny growth, near-zero player value |
| 326–345 | 19 | 18 banks | ~2,156 B | ⚠️ **38 instances from 19 lines, spread over 18 banks** — shop boilerplate; costs its growth in every one |
| 584–598 · 521–533 · 465–469 | 15 · 13 · 5 | 12 · 6,7 · 3 | small | short leftovers, good for topping a batch up to 40–60 |

⚠️ **THE ONLY BINDING BANK CONSTRAINT IN THE FEASIBLE SET IS BANK 5, and only via three lines.**
Measured this wave: across **all 606** untranslated lines that touch neither bank 40 nor 41, bank 5
is the sole bank over budget — and its whole overrun is **DATA 518, 519, 520** (growth **2,722 /
1,713 / 1,954** bytes each, three giant blocks against bank 5's 1,135 spendable). Drop those three
and 603 lines fit with room to spare. **That is exactly `queue.py`'s "603 lines, 628 instances", and
this accounting reproduces it to the line.** Banks 40 and 41 get a budget of **zero** (75 and 353
free against `RESERVE = 500`), so any line touching either is blocked outright.

**Live glossary rows — do not re-decide, do not assume exhausted:** `軍神ヘルメス` (DATA 281, 21
inst, needs a `魔法防御` form, lands in bank 40 so likely **unshippable**); `ピクシー` (DATA 817 —
**inside 707–879**, so wave 10 probably discharges it); `マーシュ` (FILE 870, 1330, 1379); `小隊`
(FILE 524, 1389). **§4.3 debts for a corrections unit, all byte-negative:** `batch_007.tsv:31`
ships `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, the only capitalised bare plural in `tl/`; merged `chunk_000` ×3,
`chunk_008`, `chunk_031` still ship `Ｈｅｙ，` against §32.3's `Ｏｉ，`.

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
