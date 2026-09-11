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
> # ▶ WAVE 13 IS RUNNING IN ITS OWN SESSION (opened 2026-09-11 ~21:48 UTC). DO NOT OPEN A SECOND ONE.
> **Units: battle chunks 15, 23, 27.** Coordinator: the wave-13 session (Opus, top-level, `Task` present,
> so the three-role split holds — translators and reviewer are its subagents).
> **If you are a coordinator reading this:** `list_sessions` — if a wave-13 session other than yours is
> alive, stop. The runner (Fable, root session) reconciles on its 15-minute watchdog and does not touch
> the repository while a wave is alive. **The engine work (Blocked 2, 4, 6 — `tools/slots.py`,
> `slotext.py`, `banks.py`, `bankext.py`, `engine.py`, `--extended`/`--layout`) belongs to the runner;
> a wave never edits it and never runs `build --extended`.**
>
> **Wave 13's own next step is tracked in In flight below.** On close: write wave 14 (chunks 28, 29, 39)
> into Next up, prove `origin/main` is at the close commit, and open the wave-14 session.
>
> ⚠️ Battle chunks are chapter-ordered and voices accumulate — read the shipped neighbours the dispatch
> names. ⚠️ Battle `tl/` holds no Japanese; **gate 6 must pair the dump positionally** (translator.md).
> ⚠️ **`queue.py battle` prints "dispatchable 7" and lists chunk 32 — it is NOT dispatchable.** §B2's
> measured floor is 1.64×; 32 is 1.61× and 16 is 1.59×, both blocked on the tier-A slot extension.
> ⚠️ **The re-dump changed the representation of 18 battle lines in exactly these chunks** (§BB4) — start
> every unit from the pristine dump as CLAUDE.md §2 says, never from an old worktree or an old PR.
>
> After wave 14 the battle store is exhausted short of the slot extension, and the script is where it
> was: **0 feasible lines, 363 of 366 behind the §F2 repoint.** Then §8's stop condition holds again.
## Last updated
2026-09-11 · by: **the wave-13 coordinator (its own session)** · **WAVE 13 DISPATCHED — battle chunks
15, 23, 27, three translators in parallel behind the wave barrier.** Glossary seeds committed as §9.W13
(`d96d42f`). Preflight green: `check` All checks passed, `origin/main` == local, one worktree, **no open
PR and no live agent at wave start**. · the game files are on `main` (`unpack.py`, §BB4) · engine build 1
still awaits its boot test (Blocked 4/6, the runner's work, not this wave's)

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **34** | 44 | 17 and 36 shipped 2026-09-11 (§BB, §BA); **6 dispatchable**; 16, 32 blocked and 5, 43 parked on the tier-A floor |
| Battle JP characters | **29,892** | 43,137 | **69.3%** — the total fell by 24: the artifact kanji had been counted as Japanese (§BB6) |
| Script unique lines | **1,064** | 1,430 | `tl/script/batch_001–022.tsv` (was 948) |
| Script message instances | **5,180** | 7,931 | **65.3%** (was 63.6%) |

`check`: **All checks passed** at the tokenise-fix commit, chunks 17 and 36 in `tl/battle/`. **glossary ends §64 · FLAGS ends §BB** — ⚠️ **always take
the next number by READING both files at commit time, never by reserving.**
`build/*_dump_merged.txt` regenerated at this close. README status table refreshed. **All worktrees
pruned — `git worktree list` shows only the main checkout.** **No open PR, no live agent.**
⚠️ **FOUR banks are under 2,000 free: 40 → 75 · 41 → 353 · 5 → 1,595 · 2 → 1,607.**
⚠️ **`bankmeasure`'s `tightest:` line prints only THREE, and WHICH ONE IT HIDES IS NOT STABLE** — it
hid bank 5 before wave 12 and hides **bank 2** now. **Quote the table, never that line.**
Parked and translated: chunks **5, 43** (tier-A budget) — nothing else is parked.

## In flight — WAVE 13, ✅ BARRIER MET 2026-09-11 ~22:50 UTC, reviewing in unit order
| Unit | Branch | PR | Bytes / 8,192 | Slack | State |
|---|---|---|---|---|---|
| battle **15** | `tl/battle-015` | **#47** | **3,275** | 4,917 | 🔄 **rework r1 pushed (`20764d2`) — RE-REVIEWER RUNNING** |
| battle **23** | `tl/battle-023` | **#49** | **6,291** | 1,901 | 🔄 **rework r1 pushed (`d917bb7`)** — all 5 implemented; **queued for re-review** |
| battle **27** | `tl/battle-027` | **#48** | 3,657 | 4,535 | ✅ PR open — queued |

All three base on `main`, all three one file, 0 re-dispatches, 0 lost. Reviewers run **one at a time,
foreground, in unit order 15 → 23 → 27**; HANDOFF is pushed before each and pulled after (the reviewer
pushes `integrate:main`). ⚠️ Each merge moves the base under the other two — expected; the reviewer
re-checks mergeability against a pinned SHA and never reuses an author's `merge-tree`.

### Integration debts the reviewer must carry onto `main` (detail in each PR body)
**PR #47 (chunk 15)** — ⭐ **close the wave-3 warning**: §9's `イフリート` row and §30.1 both say *"the
gloss is in chunk 15 — stays live for whoever takes chunk 15"*; **L0 now delivers it**. Promote the three
§9.W13 seeds (`ウシャシャシャシャシャ`, `ニール`, `炎熱騎士団` — all used as seeded, all exhausted).
Record five incumbent forms the glossary never held (`そういうワケにはいかない`, `ねえ、` → `Ｓａｙ，`,
`あと一息`, `やめたほうがいい`, `カーライン軍`); ⚠️ **two are SPELLING TWINS gate 6 cannot pair**
(`ワケ`/`訳`, `ほう`/`方`).
**PR #48 (chunk 27)** — nine glossary rows (`根城`, `坊や`, `袋のネズミ`, `間違いない`, `新手`, `ナメる`,
`ふん、`, `あっけなかった`, `ひと汗かいた`). ⚠️ **§9.W13's `根城` row STAYS LIVE** — chunk 32 holds its
fourth instance and 32 is blocked, so *that* unit strikes it, not this one. **§9.W13's `ダメージ` row is
discharged for battle** (3 script instances remain). ⭐⭐ **Flag 12 is a real cross-wave defect and needs a
RULING, not a re-cut: §30.4 reserves `ｕｎｄｅｒｅｓｔｉｍａｔｅ` for 甘く見る / 見くびる and claims it
"verified unspent across `tl/`" — but 甘く見る IS already shipped, as `ｔａｋｅ　…　ｌｉｇｈｔｌｙ`
(`chunk_006` L21, wave 2, before §30.4 was written). Invisible to a `tl/` grep; found by positional
pairing. The next unit reaching 見くびる (1 battle + 1 script) is the one that breaks.** This unit depends
on neither form and avoided both.
**Both PRs** — ⚠️ **`FLAGS.md`: the prompt and the tool disagree.** `translation_prompt.md` §3.2 tells a
translator to add a `{FCC0}` page break when four rows will not hold a page, but `assemble.py:tag_parity`
compares every tag except `{FFFE}`, so an added `{FCC0}` fails `check` (§Q2). **Both translators hit it
independently and both absorbed it by re-flowing `{FFFE}` inside the source's own pages** — chunk 27 paid
a text row on three pages to avoid §3.2 / §10-q4's untested leading-blank + trailing-blank + 4-row shape.
A tier-B/C chunk with a dense page may not be able to absorb it.

### ⚠️ PR #47 — CHANGES, round 1 (2026-09-11 ~23:15). Not merged; no integration commit; nothing pushed.
Seven of eight gates passed; **gate 7 failed**. I re-verified all three findings myself before relaying:
1. ⭐⭐ **`砲台` → `ｂａｔｔｅｒｙ`, not `ｇｕｎ` (4 places).** `glossary.md` §42.1 fixes `砲台 (prose)` →
   `ｂａｔｔｅｒｙ`, and **§42.8's correction table was written for chunk 15 BY NAME**, re-measuring
   `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` at 23 columns *specifically so chunk 15 would not be
   steered off it*. **CONFIRMED by reading §42.1 at `glossary.md:5173`.**
   ⚠️⚠️ **THIS ONE IS MINE.** My own §9.W13 census printed `砲台 … glossary:YES` and I read the
   `砲台 (prose) → ｂａｔｔｅｒｙ` row during seeding — **and then left it out of the chunk-15 dispatch's
   ALREADY KEYED list, where I did list `要塞`, `宮廷軍` and `焼き尽くす`.** The translator had no reason
   to look for it. **A seed that lists four keyed forms and silently omits a fifth is worse than one that
   lists none**, because it reads as exhaustive. Wave 12's Decisions §7 is now nine coordinator errors.
2. **`助かったよ。` → `Ｉ　ａｍ　ｓａｖｅｄ．`** (§23.4's default; 11 columns vs 10, zero re-flow).
   ⭐ **A CROSS-PR bind inside this wave: PR #49 already ships `Ｈｍ，　Ｉ　ａｍ　ｓａｖｅｄ．`**, so the
   two must agree. **CONFIRMED at `glossary.md:1795`.**
3. **`負けたよ。` → `Ｉ　ｌｏｓｅ．`, not `Ｙｏｕ　ｗｉｎ．`** (both instances, byte-identical, §40.3).
   ⚠️ **I suspected this was a substring false positive of `ｗｉｎ` inside `ｗｉｎｅ`/`ｗｉｎｄ` — the
   §3 trap — and CHECKED IT AS A WHOLE WORD. I was wrong and the reviewer is right:** `batch_015.tsv:57`
   ships `俺の負けだ。` → `Ｉ　ｌｏｓｅ．` and `勝ったら` → `ｗｉｎ` **twice in that one message**, and
   `chunk_037` renders 勝てる / 勝ち目 → `ｗｉｎ` twice more. `Ｙｏｕ　ｗｉｎ．` inverts an established
   two-store mapping.
⭐ **The wave-3 Ifrit warning is NOT discharged this round and stays live in §9 and §30.1** — the gloss
landed on the wrong noun, and a gloss in the wrong noun does not connect for the player.
**All three are FORWARD-direction misses** (what English this Japanese already has). The PR's reverse
EN→JP pass was genuinely good and caught four real problems — **it structurally cannot see this half.**
Still owed at merge: the `{FCC0}` / `tag_parity` `FLAGS.md` entry, and three PR-body corrections
(`巨大砲台` is not a new term; `ねえ、` → `Ｓａｙ，` is already §34.2; the `やめた方がいい` row over-reaches
against `batch_007.tsv:30`'s shipped `Ｂｅｔｔｅｒ　ｎｏｔ．`).

### ✅ PR #47 rework round 1 pushed (`20764d2`, 2026-09-11 ~23:35) — re-review QUEUED behind #49
**3,275 / 8,192 (4,917 slack)**, +36 bytes. `check` green, `rowcheck` clean, `{FFFE}` still body[6] only,
0 pages over 4 text rows. All three findings implemented; all three PR-body corrections accepted.
- **Finding 1 `砲台` → `ｂａｔｔｅｒｙ`: done, 4 of 4** (`ｇｕｎ` count in the file is **0**).
- ⭐⭐ **THE TRANSLATOR PUSHED BACK ON ONE POINT AND IT IS RIGHT — I VERIFIED ALL THREE OF ITS CLAIMS.**
  §42.8's correction cleared `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` **on width**, but width cannot
  settle this: **`batch_015.tsv:18` already ships `巨大な　砲台` → `ｇｉａｎｔ　ｂａｔｔｅｒｙ`** — a rumour
  line about *this* battery guarding *this* fortress. **CONFIRMED by reading the row.** Taking `ｇｒｅａｔ`
  would split a shipped compound — precisely the failure the withdrawn `Ｆｏｒｔ　Ｂａｕｅｒ` seed records.
  **`ｇｒｅａｔ` is also spent 42× across `tl/` (whole-word scan, CONFIRMED)**, including `大要塞` →
  `ｇｒｅａｔ　ｆｏｒｔｒｅｓｓ`. **So `ｇｉａｎｔ　ｂａｔｔｅｒｙ` stands and §42.8's suggestion must not be
  forced.** ⚠️ **A width-only clearance is not a gate-7 clearance** — worth a `FLAGS.md` line.
- **Two rows now sit at 24 columns** (legal; ≤23 is the preference). The translator brute-forced **every
  ≤4-row split of 26 phrasings** and reports 24 as the measured floor with every element kept; on the
  second row nothing reached ≤24 with `ｄａｎｇｅｒｏｕｓ`, so 危険 → **`ｐｅｒｉｌｏｕｓ`** — **not an
  invention: `batch_008.tsv:69` ships `危険な場所` → `ｐｅｒｉｌｏｕｓ` beside `:71`'s `ｄａｎｇｅｒｏｕｓ`
  for the same phrase. CONFIRMED by reading both rows.** Nothing dropped, no `ｇｕｎ` retained.
- **Finding 2 done** (`Ｉ　ａｍ　ｓａｖｅｄ．`, 11 cols). The adjacent `Ｉ’ｍ　Ｎｅｉｌ，` stays contracted
  on c08 L8's own incumbent — two adjacent rows differing by design, each on its own fixed form.
- **Finding 3 done on BOTH lines** (`Ｉ　ｌｏｓｅ．`, measured **13**, not the finding's 14 — one column
  narrower, zero re-flow). body[11] verified a **byte-exact 292-char suffix** of body[10].
- ⭐ **Correction 3 improved the file beyond the finding:** adopting `batch_007.tsv:30`'s shipped
  `Ｂｅｔｔｅｒ　ｎｏｔ．` freed enough width to **restore `援軍` → `ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ` and retire the
  `ａｉｄ` deviation entirely** (`ａｉｄ` count now 0). A finding aimed at consistency paid for a
  faithfulness gain elsewhere.
- **The translator withdrew its own `巨大砲台` glossary row** (not a new term) and accepted that
  `ねえ、` → `Ｓａｙ，` is already keyed at §32.3 / §34.2, not an unrecorded form.
- **It reports two more of its own round-1 hand counts wrong**, both found by `len()`. Every figure in
  the rework is tool output.
⚠️ **For the re-reviewer: the wave-3 Ifrit warning is now ARGUABLY discharged but that is the
REVIEWER'S call, not the translator's** — L0 now reads `ｔｈｅ　ｇｉａｎｔ　ｂａｔｔｅｒｙ`, the same phrase
the script store already uses for the object, so the gloss connects to both chunk 17's bare name and the
rumour line. **Do not close §9 / §30.1 without checking that in the file.**

### ⚠️ PR #49 — CHANGES, round 1 (2026-09-11 ~23:45). Not merged; no integration commit; nothing pushed.
**Eight of nine gates passed**; gate 7 failed on three already-fixed forms plus one register slip.
Merge base pinned to `f20740a`; `main` moved to `e59ac01` mid-review (HANDOFF only, so no gate redone).
Net of all fixes: **+12 bytes → 6,293 / 8,192, 1,899 slack**, one added `{FFFE}`, no re-flow.
⭐ **ALL FOUR RE-RUNS I ASKED FOR CAME BACK INDEPENDENTLY CONFIRMED, AND ONE CORRECTED THE TRANSLATOR:**
- **Twin codas: the reviewer found 10 repeated segments, 0 divergent** (translator said 11 — the extra is
  an indexer artefact, checked by hand). ⭐ **It also ran the REVERSE direction the translator did not:
  0 English forms shared between the two codas for different Japanese — nothing flattened.**
- **Cross-store frame: pairing exact, no comma or dot drift.** ⚠️ **It found a LIVE DEBT that is not this
  PR's: `batch_013.tsv:31` ships the byte-identical Japanese with a different English.** For FLAGS.
- **My figure stands, independently: `Ｈｉｍｉｋｏ’ｓ　ｓｑｕａｄ` = 14, `Ｈｉｍｉｋｏ’ｓ` = 8. 15 must not
  reach the glossary.** `Ｇｅｎｅｒａｌ　Ｉｖａｎ` 12 bare / 13 with comma — a scope difference, not a defect.
- **Flag 3's page shape: both claims hold** — the fill is attested **182× dump-wide** and the forbidden
  shape is absent from the whole battle dump (0). `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ａｌｆｒｅｄ` = 24 confirmed.
⭐⭐ **THE CROSS-PR §23.4 BIND IS DISCHARGED CONSISTENTLY** (finding 3): chunk 23's `助かったぞ。` takes the
**default** `Ｉ　ａｍ　ｓａｖｅｄ．`, same as #47's `助かったよ。` — よ and ぞ are the same particle class and
no licensing feature separates them. **The two PRs now agree.**
**I verified every finding before relaying:** §38.2 at `glossary.md:4327` is real and fixes the form
(⚠️ shipped in **3** script rows — `batch_007:32`, `batch_012:87`, `batch_014:46` — the review's "4×"
counts a different addressing convention; the finding is unaffected); §41.4 at `:4944` is real and is
exactly the register split it cites; **all five of finding 5's column corrections reproduce exactly**
(`ａｒｍｏｕｒｙ` 7, `ａ　ｐｅｔｔｙ　ｃｒｏｏｋ` 13, `ｓｈａｔｔｅｒｅｄ` 9, `Ｆｅａｒｓｏｍｅ，` 9,
`Ｈｉｍｉｋｏ’ｓ　ｓｑｕａｄ` 14), and so do findings 2–4's (8→10, 13→11, 22→21).
Still owed at merge: the eleven new rows, the **scoped** `すごい` row (scoping verified real), the
`イワン`/`ヒミコ` stay-live instruction, `まったくだ。` → `Ｉｎｄｅｅｄ．`, and the `batch_013`/`batch_017`
FLAGS debt.

### ✅ PR #49 rework round 1 pushed (`d917bb7`, 2026-09-11 ~23:56) — re-review QUEUED behind #47
**6,291 / 8,192 (1,901 slack)**, +10 bytes; realised 2.04×; `{FFFE}` 126 → 135; **`{FCC0}` 13 → 13**;
**0 rows over 23**; max 4 text rows. `check` green, `rowcheck` clean, gate 6 re-run (11 hits, all
byte-identical). **All five findings implemented.**
- ⚠️⚠️ **FINDING 1's COUNT: THREE PARTIES, THREE NUMBERS, AND MINE WAS WRONG.** The review said "4×",
  **I "corrected" it to 3 script rows, and the translator's census says 6 rows across 5 files. I
  re-ran it: THE TRANSLATOR IS RIGHT.** My search used the bare spelling `よろしく頼む` only and **missed
  `よろしく　頼む` WITH A FULL-WIDTH SPACE**, which is 3 more rows (`batch_007:28`, `batch_009:48`,
  `batch_010:65`). Verified rows: `batch_007:28`, `batch_007:32`, `batch_009:48`, `batch_010:65`,
  `batch_012:87`, `batch_014:46` — **all six ship the fixed form**, keying on **three** spellings
  (`よろしく　頼む` ×3, `よろしく頼む` ×1, `よろしく頼むぞ` ×2). **The finding is STRENGTHENED: the fixed
  form already spans the whole spelling family.** ⚠️ **This is the spelling-variant blind spot that has
  bitten this run repeatedly (§63.2 / §64.1 twins; the `ワケ`/`訳` and `ほう`/`方` pairs in #47) — and I
  walked into it while correcting someone else. A census over ONE spelling is not a census.**
  **Coordinator error #2 this wave** (after omitting `砲台` → `ｂａｔｔｅｒｙ` from the chunk-15 seed).
- **Finding 3: the translator asked for the ruling, it went against it, and it accepted on the evidence** —
  §26.8 settles the plain form in words it had read but not applied. Both of the chunk's `助かった`
  instances are now on the default side byte-identically, consistent with #47.
- **Finding 4** supersedes round-1 Flag 9's last table row. The translator then ran the REVERSE direction
  to bound the consequence: **exactly one English form in the file now renders two distinct Japanese, and
  nothing else was flattened.** Likewise finding 2 left **exactly one divergent run** (`どうやら、`,
  deliberate — narration box vs character) and it correctly did NOT "repair" it.
- ⭐ **ROUND-1 FLAG 12 IS WITHDRAWN IN FULL AND MY SEED CELL WAS RIGHT:** `Ｈｉｍｉｋｏ’ｓ` is **8**, not 9;
  `Ｈｉｍｉｋｏ’ｓ　ｓｑｕａｄ` = **14**. `Ｇｅｎｅｒａｌ　Ｉｖａｎ` 12 bare / 13 with comma — never a
  disagreement. All five of finding 5's figures reproduce.
- **New precedent worth recording at merge:** §41.4's register split applied for the first time to **a
  narration box against a character inside one file**; §23.4 / §26.8's default confirmed for a plain
  `助かったぞ` with an adjacent but out-of-sentence vocative.

### PR #49 (chunk 23) — the translator's report is in, integration debts below
**6,281 / 8,192 (1,911 slack); realised 2.03× against a 2.80× budget; 0 rows over 23 columns; no page
over 4 text rows.** ⭐ **The binding constraint was the 24×4 box, not the slot** — so there is no byte
risk if a later fix adds a character. Eleven new glossary rows (`武器倉庫`, `納庫`, `壊滅状態`,
`間抜けども`, `悪知恵`, `小悪党`, `交友関係`, `骨は拾ってやる`, `いい気味だ`, `おやすいご用です`,
`塔が襲われました。`, plus a **scoped** `すごい` row).
- ⚠️ **§9.W13's `イワン` and `ヒミコ` rows STAY LIVE** — each still has one script-store line unrendered;
  only `駐留部隊` and `帝国がバックにいた` are exhausted (the §29.1 / §30.1 cross-unit procedure).
- ⭐ **Flag 9 — the chunk's real hazard, and gate 6 is blind to it:** L21 and L22 are two mutually
  exclusive codas sharing **seven readable strings verbatim** and differing in six others by register
  alone. Gate 6 pairs whole messages and sees none of it. The translator ran a within-file run-granularity
  pass: **11 repeated runs, 0 divergent.** The reviewer should re-run that pass, not trust it.
- ⭐ **Flag 5 — a CROSS-STORE reuse no battle-side check could find:** the stock dungeon frame
  `…の中は静まり返っている` already ships in `batch_011`/`batch_014`/`batch_017`; the keys differ only in
  `館`/`ほこら`/`塔`, so the incumbent English was reused rather than forked.
- ⚠️ **Flag 12 — I VERIFIED BOTH CLAIMED CORRECTIONS TO MY SEED AND ONE OF THEM IS WRONG.** `len()`:
  `Ｇｅｎｅｒａｌ　Ｉｖａｎ` = **12** bare, **13** with the vocative comma — the translator measured the
  shipped form and its own note agrees the bare form is 12, so **there is no disagreement here**.
  `Ｈｉｍｉｋｏ’ｓ　ｓｑｕａｄ` = **14, NOT 15** — `Ｈｉｍｉｋｏ’ｓ` is **8, not 9**. **My seed cell was
  right; do not integrate 15 into the glossary.** Nothing renders differently (both ship inside rows of
  13 and 20) — but a wrong figure in the glossary propagates, and this run has already been bitten by
  relayed figures (Decisions §7). **The translator was right to challenge and right about the principle;
  this particular cell it got wrong.**
- **Open question for the reviewer — Flag 14:** which side of §23.4 `助かったぞ。` falls on. The
  translator took the active `Ｙｏｕ　ｓａｖｅｄ　ｍｅ．` and will take the default without argument
  (14 → 13 columns, one row, no re-flow). **Rule on it; do not leave it unanswered.**
- **Standing note, not a defect:** `ａｒｍｏｕｒｙ` contains `ａｒｍｏｕｒ` (§4's 防具), so any future
  substring census of `ａｒｍｏｕｒ` false-positives on this chunk. Recorded so nobody re-discovers it.

⚠️ **Every `tl/*` branch from waves 1–12 is MERGED but still on origin** — deletion returns **HTTP 403**
from the agent container (**FLAGS §AQ9**), every wave. **"Branch gone = merged" is an INVALID signal in
this repo; use the PR's `merged: true` and the squash SHA in the committed record.**

## Next up — WAVE 13, then WAVE 14 (battle; `queue.py battle` after the re-dump, 2026-09-11)
| Wave | Chunk | Tier | JP chars | Headroom | Ratio | EN budget (chars) | Note |
|---|---|---|---|---|---|---|---|
| **13** | **15** | D | 620 | 6,373 | 6.14× | 3,806 | |
| **13** | **23** | C | 1,257 | 4,521 | 2.80× | 3,517 | the tightest of the six — tier C, write tight from the first draft |
| **13** | **27** | D | 668 | 6,145 | 5.60× | 3,740 | |
| **14** | **28** | D | 770 | 5,807 | 4.77× | 3,673 | |
| **14** | **29** | D | 610 | 6,163 | 6.05× | 3,691 | |
| **14** | **39** | D | 622 | 6,479 | 6.21× | 3,861 | |

**Do not dispatch 16 (A, 1.59×) or 32 (1.61×)** — both below §B2's 1.64× floor; `queue.py`'s 1.6 cutoff is
wrong about 32. **No script batch:** 0 feasible lines (Remaining). Start each unit from the pristine
dump (CLAUDE.md §2) — these chunks' dump lines changed representation at the re-dump (§BB4).

## Remaining — 366 unique lines / 2,751 instances, and the binding constraint for every one
**Battle: 6 dispatchable** — 15, 23, 27, 28, 29, 39 (Next up). **2 blocked** — 16 and 32, on the tier-A
slot extension only (1.59× / 1.61× against §B2's 1.64×). §D1 applies to nothing any more (§BB).
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

## Decisions this run
### ⭐⭐ WAVE 12's LESSONS — the gate-7 hole is now fully mapped, and it has THREE faces
**Detail lives in `glossary.md` §61–§64 and `FLAGS.md` §AW–§AZ, not here.**
1. ⭐⭐ **GATE 7 HAS THREE FACES AND ALL THREE ARE NOW MANDATORY.** **(a) key cells** · **(b) NOTE
   cells** — wave 11's `さ、` had **0 first-column keys and 2 note-cell mentions**, so a key-first gate 7
   saw 0 of 2 and only the reading review caught a real collapse · **(c) ⭐ NEW: forms SHIPPED IN `tl/`
   THAT THE GLOSSARY NEVER RECORDED AT ALL** — **`その他` had 0 mentions of any kind, key or note, yet
   shipped 7× in `batch_013`.** **Face (c) defeats any glossary-side harvester however good, so gate 7
   needs a `tl/` COLUMN-2 PASS.** ⚠️ **It paid for itself on first use:** at PR #45 a pass over 2,893
   aligned JP→EN segment pairs found that `立ち寄る` → `ｃａｌｌ　ｉｎ` **over-reached and would have
   invalidated shipped work** (`batch_014.tsv:36` already ships `ｄｒｏｐ　ｉｎ`; §25.3 met on disjoint
   banks, so both stand and the key was narrowed). PR #46's pass covered **3,573 pairs / 2,949 distinct
   JP segments, 71 hits, 0 divergences**, and found `「古びた館」` → `“Ｏｌｄ　Ｍａｎｓｉｏｎ”` standing
   beside a shipped lowercase `ａｎ　ｏｌｄ　ｍａｎｓｉｏｎ` — **nothing else could have.**
   `その他` is now a first-column row (§64).
2. ⭐⭐ **HOW TO HAND-MEASURE COLUMNS — `assemble.py:106` SPLITS RUNS ON `{FCC0|FC30|FC51|FC50|FFFF}` AS
   WELL AS `{FFFE}`.** **A `{FFFE}`-only split CAN OVERSTATE COLUMNS.** PR #43's reviewer caught its own
   near-miss exactly that way: **27 columns reported, true rows 14 / 15**, because a `{FCC0}` sat inside
   the segment. ⚠️ **Also `rowcheck.py:_script_cols` expands only `{FFEC}{=00}{=00}` and `{FC00}` (to 7)
   and strips EVERY other insert to ZERO columns** — insert-bearing rows are **bounded, not measured**.
3. ⭐⭐ **ASSUME EVERY REACH FIGURE IN THIS REPO IS A RAW SUBSTRING COUNT UNTIL SHOWN OTHERWISE.** Three
   substring false positives in one wave: §34.1's `品` (inflated by `商品`/`景品`/`作品` — bare noun is
   **8 instances / 5 banks**, not 44 / 23) · `ｍｏｂ` (inside `ｍｏｂｉｌｅ`/`ｍｏｂｉｌｉｔｙ`) · `ＯＰ`
   (inside `＞ＯＰＥＲＡＴＩＯＮ`). Plus five more reach figures re-run and corrected at PR #44.
4. ⭐ **READ EVERY `{FFFE}` SEGMENT OF A POOLED ROW.** Two findings this wave came only from doing it —
   `品` in **segment 16** of a 25-segment row, and a `マップクリアー` incumbent in **segment 19** of a
   29-segment row. **I made the opposite mistake and it cost a false "no defect here".**
5. ⭐ **CITATION ADDRESSING — FIVE FACES NOW, AND THREE CONVENTIONS COEXIST IN `glossary.md` TODAY.**
   0-based vs 1-based; body index vs file line; and ⭐ **NEW: a line citation goes STALE THE MOMENT THE
   FILE ABOVE IT IS EDITED** — my own 65-line seed insert at line 866 silently moved every citation
   below it (`:6815`→`:6880`, `:4525`→`:4590`, `:3883`→`:3948`). **CITE BY SECTION, NOT BY LINE.** State
   for every number whether it is a 0-based index or a 1-based file line.
6. ⭐ **QUOTE DELTAS, NOT ABSOLUTES, IN A PR BODY THAT MAY SIT THROUGH ANOTHER MERGE.** Both debug PRs'
   absolute bank figures went stale by 28 bytes between authoring and review; **both deltas were exact.**
7. ⚠️ **EIGHT COORDINATOR ERRORS, ALL MINE, ALL CAUGHT BY TRANSLATORS AND REVIEWERS.** Miscounted
   `ｒｅｂｅｌｌｉｏｎ` as 10 columns (it is **9**, and my "+8 / 21→25 / needs a re-wrap" was wrong on all
   three counts) · a **case-sensitive** `Ｈｅｙ，` grep that wrongly cleared a chunk carrying lowercase
   `ｈｅｙ，`, "correcting" an inherited citation that was right · judged a **pooled 25-segment row from
   its head** · a `てーこく` cell wrong in **all three** figures whose "sets precedent" claim was false
   (wave 2 set it) · named **three** near-duplicate traps when §42.5 already held a **fourth** · a
   `フラグ`/`その他` attribution backwards · a **0-based body index that propagated into a translator's
   flag** · and ⭐ **relayed another agent's width table verbatim — wrong on 18 of 22 rows.**
   ⚠️⚠️ **THE SHARPEST LESSON OF THE WAVE: `batch_021`'s PROSE REPORT and its COMMITTED FILE disagreed
   on a width (23 vs 21). I relayed the report. THE FILE IS THE AUTHORITY — a relayed measurement is not
   a measurement, and a *reported* measurement is not one either.** ⚠️ **I also diagnosed the stale-line
   -citation bug mid-wave and then left the broken pointers in my own seed until a translator found them.
   Diagnosing a defect and not applying the fix to your own text is worse than not noticing it.**
8. ✅ **QUALITY CONTROL RAN IN BOTH DIRECTIONS, AS IT MUST.** Every one of my eight errors was caught by
   a subordinate agent. Reviewers corrected translators' figures (three of `batch_021`'s, five of
   `batch_022`'s) and translators corrected mine; **`batch_022` withdrew its own title-case draft** when
   its counter-evidence pointed at the other answer; **PR #43's reviewer disclosed a near-miss of its
   own**; PR #45's translator **disclosed that nine glossary sections were covered by key sweep rather
   than by eyes.** ⭐ **Better solutions than the ones I briefed came back twice:** the `反乱` fix took
   its article from an already-shipped sibling instead of inventing a third wording, and `batch_022`
   abbreviated only the menu row where I had said the full form must go.
9. **Rulings made this wave, all one-per-wave and binding:** ⭐⭐ **descriptive labels take SENTENCE
   CASE, title case only for a named thing or a §9-seeded label form** (§63.1/§AY3) — decided on §56.2's
   **eight sentence-case gutter menu labels**, which put §17.1's "capitalised throughout or not at all"
   back where it belongs (the class-name table) · **§AQ5's `編成` closed as a FALSE POSITIVE of its own
   gate**, for free and without the disc · **`Ｏ，　Ｏｉ，` stands** — §AJ3 argued lowercase by analogy to
   a *word doubling* when this is a *fragment stutter* (**23 : 6 capitalised** vs **7 : 0 lowercase**) ·
   the single **24-column** run ships (§64.3/§AZ3) · **`・` → `，` for apposition only**, which does
   **not** reach D1169's `ＯＮ・ＯＦＦ`.

**Standing (waves 4–12).** Integration branch is **`main`** — it was `claude/workflow-translation-iterate-uzlkns`
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
| **12** | **script 020, 021, 022 + corrections** (DATA 318/320/326–345, 997–1034, 1043–1099) | **4** | **0** | battle 32/44 (64.3%); script **1,064 (65.3%)** — ⭐ **ALL FOUR MERGED AT ROUND 1; the run's feasible queue is now EMPTY** |

**Wave 12 detail.** PRs #43–#46, **4 merged / 0 parked / 0 lost / 0 re-dispatches**, and — a first for
the run — **all four merged at ROUND 1 with no must-change finding.** Four separate reviewers, the
three-role split intact throughout, so **no unit is SELF-REVIEWED and there is NO audit debt.** Realised
growth **1.66×–1.98×** against the 2.10× plan, so every unit came in **under** its bound (bank 30 **456**
vs 782; bank 31 **1,724** vs 2,185; bank 5 **40** vs 94). Translators ran 27–53 min, reviewers 33–39 min.
**Four flags retired (§AJ3, §AP5, §AP7, §AQ5) and one closed as a false positive of its own gate.**
Detail lives in `glossary.md` §61–§64 and `FLAGS.md` §AW–§AZ.

## How to resume
1. `git fetch && git reset --hard origin/main` (a plain `checkout` can land on a stale shallow ref — see
   the top of this file), then `python3 tools/assemble.py check`.
2. **There IS dispatchable work: six battle chunks.** Run `/translate`, or open the wave-13 session with
   the SKILL.md §6a seed on `main`. Wave 13 = 15, 23, 27; wave 14 = 28, 29, 39 (Next up).
3. **After wave 14, the work is the human list under "Blocked — needs a human", in this order:** the
   boot test of engine build 1 (4 and 6 — the files exist, only an emulator is missing), the §F2
   bank-40/41 repoint (2, unlocks 363 script lines / 2,748 instances; MAIN1.EXE loader not yet traced),
   the two in-game visits (5). Engine work is done in the root session by Fable, not by wave agents.
4. **The game files are on `main`.** `python3 tools/unpack.py` rebuilds `original/` from
   `riotstars.zip.001–003` (pinned hashes; fails loudly on a bad part). `refresh` reproduced `dumps/`
   byte-for-byte on 2026-09-11 (FLAGS §BB4); if it ever does not, stop and look. `assemble.py build`
   runs the real `checkedit` anywhere now; the disc rebuild and play-test are still the human's.
