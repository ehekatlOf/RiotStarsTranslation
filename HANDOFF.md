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
> **WAVE 3 IS CLOSED — 3 merged, 1 parked (translated, blocked on tooling). `check` green.**
> The next act is to **OPEN WAVE 4'S SESSION**, which wave 3's coordinator does in the same turn.
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 4",
>   tags:            ["riotstars-translation", "wave-4"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-4 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Units: **battle chunks 18, 19, 20 + script
> batch 2** — see **Next up**. ⚠️ **NOT chunk 15**: it carries the §D1 artifact (Blocked item 0)
> and would park exactly as chunk 17 did.
>
> If this line still says "open wave 4" and no wave-4 session exists, the chain broke: open it.

## Last updated
2026-09-08 · by: **wave-3 coordinator** (`session_0126mzDCZDEoby12pU5qXegc`) ·
wave: **3 CLOSED — 3 merged, 1 parked** · queue: **fresh**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **18** | 44 | 0, 1, 2, 3, 4, 6, 7, **8**, 9, 10, 11, 12, **13**, 14, 33, 34, 35, 40 |
| Battle JP characters | **13,914** | 43,161 | **32.2%** (was 26.3% at wave-3 start) |
| Script unique lines | 211 | 1,430 | `tl/script/batch_001–005.tsv` |
| Script message instances | 4,039 | 7,931 | **50.9%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353 free,
40 → 471, 5 → 3,381**, 2 → 7,505, 33 → 9,315. Bank 40 lost 38 bytes to PR #9's item-table edits.
Parked and translated: chunks **5, 43** (tier-A budget) and **17** (dump artifact).

## In flight
**Nothing. Wave 3 is closed.** Wave 4's session dispatches its own units.

## Next up — WAVE 4

**1. Battle chunks 18 (D 6.28), 19 (B 1.94), 20 (D 4.75)** — chapter order, all three artifact-free.
⚠️ **Chunk 19 inherits two rulings already made, at cost, in wave 3** — do not re-litigate them:
- It carries **both `了解` and `わかった`**, the co-occurrence §25.3 had no reserve for. `glossary.md`
  §29.4 fixed it: `了解` keeps `Ｕｎｄｅｒｓｔｏｏｄ`, a co-occurring `わかった` takes **`Ａｇｒｅｅｄ．`**.
- Its **three `指揮下` instances take `ｃｏｍｍａｎｄ`**, not `ｓｅｒｖｅ　ｕｎｄｅｒ` (§28) — two are
  already shipped that way in chunks 7 and 14.

**2. One script batch — batch 2, already vetted clean**: unique lines **319, 335, 599–646**
(50 lines / 53 instances, 1,332 JP chars, banks 12–15, all roomy). Shop and merchant dialogue.
The full vetting table is below; batch 3 is **28/50 debug scaffolding and must not be dispatched**.

**3. Seed the glossary BEFORE dispatching.** It moved **four times** during wave 3 (§27, §28, §29,
§30) and every reviewer had to weigh "translator error" against "a ruling that did not exist yet".

| `queue.py script` batch | Lines | Banks | Verdict |
|---|---|---|---|
| batch 1 — 318, 421–469 | 50 / 52 inst, 3,056 JP | 2, 3 | ✅ clean — recruitment & shop dialogue |
| **batch 2** — 319, 335, 599–646 | 50 / 53 inst, 1,332 JP | 12–15 | ✅ **clean, the pick** |
| ~~batch 3~~ — 320, 1073–1121 | 50 / 52 inst | 31–34 | ⛔ **28/50 DEBUG SCAFFOLDING** — BGM sound-test menu (`５０：新曲１`, `１６：バトル（ザコ戦）`) and a flag screen (`どのフラグを操作しますか？`). **Do not dispatch.** |
| batch 4 — 326–328, 470–516 | 50 / 53 inst, 1,638 JP | 4, 5, 7 | ✅ clean — ノロ village + towns. ⚠️ bank 5 has 3,381 free |

⚠️ **Vetting method, or the check silently passes everything:** `script_unique.txt` rows are
`<instance count>\t<text>`, so the scaffolding regex `フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must match
the **text field**. Against the raw line the anchored `^[０-９]{2}：` never fires and batch 3 scores
18/50 instead of its true 28/50 — a vet that looks like it passed.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **21 open chunks** after wave 3, but ⚠️ **6 of them carry the §D1 dump artifact (Blocked
item 0) and will park exactly as chunk 17 did — 15, 23, 27, 28, 29, 39.** Until a human fixes
`riotbattle.tokenise`, only **15 chunks are truly dispatchable**, in chapter order (tier, ratio):
18 (D 6.28), 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59), 24 (C 2.99), 25 (C 3.48),
26 (C 3.36), 30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 41 (E 6.54),
42 (D 5.46).

Script: 1,219 unique lines / ~3,892 instances untranslated. The item/equipment description table
(unique 127–330, 21 instances each) is the highest-yield pool but **bank 40 is down to 471 free** —
lines 185–225 stay parked until it is repointed. After that the 1-instance story text in the roomy
banks (518–1,413) is what remains dispatchable; `queue.py script` offers batches 1, 2 and 4 clean.

## Blocked — needs a human
0. 🔧 **THE `riotbattle.tokenise` DUMP ARTIFACT — new 2026-09-08 (PR #12), and it is now the
   highest-leverage item on this list.** `FLAGS.md` **§D1, §R**. The dumper prefers a Shift-JIS
   text run over a control tag whenever an argument byte happens to be a valid lead byte, so an
   item id plus the *next tag's* lead byte decodes as a kanji. **24 occurrences across 10 chunks**
   — `{FC70}` in 5, 16, 17, 23, 39 and `{FCA8}` in 15, 27, 28, 29, 32 — and every one of them makes
   `assemble.py check` unsatisfiable for that chunk: the dump form passes tag parity and fails
   charset, and every re-tokenised form does the reverse. **Chunk 17 is already finished, faithful,
   format-clean and 2,335 bytes UNDER its slot, and is parked for this reason alone.**
   Fix: teach `tokenise` the argument lengths of `{FC70}` and `{FCA8}` (or stop an argument byte
   from ever starting a text run), then `assemble.py refresh`. Chunk 17 then unparks with a
   `git mv` plus a **0-byte** re-tokenisation of one tail. ⚠️ **This needs no disc, no EXE and no
   emulator — unlike everything else on this list — and it unblocks ten chunks at once.**
   ⚠️ **Chunk 15 is on wave 4's list and carries it at message line 11**, so it will park the same
   way unless this is done first (`FLAGS.md` §R3).
1. **Tier A battle chunks 5, 16, 32, 43.** Measured budget ratios 1.53 / 1.59 / 1.61 / 1.23, all
   below the **1.64× floor measured in FLAGS §B2**; no faithful translation fits 8,192 bytes.
   5 and 43 are translated and parked in `pending/`. Fix: the engine patch in
   `pending/slot-extension.md` (KOUSEI.EXE, eleven patched words, relocate the 8 KB RAM script
   buffer) — needs the EXE, the disc image and an emulator. FLAGS §B3 recommends settling
   KOUSEI.EXE first and confirming the floor on **one** of 16 or 32, not both.
2. **Main-script bank capacity** (FLAGS §F2). Translating everything that remains needs
   +30,534 bytes in bank 41 (353 free), +20,924 in bank 40 (**471**), +14,720 in bank 5 (**3,381**),
   +12,798 in bank 2 (**7,505**) and +11,492 in bank 33 (**9,315**) — about **66 KB short**. Every
   other bank has room. 376 unique lines / 3,001 instances are therefore unshippable until a
   MAIN1.EXE repoint or bank-spill scheme exists.

   **The two worst cases are whole late chapters, and they are the clearest statement of the
   problem yet:** unique lines **1160–1354** (195 lines, 4,836 JP chars) are resident in **bank 40
   alone**, which has 471 bytes free and would need about 19,000; unique lines **1355–1387**
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
6. ~~**Chunk 5 dump artifact**~~ — **subsumed by item 0**, which is the same defect measured across all
   10 affected chunks. One fix closes both.

## Decisions this run
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured, not the skill's assumed 2.0×.
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not bank 40's own
  story text. Reversible; the arithmetic is not close.
- 2026-09-08: **seed the glossary BEFORE dispatching a wave.** Wave 3 did; its four round-1 CHANGES
  had unrelated causes, against wave 2's three from a moving glossary.
- 2026-09-08: **a parked unit gets the full reading review before it is parked** (PR #12). It ships
  *unchanged* after a `git mv` and nobody re-reads `pending/`, so defects found later are inherited.

**Rulings live in their homes, not here**: `glossary.md` §23–§30, `FLAGS.md` §K–§R,
`findings.md` §24, `pending/README.md`. Wave 3 added §27–§30 and §O–§R.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections/audit-wave1 + battle 8, 13, 17 | **3** | **1** | battle **18/44 (32.2%)**; script unchanged |

**Wave 3 detail.** Full three-role split; PRs #9–#12. `#9` corrections — 12 edits across 5 files,
round 1, **closing the live CLAUDE.md §3 violation**: `tl/battle/` now holds **0 divergent duplicate
renderings** (was 1). `#11` chunk 8 — 7,437 / 8,192, round 2. `#10` chunk 13 — 5,417 / 8,192,
round 1, zero blocking findings. `#12` chunk 17 — **PARKED**, translated and 2,335 bytes under its
slot, blocked solely by the §D1 dump artifact (Blocked item 0).
**The wave's pattern was findings being verified rather than obeyed, in both directions:** a
translator disproved a finding's premise before applying it (the mid-sentence break could not be
removed — 118 columns against a 92 ceiling); another improved on a proposed fix
(`Ｉ　ｍｉｓｒｅａｄ　ｔｈｅｍ．` over `ｕｎｄｅｒｅｓｔｉｍａｔｅｄ`, reserving that word for the three dump
lines that own it) and the reviewer withdrew its own proposal; a reviewer **demoted a binding ruling
it had been asked to ratify** (`指揮下に入る` occurs once, not six times); two reviewers withdrew
findings after measuring; and translators corrected three coordinator errors — a wrong line number,
a wrong column figure, and an over-warning generalised from another chunk's geometry.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
