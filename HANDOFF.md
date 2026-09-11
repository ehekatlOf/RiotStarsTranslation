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
> ### ▶ WAVE 11 IS COMPLETE — ALL 3 UNITS MERGED AND INTEGRATED 2026-09-11. Coordinator: `session_012m7kST3Y5f2ag1jqg6pX8y`.
> **Units: `batch_017` (PR #42, squash `6e30b45`), `batch_018` (PR #41, squash `426f8c1`),
> `batch_019` (PR #40, squash `dcd2c57`).** Barrier was met at all three PRs; **each unit had its
> own independent reviewer subagent** — the coordinator translated nothing and merged nothing.
> **0 parked, 0 audit debt.** `check` green on the integration branch.
>
> **NOW, COORDINATOR — two things, in this order, in the same turn:**
> 1. **Close wave 11**: `git pull --ff-only` (the 019 integration commit is on this branch), run
>    `python3 tools/assemble.py merge` and commit `build/*_dump_merged.txt` if changed (⚠️ **the
>    committed `build/` is stale — it predates all three wave-11 units**), refresh the README status
>    table from `status`, prune worktrees, commit and push `handoff: wave 11 closed`.
> 2. **Then IMMEDIATELY open wave 12's session** with `create_session` (⚠️ **`source_url` is
>    REQUIRED alongside `source_revision`**), `source_revision` = `claude/workflow-translation-iterate-uzlkns`,
>    seeded with nothing but the wave number and "read `HANDOFF.md` first". **Do not stop to
>    summarise and do not wait to be asked** — CLAUDE.md §4 step 7.
>
> A translator that is still working is **not** a failure — wait. One that is **gone from
> `ListAgents` with no PR is LOST** — prune its worktree and re-dispatch (2 max, then park).
>
> ⚠️ **If this session is gone, take over:** `git fetch && git reset --hard
> origin/claude/workflow-translation-iterate-uzlkns`, `ListAgents`, list open PRs, reconcile against
> **In flight** below, restart what is lost, re-arm a `send_later` watchdog, finish the wave, then
> open wave 12 with `create_session` (⚠️ **`source_url` is REQUIRED alongside `source_revision`**).
>
> ✅ **NO AUDIT DEBT, IN OR OUT.** Wave 10's three units and wave 11's three units each had an
> independent reviewer subagent. Nothing in waves 10–11 is self-reviewed.
>
> ⚠️ **WAVE 11 IS SCRIPT-ONLY.** Battle stays blocked on Blocked 0 / 0a. The run is **not** complete.

## Last updated
2026-09-11 · by: **the `batch_019` REVIEWER** (integration commit) · wave: **11 — ALL 3 MERGED
(`batch_017` PR #42 r2, `batch_018` PR #41 r2, `batch_019` PR #40 **round 1**), 0 parked, 0 audit
debt** · glossary now ends **§60**, FLAGS ends **§AV** — both numbers taken by READING the files at
commit time, not reserved

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — battle is blocked, not idle |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **948** | 1,430 | `tl/script/batch_001–019.tsv` (was 905) |
| Script message instances | **5,041** | 7,931 | **63.6%** (was 63.0%) |

`check`: **All checks passed** after the `batch_019` integration commit. glossary ends **§60**,
FLAGS ends **§AV** — both re-read at commit time.
⚠️ **`build/*_dump_merged.txt` on this branch is STALE** — it predates `batch_017`, `batch_018` and
`batch_019` (147 lines out of date). Regenerating it is the coordinator's wave-close step, not a
reviewer's; `assemble.py` reads only `tl/`, so no build is broken by this.
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 2 → 1,607 · 5 → 1,635.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE, so bank 5 is invisible to anyone quoting it.**
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight
**WAVE 11 — three units, all script, all dispatched 2026-09-11. Barrier met; ALL THREE MERGED.**

| Unit | DATA lines | Lines / inst | JP chars | Banks | Branch | PR | State |
|---|---|---|---|---|---|---|---|
| `batch_017` | 1100–1159 | 60 / 60 | 3,275¹ | 31–39 | `tl/script-017` | **#42** | ✅ **MERGED 2026-09-11, round 2** — squash **`6e30b45`**, integration commit **`integrate: script batch 017 — glossary, flags, handoff`** (the commit directly after `6e30b45` on this branch). Bank 33 8,919 → **5,627** free (3,292 B); 6,152 B over banks 31–39; no bank negative. All 9 gates ✓ re-run from scratch on merged tree **`fa2d957`**. ⚠️ **Branch `tl/script-017` still on origin — deletion returns HTTP 403 (FLAGS §AQ9); NOT deleted** |
| `batch_018` | 1388–1413, 1415–1430 | 42 / 42 | 1,299¹ | 42, 43 | `tl/script-018` | **#41** | ✅ **MERGED 2026-09-11, round 2** — squash **`426f8c1`**, integration commit `integrate: script batch 018 — glossary, flags, handoff` (the commit directly after `426f8c1` on this branch). Bank 42 11,301 → **9,645** free (−1,656), bank 43 9,995 → **8,947** (−1,048), **total −2,704**; no bank negative, **exactly two banks moved** (proved by a `bankmeasure` diff with the file removed and restored). 1,299 JP → 2,647 EN = **2.038×**. All 8 gates ✓ re-run from scratch on merge tree **`7dbe045`** (base pinned `44d7cd7`, head `87c4420`, `git merge-tree` + `git archive`, **no working tree**). ⚠️ **Branch `tl/script-018` still on origin — deletion returns HTTP 403 (FLAGS §AQ9/§AU9); NOT deleted** |
| `batch_019` | 465–469, 521–533, 584–598, 870–879 | 43 / 43 | 960² | 3, 6, 7, 12, 25 | `tl/script-019` | **#40** | ✅ **MERGED 2026-09-11, ROUND 1 — no must-change finding** — squash **`dcd2c57`**, integration commit `integrate: script batch 019 — glossary, flags, handoff` (the commit directly after `dcd2c57` on this branch). Banks 3 7,741→**7,311** (+430) · 6 13,115→**12,565** (+550) · 7 12,723→**12,655** (+68) · 12 8,187→**7,695** (+492) · 25 11,829→**11,097** (+732) = **+2,272 B**; no bank negative, **none of the four banks under 2,000 free is touched**. All 8 gates ✓ re-run on merge tree **`3aec882`** (base pinned `0b5cd44`, head `86bb1bb`, `merge-tree --write-tree` derived **twice** and compared before use). ⚠️ **Branch `tl/script-019` still on origin — deletion returns HTTP 403 (FLAGS §AQ9/§AU9/§AV9); NOT deleted** |

² 960 is the kana+kanji-only count; the same 43 lines are **1,155** readable characters under
`translation_prompt.md` §0.2's tag-stripped convention. Both are correct under their own definition
and both are recorded so they are not read as a contradiction.

**Who acts next: the WAVE-11 COORDINATOR — close the wave, then open wave 12's session in the same
turn.** ✅ All three units merged and integrated, each by its own independent reviewer. ⚠️ **`git pull
--ff-only` first — the 019 integration commit is on `claude/workflow-translation-iterate-uzlkns`.**

✅ **THE FOUR GLOSSARY ROWS BATCH 019 OWED — ALL DISCHARGED OR CORRECTLY LEFT LIVE, every status
grepped in `tl/` at integration (status is not reach):**
- `　店を出る` → **D584 and D598 shipped**, so 9 of 10 done — ⚠️ **ROW STAYS LIVE, D339 (×2) remains.**
  The 018 correction that first named D339 is upheld.
- `また　どうぞ` → **D596 shipped and it AGREES with `batch_018`'s D1426**: `Ｄｏ　ｃｏｍｅ　ａｇａｉｎ！` /
  `ｄｏ　ｃｏｍｅ　ａｇａｉｎ．`, one phrase, case by sentence position, punctuation following each source.
  **EXHAUSTED, 2 of 2.**
- `いらっしゃいませ` → **D597 shipped; all 11 script-unique lines now done. EXHAUSTED.** The one battle
  "hit" is a false positive (`chunk_006`'s inflected `いらっしゃいません` / `いらっしゃいました`).
- `荷物` → **D589 shipped; 5 of 5. EXHAUSTED**, discharging §59.5's row.

### Review log
| Unit | PR | Round | Decision | Note |
|---|---|---|---|---|
| 019 | #40 | 1 | ✅ **MERGE** | **All 8 gates PASSED on the first round — the first script unit in four waves to need no rework.** Tree `3aec882` **derived twice** from pinned base `0b5cd44` before use. Gate 7 run row-first with the key count stated: a backtick-only harvester found **1,589 keys / 65 hits**, but adding **plain un-backticked column-0 cells** raised it to **2,512 keys / 89 hits** — ⚠️ **`glossary.md:67`'s `帝国` row, the one this unit's Flag 3 turns on, is itself un-backticked and invisible to a backtick-only gate 7** (FLAGS §AV7). Reviewer re-derived all seven claims it was asked to: the `炎の雨` census (5 unique / 25 / D223 ×21, and `batch_008:71`'s lowercase `ａ　ｂａｔｔｅｒｙ　ｒａｉｎｉｎｇ　ｆｉｒｅ`) ✓, the `兵器` census ✓, **all four `{FFFE}` one-row measurements (31 / 29 / 26 / 28, every one over 24, so all four forced)** ✓, zero `帝国軍` ✓, **Flag 11's two-shops-in-bank-12 split read off the `=== BANK` headers** ✓, Flag 12's bank sets ✓, and **all eight insert budgets incl. D591's 8/9-digit worst case** ✓. **Five findings, none blocking, all integration corrections**: (1) `兵器` → `ｗｅａｐｏｎ` is **NOT a first rendering** — shipped 5× in battle chunks 008/009/042, so `ｏｒｄｎａｎｃｅ` is not a free reserve (§60.5, §AV2); (2) the `イチバン` "0 battle, exhausted" is **katakana-only** — `一番` ships `Ｓｔｒｏｎｇｅｓｔ　ｉｓ　ｈｉｇｈｅｓｔ．` in `chunk_010` (§60.4, §AV3); (3) **a FIFTH insert row, D874, missing from the PR's flag table** (§AV5); (4) Flag 12 cited `batch_011:27` for a line at **`:34`**, and checked the banks it borrowed from but not bank 12, which already holds `Ｄｏ　ｃｏｍｅ　ａｇａｉｎ` at `batch_006:52` (§AV6); (5) four one-column slips in the PR's supporting arithmetic, all safe-direction (§AV6). ⭐ **Reading review: the three registers are held apart and the katakana register is carried by SYNTAX, not mangled spelling** — verified against `chunk_010`'s shipped `Ｄｅｆｉｌｅｒｓ　ｏｆ　ｓｗａｍｐ　ａｒｅ` / `Ｗｅ，　ｓｔｒｏｎｇ　ｒａｃｅ．` for the same voice. Tics 30→30 and 7→7, counted line by line |
| 018 | #41 | 2 | ✅ **MERGE** | Head `87c4420`. Translator **verified finding 1 positionally against the battle dump before applying it** — both reviewer FILE-line citations hold, census reproduced exactly (5 true hits after removing 2 false positives). Accepted 2(a)–(e) and 3; **disclosed one deviation** (D1409 shipped as ONE row, `Ｃｏｍｅ，　ｗｈｅｒｅ　ｄｏ　ｗｅ　ｇｏ？` 21, on a §5 volitional split) and **corrected two reviewer figures** (17 not 16, 6 not 7). **REVIEWER RULING: all 8 gates ✓ on tree `7dbe045`; the rework is exactly 2 rows with the tag stream identical on both; every reported figure re-derived and confirmed (−1,656 / −1,048 / −2,704 / 2.038×).** ⭐ **The translator's D1409 form was ACCEPTED and the reviewer's proposal was the worse one** — `ｓｈａｌｌ` would have put a volitional marker on a plain non-past source and collapsed the §5 split the same review endorsed in round 1. **The reviewer was wrong on three counts and says so in FLAGS §AU8**: two `len()` figures (17 not 16, 6 not 7), its own §AT8 0-based-index slip (`えっ、王女様が` is non-empty #20, index 19), and that proposal. Items 4 (gate-7 note-cell hole) and 5 (`さあ、` → `Ｃｏｍｅ，` at `chunk_030.txt:27`) **verified and integrated**; item 6 (the `ｔｈｅ　` deletion) **declined with reasons, recorded as a costed reserve in FLAGS §AU6** |
| 018 | #41 | 1 | **CHANGES** | **All 8 gates PASSED** (base pinned `f64ca52`, tree `9b68866`, `git archive`, no working tree). Gate 7 **1,540 raw / 1,300 distinct keys, 31 occur**. Reviewer re-derived **all ten `{FFEC}` insert rows** — every figure matched the PR, incl. the 21-column worst case at D1420. **1 finding on the file** ⤵ · Rework relayed to `a128d73965f6152f7`, round 1 of 3 |
| 017 | #42 | 2 | ✅ **MERGE** | Head `eb2c5c1`. Translator accepted all 3 findings, pushed back on nothing substantive. D1112 → `Ｉ　ｓｈａｌｌ　ｒａｉｓｅ　ｔｈｅｍ．` (19), D1138 → `Ｔｈｅｙ　ｈａｖｅ　ｃｏｍｅ　ｂａｃｋ` (19); +8 B, bank 33 5,635→5,627. It **added a gate of its own** — a full-file gendered-pronoun sweep — confirming the finding's scope both ways. **Reviewer re-derived everything rather than accepting it**: both `len()`s (18→19, 16→19), both page shapes (D1112 p3 = 14/11/19, D1138 p1 = 13/19/13, both 3 rows, no re-flow), the bank table (bank 33 **5,627**, total 6,152), and a **wider** pronoun sweep (adding `ｍａｎ/ｍｅｎ/ｗｏｍａｎ/ｈｉｍｓｅｌｆ/Ｌａｄｙ/Ｌｏｒｄ/…`) — after the fix **none of D1120, D1122, D1138 carries any gendered reference**. Base **pinned to a SHA** (`c017144`) because the integration branch moved twice mid-review and `merge-tree` silently returned a different tree each time |
| 017 | #42 | 1 | **CHANGES** | **All 8 gates PASSED** — merge-tree `01745f6`, `check` green, no bank negative, `rowcheck` all 17 pages inherited, 0 dupes, gate 7 **97 keys** of 1,246 distinct, 0 offending chars. Reviewer gated the **merged tree** via `git archive`, no working tree. **It independently re-derived all six of the PR's flagged claims and all six stand.** One finding on the file ⤵ |

⭐ **THE 017 FINDING IS A REAL BUG AND SETS A PROJECT-WIDE PRECEDENT.** D1112 ships
`Ｉ　ｓｈａｌｌ　ｒａｉｓｅ　ｈｉｍ．` and D1138 `Ｈｅ　ｈａｓ　ｃｏｍｅ　ｂａｃｋ` for the **runtime unit-name
insert `{FFEC}{=00}{=05}`** — but the roster has women (§1 fixes Cress FEMALE; Beatrice, Maya;
§4's 女剣士/女魔術師), the Japanese has no pronoun, and the same unit keeps the referent ungendered
at D1119/D1122/D1129/D1133. ⚠️ **`batch_017` is the ONLY file in `tl/` or `pending/` that renders
this insert, so whatever it ships becomes the precedent for every future line carrying a unit name.**
Fixes offered: `Ｉ　ｓｈａｌｌ　ｒａｉｓｅ　ｔｈｅｍ．` (19) / `…ｔｈａｔ　ｏｎｅ．` (23); `Ｔｈｅｙ　ｈａｖｅ　ｃｏｍｅ　ｂａｃｋ` (19).

✅ **THAT REVIEWER FINDING HELD, AND THE TRANSLATOR VERIFIED IT BEFORE CONCEDING.** PR Flag 11 was
false: D834 **is** shipped (`batch_016.tsv:62`), so **`体力` is 2 unique / 0 battle and EXHAUSTED by
this unit** — §57.1's row is struck at integration. ⚠️ **§57.1 read "LIVE — DATA 1126 outstanding",
and D1126 is this unit's own line, so the row was live only because of `batch_017` itself.**

⭐ **A NEW METHOD RULE, COINED BY `batch_017`'s TRANSLATOR ABOUT ITS OWN ERROR — put it in every
future dispatch: "RE-DERIVING A REACH IS NOT RE-DERIVING A STATUS."** It censused `体力`'s reach
correctly (2 unique) and then asserted D834's *shipped status* without ever grepping `tl/`. **This is
a distinct failure from the four coordinator errors above** — those censused the wrong corpus; this
one censused the right corpus for the wrong question. `HANDOFF.md`'s wave-10 table already warns that
*"where is it translated?"* and *"where does it occur?"* differ; this is the third question,
*"has this specific instance shipped?"*, and it needs its own grep.

⭐ **THE 018 FINDING — A TERMINOLOGY COLLAPSE GATE 6 CANNOT SEE. ✅ FIXED IN ROUND 2 AND MERGED; the
ruling is now `glossary.md` §59.1, a FIRST-COLUMN row.** Round 1 rendered **`さ、`** as
`Ｎｏｗ，` at D1408/D1409 — but `Ｎｏｗ，` is **`さあ、`'s** settled English, and the same file ships
`さあ、` → `Ｎｏｗ，` at D1388/D1415, so **two source strings land on one English inside one file**.
`glossary.md:2261` and `:1788` hold them apart. The proof is a shipped battle line: **`chunk_006.txt:13`
carries BOTH in one Fernando speech** — `さ、お城へ戻りましょう。` → `Ｃｏｍｅ，　ｌｅｔ　ｕｓ　ｒｅｔｕｒｎ`
beside `さあ、` → `Ｎｏｗ，`; `chunk_007.txt:20` gives a second, a **different speaker** (Nacol), also
`Ｃｏｍｅ，`. `さ、` is **5 occurrences in the whole game**; this unit renders 2 of the 3 script ones and
was the only work anywhere rendering it as anything but `Ｃｏｍｅ，`. **Shipped in round 2 as
`Ｃｏｍｅ，　Ｐｒｉｎｃｅｓｓ，　ｌｅｔ　ｕｓ` (22) at D1408 and `Ｃｏｍｅ，　ｗｈｅｒｅ　ｄｏ　ｗｅ　ｇｏ？` (21) at D1409** —
the latter the translator's own one-row form, not the reviewer's two-row proposal, which would have put
`ｓｈａｌｌ` (volitional) on a plain non-past source. **D1368 (bank 41) is the one instance left.**

⚠️ **THE 018 REVIEWER CORRECTED THE PR'S "FIRST IN THE SCRIPT STORE" CLAIM.** D1408 is the **third**
§L2-shape pool, not the first: **D517 (61 breaks / 62 segments) is already shipped in `batch_002.tsv`**
and D1387 (12 / 13) is untranslated. ⚠️ **CORRECTED AT THE 018 INTEGRATION — there are FIVE, not three.**
The reviewer censused at ≥12 breaks; the translator's ≥10 also finds **D1361 (11 / 12)** and **D1379
(10 / 11)**, both untranslated. Full table in FLAGS §AU3. It also relocated the PR's own strongest
evidence — the pool ends on a *complete* sentence (`城へ帰りましょう。`), and the incomplete fragment
`えっ、王女様が` sits **inside** it. ⚠️ **The reviewer wrote "19th of 22"; 19 is its 0-BASED INDEX, and as
an ordinal it is non-empty #20 of 22 — the §AT8 trap, sprung in the review that cited §AT8. FLAGS §AU8.**

⭐⭐ **A NEW STRUCTURAL HOLE IN GATE 7, FOUND BY `batch_018`'s TRANSLATOR AND VERIFIED BY ME —
PUT IT IN EVERY FUTURE DISPATCH.** **`さ、` has ZERO first-column keys in `glossary.md`; its ruling
lives entirely in two *Note cells*.** Measured by me: `grep -cE '^\| *`?さ、' glossary.md` = **0**,
`grep -c 'さ、' glossary.md` = **2**. **A key-first gate 7 is therefore STRUCTURALLY INCAPABLE of
finding it** — which is exactly why the 018 reviewer's *reading* review caught the collapse and no
gate did. ⚠️ **This is §48.5's hole in a new shape: the glossary DID record the ruling, just not
where the gate looks.** HANDOFF's standing rule already says gate 7 runs glossary-row-first and that
*"it cannot surface a word the glossary never recorded"* — **this is the sharper case, a word the
glossary DID record, in a cell the gate does not read.** Fix, both halves: **(1) extract `X` → `Y`
pairs from NOTE CELLS as well as key cells when running gate 7; (2) promote such rulings to real
first-column rows** so the next gate 7 can see them.

⚠️ **`FLAGS.md` §AQ8 IS STALE** — "51 rows, none over 8" predates `batch_016`/`batch_017`; the true
pre-018 figure is **58 rows, maximum +14**, and D1420's **+17** will be the new corpus maximum. The
018 reviewer will correct §AQ8 at integration. **68 gate-blind insert rows now ride on §V1's shop visit**,
and D1404/D1424 are the cheapest in-game test case in the corpus (1 and 5 visible columns).

⚠️ **FORWARD HAZARDS censused by `batch_017` but NOT in its banks — for `FLAGS.md` at integration:**
`よかろう` [2, 33, 41] and `わかったわ` [36, 41] **share bank 41**, and `なんだ、` is **also** bank 41 —
two hazards in one bank. `Ｖｅｒｙ　ｗｅｌｌ` already renders `いいでしょう。`, `いいわ。` and `よし、ひとつ`,
so with this unit's it is **five source words under one English phrase corpus-wide**; `chunk_035`'s
`よし` sits oddly beside §57.2's `よし` → `Ｒｉｇｈｔ`.
⛔ **Nothing is reviewed until all three are open** (CLAUDE.md §4 step 4). At 09:07Z both remaining
translators were alive and 43–44 min in; wave 9's ran 52 min – 1 h 34 m, so this is normal, not a stall.

⚠️ **TWO COORDINATOR ERRORS ALREADY CAUGHT BY A TRANSLATOR — both verified by me against the primary
sources, both mine, and the reviewer must NOT re-report them as the translator's:**
1. **My dispatch to `batch_019` said "`帝国` / `帝国軍` → `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` (§20.4)". WRONG
   — I conflated two rows.** `glossary.md:67` fixes bare **`帝国` → `ｔｈｅ　Ｅｍｐｉｒｅ`**; §20.4 is
   `帝国軍` only. `batch_019` contains `帝国軍` **zero** times and bare `帝国` twice (D527, D532), and
   it correctly rendered the Empire row. **The file is right and the dispatch was wrong.**
   ✅ **CONFIRMED at the PR #40 review** — the reviewer re-counted `帝国軍` in the unit's own 43 keys
   independently and got **zero**; the five `帝国軍` lines are D800, D801, D1102, D1356, D1366.
2. ⭐ **My §9 seed `炎ノ雨` → `Ｒａｉｎ　ｏｆ　Ｆｉｒｅ`, "1 unique, 0 battle — D532, exhausted", censused
   only the KATAKANA spelling.** Re-derived by me just now: **`炎の雨`, the ordinary spelling, is 5
   unique lines / 25 dump instances — D223 (count 21), D514, D518, D520, D1287** — and **D514 is
   ALREADY MERGED** in `batch_008.tsv` as lowercase `ａ　ｂａｔｔｅｒｙ　ｒａｉｎｉｎｇ　ｆｉｒｅ`. `batch_019`
   therefore takes §9's own stated lowercase alternative, `ｒａｉｎ　ｏｆ　ｆｉｒｅ`. ⚠️ **The §9 row must
   be kept LIVE, NOT struck as exhausted**, and whoever renders D223 decides the description sense.
   **This is wave 10's "measured ONE SIDE of a comparison" shape, committed by me in a seed.**
   ✅ **BOTH CENSUSES RE-DERIVED AND CONFIRMED at the PR #40 review**, and the §9 row was **kept LIVE**
   at integration with the corrected figures (glossary §9, FLAGS §AV4). ⭐ **AND THE SAME SHAPE
   RECURRED INSIDE THE PR ITSELF**: its `イチバン` cell claimed "0 battle — the row is exhausted" on a
   **katakana-only** census, while `一番` already ships `Ｓｔｒｏｎｇｅｓｔ　ｉｓ　ｈｉｇｈｅｓｔ．` in
   `tl/battle/chunk_010.txt` for the identical sentence formula. Neither rendering was wrong and
   nothing changed in the file, but the row is now scoped to the katakana and cross-referenced —
   **glossary §60.4, FLAGS §AV3. Two waves, three instances: censusing ONE spelling of a two-spelling
   term is now the single most repeated error in this run.**
3. ⚠️ **My §9 seed's REASON for `的中確率` → `ｈｉｔ　ｒａｔｅ` is FALSE, though the rendering stands.**
   I wrote that `命中率` is *"a different word in a different store"*. Re-derived by me: `命中率` is
   **script DATA 830, 979, 1237 — 0 battle-dump hits — i.e. the SAME store**, and **D830 already
   ships as `ｈｉｔ　ｒａｔｅ` in `batch_016.tsv`.** What actually licenses the row is §25.3 measured:
   `的中確率` is bank [42], `命中率` banks [21, 29, 40] — **0 shared banks, 0 messages hold both.**
   ⚠️ **HANDOFF's own inherited list names `命中率 (D1237)` as a live §9 row — i.e. script — and I
   wrote "different store" with that on the page in front of me.** Keep the rendering; the §9 row's
   stated reason must be replaced at integration.
4. ⚠️ **My §9 `ほこら` seed states its reach WRONGLY IN BOTH DIRECTIONS — and would have struck a live
   row.** I wrote *"3 unique, 0 battle — D1104, D1105 (batch 017) and D324"*. Re-derived by me:
   **4 unique — D324, D1086, D1095, D1104 — and D1105 contains no `ほこら` at all.** I named a line
   that does not have the word and missed two that do (D1086/D1095, debug-menu lines in bank 31).
   `batch_017` renders **D1104 only**, so **three instances remain and the §9 row STAYS LIVE.**
   Had the translator trusted the cell, the row would have been struck as exhausted.
   ✅ **RE-DERIVED A THIRD TIME BY THE 017 REVIEWER AND CONFIRMED** (D324 bank 40, D1086 bank 31,
   D1095 bank 31, D1104 bank 33; `'ほこら' in D1105` → `False`). The §9 cell is **corrected in place**
   by the integration commit and the row is **kept live**.
5. ✅ **`Ｘボタン` → `Ｃｒｏｓｓ　ｂｕｔｔｏｎ` is settled by SHIPPED WORK, not by my §16 reasoning.**
   **D1414 — already merged in `batch_002.tsv`, bank 43, same speaker, same scene — renders
   `×ボタンを押してね` as `Ｃｒｏｓｓ　ｂｕｔｔｏｎ`**, and D1393's `Ｘボタンよ` is the same instruction in
   the same words. My proposal was right; the corpus proof is stronger than the argument I gave.

⚠️ **FOUR COORDINATOR ERRORS IN ONE WAVE, ALL IN SEEDS OR DISPATCHES, ALL CAUGHT BY TRANSLATORS, ALL
THE SAME SHAPE: I asserted one side of a comparison without censusing the other.** Three of the four
(`炎ノ雨`, `的中確率`, `ほこら`) would each have STRUCK OR MIS-JUSTIFIED A GLOSSARY ROW THAT MUST STAY
LIVE. **The seeding step needs the same `len()`-both-sides / state-your-corpus discipline the
translating step already has** — wave 12's coordinator should census every reach cell in BOTH
spellings and BOTH stores before writing it, and mark any cell it did not verify as unverified.
⚠️ **No unit touches banks 2, 5, 40 or 41** (verified: the three bank-sets are disjoint from the
four tight banks). Tightest bank touched is **33** — 8,919 free, ~4,415 projected demand.

⚠️ **Every merged `tl/script-*` branch is still on origin** — branch deletion fails from the agent
container (**FLAGS §AQ9**). **"Branch gone = merged" is an INVALID signal in this repo**; use the
`integrate:` commit and the PR's merged state. Human fix: enable *Automatically delete head branches*.

## Next up — WAVE 12 (⚠️ still script-only unless a human clears Blocked 0 / 0a)
**COMPUTE YOUR OWN BATCHES.** Every figure here I re-derived at wave 11's dispatch; bank figures
move with every merge. **627 lines / 3,035 instances were untranslated when wave 11 opened**
(independently confirmed against `queue.py script`). Wave 11 takes 145 of them.

⭐ **A CORRECTION TO THE INHERITED QUEUE, FOUND BY READING THE LINES RATHER THAN THE TABLE.**
Wave 10's table called **1043–1105 a "DEVELOPER DEBUG MENU"**. It is not, at its top end: the debug
flag menu ends at **D1099** (`他に用はありますか？`), and **D1100–D1105 are real dialogue** — Father
Batou's church (D1100, bank 31), the Farina reconstruction scene with Bishop Cleus and Governor
Felix (D1101–1103, bank 32, D1102 alone is 365 JP chars), the shrine interior (D1104) and **the
hermit's quest-giver line (D1105)**, which is the direct set-up for D1106's *"did you bring the
cake?"*. Wave 11's `batch_017` therefore runs **1100–1159, not 1106–1159** — it keeps one
conversation in one file and exhausts the `『ようせいのケーキ』` row (D1105 + D1107 are its only two
instances). **The debug range left for a future wave is 1043–1099 (57 lines), not 1043–1105.**

| DATA | Lines | JP | Banks | Verdict |
|---|---|---|---|---|
| 1043–1099 | 57 | ~1,640 | 31–33 | ⚠️ **DEVELOPER DEBUG MENU — feasible, near-zero player value. NEVER batch with real dialogue.** |
| 997–1034 | 38 | 356 | 30 | ⚠️ debug flag / sound test — same caution |
| 326–345 | 19 | — | 18 banks | ⚠️ feasible but pays its growth in **every one of 18 banks** for 38 instances |
| 518/519/520 | 3 | — | 5 | ⛔ **not shippable** — 6,389 B against bank 5's 1,135 spendable |
| **1160–1354** | **195** | 4,836 | **40 only** | ⛔ **BLOCKED — bank 40 has 75 free bytes.** No re-translation helps |
| 1355–1387 | 33 | — | **41 only** | ⛔ **BLOCKED — bank 41 has 353 free** |

⚠️ **AFTER WAVE 11 THE BANK-FEASIBLE PLAYER-FACING SCRIPT IS ESSENTIALLY DONE.** What remains is
95 lines of developer debug menus, the 18-bank table rows, and ~400 lines behind the §F2 repoint.
**Wave 12 should plan for that**: either the debug menus (low value, honest completion), the
corrections unit below (real quality gain, byte-negative), or a final handoff. This is the first
wave where "no dispatchable unit left" comes into view — but it does **not** hold yet.

**A corrections unit is still worth a slot.** §4.3 debt in merged work, all byte-negative or free:
**§AP5** `chunk_000`'s three hyphen stutters (census 19 : 3) · **§AP7** `品` → `ｇｏｏｄｓ` at DATA 376 ·
**§AP9** a stale `トリフ` row, `batch_007.tsv:31`'s `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, and `Ｈｅｙ，` against
§32.3's `Ｏｉ，` in `chunk_000` ×3 / `chunk_008` / `chunk_031` · **§AQ5** `batch_007` renders `編成` as
BOTH `Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ` and `Ｆｏｒｍａｔｉｏｎ` · `batch_010` D897 ships `ｒｅｖｏｌｔ` for bare
`反乱` against §38.3's `ｒｅｂｅｌｌｉｏｎ`.

⚠️ **§9 ROWS THAT STAY LIVE AFTER WAVE 11** (a promotion is not a strike): `親衛隊` (D1330, **bank
40**, may never land) · `マーシュ` (FILE 1330, 1379) · `クーデター` (D1373) · `腕力` (D1234) · `体力`
(D1126 — ⚠️ **that is in `batch_017`, so wave 11 may discharge it**) · `慰霊金` (D1351) · `命中率`
(D1237) · and, new this wave, `ほこら` (D324, bank 40) · `魔道書` (**D293 — 21 of its 23 instances,
reaching 21 banks**) · `生き返りの秘法` (D324, bank 40).

## Remaining
**Battle: 0 dispatchable.** 8 chunks remain, **all blocked** — 15, 23, 27, 28, 29, 39 by §D1's dump
artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's 1.64×).
⚠️ **`queue.py battle` reports "dispatchable 11" and is WRONG ON BOTH COUNTS** — its tier-A cutoff is
hardcoded **1.6**, and it knows **nothing** about §D1.

**Script: 627 unique lines / 3,035 instances untranslated** after wave 10 (was 790 / 3,198), re-derived
at the close from `script_unique.txt` + `script_dump.txt` + `bankmeasure`. Of those, the **feasible**
work is the Next up table: **1106–1159 (54)**, **1388–1430 (42)**, **870–879 (10)**, **584–598 (15)**,
**465–469 (5)** — about **126 lines of real player-facing dialogue, i.e. 2–3 more waves** — plus
**101 lines of developer debug menus** (1043–1105, 997–1034) that are feasible but near-zero value.
⛔ **195 lines (DATA 1160–1354) live in BANK 40 ALONE, which has 75 free bytes**, and a further ~200
are bank-blocked elsewhere. CLAUDE.md §8's "no dispatchable unit left" does **NOT** hold; the run
continues, but **the end of the bank-feasible script is now in sight** — after those 2–3 waves, what
remains needs the §F2 repoint or nothing.

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

### ⭐ WAVE 10's LESSONS — the coordinator's own errors are the useful part
**Thirteen coordinator figure errors, every one caught before it shipped.** Not one reached a merged
file, because translators and reviewers checked me — but the *shapes* repeat and are worth naming:
| shape | count | example |
|---|---|---|
| hand-counted widths | 1 event, **45 figures** | every first-draft seed width, each wrong by one — `len()` fixed all 45 |
| instance lists built from the English side | 5 | `親衛隊` "3" (真 5), `機械兵`, `材料`, `極上のワイン`, `踊り子` |
| **an error INSIDE a correction** | **2** | `ｈｅｒｍｉｔ` "(7)" (真 6) written *while* fixing a phantom seed; "both banks wrong" when only one was |
| **a figure RELAYED from a report, unverified** | **2** | `素材` "21 banks" (真: 21-bank reach is D289 alone); D849 "bounded" (真: no `{FFEC}` at all) |
| **censusing the WRONG CORPUS** | 1 | counted shipped `tl/` lines to answer §25.3's *"where does this term OCCUR?"* — untranslated lines are invisible to a `tl/` census and are exactly what the test is about |
| scope/wording | 2 | `ピクシー` "solely D817"; `親衛隊` filed to §B instead of §F2 |
**Three rules follow, and they are mechanical, not counsels of care:**
1. **STATE YOUR CORPUS when you census.** "Where is it translated?" and "where does it occur?" are
   different questions with different answers, and §25.3 asks the second.
2. **NEVER RELAY A FIGURE YOU DID NOT RE-DERIVE.** Two of my thirteen came from a PR body I trusted.
3. **`len()` BOTH values and PRINT BOTH.** ⚠️ **And verify corrections in both directions** — I put an
   error *inside a correction* twice, which is §4.3's own named trap.

⭐ **METHOD GAIN, invented mid-wave and adopted by two reviewers: PAIR THE BATTLE DUMP'S JAPANESE
AGAINST `tl/battle/` ENGLISH.** Battle `tl/` holds no Japanese, so grepping it is a **null check** —
positional pairing is the only way to census the battle corpus. `batch_015`'s translator built it to
answer a `Ｈｍｍ` question (finding **8** shipped instances where I found 6 and the reviewer 5), and it
then found the **`chunk_003` `よし、じゃあ、` → `Ｒｉｇｈｔ，　ｔｈｅｎ．`** precedent that settled a ruling
from a single line. **Every future census of a term that might appear in battle must use it.**

⚠️ **SIX SETTLED CONVENTION/SCOPE MISMATCHES — do NOT re-report these as anyone's error.** Each cost
attention this wave: **DATA vs FILE** line numbers (D750 is FILE 52 *and* data-index 44) · **0-based vs
1-based** (§37.1's list; true 1-based **DATA 444, 786, 897, 1384**) · the **gutter census** (20 → 20 true
gutters **plus** 8 separate insert word-spaces — the PR body and round 1 each conflated the two) · the
**run-splitter** difference (373 vs 372, a D794 definition) · **§45.2's "`.TTTT.` = 0" is BATTLE-scoped**
(the script dump has 1) · **`ピクシー`** covering two instances of which one was outstanding. Also
**method** differences, not errors: gate-7 key counts vary with splitter and struck-row handling
(1,138 / 1,175 / 1,317 / 1,430 all seen), and **a price census reads 4 of 4 or 5 of 5 depending on
whether the unit under review is in the corpus.** **State the convention; never file it as a mistake.**

⚠️ **A GATE-BLIND CLASS THAT COST A ROUND, now documented:** `rowcheck.py:_script_cols` **strips number
inserts `{FFEC}{=00}{=01}` / `{=00}{=02}` to ZERO columns**, so any row carrying one is *bounded, not
measured*. `batch_014` shipped a **21-column** price row past every gate against §V1's bound of **8**;
four-digit prices are literal in the dump, so it would have rendered at **25 columns in game**.
**Every reviewer must hand-measure those rows.** `{FFEC}{=00}{=00}` (the player name) IS counted, at 7.

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
| 10 | script 014, 015, 016 (**script-only**, DATA 707–869) | **3** | 0 | battle 32/44 (64.3%); script **803 (61.7%)** |

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
