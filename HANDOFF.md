## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` top banner). ⚠️ A fresh container clones SHALLOW and may carry a stale
local ref: if `git checkout main` lands on an old commit, `git fetch && git reset --hard origin/main`.

## NEXT ACTION — always current, always a literal instruction
> # ▶ THE SCOPED REPAIRS SESSION IS OPEN AND DISPATCHED (2026-09-12, `session_01UuuxzfFxNMkah4YTPHdq5T`)
> Not wave 15. It dispatches **no chunk and no batch** and **opens no successor session**. When the
> four repair units below are merged or parked, it closes with `check` green, `merge`, the README
> table, a `handoff: repairs closed` commit carrying the `origin/main` proof, restores this NEXT
> ACTION to "THE RUN IS STOPPED" below, and ends.
>
> **All six Blocked-6 divergences are DECIDED — re-derived Japanese-side, across every spelling,
> before anything was dispatched. Three need a repair; three are confirmed NON-defects.** The
> derivations are under "Decisions — repairs session" below. ⚠️ **Four units, not six: two
> divergences live in the same file as another repair, and three need no change at all.**
>
> | # | Item | §3 engaged? | Decision | Unit |
> |---|---|---|---|---|
> | 0 | `chunk_000` body[12] page 21 `.TTTT.` (FLAGS §BI2) | n/a | **RE-FLOW, 0 bytes** | `tl/battle/chunk_000.txt` |
> | 5 | `餌食` → `ｐｒｅｙ` (`chunk_000` body[2]) | no — lemma | **CONFORM IF IT FITS** (27 bytes slack) | same file as #0 |
> | 2 | `それよりも` (`chunk_018` body[4]) | no — lemma | **CONFORM** to `Ｍｏｒｅ　ｔｏ　ｔｈｅ　ｐｏｉｎｔ，` | `tl/battle/chunk_018.txt` |
> | 1 | `君、{FFFE}すまない。` (`batch_012:63`) | **YES** | **CONFORM** to `ｍｙ　ａｐｏｌｏｇｉｅｓ．` | `tl/script/batch_012.tsv` |
> | 6a | `静まり返っている・・・。` (`batch_013:31`) | **YES** | **CONFORM** to `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ．．．．` | `tl/script/batch_013.tsv` |
> | 3 | `納得がいく` | no | ⛔ **NO CHANGE** — §69.5/§BI4's split is justified; re-derived | — |
> | 4 | `この通り` | no | ⛔ **NO CHANGE** — conforming would WORSEN a §25.3 collapse | — |
> | 6b | `騒ぎ` (`batch_017:39`) | no | ⛔ **NO CHANGE** — confirms §BF4; 8 distinct source strings | — |
>
> # ⛔⛔ THE RUN IS STOPPED. THERE IS NO WAVE 15, AND NONE SHOULD BE OPENED.
> **Wave 14 closed with all three units merged. `CLAUDE.md` §8's FIRST stop condition — "no dispatchable
> unit left" — now holds, and it is the reason the chain ended.** This was not a failure, a stall, or a
> context limit: the coordinator ended the chain deliberately.
>
> **Nothing is dispatchable, and each reason is measured, not assumed:**
> - **Battle 40 / 44 merged.** Chunks **16 (1.59×)** and **32 (1.61×)** sit below §B2's measured
>   **1.64×** floor — no faithful translation fits 8,192 bytes. Chunks **5 (1.53×)** and **43 (1.23×)**
>   are translated and **parked**. All four need the **tier-A slot extension**, which is BUILT and
>   awaiting one human boot test (Blocked 2).
> - **Script unchanged: 0 feasible lines.** **363 of the 366 remaining unique lines and 2,748 of the
>   2,751 remaining instances — 99.9% — sit behind the §F2 bank-40/41 repoint** (Blocked 1).
> ⚠️ **`queue.py battle` still prints "dispatchable" for chunk 32** — its cutoff is hardcoded 1.6, not
> §B2's 1.64. **It is wrong. Do not dispatch 32 on its say-so.**
>
> **▶ THE WORK IS NOW THE HUMAN LIST BELOW, IN ORDER. Two emulator sessions unblock everything.**
> An agent session can still do useful work WITHOUT the human: the recorded repairs under Blocked 6.

## Wave-14 close proof (CLAUDE.md §4 step 6 — `origin/main` is AT the close commit)
Close commit **`4890aec`**. Run immediately after pushing it:
```
$ git rev-parse origin/main HEAD
4890aecd5a203f275d36640ed12aabe966d99a27
4890aecd5a203f275d36640ed12aabe966d99a27
$ git rev-list --count origin/main..HEAD
0
```
**One hash twice, count 0 — the wave is closed and `main` carries it.** Recorded as a follow-up commit
rather than an amend, because amending a pushed commit would mean force-pushing `main`; this is the
same shape wave 13 used (`handoff: final origin/main proof for the wave-13 close`).
⭐ **Someone who clones this repo and looks at `main` sees the whole run's progress.** That is the test
in the CLAUDE.md banner, and it passes.

## Progress (`python3 tools/assemble.py status`, run on the merged tree at this close)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **40** | 44 | wave 14 added 28, 29, 39; **16, 32 blocked**, **5, 43 parked** — all four on the tier-A floor |
| Battle JP characters | **34,439** | 43,137 | **79.8%** (was 75.2% at the wave's start) |
| Script unique lines | 1,064 | 1,430 | unchanged — 0 feasible lines this wave |
| Script message instances | 5,180 | 7,931 | 65.3% |

**40 merged + 2 blocked + 2 parked = 44. Nothing battle-side is left that is not blocked or parked.**
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE and which one it hides is NOT stable** — quote
the table, never that line.

## In flight — ✅ THE WAVE BARRIER IS MET: all four units have an open PR, base `main`
| Order | Unit | File | PR | Head | Cost | Review |
|---|---|---|---|---|---|---|
| 1 | R2 | `tl/battle/chunk_018.txt` | **#53** | `a881998` | +6 B → 3,041 / 8,192 (5,151) | **reviewer running** |
| 2 | R1 | `tl/script/batch_012.tsv` | **#55** | `a452e94` | +4 B, bank 1 → 26,187 free | queued |
| 3 | R6a | `tl/script/batch_013.tsv` | **#54** | `588de7c` | +10 B, bank 29 → 16,869 free | queued |
| 4 | R0+R5 | `tl/battle/chunk_000.txt` | **#56** | `f8308bb` | **−2 B → 8,163 / 8,192 (29 slack)** | queued **last** |

**Reviewed one at a time, in the foreground, in that order.** #56 is taken last deliberately: its
translator was still finishing its write-up when the barrier opened, and a reviewer must not read a
moving head. ⚠️ **`chunk_000`'s re-flow GAINED 2 bytes** (slack 27 → 29) rather than spending any —
the title reports the re-flow only, so **whether the conditional `餌食` → `ｐｒｅｙ` conformance was
taken or measured-and-declined is for the reviewer to establish from the PR, not assumed here.**

Bases: #53/#54 on `c583bd7`, #55/#56 on `1644ff0`; `main` has advanced only by `handoff:` commits
(`git diff --name-only c583bd7 origin/main` = `HANDOFF.md` alone), so **gate 2 holds for all four and
no rebase is owed** — each reviewer re-runs it against current `origin/main` regardless.
No tight bank is touched (40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607); only banks 1 and 29 move.
⚠️ **Every `tl/*` branch from waves 1–14 is MERGED but still on origin** — deletion returns **HTTP 403**
from the agent container (FLAGS §AQ9). **"Branch gone = merged" is an INVALID signal in this repo; use
the PR's `merged: true` and the squash SHA.**

### 📋 INTEGRATION DEBT THE REVIEWER MUST CARRY, collected from the four translators' reports
The translators cannot write `glossary.md` or `FLAGS.md` (CLAUDE.md §3); each of these is theirs to
integrate on `main` at the merge that raises it.
1. **`FLAGS §BF3` is DISCHARGED at #54's merge — and its citation list must be CORRECTED, not merely
   struck.** §BF3 names `batch_011:61`, `batch_014:13/16/18`, `batch_017:9/61` as sites of the
   byte-identical `静まり返っている・・・。`; **none of the five is** (three spellings, three different dot
   counts). PR #54's flag-2 table is the re-derived replacement.
2. **`glossary.md` §58 was the live row `batch_013:31` actually violated** — a **gate-7** divergence,
   not only a CLAUDE.md §3 one. §58 postdates `batch_013`/PR #36. §BF3 does not say this.
3. **§69.5's `それよりも` census is understated: 4 sites recorded, 12 rendered sites real** (7 `それよりも`
   + 5 bare `それより`, six Englishes). The **ruling is unaffected** and needs no §4.3 correction.
   Correct the census in place so it is not re-derived a sixth time.
4. **Two stale width figures for one 13-column string, §4.3 in-place, no rendering affected:**
   §39.3 item 3 says `ｍｙ　ａｐｏｌｏｇｉｅｓ．` is "14 columns either way"; §58.3's `すまんすまん。` cell
   says "**15**". `len()` = **13** (`ａｐｏｌｏｇｉｅｓ` is 9 letters).
5. **§70.7's `君、すまない。` bullet is struck as resolved** at #55's merge.
6. **Three `すま` sites no census had**, none a §3 case: FILE 815 `すまん、勘弁してくれ！`, and FILE 1360 /
   1377 (`お話中　すまないが、`, `リオン、すまん。`) — the last two **bank-41 blocked** behind the §F2
   repoint, recorded for whoever renders them then.
7. **Five `それより` sites no census had**, all motivated departures, none to be "repaired":
   `chunk_000` body[12], `chunk_003` body[15], `chunk_037` body[17], `batch_016:93`'s second instance,
   and **`pending/chunk_005` body[9]'s `Ｍｏｒｅ　ｕｒｇｅｎｔ，`** — a conformance the **tier-A unpark**
   owes alongside §BE4's retired wordings in that same parked file.

### ⭐⭐⭐ A THIRD NUMBERING CONVENTION, AND IT MADE *ME* FILE A FALSE CORRECTION
⛔ **`script_unique` citations are ambiguous in this repo and three agents used three readings of the
same line this session. Settle it before citing: `FILE = DATA + 5`** (the first data line is FILE 6;
`grep -n` prints FILE). **FILE 1360 = DATA 1355**, and it is **one pooled row carrying 14 `{FCC0}`
messages** — among them *both* `ねえ、それより{FFFE}指輪は・・・・？` *and* `お話中　すまないが、`, which is
why two units citing "1360" for different text were **both right**.
⚠️ **I retract the counter-correction I pushed at `1644ff0` against PR #53.** I claimed its
`script_unique` 1360 was wrong and that the run carried no `{FFFE}`. **PR #53 was right on both
counts** — 1360 is the FILE line (the same convention the project uses for `batch_NNN:k`), and the run
is `ねえ、それより{FFFE}指輪は・・・・？`, `{FFFE}` included. I had read my own tag-stripped display output
as if it were the raw string. **Nothing downstream depended on it**, but the false correction is the
exact failure §BI3 was written about, so it is struck here rather than left on the board.

### ⭐⭐ ALL THREE RETURNING TRANSLATORS CHECKED THE COORDINATOR'S FIGURES; TWO FOUND REAL ERRORS
**Byte figures held 3 / 3. Column and character counts did not: two of three dispatches carried
arithmetic slips of mine, both caught by the agent doing the work, neither changing a decision.**
1. **PR #53 — `それよりも` is 12 rendered sites, not 7: I censused ONE spelling.** 7 `それよりも` + 5 bare
   `それより`, six Englishes. Verified here. §69.5's census is understated the same way and the
   integrator should correct it in place. **The ruling stands** — `Ｍｏｒｅ　ｔｏ　ｔｈｅ　ｐｏｉｎｔ` is
   7 of 12 across four files; `chunk_018`'s `Ｍｏｒｅ　ｔｈａｎ　ｔｈａｔ` was a lone hapax. My byte and
   column figures for this unit (15 → 18 cols, +6 bytes) were confirmed exactly.
2. **PR #54 — `Ｉｎｓｉｄｅ` is 6 characters, not 7.** `batch_013:31` costs **+10 bytes at 16/17 columns**,
   not the +12 at 17/17 I dispatched; `bankmeasure` confirms independently (bank 29: 16,879 → 16,869).
3. **PR #55 — `ｍｙ　ａｐｏｌｏｇｉｅｓ．` is 13 columns.** `ａｐｏｌｏｇｉｅｓ` is 9 letters, not 10. My
   predicted page widths `1 / 14 / 22 / 22` are all wrong; measured **`8 / 13 / 21 / 19`** (row 1's `1`
   omits the 7-column name insert — ⚠️ note `rowcheck` substitutes `NAME_COST` for `{FC00}{=0000}`
   **only**, so it measures the script store's `{FFEC}{=00}{=00}` insert as **zero**). +4 bytes was right.
   ⚠️ **Two stale glossary figures for the same 13-column string, for the integrator as §4.3 in-place
   corrections, no rendering affected:** §39.3 item 3 says "14 columns either way"; §58.3's
   `すまんすまん。` cell says "**15**".
4. **PR #55 also found three `すま`-family sites my table omitted**, none of them a §3 case: FILE 815
   `すまん、勘弁してくれ！`, and FILE 1360 / 1377 (`お話中　すまないが、`, `リオン、すまん。`) which sit in
   the **blocked bank-41 block** and will need renderings after the §F2 repoint. **The exact run
   `君、{FFFE}すまない。` occurs exactly once per dump**, so the pair PR #55 repaired is the whole §3 case.

## Next up
⛔ **NOTHING. The dispatch queue is empty and will stay empty until a human unblocks it.** See NEXT ACTION.

## Remaining — 366 unique script lines / 2,751 instances, and the binding constraint for each
| Binding bank | Lines | Instances | Free | Note |
|---|---|---|---|---|
| **bank 40** | **330** | **2,715** | **75** | the item/armour description tables, ~21 instances per line |
| **bank 41** | **33** | **33** | **353** | unique 1355–1387, story text, bank 41 alone |
| bank 5 | **3** | 3 | 1,595 | D518/D519/D520 — the pooled rows |

⭐ **363 of 366 lines and 2,748 of 2,751 instances — 99.9% of everything left — sit behind ONE task:
the §F2 bank-40/41 repoint.** Everything else is rounding.
**Battle: 0 dispatchable.** 16 and 32 blocked on the tier-A floor; 5 and 43 parked.

## Blocked — needs a human, IN PRIORITY ORDER
### 1. ⭐⭐ THE BANK-40/41 REPOINT (§F2) — BY FAR THE BIGGEST LEVER LEFT, and it needs ONE input
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


### 2. Tier-A battle chunks 5, 16, 32, 43 — ENGINE BUILD 1 DONE, AWAITING THE BOOT TEST
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


### 3. Disc rebuild and play-test — ENGINE BUILD 1 delivered, boot test pending
The game files are on `main` as `riotstars.zip.001–003`; `python3 tools/unpack.py` rebuilds `original/`.
The full file set for the first boot test was built and handed to the human: `build/KOUSEI.EXE`,
`build/SLPS_008.29` (`python3 tools/engine.py build`, FLAGS §BC3), `build/HEXMAP.BIN`
(extended, `assemble.py build --extended`) and `build/SCRIPT.BIN`. Any session rebuilds them: `unpack.py`,
then `python3 tools/engine.py build`, then `python3 tools/assemble.py build --extended`.
**Left for the human: the disc rebuild (HEXMAP.BIN last in the image) and the boot test in Blocked 4.**
Still open from findings §11: the boot EXE's own half-width port (#11) and the 7-character name cap (#10).


### 4. 🎮 Two in-game visits that settle four open questions between them
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


### 5. Small, cheap, and each kills a standing false signal
Branch deletion returns **HTTP 403** from every agent container (§AQ9), so ~45 merged `tl/*` branches
linger and "branch still exists" has been a misleading signal for twelve waves.

- **🖥️ The main-script text box is NOT yet widened (MAIN1.EXE) — a standing note, not a blocker.**
  Translate to **24 columns anyway**; `riotfont.py rewrap` re-flows later if the box is widened. This has
  been true and harmless for twelve waves; it is recorded so nobody "discovers" it as a defect.

### 6. 📌 RECORDED REPAIRS — an agent can do these WITHOUT the human, disc, or emulator
Each is 0-byte or near-0-byte and none was in scope for the wave that found it.
- **`FLAGS.md` §BI2 — `tl/battle/chunk_000.txt` body[12] page 11 is the ONLY `.TTTT.` page in all of
  `tl/`** (0 attestations in 1,854 source pages), with its two neighbours having given up rows to it.
  **A 0-byte re-flow. ⚠️ Chunk 0's battle is test (1) of the Blocked-2 boot test — fix it BEFORE that
  test**, or the human tests a page shape the game never uses.
- **Six pre-existing `main`-level divergences**, none a defect in the unit that found it (`glossary.md`
  §70.7): `君、すまない。` (`batch_012:63` vs `chunk_024` body[14]) · `それよりも` (`chunk_018` vs
  chunks 22/37 and `batch_016`) · `納得がいく` (`chunk_021` vs chunk 29) · `この通り` (`batch_009:68`
  vs `batch_017:42`) · `餌食` (`chunk_000` body[2] vs `ｐｒｅｙ` elsewhere) · `batch_013:31` and
  `batch_017:39` (FLAGS §BF3/§BF4).
- **`FLAGS.md` §BE4 — `pending/chunk_005.txt` body[17] and body[27] carry RETIRED wordings** (§27.2's
  binding string; §32.3's ruling). **Harmless while parked, a CLAUDE.md §3 violation the moment chunk 5
  unparks.** Apply at the tier-A unpark with the re-measure. **Chunks 5 and 43 were written before ~30
  glossary entries existed: each owes a full gate-6 and gate-7 pass against the glossary AS IT STANDS
  ON THE DAY IT UNPARKS.**
- **`FLAGS.md` §BF5 — the §3.2 short-row-end preference is a PROJECT-WIDE SWEEP, not a per-unit
  finding** (8.7% mean across all shipped chunks). ⚠️ **Do not relitigate it per chunk.**
- **Glossary rows that must STAY LIVE** (all re-derived Japanese-side this wave): `飛行船` (chunk 16 +
  script 1307/1375/1376) · `新型` (chunk 16 ×4) · `４号`/`Ｕｎｉｔ　４` (chunks 32, 43 + 5 script lines) ·
  `敗れ去` (chunks 16, 32) · `巣窟` (523, 525) · `一巻の終わり` (1387) · bare `渓谷` (1292, 1381) ·
  §46.2 `大渓谷` (1313) · `永遠`, `甘すぎ`, `勝ち目`, `まあいい`, `残念`, `つまらない` · `根城`, `坊や`
  (chunk 32). ⭐ **Chunk 16 is a PARALLEL SCENE to chunk 39** — chunk 39 is its reference text for
  `新型(の)機械兵`, `敗れ去る`, `父さん・・・・` and `昔みたいに…飛行船の研究` the day it unblocks.

### 7. ⚠️ IF THE RUN EVER RESUMES — the session lineage cap killed the chain once
`FLAGS.md` **§Z / Blocked 0b (waves 9–10).** Waves ran as child sessions and the platform caps lineage
at **depth 8**; at the cap `send_later`, `create_trigger` and `create_session` all fail, so that wave ran
**without a watchdog and could not open its successor.** ✅ **Fixed by a human opening the next wave as a
fresh TOP-LEVEL session** (resets depth to 0). ⚠️ The in-run fallback — an `orchestrator` subagent — is
**degraded: subagents cannot spawn subagents, so it has no reviewer and self-reviews its own merges**
(wave 1, four merges). **Prefer the human action.** Waves 12–14 ran top-level and hit none of this.

### 8. ✅ RESOLVED EARLIER, kept as one line each so nobody re-opens them
- **`tokenise` argument-length table** — `FLAGS.md` §BB; `tools/tagargs.py`; both dumps re-generated and
  proven byte-for-byte against the real binaries; chunk 17 shipped.
- **`assemble.py:validate_body` charset whitelist** — `FLAGS.md` §BA; chunk 36 shipped, 2,887 / 8,192.
- **The `main` redirect** — waves 1–12 merged onto a feature branch while `main` sat untouched; `main`
  was fast-forwarded 2026-09-11 (284 commits, 54 units). **Every wave since has verified `origin/main`
  at its close commit.** Do not reintroduce a "Run configuration" block naming another branch.

## Decisions — repairs session (2026-09-12), every census re-derived Japanese-side
### ⭐⭐ THE SESSION'S FIRST FINDING: `FLAGS §BF3`'s CITATION LIST CONFLATES **FOUR SOURCE SPELLINGS**
§BF3 names six sites for `静まり返っている` (`batch_011:61`, `batch_014:13/16/18`, `batch_017:9/61`).
**Read at those exact rows, they are not one Japanese string but three spellings, one of them a typo
in the original game:**
| Spelling | Sites | English |
|---|---|---|
| `静まり返っている` (kanji 返) | `chunk_023` body[5] · `batch_013:31` · `batch_017:9` · `batch_017:61` | hushed ×3, **`ｑｕｉｔｅ　ｓｉｌｅｎｔ` ×1** |
| `静まりかえっている` (kana かえ) | `batch_011:61` | `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ` |
| `静まりかっている` (**kana か — the え is MISSING in the source**) | `batch_014:13` · `:16` · `:18` | `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ` ×3 |
⭐ **The byte-identical §3 pair is ONLY `chunk_023` body[5] ↔ `batch_013:31`** — both
`静まり返っている・・・。`, four dots. The other six are different strings and engage §3 not at all.
**7 of the family's 8 sites ship `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ`; `batch_013:31` alone ships `ｑｕｉｔｅ
ｓｉｌｅｎｔ`**, so it is the losing side on either test. ⚠️ **§BF3 was censused on the ENGLISH side —
the exact failure mode wave 14 named ten times (§BI3).** `batch_014:18`'s source even carries
`・・・。。` and correctly ships five stops, so the dot-count discipline is intact throughout.

### The three divergences that are NOT defects, each re-derived before it was let go
- **`納得がいく` — NO CHANGE, confirms §69.5/§BI4.** Exactly 2 sites, both battle, both shipped, 0
  script. `chunk_021` body[12] `納得がいく。` is a **bare predicate** → `ｉｔ　ｆｉｔｓ．`; `chunk_029`
  body[8] `やられたのも納得がいく。` takes an explicit **`〜のも` complement** → `ｎｏ　ｗｏｎｄｅｒ`.
  Strings differ, §3 not engaged, and *that Treize was beaten fits* is not English. §69.5's derivation
  holds exactly as written.
- **`騒ぎ` (`batch_017:39`) — NO CHANGE, confirms §BF4.** The `騒` family is **eight distinct source
  strings** — `騒ぎだす`, `この騒ぎ`, `騒がしい` ×2, `大騒ぎ`, `騒然` ×2, `騒ぎを巻き起こす`, `物騒`,
  `何の騒ぎ` — no two byte-identical. `ｓｔｉｒ　ｕｐ　ｕｐｒｏａｒ` would be poor English for the idiom.
- **`この通り` — NO CHANGE, and the divergence HANDOFF named points the WRONG WAY.** 13 sites across the
  demonstrative‐`とおり` family. The glossary binds `ご覧の/ごらんのとおり` → `Ａｓ　ｙｏｕ　ｓｅｅ`
  (§70.6, **EXHAUSTED**) and `あの/あのとおり` → `Ａｓ　ｙｏｕ　ｓａｗ` (§68.4/§69.4); **it binds
  `この通り` not at all.** `batch_009:68` (`この通り、村は…` → `Ａｓ　ｙｏｕ　ｓｅｅ，`) and
  `batch_017:42` (`俺は　この通り、生きてるぞ？` → `Ｉ’ｍ　ｒｉｇｈｔ　ｈｅｒｅ，`) are different strings
  with different deixis — the surroundings against the speaker's own body — in chapters that never meet,
  so §25.3 is met. ⛔ **Conforming `batch_017:42` to `Ａｓ　ｙｏｕ　ｓｅｅ，` would put a FOURTH source
  form under an English head already bound to an exhausted family — the §25.3 error in the direction
  that destroys a distinction.** ⚠️ The real open note is the reverse: **`batch_009:68` already shares
  `Ａｓ　ｙｏｕ　ｓｅｅ，` with the bound `ご覧のとおり` family.** Recorded, NOT fixed — that is glossary
  relitigation and out of this session's scope.

### Three more mis-citations found while re-deriving, none of them load-bearing for a decision
1. **The glossary's `すまんすまん。` cell cites "`batch_015`'s すまない → `Ｓｏｒｒｙ，`". There is no
   `すまない` in `batch_015` at all** — it is **`batch_014:46`**. The cell's *ruling* is unaffected.
2. **§69.5's `それよりも` census missed two script sites.** It names 4 (`chunk_018` vs 22/37/`batch_016`);
   the family is **7 sites and FOUR Englishes** — add `batch_012:55` (restructured to `ｉｎｓｔｅａｄ`,
   a legitimate §2 departure) and `batch_018:27` (`Ｎｅｖｅｒ　ｍｉｎｄ　ｔｈａｔ．`, dismissive rather than
   topic-shifting). **`chunk_018` is still the outlier the glossary names and still the repair**;
   the other two are recorded, not cut.
3. **§BI2's page indices (p8 / p10 / p11) come from a coarser splitter.** On `rowcheck.py:77`'s **five**
   delimiters they are **pages 17 / 20 / 21** of `chunk_000` body[12]. Same three pages, same defect —
   `TTTT`→`TTT`, `.TTTT`→`.TTT`, **`.TTT.`→`.TTTT.`**. Re-derived: **1,850 source pages, `.TTTT.` = 0**,
   and `.TTTT.` occurs **exactly once in all of `tl/battle`**, at that page. §BI2 is confirmed.

### ⚠️ A STRUCTURAL GATE GAP, recorded beside §BJ2's two
**`merge_script` never calls `tag_parity`** (`assemble.py:280`; the battle path calls it at line 228).
So the script store has **no tag-stream invariant at all** — which is why `batch_018:12`'s extra
`{FCC0}` (§70.7) passes `check` green. Battle files keep every tag but `{FFFE}` byte-identical and in
order; **`tl/script/*.tsv` keeps nothing.** Not a tool change (CLAUDE.md §3 forbids it mid-run):
recorded so script reviews pair pages by hand rather than trusting index alignment.

## Decisions — wave 14 (detail in `glossary.md` §68–§70 and `FLAGS.md` §BH–§BJ)
### ⭐⭐ THE WAVE'S ONE LESSON: A COUNT IS NOT EVIDENCE UNTIL IT IS RE-DERIVED
**TEN "exhausted / hapax" claims were made this wave. NOT ONE survived re-derivation** — three were
mine, seven came from agents, and one reached `main` and needed a §4.3 correction (§68.3 `つまらない`,
fixed at `0c5bf2b`: 3 battle instances, not a hapax). **Every single bad claim was censused on the
ENGLISH side, or over ONE SPELLING.** The corpus splits by **Japanese head** and by **kana/kanji
variant**, so a one-spelling English census cannot see what it is counting.
⭐ **The last unit broke the streak: all ten of PR #50's claims survived re-derivation** — the first
clean sweep, and it was done Japanese-side across both spellings.
**Rule, now proven eleven times over: re-derive every exhaustion claim on the Japanese side, across
both spellings, before striking a glossary row.** A wrongly struck row is invisible until a later unit
re-invents the word.

### ⭐⭐ TWO GATE BLIND SPOTS FOUND THIS WAVE — both recorded in `FLAGS.md` §BJ
1. **`rowcheck` structurally cannot see the trailing-blank defect** (`row_problems()` counts non-empty
   rows only), so a page carrying a spurious fifth segment PASSES. **The cheap detector is a line whose
   `{FFFE}` total went UP against the source — which `rowcheck` already prints.** §BJ2. ⚠️ The suggested
   `row_problems()` second pass is **recorded, not done**: CLAUDE.md §3 forbids touching the tools mid-run.
2. **A gate-6 parsing trap that silently voids half the gate:** `tl/script/*.tsv` rows are
   `<count>\t<JP>\t<EN>`, so **the key is COLUMN 2**. Splitting on the first tab takes the instance
   count as the key, **drops the entire script store, and still prints a clean result.** Correcting it
   took one reviewer's paired corpus from 1,714 runs to 3,754.

### ⭐ PROCESS THAT WORKED AND SHOULD CONTINUE
Every finding was **verified before it was relayed**, and it changed something almost every round: a
translator overturned nothing this wave but two had rulings go their way on evidence; **the coordinator
was wrong four times and each was caught by a subordinate** (the `工場` seed, two bad hapax labels, and
a page-shape census that used a one-delimiter splitter where `rowcheck.py:77` uses **five** — that last
one is withdrawn at `a309fee`). **Cross-unit constraints that no single review can see were routed
through `HANDOFF.md`, not through the coordinator's context** — the stolen-item box (11 instances) and
three kana/kanji twins were caught that way.
**Standing conventions:** PR bodies are **rewritten in full on every rework push** · never push while a
reviewer runs · take glossary/FLAGS section numbers by **READING at commit time** · pin the merge base
to an explicit SHA · battle `tl/` holds **no Japanese**, so pair the dump **positionally** · gate 6
pairs whole messages, so kana twins and sub-message forms are **structurally invisible** to it ·
GitHub **REFUSES `REQUEST_CHANGES`** here (§AQ1) — an absent REQUEST_CHANGES is never approval.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1–8 | battle 1–4, 6, 8, 9, 13, 17–22, 24–26, 30, 31, 36–38, 41, 42 + script 004–010 | 31 | 2 | battle 32/44 (64.3%); script 461 (57.4%) |
| 9–12 | script 011–022 (battle exhausted at the time) | 13 | 0 | battle 32/44; script **1,064 (65.3%)** |
| 13 | battle 15, 23, 27 | **3** | 0 | battle 37/44 (75.2%) — 3/3 merged, all at round 2 |
| **14** | **battle 28, 29, 39** | **3** | **0** | battle **40/44 (79.8%)** — 3/3 merged, 0 parked, 0 lost, 0 re-dispatches; **all three at round 2** |

**Wave 14 detail.** PRs #52 (chunk 28, 3,953/8,192), #51 (chunk 29, 3,403/8,192), #50 (chunk 39,
3,161/8,192). Realised growth 2.01×–2.14× against ceilings of 4.77×–6.21×. Every unit took exactly one
CHANGES round; **every finding was a conformance or geometry issue, never a mistranslation.** The
three-role split held throughout — **nothing is SELF-REVIEWED and there is no audit debt.**

## How to resume
1. `git fetch && git reset --hard origin/main`, then `python3 tools/assemble.py check` → All checks passed.
2. ⛔ **Do NOT run `/translate` and do NOT open a wave session. The queue is empty** (NEXT ACTION).
   `queue.py battle` will lie to you about chunk 32; §B2's floor is 1.64×, not the hardcoded 1.6.
3. **The work is the human list under "Blocked — needs a human", in order.** Blocked 1 and 2 between
   them unblock 100% of what is left, and both are waiting on an emulator, not on code.
4. **An agent CAN still do Blocked 6 without a human** — the recorded repairs, all of them 0-byte or
   near-0-byte, none requiring the disc.
5. **The game files are on `main`** as `riotstars.zip.001–003`; `python3 tools/unpack.py` rebuilds
   `original/` against pinned hashes. `refresh` reproduced `dumps/` byte-for-byte on 2026-09-11
   (FLAGS §BB4); if it ever does not, stop and look.
