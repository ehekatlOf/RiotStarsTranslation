**Last updated: 2026-09-12** — `integrate: chunk 000 repair` (PR #56 merged, squash `84e6b54`).
✅ **All four scoped repair units are merged, every one with no findings.** What remains is the
**session close only** (`check`, `merge` + `build/`, README table, restore NEXT ACTION, push the
`origin/main` proof). No unit is in flight; nothing is dispatchable.

## Integration branch: `main`. Not configurable.
Every PR bases on `main`; the reviewer merges into `main`; a wave is closed only when `origin/main` is
at the close commit (`CLAUDE.md` top banner). ⚠️ A fresh container clones SHALLOW and may carry a stale
local ref: if `git checkout main` lands on an old commit, `git fetch && git reset --hard origin/main`.


## NEXT ACTION — always current, always a literal instruction
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

>
> ✅ **The Blocked-6 repairs are DONE (2026-09-12).** One scoped session, four units, all merged with
> **no findings on any of them**. See "Repairs session" below. It opened no successor, by design.

## Repairs-session close (CLAUDE.md §4 step 6 — `origin/main` IS AT the close commit)
Close commit **`523818e`**. Run immediately after pushing it:
```
$ git rev-parse origin/main HEAD
523818e7596a0a5c25cbab57907d8890adceefb0
523818e7596a0a5c25cbab57907d8890adceefb0
$ git rev-list --count origin/main..HEAD
0
$ python3 tools/assemble.py check
All checks passed.
```
**One hash twice, count 0 — the session is closed and `main` carries it.** Recorded as a follow-up
commit rather than an amend, because amending a pushed commit would mean force-pushing `main`; this is
the same shape waves 13 and 14 used.
⭐ **Someone who clones this repo and looks at `main` sees the run's progress.** That is the test in the
CLAUDE.md banner, and it passes.
Four units, four PRs, four squash merges, four `integrate:main` commits, `check` green throughout:
| Unit | PR | Squash | Integration | Result |
|---|---|---|---|---|
| `tl/battle/chunk_000.txt` | #56 | `84e6b54` | `72e2a69` | **−2 B**: 8,165 → **8,163 / 8,192**, slack 27 → **29** |
| `tl/battle/chunk_018.txt` | #53 | `dac2ee4` | `8e2b454` | +6 B: **3,041 / 8,192**, slack 5,151 |
| `tl/script/batch_012.tsv` | #55 | `30d45aa` | `deef0ab` | +4 B, bank 1 → **26,187** free |
| `tl/script/batch_013.tsv` | #54 | `a82e742` | `a2853ad` | +10 B, bank 29 → **16,869** free |
**No tight bank was touched** — 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607, all unchanged.
⚠️ **Branch deletion returned HTTP 403 on all four** (§AQ9); the `fix/*` branches linger on origin and
that is **not** a merge signal — `merged: true` plus the squash SHA is.

## Progress — UNCHANGED by this session, which repaired shipped units rather than translating new ones
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


## In flight
**Nothing.** No open PR, no live agent, no worktree (`git worktree list` shows only the main checkout).

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


### 6. 📌 RECORDED REPAIRS — ✅ **THE NO-HUMAN ONES ARE DONE (2026-09-12).** What is left needs the unpark
**All six §70.7 divergences are decided and `FLAGS.md` §BI2 is DISCHARGED.** Three needed a repair;
**three were confirmed NON-defects and are closed with their derivations** — do not reopen them.
| Item | §3 engaged? | Outcome |
|---|---|---|
| `君、すまない。` `batch_012:63` | **yes** — byte-identical run | ✅ conformed to `chunk_024`'s `ｍｙ　ａｐｏｌｏｇｉｅｓ．` (#55) |
| `静まり返っている・・・。` `batch_013:31` | **yes** — byte-identical run | ✅ conformed to `chunk_023`'s `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ．．．．` (#54) |
| `それよりも` `chunk_018` | no — lemma | ✅ conformed to the glossary-bound `Ｍｏｒｅ　ｔｏ　ｔｈｅ　ｐｏｉｎｔ，` (#53) |
| `餌食` `chunk_000` body[2] p60 | no — lemma | ✅ conformed to `ｐｒｅｙ` (#56) — **and it was FREE**: §47.3's recorded "chunk 0 has 27 bytes of slack" reason was re-measured and **false** |
| `納得がいく` | no | ⛔ **NO CHANGE** — §69.5/§BI4's split is justified: `chunk_021`'s bare predicate vs `chunk_029`'s `〜のも` complement; *that Treize was beaten fits* is not English. 2 battle, 0 script, both shipped |
| `この通り` | no | ⛔ **NO CHANGE** — the glossary binds `ご覧のとおり`→`Ａｓ　ｙｏｕ　ｓｅｅ` (§70.6, **exhausted**) and `あの通り`→`Ａｓ　ｙｏｕ　ｓａｗ`, but binds `この通り` **not at all**. Conforming `batch_017:42` would put a FOURTH source form under an exhausted English head — the §25.3 error in the direction that destroys a distinction |
| `騒ぎ` `batch_017:39` | no | ⛔ **NO CHANGE** — confirms §BF4. The `騒` family is **eight distinct source strings**; `ｓｔｉｒ　ｕｐ　ｕｐｒｏａｒ` would be poor English for the idiom |

**Still open, and each needs the unpark or a human — an agent cannot clear them now:**
- ⚖️ **The seventh divergence is RULED: `あの世へ送ってやる。` — RECORDED, NOT RE-CUT** (`glossary.md`
  §74.4, ruled at #56's merge). ⚠️ **My framing of it was INVERTED and the board said so for an hour:**
  I called `chunk_000`'s `Ｉ’ｌｌ` the lone outlier against chunks 25 and 41. **§41.3 and §49 had already
  ruled it twice** — `chunk_000` is the **incumbent**, and Helfer (§11.6) and the castle warden (§49.5)
  *deliberately did not copy it* because neither takes contractions. The three **messages** differ, so
  gate 6 never engages. **The real defect is larger: Rimul ships FOUR contractions against §7 in chunk 0,
  and the whole-speaker fix measures +14 bytes, which does not fit.** Scoped at `FLAGS.md` §BN4 — not
  half-fixed.
- ⭐ **`.TT.` is a SECOND unattested page shape, still open** (`FLAGS.md` §BN): **0** of 1,850 pristine
  pages, **4** shipped — `chunk_000` body[9] p3 · `chunk_002` body[13] p9 · `chunk_008` body[9] p18 ·
  `chunk_030` body[4] p11. ⭐ Unlike `.TTTT.` all four are **SHRINKS** (source `.TTT.` → `.TT.`), so no
  four-row wall and no fit risk — §3.2's hazard is growth, not loss. **3 of the 4 are other units' files.**
- **`pending/chunk_005.txt` now owes THREE conformances at the tier-A unpark, not two.** §BE4's two
  (§27.2's binding string at body[17]; §32.3's `ねえ、`→`Ｓａｙ，` at body[27]) **plus body[9]'s
  `Ｍｏｒｅ　ｕｒｇｅｎｔ，` for `それより、`** (§BK5, found this session). **Chunks 5 and 43 each owe a
  full gate-6 and gate-7 pass against the glossary AS IT STANDS ON THE DAY IT UNPARKS.**
- **`FLAGS.md` §BF5 — the §3.2 short-row-end preference is a PROJECT-WIDE SWEEP, not a per-unit
  finding** (8.7% mean across all shipped chunks). ⚠️ **Do not relitigate it per chunk.**
- **Glossary rows that must STAY LIVE:** `飛行船` (chunk 16 + script 1307/1375/1376) · `新型` (chunk 16 ×4) ·
  `４号`/`Ｕｎｉｔ　４` (chunks 32, 43 + 5 script lines) · `敗れ去` (chunks 16, 32) · `巣窟` (523, 525) ·
  `一巻の終わり` (1387) · bare `渓谷` (1292, 1381) · §46.2 `大渓谷` (1313) · `永遠`, `甘すぎ`, `勝ち目`,
  `まあいい`, `残念`, `つまらない` · `根城`, `坊や` (chunk 32). ⭐ **Chunk 16 is a PARALLEL SCENE to chunk 39** —
  chunk 39 is its reference text for `新型(の)機械兵`, `敗れ去る`, `父さん・・・・` and
  `昔みたいに…飛行船の研究` the day it unblocks.
- **Bank-41 blocked, recorded for after the §F2 repoint:** `script_unique` FILE 1360 (`お話中　すまないが、`
  and `ねえ、それより{FFFE}指輪は・・・・？` — **one pooled row of 14 `{FCC0}` messages**) and FILE 1377
  (`リオン、すまん。`).

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


## Decisions — repairs session (2026-09-12). Detail: `glossary.md` §71–§74, `FLAGS.md` §BK–§BN
### ⭐⭐ THE SESSION'S LESSON: A CENSUS ON ONE SPELLING, OR ON THE ENGLISH SIDE, IS NOT A CENSUS
Wave 14 said it; this session proved it four more times, and **twice against the coordinator**:
- **`FLAGS §BF3`'s five citations conflate THREE SOURCE SPELLINGS** — `静まり返って` / `静まりかえって` /
  `静まりかって` (**the え is MISSING in the source — a typo in the original game**) — with dot counts 4,
  3, 1 and 5. **None of the five sites it names carries the byte-identical string it claims.** §BF3 was
  censused on the ENGLISH side. The real §3 pair was `chunk_023` body[5] ↔ `batch_013:31`, and 7 of the
  family's 8 sites already shipped `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ`. **Discharged at #54 with the citation list
  CORRECTED IN PLACE, not merely struck.**
- **I censused `それよりも` on one spelling and missed the bare `それより`.** The family is **13 instances /
  12 rendered / six Englishes**, not the 7 sites and 4 Englishes I dispatched. `glossary.md` §69.5 was
  understated the same way; corrected in place at #53. The **ruling was unaffected**.
### ⭐⭐ THE THREE-ROLE SPLIT EARNED ITS KEEP: EVERY SUBORDINATE CORRECTED THE COORDINATOR
**My byte figures held 4 / 4. My column arithmetic, citations and framing did not — six errors, every
one caught below me and none reaching a merged file:**
1. `Ｉｎｓｉｄｅ` is **6** characters, not 7 → `batch_013:31` is +10 B at 16/17 cols, not +12 at 17/17.
2. `ａｐｏｌｏｇｉｅｓ` is **9** letters, not 10 → `ｍｙ　ａｐｏｌｏｇｉｅｓ．` is **13** columns. ⚠️ `glossary.md`
   §39.3 item 3 ("14") and §58.3 ("15") were stale for the same string; both corrected in place at #55.
3. I claimed `rowcheck` measures the script name-insert as zero. **False** — `rowcheck.py:19`
   `SCRIPT_NAME = '{FFEC}{=00}{=00}'` and `_script_cols` substitute it, as does `assemble.py:134`.
   **Only battle mode is `{FC00}`-only** (§BL4).
4. I filed a **false correction** against PR #53's `script_unique` 1360 citation. It was right:
   **`FILE = DATA + 5`**, `grep -n` prints FILE, so FILE 1360 = DATA 1355 — and that line is **one pooled
   row of 14 messages** carrying both texts two units cited it for. Retracted at `eecd47e`.
5. My `餌食` page index (39) and §BI2's ("page 11") were both wrong: **`body[2]` p60** and **`body[12]`
   p21** on `rowcheck.py:77`'s five delimiters. **Three numberings were in circulation.**
6. **I inverted the seventh divergence**, calling the incumbent an outlier — see Blocked 6.
### ⭐ THREE GATE BLIND SPOTS RECORDED, beside §BJ2's two
- **`merge_script` applies NO `tag_parity`** (`assemble.py:280`; the battle path calls it at line 228).
  The script store has **no tag-stream invariant at all** — which is why `batch_018:12`'s stray `{FCC0}`
  passes `check` green. Script tag streams must be compared by hand (§BK2).
- **A positional-pairing script that pairs NOTHING prints "no duplicates" and passes.** Assert a non-zero
  pair count before believing a clean gate-6 result (§BK3). #54's reviewer positive-controlled its zero.
- **A `{FC50}`/`{FB00}`-scoped speaker audit MISATTRIBUTES borrowed channels**; a borrow is marked by
  `{FB01}` only (§BL3). #55's reviewer nearly filed a false register finding on it; #56's used it to
  settle the attribution that decided the seventh divergence.
⚠️ **`bankmeasure`'s `tightest:` line hid bank 2 on a real run this session** — quote the table, never
that line. **GitHub refuses `APPROVE` as well as `REQUEST_CHANGES` from this account** (§BK7): decisions
post as `COMMENT` reviews with `DECISION:` on line 1, so an absent approval and an absent rejection are
both non-signals.

## Decisions — wave 14
Collapsed at the repairs close. Detail lives in `glossary.md` §68–§70 and `FLAGS.md` §BH–§BJ. Its one
lesson — **re-derive every exhaustion claim Japanese-side across both spellings before striking a
glossary row** — is restated and reinforced above.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1–8 | battle 1–4, 6, 8, 9, 13, 17–22, 24–26, 30, 31, 36–38, 41, 42 + script 004–010 | 31 | 2 | battle 32/44 (64.3%); script 461 (57.4%) |
| 9–12 | script 011–022 (battle exhausted at the time) | 13 | 0 | battle 32/44; script **1,064 (65.3%)** |
| 13 | battle 15, 23, 27 | **3** | 0 | battle 37/44 (75.2%) — 3/3 merged, all at round 2 |
| **14** | **battle 28, 29, 39** | **3** | **0** | battle **40/44 (79.8%)** — 3/3 merged, 0 parked, 0 lost, 0 re-dispatches; **all three at round 2** |
| **repairs** | **chunk 000, chunk 018, batch 012, batch 013** (no new text) | **4** | **0** | unchanged — **4/4 merged, 0 findings on any, 0 parked, 0 lost, 0 rework rounds** |

**Wave 14 detail.** PRs #52, #51, #50. Every unit took exactly one CHANGES round; every finding was a
conformance or geometry issue, never a mistranslation. **Nothing is SELF-REVIEWED and there is no audit debt.**

**Repairs-session detail (2026-09-12).** PRs #53, #54, #55, #56 — **the run's only 4/4 clean sweep: every
unit merged at round 1 with no findings.** It added no Japanese and moved no progress figure; it made
identical Japanese byte-identical English at two sites, conformed two glossary rows, and cleared
`FLAGS.md` §BI2 before the boot test. **Net −2 bytes on chunk 0, the project's tightest file.** The
three-role split held throughout and earned its keep: **six coordinator errors were caught below the
coordinator and none reached a merged file** (Decisions above). Nothing is SELF-REVIEWED; no audit debt.


## How to resume
1. `git fetch && git reset --hard origin/main`, then `python3 tools/assemble.py check` → All checks passed.
2. ⛔ **Do NOT run `/translate` and do NOT open a wave session. The queue is empty** (NEXT ACTION).
   `queue.py battle` will lie to you about chunk 32; §B2's floor is **1.64×**, not the hardcoded 1.6.
3. **The work is the human list under "Blocked — needs a human", in order.** Blocked 1 and 2 between
   them unblock 100% of what is left, and both are waiting on an emulator, not on code.
4. ⛔ **Blocked 6's no-human repairs are DONE.** What remains there needs the tier-A unpark or a human.
   **Do not re-open the three NO-CHANGE divergences** — each is closed with a derivation.
5. **The game files are on `main`** as `riotstars.zip.001–003`; `python3 tools/unpack.py` rebuilds
   `original/` against pinned hashes. `refresh` reproduced `dumps/` byte-for-byte on 2026-09-11
   (FLAGS §BB4); if it ever does not, stop and look.
