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
> **WAVE 6 IS RUNNING** in `session_013hHmA6EJT3rCC5wAiX6fwt`. Glossary seeded (`44333d8`);
> four translators dispatched. The coordinator reviews behind the wave barrier, closes the wave,
> then opens **wave 7's session** (`create_session`, BOTH `source_url` and `source_revision`).
>
> If this line still says "wave 6 is running" and no agent is alive (`ListAgents`) and no wave-6
> PRs are open, the chain broke here: re-dispatch the missing units, or open a replacement session.

## Last updated
2026-09-09 · by: **wave-6 reviewer, unit 1 of 4** (PR #24, battle chunk 24) ·
wave: **6 reviewing — 1 of 4 merged** · queue: **fresh; 8 §9 seed errors corrected in place**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **24** | 44 | 0–4, 6–14, 18–22, **24**, 33, 34, 35, 40 |
| Battle JP characters | **19,874** | 43,161 | **46.0%** |
| Script unique lines | **311** | 1,430 | `tl/script/batch_001–007.tsv` |
| Script message instances | **4,162** | 7,931 | **52.5%** |

`check`: **All checks passed** on the integration branch after PR #24's integration. Tightest banks:
**41 → 353, 40 → 447, 5 → 3,357, 2 → 3,365**, 33 → 9,291. Parked: chunks **5, 43** (tier-A budget)
and **17** (dump artifact). ⭐ **The dumper is still unfixed** — re-checked at wave-6 preflight with
`grep -n "FC70\|FCA8" tools/riotbattle.py`: no match. Chunk 17 stays parked.

## In flight — WAVE 6 (dispatched 2026-09-09)
| Unit | Branch / file | Budget | Round | State |
|---|---|---|---|---|
| battle chunk 24 | ~~`tl/battle-024`~~ → `tl/battle/chunk_024.txt` | 1,210 JP, headroom 4,819, ratio 2.99 (C) | 1 | ✅ **MERGED — PR #24, decision MERGE, squash `f1d1581`, integration commit `integrate: chunk 024 — glossary, flags, handoff`.** All 9 gates passed, every figure re-measured exact: **5,913 / 8,192 (2,279 slack)**, 2.0479× against a 2.9913× ceiling, 157 text rows (src 155), widest 23, **none at 24**, `{FFFE}` 132→134, `{FCC0}` 14→14. Gate 6 by the positional method over 28 files: **zero new divergences**. Glossary **§39**, FLAGS **§AA**. Nothing sent back — 6 PR figures corrected at merge (§39.3), no line changed |
| battle chunk 25 | `tl/battle-025` → `tl/battle/chunk_025.txt` | 1,039 JP, headroom 5,161, ratio 3.48 (C) | 1 | ✅ **PR #23 OPEN** — **5,419 / 8,192 (2,773 slack)**, 2.14× growth, widest row 23, +5 `{FFFE}`, `{FCC0}` untouched. Awaiting the barrier |
| battle chunk 26 | `tl/battle-026` → `tl/battle/chunk_026.txt` | 1,085 JP, headroom 5,115, ratio 3.36 (C) | 1 | ✅ **PR #22 OPEN** — **5,325 / 8,192 (2,867 slack)**, 1.84× growth, max run 23 cols, +3 `{FFFE}`. All six seed reach figures and widths re-measured **exact**. Awaiting the barrier |
| script batch 008 | `tl/script-008` → `tl/script/batch_008.tsv` | unique **470–516**, 47 lines / 47 instances, 1,577 JP | 1 | ✅ **PR #21 OPEN** — 47/47 shipped, 0 parked. bank 4 **→10,179**, bank 5 **→2,007**, banks 3/40 untouched; growth **1.86×** (leaner than the 2.10× model). Widest row 23 cols. Awaiting the barrier |

✅ **BARRIER MET 2026-09-09 — all four units have open PRs (#21, #22, #23, #24).** Reviewing
proceeds ONE reviewer at a time, in unit order: **~~24 (#24)~~ ✅ MERGED → 25 (#23) → 26 (#22) →
batch 008 (#21)**. Next reviewer: **PR #23, battle chunk 25.**

✅ **SETTLED at the PR #24 review — the faction widths.** Measured with `len()`: the **phrases**
`ｔｈｅ　Ｈｏａｇ　ｆａｃｔｉｏｎ` / `ｔｈｅ　Ｔｏｒｉｆ　ｆａｃｔｉｏｎ` are **16 / 17**; the PR's "20 / 18" are
the **shipped ROW widths** (`…　ｆａｃｔｉｏｎ　ａｎｄ` = 20, `…　ｆａｃｔｉｏｎ．` = 18), so the numbers
were right and the label was wrong. The page is 23 / 22 / 20 / 18. §9 now records 16 / 17, and the
long forms are confirmed **21 / 22**. See glossary §39.3 and FLAGS §AA9.

### ⚠️ WHAT THE PR #24 REVIEWER HANDS TO THE NEXT THREE — read before reviewing #23
1. ⚠️ **FLAGS.md's single letters are EXHAUSTED at §Z. The scheme is now DOUBLE LETTERS.** PR #24's
   review took **§AA**; take the next free double letter by **reading `FLAGS.md` at commit time**,
   never by reservation. Glossary is at **§39** after PR #24.
2. ⚠️ **`末えい` → `ｄｅｓｃｅｎｄａｎｔ` IS ALREADY SHIPPED** — `tl/battle/chunk_010.txt` 12.2 renders
   `誇リ高キ　龍人族ノ　マツエイダ。` as `Ｗｅ　ａｒｅ　ｄｅｓｃｅｎｄａｎｔｓ　ｏｆ　ｔｈｅ　ｐｒｏｕｄ　ｄｒａｇｏｎｆｏｌｋ．`
   The seed's **choice is confirmed by shipped work**; its "new form, 1 instance each" claim is
   wrong and §9 is patched. **This is a THIRD spelling class past §Y2** — full **katakana**, a
   register transform no kanji or kanji+kana search can find. Bears on PR #23 and PR #21.
3. ⚠️ **`そして、` diverges between chunks 24 and 25.** Chunk 24 ships `Ａｎｄ，`, matching shipped
   `pending/chunk_043.txt` 13.2; **PR #23 ships `Ａｎｄ　ｔｈｅｎ，`** (line 11, page 31). Chunk 24
   matches the earlier work, so **the change belongs to chunk 25**.
4. ⚠️ **`どけっ` is cross-unit and NOBODY listed it.** Chunk 24 9.7 `どけっ、` → `Ｍｏｖｅ！`; chunk 25
   11.58 `どけっ！` → `Ｏｕｔ　ｏｆ　ｍｙ　ｗａｙ！` with `どかないと` → `Ｍｏｖｅ，`. Different source
   strings so nothing is gate-bound, but it wants a ruling from #23's reviewer.
5. ⚠️ **"Verified free" is a MEASUREMENT.** Three of PR #24's were false (`ｂｌｏｗ`, `ｂｉｒｔｈ`, and
   the `ｐｌｏｔ` accounting). All survived §25.3 so no line changed, but check every such claim
   with one grep of `tl/` and `pending/` — this is §Y3's failure mode in its other direction.
6. **Two gate-6 traps, both of which silently produce a false clean pass** — `split_battle` returns
   a trailing blank separator line (strip it from the dump body too, or every file mismatches and
   the checker reports zero pairs), and `pending/chunk_043{,_abridged}.txt` are two translations of
   one dump chunk (exclude `_abridged`, or get 31 spurious divergences). FLAGS §AA2.
7. ✅ **`王位` and `恨み` §9 rows are LEFT LIVE** — chunk 24 was the FIRST of the pair to merge, and
   both agree with chunk 25. Per the `ルート` precedent (§29.1 / §30.1) **chunk 25's reviewer strikes
   them**, having verified the merged chunk 24 rather than assuming.
8. ❌ **Do NOT apply PR #23's Flag 15** — `len('ｄｅｓｃｅｎｄａｎｔ')` = **10**, not 11. The seed was
   right; the §9 row now carries the measurement so it is not "corrected" a third time.
9. ⚠️ **`FLAGS.md` §AA3 is left OPEN on purpose** — chunk 24's `・・ル・・・様・・・` →
   `．．ｌ．．．　ｍｙ　ｌｏｒｄ．．．` commits to a **male** patron and nothing in the corpus settles it.
   Chunk 25 makes Helfer the conspirator, which points at `Ｌｏｒｄ　Ｈｅｌｆｅｒ` but does not prove the
   referent. 4 columns either way, no re-flow. Re-check when a chunk names Fernando's backer.
10. ⚠️ **The two batch TSVs use DIFFERENT line conventions.** `batch_008.tsv` counts **DATA lines**
    (data rows only, `= FILE line − 5`); `batch_007.tsv` counts **FILE lines**. Read the header
    before citing a number. §9's wave-6 `batch_008` citations are now corrected to DATA 488 / 498 /
    515 — and the dispatch's gloss for the error ("exactly `unique − 470`") was itself wrong.

### ✅ Coordinator §9 errors — ALL APPLIED IN PLACE by the PR #24 reviewer in `integrate: chunk 024 — glossary, flags, handoff`
Eight in total: the three below, the `Ｔｒｉｆ` pair, the `ライトエルフ`/`オーラスマッシャー`
attribution, and `末えい`'s novelty claim. **Each was re-verified by the reviewer before applying**,
and each glossary row now carries the correction inline, dated, with the PR number, per §4.3.
**No rendering anywhere changed.** Full table at `FLAGS.md` §AA8. Kept below as the record of how.
1. ⚠️ **§9's wave-6 block cites LIST INDICES as unique line numbers for `batch_008`.** `古代文明` is
   at unique **488** (seed says 473), `魔族`/`末えい`/`司教様` at **498** (seed says 483), and
   `ウェストバリー` at **515** (seed says 505). ⚠️ **The figures are right but this gloss is wrong:**
   they are not "exactly `unique − 470`" (488−473=15, 498−483=15, 515−505=10, inconsistent). The real
   mapping is `batch_008.tsv`'s **declared DATA-line convention = FILE line − 5**; `batch_007.tsv`
   uses FILE lines instead, so **read the header before citing a number**. The
   block **contradicts itself** — its own FACT 1 correctly lists 483 as a *menu* line.
   Cause: the term-context script printed `enumerate()` indices while the duplicate-group and `あら`
   scripts used real unique numbers; only the former reached the seed. **The duplicate groups, the
   `あら` list (478/479/482/489/490/499/500) and the menu group (472/483/493/504) are all correct.**
2. ⚠️ **"~26 distinct translations" is wrong — it is 32.** 47 lines − 22 in groups + 7 groups = 32.
   Re-measured independently. The seven groups themselves are named correctly.
### ⚠️ PR #23 (chunk 25) caught a FOURTH coordinator error — `Ｔｒｉｆ` should be `Ｔｏｒｉｆ`
**CONFIRMED and relayed to chunk 24 mid-flight.** `glossary.md` §9's wave-6 block (line 520) renders
`トリフ王子派` as `Ｐｒｉｎｃｅ　Ｔｒｉｆ’ｓ　ｆａｃｔｉｏｎ`. **`トリフ` → `Ｔｏｒｉｆ` is FIXED** at
glossary line 290 and **promoted at §38.1**, and is **shipped** in `tl/script/batch_007.tsv` L56 as
`Ｐｒｉｎｃｅ　Ｔｏｒｉｆ`. `Ｔｒｉｆ` appears nowhere in `tl/` or `pending/`. A main-table entry beats a
provisional §9 row. **The reviewer must patch §9 line 520 in place** and check chunk 24's PR renders
`Ｔｏｒｉｆ` — chunks 24 and 25 share a scene and chunk 25 has shipped four `Ｔｏｒｉｆ`.
Correct form: `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ’ｓ　ｆａｃｔｉｏｎ`, **22 columns**.

### Other PR #23 findings — two confirmed, one REFUTED
- ✅ **CONFIRMED: `王位` and `恨み` are cross-unit with chunk 24 and my computed list missed both.**
  `王位` = chunks 24, 25 only; `恨み` = chunks 24, 25, 43. Cause: my intersection takes **maximal**
  kanji runs, so chunk 24's `王位継承` never matched chunk 25's `王位` — the same failure that hid
  `司教様` vs `司教`; and `恨み` is kanji+kana, the `末えい` class. Chunk 25 ships `ｔｈｅ　ｔｈｒｏｎｅ`
  and `ｇｒｕｄｇｅ` (the latter matching parked `chunk_043` L13). Relayed to chunk 24.
- ✅ **CONFIRMED: §9's `ライトエルフ` / `オーラスマッシャー` note misattributes them to Torif — they
  are ARIES's.** Traced through the `{FCB0}` portrait stream. **The renderings are unaffected**;
  only the note is wrong. Coherent with Aries being Bishop Creus's grandchild (chunk 24 L15).
- ❌ **REFUTED — do NOT "fix" this: `末えい` → `ｄｅｓｃｅｎｄａｎｔ` is 10 columns, not 11.**
  PR #23 Flag 15 says the seed's "10 columns" is wrong and should be 11. Measured
  `len('ｄｅｓｃｅｎｄａｎｔ')` = **10** (d-e-s-c-e-n-d-a-n-t). **The seed was right and Flag 15 is a
  hand-count one high** — the exact failure mode that PR warns about elsewhere. Nothing depends on
  it in either unit, but the reviewer must not propagate the correction into §9.
- Open for the reviewer to rule: `王子様` (vocative `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ` rendered; 8 script
  instances read referential, wanting `ｔｈｅ　Ｐｒｉｎｃｅ` on §1's `王女様` precedent) and `王家`
  (`ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ` proposed; parked `chunk_005` L27 has `ｔｈｅ　ｃｒｏｗｎ`, not gate-bound
  because chunk 5 is parked).

### Findings from PR #22 (chunk 26) the reviewer must carry forward
- ⚠️ **`大歓迎` has TWO shipped English forms — CONFIRMED by me.** `glossary.md` §38.2 fixes
  `Ｍｏｓｔ　ｗｅｌｃｏｍｅ`, but `tl/battle/chunk_007.txt` L5 already ships
  `Ｓｕｃｈ　ａ　ｗａｒｍ　ｗｅｌｃｏｍｅ` for chunk 7's instance, and §38.2 did not notice. The strings
  differ so gate 6 is not engaged and chunk 7 need not be re-cut — but **chunk 15 carries two more
  untranslated instances (dump lines 10 and 11)**, so a ruling is cheap NOW and expensive after
  chunk 15 is dispatched.
- **Seti is female, Yuiti is male**, established from the tag stream and sentence-final forms.
  Chunks 27, 29, 32 and 38 need those pronouns; **PR #22 is the file that fixes them.**
- **Treize is probably the L10/L11 dark elf** (same portrait 06 on `{FC51}`, same `{FCA7}{=0006}`
  scene tag, and Seti's L15 line presupposes his L11 defeat). Not proven — chunk 26 has no
  `{FB00}` portrait tag. If it holds, chunks 27/28/29 inherit a haughty, uncontracted Treize.
- `Ｃａｐｔａｉｎ` now renders both `船長` and `隊長`; §25.3's test is met on chunks but **not on
  banks** — banks 28 and 41 hold both. Nothing shipped is affected yet.
- ⚠️ **`魔族` and `末えい` §9 rows stay LIVE until the SECOND of each cross-unit pair merges.**
  Both PRs (#21 batch 008, #22 chunk 26) are now open and both render `魔族`. **Check which
  actually merged — never assume the order** (wave 5, `FLAGS.md` §Y2).

3. **`残念だけど` is NOT a byte-identity violation across the two units.** `Ｉ’ｍ　ａｆｒａｉｄ` is
   shipped in `chunk_011` L8 and `chunk_020` L49; batch 008 uses the uncontracted `Ｉ　ａｍ　ａｆｒａｉｄ`
   because its speaker is **Phyllis**, whose §14.6 row reads "Formal, warm, maternal, **no
   contractions**". CLAUDE.md §3 engages on the message, not the phrase, and these are three
   different messages. Verified and relayed to chunk 24's translator.

### ⚠️ Wave-6 seed errors, measured and corrected at preflight
The wave-5 handoff's script-batch arithmetic was wrong in three ways. The **unit is still sound**
and was dispatched unchanged; the *figures and the rationale* were not.
1. **Banks: 4 and 5 only — bank 3 is untouched.** The seed said "banks 3/4/5, bank 3 +448 → 7,665".
   Measured: **bank 4 +2,119 → 9,662; bank 5 +1,491 → 1,866**. The seed said bank 5 → 2,640, so the
   true post-batch figure is **774 bytes tighter than advertised** on an already-tight bank.
2. **The bank-40 exclusion named the wrong lines — off by five.** The seed said unique **326/327/328**
   are count-3 gossip lines with all instances in bank 40. They are not: they are count-**2** shop
   lines in banks **{4:2}, {5:1,7:1}, {5:1,7:1}** with **zero** bank-40 instances. The lines actually
   described (Batou the priest; Limrose's casino; the hobbit village) are unique **321, 322, 323** —
   count 3, all three instances in bank 40, **+852 against 447 free → −405**. ⚠️ **321/322/323 are the
   ones that must stay parked** until the bank-40 repoint. None of the six is in this wave's batch,
   so nothing was at risk, but the wrong three would have been un-parked next wave.
3. **The 21-instance item table is unique 127–313, not 127–330** (187 lines at count 21; 314–330 are
   count 2–10). Matters for the next wave's bank-40 budgeting.

## Next up — WAVE 7 (provisional; the wave-6 close fixes it)
Battle, chapter order: **30 (B 2.43), 31 (C 3.46), 36 (C 3.92)**. Script: the next `queue.py script`
position that is scaffolding-clean **and** bank-safe — ⚠️ **verify banks by INSTANCES before
dispatch** (see the corrections above); position 4 (329–332, 521–566) is clean of scaffolding but
puts ~3,351 JP chars into bank 5 and must not be taken, and position 2 (320, 1073–1121) is the debug
batch (28/50 scaffolding under the **unanchored** `[０-９]{2}：` on the text field) — never dispatch it.

### ⚠️ Briefing correction — the `{FCC0}` rule is right, its STATED CAUSE was wrong
I told all four translators and the PR #24 reviewer that `rowcheck.py:93-94` rejects `{FCC0}`
because it "exempts only `{FFFE}`". **That is false and I verified the correction myself:**
`rowcheck.py` **splits on `{FCC0}`** at lines **64, 77, 134 and 165** — it honours it as a page and
run boundary. What actually forbids adding or removing one is **`assemble.py:tag_parity`
(lines 117–126): "Every tag except `{FFFE}` must survive, in order."**
**The rule is unchanged — never add or remove `{FCC0}`, and it is never grounds for a finding
against a PR** (`translation_prompt.md` lines 248, 361, 373, 520 are a documentation defect for a
human). Only the mechanism was misstated. ⚠️ **If `FLAGS.md` §Q2 records the narrower/wrong cause,
the next reviewer should patch it in place** per the 2026-09-09 "patch, don't merely record"
decision. Future dispatches must cite `tag_parity`, not `rowcheck`.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **18 open chunks**, but ⚠️ **6 carry the §D1 dump artifact (Blocked item 0) and will park
exactly as chunk 17 did — 15, 23, 27, 28, 29, 39**; 16 and 32 are tier-A blocked. Dispatchable after
wave 6: **30, 31, 36, 37, 38, 41, 42** — about **two more waves**.

Script: **1,072 unique lines / 3,722 instances** untranslated after wave 6. ⚠️ **Banks 40 (447),
41 (353), 2 (3,365) and 5 (1,866 after this wave) are the binding constraint**, not the queue.
⚠️ **Chunk 37 (a later wave) inherits `FLAGS.md` §Y6:** Cress's gender is fixed nowhere in
`glossary.md` and rendered nowhere in `tl/`. A third-person line forces the pronoun.

## Blocked — needs a human
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
**Rulings live in their homes**: `glossary.md` §23–§39, `FLAGS.md` §K–§Z, `findings.md` §24,
`pending/README.md`. ⚠️ **Section numbers are taken by READING both files at commit time, never
reserved.** FLAGS has exhausted single letters — the next reviewer picks a scheme (§AA, or §Z7 on)
and says so.
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns`; `main` untouched.
- 2026-09-08: script growth for planning is **2.10×** measured (wave 4: 1.89×, wave 5: 2.09×).
- 2026-09-08: **bank 40's remaining budget goes to the 21-instance item table**, not its story text.
- 2026-09-08: **seed the glossary BEFORE dispatching**; **a parked unit still gets the full reading
  review**; **the `queue.py` batch POSITION is not the filename**.
- 2026-09-09: **a term is "in the glossary" only if a row FIXES AN ENGLISH FORM** — `grep -c` on the
  Japanese is not that test.
- 2026-09-09: **findings are proposals to verify in BOTH directions.** Wave 5: three translators and
  two reviewers corrected the coordinator; three units had PR figures corrected while still merging.
- 2026-09-09: **compute cross-unit terms MECHANICALLY** (`FLAGS.md` §Y2). ⚠️ **Extended at wave 6:**
  a kanji/katakana-run intersection **cannot see mixed kanji+kana terms** — it missed `つるん` in
  wave 5 and `末えい` in wave 6. **Mixed-script terms need their own pass.**
- 2026-09-09: **a "verified free" reach claim goes STALE when a sibling merges** (`FLAGS.md` §Y3).
  Re-verify against the tree at review time, not at drafting time.
- 2026-09-09: **patch a measured documentation error in place, don't merely record it.** Wave 6 did
  this to §2's `ウエストバリー` row (9 → **8** columns) in the seed commit.
- 2026-09-09: **verify a handed-down batch's arithmetic before dispatching it, even when the handoff
  says "already vetted — do not re-derive".** Not re-deriving the *unit* and not re-checking its
  *figures* are different things: wave 6's inherited figures were wrong on banks, on the excluded
  line numbers, and on the item table's extent. Re-verifying cost one script and caught all three.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections + battle 8, 13, 17 | **3** | **1** | battle 18/44 (32.2%); script unchanged |
| 4 | battle 18, 19, 20 + script 006 | **4** | 0 | battle 21/44 (39.4%); script 261 lines (51.6%) |
| 5 | `あら` corrections + battle 21, 22 + script 007 | **4** | 0 | battle **23/44 (43.2%)**; script **311 lines (52.5%)** |

**Wave 5 detail.** PRs #17–#20, full three-role split, **four separate reviewers, all four merged at
round 1, no rework** — no independence audit is owed. The corrections unit found a **fifth** `あら`
outlier its own ruling table had dropped (§32.4 named chunk 8 in its census sentence and omitted it
from its table). Chunk 21 and 22 agreed byte-for-byte on all **eight** shared terms. PR #19 accepted
the project's first possessive on the `{FC00}` insert on the evidence that 48 rows already bind a
character to it. Detail lives in `glossary.md` §35–§38 and `FLAGS.md` §W–§Z.

## How to resume
1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (a plain
   `checkout` lands on a stale ref — see Run configuration), then `python3 tools/assemble.py check`.
2. Read this file — **NEXT ACTION says literally what to do next**; `ListAgents`, then reconcile
   open PRs (`git ls-remote --heads origin 'tl/*'`; `list_pull_requests` returns oversized bodies).
3. The run is recursive: each wave's session opens the next wave's session before it ends. If NEXT
   ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only four
   reasons to stop are in CLAUDE.md §8.
