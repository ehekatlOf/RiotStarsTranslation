## Run configuration — READ BEFORE BRANCHING
**The integration branch for this run is `claude/workflow-translation-iterate-uzlkns`, not
`main`.** The session that owns this run may only push there. It starts at the same commit as
`origin/main` (`dabdeae`), so the tree is identical. Everywhere `CLAUDE.md`, the `translate`
skill and the agent files say `main`, read `claude/workflow-translation-iterate-uzlkns`:

- translators: `git fetch origin claude/workflow-translation-iterate-uzlkns` and branch from it;
- PRs: `base = claude/workflow-translation-iterate-uzlkns`;
- reviewer: `git push origin integrate:claude/workflow-translation-iterate-uzlkns`.

The human fast-forwards `main` from this branch when the run is done. Nothing else changes.

## NEXT ACTION — always current, always a literal instruction
> **WAVE 2 IS CLOSED — 4 of 4 merged, 0 parked, `check` green. WAVE 3'S SESSION IS OPEN and is
> the active driver: `session_0126mzDCZDEoby12pU5qXegc`, "Riot Stars — wave 3", opened
> 2026-09-08 18:52Z via `create_session` on this branch.**
>
> **Wave 3 owns the repository now. Wave 2's session is done and stays out.**
>
> Wave 3's units: **the `corrections/audit-wave1` unit + battle chunks 8, 13, 17**, and optionally
> one script batch *after* grepping it for debug scaffolding — see **Next up** for per-line figures.
>
> **If wave 3's session is dead, stalled, or never started work** — check by listing open PRs
> against this branch and reading In flight — the chain is broken and whoever notices should
> re-open it exactly as above (SKILL.md §6a; `create_session` needs **both** `source_url` and
> `source_revision`). Do not run wave 3 from wave 2's session.
>
> When wave 3 closes it opens wave 4's session itself. The chain ends only on one of CLAUDE.md
> §8's four conditions.

## Last updated
2026-09-08 · by: **wave-2 coordinator** (`session_01JDoA8KzwUVk3ZjiBw8Qkf3`) ·
wave: **2 CLOSED, 4 of 4 merged, 0 parked** · queue: **fresh**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 16 | 44 | 0, 1, 2, 3, **4**, **6**, 7, **9**, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 11,351 | 43,161 | **26.3%** (was 20.1% at wave-2 start) |
| Script unique lines | 211 | 1,430 | `tl/script/batch_001–005.tsv` |
| Script message instances | 4,039 | 7,931 | **50.9%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353 free,
40 → 509, 5 → 3,419**, 2 → 7,543, 33 → 9,353. Bank 40 is spent (`FLAGS.md` §J2). Wave 2's units
touched banks 29/30/31 only, which remain roomy (25,589 / 35,119 / 34,827 free).

## In flight
**Nothing. Wave 2 is closed.** Wave 3's session dispatches its own units.

## Next up — WAVE 3

**1. `corrections/audit-wave1` — a translator + PR like any other unit.** Wave 1's independent
audit is explicit that these must **not** be applied by whoever ordered the audit. **Eight measured
edits**, every replacement row ≤ 23 columns:

| file / line | what | cost |
|---|---|---|
| `tl/script/batch_004.tsv:12` | `多くの兵士が愛用する一般的な剣。` drops 一般的な and promotes 多くの to "most" → `Ａ　ｃｏｍｍｏｎ　ｓｗｏｒｄ　ｍａｎｙ{FFFE}ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ．` **Both wave-1 audits proposed this same fix independently.** | +14 B/bank |
| `tl/battle/chunk_003.txt:5` | `しかし` → `Ｓｔｉｌｌ，` violates §23.3 (`Ｓｔｉｌｌ，` is それにしても's) | +4 B |
| `tl/battle/chunk_003.txt:5` | `“ｅｎｔｅｒ”` → `“ＥＮＴＥＲ”` — the settled §I1 / `FLAGS.md` §N2 rule. **Same line as the row above; do both in one pass.** | 0 B |
| `tl/battle/chunk_003.txt:16` | breaks split `Ｒｏｙａｌ`/`Ａｒｍｙ` and `ｓａｖｅｄ`/`ｕｓ．`; also `Ｅｖｅｒｙｏｎｅ　ｏｆ` → `ｉｎ` | 0 B |
| `tl/battle/chunk_002.txt:14` | `すみません。` → `Ｗｅ　ａｒｅ　ｓｏｒｒｙ．` reads as an apology for wrongdoing; it is apologetic *thanks* → `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` | +16 B |
| `tl/battle/chunk_001.txt:2` | break splits the compound "food store" | +2 B |
| `tl/battle/chunk_001.txt:14` | `助かった` active where §23.4 makes passive the default | 0 B |
| `tl/battle/chunk_034.txt:8` | **a live CLAUDE.md §3 violation**: `村が襲われました。` (13 dump instances) is `ｉｓ　ｕｎｄｅｒ　ａｔｔａｃｋ` in `chunk_007` L25/26 but `ｈａｓ　ｂｅｅｎ　ａｔｔａｃｋｅｄ` here. Fix **chunk 34** (6,601 slack), not chunk 7 (399). `chunk_006` L14 is a **different** source string (internal space) and stands. Both directions in `FLAGS.md` §M3. | −4 B |

⚠️ `chunk_000.txt` has **27 bytes of slack** — the tightest file in the project (`FLAGS.md` §G1).
Nothing above touches it; keep it that way.

**2. Battle chunks 8 (B 2.32), 13 (C 3.41), 17 (C 3.19)** — chapter order, from Remaining below.
Chunk 8 is tier B, so it needs a tight first draft and one re-cut pass (§0.2).

**3. One script batch**, chosen from the 1-instance story text in the roomy banks. ⚠️ **Grep the
candidate range for debug scaffolding before dispatching** — `フラグ|：新曲|^[０-９]{2}：|鑑賞モード`.
`queue.py` groups by bank and adjacency and cannot tell a sound-test menu from a scene; 89 of the
117 lines around wave 2's batch were exactly that.

**4. Three §9 seed candidates found while verifying other things**, none yet rendered:
`クロスリー` (8 battle occurrences), `ホアグ王子` → Prince `Ｈｏａｇ` (6+16), `トリフ` → `Ｔｏｒｉｆ` (9+6).

**Already done — do NOT re-queue:** `translator.md`'s gate-6 fix (`06353c7`), scratch-file
namespacing (`1195d28`), the §18.2 interjection correction (§24.4), `pending/README.md`'s re-cut
rows, and the **`queue.py` count check — discharged**: `queue.py` strips tags correctly and returns
1,980; the 1,770 figure came from wave 2's coordinator's own ad-hoc regex, not from the tool. No
ratio in Remaining is optimistic.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle, **24 dispatchable chunks** after wave 2 (`queue.py` reports 26 open — the other two are
tier-A 16 and 32, blocked below), in chapter order (tier, budget ratio):
8 (B 2.32), 13 (C 3.41), 15 (D 6.13), 17 (C 3.19), 18 (D 6.28), 19 (B 1.94), 20 (D 4.75),
21 (D 4.28), 22 (D 4.59), 23 (C 2.80), 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 27 (D 5.54),
28 (D 4.76), 29 (D 6.04), 30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37),
39 (D 6.20), 41 (E 6.54), 42 (D 5.46).

Script: 1,219 unique lines / ~4,606 instances untranslated. The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is spent at 509 free**
— lines 185–225 stay parked until it is repointed. After that, the 1-instance story text in the
roomy banks (518–1,413, ~53,000 JP chars) is what remains dispatchable.

## Blocked — needs a human
1. **Tier A battle chunks 5, 16, 32, 43.** Measured budget ratios 1.53 / 1.59 / 1.61 / 1.23, all
   below the **1.64× floor measured in FLAGS §B2**; no faithful translation fits 8,192 bytes.
   5 and 43 are translated and parked in `pending/`. Fix: the engine patch in
   `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script
   buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends settling
   KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (FLAGS §F2). Translating everything that remains needs
   +30,534 bytes in bank 41 (353 free), +20,924 in bank 40 (1,771), +14,720 in bank 5 (4,681),
   +12,798 in bank 2 (8,805) and +11,492 in bank 33 (10,615) — about **66 KB short**. Every
   other bank has room. 376 unique lines / 3,001 instances are therefore unshippable until a
   MAIN1.EXE repoint or bank-spill scheme exists.

   **The two worst cases are whole late chapters, and they are the clearest statement of the
   problem yet:** unique lines **1160–1354** (195 lines, 4,836 JP chars) are resident in **bank 40
   alone**, which has 1,771 bytes free and would need about 19,000; unique lines **1355–1387**
   (33 lines, **14,607 JP chars**) are resident in **bank 41 alone**, which has 353 bytes free and
   would need about 29,000. Neither chapter can be shipped even partially in a way worth playing.

   **Policy this run, with the numbers that decide it:** bank 40's spendable budget goes to the
   21-instance item-description table (~40 lines ≈ 840 instances) rather than to bank 40's own
   story text (~25 of 195 lines ≈ 25 instances, leaving that chapter 90% Japanese). A complete,
   coherent table beats a tenth of a chapter. Reversible — it is a choice, not a fact — but the
   arithmetic is not close.
3. **Main-script box not yet widened** (MAIN1.EXE side). Translate to 24 columns anyway;
   `riotfont.py rewrap` re-flows later.
4. **In-game checks**: FLAGS §D2/§D3 (pages over 4 rows), §D4 (is line 1234 reachable), §F6
   (description window 3 or 4 rows), §C4 (`{FFEC}` variant widths), `findings.md` menus and
   name-entry first test.
   ⭐ **The highest-value one is now `FLAGS.md` §L2 / `findings.md` §24 — do this one first.**
   Eight lines in `battle_dump.txt` carry **no `{FC50}`/`{FC51}` at all** and still exceed four
   text rows: chunk 6 L9 (15 rows) and L21 (11, tags are only `{FFFE}`/`{FFFF}`), chunk 7 L23/L24
   (5 and 6, already shipped — this is §D3), chunk 30 L23 (8), **chunk 32 L31 (59)**, chunk 37 L14
   (8), chunk 42 L11 (16). A 59-row page cannot exist, so the prediction is that these are **pools
   of independently-selected strings**, with `{FC03}` (32 occurrences, battle-only, zero in the
   script dump) as the selector. **One visit to the chapter 5 church map and chapter 6 settles it,
   and settles §D3 with it.** If the prediction holds, `rowcheck`'s `> 4 rows` warning is
   meaningless on all eight and a translator may re-flow freely inside such a line — but must
   never merge two entries. If it fails, chunk 7 L24 is already broken in shipped work.
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. **Chunk 5 dump artifact** (FLAGS §D1): dumper fix plus re-dump; needs `original/`.

## Decisions this run
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured, not the 2.0× the skill assumed.
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not to bank 40's
  own story text (~40 lines ≈ 840 instances vs ~25 of 195 lines ≈ 25 instances). Reversible.
- 2026-09-08: **`しかし` → `Ｈｏｗｅｖｅｒ，`** (§23.3). `Ｂｕｔ` is `でも`'s and `Ｓｔｉｌｌ，` is
  それにしても's; two distinct connectives are not collapsed.
- 2026-09-08: **`クリミア` is a PERSON** (§2 → §1), on 5 battle / 64 script occurrences, none a
  place, plus a vocative and `クロスリーにいるクリミア博士`. Third correction of the `メルザリオ`
  kind, after `ファリーナ`. No shipped line re-cut.
- 2026-09-08: **`将軍` → `Ｇｅｎｅｒａｌ`**, §9 correction 2 discharged — `フェルナンド将軍` 17× vs
  `フェルナンド隊長` 2×, and all three shipped `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ` render `隊長`.
- 2026-09-08: **`FLAGS.md` §I1 settled** (§N2): quoted tokens naming a command, menu option, map
  label, item or skill the game **displays** are capitalised — verbatim where the source supplies
  Latin, capitalised where it supplies Japanese; descriptive quoted phrases stay lowercase. The
  tie-breaker is that chunk 3's source reads `「入る」` while script 987's reads `「ＥＮＴＥＲ」`.
- 2026-09-08: **`様` does not collapse into §21.2's `さん` rule** — `様` has its own pattern
  (§1/§14.1), so `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` and `バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ`.
- 2026-09-08: **`弓使い` → `ｂｏｗｍａｎ`**, not the §9 seed's `archer`, which 弓兵 already spends.
- 2026-09-08: **`FLAGS.md` §J1 corrected** — it falsely stated PR #4 did not flag the `持つ者に`
  departure (Flag 3 does), and its arithmetic was wrong: 32 B/entry not 42, so 192 not 252, bank 40
  landing at 317 free rather than negative. The accept decision survives; the record did not.
- 2026-09-08: **`{FB01}` is not a tutorial marker** (666 script / 148 battle occurrences; only 47
  of 342 opened lines carry `じゃ`). The §7 register row keys on the speech.
- 2026-09-08: **battle `tl/*.txt` hold zero Japanese**, so a translator grepping JP against `tl/`
  ran a null duplicate check. Fixed in `translator.md` (`06353c7`); the correct method is positional
  row-pairing. Nothing shipped was wrong — reviewers re-derive gate 6 independently.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines / 4,013 instances (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle **16/44 (26.3%)**; script **211 lines / 4,039 instances (50.9%)** |

**Wave 2 detail.** Four merged, none parked, none past round 2, run as a full three-role split
(translator / reviewer subagents) — the first wave with independent review.
`#6` chunk 4 — 3,849 / 8,192, slack 4,343, round 1, **zero findings**; the project's first
zero-re-flow unit (tag stream byte-identical on all 25 lines). `#7` chunk 6 — 5,899 / 8,192,
slack 2,293, round 2. `#5` chunk 9 — 3,973 / 8,192, slack 4,219, round 2. `#8` script batch 005 —
26 lines / 26 instances, 4,040 B into banks 29/30/31, round 2.
Glossary grew by four sections (§23–§26), `FLAGS.md` by four (§K, §L, §M, §N), `findings.md` by
one (§24, the `{FC03}` investigation). **Three of the four round-1 CHANGES were caused by the
glossary moving under a draft mid-wave** — a merged unit's integration commit adding rulings that
name a sibling unit's lines. Wave 3 should seed the glossary before dispatching, not after.
**Twice a translator overturned a reviewer's proposed replacement on evidence**, and both times the
reviewer withdrew its finding: chunk 6's `Ｎｏｗ，` over `Ｃｏｍｅ　ｏｎ，`, and chunk 9's three-row
`Ｈｏｗｅｖｅｒ，` split over a two-row form that ended a row on the article `ａ`.
An **independent post-merge audit of wave 1's four self-reviewed units** also ran this wave
(`audits/`): the units stand as merged, with eight minor edits queued above.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
