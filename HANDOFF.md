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
> ### ▶ WAVE 12 IS RUNNING — 4 UNITS DISPATCHED. Coordinator: `session_01UMK4VSo7m2SaC6uqaJKCdX` (top-level, depth 0 — `Task`, `send_later` and `create_session` all work).
> **THIS IS THE LAST WAVE WITH DISPATCHABLE TRANSLATION WORK.** After it closes, CLAUDE.md §8's
> "no dispatchable unit left" **WILL** hold: these 4 units are *every* remaining bank-feasible line.
> Wave 13's job is to verify that and write the run's final handoff — not to hunt for more work.
>
> If this session died mid-wave: `ListAgents`, reconcile the open PRs below against **In flight**,
> re-dispatch anything with no branch, and **re-arm the `send_later` watchdog**.
>
> ### ▶ 3 of 4 REVIEWED AND MERGED (#45 `5b6c212`, #43 `1134d2b`, **#44 `b3ca8cb`**). NEXT: dispatch a `reviewer` for **PR #46 `batch_022`** — the last unit of the wave.
> **`git pull --ff-only` FIRST** — #44's reviewer pushed an integration commit appending glossary
> **§63** and FLAGS **§AY**. Then dispatch the last reviewer, `run_in_background: false`.
> ⚠️ **Tell #46's reviewer: every `glossary.md:NNNN` citation in its PR body is STALE** (+12 to +26
> from #45's integration, shifted again by #43's, and now by #63's 266 appended lines). **Cite by
> section; verify a row by its text.** ⚠️ **And that `glossary.md` uses THREE citation conventions
> (§AX6): project DATA = 0-based `script_unique.txt` body index + 1; `batch_NNN.tsv:n` and
> `chunk_NNN` are 1-based FILE lines; §37.1's battle `L6`/`L4` are 1-based BODY indices. State which
> one every number is.**
>
> ### ▶ TWO THINGS #46's REVIEWER INHERITS FROM #44, BOTH SETTLED — DO NOT RE-OPEN THEM
> 1. ⭐⭐ **CASE POLICY IS RULED (glossary §63.1 / FLAGS §AY3): descriptive labels take SENTENCE CASE**
>    — initial capital on the row's first word, glossary-fixed components byte-identical and lowercase
>    below it; **title case only for a NAMED thing or a §9-seeded label form.** It ratifies what both
>    files already shipped. **#46 must conform, not re-decide.** The decisive evidence is **§56.2's
>    eight gutter-prefixed menu labels, every one sentence case.**
> 2. ⭐⭐ **THE 30 SHARED TITLES ARE VERIFIED IDENTICAL AND NOTHING MOVED.** `batch_021` D1005–D1034 ↔
>    `batch_022` D1053–D1082 are the same 30 readable strings, differing **only** in the trailing
>    `{FFF8}` argument, so **gate 6 pairs NOTHING**. Paired at #44's review by readable text:
>    **30 / 30 identical including the `ＮＮ：` prefix**, D1027 ↔ D1075 identical including the break.
>    **#44 merged with no change to any of the 30, so #46's own 30/30 diff still stands — no re-diff
>    needed.** #46 still owes its own pairing of the ABBREVIATED menu rows (D1043–D1052), which are
>    **its own** and were not reviewed at #44: measured there, its **D1048 has a run at exactly 24**
>    (`[23, 24, 23, 15]` — legal, over the ≤23 preference) and its **D1050 abbreviates track 23** to
>    `　２３：Ｌｅｇｅｎｄａｒｙ　ａｎｃｉｅｎｔｓ` (22). ⚠️ **`その他` is entirely #46's — 0 occurrences in
>    `batch_021`, 10 in `batch_022` — and it has 0 glossary mentions of any kind while shipping 7× in
>    `batch_013` as `　Ｓｏｍｅｔｈｉｎｇ　ｅｌｓｅ`. That is gate 7's face (c) and #46 must run it.**
> ⚠️ **#46 is the SECOND of the two debug twins to merge, so IT strikes the seven §9.W12 seed rows**
> (`フラグ`, `新曲`, `任務失敗`, `ゲームオーバー` label, `宿敵`, `ザコ戦`, `ボス戦`) per the `ルート`
> precedent (§29.1 / §30.1). #44 promoted them and **deliberately left every row LIVE** (§63.4 has the
> per-DATA remaining counts). ⚠️ **But `音楽` does NOT become exhausted: D1169 remains in bank 40**
> (§AY5), and it carries a `・` that is outside §3.1.

## Last updated
2026-09-11 · by: the **wave-12 reviewer of PR #44** (`batch_021`), integration commit below ·
wave: **12 REVIEWING — barrier met, 3 of 4 reviewed and MERGED (#45, #43, #44); only #46 left** ·
**every figure in the Progress block and in all three merged rows below was re-derived by its reviewer
from the dumps + a fresh `merge`/`bankmeasure`/`rowcheck`, not inherited**
⚠️ **glossary now ends §63, FLAGS now ends §AY** — both read off the file at commit time, never reserved.
⚠️ **The four banks under 2,000 free are UNCHANGED by PR #44: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.**
`bankmeasure`'s `tightest:` line still hides **bank 2** (it hid bank 5 before #45) — **which bank is
invisible is not stable, so never quote that line; read the 44-row table.**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — battle is blocked, not idle |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **1,007** | 1,430 | `tl/script/batch_001–021.tsv` (was 969) |
| Script message instances | **5,123** | 7,931 | **64.6%** (was 64.1%) |

`check`: **All checks passed** on the integration branch after PR #44 —
`script lines replaced: 5123  (unique forms: 1007)`. glossary now ends **§63**, FLAGS now ends
**§AY** — both re-read off the file at commit time, never reserved.
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.** **PR #44 touched
none of them** — bank 30 only, 35,091 → 34,635.
⚠️⚠️ **`bankmeasure`'s `tightest:` line prints only THREE, and it currently hides BANK 2** (it hid bank
5 before PR #45). The line is a sample, not a summary: **read the full 44-bank table.**
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight — WAVE 12, dispatched 2026-09-11
| Unit | Branch | DATA | Size | Bank cost (mine) | State |
|---|---|---|---|---|---|
| `batch_020` | `tl/script-020` | 318, 320, 326–334, 336–345 | **21 lines / 44 inst**; 532 JP → 1,051 EN = **1.9756×**; widest run **23**, none at 24 | 21 banks, **+2,256 B**, max **410** (bank 18), bank 5 **realised 40** of 1,635 — all 21 deltas re-derived twice by the reviewer, by independent routes, and they agree bank for bank | ✅ **MERGED round 1, no must-change finding.** PR #45, squash **`5b6c212`**, gated at head `2b7e840` on base pinned `065e67b`. Integration commit: **`integrate: script batch 020 — glossary, flags, handoff`**, the commit that adds glossary §61 and FLAGS §AW. Branch **NOT deleted** — HTTP 403 (§AQ9); `merged: true` on the PR is the signal. Glossary **§61**, FLAGS **§AW** |
| corrections | `tl/corrections-wave12` | §4.3 debt (see below) | **5 files, 5 items — 3 fixed, 1 fixed after its citation was vindicated, 1 no defect** | chunk 0 **+0 (measured, both versions through `bytes_from_body`)**, chunk 8 −2, chunk 31 −2; bank 28 −2, bank 0 −6 (31,431 → **31,425**, §AP7's predicted figure to the byte) | ✅ **MERGED round 1, no must-change finding.** PR #43, squash **`1134d2b`**, gated at head `fa03b4e` on base pinned **`3c6c579`** (merge-base `e9db558`, merge commit `c5aec14`, clean — the author's `merge-tree` was NOT reused). Integration commit: **`integrate: corrections wave 12 — glossary, flags, handoff`**, adding glossary **§62** and FLAGS **§AX**. Branch **NOT deleted** — HTTP 403 (§AQ9); `merged: true` plus the squash SHA is the signal. **Rulings: `Ｏ，　Ｏｉ，` stands (§62.4 / §AX3); §AQ5's `編成` row closed as a false positive of its own gate (§62.5 / §AX5).** **Discharged: §AJ3, §AP5 (merged work), §AP7, §AQ5's `batch_007` row.** **§37.1's `反乱` row stays LIVE for D1384 only.** Four glossary rows corrected in place (§23.2, §24.3, §34.1, §37.1) + a cross-reference added at §47.4 |
| `batch_021` | `tl/script-021` | 997–1034 | **38 lines / 38 inst**; 356 JP → 591 EN = **1.6601×**; 39 text runs, widest **23** (D1021), **none at 24**, max **2** text rows on any page; `{FFFE}` **46 → 39, net −7**; `{FCC0}` untouched, non-`{FFFE}` tag stream byte-identical on all 38 | **bank 30 only — realised +456**, not the 782 planning bound. Bank 30 **35,091 → 34,635 free** (⚠️ **NOT** the PR body's 35,119 → 34,663 — PR #45 spent 28 bytes in bank 30 in between; the **delta** is 456 on either base). Measured by holding the file aside and diffing: **exactly one line over 44 banks**, and it closes on the text arithmetic `(591−356)×2 − 7×2 = 456` | ✅ **MERGED round 1, no must-change finding.** PR #44, squash **`b3ca8cb`**, gated at head `1e55d1b` on base pinned **`f90f613`** (merge-base `e9db558`, merge tree **`f4bbc0e`**, clean — the author's `merge-tree` was NOT reused). Integration commit: **`integrate: script batch 021 — glossary, flags, handoff`**, adding glossary **§63** and FLAGS **§AY**. Branch **NOT deleted** — HTTP 403 (§AQ9); `merged: true` plus the squash SHA is the signal. **Rulings: ⭐⭐ descriptive labels take SENTENCE CASE, one ruling for both debug files (§63.1 / §AY3) — it ratifies what shipped, so NONE of the 30 titles shared with #46 moved; `マップＯＰ` → `Ｍａｐ　ｏｐｅｎｉｎｇ` expansion ratified over the `Ｒ１`/`ＯＫ` counter-precedent; `ｂｏｓｓ`'s third sense passes §25.3 on both axes.** **New: a SECOND script-side `tokenise` artifact on a DIFFERENT branch from §R4's/§AP2's (§AY2) — `{FF00}` at D1003, control-tag branch not SJIS-lead, 1 unique / 6 dump / 0 battle, zero shipping impact, and it means the fix must be an ARGUMENT-LENGTH TABLE.** **Nine figure/citation corrections, none touching a line of any file (§63.6 / §AY7).** **Ten glossary rows (nine the PR's + `マップクリアー`, found at review in segment 19 of a 29-segment pooled row); seven §9.W12 seeds promoted and EVERY ROW LEFT LIVE for #46 to strike.** ⚠️ **`音楽` is NOT exhausted after wave 12 — D1169 remains in bank 40 (§AY5).** Glossary **§63**, FLAGS **§AY** |
| `batch_022` | `tl/script-022` | 1043–1099 | **57 lines / 57 inst** | bank 31 only — **realised 1,724**, not my 2,185 bound | ✅ **PR #46 OPEN** |

## ✅ WAVE BARRIER MET — ALL FOUR PRs OPEN. REVIEWING ONE AT A TIME; **3 of 4 DONE**.
~~**#45 `batch_020`**~~ ✅ **MERGED `5b6c212`, round 1** → ~~**#43 corrections**~~ ✅ **MERGED
`1134d2b`, round 1, no must-change finding** → ~~**#44 `batch_021`**~~ ✅ **MERGED `b3ca8cb`,
round 1, no must-change finding** → **#46 `batch_022` (NEXT, and the last unit of the wave)**
(the two debug twins were kept adjacent so the second reviewer could pair them — **#44's reviewer
did the pairing itself, 30/30, and nothing moved**). `reviewer` subagents, `run_in_background: false`.
**Three units in a row merged at round 1.**
⚠️ **`git pull --ff-only` before dispatching the next reviewer — BOTH #45's and #43's reviewers
pushed integration commits, and #43's edited five `glossary.md` rows in place.**
⚠️⚠️ **EVERY `glossary.md:NNNN` CITATION IN AN OPEN PR BODY IS NOW STALE.** #45's integration shifted
things by +12 to +26 and #43's shifted them again. Measured at #43's review: `:1677`→`:1689`,
`:3350`→`:3362`, `:3948`→`:3972`, `:4265`→`:4289`, `:7367`→`:7393`. **CITE BY SECTION AND VERIFY A ROW
BY ITS TEXT** — #44's and #46's reviewers must not trust a line number from their PR body.
⚠️ **glossary §37.1's `反乱` census cell is now RENUMBERED and the DATA convention is NAMED there:
project DATA = the 0-based `script_unique.txt` index + 1**, pinned at #43's review against three
independent anchors (§34.4's D598 and D605, §42.5's D481). ⚠️ **The same row's `L6 / L4 / L4` battle
citations are 1-based BODY indices, while §61.5.6's "chunk 8 L14" was 0-based — three conventions are
live in one file (§AX6). State which one you are using for every number you quote.**
⭐ **§AX7 — a `{FFFE}`-only column check is WRONG in the dangerous direction on pooled rows.** It
reported `batch_012:53` at 27 columns and a finding was nearly raised; a `{FCC0}` sits *inside* that
segment, so the true rows are 14 and 15. `assemble.py:106` splits on `FCC0|FC30|FC51|FC50|FFFF` as
well as `FFFE` — **any hand-rolled column check must do the same.**
**4 of 4 translators returned, 0 lost, 0 re-dispatches.** Realised growth **1.87×–1.98×** against the
**2.10×** plan, so every unit came in under its bound.

✅ **All four dispatched 2026-09-11 as `translator` subagents of this session, `run_in_background: true`.**
⏰ **Watchdog armed: `trig_01D4W2WT4UMcxh2oPaCCxJnj`, fires 12:41Z.** It re-arms itself on every wake
and the chain of timers ends only when wave 13's session is open. **`ListAgents` is the authority on
whether a translator is alive — silence is NOT evidence, and a subagent that returned nothing is
LOST, not finished.**

⚠️ **Nothing is reviewed until ALL FOUR have an open PR** (CLAUDE.md §4 step 4, the wave barrier).
Then one reviewer at a time, in the order above, `run_in_background: false`.
⚠️ `tl/script-017`–`-019` and every older `tl/*` branch are **MERGED but still on origin** — deletion
returns **HTTP 403** (§AQ9). **"Branch gone = merged" is an INVALID signal here**; use the PR's merged
state and the `integrate:` commit.

## Next up — NOTHING, AFTER WAVE 12. This is the end of the dispatchable queue.
**Re-derived by me at wave 12's open** from `script_unique.txt` + `script_dump.txt` + a fresh
`merge`/`bankmeasure`, per-line at 2.10× with a 500-byte reserve, counting occurrences **per bank
with multiplicity**. I reproduced wave 11's headline figures exactly: **482 unique lines / 2,890
instances remain · 116 feasible / 139 instances · 366 blocked / 2,751 instances (95% of the
remaining message instances).** Feasible DATA ranges, computed not inherited:
**318, 320, 326–334, 336–345, 997–1034, 1043–1099.**

⚠️ **WAVE 12 TAKES ALL 116 FEASIBLE LINES.** 21 player-facing + 95 debug-menu = 116. There is no
fifth unit to plan. **After wave 12, every remaining line is blocked behind the §F2 bank repoint
(Blocked 2), which is a human task.**

| ⛔ BLOCKED — unchanged, and confirmed by my own measurement | Lines | Inst | Why |
|---|---|---|---|
| 1160–1354 | 195 | 195 | **bank 40 only** — needs ~11,073 against **75 free** |
| 1355–1387 | 33 | 33 | **bank 41 only** — needs ~33,573 against **353 free** |
| 138 others | 138 | **2,523** | 135 by bank 40, 3 by bank 5 — the item/armour tables, 21 instances per line |

⚠️ **TWO INHERITED FIGURES CORRECTED, IN OPPOSITE DIRECTIONS — both mine, both measured:**
1. **`batch_020` touches 21 BANKS, not "8–9".** Wave 11 corrected a long-inherited "18 banks" down
   to "8–9" and **over-corrected**; the original was nearer. Measured: banks 3,4,5,6,7,8,9,12,14,15,
   16,17,18,20,21,23,24,30,31,32,34. **The substance still holds — it is cheap**: per-bank cost runs
   26–374 bytes and the tightest (bank 5) needs **94** of 1,635. The *count* was wrong, not the verdict.
2. **`batch_021` needs 782 (not ~795); `batch_022` needs 2,185 (not ~2,254).** Formula rounding only.

**THE CORRECTIONS UNIT — ✅ ALL FIVE ITEMS RESOLVED AND MERGED (PR #43, `1134d2b`). RESOLUTIONS FIRST;
the dispatch-time notes below are kept only as a record of which citations misled whom.**

| # | Item | Outcome, as MERGED and verified at review |
|---|---|---|
| 1 | `反乱` → `ｒｅｂｅｌｌｉｏｎ` at **D897** (`batch_010:48`) | ✅ **FIXED.** `ｒｅｂｅｌｌｉｏｎ` is **9** columns, so the row goes **21 → 22, +2 bytes** — **my "+8 bytes / 21→25 / needs a re-wrap" was WRONG on all three counts.** The unit took the article from **shipped `batch_015:40` (D786)**, making both renderings of `反乱を起こした` byte-identical. §37.1's own scope clause *required* the change. **Split now clean: `ｒｅｖｏｌｔ` 0× in `tl/script/`, `ｒｅｂｅｌｌｉｏｎ` 0× in `tl/battle/`.** Row **stays LIVE for D1384** (bank 41, blocked) |
| 2 | `おい、` → `Ｏｉ，` | ✅ **FIXED, 5 cells.** Census: **`おい` = 22 (14 battle + 8 script)**; **all 8 in translated chunks now render `Ｏｉ，`** (5 here + chunks 20/37/38 already right); all 8 script instances untranslated, so the script store was never in debt. English side: **13 hey-family before, 5 defects, 8 remain, all `よう`/`よっ`.** ⚠️ **My `Ｈｅｙ，` grep was CASE-SENSITIVE and wrongly cleared `chunk_031` (it carried lowercase `Ｈ，　ｈｅｙ，`); the inherited citation was right and my correction was the error.** **§AJ3 DISCHARGED** |
| 3 | `品` → `ａｒｔｉｃｌｅ` at **D376** (`batch_012:53`) | ✅ **FIXED.** ⚠️ **My "the citation does not locate a real cell" was WRONG** — D376 is a **25-segment pooled row** and the `品` is in **segment 16**. +6 bytes into bank 0, columns **22/20/10 → 21/20/14**, §AP7's prediction to the column. **`品` → `ｇｏｏｄｓ` now 0 across `tl/`** (the survivor, `batch_012:62`, renders `モノ`). §34.1's reach cell corrected 3 → **6 shipped** of **8** bare-noun instances, consistent with §61.5.1. **§AP7 CLOSED** |
| 4 | hyphen stutters → comma form | ✅ **FIXED, 3 cells.** Re-derived: **60 hyphen runs → 11 stutters / 49 compounds; 8 of the 11 in parked `chunk_043*`, leaving exactly 3 in merged work.** `tl/` now holds **0** hyphen stutters. ⭐ **All three sources are `X、X…` comma stutters, so the comma form is the LITERAL rendering** — stronger ground than §AP5's convention argument. **§AP5 DISCHARGED for merged work** |
| 5 | `編成` (§AQ5) | ✅ **NO DEFECT — and the flag is CLOSED for free.** `編成` → `“Ｆｏｒｍａｔｉｏｎ”` in **both** cells; D432's English legitimately reverses the two menu names, and **§AQ5's gate pairs the Nth bracket with the Nth quote, so a licensed reorder faked the divergence.** §Z1's own table already had the correct pairing. **No ruling, no sense-split, no disc needed. Blocked 7 / §Z1 UNCHANGED** |

**RULING ISSUED at review, 0 bytes either way:** `chunk_031` keeps **`Ｏ，　Ｏｉ，`**, not §AJ3's
suggested `Ｏ，　ｏｉ，`. **§AJ3's analogy to `おいおい、` → `Ｏｉ，　ｏｉ，` was the wrong comparison
class**: a **fragment stutter** (word said once, false start) capitalises — **23 : 6** in `tl/` — and
a **word doubling** (word said twice) does not — **7 : 0**. Both forms stand; written to glossary
**§62.4** so a later unit cannot "fix" one into the other. ⚠️ **The unit's own "27 stutters, 21 : 6"
and "all 27 are sentence-initial" were both wrong** (measured: 26 at 19 : 7 before, 29 at 23 : 6
after; only 23 of 33 segment-initial) — **its conclusion survives, its premises did not.**

⚠️ **THE DISPATCH-TIME NOTES BELOW ARE SUPERSEDED. Three of my five briefs to this unit were wrong
and the translator caught every one.** Kept for the method record only:
- ⭐⭐ **`反乱` — the GLOSSARY'S OWN CENSUS IS OFF BY ONE ON ALL FOUR ENTRIES.** The row at
  `glossary.md:3883` lists the script instances as "DATA 443, 785, 896, 1383". **None of those four
  contains `反乱` at all.** Measured: bare `反乱` (excluding `反乱軍`) is at **DATA 444, 786, 897,
  1384**. This is §AQ3's 0-based/1-based trap, sprung *inside `glossary.md`*. HANDOFF's "D897" was
  **right**; the glossary is wrong and the row must be fixed.
  **The defect itself is real and isolated**: D444 → `ｒｅｂｅｌｌｉｏｎ` ✓, D786 → `ｒｅｂｅｌｌｉｏｎ` ✓,
  **D897 → `ｒｅｖｏｌｔ` ✗** (`batch_010.tsv:48`), D1384 untranslated (bank 41, blocked). §38.3 governs
  the **script** store; `ｒｅｖｏｌｔ` is the **battle** store's form and both legitimately stand.
  ⚠️ **NOT byte-negative: `ｒｅｖｏｌｔ`→`ｒｅｂｅｌｌｉｏｎ` is +8 bytes** (bank 28, 30,491 free — fine)
  **and takes that row from 21 to 25 columns, over the 24 limit, so the page needs a re-wrap.**
- ⚠️ **`Ｈｅｙ，` vs `Ｏｉ，` (§AP9) — the census is wrong in BOTH directions.** Inherited: "`chunk_000`
  ×3 / `chunk_008` / `chunk_031`". Measured across all of `tl/`: **`Ｈｅｙ，` = 11 in 8 files**
  (`chunk_000` ×3, `chunk_006` ×1, `chunk_008` ×1, `batch_006` ×1, `batch_013` ×1, `batch_014` ×1,
  `batch_015` ×1, `batch_016` ×2) and **`Ｏｉ，` = 4** (`chunk_020`, `chunk_037`, `chunk_038`,
  `batch_007`). **`chunk_031` does NOT contain `Ｈｅｙ，`.** ⚠️ **11 is NOT 11 defects** — §32.3 fixes
  only `おい、` → `Ｏｉ，`, and `Ｈｅｙ，` may legitimately render `ねえ、`/`おーい` etc. **The source side
  must be censused per instance**; I have not done that, so this cell is **UNVERIFIED** and the unit
  must derive it.
- ⚠️ **`品` → `ｇｏｏｄｓ` "at DATA 376" (§AP7) looks MIS-CITED.** `ｇｏｏｄｓ` appears in `tl/` only at
  `batch_012.tsv:53` and `:62`; DATA 376 is a mayor's greeting in `batch_00x` with no `ｇｏｏｄｓ`.
  **UNVERIFIED — the unit must locate the real cell before changing anything.**
- **`§AP5` `chunk_000` hyphen stutters — 3 confirmed** (`Ｎ‐ｎｏｗ`, `Ｔｈ‐ｔｈｉｓ．．．`, `Ｗｈ‐ｗｈａｔ`).
  48 hyphen-joined forms exist across `tl/` in total, but that includes legitimate compounds
  (`ｅａｓｙ‐ｇｏｉｎｇ`), so the "19 : 3" split is **UNVERIFIED**.
- **`§AQ5` `編成` → both `Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ` and `Ｆｏｒｍａｔｉｏｎ` in `batch_007`** —
  `編成` is at `batch_007.tsv:32` and `:38`; `Ｆｏｒｍａｔｉｏｎ` occurs 3× in `tl/`. Real, but tangled
  with **Blocked 7 / §Z1** (the three `『』` UI labels need one look at the Formation screen).
  ⚠️ **Do not "fix" this into a wrong form while the screen is unread** — prefer flagging.

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
   chunks — and `riotscript` alongside it, since it is the same three-line change.**
   ⚠️⚠️ **WIDENED AGAIN 2026-09-11 (PR #44 review, `FLAGS.md` §AY2): THE SCRIPT SIDE HAS A SECOND
   INSTANCE ON A DIFFERENT BRANCH OF THE SAME FUNCTION, AND IT CHANGES WHAT THE FIX HAS TO BE.**
   **DATA 1003** carries `{FFF3}{=00}{FF00}{=14}` — `{FF00}` is not a real tag. `riotscript.py:38`
   `is_sjis_lead` is `0x81..0x9f or 0xe0..0xef`, so **`0xFF` is NOT a lead byte**; `tokenise_stream`,
   having no argument-length table, meets `0xFF` in its **`0xfb <= c <= 0xff` CONTROL-TAG branch** and
   emits a tag from an argument byte. **DATA 367 fires on the SJIS-LEAD branch; DATA 1003 on the
   CONTROL-TAG branch.** ⭐ **A fix that only reorders or widens the SJIS-lead test leaves DATA 1003
   standing. ONE ARGUMENT-LENGTH TABLE fixes both branches, in both tools — specify it that way.**
   Census re-run at source: `{FF00}` = **1 in `script_unique.txt`, 6 in `script_dump.txt` (lines 43,
   58, 3149, 6420, 6970, 7085), 0 in the battle dump**; all six are `{FFF3}` selector runs whose value
   is `0xFF`. ⚠️ **Zero shipping impact, proved from the encoder's grammar** — `{FFF3}{=00}{FF00}{=14}`
   and `{FFF3}{=00}{=FF}{=00}{=14}` both emit `ff f3 00 ff 00 14`, and `tl/script/batch_021.tsv`
   reproduces the dump's form verbatim on both sides. **So the script dump now holds TWO artifact lines
   by TWO mechanisms, not one.** The dumper prefers a Shift-JIS text run over a control tag whenever an argument byte
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

### ⭐⭐ WAVE 12 — PR #44 `batch_021` MERGED ROUND 1: THE CASE POLICY IS RULED FOR BOTH DEBUG FILES, AND A SECOND TOKENISER BRANCH IS NAMED
**`DECISION: MERGE`, round 1, no must-change finding.** Squash **`b3ca8cb`**, gated at head `1e55d1b`
on base pinned **`f90f613`**, merge tree **`f4bbc0e`** derived at review (the author's `merge-tree` was
**not** reused — the base had moved through two merges, two integration commits and a seed correction
since the PR was opened). Glossary **§63**, FLAGS **§AY**. 38 lines / 38 instances, DATA 997–1034,
**bank 30 only, +456 bytes** (35,091 → 34,635 free), **1.6601×**, widest run 23, none at 24, max 2 text
rows. **Findings: none that must change; nine figure/citation corrections, not one touching a line of
any file.**

1. ⭐⭐ **THE CASE POLICY IS RULED ONCE, FOR BOTH DEBUG FILES, AND IT RATIFIES WHAT SHIPPED (§63.1 /
   §AY3).** **Descriptive labels take SENTENCE CASE** — initial capital on the row's first word, every
   glossary-fixed component byte-identical and lowercase below it; **title case only for a NAMED thing
   or a §9-seeded label form.** The PR argued this, recorded the counter-argument honestly, and shipped
   the side the corpus supports. **The decisive evidence is one the PR did not cite: §56.2 ships EIGHT
   gutter-prefixed MENU LABELS and every one is sentence case** (`　Ｙｏｕｎｇ　ｗｏｍａｎ　ｐａｓｓｉｎｇ　ｂｙ`,
   `　Ｂｅａｔ　ｈｉｍ`, `　Ｄｏ　ｎｏｔｈｉｎｇ`, …) — so §17.1's "a label column is capitalised throughout or not
   at all", which is written about the **class-name table**, does not reach a *descriptive* label
   column. Title case would have reproduced §51.4's shipped `Ｗｅ　Ｈｏｂｂｉｔｓ` gate-7 failure in three
   places at once. ⭐ **#46 inherits this and must conform, not re-decide.**
2. ⭐⭐ **THE TWIN PAIRING WAS DONE AT THIS REVIEW, 30/30, AND NOTHING MOVED.** `batch_021`
   D1005–D1034 ↔ `batch_022` D1053–D1082 are the same 30 readable strings differing **only** in the
   trailing `{FFF8}` argument, so **gate 6 pairs nothing** (it reported clean — correctly and
   uselessly). Paired by readable text, resolving each `batch_022` DATA from its own JP key rather
   than by an offset: **`title mismatches: 0`, 30/30 identical including the `ＮＮ：` prefix**, D1027 ↔
   D1075 identical including the break position. **Because no finding required a change, #46's own
   30/30 diff still stands and no re-diff is needed.**
3. ⭐⭐ **A SECOND SCRIPT-SIDE `tokenise` ARTIFACT, ON A DIFFERENT BRANCH FROM §R4's AND §AP2's, AND IT
   CHANGES WHAT THE FIX MUST BE (§AY2).** `{FF00}` at **D1003**, verified **from the tool source**:
   `riotscript.py:38` `is_sjis_lead` excludes `0xFF`, so `tokenise_stream` — which has **no
   argument-length table** — meets `0xFF` in its `0xfb <= c <= 0xff` branch and emits a tag from an
   **argument byte**. **§AP2's D367 fires on the SJIS-LEAD branch; this one on the CONTROL-TAG branch.
   A lead-byte-only fix leaves it standing; one argument-length table fixes both, in both tools.**
   Census re-run at source: **1 in `script_unique.txt`, 6 in `script_dump.txt` (lines 43, 58, 3149,
   6420, 6970, 7085), 0 in the battle dump** — the PR's figures to the byte. **Zero shipping impact,
   proved from the encoder's grammar**: `{FFF3}{=00}{FF00}{=14}` and `{FFF3}{=00}{=FF}{=00}{=14}` both
   emit `ff f3 00 ff 00 14`. **Blocked 0 is now two script-unique lines by two distinct mechanisms.**
4. ⚠️ **`音楽` IS NOT EXHAUSTED AFTER WAVE 12 — D1169 remains, in bank 40 (§AY5).** 23 unique lines;
   9 here, 13 in `batch_022`, and the 23rd is `音楽のＯＮ・ＯＦＦを切り替えます` (count 1, bank 40, 75 bytes
   free — blocked). It inherits this unit's `ｍｕｓｉｃ` and its **verbatim `ＯＮ`/`ＯＦＦ`**, and ⚠️ **its
   `・` is outside §3.1 and needs the §45.7 / §56.2 treatment.** The §60.4 / §AV4 shape again: a status
   asserted from a wave's own coverage.
5. ⭐ **A NEW INCUMBENT, FOUND BY READING SEGMENT 19 OF A 29-SEGMENT POOLED ROW (§AY6).**
   `batch_013.tsv:86` (D978) already ships `マップクリアー時に` → `ｗｈｅｎ　ｙｏｕ` / `ｃｌｅａｒ　ｔｈｅ　ｍａｐ`.
   **Not a divergence from this unit's `Ｍａｐ　ｃｌｅａｒｅｄ`** — §17.2 kana-lengthener variant, clause vs
   label, one head word conjugated to each source's shape (§51.3 / §27.1) — **but written down so a
   later corrections unit cannot "fix" one into the other.** Third time a pooled row has had to be read
   segment by segment (§61.1, §62.3, this).
6. **Gate 7's three faces, corpus stated: 1,704 key cells (1,319 distinct) · 4,452 all-cell CJK runs
   (2,261 distinct) · a face-(c) `tl/` COLUMN-2 PASS over 4,075 aligned JP→EN segment pairs.** Face (c)
   paid for itself twice — it confirmed `音楽`/`ｍｕｓｉｃ` genuinely free (0 segments, 0 in all of `tl/`)
   and it is what surfaced item 5. **Three of the unit's terms are note-cell-only** (`バトル`, `伝説の`,
   `です`). ⚠️ **`その他` is NOT in this unit at all** — 0 occurrences; all 10 are `batch_022`'s, contrary
   to the dispatch.
7. **Verified rather than accepted:** `ｍｏｂ`'s five `tl/` hits are all `ｍｏｂｉｌｅ`/`ｍｏｂｉｌｉｔｙ` (read one
   by one) · `ｂｏｓｓ`'s three senses are disjoint by store and bank · the battle side of gate 6 done
   **positionally** against `dumps/battle_dump.txt` (0 of 38 messages, 0 of 46 segments) because
   `tl/battle/` holds no Japanese · `rowcheck script`'s 19 warnings **attributed**, not trusted — none
   in this unit's merged-dump range 6964–7002, and they sit in banks [0,5,12,13,14,22,25,29,33,41,42],
   **no bank 30 and no bank 31**.
8. ⚠️ **Two of my own dispatch claims were wrong and the measurement won**: "the unit's table claimed
   23 for its own 21" (**it did not** — all 38 widths reproduce exactly) and "this unit's own `その他`
   rendering depends on it" (**it has no `その他`**).

### ⭐⭐ WAVE 12 — PR #43 MERGED ROUND 1: FOUR FLAGS RETIRED, AND A TOOLING FINDING THAT CHANGES HOW WE HAND-MEASURE
**`DECISION: MERGE`, round 1, no must-change finding.** Squash `1134d2b`, integration `173c197`,
glossary **§62**, FLAGS **§AX**. Base pinned `3c6c579`, merge-base `e9db558`, **the author's
`merge-tree` was NOT reused**. No semantic collision with `batch_020`'s §34.1/§34.4 rewrite.

1. ⭐⭐ **`assemble.py:106` SPLITS RUNS ON `{FCC0|FC30|FC51|FC50|FFFF}` AS WELL AS `{FFFE}` — SO ANY
   HAND-MEASUREMENT THAT SPLITS ONLY ON `{FFFE}` CAN OVERSTATE COLUMNS.** The reviewer caught its own
   near-miss this way: a `{FFFE}`-only split reported `batch_012:53` at **27 columns**, but a `{FCC0}`
   sits inside that segment and the true rows are **14 / 15**. ⚠️ **I have been telling every agent
   to "hand-measure" insert-bearing rows without saying what to split on. Verified in the source by
   me. This goes in every future brief.**
2. ⭐⭐ **§AQ5's `編成` ROW IS CLOSED AS A FALSE POSITIVE OF ITS OWN GATE — AN OPEN FLAG RETIRED FOR
   FREE, AND WITHOUT THE DISC.** D432's English legitimately reverses the two menu names (§2.1 step 6)
   and the gate's Nth-bracket/Nth-quote pairing faked a collision. **§Z1's own table already had it
   right.** ⚠️ **§Z1 / Blocked 7 are UNCHANGED** — this answers only the consistency question, not
   whether the labels match the screen.
3. ⭐⭐ **`Ｏ，　Ｏｉ，` STANDS, AND THE REVIEWER FOUND THE FACT NOBODY NAMED.** `batch_007.tsv:24`
   ships the **doubled** `おいおい、` as `Ｏｉ，　ｏｉ，`, and **§AJ3 proposed the lowercase form by
   analogy to that — the WRONG COMPARISON CLASS.** Measured: **fragment stutters 23 : 6 capitalised;
   word doublings 7 : 0 lowercase.** Both stand, written to §62.4 so nobody "fixes" one into the other.
4. ✅ **FOUR FLAGS DISCHARGED: §AJ3 · §AP5 (merged work) · §AP7 · §AQ5's `batch_007` row.**
   **§37.1's `反乱` row stays LIVE for D1384 only** (bank 41, blocked). Four glossary rows corrected
   in place (§23.2, §24.3, §34.1, §37.1) plus a cross-reference at §47.4.
5. ⭐ **THE CITATION TRAP'S FIFTH FACE — THREE CONVENTIONS COEXIST IN ONE FILE.** §37.1's "c22 L6" is
   a **1-based BODY index**; §61.5.6's "chunk 8 L14" (mine) was **0-based**; the documented convention
   is a 1-based FILE line. **All three are live in `glossary.md` right now.** Renumbered and the
   convention named in place.
6. ⚠️ **THREE OF THE UNIT'S OWN FIGURES WERE WRONG and the reviewer re-derived them** — "27 stutters,
   21 : 6" → **26 at 19 : 7 before, 29 at 23 : 6 after**; "all 27 are sentence-initial" is **false**
   (23 of 33), though the conclusion survives; and its bank 5 paste (1,635) was stale, now **1,595**.
   ⚠️ **All its `glossary.md:NNNN` citations had moved (+12 to +26).** ✅ **All 14 DATA citations exact.**
7. ✅ **MY FIRST THREE ERRORS CONFIRMED IN DETAIL, AND ITEM 1 WAS WRONG ON ALL THREE COUNTS**: my
   "+8 bytes / 21→25 columns / needs a re-wrap" is really **+2 / 21→22 / no re-wrap**, and the donor
   is real (`batch_015.tsv:40` D786 ships `ｒａｉｓｅｄ　ａ　ｒｅｂｅｌｌｉｏｎ．`). My case-sensitive grep:
   confirmed wrong, **5 defects of 13, the 8 survivors all `よう`/`よっ`**. Pooled D376: the unit was
   right, `品` is in **segment 16**, +6 into bank 0 (31,431 → **31,425**, §AP7's predicted figure to
   the byte).
8. ⚠️ **`品` SIX vs §61.5.1's EIGHT — BOTH RIGHT, NO CONTRADICTION**: **6 shipped, 8 bare-noun**
   (D1278/D1304 untranslated in bank 40). A reach and a status, not a disagreement — §58.5's lesson.
9. ⭐ **`bankmeasure`'s `tightest:` NOW HIDES BANK 2; BEFORE #45 IT HID BANK 5. WHICH ONE IS INVISIBLE
   IS NOT STABLE.** Verified by me just now: four banks under 2,000 — **40 → 75 · 41 → 353 ·
   5 → 1,595 · 2 → 1,607** — and the line prints 40, 41, 5. **Never quote that line.**

### ⭐⭐ WAVE 12 — PR #45 MERGED ROUND 1, AND GATE 7's THIRD FACE EARNED ITS KEEP IMMEDIATELY
**`DECISION: MERGE`, round 1, no must-change finding.** Squash `5b6c212`, integration `463b01b`,
glossary **§61**, FLAGS **§AW**. Base pinned `065e67b`, re-fetched at both ends and unchanged.
Script **948 → 969 unique lines · 5,041 → 5,085 instances · 63.6% → 64.1%.** All 21 bank deltas
**re-derived twice by independent routes** and agreeing bank for bank at **+2,256 B**.

1. ⭐⭐ **THE `tl/` COLUMN-2 PASS (gate 7 face (c)) FOUND THREE FINDINGS NOTHING ELSE COULD HAVE —
   ON ITS FIRST USE.** 2,893 aligned JP→EN segment pairs, 28 of 28 counterparts byte-identical.
   ⚠️ **Its finding 1 is the kind that invalidates shipped work: the proposed `立ち寄る`/`寄る` →
   `ｃａｌｌ　ｉｎ` key OVER-REACHED.** `tl/script/batch_014.tsv:36` (D734, bank 19) already ships the
   bare verb as **`ｄｒｏｐ　ｉｎ`**. Census over every inflection: **13 instances / 9 unique lines,
   banks [3,4,19,20,21,40,41]**. §25.3 **MET** (`ｃａｌｌ　ｉｎ` [3,4,20,21] vs `ｄｒｏｐ　ｉｎ` [19],
   disjoint) → **both stand, the key was narrowed at integration, nothing re-cut.**
   **Face (c) is now mandatory in every reviewer brief and it has paid for itself once already.**
2. ⚠️ **MY CITATION-CONVENTION ERROR PROPAGATED FROM MY SEED INTO THE TRANSLATOR'S FLAG.** I wrote
   "chunk 8 L14"; that is a **0-based body index**, not the 1-based FILE line the convention promises
   — it is `battle_dump.txt` line **234** (1-based, exact) and `chunk_008.txt` **file line 16**.
   **A malformed citation does not stay in the document you wrote it in.**
3. ⚠️ **`占領` ALREADY HAD TWO SHIPPED ENGLISHES** — `ｓｅｉｚｅｄ` (`batch_010:42`, bank 28) and
   **`ｔｏｏｋ`** (`batch_012:67`, bank 1) **for the same event.** Found by reading **all 141 segments**
   of that pooled row. D320 is on the right side; recorded as live §4.3 debt.
4. ✅ **TRAP 4's ABSENT CLOSING STOP IS CORRECT, AND THE TRANSLATOR WAS RIGHT AGAINST ITS OWN DONOR**
   — settled by a **controlled positive case**: `batch_011:8` (D647) *does* carry `。` and *does* ship
   `．`, while D333/D338 carry neither. **All four traps ship byte-identically**; D339 keeps its own
   `{FFF6}` args; indents preserved per source (4 / 2 / 4+7 / 3).
5. **Three more figure corrections, none affecting a rendering:** only **1** `立ち寄` instance remains,
   not 2 (D838 is already shipped at `batch_016:66` as `ｗｈｙ　ｎｏｔ　ｃａｌｌ　ｉｎ？`, a second
   incumbent that *strengthens* the row) — and ⚠️ **`立寄って` (D1377) is a kanji-elision variant a
   `立ち寄` grep cannot see.** D328 is the **tenth** `ご用`/`用` opener, not the sixth. §34.1's
   `貼り紙` binds cell named 2 of 5 siblings. Flag 6's alternative is **24** columns, not 25 — verdict
   firmer, since the shipped English is 75 columns against a 3×24 = 72 ceiling, so **no three-row
   packing exists at any wording**.
6. ⚠️ **§34.1's `品` FIGURE REPRODUCED EXACTLY** — bare `品` = **8 instances / 5 banks [0,12,13,19,40]**
   — and **no collision with PR #43 either way it lands** (#43's target is a bare `品` in bank 0;
   `batch_020`'s new `商品` → `ｗａｒｅｓ` is a different noun in bank 20). Corrected census at §61.5.1.
7. ⚠️ **NOTE FOR THE #43 REVIEWER: `git pull --ff-only` FIRST, and its base has moved well past the
   `45bab1c` it was opened on** — re-verify the merge against the current tip, do not reuse the
   author's `merge-tree` result.
8. ⚠️ **A LIVE DEMONSTRATION OF THE BATTLE NULL-CHECK, BY ME, JUST NOW:** I grepped
   `tl/battle/chunk_008.txt` for `てーこく` to verify finding 5 and got **zero hits** — because
   **battle `tl/` holds NO Japanese.** The rule I have been handing to every agent this wave caught me
   the moment I stopped applying it. **Pair the battle dump positionally; never grep battle `tl/`.**

### ⚠️ WAVE 12 — `batch_022` (PR #46): I RELAYED A TABLE WITHOUT MEASURING IT, AND REPEATED AN ERROR I HAD ALREADY DIAGNOSED
1. ⭐⭐ **I RELAYED `batch_021`'s WIDTH TABLE TO `batch_022` VERBATIM AND IT WAS WRONG ON 18 OF 22
   ROWS.** `batch_022` distrusted the relay, **read `batch_021`'s actual branch**, and was right.
   Verified by me: `Ｔａｌｋ　ｗｉｔｈ　ｃｏｍｒａｄｅｓ` is **18** columns, so `batch_021`'s row is **21**
   (its table claimed 23) and `batch_022`'s menu row is **22** (I relayed **24**). ⚠️ **So my
   "track 20 lands at exactly 24, zero slack" was FALSE.** `track 17 = 24` **was** right, and track 18
   was understated. **A relayed measurement is not a measurement. I passed on another agent's table
   as fact without re-deriving a single cell of it.**
2. ⭐⭐ **I DIAGNOSED THE STALE-CITATION BUG THIS WAVE AND THEN LEFT IT IN MY OWN SEED.** `batch_022`
   found **both** of §9.W12's below-the-insert "already keyed" citations off by **exactly 65** — and
   §9.W12 is **exactly 65 lines**. `インターミッション` `:6815`→`:6880`, `魔族` `:4525`→`:4590`.
   (The two citations *above* line 868 — `貼り紙` `:699`, `ジュエル` `:96` — were unaffected and correct.)
   ⚠️ **I recorded this exact failure mode after the corrections translator caught it, and did not go
   back and fix the pointers sitting in my own text. Diagnosing a defect and leaving it in place is
   worse than not noticing it.** **FIXED at `6da4f95`: both now cite by SECTION, which does not move.**
3. ⭐⭐ **GATE 7 HAS A THIRD FACE, AND NO GLOSSARY-SIDE HARVESTER CAN REACH IT.** `その他` has **0
   mentions in `glossary.md` of ANY kind — 0 key cells AND 0 note cells — yet ships 7× in
   `batch_013`** as `　Ｓｏｍｅｔｈｉｎｇ　ｅｌｓｅ`. So: **(a) key cells · (b) NOTE cells (§AT1's `さ、`) ·
   (c) forms SHIPPED IN `tl/` THAT THE GLOSSARY NEVER RECORDED AT ALL.** ⚠️ **Face (c) defeats even a
   perfect note-cell harvester.** **GATE 7 NEEDS A `tl/` COLUMN-2 PASS** — harvest JP→EN pairs from the
   shipped TSVs themselves. Recorded in §9.W12 at `6da4f95`.
4. ⚠️ **MY "YOU MUST ABBREVIATE TRACK 23" WAS HALF RIGHT.** `batch_021` kept §42.1's full
   `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ` by splitting across one `{FFFE}`; `batch_022` matched it
   byte-for-byte on the confirmation row and abbreviated **only** the 4-option menu row — which is the
   source's own `ＩＭ`/`インターミッション` policy. **Better than what I told it to do.**
5. ✅ **THE CROSS-UNIT BLOCKER IS RESOLVED IN THE FILE, NOT DEFERRED.** All **30** shared strings carry
   `batch_021` PR #44's English, **verified 30/30 by direct byte diff of its branch**. The reviewer
   re-runs that diff **only if `batch_021` is reworked**. ✅ **`batch_022` WITHDREW its own title-case
   draft** after finding `batch_013` and `batch_021` both contradicted it — its own counter-evidence
   pointed at their answer. **That is the standard: an agent overturning itself on evidence.**
6. ⚠️ **ONE 24-COLUMN ROW IS THE REVIEWER'S CALL** — `　１７：Ｂａｔｔｌｅ　（ｂｏｓｓ　ｂａｔｔｌｅ）`, at the
   hard limit with zero slack, fixable by abbreviating that menu row alone. **119 of 120 runs are ≤ 23.**
7. **The unit is TWO debug tools, not one** — D1083–1099 is a **flag editor**, distinct from the sound
   test. ⭐ **First rendering anywhere of two place names**: `キエーザ城` → `Ｋｉｅｓａ　Ｃａｓｔｌｅ`,
   `ルクレール城` → `Ｌｅｃｌｅｒｃ　Ｃａｓｔｌｅ`. Live rows: `ほこら`, `館`, `キエーザ`, `インターミッション`.

### ⚠️ WAVE 12 — `batch_020` (PR #45): A FOURTH TRAP I MISSED, AND A SEED CELL WRONG IN ALL THREE FIGURES
1. ⭐⭐ **THERE WAS A FOURTH NEAR-DUPLICATE TRAP AND THE GLOSSARY HAD ALREADY WRITTEN IT DOWN.**
   I built the trap list at three and missed **D326**, which is **readable-identical** to
   `batch_008.tsv:38` (D481) — same message, differing only by a leading `{FC51}`, so gate 6 reports
   clean and a divergent English would ship undetected. ⚠️ **`glossary.md:5162` names the pair in
   terms: `| **481** | そう。疲れたときはいつでもよってね。 | **DATA 326, count 2, untranslated** |`** —
   verified by me after the fact. The translator found it independently and shipped byte-identically,
   segment for segment. **My three traps were all correct; the fourth was sitting in §42.5's
   FORWARD-BINDING table, which no gate reads and which I never opened.**
   ⭐ **STANDING RULE FROM NOW ON: §42.5's forward-binding table is the FIRST place a script unit
   looks.** It still holds **two live rows — `505` → D535 and `506` → D403**, both untranslated and
   both in the blocked set; whoever unblocks them must reuse the bound English.
2. ⭐⭐ **MY §9.W12 `てーこく` CELL WAS WRONG IN ALL THREE OF ITS FIGURES, AND THE VERDICT SURVIVED
   ANYWAY.** I wrote "**9 script / 0 battle / 0 `tl/`**" and "D320 is the first to ship, so it sets
   precedent". Measured by me after the translator's push-back:
   - **16 unique lines / 20 script instances**, not 9. **9 is the instance count of `てーこく軍`
     specifically** — my own `てーこく*` wildcard did not describe the number I put beside it.
   - **1 battle, not 0** — `dumps/battle_dump.txt:234` (chunk 8 L14).
   - **NOT 0 in `tl/`: already shipped twice** — `tl/battle/chunk_008.txt` L14 and
     `tl/script/batch_014.tsv:46`. **So the precedent was set in WAVE 2, and D320 conforms to a
     two-wave-old incumbent rather than setting anything.** `glossary.md:2470` (§29.6) already
     recorded the chunk-8 treatment.
   ⚖️ **The RECOMMENDATION was right** — do not misspell the English, carry the kana softening in
   register, keep `帝国` → *the Empire* distinct from `帝国軍` → *the Imperial army* with its article.
   **But I asserted a reach, a store and a status I had not checked, in the very cell whose header
   tells the reader I had checked all three.** ⚠️ **This is the FOURTH error of this shape by me this
   wave and it is the worst, because §9.W12's own preamble states the rule I broke: "census every
   reach cell in BOTH spellings and BOTH stores, and mark unverified cells unverified."** 13 unique /
   15 instances of `てーこく` remain, all blocked; they inherit this form.
3. ⭐ **D320 HAS AN UNTRANSLATED READABLE-IDENTICAL SIBLING: D1332, IN BANK 40.** Nothing in my
   dispatch or in `glossary.md` named it; the translator found it by visible-text pairing. Different
   tag stream, so **gate 6 is blind**. **Whoever renders D1332 after the §F2 repoint must reuse
   `batch_020`'s English byte-for-byte.**
4. ⚠️ **§34.1's `品` REACH CELL IS A RAW SUBSTRING COUNT, NOT A CENSUS.** It reads "script **44
   across 23 banks**"; the **bare noun is 8 instances across 5 banks — [0, 12, 13, 19, 40]**. The
   44/23 is inflated by `商品`, `景品`, `作品` etc. **No rendering turns on it**, but it is the number
   a future §25.3 co-occurrence test would use, and it would give the wrong answer. ⚠️ **Interacts
   with PR #43**, whose `品` → `ａｒｔｉｃｌｅ` fix is at `batch_012` D376 (bank 0, a **bare** `品`);
   `batch_020`'s new `商品` → `ｗａｒｅｓ` is a different noun in bank 20 and does not touch it.
5. ⚠️ **REALISED vs PLANNING, AGAIN — AND MY PER-BANK RANGE WAS WRONG AT THE TOP END.** Bank 5 needed
   **40**, not my 94 (unit realised **1.9756×** against the 2.10× plan). But the **maximum per-bank
   cost was 410 (bank 18), ABOVE the "26–374" range I quoted** — bank 18 carries two of the three
   longest lines at 2 occurrences each, where my 374 was bank 20's. Predicted and measured agree
   bank-for-bank in the PR. **Quote a planning bound and a realised figure as two numbers, and do
   not state a max without checking which bank actually carries the worst line.**
6. ⭐ **`bankmeasure`'s `tightest:` LINE NOW PRINTS BANK 5 INSTEAD OF BANK 2 — the cleanest possible
   proof it cannot be quoted.** Before: `40 · 41 · 2 (1,607)`. After: `40 · 41 · 5 (1,595)`. **Bank 2
   became invisible because bank 5 dropped 40 bytes past it.** Four banks are under 2,000 either way.
7. ⚠️ **NEW §4.3 DEBT, NOT CREATED BY THIS UNIT: `なるけど、いいかい？` HAS TWO SHIPPED ENGLISHES** —
   `batch_011:54` `ｔｈａｔ　ａｌｌ　ｒｉｇｈｔ？` vs `batch_012:91` `ｂｕｔ　ｉｓ　ｔｈａｔ　ａｌｌ　ｒｉｇｈｔ？`,
   byte-identical source, banks 2 and 17. **For a future corrections unit.**
8. ✅ **THE THREE TRAPS I DID NAME WERE ALL MET AND ASSERTED**: D329 = D330 and both byte-identical
   to all 10 shipped copies of the recruit menu; D339 byte-identical to `batch_011`'s monster-shop
   menu with **its own** `{FFF6}` args; D333/D338 differ in exactly one word, and **each source's own
   indent was preserved (four spaces, NOT the two-space donor's)**. ⭐ **A refinement worth keeping:
   D333/D338 correctly take NO closing full stop** — `batch_006:57`'s stop belongs to the `ノロ` tic,
   and §57.1's `「本日休業」` → `“Ｃｌｏｓｅｄ　ｔｏｄａｙ”` is the real precedent. A reviewer reading the
   donor alone would wrongly expect one.
9. ✅ **AN EXEMPLARY METHOD DISCLOSURE, AND THE BOARD SHOULD ASK FOR IT EVERY TIME.** The translator
   stated plainly that it did **not** read §27–§31, §35–§39, §41, §43–§46, §49–§54 linearly, covering
   them instead by harvesting **1,333 first-column keys + 2,158 backticked runs across key AND note
   cells** and reading all 94 rows that fired. **That is the §AT1-compliant harvester** — but it is
   not the same as a linear read, and saying so is what lets a reviewer weigh it.

### WAVE 12 — `batch_021` (PR #44): a realised-vs-planning figure, and a NEW tool artifact
1. ⚠️ **MY 782-BYTE BANK FIGURE WAS A PLANNING BOUND, NOT A PREDICTION — THE REALISED COST IS 456.**
   `batch_021` measured bank 30 at **35,119 → 34,663 free** from a real `merge` + `bankmeasure`, and
   it closes arithmetically: `(591 − 356) × 2 − 7 × 2 = 456` (English merges 8 flag rows, netting
   **−7 `{FFFE}`** at 2 bytes each). Realised growth was **1.66×**, not 2.10×.
   ⚠️ **This is not the same kind of error as the three below.** 2.10× is this run's *documented*
   planning rate (Standing, waves 4–11) and overstating is the safe direction for a **feasibility
   floor** — a unit that fits under 2.10× certainly fits. **But the realised figure is 456 and that
   is what the record should carry.** The translator's framing is exactly right: re-measuring was
   the correct instinct, and the correction is larger than the rounding I anticipated.
   **Lesson for the final handoff: quote the planning bound and the realised figure as two numbers,
   never one.** Realised growth across waves has run 1.66×–2.04× against a 2.10× plan.
2. ⚠️ **MY §9.W12 "Where seen" CELLS ARE ONE UNIT SHORT ON SIX ROWS.** `任務失敗`, `ザコ戦`, `ボス戦`,
   `ゲームオーバー`, `宿敵` and `魔族` name `batch_022` only and **omit `batch_021`'s own instance**.
   The counts are right; the attributions are wrong. One-line fix per row at promotion.
   ✅ **VERIFIED CELL BY CELL AT PR #44's REVIEW and my `6da4f95` correction is RIGHT** — `任務失敗` 3 =
   D1018 + D1047 + D1066 · `ザコ戦` 3 = D1020 + D1048 + D1068 · `ボス戦` 3 = D1021 + D1048 + D1069 ·
   `ゲームオーバー` 4 = D1019 + D1047 + D1067 + D981 (the shipped prose sense, `batch_005.tsv:22`
   segment 12) · `宿敵` 3 = D1026 + D1050 + D1074 · `魔族` 6 shipped in `tl/` plus D1029 + D1051 +
   D1077. **Not duplicated at integration.** ⚠️ **But the correction is written collectively BELOW the
   table and the six cells still read "`batch_022` D10xx"** — §4.3-compliant, and still able to mislead
   a reader of one cell in isolation (§63.6 item 9).
3. ⚠️ **`インターミッション` is 4 instances over 3 lines in `tl/`, not the 2 I stated.**
   ✅ **BOTH FIGURES ARE RIGHT AT THEIR OWN SCOPE, verified at PR #44's review**: the SOURCE is 3 unique
   lines / 4 occurrences (D978 ×2, D1005, D1053); the SHIPPED English `Ｉｎｔｅｒｍｉｓｓｉｏｎ` is **2 in
   `tl/`**, both at `batch_013.tsv:86`. `grep -c` counts lines, `str.count()` counts instances.
   **The convention has to be stated — the translator stated it, and that is the whole lesson.**
4. ⭐⭐ **NEW TOOL FINDING — A SECOND `tokenise_stream` ARTIFACT, ON A DIFFERENT BRANCH FROM §R4's.**
   D1003 carries `{FFF3}{=00}{FF00}{=14}` where its seven siblings carry `{FFF3}{=00}{=B4}{=00}{=12}`.
   **`{FF00}` is not a real tag.** `tools/riotscript.py:55–90 tokenise_stream` has **no argument-length
   table**, so after `{FFF3}` it re-enters the loop, meets `0xFF` in the `0xfb <= c <= 0xff` branch and
   emits `{FF00}` from an **argument byte**. ⚠️ **§R4's artifact came from the SJIS-lead branch; this
   one is the CONTROL-TAG branch — same missing table, second distinct symptom.** Census: **1 in
   `script_unique.txt`, 6 in `script_dump.txt`, 0 in the battle dump.** Round-trip verified: both
   forms emit `ff f3 00 ff 00 14`, so **zero shipping impact** — the token stream was copied verbatim.
   **Belongs in `FLAGS.md` beside §R4. Do NOT patch `riotscript.py` (CLAUDE.md §3).** This strengthens
   Blocked 0: the fix is one argument-length table serving **both** branches in **both** tools.
5. ⭐⭐ **THE TWIN-UNIT TRAP IS REAL AND MEASURED, AND I FORWARDED IT TO `batch_022` MID-FLIGHT.**
   `batch_021` D1005–D1034 and `batch_022` D1053–D1082 are the **same 30 readable strings**, differing
   only in the trailing `{FFF8}` argument — so **gate 6 pairs NOTHING** and a divergence would ship
   undetected. Two hard consequences for `batch_022`'s menu rows (which carry a `　` cursor gutter, so
   +1 column over `batch_021`'s): ~~**track 17 and track 20 land at exactly 24**~~ ⛔ **CORRECTED at
   PR #44's review, 2026-09-11 — ONLY TRACK 17 DOES. Track 20 is 22** (`Ｔａｌｋ　ｗｉｔｈ　ｃｏｍｒａｄｅｓ` = 18,
   `　２０：` + 18 = 22), which `batch_022` measured and was right about; re-measured on its branch, its
   D1048 runs `[23, 24, 23, 15]` — **one run at 24, not two rows at 24** — and **my figure was a
   RELAYED one, not a measurement** — and **track 23 `伝説の古代文明` is 30 columns and CANNOT FIT**,
   because a 4-option menu row cannot be split without breaking the option↔`{FFF6}` mapping; it must be
   abbreviated, and `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ` alone is 20 and fixed at §42.1 / §51.2.
   ✅ **THE 30-TITLE PAIRING IS DONE — PR #44's reviewer did it, 30/30 identical including the `ＮＮ：`
   prefix, and NOTHING MOVED**, so #46's own 30/30 diff still stands (§AY4). ✅ **The case-policy call is
   RULED: descriptive labels take SENTENCE CASE, title case only for named things and §9 seeds
   (§63.1 / §AY3).** #46 conforms; it does not re-decide. ⚠️ **What #46 still owes is its OWN
   abbreviated menu rows D1043–D1052, which PR #44 did not review.**
6. ⚠️ **`ｂｏｓｓ` now carries three disjoint senses** — `ボス戦`/`大ボス` (script banks 30–31), `おかしら`
   → `Ｂｏｓｓ` (§32.1, battle chunk 20 only), `親方` → `ｔｈｅ　ｂｏｓｓ` (§34.1, script bank 12 only).
   §25.3's co-occurrence test **passes**: no chunk and no bank holds two of the three.

### ⚠️ WAVE 12 — THREE COORDINATOR ERRORS, ALL MINE, ALL CAUGHT BY THE CORRECTIONS TRANSLATOR
**I "corrected" three inherited claims in my own dispatch and was WRONG ON ALL THREE. The inherited
claims were right and my corrections were the error.** Each verified by me after the translator
pushed back, with the command in the PR. **This is the same shape wave 11 recorded four times and
that I explicitly warned all four translators about — asserting one side of a comparison without
censusing the other properly. I then committed it while in the act of correcting someone else.**

1. ⭐⭐ **`ｒｅｂｅｌｌｉｏｎ` IS 9 COLUMNS, NOT 10 — I MISCOUNTED A STRING LENGTH.** So D897's row
   reaches **24, not 25**, which is legal, and **my "this needs a re-wrap" was false**. The translator
   shipped `ｒａｉｓｅｄ　ａ　ｒｅｂｅｌｌｉｏｎ　ｗａｓ` (**22**, +2 bytes, no `{FFFE}` moved), taking `ａ`
   from **already-merged `batch_015.tsv:40` (D786)**, which renders the identical Japanese
   `反乱を起こした` the same way. **That is better than either of my options** because it matches a
   shipped sibling instead of inventing a third wording. Measured: `ｒｅｖｏｌｔ` 6 · `ｒｅｂｅｌｌｉｏｎ` 9.
2. ⭐⭐ **MY `Ｈｅｙ，` GREP WAS CASE-SENSITIVE, SO I DECLARED `chunk_031` CLEAN WHEN IT IS THE DEFECT.**
   It carries **`Ｈ，　ｈｅｙ，` — lowercase** — which `grep 'Ｈｅｙ，'` cannot see. **The inherited
   citation naming `chunk_031` was RIGHT and my "correction" was the error.** Proper census
   (case-insensitive, word-boundary, excluding `ｔｈｅｙ`): **13 occurrences in 9 files**, of which
   **exactly 5 are defects, all battle**; the **8 non-defects all render `よう、`/`よっ、`/`よう！`**,
   `Ｈｅｙ，`'s legitimate owner — including `chunk_006`, which is §32.3's own cited instance. **The
   whole script store was clean.** ⚠️ **A case-sensitive gate 7 also fails to see the lowercase form.**
3. ⭐ **`batch_012.tsv:53` IS DATA 376 AND DOES CONTAIN `品` — I JUDGED A POOLED LINE FROM ITS HEAD.**
   DATA 376 is a **25-segment pooled multi-scene row**; the `品` sits in **segment 16**
   (`奴の　盗んだ品が` → `Ｔｈｅ　ｇｏｏｄｓ　ｈｅ　ｓｔｏｌｅ　ａｒｅ`). I read the mayor's greeting at the
   head, saw no `ｇｏｏｄｓ`, and wrote "the citation does not locate a real cell". **It does.**
   ⚠️ **NEW RULE: never judge a `script_unique` row from its head — check every `{FFFE}` segment.**
   §AP7's own prediction (21/20/14, +6 into bank 0) was confirmed exactly.

⭐ **NEW METHOD FINDING — A LINE CITATION GOES STALE THE MOMENT YOU EDIT THE FILE ABOVE IT.**
My `glossary.md:3883` citation was **correct when taken and wrong when read**: I then inserted the
**65-line §9.W12 seed at line 866**, shifting every later line by 65. **3,883 + 65 = 3,948**, exactly
where the translator found it. This is a third face of §AQ3's citation trap, and neither the 0-based
/1-based rule nor "check it against the file" catches it. **Rule: cite a line number only for a file
you are NOT about to edit, or re-derive every citation after editing — and prefer quoting the row's
text, which does not move.**

✅ **THE DISPATCH INSTRUCTION THAT SAVED THIS UNIT: "if a cell disagrees with what you measure,
YOUR MEASUREMENT WINS — put it in the PR body with the command you ran."** All three of my errors
came back with commands attached. **Keep that line in every dispatch.** The translator also reported
that **two of its own scripts were wrong before they were right** (`ｈｅｙ` matching inside `ｔｈｅｙ`;
a battle pairing off by one until the dump's trailing blank was dropped) — both would have produced
a confident wrong census. **Nobody in this run is exempt from this failure mode.**


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
