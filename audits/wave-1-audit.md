# Wave 1 — independent post-merge audit (2026-09-08)

## Why this exists
Wave 1's coordinator ran as a **subagent** and therefore had no `Task` tool. Subagents cannot
spawn subagents, so it could not dispatch a reviewer and **reviewed all four of its own PRs**.
It disclosed this rather than hiding it. Chunks 1 and 2 had an independent round-1 review before
that takeover; **chunk 3 and script batch 004 had none at all**.

This audit is the missing independent reading review, run from the parent session after the
merges. Gates were re-run as a sanity check only — they are objective and their evidence was
pasted at the time. Root cause is recorded in `CLAUDE.md` §8 and `.claude/agents/orchestrator.md`;
the structural fix is that waves run as sessions, which have the full tool surface.

## Verdict: FINDINGS — but no must-fix on any translated line
Nothing invented, nothing dropped, no plot fact or speaker turn lost, every weapon still
distinguishable. `check` passes; `rowcheck 3` clean; no segment in chunks 1/2/3 over 23 columns;
no bank negative (40 → 509, 41 → 353); **zero divergent duplicate JP keys** across all four
`tl/script/*.tsv`; **zero unspaced `，` anywhere in `tl/`** (the §18.1 rework landed completely);
chunks 1 and 2 show **no regressions** from their rework. Ellipsis dot counts, charset, tag
streams, `{PAD}`, `{HDR:}`, leading `　` and `{FFFF}` placement all intact.

The findings below are what an interested party missed in its own work. None of them is a
mistranslation; most are documentation stating something that is not so.

## must-fix
1. **`FLAGS.md` §J1 states a falsehood later sessions will read as fact.** It says a §2.1 step 5
   departure was "not flagged" by PR #4. It was — PR #4's **Flag 3** — and Flags 4, 6–13 flag
   every other departure in the batch. The translator's Flags were complete. Correct the sentence.

## should-fix
2. **`FLAGS.md` §J1's arithmetic is wrong, and it changes the conclusion.** Restoring `持つ者に`
   costs **32 bytes/entry**, not 42 — PR #4's own Flag 3 says "12 bytes each instead of 44", so
   the figure was on the page in front of the reviewer. Six entries cost **192 bytes, not 252**;
   bank 40 lands at **317 free, not negative**; and **nothing is parked**. The "seven Japanese
   holes in a table" justification for accepting 2.23× compression was therefore false. The real
   trade was 183 bytes of *planning reserve* — in the one bank `FLAGS.md` §F2 measures as 20,754
   bytes short for the text still to come, and which §J2 itself declares closed to every further
   batch. Re-state the trade honestly. Restoring the clause on all six entries is affordable:
   `Ａ　ｓｗｏｒｄ／ｓｐｅａｒ　ｗａｒｄｉｎｇ　ｉｔｓ{FFFE}ｂｅａｒｅｒ　ｗｉｔｈ　ｆｉｒｅ．` (20/18 columns).
3. **`tl/script/batch_004.tsv:12`** — `多くの兵士が愛用する一般的な剣。` →
   `Ａ　ｓｗｏｒｄ　ｍｏｓｔ　ｓｏｌｄｉｅｒｓ{FFFE}ｆａｖｏｕｒ．` drops `一般的な` and strengthens `多くの`
   to "most", while line 31 of the same table renders `もっとも一般的な` as `Ｔｈｅ　ｃｏｍｍｏｎｅｓｔ`.
   Row 2 uses only 7 of 23 columns. Fix: `Ａ　ｃｏｍｍｏｎ　ｓｗｏｒｄ　ｍａｎｙ{FFFE}ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ．`
   (19/16 columns, +14 bytes per bank).
4. **`tl/battle/chunk_003.txt:16`** — breaks split `Ｒｏｙａｌ` from `Ａｒｍｙ` and `ｓａｖｅｄ` from
   `ｕｓ．`, against §3.2's clause-boundary preference, in a chunk 3,591 bytes under budget.
   **Zero byte cost** to fix: `Ｅｖｅｒｙｏｎｅ　ｏｆ　ｔｈｅ{FFFE}Ｒｏｙａｌ　Ａｒｍｙ，　ｙｏｕ　ｔｒｕｌｙ{FFFE}ｓａｖｅｄ　ｕｓ．　Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ{FFFE}ｈｏｗ　ｔｏ　ｔｈａｎｋ　ｙｏｕ．`
   — 15/21/23/17 columns, same four rows.
5. **`tl/battle/chunk_003.txt:5`** — `しかし、敵は` → `Ｓｔｉｌｌ，`, which is glossary §19.1's fixed
   form for `それにしても`, shipped as `Ｓｔｉｌｌ，` in chunk 1 (×2) and chunk 2 (×1) **of the same
   wave**. Two distinct connectives collapsed onto one English word with no glossary note, where
   every other deliberate collapse (`ふっ/フンッ→Ｈｍｐｈ`, `む/ん→Ｈｍ`, `鬼/オーガ→ogre`) is
   recorded as such. Either `Ｈｏｗｅｖｅｒ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` (21 columns, +4 bytes — `でも→Ｂｕｔ`
   is already taken in that chunk) or record the collapse explicitly.
6. **`FLAGS.md` §I1's corpus argument counts six glossary-fixed renderings as free evidence**
   (`“Ｇｅｍｓ”` §3, `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”` §12.1, `“Ｒｉｂｂｉｔ”` §5,
   `“ｄｅｍｏｎ　ｂｌａｄｅ”` §17.3 …). Strip them and the picture inverts: `batch_002`, the only other
   free-choice body, is **100% consistent** with the sentence-position rule, and the only two
   genuinely free cases are chunk 1's `ｃｈｏｏｓｅ　“Ｗａｉｔ”` and chunk 3's `Ｉｆ　ｙｏｕ　“ｅｎｔｅｒ”` —
   same wave, same battle-map tutorial box, same grammatical position, **opposite cases**. That is
   a two-file conflict inside one wave, not a settled ambiguity. Settle it; every candidate fix is
   0 bytes and 0 columns.
7. **`glossary.md` §21 — five entries PR #1 proposed were dropped at integration with no note of
   rejection**: `ヘビー→ｈｅａｖｙ`; `洞窟／赤い屋根の家／赤い屋根の建物`; `さあ→Ｃｏｍｅ　ｏｎ，`;
   bare `隊→squad`; and `謹慎中→ｕｎｄｅｒ　ｃｏｎｆｉｎｅｍｅｎｔ` / `謹慎がとける→ｃｏｎｆｉｎｅｍｅｎｔ　ｅｎｄｅｄ`
   (§19.2 records only `ｃｏｎｆｉｎｅｄ`). All are rendered in shipped work but fixed nowhere —
   `さあ、` recurs 26 more times across both dumps, `洞窟` 4 more. Append them or record the rejection.

## Notes, no action
`きっと役に立つノロ。` → `Ｓｕｒｅ　ｔｏ　ｈｅｌｐ，　ｎｙｏｒｏ．` drops the subject, but no subject fits
24 columns with the tic. `援軍を連れてきました。` → `Ｉ　ｂｒｉｎｇ　ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ．` is present
for perfect at exactly 23 columns. Rows ending in a lone `ｔｏ`/`ｉｎ`/`ｏｆ`/`ｂｅ`/`ｓｏ` occur across
chunks 1, 2 and 3 alike — a house-wide pattern, not a chunk-3 defect. Chunk 3's two "back to the
castle" variants differ deliberately (PR Flag 6, Kasim/Tasim precedent) and that reasoning holds.

## The shape of the failure, for whoever reviews next
The `“ｅｎｔｅｒ”` question was raised at chunk 1's integration and narrowed at chunk 3's **by the
same agent**. Narrowing it was correct on the merits — the `“Ｇｅｍｓ”` analogy really was false —
but the effect was to excuse the unit then under review. Self-review failure does not look like
fabrication. It looks like a justification drifting toward the convenient answer, with each step
defensible on its own.
