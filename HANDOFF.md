## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main`
is at the close commit (`CLAUDE.md` top banner). **This block used to redirect the run to
`claude/workflow-translation-iterate-uzlkns` and told every agent to read `main` as that branch —
twelve waves merged there while `main` sat untouched and a human was told nothing had been done.**
`main` was fast-forwarded to the branch tip on 2026-09-11 (284 commits, 54 translated units); the
old branch is kept identical to `main` as a mirror and has no authority.

⚠️ **A fresh container clones SHALLOW and may carry a STALE local ref of `main`.** If `git checkout
main` lands you on an old commit or `git pull --ff-only` aborts: `git fetch && git reset --hard
origin/main`, verify with `git log -1`.

## NEXT ACTION — always current, always a literal instruction
> # ▶ WAVE 13 IS CLOSED. OPENING THE WAVE-14 SESSION NOW (2026-09-12, ~02:00 UTC).
> **Wave 13: chunks 15, 23, 27 — 3 dispatched, 3 MERGED, 0 parked, 0 lost, 0 re-dispatches.**
> Battle **37 / 44, 75.2%** (was 34 / 44, 69.3%).
>
> **The wave-13 coordinator is opening wave 14 in this same turn** — `create_session`, title
> **"Riot Stars — wave 14"**, tags `riotstars-translation` + `wave-14`, `source_revision: main`,
> environment and model inherited. **Units: battle chunks 28, 29, 39** (figures in Next up).
> **If you are a coordinator reading this:** `list_sessions` — if a wave-14 session other than yours is
> alive, stop. The runner reconciles on its 15-minute watchdog and does not touch the repository while a
> wave is alive. Engine work (Blocked 2, 4, 6) belongs to the runner, not to waves.
>
> ⚠️ **WAVE 14 IS THE LAST DISPATCHABLE BATTLE WAVE.** After it the battle store is exhausted short of the
> tier-A slot extension (16, 32 blocked; 5, 43 parked) and the script is unchanged at **0 feasible lines,
> 363 of 366 behind the §F2 repoint** — so CLAUDE.md §8's stop condition holds again and the run's next
> move is the human list under "Blocked".
> ⚠️ **Wave 14 inherits two LIVE glossary rows:** `じゃあね、` binds **chunk 28 L18** and `１度` binds
> **chunk 29 L8**. Neither may be struck until those units ship.
> ⚠️ Battle chunks are chapter-ordered and voices accumulate — read the shipped neighbours the dispatch
> names. ⚠️ Battle `tl/` holds no Japanese; **gate 6 must pair the dump positionally**.
> ⚠️ **`queue.py battle` still lists chunk 32 as dispatchable — it is NOT** (§B2's floor is 1.64×; 32 is
> 1.61×, 16 is 1.59×). ⚠️ Start every unit from the pristine dump (CLAUDE.md §2), never from an old PR.

## Last updated
2026-09-12 · by: **the wave-13 coordinator (its own session), at wave close** · **WAVE 13 CLOSED: chunks
15, 23 and 27 all MERGED — 3/3, 0 parked, 0 lost, 0 re-dispatches.** `check` **All checks passed** on
`main`; `build/*_dump_merged.txt` regenerated and committed; README status table refreshed; **all
worktrees pruned** (`git worktree list` shows only the main checkout); **no open PR, no live agent.**
**glossary ends §67 · FLAGS ends §BG** — ⚠️ **always take the next number by READING both files at commit
time, never by reserving.** The three-role split held for all three units; **nothing is SELF-REVIEWED and
there is no audit debt.**

## Progress (`python3 tools/assemble.py status`, run on the merged tree at this close)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **37** | 44 | wave 13 added 15, 23, 27; **16, 32 blocked** on the tier-A floor, **5, 43 parked** |
| Battle JP characters | **32,437** | 43,137 | **75.2%** (was 69.3% at the wave's start) |
| Script unique lines | 1,064 | 1,430 | unchanged — no script batch was feasible this wave |
| Script message instances | 5,180 | 7,931 | 65.3% |

⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE and WHICH ONE IT HIDES IS NOT STABLE** — quote the
table, never that line.

## In flight
**Nothing. Wave 13 is closed and wave 14's session is being opened.** No open PR, no unmerged unit branch,
no live agent, no worktree.
⚠️ **Every `tl/*` branch from waves 1–13 is MERGED but still on origin** — deletion returns **HTTP 403**
from the agent container (**FLAGS §AQ9**), every wave. **"Branch gone = merged" is an INVALID signal in
this repo; use the PR's `merged: true` and the squash SHA in the committed record.**

## Next up — WAVE 14, the LAST dispatchable battle wave (`queue.py battle`, figures re-measured 2026-09-11)
| Wave | Chunk | Tier | JP chars | Headroom | Ratio | EN budget (chars) | Note |
|---|---|---|---|---|---|---|---|
| **14** | **28** | D | 770 | 5,807 | 4.77× | 3,673 | ⚠️ `じゃあね、` binds **L18** — the row is LIVE |
| **14** | **29** | D | 610 | 6,163 | 6.05× | 3,691 | ⚠️ `１度` binds **L8** — the row is LIVE |
| **14** | **39** | D | 622 | 6,479 | 6.21× | 3,861 | |

**Do not dispatch 16 (1.59×) or 32 (1.61×)** — both below §B2's measured 1.64× floor; `queue.py`'s cutoff
is hardcoded 1.6 and is wrong about 32. **No script batch: 0 feasible lines.** Start each unit from the
pristine dump (CLAUDE.md §2). **After wave 14 nothing battle-side remains that is not blocked or parked.**

## Remaining — 366 unique lines / 2,751 instances, and the binding constraint for every one
**Battle: 3 dispatchable** — **28, 29, 39** (wave 14). ~~15, 23, 27~~ are **merged** (`8a08027`,
`8a9aba8`, `f88434c`). **2 blocked** — 16 and 32, on the tier-A slot extension only (1.59× / 1.61×
against §B2's 1.64×). §D1 applies to nothing any more (§BB). ⚠️ **Chunk 32 holds the last instance
of four live glossary rows** (`根城`, `坊や`, and §25.2's neighbours) — see §BG4.
⚠️ `queue.py battle` prints "dispatchable 7" because its tier-A cutoff is hardcoded 1.6, not 1.64 — it
counts 32. Use this table, not that line.

**Script: 366 unique lines / 2,751 instances**, and I measured the binding bank for each:
| Binding bank | Lines | Instances | Free | Note |
|---|---|---|---|---|
| **bank 40** | **330** | **2,715** | **75** | the item/armour description tables, ~21 instances per line |
| **bank 41** | **33** | **33** | **353** | unique 1355–1387, story text, bank 41 alone |
| bank 5 | **3** | 3 | 1,595 | D518/D519/D520 — the pooled rows in NEXT ACTION's qualification |

⭐ **So 363 of 366 lines and 2,748 of 2,751 instances — 99.9% of what is left — sit behind the ONE
task at the top of the human list: the §F2 bank-40/41 repoint.** Everything else is rounding.

## Blocked — needs a human, IN PRIORITY ORDER
### 1. ✅ RESOLVED 2026-09-11 — the `tokenise` argument-length table; both dumps re-generated; chunk 17 shipped
`FLAGS.md` **§BB**. `tools/tagargs.py` (`FC70` 2 · `FCA8` 2 · `FFED` 2 · `FFF3` 4 — **measured at byte level;
§R4's "8" and §AP2's "4" were wrong**, §BB2) is imported by both tokenisers. Dumps re-generated without
the binaries from their own lossless bytes and proven (§BB4): 18 battle + 7 script lines changed, all
byte-identical, none in a shipped chunk; artifact signatures 24 → 0, `{FF00}` 6 → 0. **§AP2's "zero
shipping impact" was wrong — `batch_012` D367 rendered a stray `お`; fixed (§BB3).** Chunk 17: `git mv`,
5,857 / 8,192. **15, 23, 27, 28, 29, 39 dispatchable; 16, 32 on the tier-A floor only.**
✅ **Confirmed against the real binaries the same day: `refresh` reproduced `dumps/` byte-for-byte,
`verify` ROUND TRIP OK on both files, both unique lists identical, `build` + `checkedit` OK — 132,487 bytes
changed, all inside script slots** (§BB4).
### 2. ⭐⭐ THE BANK-40/41 REPOINT (§F2) — by far the biggest lever left
`FLAGS.md` **§F2**, figures refreshed **§Z6**. About **66 KB short**: bank 41 needs +30,534 with **353**
free, bank 40 +20,924 with **75**, bank 5 +14,720 with **1,595**, bank 2 +12,798 with **1,607**, bank 33
+11,492. **Unblocks 363 unique lines / 2,748 instances — 99.9% of everything still untranslated.**
**The MAIN1.EXE loader is TRACED (FLAGS §BD, 2026-09-11):** `load_bank` at 0x80037B00 reads 20 sectors
at `bank*20` into a 0xA000 buffer at 0x800D8068 that is followed with zero clearance by the event record
table; eleven constant references, all mechanical to relocate. Design: a per-bank (start, count) table in
the EXE, the loader tail rewritten in place (17 words, no stub), the buffer moved to a 72 KB free region.
**Blocked on ONE input: two DuckStation savestates from MAIN1 scenes (a town mid-dialogue, the overworld)
so `riotfont.py liveness` can prove the target region is unwritten** — the four static candidates are
exactly where pointer-addressed load buffers would live. **The tooling is DONE and simulated (FLAGS §BD5):**
`tools/banks.py`, `tools/bankext.py` (image +1 sector for the table, loader tail rewritten, buffer
relocated; all 44 banks simulate; revert byte-identical), `riotscript.py --layout`, `bankmeasure.py
--extended`, `assemble.py build --extended` (SCRIPT.BIN 1,900,544 bytes, every bank slice verified).
When the savestates land: `riotfont.py liveness original/MAIN1.EXE TOWN.sav OVERWORLD.sav` on
`0x800A8000` (+73,728), then `python3 tools/engine.py build --main1-buffer 0x800A8000` (or the region the
savestates clear), then the boot test: a town dialogue in a tight bank (any bank-41 scene).
**Policy this run:** bank 40's spendable budget goes to the 21-instance item table (~840 instances), not
its own story text (~25 instances). Reversible, but the arithmetic is not close.
⚠️ **THREE THINGS COME DUE THE MOMENT BANK 40/41 OPENS, and each is written down so nothing is lost:**
- **D1169 `音楽のＯＮ・ＯＦＦを切り替えます` contains `・`, which §3.1 FORBIDS** (§AY5/§AZ7). **No existing
  precedent covers it** — wave 12 ruled `・` → `，` only for *apposition* (§64/§AZ), which does **not**
  reach `ＯＮ・ＯＦＦ`. **First known case of illegal source punctuation inside still-blocked text.**
- **D1332 is readable-identical to the shipped D320** and **D1384 must take §37.1's script-store
  `ｒｅｂｅｌｌｉｏｎ`**, not the battle store's `ｒｅｖｏｌｔ`. Both differ from their shipped twins only in
  tag stream, **so gate 6 is blind to them** — reuse the shipped English byte-for-byte.
- **§42.5's forward-binding table still holds two live rows: `505` → D535 and `506` → D403.**

### 3. ✅ RESOLVED 2026-09-11 — `assemble.py:validate_body` charset whitelist; chunk 36 shipped
`FLAGS.md` **§BA**. `validate_body` now exempts a text run byte-identical to the source line's run —
preserved machine text — **unless it still holds two or more consecutive kana/kanji**, so an
untranslated line is still caught (tested both ways, §BA3). `git mv pending/chunk_036.txt
tl/battle/chunk_036.txt`; `check` green; **2,887 / 8,192**. Battle 33 / 44, 66.6%.

### 4. Tier-A battle chunks 5, 16, 32, 43 — ENGINE BUILD 1 DONE, AWAITING THE BOOT TEST (2026-09-11)
Ratios 1.53 / 1.59 / 1.61 / 1.23, all below the **1.64× floor** (§B2); no faithful translation fits
8,192 bytes. **5 and 43 are translated and parked.** The fix is built: `pending/slot-extension.md`
(revised — appended 16 KB slots, because every large map's data runs to +0x24F18 and the old in-chunk
plan would have overwritten it, FLAGS §BC1), `tools/slots.py` + `tools/slotext.py`, `--extended` on
`riotbattle.py`/`assemble.py`. `build/KOUSEI.EXE` (font hook + half-width + renderer + slot stub,
`simcheck` PASS, `slotext simulate` PASS on all 46 maps) and `build/HEXMAP.BIN` (8,105,984 bytes,
chunks 5 = 8,679 and 43 = 11,181 in their slots, `checkedit --extended` OK) were handed to the human.
**What the human does (slot-extension.md §5):** rebuild the disc with `TACTICS/HEXMAP.BIN` as the
LAST file (it grew 64 KB), boot: (1) first battle (chunk 0, tightest normal chunk) shows 24-column
English; (2) chunk 5's battle plays through; (3) chunk 43 if a late save exists; capture one battle
savestate and one name-entry savestate for `liveness`/`gridsim`. **Until (1)+(2) pass, `--extended`
stays opt-in, 5 and 43 stay in `pending/`, and 16/32 stay blocked.** After they pass: move 5 and 43 to
`tl/battle/`, make `--extended` the default, dispatch 16 and 32 with a 16,384-byte budget.
⚠️ **THE UNPARK IS NOT A `git mv` — chunk 5 carries armed glossary divergences.** `FLAGS.md` **§BE4**
(found at PR #47's duplicate gate): `pending/chunk_005.txt` body[17] still renders §27.2's binding
string as the **retired** `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ　ａｔｔａｃｋｅｄ．` against eight shipped
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．`, and body[27] renders `ねえ、あなたたち、` as
`Ｙｏｕ　ｔｈｅｒｅ，` against §32.3's `ねえ、` → `Ｓａｙ，` (recorded at §34.2). Both are invisible while the
chunk is parked and both become live the moment it is not. **+2 bytes on a unit parked for budget, so
they are applied at the unpark with the re-measure.** Chunks 5 and 43 were written before §27.2, §32.3
and thirty other entries existed: **each owes a full gate-6 and gate-7 pass against the glossary as it
stands on the day it unparks, not as it stood when it was written.**

### 5. 🎮 Two in-game visits that settle four open questions between them
- **The nine tutorial screens** (Blocked 8, §AO1–AO3). `batch_013.tsv` adds one `{FFFE}` to each of
  DATA 958–963, 968, 969, 970 because `assemble.py`'s column model does not split on `{FFFA}`/`{FFF7}`/
  `{FFF6}`. **Open the tavern tutor, walk lectures 1–6, look for a blank first row or a misaligned
  cursor gutter.** ✅ **Jump targets are NOT at risk** — `{FFF6}` arguments are **message indices within
  the bank**, not byte offsets (verified at review). **If it looks wrong the fix is one regex and zero
  bytes.**
- **The Formation screen** (§Z1 / Blocked 7) and **one shop visit** (§C4 / §Y1). `batch_007` ships three
  `『』` UI labels as instructions to find menus whose strings are **in neither dump**. ⚠️ **Wave 12
  established that §AQ5's `編成` "inconsistency" was a FALSE POSITIVE of its own gate and closed it —
  but that answers only the consistency question, NOT whether the labels match the screen. §Z1 stays
  open.** At the shop, enter the **longest legal 7-character name** and buy the longest-named item:
  `{=00}{=01}` price and `{=00}{=03}`/`{=00}{=04}` name inserts are **gate-blind** (12 rows in
  `batch_006`, 6 in `batch_007`, each **bounded** at insert+8), and **49 rows across 15 files** put a
  character straight after `{FC00}`.
- ⭐ **`FLAGS.md` §L2 / `findings.md` §24** — eight lines carry **no `{FC50}`/`{FC51}`** yet exceed four
  text rows, worst **chunk 32 L31 at 59 rows**. A 59-row page cannot exist, so the prediction is **pools
  of independently-selected strings** with `{FC03}` as selector. **One visit to the chapter 5 church map
  and chapter 6 settles it, and §D3 with it.** ⭐ **Wave 12 found direct corroboration in the script
  store: D518/D519/D520 are exactly such pooled rows** (1,184 / 745 / 850 JP chars, multi-scene, one
  opening with a ruler string).

### 6. Disc rebuild and play-test — ENGINE BUILD 1 delivered 2026-09-11, boot test pending
The game files are on `main` as `riotstars.zip.001–003`; `python3 tools/unpack.py` rebuilds `original/`.
The full file set for the first boot test was built and handed to the human: `build/KOUSEI.EXE`,
`build/SLPS_008.29` (`python3 tools/engine.py build`, FLAGS §BC3), `build/HEXMAP.BIN`
(extended, `assemble.py build --extended`) and `build/SCRIPT.BIN`. Any session rebuilds them: `unpack.py`,
then `python3 tools/engine.py build`, then `python3 tools/assemble.py build --extended`.
**Left for the human: the disc rebuild (HEXMAP.BIN last in the image) and the boot test in Blocked 4.**
Still open from findings §11: the boot EXE's own half-width port (#11) and the 7-character name cap (#10).

### 7. Enable "Automatically delete head branches" — kills a permanent false signal
Branch deletion returns **HTTP 403** from every agent container (§AQ9), so ~45 merged `tl/*` branches
linger and "branch still exists" has been a misleading signal for twelve waves.

### 7b. 🖥️ The main-script text box is NOT yet widened (MAIN1.EXE) — a standing note, not a blocker
Translate to **24 columns anyway**; `riotfont.py rewrap` re-flows later if the box is widened. This has
been true and harmless for twelve waves; it is recorded so nobody "discovers" it as a defect.

### 7c. ⚠️ If the run RESUMES, watch the session lineage cap — it killed the chain once
`FLAGS.md` **§Z/Blocked 0b (waves 9–10).** Every wave ran as a child session of the previous one and the
platform caps that at **lineage depth 8**. At the cap, `send_later`, `create_trigger` and `create_session`
all return `caller session is at lineage depth 8 (limit 8)`, so that wave ran **without a watchdog and
could not open its successor.** ✅ **Fixed by a human opening the next wave as a fresh TOP-LEVEL session**,
which resets depth to 0. ⚠️ **The in-run fallback — an `orchestrator` subagent — WORKS BUT IS DEGRADED:
subagents cannot spawn subagents, so such a coordinator has no reviewer and self-reviews its own merges
(wave 1's failure, four merges).** **Prefer the human action; it is strictly better and nearly free.**
**Wave 12 ran as a top-level session and hit none of this** — `Task`, `send_later` and `create_session`
all worked, and the three-role split held for all four units.

### 8. 📄 `SKILL.md` §3 edit (small)
Scratch-file namespacing must bind **every** role, not just translators — a **reviewer's** script was
overwritten mid-task in wave 4 and caught only because the output was visibly the wrong unit's data.
Add: every agent namespaces every scratch file, and no agent trusts a scratch script it did not write
in the same turn.

### 9. 📌 Wave-13 standing debts — recorded, verified, and NOT this wave's to fix
None blocks a dispatch; each arms itself at a specific later moment, so they are written here rather than
left in `FLAGS.md` alone.
- **FLAGS §BE4 — `pending/chunk_005.txt` body[17] carries the RETIRED wording of §27.2's binding string**
  (8 shipped instances use the current one) and body[27] predates §32.3's ruling. **Harmless while parked;
  a CLAUDE.md §3 violation the moment chunk 5 unparks.** Apply at the tier-A unpark with the re-measure
  (+2 bytes on a budget-parked unit). Found by chunk 15's duplicate gate reaching outside its own unit.
- **FLAGS §BF3 / §BF4 — two pre-existing script-store divergences:** `batch_013:31` renders a
  byte-identical Japanese line differently from four other rows plus chunk 23, and `batch_017:39` diverges
  from its incumbent. Neither was wave 13's to fix.
- **FLAGS §BF5 — the §3.2 short-row-end preference is a PROJECT-WIDE SWEEP, not a per-unit finding.**
  Measured corpus-wide: chunk 23 is 8.8% of non-final rows against an **8.7% mean across all 36 shipped
  chunks**, and §27.2's own binding form is one such row. ⚠️ **Do not relitigate it per chunk** — a
  wave-13 reviewer nearly raised 11 such rows as a finding and calibrating against the corpus stopped it.
- **Two glossary rows are LIVE into wave 14:** `じゃあね、` binds **chunk 28 L18**, `１度` binds **chunk 29
  L8**. `根城` and `坊や` stay live for **blocked chunk 32**. Do not strike any of them early.

## Decisions this run
### ⭐⭐ WAVE 13's LESSON — ONE FAILURE WITH TWO FACES, and it produced EVERY finding in the wave
**Detail lives in `glossary.md` §65–§67 and `FLAGS.md` §BE–§BG, not here.**
1. ⭐⭐ **A CENSUS OVER ONE SPELLING IS NOT A CENSUS, AND GATE 6 PAIRING WHOLE MESSAGES CANNOT SEE A
   SUB-MESSAGE FORM.** Every gate-7 finding in all three units was one of these two, and they are the
   same failure seen from two sides. **Five instances in one wave:** `ワケ`/`訳` and `ほう`/`方` (chunk
   15) · `間違い`/`まちがい` (chunk 27) · `そうね。` bare vs `そうね。機械兵を` — a **sub-message** match
   gate 6 cannot pair (chunk 27) · and **one of mine**: I "corrected" a reviewer's count of a shipped
   form to 3 when the true figure was **6 rows across 5 files**, because I searched `よろしく頼む` and
   missed `よろしく　頼む` **with a full-width space**. ⭐ **The chunk-27 translator then applied the
   lesson UNPROMPTED** — censusing a term it had only been asked to *declare*, it found
   `batch_015.tsv:67` shipping an identical frame with different English, and conformed all three of its
   own instances.
2. ⭐ **FLAGS §BE3 — "A WIDTH CLEARANCE IS NOT A WORD RULING."** §42.8 cleared a phrasing for chunk 15 on
   **width**, and that was read as settling the **vocabulary**. It cost a review round. The translator
   pushed back with a shipped compound (`batch_015.tsv:18`), the reviewer upheld it after reading the row
   itself, and `ｇｉａｎｔ　ｂａｔｔｅｒｙ` stands.
3. ⭐ **GATE-7 FACE (b) STRUCK AGAIN, AND IT WAS A CROSS-WAVE DEFECT:** §30.4 reserved a word and
   asserted it "verified unspent across `tl/`" in wave 3 — **while the counter-evidence sat in §24.6's
   own NOTE CELL**, from wave 2. Ruled and repaired in place as **§30.4.1** (the reserve narrows; the
   wave-2 shipped form stands). Found by a translator, ruled by a reviewer, and it would have broken the
   next unit to reach the term, not this one.
4. ⚠️ **THREE COORDINATOR ERRORS, ALL MINE, ALL CAUGHT BY SUBORDINATE AGENTS.** (a) I read the
   `砲台` → `ｂａｔｔｅｒｙ` row while seeding and then **omitted it from the chunk-15 dispatch while
   listing four other keyed forms** — a seed that names four and silently drops a fifth reads as
   exhaustive, and it cost that unit its first round. (b) The one-spelling census above. (c) I told
   reviewers **five** rows must stay live; the chunk-27 reviewer re-derived them and found **four** —
   my `そうね。` count was a *substring* match on an evidential, not the fixed form.
5. ✅ **QUALITY CONTROL RAN IN BOTH DIRECTIONS, EVERY ROUND.** A translator overturned a reviewer's
   word ruling on evidence (§BE3) · a translator asked for a ruling, **lost it, and accepted on the
   evidence** (§23.4/§26.8) · a translator **withdrew its own challenge to my seed in full** after
   re-measuring, having been right to challenge me on a different count · reviewers corrected five and
   four figures respectively · a reviewer **recorded a near-miss against itself** (it nearly raised a
   §3.2 finding and calibrated against the corpus first — every shipped chunk does the same thing at
   2.6–12.0% of rows). **No finding in this wave was accepted on report; every one was re-verified.**
6. **Process:** the PR body must be **rewritten on every rework push** — chunk 15's was left describing
   its pre-rework text and its reviewer integrated from a corrected record instead (§65.7 / §BE6).
   A reviewer that shows "running" may already have merged and be **mid-integration**: with two of the
   three units the squash landed ~2 minutes before the integration commit. **Never push while a reviewer
   runs.**

### Wave 12's lessons — collapsed; full text in `glossary.md` §61–§64 and `FLAGS.md` §AW–§AZ
**Gate 7 has three faces, all mandatory: (a) key cells · (b) NOTE cells · (c) forms shipped in `tl/` the
glossary never recorded at all** — face (c) defeats any glossary-side harvester, so gate 7 needs a `tl/`
column-2 pass. **Hand-measuring columns:** `assemble.py:106` splits runs on more than `{FFFE}`, so a
`{FFFE}`-only split can overstate columns. **Assume every reach figure is a raw substring count until
shown otherwise.** **Read every `{FFFE}` segment of a pooled row.** **Cite by section, not by line** —
a line citation goes stale the moment the file above it is edited.

**Standing (waves 4–13).** Integration branch is **`main`** — it was `claude/workflow-translation-iterate-uzlkns`
with `main` untouched until 2026-09-11, which hid the whole run; see the top of this file and `CLAUDE.md`. Script growth for planning **2.10×**; ⚠️ **realised across wave 12 was 1.66×–1.98×, so quote
the planning bound and the realised figure as TWO numbers, never one.** Seed the glossary **before**
dispatching. A **parked unit still gets the full reading review**. Name script batches by **DATA line
list**. A term is "in the glossary" only if a row **fixes an English form**. Section numbers are taken by
**READING both files at commit time**, never reserved. **Runtime name/unit inserts take singular *they***
(§58/§AT4). **Battle `tl/` holds NO Japanese, so grepping it is a null check** — pair the battle dump
positionally (⚠️ **I made this mistake myself in wave 12 while checking a battle citation**). **Gate 6
pairs whole messages on exact Japanese**, so a kana variant, a sub-message term or a sibling differing
only in a tag argument is **structurally invisible** — wave 12's twin units shared **30 readable strings**
differing only in a trailing `{FFF8}` argument and **gate 6 reported clean while seeing nothing.**
**`{FCC0}` is forbidden by `assemble.py:tag_parity`, not `rowcheck.py`** (§Q2). **No gate needs a working
tree**; **pin the merge base to an explicit SHA** and **never reuse an author's `merge-tree` result** —
by wave 12's last review the base had moved through three merges. **Never infer merge state from an
agent's status**: reviewers merge *and* push `integrate:` while still showing "running", and **branch
deletion returns HTTP 403** (§AQ9). A rejected non-fast-forward push is the **mid-integration signal**:
hold, re-fetch, re-apply, **never force**. **`build/*_dump_merged.txt` is committed at WAVE CLOSE only** —
pushing it mid-review risks colliding with a reviewer's integration push. **GitHub REFUSES
`REQUEST_CHANGES` in this repo** (§AQ1): reviewers post a COMMENT review with `DECISION:` on line 1, and
an absent REQUEST_CHANGES is **never** approval. **Settled conventions, never findings:** DATA vs FILE ·
0-based vs 1-based · the gutter census · §45.2's `.TTTT.` is BATTLE-scoped · **breaks vs segments** are
two conventions over identical data · gate-7 key counts vary with splitter and struck-row handling —
**state your corpus.**

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle 23/44 (43.2%); script 311 (52.5%) |
| 6 | battle 24, 25, 26 + script 008 | **4** | 0 | battle 26/44 (51.0%); script 358 (53.1%) |
| 7 | battle 30, 31, 36 + script 009 | **3** | **1** | battle 28/44 (56.5%); script 408 (53.7%) |
| 8 | battle 37, 38, 41, 42 + script 010 | **5** | 0 | battle **32/44 (64.3%)**; script 461 (57.4%) |
| 9 | script 011, 012, 013 (**script-only — battle exhausted**) | **3** | 0 | battle 32/44; script 640 (59.7%) |
| 10 | script 014, 015, 016 (DATA 707–869) | **3** | 0 | battle 32/44; script 803 (61.7%) |
| 11 | script 017, 018, 019 (DATA 1100–1159, 1388–1430, 465–879) | **3** | 0 | battle 32/44; script 948 (63.6%) |
| 12 | script 020, 021, 022 + corrections (DATA 318/320/326–345, 997–1034, 1043–1099) | **4** | **0** | battle 32/44 (64.3%); script **1,064 (65.3%)** — ⭐ **ALL FOUR MERGED AT ROUND 1; the run's feasible queue is now EMPTY** |
| **13** | **battle 15, 23, 27** (first battle wave since wave 8) | **3** | **0** | battle **37/44 (75.2%)**; script unchanged — ⭐ **3/3 merged, 0 parked, 0 lost, 0 re-dispatches; all three at ROUND 2** |

**Wave 12 detail.** PRs #43–#46, 4 merged / 0 parked, all at round 1. Detail in `glossary.md` §61–§64
and `FLAGS.md` §AW–§AZ.

**Wave 13 detail.** PRs #47 (chunk 15), #49 (chunk 23), #48 (chunk 27) — **3 merged / 0 parked / 0 lost /
0 re-dispatches**, every one at **round 2**: each took exactly one CHANGES round, and every finding in
all three was a **gate-7** miss, never a gate 1–6 failure. Realised growth **2.03×–2.21×** against
budgets of 2.80×–6.14×, so all three came in well under. Translators 27–53 min, reviewers 18–29 min,
five separate reviewers with the three-role split intact throughout — **no unit is SELF-REVIEWED and
there is no audit debt.** Detail lives in `glossary.md` §65–§67 and `FLAGS.md` §BE–§BG.

## How to resume
1. `git fetch && git reset --hard origin/main` (a plain `checkout` can land on a stale shallow ref — see
   the top of this file), then `python3 tools/assemble.py check`.
2. **Dispatchable work: THREE battle chunks — 28, 29, 39 (wave 14, in Next up).** Open the wave-14 session
   with the SKILL.md §6a seed on `main`, or run `/translate`. ⚠️ **Wave 14 is the LAST dispatchable battle
   wave**; after it, 16 and 32 are blocked on the tier-A slot extension, 5 and 43 are parked, and the
   script is unchanged at 0 feasible lines — **CLAUDE.md §8's stop condition holds again.**
3. **After wave 14 the work is the human list under "Blocked — needs a human", in this order:** the boot
   test of engine build 1 (4 and 6 — the files exist, only an emulator is missing), the §F2 bank-40/41
   repoint (2 — unlocks 363 script lines / 2,748 instances, 99.9% of what is left; the loader is traced
   and the tooling simulated, blocked on two savestates), the two in-game visits (5). **Engine work is
   done in the root session, not by wave agents.**
4. **The game files are on `main`.** `python3 tools/unpack.py` rebuilds `original/` from
   `riotstars.zip.001–003` (pinned hashes; fails loudly on a bad part). `refresh` reproduced `dumps/`
   byte-for-byte on 2026-09-11 (FLAGS §BB4); if it ever does not, stop and look. `assemble.py build`
   runs the real `checkedit` anywhere now; the disc rebuild and play-test are still the human's.
5. ⚠️ **Read Decisions → wave 13's lesson before translating or reviewing anything.** One failure with
   two faces — a census over one spelling is not a census, and gate 6 pairing whole messages cannot see a
   sub-message form — produced **every** gate-7 finding in wave 13, across all three units and one
   coordinator miscount.
