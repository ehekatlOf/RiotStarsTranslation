# Independent reading-review audit — wave 1's four self-reviewed units

**Run:** 2026-09-08, by an independent read-only subagent of wave 2's session
(`session_01JDoA8KzwUVk3ZjiBw8Qkf3`). Required by `CLAUDE.md` §8 as amended in commit `16c179e`.

**Why:** wave 1's coordinator ran as a subagent, so it could not spawn a reviewer and it
dispatched, judged and merged all four of its own units. It disclosed this and evidenced every
mechanical gate. What was lost was the independence of the **reading** review; this audit supplies
it after the fact.

**Scope:** `tl/battle/chunk_001.txt` (PR #2), `chunk_002.txt` (PR #3), `chunk_003.txt` (PR #1),
`tl/script/batch_004.tsv` (PR #4). Reading review only; gates re-run as a cross-check.

## Verdict: the four units STAND AS MERGED

No unit changes a plot fact, drops a clause the budget did not force, mixes a verbal tic, breaks a
gate, or renders identical Japanese two ways. **No correction commit is required before wave 3
dispatches.** Every finding below is a MINOR improvement, not a defect that should have blocked a
merge.

Gates re-run independently and all pass: `check` → All checks passed; `rowcheck` on 1/2/3 → no
page over 4 rows the source did not already exceed; `merge` → no "never matched the dump";
`bankmeasure` → no negative bank. Also verified: every ellipsis dot-run matches the source; no
character outside §3.1 anywhere; the widest row in all four units is **23** columns (none at the
24 hard limit); all 23 `ノロ` instances carry the corrected `，　ｎｙｏｒｏ` form with JP/EN
counts matching per chunk (10/2/11); no duplicate JP key across the four script batches.

**Duplicate scan** (every dump line split at `{FC30}`, tags stripped, English compared for every
identical Japanese message, across all 13 shipped battle chunks): **zero divergences inside the
four audited units** — 11 repeated messages, all byte-identical. One divergence exists in *earlier*
shipped work: item 9 below.

## Eight proposed file edits — housekeeping, not blocking

Verified to fit: every proposed row is ≤ 23 columns. The four `batch_004` edits together cost
**38 bytes in bank 40 (509 → 471 free)**; each of those lines occurs once per bank in 21 banks, so
a growth of N full-width chars costs 2N bytes *per bank*, not 21×2N.

| # | Unit / line | Issue | Fix | Cost |
|---|---|---|---|---|
| 1 | `chunk_002` L14 | `すみません。` → `Ｗｅ　ａｒｅ　ｓｏｒｒｙ．` reads as an apology for wrongdoing; it is apologetic *thanks*, from characters just rescued, immediately before `ありがとうございます` | `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` (21 cols) | +16 B; slack 2,353 → 2,337 |
| 2 | `chunk_003` L6 | `しかし、` → `Ｓｔｉｌｌ，` — **takes §19.1's fixed form for それにしても**, and contradicts shipped `chunk_000` `はっ、しかし・・・` → `Ｓｉｒ，　ｂｕｔ．．．` | `Ｓｔｉｌｌ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` → `Ｂｕｔ　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` (16 cols) | **−6 B (frees bytes)** |
| 3 | `batch_004` L12 | `多くの兵士が愛用する一般的な剣。` drops 一般的な and promotes 多くの to "most"; L31 renders もっとも一般的な as `Ｔｈｅ　ｃｏｍｍｏｎｅｓｔ` two rows away | `Ａ　ｃｏｍｍｏｎ　ｓｗｏｒｄ　ｍａｎｙ{FFFE}ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ．` | +14 B/bank |
| 4 | `batch_004` L29 | `力を秘めた` flattened to "of"; L27 renders the parallel phrase as `ｈｉｄｉｎｇ` | `…ｈｉｄｉｎｇ　ｔｈｅ{FFFE}ｄｅｍｏｎ　ｇｏｄ　Ｔｙｒ’ｓ　ｐｏｗｅｒ．` | +8 B/bank |
| 5 | `batch_004` L42 | Break after "spear" garden-paths ("spear black knights" parses as a noun pile); also a third shape for 愛用 | `Ａ　ｊｅｔ‐ｂｌａｃｋ　ｓｐｅａｒ　ｔｈｅ{FFFE}ｂｌａｃｋ　ｋｎｉｇｈｔｓ　ｆａｖｏｕｒｅｄ．` | +8 B/bank |
| 6 | `batch_004` L17 | `ｂｕｒｎｉｎｇ　ａｌｌ　ｕｐ．` not idiomatic as a participial modifier; 焼き尽くす is burn-to-nothing | `ｂｕｒｎｉｎｇ　ａｌｌ　ｔｏ　ａｓｈ．` | +8 B/bank |
| 7 | `chunk_003` L17 | `Ｅｖｅｒｙｏｎｅ　**ｏｆ**　ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ` — literalism from の; English says "in" for membership | `ｏｆ` → `ｉｎ` | **0 B (free)** |
| 8 | `chunk_001` L2 | Break splits the compound "food store"; word boundary so §3.2's hard rule holds, but "the food" ends a row as a complete phrase | `ｇｕａｒｄ　ｔｈｅ　ｆｏｏｄ　ｓｔｏｒｅ{FFFE}ｆｏｒ　ｕｓ，　ｐｌｅａｓｅ，　ｎｙｏｒｏ．` | +2 B |

## 9. A live CLAUDE.md §3 violation in *earlier* shipped work — out of audit scope, real

`村が襲われました。` (**13 occurrences** in `battle_dump.txt`, same `{=FA1000300030}` tutorial-box
marker as the stolen-item message) is rendered two ways:

- `tl/battle/chunk_007.txt` L26, L27 → `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．`
- `tl/battle/chunk_034.txt` L8 → `Ｔｈｅ　ｖｉｌｌａｇｅ　ｈａｓ　ｂｅｅｎ{FFFE}ａｔｔａｃｋｅｄ．`

**Verified independently by wave 2's coordinator.** Identical Japanese, divergent English across
files — the exact twin of the case §21.3 fixed for `アイテムを{FFFE}奪われました。`. Ten further
instances are still untranslated, so one ruling binds thirteen. `chunk_034` has 6,601 bytes of
slack and `chunk_007` only 399, so the cheap fix is to change **chunk 34** to chunk 7's wording
(−4 chars there, chunk 7 untouched). Predates wave 1; neither wave 1 nor wave 2 introduced it.

## Glossary / FLAGS entries wrong or missing — the durable half of this audit

These are **precedents, not file edits**, and they are what actually stops drift. Three are live in
wave 2 right now.

1. **`しかし` has no entry and two forms are shipped** — `ｂｕｔ` (chunk 0) and `Ｓｔｉｌｌ，`
   (chunk 3), the latter colliding with §19.1's それにしても → `Ｓｔｉｌｌ，`. ⚠️ **LIVE:** wave 2
   carries it **3×** (chunk 6 ×1, chunk 9 ×2 — verified). Note chunk 3 also ships でも → `Ｂｕｔ`,
   and chunks 4, 6 and 9 each carry でも ×2, so `しかし` → `but` is a **deliberate collapse of two
   words** and must say so if chosen (the ふっ/フンッ → `Ｈｍｐｈ` precedent). This is a real
   tradeoff, which is why it is the reviewer's ruling to make, not the coordinator's.
2. **`愛用` has no entry and three shapes are shipped** — `ｆａｖｏｕｒｅｄ　ｂｙ` (batch_003 ×2),
   `ｍｏｓｔ　ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ` and `ｂｌａｃｋ　ｋｎｉｇｈｔｓ　ｆａｖｏｕｒｅｄ`
   (batch_004). **13 occurrences remain untranslated.** §22.2's stated frame ("a participial
   clause") does not actually describe either batch_004 form.
3. **`村が襲われました。` needs a §21.3-style entry and a FLAGS note** — one rendering binds 13
   instances. See item 9.
4. **Stale §9 row for `ティミー`** (glossary line 228): still listed unstruck, but §11.1 (line 350)
   already promoted it at the chunk-43 spike *and* records that Timmy is **female** — a fact §9's
   row lacks. §20.1's "four promotions out of §9" does not include it, which misleadingly reads as
   if chunk 2 rendered an unpromoted provisional. Strike §9's row and point at §11.1.
5. **`すみません` has no entry** — one occurrence in `tl/`, the one in item 1.
6. **`助かった` / `助かりました` has no entry**; the corpus carries active and passive forms
   (`ｙｏｕ　ｓａｖｅｄ　ｕｓ`, `ｙｏｕ　ｔｒｕｌｙ　ｓａｖｅｄ　ｕｓ`, `Ｗｅ　ａｒｅ　ｓａｖｅｄ`,
   and both again in chunk 12). **Wave 1 did not introduce this** and every source string genuinely
   differs, so no §3 rule is engaged — but ⚠️ **chunk 4 carries one** (verified), so the family is
   worth pinning before it spreads.

## ⚠️ CORRECTION — this audit was WRONG about `FLAGS.md` §J1

This report originally closed by saying §I1 and §J1 "anticipate exactly what this audit found" and
that "§J1's arithmetic is correct." **Both claims are false, and wave 2's coordinator verified so
against primary sources.** A *second*, independent audit run in parallel by wave 1's session
(`audits/wave-1-audit.md`) caught what this one waved through:

1. **§J1 states a falsehood.** It says the `持つ者に` departure "is a §2.1 step 5 departure and the
   PR did not flag it." **PR #4's Flag 3 flags it explicitly**, by name, by rule and by line
   number: "§2.1 step 5 — 持つ者に…をもたらす implied, lines 146–148 and 170–172." Flags 4 and
   6–13 flag every other departure in the batch. The translator's Flags were complete.
2. **§J1's arithmetic is wrong and it changes the conclusion.** §J1 costs the restore at "+42
   bytes per entry × 6 = +252 bytes." PR #4's Flag 3 — on the same page the reviewer was reading —
   gives the one-row form as "12 bytes each instead of 44", so the delta is **32 bytes per entry,
   not 42**: **192 bytes, not 252**. Bank 40 lands at **509 − 192 = 317 free**, not negative. §J1's
   "park about 7 of the 34 lines" overstates: at ~37 bytes/line the real cost is ~5 lines, or
   **zero** if the trade is taken against the 500-byte planning reserve instead — which is what it
   actually was. §J1's "seven Japanese holes in a table" justification was false.

§I1 is likewise not settled: wave 1's audit shows its corpus argument counts **six glossary-fixed
renderings as free evidence**; strip those and the only two genuinely free cases — chunk 1's
`ｃｈｏｏｓｅ　“Ｗａｉｔ”` and chunk 3's `Ｉｆ　ｙｏｕ　“ｅｎｔｅｒ”` — are the same wave, same
tutorial box, same grammatical position, **opposite cases**. A live two-file conflict, not a
settled ambiguity. Every candidate fix is 0 bytes and 0 columns.

**Why this correction is on the record rather than quietly patched:** an audit that certified a
documentation defect as sound, in a report about the cost of self-review, is exactly the failure
mode being audited. It is also the case for having run two independent audits.
