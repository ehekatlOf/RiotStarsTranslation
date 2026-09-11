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
> ### ▶ WAVE 10 IS COMPLETE — 3 of 3 MERGED, 0 parked, 0 open PRs. Coordinator `riotstarstranslation-31`:
> ### run the WAVE CLOSE (§4 step 6) and then OPEN WAVE 11's SESSION IN THE SAME TURN (§4 step 7).
> The reviewer slot is free and there is nothing left to review. Literally:
> 1. `git fetch && git reset --hard origin/claude/workflow-translation-iterate-uzlkns` (this
>    integration commit moved the branch — **do not `git checkout` a stale local ref**).
> 2. `check` on the integration branch — it passed here after integration; confirm it.
> 3. `merge`, commit `build/*_dump_merged.txt` if changed; refresh the README status table from
>    `status` (**803 / 1,430 lines · 4,896 / 7,931 instances · 61.7%**); prune worktrees.
> 4. Collapse wave 10 to one line in Wave history; write wave 11's unit list into Next up.
> 5. Commit and push `handoff: wave 10 closed`.
> 6. **Then, in the same turn, `create_session`** — this environment, `source_revision` =
>    `claude/workflow-translation-iterate-uzlkns`, prompt = wave 11 + its unit list + "read
>    `HANDOFF.md` first" — and name that session here **before** you open it. Do not stop to
>    summarise, do not ask permission. Ending the turn without opening it breaks the chain.
>
> **If this session is gone:** `git fetch && git reset --hard
> origin/claude/workflow-translation-iterate-uzlkns`, list open PRs (**there are none**), and do
> steps 1–6 above yourself — the wave is closed in substance, only the bookkeeping and the next
> session are outstanding.
>
> ✅ **The three-role split held for ALL THREE units.** `Task`, `send_later` and `create_session`
> all work here; wave 9's depth-8 cap does not apply. **No unit is SELF-REVIEWED and there is NO
> audit debt outstanding** — wave 10 closed 3 of 3, every unit reviewed by an agent that did not
> translate it, and each of the three went to a **fresh** reviewer at round 2. Wave 9 likewise
> closed 3 of 3 with five separate reviewers, and its wave-10 `orchestrator` subagent was stood
> down having merged nothing.
>
> ⚠️ **WAVE 10 IS SCRIPT-ONLY.** All 8 remaining battle chunks stay blocked on Blocked 0 / 0a.
> ⚠️ **The run is NOT complete** — ~250 lines stay bank-feasible after this wave, roughly 5–6 batches.

## Last updated
2026-09-11 · by: **PR #38 reviewer** (integration commit) ·
wave: **10 — ALL THREE UNITS MERGED. `batch_014` (PR #37, `af11117`); `batch_015` (PR #39, squash
`8f66547`); `batch_016` (PR #38, squash `900d755`)** · **3 of 3 units landed, 0 parked, 0 open PRs**

✅ **PR #38 decided MERGE at round 2, no findings.** All three round-1 findings verified applied on
`43fa715`; every §6 gate re-run on the merge tree `dc384c57`; `check` green on the integration
branch after integration. Review at `glossary.md` **§57** and `FLAGS.md` **§AS**.

⚠️ **Coordinator: the wave is COMPLETE and the reviewer slot is free. This is step 6 → step 7** —
run the wave close, then **open wave 11's session in the same turn** (CLAUDE.md §4 step 7). No unit
is SELF-REVIEWED; the three-role split held for all three units, with five separate reviewer
agents across the wave. `git pull --ff-only` before anything — this integration commit moved the
branch.

⚠️ **Do NOT write "branch deleted" for `tl/script-014`, `tl/script-015` or `tl/script-016`.** All
three are merged and all three are still on origin; `git push --delete` fails from the agent
container (§AQ9). **No deletion was attempted for `tl/script-016`.**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | **32** | 44 | unchanged — battle is blocked, not idle |
| Battle JP characters | **27,763** | 43,161 | **64.3%** |
| Script unique lines | **803** | 1,430 | `tl/script/batch_001–016.tsv` — **+55 from `batch_016`** |
| Script message instances | **4,896** | 7,931 | **61.7%** |

`check`: **All checks passed** on the `batch_016` merge tree `dc384c57` and again on this
integration branch after the integration commit. glossary ends **§57**, FLAGS ends **§AS** — both
re-read at commit time, not inherited or reserved.
⚠️ **TIGHTEST BANKS, re-measured by `bankmeasure.py` after this merge: 40 → 75, 41 → 353,
2 → 1,607, 5 → 1,635 — FOUR under 2,000, and `bankmeasure`'s `tightest:` line prints only THREE,
so bank 5 is invisible to anyone quoting it (§AS1).** Banks 40 and 41 have a spendable budget of
**zero** (free < the 500-byte reserve). Wave 10's own banks land at 18/19/20 → 8,473 / 7,803 /
21,299 and 21/22/23/24 → 34,269 / 38,033 / 28,265 / 39,511.
Parked and translated: chunks **5, 43** (tier-A budget), **17** (dump artifact), **36** (charset gate).

## In flight
✅ **BARRIER MET 2026-09-11 — all three units have an open PR (#37, #38, #39). Review has begun:
one `reviewer` subagent at a time, foreground, in unit order 014 → 015 → 016.**

⚠️ **"BRANCH GONE = MERGED" IS AN INVALID SIGNAL IN THIS REPO — DO NOT USE IT.** `git push --delete`
fails from the agent container (`send-pack: unexpected disconnect`) while ordinary pushes succeed;
`gh` is absent and the GitHub MCP has no delete-branch tool. **This has affected every reviewer all
run** — `tl/script-004`…`014` are all merged and all still present on origin. Recorded as **FLAGS
§AQ9**, ruled cosmetic. ⚠️ **PR #37's own HANDOFF row said "branch deleted"; it was not, and I have
corrected it here.** **Use the integration commit and the PR's merged state as the signal**, never
the branch's absence. One-action human fix: enable *Automatically delete head branches* on the repo.

---

⚠️ **MY ELEVENTH ERROR — AND THE SECOND TIME I HAVE PUT AN ERROR *INSIDE A CORRECTION*.** I told PR #39's
reviewer that `glossary.md:2217`'s `うーん、` row cites **both** banks wrongly. ✅ **Re-censused against the
SOURCE: only the `ふーむ` half is wrong, and my replacement figures were themselves short.**

| | the row says | I said | **true (source census, all lines)** |
|---|---|---|---|
| `ふーむ` | script bank 31 | banks 30, 11 | **banks 11, 30, 33** (D1129 is untranslated) |
| `うーん` | battle chunk 8 | "wrong" | **battle chunks 8 AND 26 — so the row is RIGHT**; script banks **2, 20, 29, 40** |

**Root cause, and it is the same shape as the phantom seed: I censused the wrong population.** I counted
**shipped lines in `tl/script/*.tsv`** — which answers *"where has this been translated?"* — when §25.3's
co-occurrence test asks *"where does this term OCCUR?"*, translated or not. Untranslated lines are
invisible to a `tl/` census and they are exactly what the test is about. **A census needs its corpus
stated, and mine was the wrong corpus.** ⚠️ **Note `うーん` occurs in bank 20 at D813 — this wave's own
line — so the row's test was live against my own unit and I could not see it.**
✅ **The RULING is untouched**: it rests on merged precedent (`batch_013` ships `ん〜` D925/D948 and
`うーん` D940 all in bank 29 as `Ｈｍｍ，`), which no census error affects.

⚠️ **STALE FIGURE IN THE HUMAN'S OWN BLOCKED LIST — for PR #38's reviewer to fix at integration.**
`FLAGS.md` **§F2 lines 321 and 330 state bank 40 has 1,771 free.** ✅ **It has 75** (`bankmeasure`, today).
That is the figure a human would read when costing the bank-40/41 repoint, which is **Blocked item 2**.
PR #39's reviewer correctly filed the `親衛隊`/D1330 blocker as **§F2a** rather than §B — **my dispatch
sent it to §B, which is tier-A battle ratios, and that was wrong too.**

---

### Review round 1 — PR #38 `batch_016`: **DECISION: CHANGES** (2026-09-11)
Gates: `paths ✓ · merge ✓ · check ✓ · figures ✓ · rows ✓ · banks ✓ · dupes ✓ · glossary ✗ · structure ✓`.
Tree gated: merge of `fad228e` + `ef1a5c9` → **`58a2337`** (`merge-tree --write-tree` + `git archive`), so
**#37 and #39 were in scope**. `check` = All checks passed, **803 unique forms = 748 + 55 exactly**. Banks
21/22/23/24 free **34,269 / 38,033 / 28,269 / 39,509**; **four banks under 2,000 free — 40 (75), 41 (353),
2 (1,607), 5 (1,635)**. Not merged; **no integration commit**.

⭐ **The unit's hardest work verified clean:** D863's lift from `batch_012` D390 is **byte-exact across 37
recurring pages, zero divergent**, and D865's lift from `chunk_037` is byte-exact across every twin found
by **positionally pairing the battle dump's Japanese against `tl/battle/` English** — the same census
technique `batch_015`'s translator invented earlier this wave, now used by a reviewer. The **Rimul
pronoun fix (Flag 12) is real and correctly shipped.**

**Three findings, all one-row or PR-body. Sent verbatim to the same translator (round 1 of 3).**
1. **D852** — `２００ジュエルで` ships as `Ｔｗｏ　ｈｕｎｄｒｅｄ　Ｊｅｗｅｌｓ？`, **the project's only
   spelled-out price**, against four shipped precedents keeping full-width digits — including
   **`batch_015:61`'s `２０ジュエルで` → `２０　Ｊｅｗｅｌｓ．　Ｗｉｌｌ　ｔｈａｔ　ｄｏ？`, the identical
   construction, merged THIS WAVE.** Fix also restores the dropped `でどうだ`.
2. **D868** — `じゃあ、` → `Ｒｉｇｈｔ　ｔｈｅｎ，` is a **third** form for a particle already shipped as
   `Ｗｅｌｌ　ｔｈｅｎ，` (`batch_010`) and `Ｗｅｌｌ，` (`batch_014`). The PR's reason — distinguishing D868
   from D860's `Ｒｉｇｈｔ，` — does not hold, since `Ｗｅｌｌ　ｔｈｅｎ，` distinguishes them equally.
3. **PR body only** — §6 wants per-line `{FFFE}` before→after; **seven messages changed and one is
   reported** (D816 7→6, D835 4→5, D839 2→3, D843 6→5, D844 2→1, D863 118→113, D865 59→62). All seven
   re-flows are sound.

⚠️ **IT CORRECTED MY DISPATCH THREE TIMES. Verified here; two are mine, and one is not a correction:**
1. ✅ **D849 is NOT a bounded row — I relayed a misclassification without checking it.** Its source writes
   **`＜個数＞` as LITERAL TEXT** and the unit renders literal `（ｎｕｍｂｅｒ）`; **the line contains no
   `{FFEC}` at all**, so it is fully measured at 19 columns. The unit's bounded rows are **D843 ×2 and
   D844 ×1**. The translator's own Flag 10 listed D849 and **I passed it into the review dispatch
   unverified — the same relay failure as the `素材` "21 banks" figure earlier this wave.** (Its
   ≥10-columns-headroom claim does hold: 13 / 10 / 16, independently measured.)
2. ✅ **The §F2 bank-40 staleness is WIDER than I found, and partly already fixed.** PR #39's reviewer had
   already written **§F2a at `FLAGS.md:386`**, which states outright that 1,771 "was true in August and is
   now stale". What is still owed is an **in-place marker**, and the stale figure appears **six times —
   lines 321, 330, 339, 360, 396, 754 — not the two I named.**
3. ⚖️ **`ピクシー` — NOT an error on either side, a scope difference; recording it so it is not "fixed"
   again.** The row covers **two** instances: **D909** (bank 28, shipped in `batch_010` before this wave)
   and **D817** (bank 21, rendered here). So D817 was the **sole OUTSTANDING** instance — my wording — and
   the row's **total census is two** — the reviewer's. **Both are true and the strike verdict is identical.**
   This is the sixth convention/scope mismatch this wave; **state the scope, do not report it as a mistake.**

**Ratified, do not reopen:** `バトウ` at D864 stays **`Ｂａｔｏｕ`** (§26.1) — the translator declined my
dispatch and the reviewer upheld it. `マーシュ`, `クーデター`, `親衛隊` **stay live**; `『獅子の勲章』` is
**exhausted** (D386/390/863 all rendered). Two figure differences are **method** differences, not errors:
gate-7 keys **1,317** (reviewer, `/`-split + struck rows) vs **1,138** (PR); insert rows **54** (post-merge)
vs **51** (pre-#38).

### Rework round 1 — PR #38 `batch_016`: **all three findings applied, pushed as `43fa715`** (2026-09-11)
**Rebased onto `53afa23` first**, so `batch_014`/`batch_015` are in its duplicate surface and §55/§56 in its
glossary surface. Gates re-run on the enlarged corpus: `check` passes (4,896 lines / 803 unique forms) ·
`merge` 0 unmatched · `rowcheck script` clean · banks 21/22/23/24 free **34,269 / 38,033 / 28,265 / 39,511** ·
slot-level Japanese-side sweep over **16 script TSVs + 32 battle chunks: 0 conflicts** · cross-file
item-name gate 63 messages / 53 names / **0 divergences** · **gate 7 re-run at 1,175 keys** (up 38 from
§55/§56), 120 occurring. Growth **+8,598 B**, ratio **2.012×**.

⭐ **IT FOUND A STRONGER PRECEDENT THAN THE REVIEWER'S FOR FINDING 2.** ✅ Corroborated here:
**`chunk_003` ships `Ｒｉｇｈｔ，　ｔｈｅｎ．` on the line whose Japanese carries `よし、じゃあ、`** — so
`よし` = `Ｒｉｇｈｔ` and `じゃあ` = `ｔｈｅｎ` in a **single shipped row**. Its coinage had appropriated
`Ｒｉｇｈｔ`, which belongs to `よし` — exactly the reviewer's objection, proved from one line rather than
two separate precedents. ⚠️ **`じゃあ、` → `Ｒｉｇｈｔ　ｔｈｅｎ，` must NOT be recorded in the glossary.**

⭐ **AND IT FOUND WHY IT MADE THE PRICE ERROR — a rule-scope gap, not carelessness (its Flag 20).** It had
applied **§10.8** (cardinals in running prose spelled out; digits kept in fixed names and tables of
numbers). **A price is neither**, so §10.8 does not reach it and the corpus does. ⚠️ **Note for the
reviewer: `glossary.md:3662` (§36.6) states "§10.8 is CLOSED", so the fix may belong in §36.6's successor
rather than in §10.8 itself — check before writing.** Either way **the corpus rule is: prices keep their
full-width digits** — 4 shipped, 4 keeping digits.

⚖️ **One change it DECLINED, disclosed rather than made silently (Flag 21) — good judgement.** D846 could
also take `Ｗｅｌｌ　ｔｈｅｎ，`, but this unit's other two instances of the particle (D863, D865) are
**lifts** rendering it bare `Ｔｈｅｎ`, so changing D846 would fork the particle **against donor rows it
must not touch**. Only D868, where the particle stands alone on its row, takes the fuller form. **One row
to overrule if the reviewer disagrees.**

✅ **It confirmed the D849 correction the hard way** — listing every tag in the source line: **six `{FFFE}`
and no `{FFEC}` at all**. My headroom figures were exact (13 / 10 / 16). Flag 10 now reads **D843 ×2 and
D844 ×1**.
✅ **Gate 7 against the 38 new §55/§56 rows: exactly one reaches this unit and it is a FALSE POSITIVE** —
§55's `なあ、` → `Ｔｅｌｌ　ｍｅ，` keys on the **clause-initial** particle; D857's `買っていったなあ。` is the
**sentence-final** musing one. Two other new rows **confirm** its existing choices.
✅ **All five of D863's and all three of D865's `{FFFE}` changes are inside the LIFTS** — the donor's own
flow reproduced byte-for-byte, so those counts are `batch_012`'s and `chunk_037`'s, not this unit's.

### Review round 2 — PR #38 `batch_016`: **DECISION: MERGE, no findings** (2026-09-11)
Gates: `paths ✓ · merge ✓ · check ✓ · figures ✓ · rows ✓ · banks ✓ · dupes ✓ · glossary ✓ · structure ✓`.
Fresh reviewer, everything re-run on `43fa715`, nothing inherited. Tree gated: `merge-tree --write-tree`
of `43fa715` onto `38cc606` → **`dc384c57`** (`git archive`, §AK6). `check` = All checks passed,
**803 unique forms = 748 + 55**. Squash **`900d755`**; integration commit below. Every PR figure
re-derived and confirmed: ratio **2.0120×**, growth **+8,598 B**, banks **34,269 / 38,033 / 28,265 /
39,511**, `{FFFE}` net **−3** on exactly the seven named messages. **Round 1's three findings all
verified applied.** Widest run **23**, **0 at 24**, 0 over 24 under `rowcheck`'s own run model.

⭐ **Both of the translator's discoveries corroborated from the dumps, not relayed.** `chunk_003` body
line 3 does ship `よし、じゃあ、` → `Ｒｉｇｈｔ，　ｔｈｅｎ．` in one row, and a census of every slot whose
Japanese is exactly `よし、` finds `Ｒｉｇｈｔ，` in **5 of 5** — `Ｒｉｇｈｔ` belongs to `よし` (§57.2).
And glossary **§36.6 does say "§10.8 is CLOSED"**, so the prices rule went to **§57.3**, not §10.8.
⚖️ **Flag 21's declined change at D846 is UPHELD** — reasoned in full at §57.2, so it is not reopened.

⚠️ **THREE OF THE ELEVEN §9 SEEDS WERE NOT STRUCK, against the PR's request.** A promotion is not a
strike: censused break-insensitively, **`腕力` (DATA 1234), `体力` (DATA 1126) and `慰霊金` (DATA 1351)
still have untranslated instances** and stay LIVE. Eight are exhausted and struck, plus `ピクシー` and
`『獅子の勲章』`. Also still live: `マーシュ` (D1325, D1374 + 1 battle), `クーデター` (D1373), `親衛隊`
(D1330), and **`命中率` (D1237)** — a form first rendered here but not exhausted.
⚠️ **Figure stated with its corpus:** the price census is **5 of 5 keeping full-width digits** *with*
this unit's D852 counted; "4 of 4" is the same census without it. Both true — say which you counted.
✅ **§F2's stale bank-40 `1,771` now carries an in-place ⚠️ STALE marker at all five remaining
occurrences** (FLAGS.md lines 321, 330, 339, 360, 754); line 396 already said so. The bank has **75**.

| Unit | DATA | Lines / inst | JP chars | Banks | Branch | State |
|---|---|---|---|---|---|---|
| `batch_014` | 707–758 | 52 / 52 | 2,742 | 18, 19, 20 | `tl/script-014` (⚠️ **NOT deleted**) | ✅ **MERGED round 2 — PR #37, squash `af11117`**, integration `aa85e2a` + `309e613` |
| `batch_015` | 759–814 | 56 / 56 | 3,161 | 20 | `tl/script-015` (⚠️ **NOT deleted**) | ✅ **MERGED round 2 — PR #39, squash `8f66547`**, integration below. Read the row as **"great port town NPCs"** — the unit never names its own town |
| `batch_016` | 815–869 | 55 / 55 | 4,251 | 21, 22, 23, 24 | `tl/script-016` (⚠️ **NOT deleted**) | ✅ **MERGED round 2 — PR #38, squash `900d755`**, integration below. Round 2 found **no findings**; all three round-1 findings verified applied |

Combined growth demand never exceeds **30% of any bank's spendable budget** (worst: bank 19 at
2,978 of 10,027). Bank-feasibility is not a risk in this wave; **terminology consistency is.**

**`batch_014` → PR #37** (2026-09-11). 52/52 lines, ratio **2.0201×** as merged, growth **5,594 B**; banks
18/19/20 land at **8,473 / 7,803 / 28,477** free, all three **under** the projection. ⚠️ **CORRECTED
2026-09-11 (PR #39 review): I recorded 7,809 / 28,469 from the PRE-REWORK PR body and never refreshed
them after the rework changed the file.** The bank-20 share is **1,012 B**, not the 1,259 I derived by
subtraction, so the wave's combined bank-20 demand was **8,190 B**, not 8,429. Widest row 23, **0 at 24**,
no page over 4 rows. One `{FFFE}` added (D715, forced), **no `{FCC0}` change**. Gate 7 run key-first:
**2,342 keys enumerated, 145 occurring, all adjudicated.**

⚠️ **THE UNIT CAUGHT THREE ERRORS IN MY SEED. All three verified against primary sources before
acceptance, not taken on the report:**
1. **`バウアーの砦` — seed WITHDRAWN.** §2 has shipped `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` since ch.40 under the
   **kana variant `バウワーの砦`**; my `Ｆｏｒｔ　Ｂａｕｅｒ` would have split a shipped proper noun.
   Census: `バウアー` script 2 / battle 1, `バウワー` script 0 / battle 1. **§AG6's mirror — I searched
   one spelling and never the other.** ⚠️ **D1300 inherits this in a later wave.**
2. **`生き返りの仙人` was a phantom compound.** Not at D756 (which has `生き返らせる…仙人`), and at D782
   only across a `{FFFE}` — so **0 hits on a raw grep of every dump**. Row corrected to bare `仙人`
   → `ｈｅｒｍｉｔ`. **D782 is `batch_015`'s; the correction was sent to that translator in flight.**
3. **D716 carries a doubled `。`** (`・・・。。` = 5 stops vs D711/D714's 4), so Table A's single English
   string was right for two of its three lines. §3.1 takes the source count; shipped with five.

⚠️ **One error in the unit's own PR body, for the reviewer:** its Glossary-additions table writes the
key as **`ボンネット平原`**; the source at D745 is **`ボネット平原`** (no `ン`) — verified. The TSV itself
must be right (`merge` reports no "never matched the dump"), so this is a report-only typo — but it
must not enter `glossary.md` as written.

**`batch_016` → PR #38** (2026-09-11). 55/55 lines, ratio **2.012×**, growth **8,596 B**; banks 21/22/23/24
land at **34,269 / 38,033 / 28,269 / 39,509** free, every one **under** the projection. One `{FFFE}` added
(D839, forced), **no `{FCC0}` change**. Both giants (D863 1,277 JP, D865 642) shipped without parking.

⚠️ **IT DECLINED MY DISPATCH ON `バトウ`, AND IT WAS RIGHT. Verified against the source and the glossary:**
- **D814 is `バトウ神父`** → §36.1 `Ｆａｔｈｅｒ　Ｂａｔｏｕ` (12). **D864 is `このバトウも`** — the bare name in
  self-reference → §26.1 `Ｂａｔｏｕ` (6), shipped as `Ｉ，　Ｂａｔｏｕ，　…` on §25.1's `このマラナ、` appositive.
- **My dispatch asserted both were `Ｆａｔｈｅｒ　Ｂａｔｏｕ` and cross-unit with `batch_015`.** They are two
  different source strings with two separately fixed forms, and §26.1 warns in terms that the `様` and
  bare patterns "must never be merged". **There is no cross-unit conflict.** I also mislabelled D814 as
  `バトウ様`; it is `バトウ神父`. ✅ `batch_015`'s D814 output is unaffected — `Ｆａｔｈｅｒ　Ｂａｔｏｕ` is right
  for it either way — so it was not interrupted a second time.
- ⚠️ **Reviewer: do NOT "harmonise" D864 to `Ｆａｔｈｅｒ　Ｂａｔｏｕ` on the strength of my dispatch.**

⚠️ **MY "FOUR NEAR-DUPLICATE PAIRS" WAS THREE.** Measured longest common substring: D859/D867 **10**,
D860/D868 **10**, D861/D869 **17** — genuine twins. **D850/D866 share only `　兵隊さん` (5)** and have no
clause in common; they are two different refusals by the same man. I over-claimed from a skim.

✅ **An independent check that came back clean:** `batch_016` re-measured all ten of my corrected seed
widths under `len()` and found **zero** errors — including `「本日休業」` → 14, where its own hand count
said 15 and the seed was right. The widths are sound **after** the correction; it was the first draft
that was wrong in all 45.

**Open for `batch_016`'s reviewer:** (a) Flag 2, the `バトウ` ruling above; (b) Flag 7 — D834's
`うまく有利すること` looks like a source typo for `利用`, English works on either reading, needs a human
in-game; (c) Flag 14 — D849 is a seven-row source page with no `{FC30}`, possibly an unused string;
(d) Flag 10 — three rows are **bounded, not measured**, because neither tool counts `{FFEC}{=00}{=01}`
/ `{=02}` number inserts (all have ≥ 10 columns headroom); (e) the §9 strikes it lists — `ピクシー` is
exhausted by D817, `『獅子の勲章』` by D863; `マーシュ` and `クーデター` **stay live** (FILE 1330/1379 and
DATA 1373 remain).

**`batch_015` → PR #39** (2026-09-11). 56/56 lines, ratio **2.13×**, growth **+7,170 B measured**
(bank 20 free 29,489 → **22,319**, 24.7% of spendable). Widest row 24, **353 of 373 runs ≤ 23**, no
page over 4 rows. Nothing parked. It measured the bank delta by moving its own file out of `tl/`,
re-running `merge`+`bankmeasure`, restoring and re-running — **not by copying my figure.**

⚠️ **IT CAUGHT FOUR MORE OF MY ERRORS. All verified here against the dumps:**
1. **`ｈｅｒｍｉｔ` is 6 columns, not 7** — and that 7 was in the row I wrote **as a correction** to the
   phantom `生き返りの仙人` seed. **A wrong correction entering the record as fact is §4.3's own named
   trap, and I walked into it.** Fixed in `glossary.md`.
2. **"Longest line is D803 at 188 JP chars" — the number is right, the line is wrong.** Measured:
   **D807 = 188**, D803 = 158, D806 = 105.
3. **"Projected growth ~3,400 B, about 12% of spendable" was the CHARACTER growth mislabelled as
   bytes.** (2.10−1)×3,161 = 3,477 characters; bytes are twice that. My own model gives **7,263 B**
   and the measured figure is **7,170 B = 24.7%**. ⚠️ **The survey and this board were NOT affected**
   — the combined bank-20 demand recorded at dispatch, 8,429 B, is right and reconciles
   (7,170 for `batch_015` + 1,259 for `batch_014`'s bank-20 share). **The error was confined to one
   dispatch line, and the conclusion — bank capacity is not binding — held either way.**
4. **`親衛隊` is 7 script-unique lines, not the 6 my seed implied**: D789/791/792/793/794 (bank 20),
   D898 (bank 28, shipped), and **D1330 in BANK 40**, which has 75 bytes free and a spendable budget
   of zero under §F2. **So the row stays LIVE after this wave and its last instance may never land
   without an engine-side fix.** Recorded in the glossary row; **it also wants a FLAGS §B entry**,
   which is the reviewer's to make.

⚠️ **MY UNIT TITLE FOR `batch_015` NAMES THE WRONG TOWN.** I called it "Rimrose town NPCs". The
speakers are **not** in Limrose: **D759** has them describe their own town as `王国一の商業都市にして、
最大の貿易港` (the kingdom's greatest commercial city and largest trading port), and **D760** says a
troupe `リムローズに　きてる` — come *to* Limrose — and the speaker wants to **go there** and see it.
**The unit never names its own town.** The translator kept my commit title so this board would still
match on it, which was the right call. Read the row as **"great port town NPCs"**.

**Open for `batch_015`'s reviewer to rule:** (a) Flag 5 — `フーム` → `Ｈｍｍｍ` vs collapsing onto
§26.5's `Ｈｍｍ`; **this unit breaks that row's stated co-occurrence test**, since `うーん、` (D813) and
`フーム` (D807) are both in bank 20; (b) Flag 10 — bare `極上のワイン` at **D770** carries no `『』`, so
it ships capitalised but unquoted; there is **no incumbent for the unbracketed case** — rule it;
(c) Flag 9 — `ｇｈｏｓｔｓ` vs the seed's singular; (d) Flag 7 — two in-bank pairs of already-fixed
forms it could not avoid and correctly did not fork.
**Pre-existing debt it found on the branch, for the reviewer (it could not touch `main`):**
`batch_010` D897 ships `ｒａｉｓｅｄ　ｔｈｅ　ｒｅｖｏｌｔ` for bare `反乱` against §38.3's fixed
`ｒｅｂｅｌｌｉｏｎ`; and **§37.1's line list "DATA 443, 785, 896, 1383" is off by one throughout** —
the true census is **444, 786, 897, 1384**.

---

### Review round 1 — PR #37 `batch_014`: **DECISION: CHANGES** (2026-09-11)
Gates: `paths ✓ · merge ✓ · check ✓ · figures ✓ · rows ✓ · banks ✓ · dupes ✓ · glossary ✗ · structure ✓`.
Tree gated: `git merge-tree --write-tree` of `tl/script-014` onto `4f22aae` → tree `ee6c21e`, which the
real merge reproduced. **Every headline figure in the PR body reproduced exactly**, including the bank
deltas, measured against a real baseline. Not merged; **no integration commit** (CHANGES means none).

**Four findings, all zero- or near-zero-byte. Sent verbatim to the same translator (round 1 of 3).**
1. **D740 — a price-insert row at 21 columns** against §V1's ratified bound of **8** (the whole shipped
   corpus holds all 42 such rows to 8). ⚠️ **`rowcheck.py:_script_cols` strips `{=00}{=01}` to 0 columns,
   so NO GATE CAN SEE THIS** — and prices reach four digits (`１０００`/`２０００`/`５０００ジュエル` are
   literal in `script_dump.txt`), so the row would render at **25 columns in game**. Fix is zero-byte.
2. **D738 — same class at 17 columns.**
3. **D744 — `乗り気` → `ｋｅｅｎ` is a real §25.3 collision.** ✅ **Verified here:** `鋭い` → `ｋｅｅｎ` ships in
   **five** lines (D36, D75, D79, D165, D169), each 21 instances spanning 21 banks **including bank 19**,
   which is D744's own bank. The unit's own Flag 13 names the unspent reserve `ｅａｇｅｒ`.
4. **D750 — `ｅｖｅｒｙ　ｌａｓｔ　ｃｏｉｎ` imports a currency the game lacks** (`ｃｏｉｎ` occurs nowhere else;
   `Ｊｅｗｅｌ` ×47). Lowest severity.

⚠️ **A FIGURE I PROPAGATED WITHOUT CHECKING, AND THE REVIEWER CAUGHT IT.** I repeated the PR body's
"`素材` reaches 21 banks" into both the review dispatch and this board. ✅ **Verified: `素材` is 4 unique
lines — D737, D738, D740 are each count 1 and ALL IN BANK 19 alone; the entire 21-bank reach is
DATA 289**, a single count-21 armour-description line that is **untranslated**. The ruling is therefore
`素材` → `ｓｔｕｆｆ` **approved but sense-split**, with D289 explicitly not bound. **This is the eighth
figure error of the wave and the first I passed along from someone else rather than generating.**

**Other rulings:** D719's developer note **stays translated in place** (reachable after the message's
first `{FC30}`; blanking it would change the byte stream — a FLAGS item for a human with the disc).
D712's `発見つけた` is a **source typo** → FLAGS §B. Three PR-body glossary keys had drifted from the
source (`ボンネット平原`→`ボネット平原`, `かくれ家`→`隠れ家`, `能力`→`能力値` — **the §9 seeds were right and
the PR table drifted**), and the gutter census is **20→27 / seven**, not 28 / eight: all **report-only,
applied by the reviewer at merge — the translator must NOT re-push for them.**
✅ It also **withdrew two findings after measuring** rather than reporting them: the unit's
line-ending and single-word-row rates (7.8% / 7.5%) sit *below* merged `batch_010`/`012`/`013`.

⚠️ **NEW INFRASTRUCTURE FLAG — REVIEWERS CANNOT SET `REQUEST_CHANGES` IN THIS REPO.** GitHub refuses
it: *"Can not request changes on your own pull request"* (single-account repo). The decision is posted
as a COMMENT review whose **first line is `DECISION: CHANGES`**, with an explicit do-not-merge note.
**Every future reviewer inherits this — do not read an absent REQUEST_CHANGES state as approval.**
Belongs in `FLAGS.md` at the next integration commit.

### Rework round 1 — PR #37 `batch_014`: **all four findings applied, pushed as `727146b`** (2026-09-11)
One commit, one file, `build/` restored. **Zero added tags, −2 bytes net.** Gates re-run on the pushed
file: `check` passes · `merge` 0 unmatched · `bankmeasure` 18/19/20 free **8,473 / 7,803 / 28,477** ·
`rowcheck script` 15 warnings, **0 of them this unit's** · gate 6 0 collisions, both internal duplicate
pairs byte-identical · cross-file item-name gate 43 names, 0 divergences of its own. Figures now
JP 2,742 → EN **5,539** = **2.0201×**, growth **5,594 B**; bank deltas close exactly against it.
**All 27 price rows in the corpus now read 7×1 / 8×26 — no outlier left.**

⭐ **THE TRANSLATOR FOUND A BETTER REASON FOR FINDING 4 THAN THE REVIEWER GAVE, AND IT RESERVES A WORD
FOR A LATER WAVE.** The reviewer objected to `ｃｏｉｎ` because the game "lacks a coin". ✅ **Verified: the
game HAS one** — `コイン` is at **DATA 1398 (bank 42)** and **DATA 1419 (bank 43)**, both **untranslated**,
both the casino medal counter (`購入するコインの枚数を決めて…`). So spending `ｃｏｉｎ` on `全部` would have
**pre-empted the word the casino's own interface needs, in the same scene domain**. Rendered
`ａｌｌ　ｏｆ　ｔｈｅｍ，` instead. ⚠️ **WAVE 11+: `ｃｏｉｎ` IS RESERVED for `コイン` at D1398 / D1419** — and
**both lines sit in the wave-11 feasible queue** (1388–1413 and 1415–1430). Do not spend it elsewhere.

⚠️ **A "CORRECTION" THAT WAS A CONVENTION MISMATCH — NEITHER SIDE IS WRONG, AND NOBODY SHOULD "FIX" IT.**
The translator reported finding 4's line number as off ("`全部` is at line 52, not 44; line 44 is D742").
✅ **Measured in the pushed file: D750 is FILE line 52 AND data-line index 44; D742 is FILE line 44 and
data-line index 36.** The reviewer counted data-lines, the translator counted file lines, **both point at
D750, and "FILE 44 = D742" is also true.** This is exactly the **DATA-vs-FILE trap** already recorded in
Decisions as having fired twice in wave 8. **Reviewer: do not act on this as an error in either
direction** — state the convention instead.

**One partial push-back, accepted, and it corrects BOTH earlier figures.** Flag 10's gutter census was
reported by the translator as 20→28/eight and by the reviewer as 20→27/seven. The translator re-measured
and both conflate two things: **true cursor gutters are 20 → 20, zero lost**, and there are separately
**8 insert word-spaces** (6 price, 2 player-name). A row opening `{FFEC}…　` has readable text starting
with a full-width space once tags are stripped, so a naive split counts it as a gutter. **It did not
re-push for this** — the Flag wording is the reviewer's to fix at merge.

### Review round 2 — PR #37 `batch_014`: **DECISION: MERGE** ✅ (2026-09-11), squash `af11117`
Gates: `paths ✓ · merge ✓ · check ✓ · figures ✓ · rows ✓ · banks ✓ · dupes ✓ · glossary ✓ · structure ✓`.
**Findings: none.** Reviewed by a **fresh** reviewer that inherited nothing — every gate re-run from
primary sources on `727146b`. Tree gated per §AK6 with no working tree: `merge-tree --write-tree` onto
`737eb05` → `070a69c`. ⚠️ **The integration head moved mid-review** (`737eb05` → `441efab`, PR #39's
HANDOFF-only rework commit); the reviewer **re-ran the merge and `check` gates against `441efab`**
(tree `1799fb9`, exit 0, "All checks passed") and confirmed the unit file byte-identical in both trees.
Integration commit: glossary **§55** (read at commit time, not reserved), FLAGS **§AQ**, eleven §9
PROVISIONAL rows struck as exhausted.

**All four round-1 findings verified applied**, at **zero added tags** (global tag multiset identical
between `db7f126` and `727146b`) and −2 bytes net. `ｋｅｅｎ` **0** in the unit; `ｃｏｉｎ` **0 in the unit
and 0 across all of `tl/`**, so the wave-11 reservation is real and unspent.

⭐ **THE GATE-BLIND CLASS IS NOW CLEAN CORPUS-WIDE, NOT JUST IN THIS UNIT.** The reviewer read
`rowcheck.py:_script_cols` directly to confirm only `{FFEC}{=00}{=00}`/`{FC00}{=0000}` expand (to 7)
and every other insert strips to **0 columns**, then hand-measured **every** gate-blind row: all **9**
in this unit at exactly **insert+8**, and across all `tl/script/*.tsv` **51 rows, none over §V1's bound
of 8** (+1 ×11, +5 ×1, +7 ×1, +8 ×38). **Price rows alone: 27, reading 7×1 / 8×26 — the translator's
claim, confirmed exactly.**

⭐ **THE TRAILING-SEGMENT MOVE WAS VERIFIED ON ALL FOUR GROUNDS, INDEPENDENTLY.** §45.2 read verbatim ·
**`.TTT` measured at 9 in `script_dump.txt`** (§45.2's own table lists no `.TTT` row, so this needed
measuring) · **`{FFF8}` shares a segment with readable text 19× in the script dump, and DATA 1423 does
it on the exact `{FFF8}{=00}{=14}` variant** · no `{FFFE}` spent. The reviewer's page-shape model
**reproduces §45.2's battle census exactly** (TTTT 389, TTT. 276, TT 262, .TTTT 182, .TTT. 132,
TTT 115, TT. 98, .TTTT. 0), which is what licenses the new figure. Full audit: 10 pages changed shape,
**every one attested, 0 over 4 text rows**.

⚠️ **A SCOPE NOTE ON §45.2, so the figure is not quoted wider than it holds:** its "`.TTTT.` has 0
occurrences" is a **battle-dump** census and is correct there; the **script** dump has **1**. Nothing
in this unit produces that shape.

**Rulings given (all requested by the PR):** (a) `素材` → `ｓｔｕｆｆ` **approved but SENSE-SPLIT**, with
**D289 explicitly NOT BOUND** — the "21-bank reach" is that one untranslated armour line, while D737/738/740
are each count 1 in bank 19 alone; (b) **D724's §2.1 compression RATIFIED** at glossary §55.3 with reasons
rather than by inheritance — `只今` is carried by "in progress", only `開発` is dropped, nothing
sentence/turn/plot-bearing goes, and the literal alternatives are worse in register or cost; it does not
reach the "must change" test. FLAGS §AQ4 carries it for a human with the disc; (c) **D719's developer note
stays translated in place** (FLAGS §AQ3 — a project-policy question for a human, not a translation call).

**Report-only, applied by the reviewer at merge — the translator did NOT re-push for any of them:**
three PR-body glossary keys corrected to the source (`ボネット平原`, `隠れ家`, `能力値` — **the §9 seeds
were right and the PR table drifted**); the **`参考になる` row STRUCK, not reworded** (D745 ships
`Ｉ　ｌｅａｒｎ　ｍｕｃｈ　ｆｒｏｍ　ｉｔ．` and `ａｃｃｏｕｎｔ` is ×0 — the row described a rendering the file does
not contain); Flag 10's gutter census settled at **20 → 20 true gutters, zero lost, plus 8 separate
insert word-spaces (6 price, 2 player-name)**, superseding both earlier figures.

⚠️ **NO FIGURE ERROR THIS ROUND — the 5,594/5,596 gap is DEFINITIONAL and both are right.**
**Text growth = 2 × (EN − JP readable chars) = 5,594.** **Bank delta = text growth + 2 per added
`{FFFE}` = 5,596**, and the *measured* bank delta is 5,596 (+1,860 / +2,724 / +1,012 against a real
baseline of 10,333 / 10,527 / 29,489). They close exactly. Recorded as convention 2 of three in
FLAGS §AQ7, beside DATA-vs-FILE and gutters-vs-insert-spaces.

**Three counts where the reviewer's figure and the PR's differ, both printed rather than adjudicated:**
text rows **348 vs 346** (the PR body is round 1's; the two trailing-segment fills added exactly 2 rows,
so they reconcile — widest **23**, **0 at 24** in both) · glossary keys **1,172 / 64 occurring vs
2,342 / 145** (key-splitting granularity) · item-name pairs **38 with 3 divergences vs 43 with 1** —
and both agree **0 divergences involve this unit**.

**One qualifier on round 1's `鋭い` census, both figures right to their own question:** `鋭い` is
**5 unique lines / 105 instances** — correct — but only **3 of the 5 render `ｋｅｅｎ`** (D36, D165, D169);
D75 and D79 render `ｓｈａｒｐ`. The finding held either way and is applied.

⚠️ **NEW §4.3 DEBT IN MERGED WORK, found by the reviewer's cross-file item-name gate, none of it this
unit's** (FLAGS §AQ5): `batch_007`'s `編成` renders **both** `Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ` and `Ｆｏｒｍａｔｉｏｎ`
— **the real one, needs a ruling**; `batch_012`'s `獅子の勲章` shows the same `{FFFE}`-split shape as
`batch_013`'s §53.1-ratified `北風のシロップ` and likely needs confirming, not fixing. ✅ **`batch_006`'s
`どの品を` will/would split is NOT debt** — it tracks the source's own politeness, and `batch_014` D735
correctly took `ｗｉｌｌ` for the plain `売ってくれるんだい`.

⚠️ **INFRASTRUCTURE FLAG NOW IN `FLAGS.md` §AQ1 — every future reviewer inherits it.** GitHub refuses
`REQUEST_CHANGES` in this single-account repo, so **the decision is a COMMENT review whose FIRST LINE is
`DECISION: …`**, and **an absent `REQUEST_CHANGES` must never be read as approval, nor an absent
`APPROVE` as a block** — the review state carries no information here.

### Review round 1 — PR #39 `batch_015`: **DECISION: CHANGES** (2026-09-11)
Gates: `paths ✓ · merge ✓ · check ✓ · figures ✓ · rows ✓ · banks ✓ · dupes ✓ · glossary ✗ · structure ✓`.
Tree gated: `merge-tree --write-tree` of `tl/script-015` onto `723c7da` → tree **`96a9e33`**, reproduced by
the real merge. **Every headline figure reproduced exactly**, including the bank delta re-derived by the
PR's own move-out/move-back method (29,489 → 22,319 = 7,170 B). Not merged; **no integration commit**.
✅ **The price-insert gate-blind class is ABSENT here — checked, not assumed:** the unit's only `{FFEC}`
form is `{FFEC}{=00}{=00}` (D770, the name insert, counted at 7); `{=00}{=01}/{=02}/{=03}` and `{FC00}`
are all absent, and `５０００ジュエル` / `２０ジュエル` are literal text. **No row is bounded rather than measured.**

**Three findings, all zero- or negative-byte, no re-flow. Sent verbatim to the same translator (round 1 of 3).**
1. **D807 `Ｈｍｍｍ` forks a form the corpus has already unified.** ✅ **Verified here, and the evidence is
   STRONGER than the review states: six shipped instances across four kana spellings** — `ふーむ`
   (`batch_005`, `batch_009`), `うーん` (**`batch_007`**, `batch_013`), `ん〜` (`batch_013` ×2) — **all
   `Ｈｍｍ`.** The reviewer cited five and missed the `batch_007` one. §38.3's row governs kana spellings
   of this grunt directly, so the ruling does not depend on the bank co-occurrence I raised in dispatch.
   The unit itself already ships `Ｈｍｍ，` for `うーん、` at D813 — **only the katakana spelling was forked.**
2. **D793 `Ｗａｓｔｅｄ` → `ｗａｓｔｅｄ`** — sole outlier of 32 comma-terminated rows; zero bytes.
3. **D792 `はあ、` unrendered** against Flag 15's "nothing else is dropped"; no incumbent exists, so a
   declared §2.1 departure discharges it.

**The four rulings it was asked for:** (a) **collapse** `フーム` → `Ｈｍｍ`; (b) D770's unquoted capitals
**ratified** — §12 converts *the source's own* brackets, and §9's `“ヘルグレイブ”` row states the mirror
principle; (c) **`ｇｈｏｓｔｓ` is right**; (d) Flag 7's two in-bank pairs **confirmed** — flagging rather
than forking was correct, and §29.4's reserve does not fire.

⚠️ **MY NINTH FIGURE ERROR — the §9 seed `幽霊` → `ｇｈｏｓｔ` (5) was simply the wrong entry.** ✅ Verified:
merged **`batch_008` already ships `ｇｈｏｓｔｓ　ｗａｌｋ　ｓｏｕｔｈ　ｏｆ　Ｋｉｅｓａ` for the same rumour.** The
translator deviated from my seed and was right; the reviewer confirmed it on stronger grounds than
either of us gave. **Corrected in `glossary.md` §9.** This is the second time this wave a translator has
been right against my seed (`バウアーの砦` was the first).

⭐ **The reviewer printed BOTH text-run counts rather than asserting either wrong** — it counts 372 runs
/ 352 ≤ 23 against the PR's 373 / 353, a splitter difference at D794; both give 94.6% and widest /
at-24 / over-24 agree exactly. **That is the discipline this run keeps failing at, done right.**
It also confirmed every dispatch correction I gave it, including that **§37.1's off-by-one is a
0-based/1-based convention mismatch, not an invented error** — the same shape as the DATA-vs-FILE
mismatch on PR #37. **Record it as a convention, never as someone's mistake.**

### Rework round 1 — PR #39 `batch_015`: **all three findings applied, pushed as `3d60879`** (2026-09-11)
Gates re-run on the pushed file: `check` passes · `merge` 0 unmatched · `bankmeasure` bank 20 free
**22,311** · `rowcheck script` clean · gate 6 0 of 56 keys recur, 0 internal duplicates · gate 8 0
problems. EN 6,742 → **6,746** chars, growth **+7,178 B** (−2 finding 1, 0 finding 2, **+10 finding 3**).
Runs at 24: 20 → **21**; ≤ 23: **352 of 373**.

⭐ **THE TRANSLATOR BEAT BOTH OF US ON FINDING 1's EVIDENCE, AND FOUND THE FACT THAT ACTUALLY SETTLES IT.**
I gave six shipped instances; the reviewer gave five. **It found eight**, by pairing the battle dump's
Japanese with `tl/battle/` English (`chunk_008`, `chunk_026`) — a census neither of us ran, since battle
`tl/` holds no Japanese and a naive grep there is a null check.
✅ **And the decisive fact, verified here: `batch_013` ALREADY SHIPS `ん〜` (DATA 925, 948) AND `うーん`
(DATA 940) IN THE SAME BANK — bank 29 — all as `Ｈｍｍ，`.** That is the exact shape of this unit's bank 20
(`フーム` D807 + `うーん` D813). **So its own §25.3 objection is answered by MERGED PRECEDENT, not merely by
§38.3's authority** — which is a much better answer than either the reviewer or I gave it.

⚠️ **A MERGED GLOSSARY ROW IS STALE AND WANTS FIXING AT #39's INTEGRATION COMMIT (reviewer's, not mine —
§4 step 2 makes seeding my only glossary write).** `glossary.md:2217`, the `うーん、` row, justifies itself
with *"§25.3's test is met: `ふーむ` is in script bank 31, `うーん` in battle chunk 8."* ✅ **Both banks are
wrong:** `ふーむ` ships in banks **30** (`batch_005` D988) and **11** (`batch_009` D581); `うーん` ships in
banks **2** (`batch_007` D425) and **29** (`batch_013` D940). **The ruling stands — the stated reason for it
does not.** This is the third stale-or-mismatched citation found in the merged record this wave.

⚠️ **MY TENTH ERROR, small and mine alone:** I wrote "six shipped instances across **four** kana spellings".
The six is right; the spellings are **three** (`ふーむ`, `うーん`, `ん〜`) — I counted the untranslated `フーム`
as a fourth. **Counting the thing you are about to translate as evidence that it is already settled is
circular, and it is the same shape as the phantom `生き返りの仙人` seed earlier this wave.**

**Finding 3 was applied by RENDERING rather than declaring, deliberately**, and the reasoning is sound:
`はあ、` is now carried in register by `ｅｖｅｒ` (+10 B, page stays 4 rows, no `{FFFE}` added), because
declaring a drop here while §2-carrying `いや、` at D765/D793 would have left the unit internally
inconsistent. An `Ａｈ`-form was measured and rejected — `Ａｈｈ，` is `ああ、` (D814) and `Ａｈ！` is `あっ！`
(D810), **both already in bank 20**. **Reviewer: reverting to a plain declaration is a one-word change if
you prefer it.** It also asks that **Flag 15 be STRUCK from the PR body at integration, not amended** —
"nothing else is dropped" was the error the reviewer caught, and is only true now because D792 was fixed.
The one remaining declared elision is D812's page-1 `らしい`.

**Splitter disagreement: closed, no action.** After the rework the ≤ 23 counts coincide at 352, but that is
arithmetic coincidence (D792's second row moved 19 → 24); the totals still differ 373 vs 372 on the D794
definitional difference. Both sides agree it needs no action.

### Review round 2 — PR #39 `batch_015`: **DECISION: MERGE** (2026-09-11) — squash `8f66547`
A **fresh** reviewer; every gate re-run on `3d60879`, nothing inherited. Tree gated:
`merge-tree --write-tree` onto the **current** head `8bb3b04` → `4994075`, reproduced by a real merge,
so `batch_014` was in the tree and **gate 6 ran against the post-#37 duplicate surface**.
`paths ✓ merge ✓ check ✓ figures ✓ rows ✓ banks ✓ dupes ✓ glossary ✓ structure ✓`.
Gate 7 row-first: **1,248** glossary rows with a JP key enumerated, **116** occur, all adjudicated.
All three round-1 findings verified applied. Integration commit below. **Glossary §56, FLAGS §AR + §F2a.**

**Figures corrected — the PR body was never refreshed after the rework and still shows round 1's.**
Measured: EN **6,746**, growth **+7,178 B**, bank 20 **28,477 → 21,299** (the round-1 pair 29,489 → 22,319
is pre-#37). Chain: pre-wave 29,489 → after `batch_014` **28,477** → after `batch_015` **21,299**.
⚠️ **Its Glossary-additions table still tables `フーム` → `Ｈｍｍｍ`, the form round 2 removed** — integrated
as `Ｈｍｍ`. *Integrate from the file and your own measurements, never from a reworked PR's tables.*

**Rulings:** `フーム` → `Ｈｍｍ` (settled by `batch_013`'s merged same-bank precedent, verified) · bare
`極上のワイン` → capitals without quotes · `幽霊` → `ｇｈｏｓｔｓ` · the two in-bank pairs → flag, don't fork ·
**D792's `はあ、` stays CARRIED by `ｅｖｅｒ`, not declared** (verified `Ａｈｈ，` D814 and `Ａｈ！` D810 are both
spent in bank 20, so §25.3 really does forbid an `Ａｈ`-form) · `シロン様` → `Ｍａｓｔｅｒ　Ｓｈｉｒｏｎ` ·
**Flag 15 struck**, as asked. `反乱` → `ｒｅｂｅｌｌｉｏｎ` at D786 confirmed **mandatory**: §37.1's scope note
names DATA 785 (0-based) as a script line that must take §38.3's form.

⚠️ **Recorded, NOT sent back: 21 runs at exactly 24 columns.** Corpus norm measured across every shipped
batch is **5 in 3,923** (`batch_001` 3, `batch_009` 2, all twelve others **0**); `batch_014` shipped **0 of
348** at a comparable ratio. §3.2 asks for ≤ 23 so a later one-character fix needs no re-flow. Nothing
exceeds 24 and bank 20 has 21,299 free, so a 21-row re-flow at round 2 of 3 would risk verified text for a
preference. **FLAGS §AR3. Future units in this chapter should hold to 23.**

⚠️ **Two record corrections for the coordinator.** (a) **HANDOFF's `batch_014` bank-20 figures are wrong**:
it lands at **28,477**, not 28,469, and its share is **1,012 B**, not 1,259 — so combined wave demand on
bank 20 is **8,190 B**, not 8,429. No conclusion changes. (b) ⚠️ **Your `glossary.md:2217` correction was
itself incomplete — §AI6's shape a third time.** Re-measured: `ふーむ` is in banks **11, 30, 33** (you omit
33); `うーん` is in banks **2, 20, 29, 40** and battle chunks **8 AND 26** (you omit 20, 40 and chunk 26);
and **the row's "battle chunk 8" claim is TRUE**, not wrong — only the `ふーむ` half was. Corrected in place
with the full census; the ruling never depended on it.

⚠️ **`親衛隊` row STAYS LIVE and its last instance is unshippable.** D1330 is in **bank 40, 75 bytes free**;
the line needs ~190 B. Recorded as **FLAGS §F2a** — bank 40, not §B, is where a bank blocker belongs
(§B is tier-A battle ratios). ⚠️ **F2's own table says bank 40 has 1,771 free; that is August's figure and
is stale — it is 75.** Do not dispatch D1330 to a translator; it needs the `MAIN1.EXE` repoint.

## Next up — WAVE 11 (⚠️ still script-only unless a human clears Blocked 0 / 0a)
**Re-derive it. Do not inherit this table** — bank figures move with every merge, and the line
counts below were measured before wave 10 merged anything.

After wave 10, **~627 lines / ~3,035 instances remain untranslated; ~264 lines stay bank-feasible.**
Contiguous feasible runs, measured 2026-09-11 by `bankmeasure` + a per-run growth model at 2.10×:

| DATA | Lines | Banks | What it is |
|---|---|---|---|
| **870–879** | 10 | 25 | ⭐ **the blacksmith (`かじ屋`, `ノロ` verbal tic) — take this FIRST.** See the cross-wave duplicate warning below. |
| 1106–1159 | ~54 | 31–39 | real dialogue — ⚠️ **1043–1105 immediately before it is a DEVELOPER DEBUG MENU; do not batch them together** |
| 1415–1430 | 16 | 43 | casino: slots, medal exchange, prizes — player-facing |
| 584–598 | 15 | 12 | leftovers, good for topping a batch to 40–60 |
| 997–1034 | 38 | 30 | ⚠️ debug flag/sound test — near-zero player value |
| 465–469 | 5 | 3 | leftovers |

⚠️ **NOT shippable:** DATA **518, 519, 520** — 6,389 B of growth against bank 5's 1,135 spendable.
These three alone are why bank 5 shows as over budget. ⚠️ DATA **326–345** pays its growth in
**18 banks for 38 instances**. ⚠️ **1043–1413 as a whole run is bank-blocked** by banks 40/41; only
sub-ranges are feasible, so slice it rather than testing it whole.

⚠️ **CROSS-WAVE DUPLICATE DEBT — wave 10 ships the incumbents these four inherit.** Measured this
wave by longest-common-substring against DATA 707–869:
`870`↔`724` share **`貼り紙がしてある・・・`** (11 chars) · `874`,`877`↔`711` share
**`か？　はい　いいえ`** (9) · `879`↔`744` share **`の材料になりそうなもの`** (11).
**None is byte-identical, so gate 6 cannot see any of them.** Whoever takes 870–879 must read
`batch_014` first and match it.

**A corrections unit is still worth a slot.** §4.3 debt in **merged** work, all byte-negative or
free: **FLAGS §AP5** — `chunk_000.txt` ships three hyphen stutters against §23.2's comma convention
(census **19 : 3**); **§AP7** — `品` → `ｇｏｏｄｓ` at DATA 376 against §34.1's `ａｒｔｉｃｌｅ`,
+6 B into a bank with 31,431 free; **§AP9** — a stale §9 `トリフ` row four merged units already
render, `batch_007.tsv:31`'s `Ｈｏｂｂｉｔｓ　ｄｏ　ｎｏｔ`, and merged `chunk_000` ×3, `chunk_008`,
`chunk_031` shipping `Ｈｅｙ，` against §32.3's `Ｏｉ，`.

## Remaining
**Battle: 0 dispatchable.** 8 chunks remain, **all blocked** — 15, 23, 27, 28, 29, 39 by §D1's dump
artifact; **16 and 32 by BOTH §D1 and the tier-A floor** (1.59× and 1.61× against §B2's 1.64×).
⚠️ **`queue.py battle` reports "dispatchable 11" and is WRONG ON BOTH COUNTS** — its tier-A cutoff is
hardcoded **1.6**, and it knows **nothing** about §D1.

**Script: 790 unique lines / 3,198 instances untranslated at wave 10's start** — re-derived this
wave from `script_unique.txt` + `script_dump.txt` + `bankmeasure`, and it reproduces wave 9's close
figure exactly. Of those, **~427 lines are bank-feasible**; **wave 10 takes 163 of them**, leaving
**~264 feasible lines, roughly 5–6 batches**. CLAUDE.md §8's "no dispatchable unit left" does
**NOT** hold; the run continues. The other ~363 lines (2,748 instances) are bank-blocked, **117 of
them 21-instance item-table rows held solely by bank 40's 75 free bytes**.

⚠️ **Two figures in wave 9's closing table did not survive re-measurement, and the table said to
re-measure.** It listed DATA 707–879 as **170 lines / ~18,183 B**; the range is **173 lines**
(707–879 inclusive is 173 slots and **none** of them is translated) and its growth at the standing
**2.10×** planning ratio is **23,985 B**. The line count is arithmetic and certain; the byte figure
differs because 18,183 B is not what 2.10× yields for 10,443 JP chars (2×1.10×10,443 = 22,974 plus
row breaks). Recorded as data, not as a complaint: **both figures were labelled "a starting point,
not a queue", and re-deriving them is what that label asks for.**

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
   chunks — and `riotscript` alongside it, since it is the same three-line change.** The dumper prefers a Shift-JIS text run over a control tag whenever an argument byte
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
⚠️ **RULINGS LIVE IN THEIR HOMES, NOT HERE** — `glossary.md` §23–**§51** plus the **§9 PROVISIONAL**
seed tables, `FLAGS.md` §K–**§AM**, `findings.md` §24, `pending/README.md`. Section numbers are
taken by **READING both files at commit time**, never reserved.

**Standing (waves 4–9).** Integration branch is `claude/workflow-translation-iterate-uzlkns`; `main`
untouched. Script growth for planning **2.10×** (realised 2.118 over 408 lines). Seed the glossary
**before** dispatching. A **parked unit still gets the full reading review**. Name script batches by
**DATA line list**, never a `queue.py` position. A term is "in the glossary" only if a row **fixes an
English form**. A glossary row's **Alt column records REJECTED options**. `{FCC0}` is forbidden by
`assemble.py:tag_parity`, **not** by `rowcheck.py` (§Q2 — never patch it, never a finding).

**⚠️ WAVE 9's OWN FINDING — MY DISPATCH TABLE PRODUCED A FALSE POSITIVE. Carry this into every
future dispatch.** I gave all three translators a "shipped clause" table built by splitting shipped
pairs on `{FFFE}`/`{FCC0}`/`{FC30}`/`{FC51}`/`{FC50}` and aligning clauses **positionally**. On
`いらっしゃいませ！！` it asserted a corpus distinction (`Ｃｏｍｅ　ｉｎ！！` vs `Ｗｅｌｃｏｍｅ！`) that
**does not exist**. `batch_011`'s translator rejected it by reading; PR #34's reviewer then proved
it independently: the form occurs **twice in the whole corpus** — bank 16 (this unit) and bank 26
(`batch_010` D885) — and D885 is exactly the message §34.5's **reserve** covers, licensed only
because `カジノへ　ようこそ！` sits on the adjacent row. **The table learned a rule from a sample of
one, and the real conditioning variable was the bank.** The cause is **generic**: positional
alignment infers a rule from whichever instances happen to be translated, and a term whose only
shipped instance sits under a documented reserve will look like a fixed distinction.
✅ **The mitigation worked** — every dispatch labelled the table "a LEAD TO VERIFY BY READING, never
a ruling", and that is exactly what the translator did. **Keep that framing, and additionally mark
any row backed by a SINGLE shipped instance as such.**

⭐ **WAVE 9's BEST PROCESS ARTIFACT — A NEW GATE THAT CLOSES A REAL HOLE IN GATE 6. Put it in
every future dispatch.** Gate 6 pairs whole messages on exact Japanese, so **two units coining
different English for the same `『…』` item name are structurally invisible to it** — which is
exactly how `『進化の木の実』` shipped as `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”` in `batch_011` and
`“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”` in `batch_013`, caught only by a reviewer **after the first had merged**.
`batch_013` then built the missing check: **pair every `『…』` in a message with the `“…”` spans in
that same message, and compare those pairings ACROSS FILES.** On its own unit: 17 names, 4 shared
with other files, 0 divergences. **Cheap, mechanical, and it would have caught this before delivery.**

⚠️ **GATE 8's "`{FFFF}` last on every message" IS A BATTLE-STORE RULE AND DOES NOT APPLY TO SCRIPT
UNITS** — my dispatches mis-scoped it onto all three. Verified: `dumps/script_unique.txt` contains
**0** `{FFFF}` (the dump has 8,760; the unique keys omit the trailing one, per CLAUDE.md §4 step 1),
and `batch_003`/`004`/`005` each carry the line *"Japanese keys are copied byte-for-byte from
script_unique.txt, i.e. without `{FFFF}`"* — **the repo documents this in three places.** PR #35's
reviewer caught it as its own instrument being wrong and said so rather than reporting a failure.

⚠️ **WAVE 9's SEVEN WRONG FIGURES — THE FULL TALLY, WITH ATTRIBUTION, EACH VERIFIED BY ME.**
Recorded because a later summary of this run attributed them **4 translators / 3 reviewers**, and
that is not what the record shows. The verified breakdown is **1 coordinator, 2 translators,
4 reviewers**:
| # | Figure | Source | Caught by |
|---|---|---|---|
| 1 | the `いらっしゃいませ！！` clause-alignment table (a rule inferred from a sample of one) | **coordinator (mine)** | the translator, by reading |
| 2 | `バニシュジュエル` 13 / 15 (true: **12 / 14**) | translator | coordinator |
| 3 | the `ベルナール教会` "promotion" — a row that was never provisional | **reviewer** | the translator, by declining |
| 4 | `こおりのゆびわ` "corrected" 10 → 12 (true: **10**) | translator | coordinator |
| 5 | the `で、` census run with a "starts with" matcher, returning the opposite of the truth | **reviewer** | itself, by re-censusing whole rows |
| 6 | net "+4 bytes" (true: **+2**) | **reviewer** | the translator |
| 7 | the stutter census "21 : 0" (true: **19 : 3**) | **reviewer** | the translator, by reading all 45 hits |
⚠️ **The source shifted across the wave: the early errors were translators', the last three were
reviewers'.** **Quality control here is NOT one-directional, and review dispatches must stop
implying it is.** A reviewer's finding is not privileged over a translator's evidence — #3 would have
written a fabricated entry into `glossary.md` had the translator complied instead of checking.

⚠️ **ALL SEVEN SHARE ONE SHAPE: someone measured ONE SIDE of a comparison and inferred the other.**
The clause table measured shipped English without counting how many instances backed it; the `で、`
census matched one way; the `バニシュジュエル` fix re-measured the source but not the replacement;
the `こおりのゆびわ` fix re-measured the value it corrected *from*, not *to*. **The operational rule
is mechanical, not a counsel of care: `len()` BOTH values and PRINT BOTH before asserting either is
wrong.** I hand-counted `Ｌｅｃｔｕｒｅ` as 8 letters (it is 7) while checking a translator's figure,
and only measuring stopped an eighth error being mine.

**Method findings (wave 8, still binding — these are what the dispatches carry).**
- ⚠️ **GATE 7 RUNS FROM THE GLOSSARY SIDE, KEY BY KEY**, with controls in **both** directions.
  **5-for-5** at catching what every other gate passed; **three units failed on a glossary row whose
  own census NAMES THE EXACT LINE**. Require the **key count** as evidence — "no findings" is not
  evidence. ⚠️ **It cannot surface a word the glossary never recorded** (how `くそ` survived twice).
- ⚠️ **§AG6's MIRROR: "I measured the rejected alternative and never looked for the incumbent."**
  Before reaching for a new word, **search for the English the SOURCE WORD already has**. Wave 9's
  seeding hit this twice: `ウエイト` already ships as `Ｗａｉｔ　ｔｉｍｅ` in `chunk_000`, and a drafted
  `素早さ` → `Ａｇｉｌｉｔｙ` would have contradicted **five shipped class rows** reading `ｓｐｅｅｄ` /
  `ｓｗｉｆｔ`. Both were caught before commit; the row was dropped.
- ⚠️ **GATE 6 PAIRS WHOLE MESSAGES AND MATCHES EXACT JAPANESE.** A unique row string or a kana
  variant (`クソッ`/`くそっ`) is **structurally invisible** to it. **A clean gate 6 is not evidence of
  terminology consistency.** Plant controls **inside** the checker's coverage set and **state the
  coverage**. Battle `tl/` holds no Japanese (grep is a null check); **script TSVs keep Japanese in
  column 2, so a column-2 comparison IS valid there.**
- ⚠️ **MEASURE THE REJECTED OPTION IN MORE THAN ONE WORD ORDER.** Two false impossibilities in wave
  8; the first nearly parked a shippable unit. **An order-independent PACKING proof beats
  enumeration, and A TOTAL NEVER RESCUES A PACKING CLAIM.** §AG6 covers the PR body's own prose too.
- ⚠️ **VERIFY CORRECTIONS IN BOTH DIRECTIONS — a wrong correction enters the record as fact.** Five
  in wave 8. The traps that fired: a **numbering convention** (DATA vs FILE, twice); a **correction
  note** (a record documenting its own former error reads as though it still contains it);
  **re-asserting a round-1 reading after the base moved**; and **a shape census quoted without its
  corpus** — a census needs its **SPLITTER *and* its DUMP**.
- **INFRASTRUCTURE (§AK6): worktree branch names are NOT per-agent and collide.** ✅ **No gate needs
  a working tree:** `git merge-tree --write-tree` for gate 2, a `git archive` extraction for the
  rest, `commit-tree` with a temporary index for integration. **Say which tree you gated and how.**
- **Never infer merge state from an agent's status.** A reviewer can merge *and* push `integrate:`
  while still showing "running"; one killed mid-run leaves **no trace in git**. A rejected
  non-fast-forward push is the mid-integration signal: **hold, re-export, re-apply, push — never
  force.** (Hit once in wave 9, on the seed commit: wave 8's coordinator had pushed a HANDOFF line
  after opening this session. Rebased, verified only `glossary.md` moved, pushed.)

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
