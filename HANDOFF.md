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
> **WAVE 4 IS RUNNING.** Coordinator: `session_013mqnLaJCts7hGduLSmsuak`. Glossary seeded
> (`e324d6c`, 15 rows in §9). Four units dispatched — see **In flight**.
>
> **If that session died mid-wave:** do NOT restart the wave. Run preflight, reconcile the open
> PR list against **In flight** below, re-dispatch only units with no PR and no live translator
> (`ListAgents` first — silence is not death), then review behind the barrier as usual.
>
> **When wave 4 closes**, its coordinator opens wave 5's session in the same turn:
>
> ```
> create_session(                                        # claude-code-remote MCP
>   title:           "Riot Stars — wave 5",
>   tags:            ["riotstars-translation", "wave-5"],
>   source_url:      "https://github.com/ehekatlOf/RiotStarsTranslation",   # BOTH are required
>   source_revision: "claude/workflow-translation-iterate-uzlkns",
>   prompt:          <the wave-5 seed, per SKILL.md §6a>
> )
> ```
> Omit `environment_id` and `model` so both inherit. Wave 5's units are in **Next up**.

## Last updated
2026-09-09 · by: **chunk-19 reviewer** (PR #16 round-2 integration, `session_013mqnLaJCts7hGduLSmsuak`) ·
wave: **4 IN FLIGHT — 3 of 4 merged (18, 19, 20); script 006 (PR #15) unreviewed, reviewer slot FREE**
· queue: **fresh**


## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **21** | 44 | 0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, **18**, **19**, **20**, 33, 34, 35, 40 |
| Battle JP characters | **17,002** | 43,161 | **39.4%** (was 32.2% at wave-4 start) |
| Script unique lines | 211 | 1,430 | `tl/script/batch_001–005.tsv` |
| Script message instances | 4,039 | 7,931 | **50.9%** |

`check`: **All checks passed** on the integration branch. Tightest banks: **41 → 353 free,
40 → 471, 5 → 3,381**, 2 → 7,505, 33 → 9,315. Bank 40 lost 38 bytes to PR #9's item-table edits.
Parked and translated: chunks **5, 43** (tier-A budget) and **17** (dump artifact).

## In flight — WAVE 4 (dispatched 2026-09-08)
✅ **BARRIER MET 4 of 4** (PRs #13, #14, #15, #16). Review is running, one reviewer at a time, in
unit order 18 → 19 → 20 → script. Base branch for every unit and PR is
`claude/workflow-translation-iterate-uzlkns`.
**Reviewer 1 DONE — chunk 18 MERGED. Reviewer 3 DONE — chunk 20 MERGED round 1 (`46b728a`).
Reviewer 2 DONE — chunk 19 MERGED at round 2 (`aecea69`), integrated.** **The reviewer slot is now
FREE and ONE unit remains: PR #15** (script batch 006, never reviewed) → its integration takes
**glossary §34 / `FLAGS.md` §V**, but **read the last heading at commit time; never reserve.**

⚠️ **PR #15's reviewer inherits three rulings made after that PR was drafted**, and must weigh each
difference as "translator error" against "a ruling that did not exist when the unit was drafted":
**(a)** `あら` → `Ｍｙ` + the source's own punctuation (§32.4), which binds it; **(b)** the narrowed
`まさか` of §33.6 — `Ｓｕｒｅｌｙ` covers only the incredulous use, **not** the `まさか…とは`
exclamative, and `Ｓｕｒｅｌｙ` is **not** free (it renders はずだ and きっと in three shipped rows);
**(c)** `宝石` → `ｇｅｍｓｔｏｎｅ` (§33.5). ⚠️ Also owed, and **not** PR #15's job: the `あら` re-cut
of `chunk_007` L19/L24, `chunk_011` L3 and `chunk_014` L3 (`FLAGS.md` §T1), and the live
`勲章`/`メダル` collision in banks 42–43 (§T2). Both belong to a §27-style corrections unit.

✅ **THE CROSS-UNIT RULE IS DISCHARGED (2026-09-09).** Chunk 20 merged first and left the §9 seed
rows live; chunk 19 merged second at `aecea69` and **struck eight of them** — the four cross-unit
rows (`アリエス`, `ヒューゴー`, `カバラ`, `火の水晶`) plus the four chunk-19-only seeds (`ソロン`,
`ノーマン`, `トレジャーハンター`, `傭兵団`), all promoted to §33.1. **Every one was used exactly as
seeded by both translators; not one was improved on unilaterally.** ✅ The seed's
`Ｆｉｒｅ　Ｃｒｙｓｔａｌ` contingency **never fired** — chunk 19's four rows measure 18/18/21/21 and it
shipped with 127 bytes spare, so the long `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` stands in both units.
⚠️ The fifth term `宝石` **had no §9 row to strike** (the seed missed it); it is ruled
`ｇｅｍｓｔｏｎｅ` at §33.5 and entered at §32.1 and §33.1. **Chunk 31 inherits it**, as do the three
still-untranslated script lines.

✅ **SECTION NUMBERS: chunk 20 took §32 / `FLAGS.md` §T; chunk 19 took §33 / §U** (verified against
the files at commit time, not reserved). **PR #15's integration takes §34 / §V — but read the last
heading immediately before writing; never reserve.** Wave 3 lost work to two reviewers both
holding §28, and wave 4 nearly repeated it.

| Unit | Branch | File | Budget | PR | Status |
|---|---|---|---|---|---|
| battle chunk 18 | `tl/battle-018` | `tl/battle/chunk_018.txt` | 611 JP, tier D (6.28) | **#13** | ✅ **MERGED round 1** (squash `45e89d8`), integrated by `integrate: chunk 018 — glossary, flags, handoff (PR #13)`. 3,035 / 8,192 (5,157 slack); 78 text rows (not the PR's 60), widest 23, none at 24. All §6 gates passed and pasted; **zero blocking findings**. Both judgement calls ruled in the PR's favour: `いや、わかった。` → `Ｎｏ．　Ｒｉｇｈｔ．` (glossary §31.4) and `シナリオ` → `ｓｃｒｉｐｔ` (§31.5). 14 rows + `まさか` → `Ｓｕｒｅｌｙ` integrated as **glossary §31**; **`FLAGS.md` §S**. Nothing left on this unit |
| battle chunk 19 | `tl/battle-019` | `tl/battle/chunk_019.txt` | 1,745 JP, tier B (**1.94 — tight**) | **#16** | ✅ **MERGED round 2** (squash `aecea69`), integrated by `integrate: chunk 019 — glossary, flags, handoff (PR #16)`. **8,065 / 8,192 (127 slack)** — the wave's tight unit, 1.91× against a 1.94 ceiling; 200 text rows, widest 23 with 14 at 23, none at 24, no page over 4 rows; `{FFFE}` net −9 on five lines, **`{FCC0}` untouched at 24**, non-break tag stream byte-identical on all 28 lines. Every §6 gate re-run from scratch in a real checkout at round 2 (not diffed) and pasted; gate 6 re-run against the **new** corpus including chunk 20. **All 4 round-1 findings accepted, none contested, and every one byte-neutral or byte-positive** — `ウルフ` → **`Ｕｌｆ`** (−2 B), the orphaned `Ｉ　ａｍ` row repacked (0 B), a row-final lone `ａ` + 5-column orphan removed (0 B), and a second undisclosed §2.1 step-6 reorder restored to source order (0 B). ⚠️ **The translator corrected the reviewer's own evidence on finding 1 and was right**: `ｗｏｌｆ` is shipped across **2 unique lines of `batch_003` = 42 message instances**, and L40's key contains the katakana `ウルフ` itself. 17 rows + 3 rulings + the `まさか` narrowing integrated as **glossary §33**; **`FLAGS.md` §U**. **Eight §9 wave-4 seed rows struck** — the cross-unit rule is discharged. Nothing left on this unit |
| battle chunk 20 | `tl/battle-020` | `tl/battle/chunk_020.txt` | 732 JP, tier D (4.75) | **#14** | ✅ **MERGED round 1** (squash `46b728a`), integrated by `integrate: chunk 020 — glossary, flags, handoff (PR #14)`. **4,265 / 8,192 (3,927 slack); 94 text rows, widest 23, none at 24**; three `{FFFE}` added on two lines, none deleted, **no `{FCC0}`**; all 48 other body lines byte-identical to the dump. All §6 gates run in a real checkout and pasted; **every figure in the PR was correct as stated** and **no finding required a change to the unit**. **All five open questions ruled** (see below). 24 rows integrated as **glossary §32**; **`FLAGS.md` §T**. ⚠️ **Two items of owed work left behind, both in `FLAGS.md` §T1/§T2** — the `あら` re-cut of chunks 7, 11, 14, and the live `勲章`/`メダル` collision in banks 42–43 |
| script batch pos. 2 | `tl/script-006` | **`tl/script/batch_006.tsv`** | 50 lines / 53 inst, 1,332 JP, banks 12–15 | **#15** | ✅ **PR open** — 1.89× growth, −2,480 bytes across banks 12–15, none negative; banks 41/40 untouched; 27 glossary rows |

⚠️ **The script unit is `queue.py` batch POSITION 2, written to `batch_006.tsv`** — `batch_002.tsv`
already exists and is merged. Do not let the position number become the filename.

⚠️ **A FIFTH CROSS-UNIT TERM, missed by the wave-4 seed and found by chunk 20's translator:
`宝石` / `宝`.** Re-counted in the dump and confirmed: c19 has 宝石 ×1 and 宝 ×4 (incl. 財宝 ×1),
c20 has 宝石 ×4 and 宝 ×7 (incl. お宝 ×2); c31 ×1 is untranslated. **Chunk 20 ships `宝石` →
`ｇｅｍｓｔｏｎｅｓ`, `宝`/`お宝` → `ｔｒｅａｓｕｒｅ`/`ｔｈｅ　ｔｒｅａｓｕｒｅ`**, rejecting lowercase
`ｊｅｗｅｌｓ` because §3 fixes ジュエル → `Ｊｅｗｅｌ` and ジェム → `Ｇｅｍ` and `Ｇｅｍ` already appears
**147×** across `tl/`. Relayed to chunk 19's translator mid-flight with the counts; chunk 19 is
tier B and holds the casting vote on width, and chunk 20 can be moved to match at no cost.

**Chunk 20's five open questions — ALL RULED at PR #14's review, 2026-09-09.** Detail in
`glossary.md` §32.4–§32.6 and `FLAGS.md` §T. **The unit changed on none of them.**
1. ✅ **`あら` takes `Ｍｙ` + the source's own punctuation (§32.4).** §28.3 upheld and extended;
   chunk 20's `Ｍｙ？` / `Ｍｙ．．．？` stand. Decided on the corpus, not the five sample points: the
   full census is **12 `あら` rows in the battle dump (chunks 7, 8, 11, 13, 14, 16, 20 ×2, 27, 29)
   + ~30 script** — larger than §28.3's "16". The same-speaker argument (portrait 02) is real but
   argues only for *one* form; **§24.4 settles which, because it already spent `Ｏｈ？` on おや
   outright across 29 occurrences**, so `chunk_014`'s `あら？` → `Ｏｈ？` is byte-identical to a
   different fixed source word. ⚠️ **§28.3's "the alternative `Ｏｈ　ｍｙ，` is also free" is FALSE
   and is struck** — `chunk_011` L3 ships it **for `あら、` itself**. ⚠️ **OWED: four rows in three
   shipped files must move (`chunk_007` L19 + L24, `chunk_011` L3, `chunk_014` L3), all
   width-neutral or −6 bytes — `FLAGS.md` §T1 carries the table.** Deliberately not done inside a
   battle-chunk merge with PR #15 open on the same question and chunk 19 in rework; it is a §27
   corrections-unit job. **This ruling binds PR #15 and chunk 19 from now.**
2. ✅ **`宝石` → `ｇｅｍｓｔｏｎｅ(ｓ)` conforms** to chunk 19's reviewer's ruling; `ｇｅｍｓｔｏｎｅ`
   verified free across `tl/`, `ｇｅｍ` only in `batch_003` (§4's lowercase brow-gem), `Ｇｅｍ` the
   pickup — no collision. `宝`/`お宝` → `ｔｒｅａｓｕｒｅ` free and held distinct.
3. ✅ **`Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` (15), the long form, stands.** Still reversible: if chunk 19
   (tier B) is forced to `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` (12), chunk 20 follows at −6 bytes on a standalone
   row with 3,927 bytes of slack. **Chunk 19's re-reviewer must check this.**
4. ✅ **`Ｂｏｓｓｓ！` stands; `Ｂｏｓｓ！！` rejected (§32.6).** Not on width — both are 6 — but on §5:
   the source has **one** `！` and carries the lengthening in the kana `ぁ`, so `Ｂｏｓｓ！！` would
   invent a mark the source lacks *and* discard the beat it has.
5. ⚠️ **`勲章`/`メダル` — the rendering stands, the discharge does NOT (§32.5, `FLAGS.md` §T2).**
   The PR and the §9 seed both said "**2 battle**"; it is **4 battle (20, 22) + 59 `script_dump` /
   39 `script_unique`**, and `勲章` is the plot item **`獅子の勲章`** — the King's decoration and
   Fernando's forged coup. §25.3's test as this project states it ("no chunk and **no bank**
   contains both") is **NOT met**: `メダル` is in banks 42–43 and `勲章` is in 42–43 among many.
   **0 messages hold both**, so nothing is unreadable and nothing is re-cut — but the collision is
   **live** for whoever takes banks 42–43. Reserve: **`ｔｏｋｅｎ`** (5 columns, free), moving the
   **racetrack** side under §4.3 with `batch_002.tsv` named.

⚠️ **Chunks 19 and 20 share four terms** (`火の水晶`, `アリエス`, `カバラ`, `ヒューゴー`). Both
translators were seeded with the same forms (`glossary.md` §9, wave-4 block); CLAUDE.md §3 requires
byte-identical English. The seed row is struck by the **second** of the two reviewers to merge.
⚠️ Chunk 18 rendered **none** of the fifteen wave-4 seeds (verified, all zero), so PR #13's merge
left every one of those rows live — the cross-unit rule is untouched by it.

### ⚠️ WHAT THE REMAINING REVIEWERS INHERIT FROM PRs #13 AND #14
Detail in `glossary.md` §31 (chunk 18) and **§32 (chunk 20)**, `FLAGS.md` §S and **§T**. Section
numbers were taken at commit time: **glossary now ends at §32, `FLAGS.md` at §T** — chunk 19's
round 2 takes **§33/§U** and PR #15 takes **§34/§V**, re-reading both files first.

**From PR #14 (chunk 20), binding on both remaining units:** `あら` → **`Ｍｙ`** + the source's own
punctuation (§32.4) — batch_006 already conforms; the `勲章`/`メダル` collision is **live in banks
42–43**, reserve `ｔｏｋｅｎ` on the racetrack side (§32.5); `何だ、` is **not** a fixed form (§32.8);
`ふふ` is not feminine-only and `ふふっ` joins it (§32.7); new fixed forms `Ｏｉ，` for おい、,
`Ｓａｙ，` for ねえ、, `Ｙｏｕ’ｒｅ　ｒｉｇｈｔ．` for そうだな (**7 battle + 10 script — chunk 19 has
one**), `Ｎｗｏｈ` for ぬおっ, `Ａｇｈ！` for ああっ！, `ｓｃａｒｐｅｒ` for ずらかる, `ｃｒｅｄｉｔ` for 手柄.
**Chunk 19 also owns the strike of the five §9 cross-unit rows** — chunk 20 merged first and left
them live.

- **Chunk 19 (PR #16) — three direct inheritances.** (a) It carries **`守備兵` four times** (msgs
  3, 6, 7, 19); §2 fixes *garrison* / *garrison men* and `chunk_000` ships it, and it must stay
  distinct from chunk 18's new bare 守備 → `ｔｈｅ　ｄｅｆｅｎｃｅ` (glossary §31.2). (b) It carries
  **`了解。` and `わかった。` together**, which is exactly the case §29.4 wrote the `Ａｇｒｅｅｄ．`
  reserve for — chunk 18 did **not** engage it (verified: 了解 0, わかった 1) so the two rulings
  must not blur. (c) **`まさか` → `Ｓｕｒｅｌｙ` is now a fixed row** (glossary §31.3); chunk 19
  carries it twice.
- **`ｐｌａｎ` is spent.** §19.2's 作戦 → `Ｔｈｅ　ｐｌａｎ？` is what ruled `シナリオ` → `ｓｃｒｉｐｔ`
  (§31.5). Do not spend it again.
- **batch_006 (PR #15) — the `おっと` ruling it raised now has its counts.** `Ｎｏｗ　ｔｈｅｎ`
  already serves **three** source strings: `さて、` (chunk 33 shipped, chunk 18), `それじゃ、`
  (chunk 3) and `おっと。` (chunk 7). ⚠️ **`それじゃ` and `おっと` DO co-occur — chunks 7 and 43** —
  so §25.3's test *fails* for that pair and the `おっと` ruling has to name a reserve, not just a
  form. `さて、` is safe (chunks 18/26/33, disjoint from both). `FLAGS.md` §S5.
- **Two traps for any positional duplicate check** (`FLAGS.md` §S6): `ええい、` → `Ｅｎｏｕｇｈ！`
  is **not** §5's punctuation mechanism — §14.5 fixes the `！` as part of the form and the source
  has `、` in all three instances, so "correcting" it to `Ｅｎｏｕｇｈ，` would break two shipped
  files. And chunk 18 renders `いや、` as **both** `Ｎｏ，` and `Ｎｏ．` inside one message; that is
  correct per glossary §31.4 and is not a divergence.
- **Chunk 23 is now bound in three places** by this merge (`FLAGS.md` §S3): `かかってくるがいい。`
  → `Ｙｏｕ　ｍａｙ　ｃｏｍｅ　ａｔ　ｍｅ．` (byte-identical, L15), `シナリオ` → `ｓｃｒｉｐｔ` (×2) and
  bare `守備` → `ｔｈｅ　ｄｅｆｅｎｃｅ`.

### ✅ ROUND-2 EVIDENCE: the translator STRENGTHENED the finding against itself
Chunk 19's translator accepted all four findings and, re-counting rather than trusting the
finding's own parenthetical, found the case for `Ｕｌｆ` is **stronger** than the reviewer stated:
`ｗｏｌｆ` is shipped across **2 unique lines** of `batch_003` (L39, L40) at 21 instances each —
**42 message instances, not 21**. And the decisive point neither the reviewer nor the seed made:
**L40's source is `キラーウルフが進化した狼の怪物。`, so the KATAKANA `ウルフ` already maps to
`ｗｏｌｆ` in shipped work**, not merely the kanji 狼. `Ｗｏｌｆ` would make one katakana string yield
the same English for a monster class and for a man announcing himself by name.

It also declined the invitation to contest finding 4 — the reviewer had named it as the one it
thought the translator could win — after checking and concluding the premise was true. Two of the
repacks fixed defects neither party had claimed: an orphaned `ａｍ` (§3.2), and a page that was
leading-blank + 4 text rows = 5, now 4 and inside the box. **No round-1 edit touches a cross-unit
term, so chunk 20 still needs no re-cut.**

### ✅ `あら` IS RULED (chunk 20's review, PR #14) — and §28.3 is corrected
→ **`Ｍｙ` + the source's own punctuation.** §24.4 already spent `Ｏｈ？` on おや across **29
occurrences**, so `Ｏｈ` cannot take a fourth string. §28.3's claim that "the alternative
`Ｏｈ　ｍｙ，` is also free" is **struck as false** — `chunk_011` L3 ships it for `あら、` itself —
with a full 12-row census recorded. This settles the question **both** chunk 20 and batch_006
raised independently, and it binds batch_006's review (PR #15).

⚠️ **OWED WORK, deliberately deferred to a §27-style corrections unit — put it in wave 5's queue:**
the `あら` re-cut of four shipped rows — `chunk_007` L19 and L24, `chunk_011` L3, `chunk_014` L3 —
all width-neutral or −6 bytes. It was not applied now because PR #15 is open on the same question
and chunk 19 was mid-rework. **Nothing shipped is wrong in a way that breaks a gate; this is
consistency debt with a known, measured fix.**

⚠️ **`勲章`'s §25.3 discharge was WITHDRAWN at that review.** Chunk 20's PR claimed the
co-occurrence test passed (never in one scene); the reviewer measured its true reach — **4 battle +
59 script-dump / 39 script-unique**, the plot item `獅子の勲章` — and found **banks 42 and 43 hold
both `勲章` and `メダル`**, so the test **fails**. Recorded as a live collision, with `ｔｏｋｅｎ`
reserved on the racetrack side. The merge stands; the collision is now documented rather than
believed discharged.

### ⚠️ A REVIEWER CORRECTED THE PREVIOUS REVIEWER'S RULING — same wave, one hour apart
Reviewer 1 added **glossary §31.3** (`まさか` → `Ｓｕｒｅｌｙ`) while merging chunk 18. Reviewer 2,
reviewing chunk 19, found it **over-broad, and chunk 19's non-conforming rendering to be the
correct one**:
- Of the **18 `まさか` in the battle dump, only 8** are the incredulous use `Ｓｕｒｅｌｙ` fits;
  **10 are the exclamative `まさか…とは`**, where `Ｓｕｒｅｌｙ` *inverts the sense*.
- §31.3 claims `Ｓｕｒｅｌｙ` is free across `tl/`. It is not — three shipped lowercase `ｓｕｒｅｌｙ`
  render `はずだ` and `きっと` in chunks 0, 7 and 34.
- §31.3 names chunk 0, but chunk 0's `まさか、` already ships as `Ｉｔ　ｃａｎ’ｔ　ｂｅ，`.

**Lines affected: none.** Both shipped `Ｓｕｒｅｌｙ` are the incredulous use and stand; chunk 0 stays
recorded-not-re-cut. Reviewer 2 will narrow it under §4.3 at its integration. **This is the review
layer working as designed — a ruling made at speed, caught by the next reader before it propagated
into three more chunks.**

### ⚠️ TWO COORDINATOR ERRORS, both caught by translators and both verified before recording

**1. I told chunk 19's translator that `フェリクス`, `ウルフ`, `自治官` and `衛兵隊長` were "already
in the glossary". They are not.** All four appear in `glossary.md` **only as Japanese quotations
inside §2's ファリーナ evidence note** (`ファリーナの衛兵隊長、ウルフ`, `ファリーナの自治官フェリクス`)
— quoted to prove Farina is a place. **No English form is fixed for any of them.** My preflight
check was `grep -c` for the Japanese string, and a substring hit is **not** a ruled rendering.
➡️ **Method for every future seed: a term is "in the glossary" only if a row FIXES an English
form for it.** Chunk 19 proposes `Ｆｅｌｉｘ`, `Ｗｏｌｆ` (alt `Ｕｌｆ`), `ｇｏｖｅｒｎｏｒ`,
`ｇｕａｒｄ　ｃａｐｔａｉｎ`; these are genuinely new and need ruling, not matching.

**2. My cross-unit note on `宝石` was incomplete in the other direction.** `宝石` → **`ｇｅｍ`
(lowercase) is ALREADY SHIPPED** — `tl/script/batch_003.tsv` L36, `額に宝石のはまった謎の生物。` →
`ｗｉｔｈ　ａ　ｇｅｍ　ｉｎ　ｉｔｓ　ｂｒｏｗ．`, one unique line carrying **21 instances**. Verified.
So `宝石` now has **three** English forms in play: shipped `ｇｅｍ`, chunk 20's `ｇｅｍｓｔｏｎｅｓ`
(PR #14), chunk 19's `ｇｅｍｓｔｏｎｅ` (PR #16). §3 is not engaged — all different messages — but
this is exactly the divergent-duplicate class wave 3's PR #9 existed to clean up. ⚠️ Note the
existing deliberate split it must not break: capitalised `Ｇｅｍ` (147×) renders **ジェム**, a
different Japanese word. **Chunk 31 inherits whatever is decided.**

### ✅ RULED 2026-09-09 — `あら` takes `Ｍｙ` + the source's own punctuation
Battle chunk 20 (PR #14) and script batch_006 (PR #15) raised this separately, from opposite ends
of the corpus, neither knowing the other had. **Chunk 20's reviewer ruled it at that merge:
`glossary.md` §32.4 and `FLAGS.md` §T1.** `Ｍｙ？` (3) / `Ｍｙ．．．？` (6) / `Ｍｙ，` (3).

**§28.3 is upheld and extended.** What decided it was not the count but that **§24.4 already spent
`Ｏｈ？` on おや outright, across 29 occurrences (6 battle + 23 script)** — so `chunk_014`'s
`あら？` → `Ｏｈ？` is byte-identical to a *different* fixed source word, and matching it would
delete a member of §24.4's set. The same-speaker fact (portrait 02) is real and argues for making
*one* form consistent; it does not choose which form.

**The census, gathered at that review — larger than §28.3's "16 further occurrences":** **12 `あら`
rows in the battle dump (chunks 7, 8, 11, 13, 14, 16, 20 ×2, 27, 29) + ~30 in the script.**

✅ **§28.3's "The alternative `Ｏｈ　ｍｙ，` is also free" is FALSE and has been STRUCK** — and it is
worse than recorded here: `Ｏｈ　ｍｙ，` is shipped in `chunk_011` L3 **for `あら、` itself**.

⚠️ **OWED WORK — four rows in three shipped files, NOT yet applied.** `FLAGS.md` §T1 carries the
table: `chunk_007` L19 (`Ｏｈ．．．．？`→`Ｍｙ．．．．？`, 0 bytes), `chunk_007` L24
(`Ｏｈ，　ｓｎｏｗ．．．？`→`Ｍｙ，　ｓｎｏｗ．．．？`, 0), `chunk_011` L3
(`Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？`→`Ｍｙ，　ｖｉｓｉｔｏｒｓ？`, −6), `chunk_014` L3 (`Ｏｈ？`→`Ｍｙ？`, 0).
All width-neutral or shorter; both files have ample slack (chunk 7: 399, chunk 11: 6,625). Left to
a §27-style corrections unit rather than done inside a battle-chunk merge while PR #15 was open on
the same question and chunk 19 was in rework. **Re-run `check` and `rowcheck` on 7, 11, 14 after.**
**PR #15's reviewer: batch_006 already ships `Ｍｙ，`, so it conforms — merge on this point.**

The five segment-checked data points batch_006 assembled:

| Where | Japanese | English |
|---|---|---|
| `chunk_011.txt` L3 | `あら、お客様？` | `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` |
| `chunk_014.txt` L3 | `あら？` | `Ｏｈ？` |
| `chunk_007.txt` L19 | `あら・・・・？` | `Ｏｈ．．．．？` |
| `chunk_013.txt` L4 | `あら、` | `Ｍｙ，` (§28.3's ratified form) |
| `chunk_007.txt` L24 | `あら、雪・・・？` | `Ｏｈ，　ｓｎｏｗ．．．？` (line-level only) |

⚠️ **`chunk_014.txt` L3 and chunk 20's instances are the SAME SPEAKER** (portrait 02) — §21.4 /
§25.5's unnamed female companion, "the one who notices", and both `あら` lines in chunk 20 are
hers. §3 is not engaged anywhere — all are different messages — so **no re-cut is forced**; the
four rows above move for house consistency under §4.3, not because a gate demands it. Batch_006
ships `Ｍｙ，` and chunk 20 ships `Ｍｙ？` / `Ｍｙ．．．？`: **both already conform to the ruling.**

### batch_006's other open items
- ⚠️ **`{FFEC}` insert widths — needs the disc, not a reviewer** (`FLAGS.md` §C4). **Both gates strip
  these inserts to 0 columns**, so the column gate is *blind* to twelve rows in this batch. The
  translator bounded every one at insert+8 against the Japanese's insert+0..+7 and did not spend a
  `{FFFE}` it could not justify. Four further copies of the same shop skeleton queue behind this.
- `おっと` has **no glossary entry and two divergent shipped renderings** (`chunk_007` `Ｎｏｗ　ｔｈｅｎ．`,
  parked `chunk_043` `Ａｈ　ａｈ，`); batch_006 took `Ｏｏｐｓ，` and flagged rather than silently adding
  a third. `そうだ、` gets a second form (`Ｓａｙ，`) on a grammatical argument — recall marker, not
  agreement. Both want ratifying or overturning, not drifting.
- `ノロ？` standing alone → `Ｎｙｏｒｏ？` is the tic's first non-suffixed rendering; a ruling binds the
  frog shop's `ゲロゲロ？`.
- **FORWARD-BINDING for later waves:** unique **598** must reuse this batch's menu strings
  byte-for-byte (`　Ｂｕｙ　ａｎ　ｉｔｅｍ` / `　Ｓｅｌｌ　ａｎ　ｉｔｅｍ` / `　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ`), and
  unique **592–597, 647–655** are the other two copies of the same shop skeleton — they inherit
  `Ｗｅｌｃｏｍｅ`, `Ｍａｎｙ　ｔｈａｎｋｓ`, `ａｒｔｉｃｌｅ`, `　Ｌｅａｖｅ　ｉｔ` and the notice wording.

## Next up — WAVE 5
**Battle chunks 21 (D 4.28), 22 (D 4.59), 24 (C 2.99)** — chapter order, all artifact-free.
⚠️ **Skip 23** as well as 15: both carry the §D1 dump artifact (Blocked item 0).

**One script batch — `queue.py script` position 1**, unique lines **318, 421–469** (50 lines /
52 instances, 3,056 JP chars, banks 2–3): recruitment and shop dialogue, vetted clean by wave 3.
⚠️ **Write it as `tl/script/batch_007.tsv`** — the position number is not the filename; wave 4
took `batch_006.tsv`.

| `queue.py script` position | Lines | Banks | Verdict |
|---|---|---|---|
| **1** — 318, 421–469 | 50 / 52 inst, 3,056 JP | 2, 3 | ✅ **clean — wave 5's pick** |
| ~~2~~ — 319, 335, 599–646 | 50 / 53 inst | 12–15 | ⏳ taken by wave 4 → `batch_006.tsv` |
| ~~3~~ — 320, 1073–1121 | 50 / 52 inst | 31–34 | ⛔ **28/50 DEBUG SCAFFOLDING** — BGM sound-test menu (`５０：新曲１`) and a flag screen (`どのフラグを操作しますか？`). **Never dispatch.** |
| 4 — 326–328, 470–516 | 50 / 53 inst, 1,638 JP | 4, 5, 7 | ✅ clean — ノロ village + towns. ⚠️ bank 5 has 3,381 free |

⚠️ **Vetting method, or the check silently passes everything:** `script_unique.txt` rows are
`<instance count>\t<text>`, so the scaffolding regex `フラグ|：新曲|^[０-９]{2}：|鑑賞モード` must
match the **text field**. Against the raw line the anchored `^[０-９]{2}：` never fires and position
3 scores 18/50 instead of its true 28/50 — a vet that looks like it passed.

**Seed the glossary BEFORE dispatching.** It moved four times during wave 3; wave 4 seeded 15 rows
up front and told every reviewer to re-run gate 7 against the *current* glossary.

## Remaining (dispatchable) — `python3 tools/queue.py battle`
Battle: **21 open chunks** after wave 3, but ⚠️ **6 of them carry the §D1 dump artifact (Blocked
item 0) and will park exactly as chunk 17 did — 15, 23, 27, 28, 29, 39.** Until a human fixes
`riotbattle.tokenise`, only **15 chunks are truly dispatchable**, in chapter order (tier, ratio) —
**~~18~~ ✅ merged 2026-09-08 (PR #13), 14 left; 19 and 20 are in flight in this wave**:
~~18 (D 6.28)~~, 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59), 24 (C 2.99), 25 (C 3.48),
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

   **Worst cases:** unique 1160–1354 (195 lines) are resident in **bank 40 alone** (471 free,
   needs ~19,000); unique 1355–1387 (33 lines, 14,607 JP chars) in **bank 41 alone** (353 free,
   needs ~29,000). Neither late chapter can be shipped even partially in a way worth playing.

   **Policy this run:** bank 40's spendable budget goes to the 21-instance item-description table
   (~40 lines ≈ 840 instances), not to bank 40's own story text (~25 of 195 lines ≈ 25 instances,
   leaving that chapter 90% Japanese). Reversible — a choice, not a fact — but the arithmetic is
   not close.
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

- 2026-09-08 (wave 4 preflight): ⚠️ **a fresh container clones SHALLOW and carries a STALE local
  `claude/workflow-translation-iterate-uzlkns` ref** (wave-1 state, *no merge base* with origin).
  The container starts detached at the right commit, so `git checkout <branch>` silently moves you
  backwards 51 commits and `git pull --ff-only` then aborts. Fix: `git reset --hard
  origin/claude/workflow-translation-iterate-uzlkns` after fetching. Verify with `git log -1`
  before trusting the tree — no work is lost, the local ref is a container artifact.
- 2026-09-08: **the `queue.py` batch POSITION is not the filename.** Wave 4's unit was position 2
  and became `batch_006.tsv`; `batch_002.tsv` has been merged since wave 1.

- 2026-09-09 (chunk 20, PR #14): **a co-occurrence discharge is only as good as its counts.** The
  §9 seed said `勲章` was "2 battle"; it is **4 battle + 59 script-dump** and a named plot item, and
  §25.3's test — *no chunk and no bank* — **fails** on banks 42–43. The rendering was still right.
  Count the corpus before writing "never in one scene"; a wrong reach figure turns a live collision
  into a closed one on paper (`FLAGS.md` §T2).
- 2026-09-09 (chunk 20, PR #14): **a reviewer may rule a cross-file question without re-cutting the
  outliers in the same commit.** The `あら` ruling binds immediately; the four shipped rows it
  invalidates are recorded with lines and measured costs and left to a §27-style corrections unit,
  because two sibling PRs were in flight on the same question. Recording with the lines named is
  what §4.3 requires; applying them mid-wave is not.

**Rulings live in their homes, not here**: `glossary.md` §23–§32, `FLAGS.md` §K–§T,
`findings.md` §24, `pending/README.md`. Wave 3 added §27–§30 and §O–§R; **wave 4 has added
glossary §31 / `FLAGS.md` §S (chunk 18, PR #13) and glossary §32 / `FLAGS.md` §T (chunk 20,
PR #14)**. ⚠️ **Section numbers are taken by reading both files at commit time, never reserved in
advance** — chunk 19's round-2 integration takes **§33 / §U** and PR #15's takes **§34 / §V**.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 13/44 (20.1%); script 185 lines (50.6%) |
| 2 | battle 4, 6, 9 + script 005 | **4** | 0 | battle 16/44 (26.3%); script 211 lines (50.9%) |
| 3 | corrections/audit-wave1 + battle 8, 13, 17 | **3** | **1** | battle **18/44 (32.2%)**; script unchanged |

**Wave 3 detail.** PRs #9–#12, full three-role split. `#9` corrections (12 edits, 5 files) closed
the live CLAUDE.md §3 violation — `tl/battle/` now holds 0 divergent duplicate renderings. `#11`
chunk 8 — 7,437 / 8,192, round 2. `#10` chunk 13 — 5,417 / 8,192, round 1, zero blocking findings.
`#12` chunk 17 — **PARKED**, translated and 2,335 bytes under its slot, blocked solely by the §D1
dump artifact. **The wave's pattern was findings being verified rather than obeyed, in both
directions** — translators disproved a finding's premise and improved on a proposed fix, two
reviewers withdrew findings after measuring, one demoted a ruling it had been asked to ratify, and
translators corrected three coordinator errors. Detail lives in `glossary.md` §27–§30 and
`FLAGS.md` §O–§R.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION says literally what to do next**; list open PRs and reconcile.
3. `/translate` — preflight, then do what NEXT ACTION says.
4. The run is recursive: each wave's session opens the next wave's session before it ends. If
   NEXT ACTION names a spawn that never happened, the chain broke — spawn it yourself. The only
   four reasons to stop are in CLAUDE.md §8.
