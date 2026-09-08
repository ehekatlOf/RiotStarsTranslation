# HANDOFF — live board for the Riot Stars translation

Read this first. Update it after every step (rules: `CLAUDE.md` §7). A fresh session resumes
from this file plus the open PR list; nothing else is required.

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
> **Wave 2 is IN FLIGHT. Its session — `session_01JDoA8KzwUVk3ZjiBw8Qkf3`, "Riot Stars — wave 2" —
> owns the repository and is the active driver. Preflight passed 2026-09-08: `check` green, zero
> open PRs, zero stale worktrees.**
>
> The literal next act is: **dispatch the reviewer for PR #7 (battle chunk 6), in the foreground,
> one at a time.** The barrier is met and **#6 (chunk 4) is MERGED** — squash `e08bee8`,
> integration commit on this branch. Remaining review order: **#7 → #5 → #8**. Pull
> `--ff-only` before dispatching (this integration commit is already pushed), and pass the
> reviewer the five rulings listed under **In flight** — `しかし` in particular binds #7 and #5.
>
> Wave 2 has `Task`: it is running the proper three-role split (translator / reviewer subagents),
> so wave 1's spawn constraint below does **not** apply to it.
>
> **When wave 2 closes it opens wave 3's session itself** (SKILL.md §6a; `create_session` needs
> **both** `source_url` and `source_revision`). If this session is dead or stalled — check by
> listing open PRs against this branch and reading In flight — the chain is broken and whoever
> notices should re-open the wave. The chain ends only on one of CLAUDE.md §8's four conditions.

## Last updated
2026-09-08 · by: **the PR #6 reviewer** (integration commit) ·
wave: **2 IN REVIEW — 4 units, 4 PRs open, 1 MERGED (#6, chunk 4)** ·
queue: **fresh (survey ran 2026-09-08)**

## Progress (`python3 tools/assemble.py status`)
| | Done | Total | |
|---|---|---|---|
| Battle chunks | 14 | 44 | 0, **1**, **2**, **3**, **4**, 7, 10, 11, 12, 14, 33, 34, 35, 40 |
| Battle JP characters | 9,426 | 43,161 | **21.8%** |
| Script unique lines | 185 | 1,430 | `tl/script/batch_001–004.tsv` |
| Script message instances | 4,013 | 7,931 | **50.6%** |

`check`: **All checks passed** on the integration branch. Tightest banks (`bankmeasure`, measured
after batch 004): **41 → 353 free, 40 → 509, 5 → 3,419**, 2 → 7,543, 33 → 9,353; every other bank
≥ 10,300. Bank 40 is spent — see `FLAGS.md` §J2.

## In flight — WAVE 2, dispatched 2026-09-08

Four translators, all `run_in_background`, each in its own worktree, branching from
`claude/workflow-translation-iterate-uzlkns`. **Wave barrier: review nothing until all four have
an open PR.** Review order when the barrier is met: chunk 4 → chunk 6 → chunk 9 → script 005.

| Unit | Branch | Tier / budget | Round | PR | State |
|---|---|---|---|---|---|
| battle chunk 4 | `tl/battle-004` | D, 734 JP ch, ratio 5.08 | 1 | **#6** | ✅ **MERGED round 1** — squash `e08bee8`, integrated by the commit that carries this row. 3,849 / 8,192, **4,343 slack**, widest row 23 col, **tag stream byte-identical on all 25 lines including every `{FFFE}` — the first zero-re-flow unit in the project**. All 8 gates green, no findings. Rulings: `辺境`→frontier, `そうそう。`→`Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`, `しかし`→`Ｈｏｗｅｖｅｒ，`, `助かった` pinned, `ファリーナ` moved. Nothing left on this unit |
| battle chunk 6 | `tl/battle-006` | C, 1,165 JP ch, ratio 3.09 | **2** | **#7** | 🔄 **CHANGES round 1, rework sent 16:20Z** — 5,897 / 8,192, 2,295 slack. Seven gates green; **gate 7 (glossary) failed** because `4899c93` added §23 *after* this PR was drafted, and §23.1 / §23.3 name chunk 6's own lines. Six findings, all ≤ 23 col replacements. Reviewer ratified `弓使い`→`ｂｏｗｍａｎ`, `ナコール様`→`Ｆａｔｈｅｒ　Ｎａｃｏｌ`, `ま、待て！`→`Ｗ，　Ｗａｉｔ！`; cleared Flag 14; queued `{FC03}` for `findings.md` at merge |
| battle chunk 9 | `tl/battle-009` | D, 760 JP ch, ratio 4.93 | 1 | **#5** | **PR open** — 3,971 / 8,192, **4,221 slack**, widest row 23 col, `{FFFE}` +1 on lines 8 and 9 (both flagged) |
| script batch 005 | `tl/script-005` | 26 lines / 26 inst, **1,980** JP ch | 1 | **#8** | **PR open** — 4,036 B across banks 29/30/31 → 25,597 / 35,103 / 34,839 free; ratio 2.02×; widest row 23 col |

**BARRIER MET at 15:15Z — 4 of 4. REVIEW IN PROGRESS: 1 of 4 done.** PRs: chunk 4 **#6 ✅ MERGED**,
chunk 6 **#7**, chunk 9 **#5**, script 005 **#8**. Review order, one reviewer at a time,
foreground: ~~#6~~ → **#7 next** → #5 → #8. HANDOFF is pushed before each reviewer and pulled
after it.

**⚠️ RULINGS FROM #6's REVIEW THAT BIND THE REMAINING THREE — do not re-decide these:**
- **`しかし` / `しかしながら` → `Ｈｏｗｅｖｅｒ，`** (glossary §23.3). Chunk 4 had none; **#7 has 1
  and #5 has 2.** `Ｂｕｔ，` is taken by `でも` (shipped chunks 7 and 4); `Ｓｔｉｌｌ，` is §19.1's
  fixed form for `それにしても` (shipped chunks 1 ×2, 2 ×1). Chunk 0's `はっ、しかし・・・` →
  `Ｓｉｒ，　ｂｕｔ．．．` is phrase-level and is **not** an outlier — leave it.
- **`助かった` → passive `Ｉ／Ｗｅ　ａｍ／ａｒｅ　ｓａｖｅｄ` by default**, active `Ｙｏｕ　ｓａｖｅｄ　…`
  only where the source turns to address the rescuer (glossary §23.4).
- **`ファリーナ` is MOVED** — §1 → §2, done in #6's integration commit, verified against both
  dumps. **#7 and #8 must not move it again.**
- **`クリミア` is deliberately NOT moved.** #6's reviewer had no evidence for it and would not
  touch a fixed row on an unverified claim. **#5's reviewer owns that call.**
- **`辺境` → frontier** ratified, and `chunk_000.txt` is **not** re-cut (§20.4 pattern, now a
  stated rule at `FLAGS.md` §K2). Chunk 0 is effectively frozen at 27 bytes of slack.

**Cheap barrier/status check — use this, not `list_pull_requests`** (full PR bodies burn context):
`git ls-remote --heads origin 'tl/*'`.

**⚠️ A SURVEY DEFECT THIS COORDINATOR INTRODUCED, corrected by PR #8 — carries into every future
wave.** This coordinator measured batch 005 at **1,770 JP characters** using the regex
`[぀-ヿ一-鿿]`, which counts kana and kanji only. The translator's count over every non-tag
character (`re.sub(r'\{[^}]*\}','',jp)`) is **1,980** — a **210-character, 12% gap**, entirely
full-width spaces and punctuation. Those characters cost bytes and columns like any other, so the
kana/kanji-only count **under-models growth on any line with heavy spacing**. Use the non-tag
count. Worth checking whether `tools/queue.py` has the same bug; if it does, every ratio in
Remaining is optimistic.

**PR #8's other decisions for the reviewer:**
- **`将軍` → `Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ`** as instructed, settling §10.2. Note the translator's
  refinement: line 992 says bare `２軍`, not `宮廷第２軍`, so it is `２ｎｄ　Ａｒｍｙ` and **not**
  §20.1's `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ`.
- **`リース文明` ≠ `古代ハイランド`** — the §9 seed asked; the translator checked and says keep
  them distinct. Highland is a technological civilisation whose works survive and still function
  (the floating island, the sky fortress, Helfer's machines in ch.43); Reese is known only from
  documents at Farina, died `同種族の戦いによって`, and is remembered by the church. Merging them
  would invent a plot fact. **Record as a finding, do not merge the rows.**
- **Tutorial register** (Flag 10): the dispatch said match `batch_002`, but §15.3 records that
  speaker as explicitly *not* a §7 box, with light contractions; §7's じゃ rule says **no**
  contractions. The translator applied §7. ⚠️ These five boxes carry `{FB01}`, not
  `{=FA1000300030}`, so neither existing register row covers them — a new §7 row is probably
  wanted. **This is the ruling most worth the reviewer's attention.**
- **`アップミーズ` → `Ａｐｕｍｉｚｕ`** is genuinely new (5 script occurrences, none in `tl/` yet) —
  fix it now so the later four do not drift.
- Line 987 page 2 **ends mid-sentence**, predicate arriving after the `{FCC0}`; preserved because
  a translator cannot move a `{FCC0}`. Worth an in-game look beside `FLAGS.md` §D2.

**⚠️ A ruling conflict the reviewer of #7 identified and handed to #8's reviewer, with its
decision attached — do NOT let #8 settle it the other way by default.** PR #8 proposes
`バトウ様` → bare `Ｂａｔｏｕ`, honorific carried in register, on the §21.2 precedent. #7's
reviewer rules that **inconsistent**: §21.2's "dropped, carried in register" governs `〜さん` on a
personal name **only**; `様` has its own settled pattern in §1/§14.1 (Lady Rimul, Lord Helfer,
Lady Phyllis, Lady Cavia) and must not be collapsed into the `さん` rule. Chunk 6 is the one
following the glossary. #8's reviewer decides, but must decide *knowing this*.

**⚠️ A glossary defect found by #7's reviewer, to be recorded at merge:** §18.2 separates
`ほう` / `おや` / `おお` / `あ、` by punctuation, but `おお、` → `Ｏｈ，` **collides with**
`ほう、` → `Ｏｈ，`. The dumps hold 4 `ほう、`/`ほお、` against 40 `おお、`, so the four-way split
does not actually hold as written.

**Measured at dispatch (corrections to the wave-2 plan as written by wave 1):**
1. **Batch 005 spans banks 29, 30 and 31 — not 30 and 31.** Lines 984–988 (the five tutorial
   boxes) are resident in **bank 29**, 989–1001 in bank 30, 1040–1047 in bank 31. Free:
   **29 → 27,323 · 30 → 36,671 · 31 → 35,581**. All roomy; at the measured 2.10× growth the batch
   needs ~3,700 bytes spread over three banks. No bank pressure.
2. **The corrected range is confirmed clean**: 26 lines, 1,770 JP characters, 26 instances (all
   1-instance), and `grep -E 'フラグ|：新曲|^[０-９]{2}：|鑑賞モード'` over it returns **nothing**.
   The 89 debug lines are excluded as planned.
3. **No re-seeding was needed.** Every proper noun in all four units is already fixed by
   `glossary.md` — §1/§2 for the decided ones, §9 "Wave 2 seeds" for the rest. Checked all 20.

**Three cross-unit decisions routed to the translators, to be ratified by the reviewer:**
- **`ファリーナ` is a PLACE** (§1 files it under People). Chunk 6 `ファリーナの南、カペラの村`;
  script 1046–1047 `ファリーナの復興`, `ファリーナで発見された`. The rendering `Farina` is
  unchanged — only the classification is wrong. Both PRs flag it; the reviewer moves the row.
- **Fernando's title** (glossary §10 open question 2). `隊長` → captain is fixed (§2) and chunk 2
  shipped `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ`; script 992 reads `２軍のフェルナンド将軍`. Batch
  005's translator is instructed to render `将軍` → **`Ｇｅｎｅｒａｌ`** (two distinct ranks, the
  higher fitting the man who leads the 2nd Royal Army) and to flag it as settling §10.2.
- **`リオン` → `Ｌｅｏｎ`** (§9 wave-2 seed) settles **§10.1**, and also makes the stale
  "unresolved — Lion or Leon" row in §1 wrong. Chunk 6's PR flags both for the reviewer.

### ✅ DONE: the wave-1 reading-review audit — **TWO independent audits, reconciled**

`CLAUDE.md` §8, as amended in `16c179e`, required an independent post-merge reading audit of wave
1's four self-reviewed units. **Two ran, in parallel and unaware of each other** — wave 1's session
(`audits/wave-1-audit.md`) and wave 2's read-only subagent (`audits/wave1-reading-review.md`).
Duplicated effort, but a far stronger result: they cross-validate, and each caught what the other
missed. **Read both.**

**Both agree, independently: no must-fix on any translated line. The four units stand as merged.**
Nothing invented, nothing dropped, no plot fact or speaker turn lost, no verbal tic mixed, gates
green on re-run, zero unspaced `，` left in `tl/`, zero divergent duplicate JP keys across the four
script batches, no regressions from the rework rounds. They converged *independently on the same
fix* for `batch_004:12` and both caught `chunk_003`'s `しかし` → `Ｓｔｉｌｌ，` collision.

**The one contradiction, adjudicated by this coordinator against primary sources — wave 1's audit
was right, wave 2's was wrong:**
- Wave 2's auditor certified `FLAGS.md` §J1 as sound. It is not. **§J1 says the `持つ者に`
  departure was "not flagged" by PR #4. PR #4's Flag 3 flags it explicitly**, by rule and line
  number. Verified in the PR body.
- **§J1's arithmetic is wrong and it changes the conclusion.** §J1 costs the restore at 42
  bytes/entry × 6 = 252. PR #4's Flag 3 gives the one-row form as "12 bytes each instead of 44" →
  delta **32/entry = 192 bytes, not 252**. Bank 40 lands at **317 free, not negative**; the "park
  ~7 lines" claim is really ~5, or **zero** if taken against the 500-byte planning reserve — which
  is what the trade actually was. **§J1's "seven Japanese holes in a table" justification is false.**
- **`FLAGS.md` §I1 is not settled either.** Its corpus argument counts six *glossary-fixed*
  renderings as free evidence; strip them and the only two free cases (chunk 1 `“Ｗａｉｔ”`,
  chunk 3 `“ｅｎｔｅｒ”`) are same wave, same tutorial box, same position, **opposite cases**.
  Every candidate fix is 0 bytes, 0 columns. ⚠️ This binds **script batch 005**, in flight now,
  which carries `“Ｐｅｒｓｕａｄｅ”`.
- Wave 2's audit file carries this correction on its own face rather than being quietly patched.

**Unique to wave 2's audit** (wave 1's missed): `chunk_002:14` `すみません。` → `Ｗｅ　ａｒｅ
ｓｏｒｒｙ．` reads as an apology for wrongdoing where it is apologetic *thanks* — the one line a
player is likeliest to stop at; three more `batch_004` idiom/parallelism fixes; and **a live
`CLAUDE.md` §3 violation in earlier shipped work**: `村が襲われました。` (13 dump instances) is
`ｉｓ　ｕｎｄｅｒ　ａｔｔａｃｋ` in `chunk_007` but `ｈａｓ　ｂｅｅｎ　ａｔｔａｃｋｅｄ` in
`chunk_034` — **independently verified by this coordinator**. Predates wave 1. Cheap fix: change
chunk 34 (6,601 slack), not chunk 7 (399 slack).

**Unique to wave 1's audit** (wave 2's missed): the §J1 must-fix and arithmetic above; the §I1
corpus flaw; `chunk_003:16` breaks splitting `Ｒｏｙａｌ`/`Ａｒｍｙ` and `ｓａｖｅｄ`/`ｕｓ．`
(0-byte fix); and **`glossary.md` §21 dropped five entries PR #1 proposed with no note of
rejection** (`ヘビー`, `洞窟`/`赤い屋根の家`, `さあ→Ｃｏｍｅ　ｏｎ，`, bare `隊→squad`,
`謹慎中`) — all rendered in shipped work but fixed nowhere; `さあ、` recurs 26 more times.

**Who acts, and when — nothing here blocks wave 2:**
- **Doc corrections** (§J1 must-fix + arithmetic, §I1, glossary §21's five, the stale §9
  `ティミー` row) are integration work: the **reviewer** does them in its integration commits this
  wave, or they ride a housekeeping commit at wave close.
- **Line edits** (`batch_004:12`, `chunk_003:5` and `:16`, `chunk_002:14`, `chunk_001:2`, and the
  `chunk_034` §3 fix) need a translator and a PR like anything else — wave 1's audit is explicit
  that they must not be applied by whoever ordered the audit. **Queued as a wave 3 unit** (see
  Next up).
- **Three rulings are live in wave 2 right now**: `しかし` (chunk 6 ×1, chunk 9 ×2, verified),
  `助かった` (chunk 4 ×1), and §I1's quoted-UI-token case (batch 005). The **reviewer** rules on
  these under §6. This coordinator deliberately did **not** interrupt four live mid-draft
  translators to pre-empt them — `しかし` is a genuine tradeoff (chunk 3 also ships `でも` →
  `Ｂｕｔ`, and chunks 4/6/9 each carry `でも` ×2, so collapsing them is a deliberate choice;
  wave 1's audit proposes `Ｈｏｗｅｖｅｒ，` at +4 bytes to avoid both collisions) and rework
  rounds exist for exactly this.

### ⚠️ The spawn constraint — read before planning any wave

The session that ran wave 1 had **no `Task` tool** and no `ListAgents`: it could not spawn a
translator, a reviewer, or a successor orchestrator. Discovered mid-wave, when the first reviewer
dispatch was refused.

**What was done, and why.** CLAUDE.md §8 lists four stop conditions and "cannot spawn subagents"
is not one of them. So that session ran all four reviews itself under the identical §6 contract —
a real checkout, every mechanical gate executed and its output pasted into the PR review, the full
line-by-line reading against the Japanese, one PR at a time, integration commits serialised. **What
was lost is reviewer independence, not gate coverage**: the agent that routed the wave also judged
it. Recorded rather than quietly absorbed.

**If your session has `Task`, go back to the three-role split** — it is the better arrangement and
wave 2's session should use it. The wave-boundary chain does *not* depend on `Task`: it uses
`create_session` (SKILL.md §6a).

### Four tooling facts established in wave 1 — carry these into every future wave
1. **Neither `REQUEST_CHANGES` nor `APPROVE` is possible on these PRs.** GitHub refuses both on a
   PR opened by the same account (`Can not approve your own pull request`), which is every PR here.
   **Every** decision — MERGE, CHANGES, PARK — goes as a **COMMENT** review. Do not retry either.
2. **Squash-merging via the GitHub MCP works** — `merge_pull_request`, `merge_method: "squash"`,
   with `expectedHeadSha`. Put the true post-rework figure in `commit_title`: a PR title written
   before a rework is stale, and the squash title is what lands in history.
3. **The proxy blocks branch deletion** (`git push origin --delete` → HTTP 403). Normal pushes are
   unaffected. The four wave-1 branches are merged but still exist on the remote; harmless, and a
   human can delete them in the GitHub UI. **Do not treat this as the §8 "cannot push" condition.**
4. **`translation_prompt.md` §3.2's "add a `{FCC0}`" escape does not exist for a translator.**
   `assemble.py check` fails with `tag stream changed` — `tag_parity` exempts only `{FFFE}`. A
   translator at the 4-row wall has re-flow and §2.1 only.

## Next up

### WAVE 3 — one unit already queued: the audit-corrections unit
`corrections/audit-wave1` — a **translator + PR like any other unit**, because wave 1's audit is
explicit that its line edits must not be applied by whoever ordered the audit. **Seven** line
edits, all verified to fit (every proposed row ≤ 23 columns):
`batch_004:12` (+14 B/bank, both audits agree on the same fix) · **`chunk_003:5` (`しかし` →
`Ｈｏｗｅｖｅｒ，` — the PR #6 reviewer's ruling, glossary §23.3; `Ｓｔｉｌｌ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ`
→ `Ｈｏｗｅｖｅｒ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ`, **19 → 21 cols, +4 B**)** · `chunk_003:16` (0 B,
re-flow) · `chunk_002:14` (`すみません`, +16 B) · `chunk_001:2` (+2 B) · **`chunk_001:14` (NEW,
found at PR #6's review — `助かったノロ。`: `ｙｏｕ　ｓａｖｅｄ　ｕｓ，　ｎｙｏｒｏ．` →
`ｗｅ　ａｒｅ　ｓａｖｅｄ，　ｎｙｏｒｏ．`, glossary §23.4, **20 → 20 cols, 0 B**)** ·
`chunk_034:8` (the `村が襲われました。` §3 fix, −4 chars, do **not** touch `chunk_007` at 399
slack). Total bank-40 cost of the script edits: 38 B → **471 free**.
Wave 3's other units come from Remaining below.

**Also for wave 3, when the slot patch lands:** `pending/chunk_005.txt` line 32's `そうそう。` →
`Ｑｕｉｔｅ　ｓｏ．` must become `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` (**+4 cols, +8 B**) or the re-cut creates
a CLAUDE.md §3 violation against shipped `chunk_004.txt`. Recorded at `glossary.md` §23.2.

### The wave-2 queue as dispatched (kept for reference — all four are IN FLIGHT, see In flight)

**Battle: chunks 4 (D 5.08), 6 (C 3.09), 9 (D 4.93).** Chapter order, all tier C/D, no byte
pressure. Glossary seeds for all three are already in **§9, "Wave 2 seeds"** — `Ｌｅｏｎ`
(which settles §10.1), `Ｃａｐｅｌｌａ`, `Ｋａｚａｒｏｖ`, `Ｍａｒｔｉｎ`, `Ｐｅｒｃｉｖａｌ`,
`Ｄｉｅｌ` Empire, `Ｗａｒｗｉｃｋ`, 弓使い.

**⚠️ Script batch 005 — the surveyed range was wrong and is CORRECTED here.**

`Next up` previously read "unique lines 1035–1100 (66 lines, one scene, bank 31)". **It is not one
scene.** Measured line by line: of lines 984–1100, **89 are developer debug scaffolding** — a
sound-test / music-appreciation menu (`０１：インターミッション`, `０７：マップの音楽１`,
`５０：新曲１`…) and a flag editor (`フラグ４をＯＮにします。２章でキエーザ城に入れるように
なります。`) — and only **28 are player-facing**.

**Batch 005 is therefore: unique lines 984–1001 and 1040–1047 — 26–28 player-facing lines,
~1,777 JP characters.** Two coherent groups:

| lines | what | bank |
|---|---|---|
| 984–988 | five tutorial boxes: ZOC, front/rear unit composition, `『ＧＵＥＳＴ　ＵＮＩＴ』`, `「ＥＮＴＥＲ」` points, neutral units and `『説得』` | 30 |
| 989–1001 | fortress-guard and rumour dialogue: the Princess's disappearance, Bernard's church, the Carline–Empire alliance, Helfer's plot | 30 |
| 1040–1047 | the church scene — the priest Batou, Farina's reconstruction, the legend of the **Reese civilisation** and Bishop Creus | 31 |

Both banks are roomy (30 → 36,671 free, 31 → 35,581), so there is no bank pressure either way.

**Do NOT queue the 89 debug lines.** The player never reaches them, they are 1-instance each, and
they would spend bank 30/31 on a sound test. If someone later wants them for completeness they are
a deliberate, separate decision — not wave 2's.

**Do NOT queue more of the item-description table**: bank 40 is spent at 509 free, measured
(`FLAGS.md` §J2). Lines 185–225 must be parked until bank 40 is repointed.

### ⚠️ A survey defect this exposed, which affects every future script wave
`tools/queue.py` groups script lines by **bank residency and adjacency only**. It has no notion of
whether a line is player-facing, so a contiguous run of debug menu text looks exactly like a scene
and is 76% of this neighbourhood. **Every future script batch must be eyeballed for debug
scaffolding before dispatch** — grep the candidate range for `フラグ`, `：新曲`, `^[０-９]{2}：`
and `鑑賞モード`. Worth fixing in `queue.py` as a filter; recorded in `FLAGS.md`.

## Remaining (dispatchable) — measured by `python3 tools/queue.py battle`, 2026-09-08
Battle, **26 chunks / 29,246 JP characters** after chunk 4 merged (was 27 / 29,980), in chapter
order (tier, budget ratio). ~~4 (D 5.08)~~ **merged, PR #6**; 6 and 9 are in review now:
6 (C 3.09), 8 (B 2.32), 9 (D 4.93), 13 (C 3.41),
15 (D 6.13), 17 (C 3.19), 18 (D 6.28), 19 (B 1.94), 20 (D 4.75), 21 (D 4.28), 22 (D 4.59),
23 (C 2.80), 24 (C 2.99), 25 (C 3.48), 26 (C 3.36), 27 (D 5.54), 28 (D 4.76), 29 (D 6.04),
30 (B 2.43), 31 (C 3.46), 36 (C 3.92), 37 (C 3.69), 38 (C 3.37), 39 (D 6.20), 41 (E 6.54),
42 (D 5.46).

Script, from `python3 tools/queue.py script` (growth modelled at **2.10× JP characters — the
measured aggregate of the 151 lines already shipped**, 9,595 EN / 4,482 JP; 500 bytes reserved
per bank):

| | unique lines | instances |
|---|---|---|
| untranslated | 1,279 | 4,632 |
| **fit the banks** (greedy scarcity-weighted allocation) | **903** | **1,631** |
| bank-blocked → `pending/script/` | 376 | 3,001 |

The dispatchable script work in instance order is the **item / equipment description table**
(unique lines 127–330, 21 instances each — every map bank carries a copy). Bank 40 (1,771 free)
is the ceiling on it: about 40–45 such lines in total, so it is being spent deliberately, highest
instance yield first. After that the pool is the 1-instance story text in the roomy banks
(518–1,413, ~53,000 JP characters).

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
5. **Binaries**: put `SCRIPT.BIN` and `HEXMAP.BIN` in `original/`, run
   `python3 tools/assemble.py all` (real `checkedit`), rebuild the disc, play-test after each wave.
6. **Chunk 5 dump artifact** (FLAGS §D1): dumper fix plus re-dump; needs `original/`.

## Decisions this run
- 2026-09-08: workflow bootstrapped — `CLAUDE.md`, agents, `/translate`, PR template, this file.
- 2026-09-08: integration branch is `claude/workflow-translation-iterate-uzlkns` (see the Run
  configuration section). `main` is untouched and identical to this branch's base.
- 2026-09-08: **survey ran.** Added `tools/queue.py` (planning only; it imports `assemble` and
  `bankmeasure` read-only and changes neither). Battle: 30 dispatchable, 2 newly confirmed
  blocked (16 at 1.59, 32 at 1.61 — both under the 1.64× floor). Script: per-bank greedy
  allocation replaces the blanket "any pressured bank blocks the line" rule, which was costing
  545 shippable instances.
- 2026-09-08: growth factor for script planning set to **2.10×**, measured on shipped work, not
  the 2.0× assumed in the skill. 2.0× was optimistic.
- 2026-09-08: **all three wave-1 cross-PR conflicts settled by the PR #2 reviewer** — ノロ →
  `，　ｎｙｏｒｏ．` (glossary §5 corrected, decided on `riotfont.py`'s comma glyph), おお →
  `Ｏｈ！`, サイクス → `Ｓｙｋｅｓ`. Full reasoning in `glossary.md` §18; it binds every later unit.
- 2026-09-08: **`tl/battle/chunk_000.txt` corrected twice** (`Ｕｇｈ．．．` → `Ｔｃｈ．．．`,
  `Ｙｅｓ．` → `Ｙｅａｈ．`). The first closed a live CLAUDE.md §3 violation against shipped
  `chunk_007.txt`. Chunk 0 is now 8,165 / 8,192 — **27 bytes of slack, the tightest file in the
  project**; see `FLAGS.md` §G1 before any further correction lands on it.
- 2026-09-08: **PR #2 decided CHANGES** (round 1). All eight gates passed; the two findings are
  the two rulings above landing on that PR. 11 respellings, no re-flow.
- 2026-09-08: **PR #6 (battle chunk 4) decided MERGE, round 1, zero findings** — the first unit in
  the project to ship with a **byte-identical tag stream, every `{FFFE}` included**. Squash
  `e08bee8`. Wave 2's first review, and the first genuinely independent review of the run.
- 2026-09-08: **five rulings by the PR #6 reviewer**, all in `glossary.md` §23 and `FLAGS.md` §K:
  `辺境` → *frontier* with `chunk_000.txt` recorded and **not** re-cut (§20.4 pattern, now stated
  as a rule at §K2); `そうそう。` → `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`, which now **binds
  `pending/chunk_005.txt`'s re-cut** (+8 bytes, measured); **`しかし` → `Ｈｏｗｅｖｅｒ，`** —
  binds PRs #7 and #5; the **`助かった`** family pinned to a passive default; `ファリーナ` moved
  §1 → §2, **once, for the whole wave**. `クリミア` deliberately deferred to PR #5's reviewer.
- 2026-09-08: **`FLAGS.md` §J1 corrected** by the PR #6 reviewer, verified against PR #4's body.
  Two statements were false: PR #4's **Flag 3 did flag** the `持つ者に` departure by rule and line
  number, and the restore costs **32 bytes/entry → 192 total, not 42 → 252** (bank 40 → **317
  free**, ~**5** lines of parking, not seven). **The accept decision survives unchanged** — 317 is
  still 183 below the 500-byte reserve — so the correction is to the record, not to the trade.
- 2026-09-08: **a second shipped inconsistency found at review that neither wave-1 audit caught** —
  `chunk_001:14` renders `助かったノロ。` active while `chunk_003:7` renders `助かったノロ、`
  passive. **0-byte fix**, added to the wave-3 corrections unit.

## Wave history
| Wave | Units | Merged | Parked | Progress after |
|---|---|---|---|---|
| 1 | battle 1, 2, 3 + script 004 | **4** | 0 | battle 10 → 13 / 44 (13.8% → 20.1% of JP chars); script 151 → 185 unique lines, 3,299 → 4,013 instances (41.6% → **50.6%**) |

**Wave 1 detail.** All four merged, none parked, no unit past round 2.
`#2` battle chunk 1 — 3,517 / 8,192, slack 4,675, round 2 (`dddf0ae`).
`#3` battle chunk 2 — 5,839 / 8,192, slack 2,353, round 2 (`f298fe1`).
`#1` battle chunk 3 — 4,601 / 8,192, slack 3,591, round 1 (`1491ccd`).
`#4` script batch 004 — 34 lines / 714 instances, bank 40 → 509 free, round 1 (`b3b2abb`).
Glossary grew by four sections (§19–§22) and 13 seeds were promoted out of §9. `FLAGS.md` grew by
three sections (§H, §I, §J). Every unit's gates were re-run in a real checkout on the moved base.

## How to resume
1. `git checkout claude/workflow-translation-iterate-uzlkns && git pull --ff-only && python3 tools/assemble.py check`
2. Read this file — **NEXT ACTION at the top says literally what to do next**; list open PRs and
   reconcile the In flight table with reality.
3. `/translate` — preflight, then do what NEXT ACTION says. The queue is fresh.
4. The run is recursive: each wave's `orchestrator` subagent spawns the next wave's orchestrator
   before it returns, so it continues unattended. If NEXT ACTION names a spawn that never
   happened, the chain broke — spawn it yourself and carry on. The only four reasons to stop are
   in CLAUDE.md §8.
