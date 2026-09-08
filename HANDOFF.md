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
> **WAVE 3 IS RUNNING** in `session_0126mzDCZDEoby12pU5qXegc`. Glossary seeded (`19a0391`),
> four units dispatched. The coordinator closes the wave and then opens wave 4's session.
>
> If this line still says "wave 3 is running" and no agent is alive (`ListAgents`) and no PR has
> moved for an hour, the chain broke: reconcile open PRs against **In flight**, re-dispatch what
> is lost, finish the wave, then open wave 4 with `create_session` (BOTH `source_url` and
> `source_revision` = `claude/workflow-translation-iterate-uzlkns`).

## Last updated
2026-09-08 · by: **wave-3 coordinator** (`session_0126mzDCZDEoby12pU5qXegc`) ·
wave: **3 dispatched, 4 units in flight** · queue: **fresh**

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

## In flight — WAVE 3 (4 units, dispatched 2026-09-08)
Barrier: **review nothing until all four have an open PR** (CLAUDE.md §4a).

| Unit | Branch | Round | PR | State |
|---|---|---|---|---|
| corrections/audit-wave1 (11 edits) | `tl/corrections-audit-wave1` | 1 | — | dispatched |
| battle chunk 8 (B 2.32) | `tl/battle-008` | 1 | — | dispatched |
| battle chunk 13 (C 3.41) | `tl/battle-013` | 1 | — | dispatched |
| battle chunk 17 (C 3.19) | `tl/battle-017` | 1 | — | dispatched |

**No script batch this wave.** Four units is CLAUDE.md §4 step 3's ceiling and the corrections
unit takes the fourth slot. A vetted script range for wave 4 is in **Next up**.

## Next up

**Wave 3's unit specs live in the dispatch messages and in `audits/`** — enough to re-dispatch any
unit from here:

- **corrections/audit-wave1** — apply the wave-1 audit's measured edits to already-shipped files.
  `audits/wave1-reading-review.md` §"table of 8" (**file** line numbers) + `audits/wave-1-audit.md`
  items 3–5 (**message** line numbers — the two docs number differently and mean the same lines),
  plus the §3 violation in that doc's §9. **Eleven** translated-line edits: `batch_004` L12/L17/
  L29/L42, `chunk_003` L6 (×2) and L17, `chunk_002` L15, `chunk_001` L2 and msg-L14, `chunk_034` L8.
  ⚠️ The audit's proposed `しかし` → `Ｂｕｔ` is **superseded** by §23.3 (`Ｂｕｔ` is でも's) → use
  `Ｈｏｗｅｖｅｒ，` and re-measure. ⚠️ `chunk_000.txt` (27 B slack) is **out of scope**.
- **battle chunks 8 / 13 / 17** — `python3 tools/queue.py battle` for figures; seeds in glossary §9.

**Wave 4 candidates**, in this order:
1. Any wave-3 unit that parked.
2. Battle chunks **15 (D 6.13), 18 (D 6.28), 19 (B 1.94)** — next in chapter order.
3. **One script batch — ALREADY VETTED by the wave-3 coordinator, take one of these:**

   | `queue.py script` batch | Lines | Banks | Verdict |
   |---|---|---|---|
   | **batch 1** — 318, 421–469 | 50 / 52 inst, 3,056 JP | 2, 3 | ✅ **CLEAN** — recruitment & shop dialogue |
   | **batch 2** — 319, 335, 599–646 | 50 / 53 inst, 1,332 JP | 12–15 | ✅ **CLEAN** — shop lines, roomy banks |
   | ~~batch 3~~ — 320, 1073–1121 | 50 / 52 inst | 31–34 | ⛔ **28 of 50 are DEBUG SCAFFOLDING** — a BGM sound-test menu (`５０：新曲１`, `１６：バトル（ザコ戦）`) and a flag-manipulation screen (`どのフラグを操作しますか？`). **Do not dispatch.** |
   | **batch 4** — 326–328, 470–516 | 50 / 53 inst, 1,638 JP | 4, 5, 7 | ✅ **CLEAN** — ノロ village + town descriptions. ⚠️ bank 5 has only 3,419 free |

   **Batch 2 is the pick** — cleanest, roomiest banks, lowest JP count.
   ⚠️ **Method note, or the vet silently passes everything:** `script_unique.txt` lines are
   `<instance count>\t<text>`, so the scaffolding regex `フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must be
   matched against the **text field**, not the raw line — anchored `^[０-９]{2}：` never fires on the
   raw line and batch 3 scores 18/50 instead of its true 28/50.

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
- 2026-09-08: script growth for planning is **2.10×** measured, not the skill's assumed 2.0×.
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not bank 40's own
  story text (~40 lines ≈ 840 instances vs ~25 of 195 lines ≈ 25 instances). Reversible.
- 2026-09-08: **wave 3 seeds the glossary BEFORE dispatch** (`19a0391`, 10 §9 rows). Wave 2's three
  round-1 CHANGES all came from the glossary moving under a draft mid-wave.

**Wave-2 rulings are no longer duplicated here** — they are written into their homes and that is
where they bind: `glossary.md` §23–§26 (`しかし`→`Ｈｏｗｅｖｅｒ，`, `クリミア` is a person, 将軍→General,
`様`≠さん, 弓使い→bowman), `FLAGS.md` §K–§N (§I1/§N2 quoted-token capitalisation, §J1's corrected
arithmetic), `findings.md` §24 (`{FC03}`), `translator.md` `06353c7` (the null gate-6 grep).

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
