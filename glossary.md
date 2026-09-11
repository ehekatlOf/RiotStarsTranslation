# Riot Stars — Translation Glossary

Paste this into every translation session, directly under `translation_prompt.md`.

**Every entry here is fixed.** Use the English form exactly as written, everywhere, forever. To
change one, follow §4.3 of the prompt: state the correction explicitly and list every previously
translated line that must be revisited.

Entries in **§9 PROVISIONAL** are *not* decisions — they are names seen in the dumps but not yet
rendered in any translated line. Promote one to its proper table the first time you use it.

Status: covers `script_unique.txt` lines 1–216 (unit, class, monster and equipment descriptions), 984–1001 and 1040–1047 (batch 005), and `battle_dump.txt`
chunks **0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19, 20, 33, 34, 35, 40** (prologue + chapters
2–5 + all of tier E), plus the parked **5, 17, 43**. ⚠️ **This line was stale and is corrected
2026-09-08 (PR #13 review): it omitted chunks 6, 8, 9, 13 and 17, all merged or parked in waves
2–3.** It is a coverage note, not a fixed entry — no rendering changes and nothing needs
revisiting; §4.3 applies to entries, and the correction is recorded here and in `FLAGS.md` §S so
it is not silent.

---

## 1. People

| Japanese | English | Note |
|---|---|---|
| カイン | Kain | main companion; casual register, contractions throughout |
| リムル | Rimul | enemy commander, female, addressed as 様 → **Ｌａｄｙ　Ｒｉｍｕｌ**; formal, unhurried register |
| ドースン | Dawson | enemy officer, defeated before/around chunk 0 |
| レンドル | Rendol | Rimul's subordinate |
| セネカ | Seneca | craftsman |
| フィリス | Phyllis | |
| フェルナンド | Fernando | commander of the 2nd Royal Army |
| ギルフォード | Guilford | |
| アルフレッド | Alfred | 少尉 → **Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ａｌｆｒｅｄ**; orders Beatrice to the 9th Army (ch.14) |
| アルテミス | Artemis | |
| リッジ | Ridge | party member; snarky, blunt, casual. Also `script_unique` 1366 |
| マヤ | Maya | forest witch (ch.11), spareable; later a shopkeeper (`script_unique` 1348–1350) |
| シロン | Shiron | martial artist, master of the Caucasus dojo, joins the party (ch.12). Alt readings *Sylon*, *Chiron* — Shiron chosen as the plainest |
| ベアトリス | Beatrice | captain, Carline 7th Army 3rd Squad; joins in ch.14 |
| カシム | Kasim | ch.34 boss, portrait 7 — speaks first |
| タシム | Tasim | ch.34 boss, portrait 8 — his brother. The near-identical names are the joke; keep them near-identical |
| リオン | Ｌｅｏｎ | ⚠️ **DECIDED 2026-09-08 (PR #7 review) — this row previously read “unresolved — Lion or Leon”, and §10.1 is discharged with it.** Rendered twice in battle chunk 6 (`匿名希望のリオンって`, `リオンが？`): the man who sent Ridge to the 9th Army and wants to stay anonymous. `Ｌｅｏｎ` over `Ｌｉｏｎ` on the European-reading convention every other name follows (Bauer, Carline, Helfer, Albert, Fernando, Anselmo) — `Ｌｉｏｎ` would read as the animal, the failure §17.2 avoided for Ｎｅｒｇａｌｉ. **Promoted from §9's wave-2 seed, used exactly as seeded.** 4 columns. See §24.1 |
| 王女様 | the Princess | |
| 神父 | priest | the fairy's ring-bearer |
| 妖精 | fairy | lowercase, common noun; referred to as *she* |
| 市長 | the mayor | Caucasus (ch.12); also `script_unique` 380 |
| クレス | Ｃｒｅｓｓ | 少尉 → **Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ** (**17+5 = 23 bare, 24 in the vocative**, so it does not share a row in the only form either dump renders — corrected in place 2026-09-09, §4.3, PR #18 review; this row read “18+5 columns, never on one row”, and the blanket claim is false for shorter names: `Ｒｙａｎ` is 4 and fits at 23. §29.5 reasoned this on Cress and it holds **for Cress only**; see §36.4). ⚠️ **FEMALE — settled 2026-09-09 (§4.3, PR #29 review), and `FLAGS.md` §Y6's own premise is REFUTED with it.** §Y6 claimed “no shipped English anywhere genders Cress”; merged `tl/battle/chunk_013.txt` body line 0 has shipped `Ｉ　ｈａｄ　ｈｅａｒｄ　ｏｆ　ａ　ｗｏｍａｎ` / `ｃａｐｔａｉｎ` since **wave 3**, rendering the source's `女隊長` two segments after the same speaker confirms her name (`その方、クレスと申したな。`), with `上玉` and `ギルフォード将軍に献上してやる` corroborating; `chunk_022` body line 0 fixes the referent independently by addressing her as `クレス隊長`. Read at review, not taken from a citation. **No rendering changes anywhere** — no shipped line uses a pronoun for her, and chunk 37's only `クレス` is `Ｃｒｅｓｓ　ｉｓ　ｗｉｔｈ　ｙｏｕ　ｔｏｏ！！`. See §48.3. Court‐martialled alongside Alfred for the failed expedition (script 1236). Alt *Kress*, *Cres* |
| アンゼルモ | Ａｎｓｅｌｍｏ | 中尉 → **Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ** (**24** columns). **Promoted from §14.6**, which already used this form for his register but never fixed the name. **7 columns** (corrected in place 2026-09-09, §4.3, PR #18 review; this row read “8”, and §29.5 read 25 for the titled form). See §36.4 |
| ゼファー・クリッペン | Ｚｅｐｈｙｒ　Ｋｒｉｐｐｅｎ | 帝国の司令官 → Commander of the Empire. `・` has no glyph in §3.1 and becomes `　`. 14 columns. Alt *Zepher*, *Crippen*, *Klippen* |
| ヘルファー様 | Ｌｏｒｄ　Ｈｅｌｆｅｒ | 様 → **Lord** for a male superior, paralleling 様 → Lady (Rimul §1, Phyllis §14.1). 11 columns. Does not change the §11.1 bare-name entry |
| マラナ | Ｍａｒａｎａ | **Promoted from §9's wave-8 seed 2026-09-09 (PR #33), used exactly as seeded.** 7 columns. Imperial commander, and — `かつての上官` (chunk 38 L16) — **the party's own former superior officer**, who returns "from the depths of hell" after an earlier defeat. Register: the §14.6 / §20.5 / §25.5 / §28.6 Imperial-officer column, **zero contractions anywhere** (verified line by line at review). `この…` self-aggrandisement is kept as an appositive per §25.1 / §30.1: `このマラナ、` → `Ｉ，　Ｍａｒａｎａ，` and `このマラナにとっては` → `Ｔｏ　ｍｅ，　Ｍａｒａｎａ，`. ⚠️ **GENDER IS UNFIXED AND UNRENDERED — do not guess it.** The wave-8 seed asserted female from `〜わ`; that inference is refuted (see the struck §9 row for the 40-instance census and the four male speakers), and `おっさん` → `ｇｅｅｚｅｒ` at chunk 38 L10 points the other way. No shipped English genders her, and none should without evidence. **2 battle, 0 script — exhausted.** Alt *Malana* |
| クリミア | Ｃｒｉｍｅａ | ⚠️ **CORRECTED 2026-09-08 (§4.3, PR #5 review): a PERSON — `クリミア博士`, the designer of the Empire's machine soldiers — not the region §2 filed him as.** Verified in both dumps before moving, not taken from the PR: **5 battle + 64 script occurrences, not one of them a place.** He self-refers in the third person (`この砦は、このクリミアにお任せ下さい。` — *leave this fort to Crimea*, i.e. to me; `またこのクリミアの新型機械兵` — *this Crimea's new machine soldier*), is addressed vocatively twice (`クリミア博士、反乱軍です・・・！！`, `クリミア博士、事は計画通り進んで`), is located **inside** a place (`クロスリーにいるクリミア博士`), and the script's machine-soldier table credits him as their maker (`クリミアの量産型機械兵２号機`). **Already-shipped work agrees**: `tl/script/batch_003.tsv` lines 85, 86 and 94 render that table as `Ｃｒｉｍｅａ’ｓ　ｍａｓｓ‐ｐｒｏｄｕｃｅｄ　…`, `Ｃｒｉｍｅａ’ｓ　ｉｍｐｒｏｖｅｄ　…`, `Ｃｒｉｍｅａ’ｓ　ｆｉｎａｌ　ｍａｃｈｉｎｅ　ｓｏｌｄｉｅｒ．` — a person's possessive, written before anyone noticed the §2 row was wrong. The rendering `Ｃｒｉｍｅａ` is unchanged, so **no translated line needs revisiting** — only the classification was wrong. This is the メルザリオ / ファリーナ shape (§20.1, §2); `FLAGS.md` §K6 deliberately deferred it to this reviewer. 6 columns. See §25.1 |

## 2. Factions, places, ranks

| Japanese | English | Note |
|---|---|---|
| 第９軍 / ９軍 | 9th Army | the player's unit; `９` is full-width in source |
| 第７軍 | 7th Army | Alfred's; `７` full-width, same rule |
| 第３分隊 | 3rd Squad | `３` full-width |
| 分隊長 | squad captain | promoted from PROVISIONAL. Use **squad captain** where 隊長 is written out (ベアトリス, ch.14), **squad leader** for the bare 分隊長 |
| 隊長 | captain | how the player character is addressed. `Ｃａｐｔａｉｎ　{FC00}` = 15 columns; `Ｃｏｍｍａｎｄｅｒ` does not fit alongside the insert |
| 少尉 | Second Lieutenant | **17 columns** (corrected in place 2026-09-09, §4.3, PR #18 review — this row read “18 columns — will not share a line with a name”, and **both halves were wrong**). It **does** share a line with a short name: `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ，` is **23** and ships as one row in `chunk_021`. Add the name's width + 1 and check against 23; `Ｃｒｅｓｓ` (5) reaches 24 in the vocative and still needs the split. See §29.5 and §36.4 |
| 中尉 | First Lieutenant | **16 columns** (corrected in place 2026-09-09, §4.3, PR #18 review; this row read “17”). Same arithmetic error as 少尉, first measured by §29.5 in wave 3. `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` is **24** — inside the box, at the hard limit, over the ≤23 preferred limit — so put the name on the next row unless a shorter name makes it fit. See §36.4 |
| 宮廷軍 / 宮廷防衛軍 | Royal Army / Royal Defence Force | keep the two distinct |
| 紅の騎士団 | Crimson Knights | elite imperial unit |
| 帝国 | the Empire | 帝国軍 → the Empire's men where 24 columns will not take "the Imperial army" |
| 精鋭部隊 | elite corps | the Crimson Knights' formation |
| 本隊 | the main force | distinct from 精鋭部隊 |
| ファリーナ | Ｆａｒｉｎａ | ⚠️ **CORRECTED 2026-09-08 (§4.3, PR #6 review): a PLACE — a country and its castle — not a person.** §1 listed it under People with no gloss. Verified in the dumps before moving: `ファリーナという国も昔は栄えとった` (*the country called Farina prospered once*), `ファリーナ城`, `ファリーナの南、カペラの村`, `ファリーナを占領した`, `ファリーナ出身`, and three people identified **by** it — `ファリーナの司教、クレウス`, `ファリーナの衛兵隊長、ウルフ`, `ファリーナの自治官フェリクス`. **Not one instance in either dump uses it as a personal name.** The rendering `Ｆａｒｉｎａ` is unchanged, so **no translated line needs revisiting** — only the classification was wrong. Flagged by PRs #7 and #8; moved once, here, so the wave does not move it three times. 6 columns |
| カーライン | Carline | home castle/territory |
| カーライン王国 | Kingdom of Carline | |
| カーライン城 | Carline Castle | |
| コーカサス | Caucasus | town of martial artists; Shiron's dojo is here |
| バウワーの砦 | Bauer's fort | ch.40. Alt *Bower*; Bauer chosen as the likelier source reading |
| バジリスクの砂漠 | the Basilisk Desert | ch.14 map. Capitalised only as the place name — the monster stays lowercase |
| ホビット / ホビットの村 | Hobbit / Hobbit Village | ⚠️ **SCOPE WRITTEN IN 2026-09-11 (§4.3 in-place correction, PR #35 review) — THE RENDERING IS UNCHANGED, only the scope is now stated.** This note column was **empty**, so a key-first gate 7 read the row as fixing a capital everywhere and flagged `batch_012`'s **correct** lowercase `ｈｏｂｂｉｔ　ｖｉｌｌａｇｅ　ｃｈｉｅｆ` (DATA 370–373) as a failure; the scope was recoverable only two thousand lines away. `Ｈｏｂｂｉｔ　Ｖｉｌｌａｇｅ` is capitalised **as a place name**; the **descriptive** use is lowercase `ｈｏｂｂｉｔ`, ruled at **§17.1** (“lowercase in prose”) and **§38.4** (on shipped `chunk_002.txt` L12, “in word *and* case”). `ホビットの村の村長` is descriptive, so lowercase is conformance |
| 龍人族 | dragonfolk | one word, 11 columns. Will not fit a ≤20 class slot as "Dragonfolk descendant" — flag if it is ever needed there |
| トカゲ | lizard | 〜さん as address → **Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ** |
| 司令部 | headquarters | 12 columns — only fits alone on a line |
| 守備兵 | garrison / garrison men | seed had "garrison soldier"; 8+8 columns rarely fits, so bare **garrison** is the default and **garrison men** the plural-personal form |
| 機械兵 | machine soldier | |
| 援軍 | reinforcements / **aid** | use "aid" only where 24 columns will not take the full word; flag each time |
| 要塞 | fortress | 8 columns |
| 旗印 | banner | |
| ウエストバリー | Ｗｅｓｔｂｕｒｙ | Town taken by the 9th Army. **8 columns** (⚠️ corrected in place 2026-09-09, wave-6 seed: this row said 9; `Ｗｅｓｔｂｕｒｙ` is eight characters, measured with `len()`, and it is shipped 5× in `chunk_008`, `chunk_009` and `batch_002`). ⚠️ **The dumps spell it TWO ways** — `ウエストバリー` (large エ; 4 battle + 3 script) and `ウェストバリー` (small ェ; 0 battle + **1 script, in `batch_008`/unique 505**). **Both render `Ｗｅｓｔｂｕｒｙ`.** A gate-6 grep on the exact Japanese will not pair them. Alt *Westbarry* |
| 大要塞 | ｇｒｅａｔ　ｆｏｒｔｒｅｓｓ | 14 columns. Keep **distinct** from 要塞 → fortress and 空中要塞 → sky fortress (§11.2) |
| 作戦会議 | ｗａｒ　ｃｏｕｎｃｉｌ | 11 columns |
| 穀潰し | ｆｒｅｅｌｏａｄｅｒｓ | Contemptuous — one who eats but does not work. 12 columns. **Distinct** from 雑草ども → weeds (§11.5) and ゴミ → rubbish (§14.4). Recurs in script 1236 |
| 死罪 | death (as a penalty) | 逃亡は死罪 → `Ｆｌｉｇｈｔ　ｂｅｆｏｒｅ　ｔｈｅ　ｅｎｅｍｙ　ｍｅａｎｓ　ｄｅａｔｈ` |

## 3. Items and mechanics

| Japanese | English | Note |
|---|---|---|
| ジュエル | Jewel | currency; **do not** translate as "gem" |
| ジェム / 『ジェム』 | Gem / “Ｇｅｍｓ” | battle pickup — distinct from Jewel, keep both |
| ジェムタイプ | Gem Type | 2,964 occurrences — never vary it |
| 緑 / 赤 / 青 (Gem Type) | Green / Red / Blue | |
| サイクル / ランダム (Gem Type) | Cycle / Random | |
| パワーストーン / 『パワーストーン』 | “Ｐｏｗｅｒ　Ｓｔｏｎｅ” / “Ｐｏｗｅｒ　Ｓｔｏｎｅｓ” | `『…』` → `“…”` |
| 必殺技 | special attack | |
| 指輪 | the ring | plot item |
| 玉 (ジェムの) | orbs | the small red and green drops |
| ユニット / クラス / クラスチェンジ | unit / class / class change | |
| 待ち時間（Ｗａｉｔ） | Ｗａｉｔ　ｔｉｍｅ | the parenthetical gloss is redundant in English — drop it |
| ＨＩＴ | hits | source uses full-width caps for the loanword; English needs no emphasis |
| ○ボタン / □ボタン | Ｃｉｒｃｌｅ　ｂｕｔｔｏｎ / Ｓｑｕａｒｅ　ｂｕｔｔｏｎ | ○ □ are outside the permitted charset |
| ×ボタン | **Ｃｒｏｓｓ　ｂｕｔｔｏｎ** | 12 columns. **Decided 2026‐08‐06, see §16.** Shape name, not keycap letter — `Ｘ　ｂｕｔｔｏｎ` would be the only button named by its glyph while ○ and □ are named by shape, and §4.3 forbids restyling those silently |
| △ボタン | Ｔｒｉａｎｇｌｅ　ｂｕｔｔｏｎ | 15 columns. Fixed now, prospectively, so the fourth button cannot drift |
| メダル (racetrack) | ｍｅｄａｌ / ｍｅｄａｌｓ | The betting token at the horse track. **Distinct** from ジュエル → Jewel; do not merge |

## 4. Classes and class descriptions

| Japanese | English | Note |
|---|---|---|
| 剣士 / 女剣士 | swordsman / swordswoman | 女 marks the female classes |
| 戦士 | warrior | |
| 弓兵 / 弓の戦士 | archer / bow warrior | |
| 軽騎兵 | light cavalry | |
| 騎士 | knight | |
| 天馬騎士 | pegasus knight | lowercase — a class noun, not a name |
| 魔術師 / 女魔術師 | mage / sorceress | "sorceress" only where 女 is explicit |
| 魔法戦士 / 魔法騎士 | magic warrior / magic knight | keep the two distinct |
| 盗賊 | thief | |
| 武闘家 | martial artist | lowercase in prose; `Ｍａｒｔｉａｌ　Ａｒｔｉｓｔ` = 14, fits the ≤20 class cap |
| バジリスク | basilisk | monster common noun, lowercase; capitalised only in the Basilisk Desert |
| フリーナイト | Free Knight | capitalised — a named class |
| ビーストマスター | Beast Master | two words, capitalised |
| 昇格型 | promoted | → "a promoted X"; distinct from 上級 |
| 上級 / 上級職 / 最上級 | advanced / advanced class / highest‐class | three distinct tiers, never interchange |
| 全体魔法 / 単体魔法 | all‐target magic / single‐target magic | uses ‐ (U+2010) |
| 炎 / 雷 / 氷 / 暗黒 / 光 / マヒ | fire / thunder / ice / dark / light / paralysis | **雷 = thunder**, not lightning — 9 columns will not fit |
| 攻撃力 / 防御力 / 機動力 / 戦闘力 | attack power / defence power / mobility / combat power | British spellings (defence, armour) throughout |
| 一撃必殺 | kills with one blow | |
| 山林 | woodlands | |
| クラスＮＮ | Ｃｌａｓｓ　ＮＮ | untranslated placeholder slots 41–43 and 70; digits stay full-width |
| ダミーぶきです | Ｔｈｉｓ　ｉｓ　ａ　ｄｕｍｍｙ　ｗｅａｐｏｎ． | unused placeholder, 126× |
| ダミーぼうぐです | Ｔｈｉｓ　ｉｓ　ａ　ｄｕｍｍｙ　ａｒｍｏｕｒ． | unused placeholder, 84× |
| 進化型 / 進化した | evolved | adjectival, as 昇格型 → *promoted* already is: `Ｘの進化型` → **an evolved X**. **Third ladder** — never interchange with 昇格型 or 上級 |
| 完成型 | perfected | `オークの完成型` → *the perfected orc*. Distinct from 進化型 and from 最上級 → highest‐class |
| 突然変異 / 突然変異種 | mutation / a mutant X | `スライムの突然変異種` → *a mutant slime* |
| 亜人種 | demi‐human | uses ‐ (U+2010) |
| アンデッド | undead | |
| ブレス | breath | `炎のブレスを吐く` → *breathing fire* |
| 石化能力 | petrifying power / petrification | both forms used; the noun where a row will not take the adjective |
| 触手 | tentacles | |
| 粘液状 / ゼラチン状 | slimy / gelatinous | keep the two distinct — they are two different classes |
| 怪力無双 | matchless might | |
| 暗殺猫 | assassin cat | |
| 額に宝石 | a gem in its brow | the `謎の生物` entry; **Gem** stays capitalised only as the pickup (§3), lowercase here — it is an ornament, not the item |
| 加護 | blessing | `加護を得た` → *blessed by*. Recurs on three weapon entries and the shadow dragon |
| 機械兵 ＮＮ号機 | machine soldier Unit ＮＮ | 号機 → **Unit**, per ４号機 → Ｕｎｉｔ　４ (§11.2); digit full-width |
| 量産型 / 試作機 / 改良型 / 最終型 | mass‐produced / prototype / improved / final | four distinct model words |
| 乱射タイプ | Barrage | the scatter-fire machine line |
| 自走砲 / 固定砲 / 無人砲台 | Self‐propelled Gun / Fixed Gun / turret | the first two are numbered dev placeholders (`です！`) and keep the `Ｔｈｉｓ　ｉｓ` frame of ダミーぶきです |
| パーティーアタック / パーティアタック | party attack | both spellings, one English form |
| パワーＵＰ | plain English (*more power*, *raises … power*) | the full-width caps are Japanese emphasis on a loanword; per ＨＩＴ → *hits* (§3), English needs none |
| 攻撃力＋ＮＮ (weapon stat row) | Ａｔｋ＋ＮＮ | **stat row only** — prose keeps *attack power* (§4). `Ａｔｔａｃｋ＋１０　Ｇｅｍ　Ｔｙｐｅ：Ｇｒｅｅｎ` is exactly 24 columns; `Ａｔｋ` holds every stat row at ≤ 21. See FLAGS |

## 5. Verbal tics — decided, never mix

| Japanese | English | Note |
|---|---|---|
| ノロ (sentence-final) | trailing **`，　ｎｙｏｒｏ．`** | hobbit shopkeeper. Appended to the final clause of each sentence, replacing that sentence's own full stop. Mechanical by design, so duplicated lines stay byte-identical. ⚠️ **Corrected 2026-09-08 (§4.3) — the space after the comma is required; the entry previously read `，ｎｙｏｒｏ．`. See §18.1.** The stop still follows the source: `，　ｎｙｏｒｏ，` on a clause the source ends in `、` |
| ゲロゲロ | **`Ｒｉｂｂｉｔ`** + the source's own punctuation | **not only the frog merchant** — the ch.10 lizardmen use it too, and the punchline of that chunk turns on it. The *word* is fixed; the stop that follows is whatever the source has (`。` → `．`, `！` → `！`), and inside the ch.10 joke it is quoted: `“Ｒｉｂｂｉｔ”` |
| katakana speech (lizardmen, frog merchant) | blunt, article-dropping English | `オ前タチ、強イカラ` → `Ｙｏｕ　ｓｔｒｏｎｇ，　ｓｏ`. Drop articles always; drop the copula in short predicative statements; keep the verb where a negation needs it (`Ｗｅ　ａｒｅ　ｎｏｔ　ｌｉｚａｒｄｓ．`) |

## 6. Stock phrases and interjections

| Japanese | English | Note |
|---|---|---|
| 命拾いしたな | Ｙｏｕ　ｋｅｅｐ　ｙｏｕｒ　ｌｉｖｅｓ．．． | recurs across chunks — match it every time; preserve each instance's own dot count |
| よし、次はコーカサスだ。先を急ごう！ | `Ｒｉｇｈｔ，` / `Ｃａｕｃａｓｕｓ　ｉｓ　ｎｅｘｔ．` / `Ｌｅｔ’ｓ　ｈｕｒｒｙ　ｏｎ！` | three `{FFFE}` segments. 4 occurrences across chunks 10 and 11 — verified byte-identical |
| 私たち沼を侵したりするつもりはなかった | `Ｗｅ　ｎｅｖｅｒ　ｍｅａｎｔ　ｔｏ` / `ｉｎｔｒｕｄｅ　ｏｎ　ｙｏｕｒ　ｓｗａｍｐ．` | ch.10, 3 occurrences across two speakers; the `の` / `のよ` variants get the same English |
| ソノ事、モウ気ニシナイ。… | `Ｔｈａｔ　ｍａｔｔｅｒ，　ｆｏｒｇｏｔｔｅｎ．` / `Ｙｏｕ　ｓｔｒｏｎｇ，　ｓｏ` / `ｗｅ　ｗｅｌｃｏｍｅ　ｙｏｕ．` / `Ｃｏｍｅ　ｂｙ　ａｎｙ　ｔｉｍｅ．` | ch.10, 2 occurrences |
| 俺たちは兄弟。… | `Ｗｅ　ａｒｅ　ｂｒｏｔｈｅｒｓ．` / `Ｔｏｇｅｔｈｅｒ　ｉｎ　ａｌｌ　ｔｈｉｎｇｓ！` / `Ｉｎ　ｌｉｆｅ　ａｎｄ　ｉｎ　ｄｅａｔｈ．` | ch.34, 2 occurrences |
| ・・・・！？ | ．．．．！？ | ch.10 and ch.11, 2 occurrences |
| ムムッ | Ｈｍｐｈ | grunt |
| ふっ / フンッ | Ｈｍｐｈ | both scoffs collapse to the same English — deliberate |
| ほう / ほお | **Ｏｈ** | impressed grunt; **distinct** from the Ｈｍｐｈ pair. Was `Ｈｏｈ`; **§10.6 is now resolved in favour of chunk 0's `Ｏｈ`** — ch.35 line 13 still needs the edit. Always carries `．．．` or `，` |
| おお | **Ｏｈ** + the source's own punctuation | Hearty exclamation of pleased recognition (`おお！` → `Ｏｈ！`). **Decided 2026-09-08, see §18.2.** Not `Ｏｈｏ` — §10.6 already rejected a transliterated grunt (`Ｈｏｈ`) for the neighbouring ほう, and none remains in `tl/`. The four members of this set are held apart by their punctuation, not by four different words: ほう / ほお → `Ｏｈ` (with `．．．` or `，`), おや → `Ｏｈ？`, **おお → `Ｏｈ！`**, あ、 → `Ａｈ，` |
| む | Ｈｍ | shorter, more sceptical grunt (ch.12) |
| まったく | Ｒｅａｌｌｙ， | exasperation / contempt |
| ふう | Ｐｈｅｗ， | relief |
| グッ / ぐわっ | Ｇｕｈ / Ｇｗａｈ | pain, then the death cry |
| はっ (military assent) | Ｓｉｒ | a recruit answering an officer |
| いいな！！ / わかったなっ！！ | Ｇｏｔ　ｉｔ！！ / Ｇｏｔ　ｔｈａｔ！！ | keep the two distinct, they are different source strings. **Do not** use either for a plain 分かった — that is `Ｒｉｇｈｔ，` |
| 行くぞ！ | Ｍｏｖｅ　ｏｕｔ！ | |
| ああ (assent) | **Ｙｅａｈ　from a casual, contraction-taking speaker; a register-appropriate formal assent from a contraction-free one** | ⚠️ **CONDITION ADDED IN PLACE 2026-09-09 (§4.3, PR #27 review) — the row already said "casual agreement from a rough speaker", and that scope is now binding rather than descriptive; see §43.1.** `Ｙｅａｈ` is unchanged for every speaker it already covers. **Distinct** from はっ → Ｓｉｒ (military assent) and from 分かった → `Ｒｉｇｈｔ，`. ✅ **`tl/battle/chunk_000.txt` line 4 is now fixed** (2026-09-08): it rendered `ああ。` as `Ｙｅｓ．`. 4 → 5 columns, +2 bytes, standalone row so nothing re-flows. **No `Ｙｅｓ` for ああ remains in `tl/`, and none is reintroduced** — Rimul's formal assent is `Ｉ　ｄｏ．` (§43.1), not `Ｙｅｓ．`. See §18.3 and §43.1 |
| 何だと？ / なんだと？ | Ｗｈａｔ　ｗａｓ　ｔｈａｔ？ | Incredulous. The kanji and kana spellings are different source strings but take the same English; `何だと！？` keeps its own `！？` |
| だまれ | Ｓｉｌｅｎｃｅ | An officer cutting a subordinate off. Not "shut up" — the register is command, not brawl |

## 7. Register per character

| Who | Register |
|---|---|
| Kain, the player character | casual; contractions freely (`ｄｏｎ’ｔ`, `ｉｔ’ｓ`, `ｌｅｔ’ｓ`) |
| Rimul | formal, measured, no contractions in her own lines |
| Officers addressing the 9th Army | gruff, imperative, clipped |
| Ridge | blunt and needling; the shortest line in any exchange is usually his |
| Maya | arch, coquettish; **third-person self-reference is kept in English** (`ｌｅｔ　Ｍａｙａ　ｐｌａｙ　ｗｉｔｈ　ｙｏｕ`) except where the source itself switches to 私 |
| Shiron | rough and warm; contractions, `Ｉ’ｖｅ`, `ｃａｎ’ｔ`; addresses the player informally |
| Beatrice | crisply formal, military; no contractions |
| Kasim and Tasim | simple, doubled, comic; their paired lines echo but never match exactly |
| Village elders (じゃ / のう) | plain and old-fashioned, no contractions, no archaic English spelling |
| The Caucasus mayor | polite, slightly fussy; `Ｉ　ａｍ`, not `Ｉ’ｍ` |
| Lizardmen / frog merchant | see §5 — blunt, article-dropping |
| Tutorial boxes (`{=FA1000300030}`) | plain instructional second person, no personality |

## 8. Fixed-width caps

| Table | Cap |
|---|---|
| player name (`{FC00}{=0000}`) | 7 characters — budget 7 columns wherever it appears |
| unit names | ≤ 16 half-width characters |
| class names, monster names | ≤ 20 half-width characters |

New unit-table candidates all clear the ≤ 16 cap as written: Ridge (5), Maya (4), Shiron (6),
Beatrice (8), Kasim (5), Tasim (5).

⚠️ The class *names* have not been fixed yet — §4 above covers only the description prose. Set them
before any chunk that displays a unit roster.

---

## 9. PROVISIONAL — seen in the dumps, not yet rendered

Do not treat these as decisions. Promote on first use.

| Japanese | Likely English | Where seen | Alt spellings / promotion note |
|---|---|---|---|
| ~~メルザリオ~~ | ✅ **PROMOTED to §20.1** — `Ｍｅｌｚａｒｉｏ`, and it is a **PLACE**, not the chief's son; this row's original description was wrong | battle chunk 2 (PR #3) |
| ~~ティミー~~ | ✅ **PROMOTED to §11.1** — `Ｔｉｍｍｙ`, rendered in ch.43 and again in `tl/battle/chunk_004.txt` (PR #6). This row was stale; struck 2026-09-08 | battle chunk 4, ch.43 |
| ~~サイクス~~ | ✅ **PROMOTED to §20.1** — `Ｓｙｋｅｓ` (§18.4) | battle chunk 2 (PR #3) |
| ~~宮廷第２軍~~ | ✅ **PROMOTED to §20.1** — `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ`, both source spellings | battle chunk 2 (PR #3) |
| リザードマン | Lizardman | `script_unique` 1297; the ch.10 dragonfolk are presumably this class |
| ~~レバーク~~ | ✅ **PROMOTED to §28.1** — `Ｌｅｖｅｒｋ`, rendered in `tl/battle/chunk_013.txt` (PR #10). ⚠️ **This row's description was wrong: it is a KINGDOM, not "a castle Maya has left"** — corrected at §28.1 with the dump evidence. `Ｒｅｂａｒｋ` rejected at review | `script_unique` 1350, ~~a castle Maya has left~~ |
| オーク | Orc | monster class |
| ブラウニー | Brownie | monster class |
| 鬼 / 悪鬼 | ogre / fiend | monster classes; 悪鬼 glossed as 豚顔 (pig-faced) |
| 巨人 | giant | monster class |

**Wave 1 seeds (2026-09-08) — battle chunks 1, 2, 3 and script batch 004.** Proposed forms follow
the conventions already fixed: European readings (§11.4, §14), the divine-name pattern set in
batch 003 (`魔神ルシファ` → *the demon god Ｌｕｃｉｆｅｒ*, `アポロン神` → *the god Ａｐｏｌｌｏ*,
`女神アルテミス` → *the goddess Ａｒｔｅｍｉｓ*), and the species test (§17.1).

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| ~~アルベール~~ | ✅ **PROMOTED to §20.1** — `Ａｌｂｅｒｔ`, Fernando's subordinate | battle chunk 2 (PR #3) | — |
| ~~シャスタ~~ | ✅ **PROMOTED to §21.1** — `Ｓｈａｓｔａ` | battle chunk 3 (PR #1) | — |
| ~~マーベル~~ | ✅ **PROMOTED to §21.1** — `Ｍａｒｖｅｌ (person)` | battle chunk 3 (PR #1) | — |
| ~~マーベラス~~ | ✅ **PROMOTED to §21.1** — `Ｍａｒｖｅｌｌｏｕｓ (town)` | battle chunk 3 (PR #1) | — |
| ~~ファイバー~~ | ✅ **PROMOTED to §21.1** — `Ｆｉｂｅｒ` | battle chunk 3 (PR #1) | — |
| ~~コーネフ~~ | ✅ **PROMOTED to §21.1** — `Ｋｏｒｎｅｆｆ` | battle chunk 3 (PR #1) | — |
| ~~探検家~~ | ✅ **PROMOTED to §21.1** — `explorer` | battle chunk 3 (PR #1) | — |
| ~~魔神ティール~~ | ✅ **PROMOTED to §22.1** — `the demon god Ｔｙｒ` | script batch 004 (PR #4) | — |
| ~~軍神オーディン~~ | ✅ **PROMOTED to §22.1** — `the war god Ｏｄｉｎ` | script batch 004 (PR #4) | — |
| ~~雷神~~ | ✅ **PROMOTED to §22.1** — `the thunder god`, 6 entries identical | script batch 004 (PR #4) | — |
| ~~守護をもたらす~~ | ✅ **PROMOTED to §22.1** — `〜‐ｗａｒｄｉｎｇ`, byte-identical in all six | script batch 004 (PR #4) | — |
| ~~ブヒ / ブヒィィィィ~~ | ✅ **PROMOTED to §19.1** — rendered `Ｏｉｎｋ` / `Ｏｉｎｋｋｋｋ` in `tl/battle/chunk_001.txt` (PR #2, merged 2026-09-08) | battle chunk 1 | — |

**Wave 2 seeds (2026-09-08) — battle chunks 4, 6, 9 and script batch 005.** Proposed forms follow
the European-reading convention (§11.4, §14, §17.3) and the species test (§17.1).

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| ~~リオン~~ | ✅ **PROMOTED to §1** — `Ｌｅｏｎ`, rendered in `tl/battle/chunk_006.txt` (PR #7). **Discharges §10.1** | battle chunk 6 | — |
| ~~カペラ~~ | ✅ **PROMOTED to §24.1** — `Ｃａｐｅｌｌａ` | battle chunk 6 (PR #7) | — |
| ~~カザロフ~~ | ✅ **PROMOTED to §24.1** — `Ｋａｚａｒｏｖ` | battle chunk 6 (PR #7) | — |
| ~~マーティン~~ | ✅ **PROMOTED to §24.1** — `Ｍａｒｔｉｎ` | battle chunk 6 (PR #7) | — |
| ~~パーシバル~~ | ✅ **PROMOTED to §24.1** — `Ｐｅｒｃｉｖａｌ` | battle chunk 6 (PR #7) | — |
| ~~ディール帝国~~ | ✅ **PROMOTED to §25.1** — the `Ｄｉｅｌ` Empire, rendered in `tl/battle/chunk_009.txt` (PR #5), used exactly as seeded | battle chunk 9 | — |
| ~~ワーウィック~~ | ✅ **PROMOTED to §25.1** — `Ｗａｒｗｉｃｋ`, rendered in `tl/battle/chunk_009.txt` (PR #5), used exactly as seeded | battle chunk 9 | — |
| ~~クロスリー~~ | ✅ **PROMOTED to §30.1** — `Ｃｒｏｓｓｌｅｙ`, rendered **5 times** in `pending/chunk_017.txt` (PR #12), **used exactly as seeded**; 8 columns confirmed at review | ~~**New seed, 2026-09-08 (PR #5 review)** — surfaced while verifying `クリミア`, and **not chunk 9's business**: chunk 9 does not render it. A **place**, on the same evidence test §2 applied to ファリーナ — `クロスリーの守備隊` (its garrison), `クロスリーの丘` (its hills), `クロスリーを通らずに` (without passing through it), `クロスリーまで伝令を送って` (send a messenger *to* it), `クロスリーに向かう` (head *to* it), and `クロスリーにいるクリミア博士` (Doctor Crimea, who is *in* it). **8 battle + 2 script occurrences, none a person.** 8 columns | Ｃｒｏｓｌｅｙ, Ｋｕｒｏｓｕｒｉ. Promote in the wave that first renders it |
| ~~弓使い~~ | ✅ **PROMOTED to §24.2 as `ｂｏｗｍａｎ`**, not the seed's `archer` — the seed's own “consider `bowman`” note was taken, and ratified at review | battle chunk 6 (PR #7) | — |
| ~~バトウ~~ | ✅ **PROMOTED to §26.1** — `Ｂａｔｏｕ`, and `バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ` per §24.1, rendered in `tl/script/batch_005.tsv` (PR #8). Used exactly as seeded | script 1041, 1045 | — |
| ~~リース文明~~ | ✅ **PROMOTED to §26.1** — the `Ｒｅｅｓｅ` civilisation, used exactly as seeded (PR #8). ⚠️ **The 古代ハイランド warning is DISCHARGED: they are NOT the same.** Counted at that review — `リース` 8 script / 0 battle, `ハイランド` 2 script / 9 battle, **zero lines in either dump contain both**. §11.2's ancient Highland row is untouched and stays | script 1047 | — |
| ~~クレウス司教~~ | ✅ **PROMOTED to §26.1** — Bishop `Ｃｒｅｕｓ` (PR #8) | script 1047 | — |
| ~~キエーザ~~ | ✅ **PROMOTED to §42.1** — `Ｋｉｅｓａ`, 5 columns, rendered **twice** in `tl/script/batch_008.tsv` (DATA 512) as `ｔｈｅ　ｓｗａｍｐ` / `ｏｆ　Ｋｉｅｓａ．` and `ｓｏｕｔｈ　ｏｆ` / `Ｋｉｅｓａ．`, **used exactly as seeded** and the first rendering anywhere. ⚠️ **This row's question is answered only in the negative and stays open for `キエーザ城`**: the unit names a swamp and a direction and gives **no** religious evidence, so `Ｃｈｉｅｓａ` is not taken — but nothing here rules it out either. See §42.1 | ~~script 1090, 1092 — `キエーザ城`, a castle~~ | Ｃｈｉｅｓａ — which is Italian for *church*, so the name may be deliberate; check whether the castle is a religious site before fixing |
| ~~ルクレール~~ | ✅ **PROMOTED to §28.1** — `Ｌｅｃｌｅｒｃ`, used exactly as seeded, rendered in `tl/battle/chunk_013.txt` (PR #10). ⚠️ **This row's description was wrong: it is a KINGDOM, not "a castle"** — corrected at §28.1 with the dump evidence | script 1090, 1096 — `ルクレール城`, ~~a castle~~ | Ｌｕｃｌｅｒｅ. The French reading matches the European naming |
| ~~ＺＯＣ（支配地域）~~ | ✅ **PROMOTED to §26.3** — used exactly as seeded (PR #8) | script 984 | — |
| ~~中立ユニット~~ | ✅ **PROMOTED to §26.3** (PR #8) | script 988 | — |
| ~~前衛 / 後衛~~ | ✅ **PROMOTED to §26.3** — front line / rear line, with one width variant `ｉｎ　ｆｒｏｎｔ` / `ｂｅｈｉｎｄ` flagged (PR #8) | script 985 | — |
| ~~『説得』 / 『ＧＵＥＳＴ　ＵＮＩＴ』 / 「ＥＮＴＥＲ」~~ | ✅ **PROMOTED to §26.3** — used exactly as seeded (PR #8), the last two reproduced not re-cased. ⚠️ **`FLAGS.md` §I1 is now SETTLED** by that review, and these three are the rows that settled it | script 986–988 | — |
| ~~司教~~ | ✅ **PROMOTED to §26.1** — Bishop, spelled out like Commander / Captain / Doctor (PR #8) | script 1047 | — |
| ~~報奨金~~ | ✅ **PROMOTED to §24.2** — `ｒｅｗａｒｄ`, rendered in battle chunk 6 (PR #7) before script 991 reached a batch | script 991, battle chunk 6 | — |
| ~~同盟~~ | ✅ **PROMOTED to §26.3** — alliance (PR #8) | script 999–1001 | — |
| ~~ホアグ王子~~ | ✅ **PROMOTED to §39.1 (PR #24)** — `Ｐｒｉｎｃｅ　Ｈｏａｇ` / `Ｈｏａｇ`, **used exactly as seeded**, the first rendering in the project. Original seed note follows: **New seed, 2026-09-08 (PR #8 review)** — surfaced while verifying `アップミーズ`, and **not batch 005's business**: that batch does not render it. Carline's first prince, Cavia's elder brother (`私の兄でもあるホアグ王子`), the man who built Apumizu (`ホアグ王子がつくった街`), and a target of Helfer's (`奴らにはホアグとともに舞台から下りてもらう`). **6 battle + 16 script occurrences.** ~~10 columns with the title~~ ⚠️ **11 with the title** (corrected in place 2026-09-09, §4.3, PR #23 review — this row read 10 and is one **LOW**, the opposite direction to every other width error this wave; `len('Ｐｒｉｎｃｅ　Ｈｏａｇ')` = 11), 4 bare | Ｈｏａｇｕ, Ｈｏｇ. Promote in the wave that first renders it |
| トリフ | `Ｔｏｒｉｆ` | **New seed, 2026-09-08 (PR #8 review)**, same sweep. Hoag's younger brother (`弟のトリフ`), whom Helfer prefers as the more pliable heir. **9 battle + 6 script occurrences.** 5 columns | Ｔｒｉｆ, Ｔｏｌｉｆ. Promote in the wave that first renders it |
| ~~シェルビー~~ | ✅ **PROMOTED to §29.1** — `Ｓｈｅｌｂｙ`, a PLACE, rendered four times in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~カーゴ~~ | ✅ **PROMOTED to §29.1** — `Ｃａｒｇｏ`, the proper name of a machine, rendered twice in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded; the `ｔｈｅ　ｃａｒｇｏ` trap was avoided** | battle chunk 8 | — |
| ~~プロキオン~~ | ✅ **PROMOTED to §29.1** — `Ｐｒｏｃｙｏｎ`, rendered in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~ルート~~ | ✅ **PROMOTED to §29.1 (chunk 8) and STRUCK HERE at chunk 17's merge (PR #12).** `ｒｏｕｔｅ`, lowercase, rendered twice in **each** of the two units, exactly as seeded. **The cross-unit rule is discharged**: chunk 8 merged first and deliberately left this row live, chunk 17 merged second and strikes it, which is the whole of what that rule prescribes. See §30.1 | ~~**Wave-3 seed — CROSS-UNIT (chunks 8 and 17), lowercase common noun** per the バジリスク → basilisk precedent (§17.1 species test): `敵は別のルートから来たようです` (chunk 17 L3) and `ここへ抜けるルートは、バージェス峡谷か南の砂漠` (chunk 17 L4). **4 battle (ch8 L9 ×2, ch17 L3, L4) + 8 script.** 5 columns | Not `Ｒｏｕｔｅ`; not `ｐａｔｈ` where the source says ルート | ⚠️ **RENDERED by chunk 8 (PR #11, merged) as `ｒｏｕｔｅ`, twice, exactly as seeded — this row is DELIBERATELY LEFT LIVE.** Chunk 17 (PR #12) renders it too and merges second; per the wave's cross-unit rule it is struck once, by that reviewer. See §29.1
| ~~スパイ~~ | ✅ **PROMOTED to §29.1** — `ｓｐｙ`, lowercase, rendered twice in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~アーバイン様~~ | ✅ **PROMOTED to §28.1** — `Ｌｏｒｄ　Ｉｒｖｉｎｅ`, rendered in `tl/battle/chunk_013.txt` (PR #10). ⚠️ **This row's widths were both one too many** — `Ｉｒｖｉｎｅ` is **6** columns and `Ｌｏｒｄ　Ｉｒｖｉｎｅ` is **11**, not 7 and 12. The seed was mine and it was wrong; the translator caught it and I remeasured on the shipped row (`Ｌｏｒｄ　Ｉｒｖｉｎｅ！` = 12 with the mark). The rendering is unchanged | **Wave-3 seed** — an enemy commander (chunk 13 L2, `アーバイン様！敵襲です！！`), addressed 様 by a subordinate; masculine, authoritative register (`まあよい`, `叩き潰してやれ！！`). 様 → Lord on the `リムル` / `フィリス様` precedent (§14.1), **not** §21.2's さん rule. **1 battle + 0 script.** ~~7 columns bare, 12 with the title~~ | Ｕｒｂａｉｎ, Ｅｒｂｉｎｅ |
| ~~バージェス~~ | ✅ **PROMOTED to §30.1** — `Ｂｕｒｇｅｓｓ` / `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ`, rendered in `pending/chunk_017.txt` (PR #12), used exactly as seeded. ⚠️ **This row's widths are both one too many** — `Ｂｕｒｇｅｓｓ` is **7** columns and `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` is **14**, not 8 and 15; remeasured at review. Rendering unchanged | ~~**Wave-3 seed** — a **PLACE**, on the §2 test: `バージェス峡谷か南の砂漠` (a route out, chunk 17 L4) and `バージェスからの定期連絡` (regular reports *from* it, chunk 17 L5). Capitalised as a place name on the `バジリスクの砂漠` → *the Basilisk Desert* precedent (§2). **2 battle (chunk 17) + 5 script.** 8 columns bare, 15 with Ｃａｎｙｏｎ | `Ｂｕｒｇｅｓｓ　Ｇｏｒｇｅ` also 15 — 峡谷 is literally a gorge; either fits. Rendered by chunk 17 — promote on merge |
| ~~イフリート~~ | ✅ **PROMOTED to §30.1** — `Ｉｆｒｉｔ`, capitalised, rendered in `pending/chunk_017.txt` (PR #12), **used exactly as seeded**; 5 columns confirmed. ⚠️ **The chunk-15 gloss warning stays live for whoever takes chunk 15** | ~~**Wave-3 seed. A named FORTRESS GUN, not a monster and not a person** — so the §17.1 species test does **not** apply and it stays capitalised. ⚠️ **The gloss is in chunk 15, not in chunk 17**: chunk 15 L1 has `この巨大砲台イフリートの前には、カーライン軍など風の前の塵に同じ！！` (*this giant gun emplacement Ifrit*) and `紅蓮の炎で焼き尽くしてくれるわっ！` (the fire association the name carries). **Chunk 17 L5 renders only `・・・イフリートが落とされたか。`** — without this row its translator cannot tell what Ifrit is. **2 battle (ch15 L1, ch17 L5) + 3 script.** 5 columns | Ｅｆｒｅｅｔ, Ｉｆｒｅｅｔ. Rendered by chunk 17 — promote on merge |
| ~~マムー~~ | ✅ **PROMOTED to §30.1** — `Ｍａｍｕ`, **with no `Ｌｏｒｄ`**, rendered in `pending/chunk_017.txt` (PR #12); 4 columns confirmed. The self-reference warning was heeded exactly. ✅ **The `マムー兄さん` note is DISCHARGED 2026-09-10: chunk 41 renders it `Ｂｒｏｔｈｅｒ　Ｍａｍｕ` (PR #30), exactly as reserved** | ~~**Wave-3 seed** — a **PERSON**, male. ⚠️ **`このマムー様が` (chunk 17 L7) is boastful SELF-reference, not an honorific from a subordinate** — the `このクリミアに` pattern (§25.1) — so it takes **no** `Ｌｏｒｄ`; put the swagger in the verb (`ぜ`, §7), not in a title. `マムー兄さん` → `Ｂｒｏｔｈｅｒ　Ｍａｍｕ` is **chunk 41's** line, not chunk 17's. **2 battle (ch17 L7, ch41 L5) + 0 script.** 4 columns | Ｍａｍｍｏｏ, Ｍａｍｕｕ. Rendered by chunk 17 — promote on merge |
| ~~フェミナ~~ | ✅ **PROMOTED to §30.1** — `Ｆｅｍｉｎａ`, rendered in `pending/chunk_017.txt` (PR #12); 6 columns confirmed. **The relation this row asked to be confirmed IS confirmed from inside the chunk** — see §30.5 | ~~**Wave-3 seed** — a **PERSON**, female, already dead when named: `フェミナ、ごめんね。あんたの仇、とれなかったよ・・・` (chunk 17 L24 — *sorry, I could not avenge you*). Almost certainly the murdered sister of chunk 17 L6–7's `あんたの妹を殺した奴ら` / `カーライン第９軍・・・まちがいない`; chunk 17's translator should confirm the relation from the full chunk before leaning on it. **1 battle + 0 script.** 6 columns | Ｆｅｍｉｎａｈ. Rendered by chunk 17 — promote on merge |

**Wave 4 seeds (2026-09-08) — battle chunks 18, 19, 20 and script batch 002.** Proposed forms
follow the European-reading convention (§11.4, §14, §17.3), the species test (§17.1), the plain-
transliteration precedent set by `ネルガリ` → `Ｎｅｒｇａｌｉ` (§17.4 — the transliteration is
preferred over the mythological source the kana point at), and the `『…』` → `“…”` rule fixed by
`『知識の書』` (§12). **All widths below were measured, not estimated** — wave 3 shipped two seeds
whose hand-counted widths were each one column too many (§9, アーバイン様 and バージェス rows).

⚠️ **FOUR OF THESE TERMS ARE CROSS-UNIT between chunks 19 and 20, which are being translated in
parallel in this wave.** `火の水晶` (c19 ×4, c20 ×1), `アリエス` (c19 ×1, c20 ×3), `カバラ`
(c19 ×4, c20 ×1) and `ヒューゴー` (c19 ×1, c20 ×1). CLAUDE.md §3 requires byte-identical English
across files, so **both translators must render these exactly as seeded here** rather than each
choosing. Per the `ルート` precedent (§29.1/§30.1) the row is struck once, by the **second** of the
two reviewers to merge — the first deliberately leaves it live.

✅ **STATUS 2026-09-09, FINAL — the cross-unit rule is DISCHARGED and all eight wave-4 battle seeds
are struck.** Chunk 20 (PR #14) merged first and deliberately left the four cross-unit rows live;
chunk 19 (PR #16) merged **second**, at `aecea69`, and strikes them here — which is the whole of
what the `ルート` precedent (§29.1 / §30.1) prescribes. Struck at that merge: the four cross-unit
rows (`アリエス`, `ヒューゴー`, `カバラ`, `火の水晶`) **plus the four chunk-19-only seeds**
(`ソロン`, `ノーマン`, `トレジャーハンター`, `傭兵団`), all eight promoted to §33.1 and **all eight
used exactly as seeded by both translators — not one was improved on unilaterally.**

✅ **The `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` contingency never fired.** This note previously warned that tier-B
chunk 19 (ratio 1.94) might be unable to fit `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` (15) and would drag chunk 20
onto the short form. It fitted: chunk 19's four rows measure **18 / 18 / 21 / 21** and the unit
shipped with **127 bytes of slack**, so **the long form stands in both units and neither was
re-cut.**

⚠️ **A FIFTH term belonged on this list and the seed missed it: `宝石`** (c19 ×1, c20 ×4, c31 ×1),
with `宝` / `お宝` beside it — ruled `ｇｅｍｓｔｏｎｅ` at chunk 19's review and shipped consistently by
both units. **It has no §9 row to strike** because it was never seeded; the entries are §32.1 and
§33.1. **Chunk 31 inherits `ｇｅｍｓｔｏｎｅ`.**

✅ **STATUS 2026-09-09 — the wave-4 SCRIPT seeds are struck too, and the whole wave-4 block is now
clear.** `batch_006.tsv` (PR #15) merged last and renders all four of the script seeds — `デビルズラック`,
`オイラ`, `ハッピー` and `親方` — **every one exactly as seeded, not one improved on unilaterally**,
including the two the seed argued hardest for: `ハッピー` lowercase in both instances so the repetition
stays byte-identical, and `オイラ` carried as register with no pronoun and no dialect spelling. They are
promoted to **§34.1** and struck below. ⚠️ **`親方`'s drift warning against §32.1's `おかしら` → `Ｂｏｓｓ`
is DISCHARGED**, not merely heeded — §25.3's test was counted at review and is met in both dimensions.
⚠️ **The seed block's "script batch 002" is the queue POSITION, not the filename**: the unit was written
to `batch_006.tsv`, `batch_002.tsv` having shipped in wave 1.

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| ~~アリエス~~ | ✅ **PROMOTED to §33.1** — `Ａｒｉｅｓ`, rendered once in `tl/battle/chunk_019.txt` (PR #16) and three times in `tl/battle/chunk_020.txt` (PR #14), **used exactly as seeded in both**. ⚠️ **This is one of the four CROSS-UNIT rows §9 deliberately left live at chunk 20's merge; chunk 19 merged second and strikes it**, per the `ルート` precedent (§29.1 / §30.1) | **CROSS-UNIT — chunk 19 L1, chunk 20 L47/L48 (×3).** A **PERSON**, female, and a travelling performer: asked `アリエスさんは、ファリーナは初めて？` she answers `いいえ。旅の巡業で何度か来たことが。` (*no — I have come a few times, touring*). Polite です/ます register. **11 battle + 9 script occurrences — the most-used new name in this wave.** 5 columns | — |
| ~~ソロン~~ | ✅ **PROMOTED to §33.1** — `Ｓｏｌｏｎ`, rendered three times in `tl/battle/chunk_019.txt` (PR #16), **used exactly as seeded** | chunk 19 L24 (×3). A **PERSON**, male — an imperial soldier recognised by his elder brother: `ソロン！？ソロンじゃねぇか！！` … `実の兄貴の頼みだ。手を貸そう。` **3 battle + 0 script.** 5 columns | — |
| ~~ヒューゴー~~ | ✅ **PROMOTED to §33.1** — `Ｈｕｇｏ`, rendered once in each of chunks 19 and 20, **used exactly as seeded in both**. **CROSS-UNIT row, struck at chunk 19's second merge** | **CROSS-UNIT — chunk 19 ×1, chunk 20 L1 ×1.** A **PERSON**, male, named dismissively by a rival imperial officer: `ふふっ、ヒューゴーの奴、今ごろ　ファリーナを探索しておるんだろうが、見当違いもいいところだ。` **2 battle + 0 script.** 4 columns | — |
| ~~ノーマン~~ | ✅ **PROMOTED to §33.1** — `Ｎｏｒｍａｎ`, rendered once in `tl/battle/chunk_019.txt` (PR #16), **used exactly as seeded** | chunk 19 ×1 (`ほう。ノーマン、よければ、話して差し…`). A **PERSON**, male, of Farina; the main script has him leading the rebuilding afterwards (`今は、ノーマンさんたちがふっこーにはげん…`). **1 battle + 3 script.** 6 columns | — |
| ~~カバラ~~ | ✅ **PROMOTED to §33.1** — `Ｋａｂａｌａ`, rendered four times in chunk 19 and once in chunk 20, **used exactly as seeded in both**, with `盗賊カバラ` → `ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` ratified at chunk 19's review. **CROSS-UNIT row, struck at chunk 19's second merge** | **CROSS-UNIT — chunk 19 ×4, chunk 20 L47 ×1.** A **PERSON**, male, a **dead bandit** whose hoard is this chapter's object: `カバラという盗賊の手に渡ったと聞きます`, `そのカバラも帝国に追われて、もうこの世に…`, `このカバラの財宝を捜しているトレジャーハンター`, `これも、盗賊カバラのお宝のひとつか。` `盗賊カバラ` → `ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` (17 columns). **5 battle + 0 script.** 6 columns bare | — |
| ~~火の水晶 / 『火の水晶』~~ | ✅ **PROMOTED to §33.1** — `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` / `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”`, **the LONG form, all five instances across both units** — chunk 19 ×4 (one quoted) and chunk 20 ×1. The seed's warning that tier-B chunk 19 might be forced onto the short `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` **did not materialise**: all four of its rows measure 18 / 18 / 21 / 21 and the chunk landed with 127 bytes to spare, so neither unit was re-cut. **CROSS-UNIT row, struck at chunk 19's second merge** | **CROSS-UNIT — chunk 19 ×4, chunk 20 L47 ×1.** The chapter's plot object, and **an inventory item whose description line is a 21-instance row of the untranslated description table**: `ファリーナに伝わる伝説の水晶。炎のような美しい光を放つ。` (*a legendary crystal handed down in Farina; it gives off a beautiful light like flame*). Chunk 19 carries one instance in `『』` and the rest bare. `『…』` → `“…”` per `『知識の書』` (§12). **5 battle + 22 script.** 15 columns bare, **17 quoted** | — |
| ~~バーストウーズ~~ | ✅ **PROMOTED to §32.1** — `ｂｕｒｓｔ　ｏｏｚｅ`, lowercase, rendered in `tl/battle/chunk_020.txt` (PR #14), **used exactly as seeded**; 10 columns confirmed at review. ⚠️ **This row's citation was wrong: the `グレイウーズ` → `ｇｒｅｙ　ｏｏｚｅ` precedent is at §17.2, not §17.4.** The derivation is unaffected | battle chunk 20 | — |
| ~~トレジャーハンター~~ | ✅ **PROMOTED to §33.1** — `ｔｒｅａｓｕｒｅ　ｈｕｎｔｅｒ`, rendered once in `tl/battle/chunk_019.txt` (PR #16), lowercase, **used exactly as seeded**. The seed's warning held — the dump splits it `トレジャー|ハンター` across a `{FFFE}` | chunk 19 ×1 — the people hunting Kabala's hoard in Marvellous. **Lowercase**: a trade, by the §17.1 species test and the `探検家` → `ｅｘｐｌｏｒｅｒ` precedent (§21.1). ⚠️ **In the dump it is SPLIT across a line break** — `トレジャー|ハンター` — so a naive grep for the whole word finds zero. **1 battle + 0 script.** 15 columns | — |
| ~~傭兵団~~ | ✅ **PROMOTED to §33.1** — `ｍｅｒｃｅｎａｒｙ　ｂａｎｄ`, rendered twice in `tl/battle/chunk_019.txt` (PR #16), **used exactly as seeded**; the seed's shorter `ｍｅｒｃｅｎａｒｉｅｓ` alternative was not taken even under byte pressure | chunk 19 L3 ×2 — `どうやら、傭兵団のようだな。` **2 battle + 0 script.** 14 columns | — |
| ~~おかしら (vs 将校 / 将軍)~~ | ✅ **PROMOTED to §32.1** — `Ｂｏｓｓ` (4) and `将校` → `ｏｆｆｉｃｅｒ` (7), rendered in `tl/battle/chunk_020.txt` (PR #14), **the seed's primary form taken over its `Ｃｈｉｅｆ` alternative**. ⚠️ **The gag SURVIVED and was read against the source at review** — `Ｙｏｕ　ｆｏｏｌ，` / `Ｉ　ａｍ　ａｎ　ｏｆｆｉｃｅｒ　ｏｆ　ｔｈｅ` / `Ｅｍｐｉｒｅ！　Ｃａｌｌ　ｍｅ` / `Ｇｅｎｅｒａｌ！　Ｇｅｎｅｒａｌ！！`, three words still three words, the doubled repeat kept. See §32.4a | battle chunk 20 | — |
| ~~勲章~~ | ✅ **PROMOTED to §32.1** — `ｍｅｄａｌ`, rendered ×2 in `tl/battle/chunk_020.txt` (PR #14); 5 columns confirmed. ⚠️ **This row's reach was badly wrong and its silence on `メダル` cost a review: it is 4 battle (chunks 20 and 22) + 59 `script_dump` / 39 `script_unique`, not "2 battle", and it is the plot item `獅子の勲章` / `『獅子の勲章』`.** The clash with §3's racetrack `メダル` → `ｍｅｄａｌ` is **LIVE in banks 42 and 43** and is NOT discharged — see §32.5 | ~~chunk 20 L47/L48 ×2 — dug up beside the jewels~~ | `ｄｅｃｏｒａｔｉｏｎ` (12) rejected as too vague; `ｔｏｋｅｎ` (5) is the reserve, on the **racetrack** side |
| ~~デビルズラック~~ | ✅ **PROMOTED to §34.1** — `Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ`, **the bare form this row itself preferred**, rendered once in `tl/script/batch_006.tsv` (PR #15) as `Ｉｔ’ｓ　Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ！！`. **Used exactly as seeded**: the line is a predicate nominal and not a title, so the quoted `“…”` alternative correctly did not fire; `’` is U+2019, verified at review. 12 columns | ~~script batch 002 (written to `batch_006.tsv`), unique 631~~ | — |
| ~~オイラ~~ | ✅ **PROMOTED to §34.1** — carried as **register, not rendered as a word**, in all four instances in `tl/script/batch_006.tsv` (PR #15). **Seed followed exactly**: dropped subjects and contractions (`Ａｓ　ｙｏｕ　ｃａｎ　ｓｅｅ，　Ｉ’ｍ　ｈａｐｐｙ！`, `Ｉ’ｍ　ｔｈｅ　ｄｏｇｓｂｏｄｙ`, `Ｙｏｕ　ａｎｄ　ｍｅ　ｇｏ　ｂａｃｋ．`), no dialect spelling, no rendered pronoun | ~~script batch 002 (written to `batch_006.tsv`), unique 632 ×4~~ | — |
| ~~ハッピー~~ | ✅ **PROMOTED to §34.1** — `ｈａｐｐｙ`, rendered twice in `tl/script/batch_006.tsv` (PR #15), **lowercase in BOTH instances so the repetition survives byte-identically** (`Ａｒｅ　ｙｏｕ　ｈａｐｐｙ？` / `Ｉ’ｍ　ｈａｐｐｙ！`). **Used exactly as seeded** — the obvious `Ｈａｐｐｙ？` was rejected precisely so the two would not differ by capitalisation, which is what this row's "the joke is that he keeps saying it" required. 5 columns | ~~script batch 002 (written to `batch_006.tsv`), unique 632 ×2~~ | — |
| ~~親方~~ | ✅ **PROMOTED to §34.1** — `ｔｈｅ　ｂｏｓｓ`, lowercase, rendered twice in `tl/script/batch_006.tsv` (PR #15), **used exactly as seeded**. ⚠️ **This row's warning against drifting into §32.1's `おかしら` → `Ｂｏｓｓ` is DISCHARGED, not merely heeded**: §25.3's test was counted at review and is **MET** — `おかしら` is battle chunk 20 only (×5, 0 script) and `親方` is script bank 12 only (×2, 0 battle), so no chunk, no bank and no message holds both. 7 columns | ~~script batch 002 (written to `batch_006.tsv`), unique 632 ×2~~ | — |

⚠️ **Two corrections the wave-2 units force, both of the メルザリオ kind (§20.1):**

1. ~~**`ファリーナ` is a PLACE, not only a person.**~~ ✅ **DISCHARGED 2026-09-08 (PR #6 review).**
   The row is moved from §1 (People) to §2 (Factions, places, ranks) with the dump evidence
   recorded there. It is a place **only** — no instance in either dump uses it as a personal
   name. `Ｆａｒｉｎａ` is unchanged, so nothing translated needs revisiting. **Moved once; PRs #7
   and #8 flagged it and must not move it again.**
2. ~~**Fernando is `隊長` in the battle script but `将軍` in the main script.**~~
   ✅ **DISCHARGED 2026-09-08 (PR #8 review).** **将軍 → `Ｇｅｎｅｒａｌ`, and the man holds two
   titles** — recorded in §26.2. Decided on a corpus count, not a guess: `フェルナンド将軍` occurs
   **17 times** (6 battle + 11 script) against `フェルナンド隊長`'s **2** (2 battle + 0 script).
   §2's 隊長 → *captain* is untouched, and **nothing shipped is re-cut**: all three shipped
   `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ` were traced to their sources at that review — `chunk_002` ×2
   render `フェルナンド隊長`, `chunk_006` ×1 renders `この宮廷第２軍隊長、フェルナンドめが` — and
   **neither chunk contains a single `将軍`**. Note this discharges *this* item; **§10 question 2,
   the class/unit name table, is a different item and remains open**.

**Wave 5 seeds (2026-09-09) — battle chunks 21, 22 and script batch 007 (unique 318, 421–469).**
Proposed forms follow the conventions already fixed: European readings (§11.4, §14), the species
test (§17.1), the army-number series (§2), and `『…』` → `“…”` (§12). Every width below was
**measured programmatically**, not estimated (wave 3 shipped two seeds a column too wide).

⚠️ **This wave carries THREE two-title officers at once** — the exact shape of §9's discharged
Fernando correction (§26.2, "the man holds two titles"). That case was settled on a corpus count
of 17 against 2. **None of these three has a majority**, so the count does not settle them:

| Officer | Rank A | Rank B | Bare | Reading |
|---|---|---|---|---|
| ライアン | `ライアン少尉` 1 battle | `ライアン隊長` 1 battle | 2 battle / 0 script | **both in THIS wave** — 少尉 in chunk 21, 隊長 in chunk 22, and 21 precedes 22 in chapter order |
| クレス | `クレス少尉` 1 battle + 2 script | `クレス隊長` 1 battle | 7 battle / 4 script | §1 already renders 少尉 → `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ`; chunk 22 is the first 隊長 |
| リオン | `リオン将軍` 1 battle | `リオン隊長` 1 battle + 1 script, `第１軍隊長` 1 script | 7 battle / 14 script | script 427 (**this batch**) has him introduce himself as `第１軍隊長のリオン` |

**Proposal for all three: render each occurrence with the rank the source gives it**, as §26.2
already permits, and do **not** collapse them to one rank. ~~A promotion between chapters is the
likelier reading for ライアン (21 → 22) and is consistent either way.~~ **Do not re-cut shipped
work**; if a shipped file disagrees, record it and leave it to a corrections unit (§4.3).

✅ **RULED 2026-09-09 (PR #19 review), and the struck sentence is why.** The *rendering* proposal is
correct and both units followed it. **The promotion reading is NOT ratified** — chunk 21's `少尉`
comes from an outsider and chunk 22's `隊長` from Ryan's own subordinate, which accounts for both
with no promotion at all. See **§37.4**. Nothing follows from leaving it open, because §26.2's
source-rank rule is correct under either reading.

✅ **STATUS 2026-09-09, FINAL — the wave-5 block is now clear.** `batch_007.tsv` (PR #20) merged
last and renders **twelve** of the script seeds — `第１軍`, `リムローズ`, `イートン`/`イートンの森`,
`チェコットの丘`, `レバーク城`, `兵舎`, `ジャガイモ`/`イモ`, `バター`, `ワイン` (bare),
`とかいじん`, `ナンダイ`, `第２王子のトリフ様` — plus the three UI labels, **every one exactly as
seeded, not one improved on unilaterally**, and it executes the `殿` decision as written. They are
promoted to **§38.1** and struck above. **Two rows deliberately stay live**: `『極上のワイン』`,
which this batch does not render, and the **UI-label block**, which §9 itself says the reviewer must
flag rather than resolve (`FLAGS.md` §Z1). ⚠️ **Four of this block's own figures were wrong and are
corrected in place above** — `リムローズ`'s reach (9 → 10 further, 12 → 11 unique), `ワイン`'s
"24 unique" (→ 18), `ナンダイ`'s width (16 → **14**), and `第２王子のトリフ様`'s cost note; and
⚠️ **the PR's proposed correction to `兵舎`'s "4 script" is itself wrong — this block was right.**
See §38.6.

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| ~~ライアン~~ | ✅ **PROMOTED to §36.1 (chunk 21) and STRUCK HERE at chunk 22's merge (PR #19, `6423083`).** `Ｒｙａｎ`, 4 columns, rendered in **both** units exactly as seeded — `ライアン少尉` → `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ` in chunk 21 (22 bare, 23 in the vocative, one row) and `ライアン隊長` → `Ｃａｐｔａｉｎ　Ｒｙａｎ` (12) in chunk 22. **The cross-unit rule is discharged**: #18 merged first and deliberately left this row live, #19 merged second and strikes it, which is the whole of what the `ルート` precedent (§29.1 / §30.1) prescribes. ⚠️ **The seed's promotion reading is NOT ratified — see §37.4**; both renderings are correct under either reading, so nothing follows from leaving it open | ~~battle chunks 21 + 22, CROSS-UNIT~~ | ~~`Ｌｉａｎ`, `Ｒｉａｎ`~~ |
| ~~ジェイク~~ | ✅ **PROMOTED to §37.1** — `Ｊａｋｅ`, rendered ×2 in `tl/battle/chunk_022.txt` (PR #19), **used exactly as seeded**; 4 columns confirmed at review. **Not cross-unit**: `ジェイク` is battle chunk 22 only, so nothing is left live | ~~battle chunk 22, 2 battle / 0 script~~ | — |
| ~~クレス隊長~~ | ✅ **PROMOTED to §37.1** — `Ｃａｐｔａｉｎ　Ｃｒｅｓｓ`, **used exactly as seeded**; 13 columns confirmed at review. **Not cross-unit**: `クレス隊長` is battle chunk 22 only | ~~battle chunk 22~~ | — |
| ~~リオン将軍~~ | ✅ **PROMOTED to §37.1** — `Ｇｅｎｅｒａｌ　Ｌｅｏｎ`, **used exactly as seeded**; 12 columns confirmed at review. **Not cross-unit**: `リオン将軍` is battle chunk 22 only | ~~battle chunk 22~~ | — |
| ~~バトウ神父~~ | ✅ **PROMOTED to §36.1** — `Ｆａｔｈｅｒ　Ｂａｔｏｕ`, rendered ×3 in `tl/battle/chunk_021.txt` (PR #18), **used exactly as seeded**; 12 columns confirmed at review. **Not cross-unit**: all 3 battle occurrences are in chunk 21 (counted at review — `バトウ` is battle chunk 21 only), so nothing is left live | ~~battle chunk 21, 3 battle / 2 script~~ | — |
| ~~５軍 / 第５軍~~ | ✅ **PROMOTED to §37.1** — `５ｔｈ　Ａｒｍｙ`, 8 columns confirmed. ⚠️ **NOT a first rendering, and this row's own advice pointed at the wrong tree**: `tl/battle/chunk_013.txt` L2 already ships the bare form as `ｔｈｅ　５ｔｈ　Ａｒｍｙ` and chunk 22 **matches it byte-for-byte**. The row said "grep `batch_005`", which the translator did and reported honestly; the reach that mattered was in `tl/battle/`. See §37.3 | ~~5 battle / 3 script~~ | — |
| ~~第１軍~~ | ✅ **PROMOTED to §38.1** — `１ｓｔ　Ａｒｍｙ`, 8 columns confirmed, rendered in `tl/script/batch_007.tsv` (PR #20) in `第１軍隊長のリオン` → `Ｉ　ａｍ　Ｌｅｏｎ，　ｃａｐｔａｉｎ` / `ｏｆ　ｔｈｅ　１ｓｔ　Ａｒｍｙ．`, **used exactly as seeded** | ~~0 battle / 3 script~~ | — |
| ~~リムローズ~~ | ✅ **PROMOTED to §38.1** — `Ｌｉｍｒｏｓｅ`, rendered 4× (PR #20), **used exactly as seeded**; **7 columns confirmed — this row's figure was right** and the PR's own hand-count of 8 was its own error, caught before pushing. ⚠️ **This row's reach was low: 10 further `script_dump` instances (banks 18, 20, 40, 41) + 2 battle (chunk 38)**, remeasured at review; the "12 unique script lines" is 11 | ~~2 battle / 12 unique script lines~~ | — |
| ~~イートン / イートンの森~~ | ✅ **PROMOTED to §38.1** — `Ｅａｔｏｎ` / `Ｅａｔｏｎ　Ｆｏｒｅｓｔ`, 5 / 12 columns, rendered 3× in unique 430 (PR #20), **used exactly as seeded**. The 妖精の森 warning was heeded: unique 430 carries **both** and renders the fairy village lowercase beside the capitalised `Ｅａｔｏｎ　Ｆｏｒｅｓｔ`. Reach confirmed at review: **1 further script instance (bank 40), 0 battle** — 3 rendered + 1, so this row's "4 script" is right | ~~0 battle / 4 script~~ | — |
| ~~チェコットの丘~~ | ✅ **PROMOTED to §38.1** — `Ｃｈｅｋｏｔ　Ｈｉｌｌ`, 11 columns confirmed (PR #20), **used exactly as seeded**. **A true hapax — 0 further occurrences in either dump**, verified at review | ~~0 battle / 1 script~~ | — |
| ~~レバーク城~~ | ✅ **PROMOTED to §38.1** — `Ｌｅｖｅｒｋ　Ｃａｓｔｌｅ`, 13 columns confirmed (PR #20), **used exactly as seeded**. **1 further script instance (bank 41), 0 battle** | ~~0 battle / 2 script~~ | — |
| ~~兵舎~~ | ✅ **PROMOTED to §38.1** — `ｂａｒｒａｃｋｓ`, 8 columns, lowercase, verified free across `tl/` and `pending/` (PR #20), **used exactly as seeded**. ⚠️ **This row's "4 script" is RIGHT.** The PR proposed correcting it to 3; measured at review, `script_dump.txt` holds **4** instances, 1 of them the unit's own → **3 further, 4 in total**. The PR's 3 is the *unique-line* count. See §38.6 | ~~0 battle / 4 script~~ | — |
| ~~ジャガイモ / イモ~~ | ✅ **PROMOTED to §38.1** — `ｐｏｔａｔｏｅｓ` / `ｐｏｔａｔｏ` (PR #20), **used exactly as seeded**; **8 / 6 columns — this row's figures were right** and the PR's hand-count of 9 was its own error, caught before pushing. **0 further occurrences of ジャガイモ** | ~~0 battle / 1 + 6 script~~ | — |
| ~~バター~~ | ✅ **PROMOTED to §38.1** — `ｂｕｔｔｅｒ`, 6 columns, lowercase, verified free (PR #20), **used exactly as seeded**. 0 further occurrences | ~~0 battle / 1 script~~ | — |
| ワイン / ~~ワイン~~ / ~~『極上のワイン』~~ | **The BARE noun is ✅ PROMOTED to §38.1** — `ｗｉｎｅ`, 4 columns, lowercase, rendered 3× in `tl/script/batch_007.tsv` (PR #20), **used exactly as seeded and verified free** (`tl/`'s only hits are *swine*). ✅ **`『極上のワイン』` → `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` (13) IS NOW PROMOTED TO §54 AND STRUCK (PR #35, merged 2026-09-11), used exactly as seeded.** Two units of wave 9 render it, and the `ルート` precedent (§29.1 / §30.1) puts the strike on the **second to merge**: `batch_013` (PR #36) merged first and deliberately left this row live; `batch_012` (PR #35) merged second and strikes it. **Verified byte-identical across both files at PR #35's review** — 4 instances in `batch_012` (DATA 370–373), 2 in `batch_013` — by the cross-file item-name gate, 0 divergences over 45 files. ⚠️ **This row's “44 script-dump instances” is RIGHT** (the PR's “35 further” is six low; measured, 44 total − 3 own = **41 further**); the “24 unique” is 18 | `Ｅｘｑｕｉｓｉｔｅ　Ｗｉｎｅ`, `Ｖｉｎ` rejected |
| ~~とかいじん (都会人)~~ | ✅ **PROMOTED to §38.1** — `ｃｉｔｙ　ｆｏｌｋ`, 9 columns, lowercase (PR #20), **used exactly as seeded**; the hiragana lightness carried in **register**, not in a misspelling, exactly as this row required | ~~0 battle / 1 script~~ | — |
| ~~ナンダイ (難題)~~ | ✅ **PROMOTED to §38.1** — `ａ　ｒｅａｌ　ｐｒｏｂｌｅｍ` (PR #20), **used exactly as seeded**: the katakana emphasis rendered as weight in the English, not transliterated. ⚠️ **This row's width was wrong — it is 14 columns, not 16**, remeasured twice at review | ~~0 battle / 1 script~~ | ~~`ａ　ｔａｌｌ　ｏｒｄｅｒ` (14)~~ |
| ~~第２王子のトリフ様~~ | ✅ **PROMOTED to §38.1** — `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ`, 12 columns, rendered in `tl/script/batch_007.tsv` (PR #20), **used exactly as seeded**, and **the ordinal drop is RULED AND STANDS — see §38.5.** Decisive at review: `第２王子` occurs **exactly once in the whole script dump — that very line — and zero times in battle**, and the same fact is carried twice more by `弟のトリフ`, so no plot fact is lost from the game. ⚠️ **This row's cost figure is wrong**: `Ｓｅｃｏｎｄ　Ｐｒｉｎｃｅ　Ｔｏｒｉｆ` is 19 bare but the row it would sit in measures **29**, so restoring the ordinal needs a page re-flow, not a word swap | ~~0 battle / 1 script~~ | — |

⚠️ **`モンスター` is NOT a seed — it is already SHIPPED.** `tl/script/batch_001.tsv` L33 renders it
`ｍｏｎｓｔｅｒ` (7 columns). The menu option `　モンスターがいい` in unique 432 and the reply in 435
**must reuse that word**; *creature* / *beast* would break CLAUDE.md §3's byte-identical rule.
Recorded here only so nobody re-invents it. (**2 battle / 214 script-dump / 32 unique.**)
✅ **DONE (PR #20)** — both render `ｍｏｎｓｔｅｒ` / `ｍｏｎｓｔｅｒｓ`, reused as required.

⚠️ **`殿` on the `{FFEC}` player-name insert — a decision, not a word.** Unique 427 has
`９軍の隊長に任命された{FFEC}{=00}{=00}殿。` (Leon's first meeting). **Count the corpus before
reasoning about it:** almost every `殿` in both dumps is `神殿` *temple*, a different word —
only **2 unique lines** carry the name-insert `殿`, plus one `ホッジス殿`.
**Proposal: carry it in register, adding no word**, on §2's `貴官` → "carried in **register**, not
in an added word" and §21.2's `さん` rule that drops the honorific. Leon's contraction-free
formality already does the work, and the same sentence *names the rank* (`９軍の隊長に任命された`),
so an added title would say it twice. Alt `Ｓｉｒ　{FFEC}` (3 + the insert).

✅ **EXECUTED AND RATIFIED 2026-09-09 (PR #20, `tl/script/batch_007.tsv`).** Unique 427 renders
`Ｏｈ？　Ｙｏｕ　ｍｕｓｔ　ｂｅ` / `{FFEC}{=00}{=00}，　ａｐｐｏｉｎｔｅｄ` / `ｃａｐｔａｉｎ　ｏｆ　ｔｈｅ` /
`９ｔｈ　Ａｒｍｙ．` — **no word added**, the insert moved to where English wants it (which §1 permits
and `translation_prompt.md` §5's own worked example does). The `Ｓｉｒ　{FFEC}` alternative is not
taken and stays on record. See §38.1.

⚠️ **`『編成』`, `『キャラクター育成』`, `『キャラを入れる』` — UI SCREEN LABELS, and a FLAG.**
§19.2 fixes 編成 → `form (your units)` **verbally**, and `batch_005` shipped exactly that
(`ｉｆ　ｙｏｕ　ｆｏｒｍ　ｙｏｕｒ　ｕｎｉｔｓ`). These three are different: they are the **names of menus
the player is told to go and find on screen**. ⚠️ **The menu strings themselves are in neither
dump** — so an English label here **cannot be verified against what the screen actually shows**,
and if the menus stay Japanese the instruction sends the player to a menu that does not match.
Proposal: `“Ｆｏｒｍａｔｉｏｎ”` (11), `“Ｃｈａｒａｃｔｅｒ　Ｇｒｏｗｔｈ”` (18),
`“Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ”` (17), all with `『…』` → `“…”` per §12. **This needs the disc:
the reviewer should raise it as a FLAGS entry, not resolve it.**

✅ **DONE as this row directs (PR #20).** All three are rendered in `tl/script/batch_007.tsv`
(unique 431 and 437) **exactly as proposed**, and **all three widths are correct as remeasured** —
11 / 18 / 17. The reviewer did **not** resolve them: the question is raised as `FLAGS.md` **§Z1**
and added to HANDOFF's **Blocked — needs a human** list, because the menu strings are in neither
dump and no English label here can be checked against what the screen shows. §26.3's *verbal*
編成 → *form (your units)* is used unchanged where the source is verbal (unique 437 ×2), which is
the source's own split. Promoted to §38.1; **this row stays live until the disc settles it.**

✅ **RULED AND APPLIED 2026-09-09 (PR #18 review): §1's and §2's figures are corrected IN PLACE**, so
the block below is now history rather than a live proposal. The measurement is not new — §29.5 made
it in wave 3 and deliberately recorded rather than patched, which is how a wrong figure travelled
two waves and was restated here as if open. Chunk 21's translator re-measured it independently with
`rowcheck`'s own algorithm and the reviewer re-measured it a third time; all three agree. **少尉 17,
中尉 16, `Ａｎｓｅｌｍｏ` 7, `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` 24.** No rendering changes
anywhere. See §36.4.

⚠️ **MEASURED CORRECTION to §2's rank widths — verify it yourself before relying on it.**
§2 states 少尉 → Second Lieutenant is "**18 columns** — will not share a line with a name" and
中尉 → First Lieutenant "**17 columns** — same rule". Measured full-width, both are **one column
too many**: `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` is **17** and `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ` is **16**.
The consequence is not cosmetic — **the "will not share a line with a name" rule is false for
every name yet tested**: `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ` = **22**,
`Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ` = **23**, `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` = **24**
— all inside the 24-column box, though the last two are at or over the ≤23 preferred limit
(CLAUDE.md §6). **This is an orchestrator's measurement, and §2 is not an orchestrator's to
edit: it is a proposal for the reviewer to rule on, and chunk 21's translator should re-measure
it independently before leaning on it.**

**Wave 6 seeds (2026-09-09) — battle chunks 24, 25, 26 and script batch 008 (unique 470–516).**
Proposed forms follow the European-reading convention (§11.4, §14, §17.3) and the species test
(§17.1). ⚠️ **Reach figures below are measured with `str.count()` over both dumps and are counted
in INSTANCES, not lines** (the wave-5 error at `FLAGS.md` §Y3/§Z). ⚠️ **The cross-unit set was
computed mechanically per `FLAGS.md` §Y2 — and the kanji-run intersection MISSED `末えい`, which is
mixed-script, exactly as it missed `つるん` in wave 5.** Mixed kanji+kana terms need their own pass.

✅ **STATUS 2026-09-09, FINAL — the wave-6 block is now CLEAR and every row in it is struck.**
`batch_008.tsv` (PR #21) merged **last** of the four and renders six of the seeds — `魔族`, `魔物`,
`末えい`, `古代文明`, `司教様`, `ウェストバリー` — **every one exactly as seeded, not one improved on
unilaterally**, plus `キエーザ` from the wave-2 block. The two cross-unit rows this wave deliberately
left live (`魔族`, paired with chunk 26; `末えい`, paired with chunk 25) are struck **here**, by the
second of each pair, which is the whole of what the `ルート` precedent (§29.1 / §30.1) prescribes —
and both merged siblings were **verified by reading the tree**, not assumed. Promoted to **§42**.
⚠️ **A fourth line-citation error survived PR #24's sweep**: the `司教様` row still read "unique 483",
a *menu* line. PR #21's Flag 5 named it and it is corrected in place above. ⚠️ **`場所` has no row in
this block and never had one** — confirmed a third time; the dispatch's pairing was wrong (§AB7).
⚠️ **`大陸` also has no row**: it is cross-unit between chunk 25 and `batch_008` and is recorded at
§41.1 and §42.1 instead, where the two units' **determiners differ because their sources do**.

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| ~~魔族~~ | `ｄｅｍｏｎ` / `ｄｅｍｏｎｓ` — **lowercase** | ✅ **PROMOTED to §40.1 (chunk 26, PR #22) and STRUCK HERE at `batch_008`'s merge (PR #21, 2026-09-09).** `ｄｅｍｏｎ` / `ｄｅｍｏｎｓ` — **lowercase**, rendered **4×** in `tl/script/batch_008.tsv` (DATA 498) exactly as seeded, and `tl/battle/chunk_026.txt` L5's `Ｔｈｅｓｅ　ｓｏ‐ｃａｌｌｅｄ　ｄｅｍｏｎｓ’` was **verified in the merged tree** rather than assumed. **The cross-unit rule is discharged**: chunk 26 merged first and deliberately left this row live, `batch_008` merged second and strikes it — the whole of what the `ルート` precedent (§29.1 / §30.1) prescribes. See §42.1. Original seed note follows: ⚠️ **CROSS-UNIT: `batch_008` (DATA line 498 — ⚠️ corrected in place 2026-09-09, PR #24 review; this read "unique 483", which is a *menu* line, as this block's own FACT 1 says) AND chunk 26 (L5, L14).** **13 battle + 21 script instances**, reaching battle chunks **26, 27, 28, 29, 30, 32** — the largest-reach term this wave | Lowercase by the §17.1 species test: it names *what they are*, the exact case of `ホビット` → hobbit. **Not** `Ｄｅｍｏｎ`. Race-level use ("the demon race", "demonkind") is ordinary prose, not a second fixed form. Keep distinct from 魔物 → `ｍｏｎｓｔｅｒ`. **5 / 6 columns** ⚠️ **STAYS LIVE after PR #22 merged 2026-09-09: chunk 26 was the FIRST of this pair to merge — `tl/script/batch_008.tsv` is still ABSENT from the tree (verified by reading it). Per the `ルート` precedent (§29.1 / §30.1) **PR #21's reviewer strikes this row.** Chunk 26 used it exactly as seeded and every reach figure re-measured EXACT; see §40.1.** |
| ~~魔物~~ | ✅ **PROMOTED to §42.1 and STRUCK** — `ｍｏｎｓｔｅｒｓ`, rendered once in `tl/script/batch_008.tsv` (DATA 512), **used exactly as seeded**. Not cross-unit: chunk 26 carries no `魔物` (verified at §40.1), so no row is left live. ⚠️ **The 魔族 / 魔物 distinction it was written to hold IS held — but `ｍｏｎｓｔｅｒ` now renders `魔物` AND `モンスター` in one bank and one speaker's gossip; see §42.3** | ~~`batch_008` ×1; 6 script~~ | Holds the 魔族 / 魔物 distinction apart. 7 columns |
| ~~末えい~~ | `ｄｅｓｃｅｎｄａｎｔ` | ✅ **PROMOTED to §41.1 (chunk 25, PR #23) and STRUCK HERE at `batch_008`'s merge (PR #21, 2026-09-09).** `ｄｅｓｃｅｎｄａｎｔ`, **10 columns**, rendered in `tl/script/batch_008.tsv` (DATA 498) as `Ｔｈｅ　ｄｅｓｃｅｎｄａｎｔ　ｏｆ　ｔｈｅ` / `ｗｉｓｅ` exactly as seeded, and `tl/battle/chunk_025.txt` L13's `ａ　ｄｅｓｃｅｎｄａｎｔ　ｏｆ　ｔｈｅ` / `ｌｉｇｈｔ　ｅｌｖｅｓ，　ｉｔ　ｓｅｅｍｓ．` was **verified in the merged tree** rather than assumed. **The cross-unit rule is discharged**: chunk 25 merged first and left this row live, `batch_008` merged second and strikes it (§29.1 / §30.1). See §42.1. Original seed note follows: ⚠️ **RENDERED by chunk 25 (PR #23, merged 2026-09-09) as `ａ　ｄｅｓｃｅｎｄａｎｔ　ｏｆ　ｔｈｅ` / `ｌｉｇｈｔ　ｅｌｖｅｓ，　ｉｔ　ｓｅｅｍｓ．`, exactly as seeded — and THIS ROW IS DELIBERATELY LEFT LIVE.** `batch_008` (PR #21) is still open and renders it too; per the `ルート` precedent (§29.1 / §30.1) the row is struck once, by the **second** of the pair, so **PR #21's reviewer strikes it** after verifying the merged chunk 25 rather than assuming. Promoted to §41.1. ⚠️ **CROSS-UNIT: `batch_008` (DATA line 498, `知に長けた者の末えい`) AND chunk 25 (L11, `ライトエルフの末えい`).** ⚠️⚠️ **NOT "1 instance each", and NOT a new form — corrected in place 2026-09-09 (§4.3, PR #24 review): `ｄｅｓｃｅｎｄａｎｔ` IS ALREADY SHIPPED.** `tl/battle/chunk_010.txt` 12.2 renders `誇リ高キ　龍人族ノ　マツエイダ。` as `Ｗｅ　ａｒｅ　ｄｅｓｃｅｎｄａｎｔｓ　ｏｆ` / `ｔｈｅ　ｐｒｏｕｄ　ｄｒａｇｏｎｆｏｌｋ．` — the same word in the lizardmen's **full-katakana** register (§5), which is why neither a kanji-run nor a kanji+kana search found it. **The choice is CONFIRMED by shipped work; only the novelty and reach claims were wrong.** Gate 6 is not engaged (different source strings), but both wave-6 units must match `ｄｅｓｃｅｎｄａｎｔ`. ✅ **`ｄｅｓｃｅｎｄａｎｔ` is 10 columns, measured `len()` — PR #23's Flag 15 says 11 and is a hand-count one high; the seed was right and the "correction" is NOT applied** | ⚠️ **A kanji-run intersection does NOT find this term** — it is kanji+hiragana. Alt *scion*, *last of the line*. Both units must agree. 10 columns |
| ~~ライトエルフ~~ | ✅ **PROMOTED to §41.1 and STRUCK HERE (PR #23, merged 2026-09-09)** — `ｌｉｇｈｔ　ｅｌｆ` / `ｌｉｇｈｔ　ｅｌｖｅｓ`, lowercase, **used exactly as seeded**, 9 / 11 columns confirmed. Chunk 25 renders **both** battle instances, so the term is **exhausted** and this row is struck outright rather than left live — the `ルート` cross-unit procedure (§29.1 / §30.1) does not apply where one unit carries every occurrence. The ARIES attribution below is **confirmed independently at PR #23's review from the `{FC50}`/`{FC51}` CHANNEL byte, not the portrait id** — the whole Guilford/Aries duel runs under one `{FCB0}{=00060000}` and the channel is what separates the speakers; see §41.2 | ~~chunk 25 (L11) ×2 — ⚠️ **ARIES's bloodline, NOT Torif's** (corrected in place 2026-09-09, §4.3, PR #24 review; this read "Trif's bloodline"). Gilford says `なるほど、確かにライトエルフの末えいのようだな` **to Aries**, who then finds his own spell useless — coherent with Aries being Bishop Creus's grandchild (chunk 24 L15). `ライトエルフの封印` is separately the seal Gilford intends to break. **The renderings are unaffected; only the note was wrong.** 2 battle + 0 script~~ | ~~⚠️ **NOT open after all — corrected in this same seed before dispatch.** The sibling term `ダークエルフ` is ALREADY FIXED at **§17 as `ｄａｒｋ　ｅｌｆ`, lowercase**, and is already shipped lowercase in `tl/script/batch_003.tsv` L20 (`ａｎｃｉｅｎｔ　ｄａｒｋ　ｅｌｖｅｓ`). `ライトエルフ` is the same construction and takes the same case: **`ｌｉｇｈｔ　ｅｌｆ` / `ｌｉｇｈｔ　ｅｌｖｅｓ`, lowercase, not a reviewer question.** Consistent with §17.1 and the `ホビット` → hobbit precedent. **Both instances must agree.** 9 / 11 columns~~ |
| ~~アネット~~ | ✅ **PROMOTED to §40.1 (PR #22, merged) — `Ａｎｎｅｔｔｅ`, used exactly as seeded; reach re-measured EXACT.** Original seed note follows: | chunk 26 (L14) ×5 — **Dolgan's daughter**, the survivor who guides the party to the mountain settlement. 5 battle + 4 script | European reading. 7 columns |
| ~~ドルガン~~ | ✅ **PROMOTED to §40.1 (PR #22, merged) — `Ｄｏｌｇａｎ`, used exactly as seeded; reach re-measured EXACT.** Original seed note follows: | chunk 26 (L14) ×2 — Annette's father, alive among the survivors. **Also battle chunk 32 + 8 script instances**; 4 battle + 8 script | Alt *Durgan*, *Dorgan*. 6 columns |
| ~~セティ~~ | ✅ **PROMOTED to §40.1 (PR #22, merged) — `Ｓｅｔｉ`, used exactly as seeded, and FIXED AS FEMALE (§40.2).** Original seed note follows: | chunk 26 (L14, L15) — one of the **two ruling 魔族**, `恐ろしく強大で、驚くほど頭が回り、極めて残忍`. **Reaches battle chunks 26, 27, 28, 29, 38** — 6 battle instances | ⚠️ **A matched pair with ユイティ**: the Japanese rhymes them (‑ティ / ‑ティ) and the English should keep that. Alt *Sethi*, *Sety* — but pair the choice. 4 columns |
| ~~ユイティ~~ | ✅ **PROMOTED to §40.1 (PR #22, merged) — `Ｙｕｉｔｉ`, used exactly as seeded, and FIXED AS MALE (§40.2).** Original seed note follows: | chunk 26 (L14, L15) — the other ruling 魔族. **Reaches battle chunks 26, 27, 29, 32, 38** — 7 battle instances | Pair with `Ｓｅｔｉ`. Alt *Yuity*, *Uiti*. 5 columns |
| ~~トレーズ~~ | ✅ **PROMOTED to §40.1 (PR #22, merged) — `Ｔｒｅｉｚｅ`, used exactly as seeded. He is ALSO the dark elf of L10/L11, confirmed on the channel test (§40.5).** Original seed note follows: | chunk 26 (L15) — a wounded demon who begs Seti for help. **Reaches battle chunks 26, 27, 28, 29** — 6 battle instances | `トレーズ` is the standard katakana for French *Treize*, so this is the European reading. Alt *Traize*, *Trays*. 6 columns |
| ~~カッフィ~~ | ✅ **PROMOTED to §39.1** — `Ｃａｆｆｉ` / `Ｃａｆｆｉ　Ｐｏｒｔ`, used exactly as seeded (PR #24) | chunk 24 (L14) ×3 — ⚠️ **a PORT, not a person**: `カッフィの港`, `カッフィへ来てくれ`. 3 battle + 3 script | Alt *Kaffi*, *Caffy*. 5 columns |
| ~~ゴードン~~ | ✅ **PROMOTED to §39.1** — `Ｇｅｎｅｒａｌ　Ｇｏｒｄｏｎ`, used exactly as seeded (PR #24) | chunk 24 (L15) — `ファリーナのゴードン将軍`, one of the three who plotted the killing. 1 battle | **`将軍` → `Ｇｅｎｅｒａｌ` is ALREADY FIXED** (§32.1, and the §10 discharge at PR #8) — only the name is new here. 6 columns bare, 15 with the rank |
| ~~オーラスマッシャー~~ | ✅ **PROMOTED to §41.1 and STRUCK HERE (PR #23, merged 2026-09-09)** — `Ａｕｒａ　Ｓｍａｓｈｅｒ`, **used exactly as seeded**, 12 columns confirmed. A hapax carried entirely by chunk 25, so struck outright. ⚠️ **ARIES's spell, NOT Torif's — re-confirmed at PR #23's review on the CHANNEL byte**: the caster is `{FCB0}{=00060000}` **channel 1**, the same channel that then says `そ、そんな・・・オーラスマッシャーがきかない・・・？`; channel 0 is Guilford throughout. See §41.2 | ~~chunk 25 (L11) — Aries casts it at Gilford and it fails: `オーラスマッシャーがきかない・・・？`. 1 battle | 12 columns~~ |
| ~~ホアグ王子派 / トリフ王子派~~ | ✅ **PROMOTED to §39.1** — `ｔｈｅ　Ｈｏａｇ　ｆａｃｔｉｏｎ` / `ｔｈｅ　Ｔｏｒｉｆ　ｆａｃｔｉｏｎ`, rendered in `tl/battle/chunk_024.txt` (PR #24) | chunk 24 (L14) — `ホアグ王子派とトリフ王子派との間で、争いが起こるのだ` | ⚠️⚠️ **THIS ROW CARRIED TWO ERRORS, BOTH CORRECTED IN PLACE 2026-09-09 (§4.3, PR #24 review). It is kept, struck through, rather than deleted, because a provisional row contradicting a main-table entry cost two translators a round this wave and the record of how should survive.** (1) It read **`Ｐｒｉｎｃｅ　Ｔｒｉｆ’ｓ　ｆａｃｔｉｏｎ`**. `トリフ` → **`Ｔｏｒｉｆ`** is fixed at §9 line 290, **promoted at §38.1**, and **shipped** at `tl/script/batch_007.tsv` L56 as `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ`; `Ｔｒｉｆ` occurs **nowhere** in `tl/` or `pending/` — grepped at review. A main-table entry beats a provisional §9 row. Chunk 24's translator reached `Ｔｏｒｉｆ` independently, before the correction arrived. (2) It read "**21 / 21 columns**". Measured with `len()`: `Ｐｒｉｎｃｅ　Ｈｏａｇ’ｓ　ｆａｃｔｉｏｎ` is **21** and `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ’ｓ　ｆａｃｔｉｏｎ` is **22** — `Ｔｏｒｉｆ` is 5 columns to `Ｈｏａｇ`'s 4. **No rendering changes**: the long forms were never used, because they do not fit (§39.3). The two appear in ONE sentence and must be parallel; both shortened together, as this row directed. Note `’` not `'` (CLAUDE.md §3) |
| ~~古代文明~~ | ✅ **PROMOTED to §42.1 and STRUCK** — `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ`, **20 columns as seeded** (re-measured with `len()`), rendered in `tl/script/batch_008.tsv` (DATA 488), **used exactly as seeded** including the British `‑ｓａｔｉｏｎ`. The battle instance is in chunk 16, which is tier-A blocked, so this unit is the only shipper for now. Original seed note follows: | `batch_008` (**DATA line 488** — ⚠️ corrected in place 2026-09-09, PR #24 review; this read "unique 473") — `古代文明の宝庫`. 1 battle (ch.16) + 5 script | ⚠️ **British `‑ｓａｔｉｏｎ`**, matching `Ｒｅｅｓｅ　ｃｉｖｉｌｉｓａｔｉｏｎ` already shipped in `batch_005.tsv` L46. 20 columns |
| ~~司教様~~ | ✅ **RENDERED by `batch_008` (PR #21, merged 2026-09-09) as `ｔｈｅ　ｌａｔｅ　Ｂｉｓｈｏｐ` / `ｏｆ　Ｆａｒｉｎａ．`, and STRUCK — `Ｂｉｓｈｏｐ` is §26.1's, only the appellation is new.** `亡くなられた` is carried by *the late*, matching the massacre `tl/battle/chunk_021.txt` L10 already ships. See §42.1 | `batch_008` (**DATA line 498** — ⚠️ corrected in place 2026-09-09, PR #21 review; this read "unique 483", a *menu* line, and it is the **fourth** row of this block to carry a list index. PR #24's reviewer patched the `魔族`, `末えい`, `古代文明` and `ウェストバリー` rows and left this one; PR #21's Flag 5 named it correctly and it is now applied) `亡くなられたファリーナの司教様`; chunk 24 (L15) ×2 `ファリーナの司教、クレウス` / `クレウス司教の孫` | ⚠️ **Not a new person: this is Bishop `Ｃｒｅｕｓ`**, the late Bishop of Farina. Already rendered in `tl/battle/chunk_021.txt` L10/L20 and `batch_005.tsv` L46. `司教` → **Bishop**, possessive `Ｃｒｅｕｓ’` (§26.1) |
| ~~ウェストバリー~~ | ✅ **RENDERED by `batch_008` (PR #21, merged 2026-09-09) as `Ｉｎ　Ｗｅｓｔｂｕｒｙ，　ｔｈｅｙ　ｓａｙ，` and STRUCK.** `Ｗｅｓｔｂｕｒｙ`, 8 columns, byte-identical to the five shipped `ウエストバリー` (large エ) instances that a gate-6 grep on the exact Japanese cannot pair with it — §2's corrected row records both spellings. Original seed note follows: | `batch_008` (**DATA line 515** — ⚠️ corrected in place 2026-09-09, PR #24 review; this read "unique 505") | ⚠️ **NOT a new term — a SOURCE SPELLING VARIANT** of `ウエストバリー` (large エ), which is shipped 5× as `Ｗｅｓｔｂｕｒｙ`. See the corrected §2 row. 8 columns |
| クロイツェル | `Ｋｒｅｕｔｚｅｌ` | ✅ **RENDERED in `tl/battle/chunk_030.txt` (PR #27) exactly as seeded — but the row STAYS LIVE.** ⚠️ **CORRECTED 2026-09-09 (PR #27 review): PR #27 called it "1 battle + 0 script, a hapax, struck outright" and the dispatch repeated it. Counted at review over BOTH dumps: 1 battle (chunk 30) + **1 script — bank 41, `script_unique` line 1391** — and the script instance is the SAME construction (`紅の騎士団の将、リムル・クロイツェルだな？`).** A later script batch renders it and must match `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ` byte-for-byte, so the row is struck by **that** unit, not by chunk 30. **8 columns**; `リムル・クロイツェル` → `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ` = **14** — both re-measured with `len()` and confirmed. German/European spelling per `Ｄｉｅｌ` (§25.1), `Ｈｅｌｆｅｒ`, `Ｂａｕｅｒ`. Does **not** disturb §1's `リムル` → `Ｒｉｍｕｌ` or `リムル様` → `Ｌａｄｙ　Ｒｉｍｕｌ`. See §43.5 | battle chunk 30 ✅; **script bank 41 (unique 1391) OUTSTANDING** | Alt *Kreutzell*, *Creutzel*, *Cruzel* |
| ~~カイザード~~ | ✅ **PROMOTED to §45.1 (PR #26, merged 2026-09-09)** — `Ｋａｉｚａｒｄ`, **used exactly as seeded**, 7 columns confirmed with `len()` at review. Rendered **only** in the honorific form `Ｌｏｒｄ　Ｋａｉｚａｒｄ` (12, ×4, byte-identical); the bare form is not yet spent anywhere. Original seed note follows: **7 columns.** The imperial officer running the summoning in battle chunk 31; addressed `カイザード様` by his own men → `Ｌｏｒｄ　Ｋａｉｚａｒｄ` (**12**) on the §14.1 / §28.1 様 → **Lord** precedent, *not* §21.2's さん rule | battle chunk 31 | Alt *Kaisard*, *Kaiserd* |
| ~~ジュエルビースト~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `Ｊｅｗｅｌ　Ｂｅａｓｔ`, **used exactly as seeded**, 11 columns confirmed. ×2. The currency sense (`Ｊｅｗｅｌｓ`) stands beside it two messages later and the two stay distinguishable by capitalisation and context, as this row predicted. Original seed note follows: **11 columns.** A named monster whose forehead gem sells high; `ジュエル` → `Ｊｅｗｅｌ` is already fixed, so only the compound is new. Capitalised as a creature **name** here, not a class | battle chunk 31 | Alt *Jewelbeast* |
| ~~カーバンクル~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `Ｃａｒｂｕｎｃｌｅ`, **used exactly as seeded**, 9 columns confirmed. ×2, and held visibly distinct from `Ｊｅｗｅｌ　Ｂｅａｓｔ`: the name is kept on the row rather than pronominalised, so the `少し違うようだが` contrast the chunk turns on survives in English. Original seed note follows: **9 columns.** The standard RPG gem-browed beast; chunk 31 distinguishes it from the Jewel Beast (`カーバンクルとは少し違うようだが`), so the two forms must stay visibly distinct | battle chunk 31 | — |
| ~~『闇の紋章』~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `“Ｅｍｂｌｅｍ　ｏｆ　Ｄａｒｋｎｅｓｓ”`, **used exactly as seeded, the primary form and not the `Ｄａｒｋ　Ｅｍｂｌｅｍ` alternative. The seed's 18 / 20 figures are CORRECT**, re-measured with `len()` at review; the translator's own first hand count of 19 / 21 was the error, which it caught and reported itself. Ships at 21 with its stop, on the row a source trailing blank freed (§45.2). Original seed note follows: **18 columns bare, 20 with the §12 quotes** (`『…』` → `“…”`). 紋章 appears nowhere else in the glossary | battle chunk 31 | Alt *Dark Emblem* (11) if the row will not carry 20 |
| ~~冥界の王~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `ｔｈｅ　Ｎｅｔｈｅｒｗｏｒｌｄ　Ｋｉｎｇ`, **used exactly as seeded; the seed's 20 is CORRECT** and `ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｅ　Ｕｎｄｅｒｗｏｒｌｄ` measures **26**, both re-measured at review. ×3 — two take `ｏｕｒ` for `我らが` (20), the third is a **vocative** and drops the article (§45.3). Original seed note follows: **20 columns**, so it fits one row; `ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｅ　Ｕｎｄｅｒｗｏｒｌｄ` is **26** and cannot. Capitalised per §2's 王女様 → *the Princess* and §28.1's 国王 → *the King* | battle chunk 31 ×3 | Alt *the Underworld King* |
| ~~リッチ~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `Ｌｉｃｈ`, **used exactly as seeded**, 4 columns confirmed. The game's own `ＬｉＣＨ` spelling survives verbatim in the incantation two rows below it (§45.5). Original seed note follows: **4 columns.** ⚠️ **The game spells it itself** — chunk 31's incantation ends `ＥＬＡＧＬＡ・ＬｉＣＨ！` in full-width Latin, so this is a transcription, not a choice. Capitalised: chunk 31 uses it as the creature's name (`冥界の王、リッチよ！`) | battle chunk 31 | — |
| ~~石版~~ | `ｔａｂｌｅｔ` | ✅ **STRUCK 2026-09-10 at `batch_010`'s merge (PR #32) — DATA 300 is rendered, and it was the last outstanding instance this row was being held for.** Verified at review over both dumps, not taken from the PR: 3 script-unique lines (DATA 300 ✅ PR #32, 569 ✅ / 571 ✅ PR #28) + 5 battle (chunks 30 ✅, 36 ✅). PR #32 renders `漆黒の石版` as bare lowercase `ｔａｂｌｅｔ`, 6 columns, byte-identical to chunk 30's four instances and `batch_009`'s two. The `ルート` procedure (§29.1 / §30.1) is complete: the last unit to land strikes the row, and this is it. Original note follows:  ✅ **RENDERED ×3 in `tl/battle/chunk_030.txt` (PR #27) exactly as seeded; 6 columns confirmed. ⚠️ THE ROW STAYS LIVE — do not strike it on chunk 30.** CROSS-UNIT: reach re-counted at the PR #27 review over both dumps and PR #27's figures are **exact** — **5 battle (chunks 30, 36) + 25 script instances across 21 banks** (2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 25, 33, 40, 42, 43). Per the `ルート` precedent (§29.1 / §30.1) it is struck by the **last** of chunk 36 and the script units to land. ⚠️ **Unique-line ids, with the convention named — CORRECTED 2026-09-09 (§4.3, PR #25 review, §44.5).** The instances are **DATA 300 / 569 / 571 = FILE 305 / 574 / 576** (FILE = DATA + 5; the first data row of `script_unique.txt` is FILE 6). This row previously said "574/576 right, 569/571 wrong": **they are the same two lines in two conventions and neither was wrong.** What PR #27's review genuinely found, and it stands, is that **DATA 300 / FILE 305** (`軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`) is a third instance no row had named. Reach unchanged and exact; no rendering changes. The plot object the whole wave turns on. ⚠️ **STILL LIVE AFTER WAVE 7 — CHECKED AT PR #28's REVIEW AND THE ANSWER IS NO.** PR #28 renders **DATA 569 and 571** exactly as seeded (`ｔａｂｌｅｔ`, 6 columns, byte-identical to chunk 30's four bare instances), which left only **DATA 300**. That line — `軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`, **count 21, an item description spanning 21 banks** — is **NOT in any wave-7 unit and is NOT translated in any `tl/script/*.tsv`**; verified by direct lookup at review, not inferred. **PR #28 is therefore not the last unit to render `石版`, and the wave-7 dispatch's instruction to "strike both rows" was wrong on this one.** The row is struck by whichever unit takes DATA 300 | battle 30 ✅, **36 ✅ (PR #25, inside the proper name only — the bare noun is untouched there)**; script **569 ✅, 571 ✅ (PR #28); DATA 300 OUTSTANDING — this is what keeps the row live** | Alt *stone tablet* (12) |
| ~~『かげの石版』~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE at `batch_009`'s merge (PR #28, 2026-09-09) — this was the LAST of its instances to land, so the `ルート` precedent (§29.1 / §30.1) is discharged and the row is struck.** `“Ｓｈａｄｏｗ　Ｔａｂｌｅｔ”`, **used exactly as seeded; 13 bare / 15 quoted re-measured a third time at review, both exact.** Its whole reach is **battle chunk 36 (rendered, `pending/chunk_036.txt`) + script DATA 569 (rendered by PR #28)** — nothing outstanding. ✅ **Cross-unit consistency verified at review against the MERGED tree, not a report**: chunk 30 renders bare `石版` as lowercase `ｔａｂｌｅｔ`, chunk 36 renders the proper name `“Ｓｈａｄｏｗ　Ｔａｂｌｅｔ”`, and `batch_009` renders **both** — the three agree exactly. ⚠️ **The bare `石版` row ABOVE is a different matter and STAYS LIVE — see it.** Original seed note follows: **Wave-7 seed.** ⚠️ **CROSS-UNIT — battle chunk 36 AND script DATA 569 (= FILE 574); convention named per §44.5.** Builds on 石版 → `ｔａｂｌｅｔ` above; `かげ` is kana here, so the **mixed-script blind spot** applies (§Y2) — grep `かげ`, `影` and `カゲ` before calling any form new. **That check was done at the PR #25 review and is clean**: `かげ` = *shadow* is battle chunk 36 and script DATA 569 only; every other battle `かげ` is `おかげ` (chunk 8), `影` is 0 battle, and all 4 battle `カゲ` are `トカゲ` | battle chunk 36 ✅; script **DATA 569** OUTSTANDING | Alt *Tablet of Shadow* (16) |
| ~~鏡の神殿~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE at `batch_009`'s merge (PR #28, 2026-09-09)** — `Ｍｉｒｒｏｒ　Ｔｅｍｐｌｅ`, **used exactly as seeded; 13 columns re-measured with `len()` at review and the seed's figure is exact.** Reach re-counted over both dumps at review: **script DATA 569, 571 and 0 battle — both rendered here, so the term is exhausted and the row is struck outright.** ⚠️ 569 page 3 and 571 render the *second* instance as bare `ｔｈｅ　ｔｅｍｐｌｅ` (§46's Flag 7): with the proper name that page needs **5 rows against a 4-row limit** — re-measured at review under an optimal wrap, and the departure is genuinely forced | script 569, 571 — both ✅ | Alt *the Temple of the Mirror* (24 — fills a whole row) |
| ~~リースの化身~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE (PR #28, 2026-09-09)** — `ｔｈｅ　ｉｎｃａｒｎａｔｉｏｎ　ｏｆ　Ｒｅｅｓｅ` / bare `ｉｎｃａｒｎａｔｉｏｎ`, **used exactly as seeded. The seed's 24 / 11 are BOTH EXACT**, re-measured at review, and the 24 is confirmed to be the widest run in the whole unit: it stands alone on its row in 569 and 571 and takes no mark or particle, exactly as the seed warned. ⚠️ **Reach corrected at review: DATA 568, 569, 571 — the seed's cell said "569, 571" and missed 568**, where the bare noun carries the verse so the quote mark can sit on the row. All three are rendered here, so the row is struck | script 568, 569, 571 — all ✅ | Alt *Reese's incarnation* |
| ~~リースの神々~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE (PR #28, 2026-09-09)** — `ｔｈｅ　ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ`, **used exactly as seeded, 17 columns confirmed.** 560 splits it at `ｏｆ` across a break; **567 is a vocative and correctly drops the article — `Ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ，`, which measures 14, not the PR's 15** (re-measured at review; §9's "your measurement wins" rule applied). Both instances rendered, so the row is struck | script 560, 567 — both ✅ | — |
| ~~遠征軍~~ | ✅ **PROMOTED to §43.2** — `ｅｘｐｅｄｉｔｉｏｎａｒｙ　ｆｏｒｃｅ`, rendered in `tl/battle/chunk_030.txt` (PR #27) in the **long** form; 19 columns confirmed with `len()`. **Exhausted: 1 battle (chunk 30) + 0 script, re-counted at review — this is the one wave-7 seed that is genuinely spent, and it is struck.** The licensed short `ｅｘｐｅｄｉｔｉｏｎ` (10) was **never needed** and is not spent: the chunk landed 577 bytes under and the long form fits the source's own four rows | battle chunk 30 ✅ | Alt *expedition* — unspent |
| ~~選ばれし者~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE (PR #28, 2026-09-09)** — `ｔｈｅ　ｃｈｏｓｅｎ　ｏｎｅ`, **used exactly as seeded, 14 columns confirmed** with `len()` at review. A hapax — **script DATA 570 only, 0 battle**, re-counted at review — so the term is exhausted and struck outright. The elder's uncontracted register holds around it (`Ｔｏ　ｙｏｕ，　ｗｈｏ　ｈａｖｅ　ｂｅｃｏｍｅ　／　ｔｈｅ　ｃｈｏｓｅｎ　ｏｎｅ，`) | script 570 ✅ | — |
| ~~召喚の儀式~~ | ✅ **PROMOTED to §45.1 (PR #26)** — `ｓｕｍｍｏｎｉｎｇ　ｒｉｔｕａｌ`, **used exactly as seeded and not the `ｓｕｍｍｏｎｉｎｇ　ｒｉｔｅ` alternative**, 16 columns confirmed. **1 battle + 0 script — exhausted, and struck outright.** The short alternative was never needed: the chunk landed 2,793 bytes under | battle chunk 31 ✅ | ~~Alt *summoning rite* (14)~~ — unspent |
| ~~ビーストショップ / アイテムショップ~~ | `Ｂｅａｓｔ　Ｓｈｏｐ` / `Ｉｔｅｍ　Ｓｈｏｐ` | ✅ **STRUCK 2026-09-10 at `batch_010`'s merge (PR #32) — DATA 899 is rendered, and it was the only thing keeping this row live.** ⚠️ **The PR #28 correction was exactly right and is now confirmed by the shipped line: DATA 899 IS prose**, and `batch_010` renders it `Ａｔ　ｔｈｅ　“Ｂｅａｓｔ　Ｓｈｏｐ”` — §12 quotes for the source's `『　』` and **no leading `　` cursor gutter**, the bare name byte-identical to §46.1's menu form minus its gutter. Reach re-measured at review: `ビーストショップ` 2 script lines (DATA 555 ✅ PR #28, 899 ✅ PR #32), 0 battle; `アイテムショップ` DATA 555 only. Both halves exhausted. Original note follows:  ✅ **RENDERED in `tl/script/batch_009.tsv` (PR #28) exactly as seeded — 10 / 9 bare and 11 / 10 with the cursor gutter, all four re-measured with `len()` at review and all four exact. ⚠️ BUT THE ROW STAYS LIVE, AND ITS REACH CELL WAS WRONG.** ⚠️ **CORRECTED 2026-09-09 (PR #28 review): the reach is NOT "script 555" alone.** `ビーストショップ` also occurs at **script DATA 899 (bank 28), which is untranslated** — `『ビーストショップ』でドラゴンやゴーレムを売ってくれるぜ。`, a signpost NPC in another town. Neither the wave-7 dispatch nor PR #28's body caught this; it was found by counting the term's reach over the dump at review rather than trusting the cell. **`アイテムショップ` alone IS exhausted (DATA 555 only) — but the two share one row, so the row is held live for `ビーストショップ`.** ⚠️ **DATA 899 is PROSE, not a menu**: it takes `“Ｂｅａｓｔ　Ｓｈｏｐ”` with §12 quotes for the source's `『　』` and **no leading `　` cursor gutter** — the gutter belongs only to 555's two menu options. §34.1's shop vocabulary was checked first and fixes ジュエル / 品 / アイテム and the menu options, but **no shop *name***, so only the compounds are new | script 555 ✅ (PR #28); **DATA 899 OUTSTANDING — this is what keeps the row live** | — |
| ~~オーホホホ~~ | ✅ **PROMOTED to §46.1 and STRUCK HERE (PR #28, 2026-09-09)** — `Ｏｈｏｈｏｈｏ`, **used exactly as seeded, 7 columns confirmed.** Rendered with the source's own four stops as `Ｏｈｏｈｏｈｏ．．．．` (the `・・・・` run is 4 in the source and 4 in the English — verified at review). A hapax: **script DATA 559 only, 0 battle**, and both kana scripts were grepped (`オーホホホ` 1, `おーほほほ` 0) before it was called new. Struck outright | script 559 ✅ | — |

⚠️ **WAVE-7 SEEDS (battle chunks 30, 31, 36 + script `batch_009` = unique 534–583).** Proposed
forms only — **promote on first use, and measure before you trust a width.** Every figure in the
rows above was produced with `len()` on the full-width string (§AC3); if your own `len()` disagrees
with a cell, **your measurement wins and the cell is the error** — say so in the PR.

⚠️ **FOUR TERMS THAT LOOK NEW AND ARE ALREADY FIXED — do NOT reseed them:**
1. **`３号機` → `Ｕｎｉｔ　３`** (6). `号機` → **Unit** is fixed (`機械兵 ＮＮ号機`, `４号機`).
2. **`うらみ` → `ｇｒｕｄｇｅ`** (6). Chunk 30 writes it in **kana**; the fixed row is `恨み`. This is
   the **mixed-script blind spot** (§Y2/§AC1) exactly — a kanji search never finds chunk 30's form.
3. **`モンスター` → `ｍｏｎｓｔｅｒ`** — shipped, 214 instances, and §42.3 ruled the 魔物/モンスター
   collapse **stands**. Chunk 31 has `モンスター` and `アンデッドモンスター` → `ｕｎｄｅａｄ　ｍｏｎｓｔｅｒ`
   (14). **Do NOT spend the reserved `ｃｒｅａｔｕｒｅ`** — it is held for a future 魔物 split only.
4. **`砦` → `ｆｏｒｔ`**, **`王女様` → `ｔｈｅ　Ｐｒｉｎｃｅｓｓ`**, **`第９軍`/`９軍` → `９ｔｈ　Ａｒｍｙ`**,
   **`カーライン` → `Ｃａｒｌｉｎｅ`**, **`オーク` → `ｏｒｃ`** (lower-case in prose), **`神殿` → `ｔｅｍｐｌｅ`**,
   **`聖堂` → `ｓａｎｃｔｕａｒｙ`**, **`ドルガンさん` → bare `Ｄｏｌｇａｎ`** (§21.2) — all fixed already.


⚠️ **THREE BINDING FACTS FOR `batch_008` THAT ARE NOT GLOSSARY TERMS**, recorded here because the
unit cannot be translated correctly without them:

1. **The menu line is ALREADY SHIPPED and gate 6 binds it byte-for-byte.** Unique **472, 483, 493
   and 504** all carry the visible text `　兵士を　補充したい　情報を　聞きたい　何でもない`, and
   `tl/script/batch_007.tsv` already ships it three times (L41, L51, L62) as
   `　Ｒｅｃｒｕｉｔ　ｓｏｌｄｉｅｒｓ　Ａｓｋ　ｆｏｒ　ｉｎｆｏｒｍａｔｉｏｎ　Ｎｏｔｈｉｎｇ`.
   **All four lines must reuse that exact string** — leading ideographic space included
   (CLAUDE.md §6.8) — not a fresh translation.
2. **`batch_008` is 47 lines but only 32 distinct translations.** ⚠️ **Corrected in place 2026-09-09
   (§4.3, PR #24 review): this read "~26". 47 lines − 22 in groups + 7 groups = 32.** Seven groups share identical
   visible text and each group must be byte-identical in English:
   **[472, 483, 493, 504]**, **[473, 484, 494]**, **[474, 485, 495]**, **[476, 487, 497]**,
   **[478, 489, 499]**, **[479, 490, 500]**, **[480, 491, 501]** — 22 of the 47 lines.
   The keys differ only in their trailing `{FFF8}` argument, so they are separate unique rows.
3. **`あら` is RULED, and seven of these lines carry it.** §32.4 / §35: `あら` → `Ｍｙ` plus the
   source's own punctuation. Unique **478, 479, 482, 489, 490, 499, 500**. Wave 5 spent a whole
   corrections unit enforcing this across four shipped files — do not re-litigate it here.

⚠️ **AND ONE FOR CHUNK 24.** L15 turns on gender and must not be smoothed over:
`ファリーナの司教、クレウスの孫だ` → `えっ、でも、クレウス司教の孫って男だったんじゃ・・・` →
`・・・・・そうだ、僕は男だ。` — Aries is asked whether Bishop Creus's grandchild was not *a boy*,
and answers in male-coded `僕` that he is. **The exchange is the point; keep the question and the
answer both explicit.** It is the same massacre `tl/battle/chunk_021.txt` L10 already ships as
`ｔｅｎ　ｙｅａｒｓ　ａｇｏ　ａｌｌ　ｔｈｅ　Ｂｉｓｈｏｐ’ｓ　ｋｉｎ　ｗｅｒｅ　ｓｌａｕｇｈｔｅｒｅｄ`
(`一族` → `ｋｉｎ`, `皆殺し` → `ｓｌａｕｇｈｔｅｒｅｄ`) — read chunk 21 before rendering it.
This is adjacent to but **distinct from** `FLAGS.md` §Y6, which is about **クレス** (Cress), a
different character; §Y6 stays open and unaffected.

**Wave 8 seeds (2026-09-09) — battle chunks 37, 38, 41, 42 and script batch 010.** Battle names
follow the European-reading convention (§11.4, §14, §17.3); item-table vocabulary follows §4
(British spellings) and the stat-row precedent of §22/§4. ⚠️ **Every width below was measured with
`len()`, not hand-counted** (§AC3 / FLAGS §AG6), and **the proposer is fallible: if your
measurement disagrees with a cell here, your measurement wins and this cell is the error.**

| Japanese | Likely English | Where seen | Alt spellings / promotion note |
|---|---|---|---|
| ~~マザロー~~ | ✅ **PROMOTED to §48.1 and STRUCK (PR #29, merged 2026-09-09)** — `Ｌｏｒｄ　Ｍａｚａｒｏ`, **used exactly as seeded**. **1 battle + 0 script — a hapax, re-counted over both dumps at review, so the row is exhausted.** Original seed note follows: battle chunk 37 — `マザロー様！{FFFE}反乱軍の生き残り` | A **PERSON**, addressed `様`. ⚠️ **NOT `メルザリオ` → `Ｍｅｌｚａｒｉｏ` (§20.1), which is a PLACE** — different kana, the §Y2/§AC1 kana-variant blind spot. Keep the two visibly distinct. Alt *Mazarow*, *Masaro* |
| マーシュ | `Ｍａｒｓｈ` | ⚠️ **RENDERED in `tl/battle/chunk_037.txt` (PR #29) exactly as seeded — but the row STAYS LIVE.** ⚠️ **Count corrected 2026-09-09 (§4.3, PR #29 review): 1 battle + 3 script LINES / 4 instances** — FILE **870** (the main-script twin of chunk 37's own scene), FILE **1330** (`ここの港には、マーシュが　いるはずよ。`) and FILE **1379** (**twice**); the seed's “script ×3” counted lines, not instances. **None of the three is translated and none falls in `batch_010`'s window**, so a later batch must render all three `Ｍａｒｓｈ`. | A person at the port — `おお、マーシュ。{FFFE}無事だったか。` ⚠️ **FILE 1379 establishes WHAT HE IS and the seed did not know it: `俺はこの船の船長、{FFFE}マーシュってんでさ。` — Marsh is the SHIP'S CAPTAIN**, which is why he is at the port, why he was watching Rimul, and what `あの船は？` in chunk 37 L14 refers to. Whoever takes FILE 1379 should check it against 船長 as an address. Alt *Mashu*, *March* |
| ~~マラナ~~ | ✅ **PROMOTED to §1 and STRUCK HERE (PR #33, merged 2026-09-09)** — `Ｍａｒａｎａ`, **used exactly as seeded**, 7 columns. Chunk 38 renders **both** battle instances and there are 0 in script, so the term is **exhausted** and this row is struck outright rather than left live (the `ライトエルフ` precedent, §41.1; the `ルート` cross-unit procedure §29.1/§30.1 does not apply where one unit carries every occurrence). See §47.1 | ~~battle chunk 38 ×2 — `このマラナ、{FFFE}お前たちと再会する`~~ | ⚠️ **THE GENDER NOTE IN THIS SEED WAS WRONG AND IS CORRECTED IN PLACE (§4.3), NOT MERELY STRUCK.** It read “self-referential boast, `〜わ` → **female**”. **`〜わ` does not mark female in this corpus.** Raised by PR #33 and **re-measured independently at review**: sentence-final `わ` occurs **40** times in `battle_dump.txt` and at least four speakers are unambiguously male — c16 L14 `このワシが始末してくれるわ！` (**ワシ**), c39 L1 `一人残らず始末してくれるわ！` (**Doctor Crimea**, §1/§25.1), c42 L7 `俺様が始末してやるわ！` (**俺様**), c43 L1 `雑草どもが。目にもの見せてくれるわ。` (**Helfer**, §11.6). Marana's own is `あると思ったわ！！` after a volitional — the same masculine emphatic — and her other particles are `ぞ` and `〜おって`. ⚠️ **The source in fact male-codes her**: Seti calls the opponent `おっさん` (c38 L10), whose fixed English is `ｇｅｅｚｅｒ` (§24.2). **NO RENDERING TURNS ON IT OR EVER DID** — she is first person throughout and PR #33 wrote no gendered third-person pronoun, deliberately declining `ｆｅｌｌｏｗ` (§32.2) so as not to add an assertion of its own. Gender is therefore **recorded as unfixed**, not decided. ⚠️ **This is the §Y6 (Cress) shape a second time: a seeded gender assertion the corpus does not carry.** Alt *Malana* recorded and not taken |
| ~~防御力＋ＮＮ (armour stat row)~~ | `Ｄｅｆ＋ＮＮ` | script DATA 226, 239, 272 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** **Zero-growth confirmed by `len()` at review, not assumed: `防御力＋１` 5 columns → `Ｄｅｆ＋１` 5, growth +0** — the property the whole item table's affordability against bank 40 rests on. DATA 226, 239, 272 all rendered. **The first `防御力` stat rows ever shipped.** Original note follows:  ⚠️ **Exact analogy with `攻撃力＋ＮＮ` → `Ａｔｋ＋ＮＮ` (§4; 32+ instances already shipped). Prose keeps *defence power*.** **No `防御力＋ＮＮ` stat row has ever shipped — these are the first.** The form is **zero-growth** (5–6 columns in, 5–6 out) and that is load-bearing: **bank 40 has 447 bytes free**, and the armour rows are affordable only because the stat tail does not grow |
| ~~ボウガン~~ | `ｃｒｏｓｓｂｏｗ` | script DATA 224 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 8 columns, the seeded cell exact. DATA 224 — exhausted. Original note follows:  8 columns |
| ~~ボウキャノン~~ | `ｂｏｗ　ｃａｎｎｏｎ` | script DATA 225 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 10 columns, the seeded cell exact. DATA 225 — exhausted. Original note follows:  10 columns; kept audibly distinct from ボウガン. Alt *Bowcannon* |
| ~~ひみつの店~~ | `ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ` | script DATA 310 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** **Settled lowercase on use, as this row asked** — it is not a named shop: its whole reach is DATA 310, with no `『　』` and in no menu, unlike `『ビーストショップ』`. Rendered possessively `Ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ’ｓ`. Exhausted. Original note follows:  ⚠️ Lowercase **unless** it proves to be a *named* shop like `Ｂｅａｓｔ　Ｓｈｏｐ` (§12) — settle it on use and say which |
| ~~会員証~~ | `ｍｅｍｂｅｒｓｈｉｐ　ｃａｒｄ` | script DATA 310 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** **The seed's own tight-row Alt `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` (13) taken, which this row licenses** — `ｍｅｍｂｅｒｓｈｉｐ　ｃａｒｄ` (15) costs +48 against bank 40's 75 instead of +44. DATA 310 — exhausted. Original note follows:  15 columns. Alt *ｍｅｍｂｅｒ’ｓ　ｃａｒｄ* (13) if the row is tight |
| ~~鋼鉄の手袋~~ | `ｓｔｅｅｌ　ｇａｕｎｔｌｅｔｓ` | script DATA 272 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 15 columns, seeded cell exact. DATA 272 — exhausted. `腕を守る` is compressed to the attributive `ａｒｍ` (§2.1 step 5), flagged in the PR and at §AM. Original note follows:  `腕を守る` → *that guard the arms* |
| ~~鉄製の鎧~~ | `ｉｒｏｎ　ａｒｍｏｕｒ` | script DATA 239 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 11 columns, British per §4, seeded cell exact. DATA 239 — exhausted. `動きやすい` → `Ｓｕｐｐｌｅ` (§2.1 step 4), flagged. Original note follows:  British per §4; `動きやすい` → *easy to move in* |
| ~~ダミーよろい１／２~~ | `ｄｕｍｍｙ　ａｒｍｏｕｒ　１` / `ｄｕｍｍｙ　ａｒｍｏｕｒ　２` | script DATA 261, 262 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 14 columns. Inside §4's `です` frame → `Ｔｈｉｓ　ｉｓ　ｄｕｍｍｙ　ａｒｍｏｕｒ　Ｎ．`, matching shipped `ダミーぶきです` → `Ｔｈｉｓ　ｉｓ　ａ　ｄｕｍｍｙ　ｗｅａｐｏｎ．` (`batch_001.tsv:6`, read at review). DATA 261/262 — exhausted. Original note follows:  Matches the shipped `Ｔｈｉｓ　ｉｓ　ａ　ｄｕｍｍｙ　ｗｅａｐｏｎ．` pattern |
| 軍神ヘルメス | *the war god* `Ｈｅｒｍｅｓ` | script DATA 300 ✅ (PR #32) **and DATA 281 — OUTSTANDING, and this is what keeps the row live** | ⚠️ **THIS ROW STAYS LIVE. Its "Where seen" cell named only DATA 300 and that was incomplete — corrected in place 2026-09-10 (§4.3, PR #32 review), verified by direct census over both dumps, not taken from the PR: `軍神ヘルメス` is 2 script-unique lines / 42 instances, 0 battle.** DATA 300 (`…漆黒の石版。`) is rendered by `batch_010`; **DATA 281 (`軍神ヘルメスの愛用したブーツ。{FFFE}防御力＋１　魔法防御＋１`, count 21) is untranslated.** Whoever takes DATA 281 needs a **`魔法防御`** form beside §51.1's `Ｄｅｆ＋ＮＮ`, and it also carries `愛用` → `ｆａｖｏｕｒ` (§27.1). ⚠️ **It may now be unshippable: DATA 281 is a 21-instance line, so its growth is spent in all 21 banks including bank 40, which has 75 bytes free after PR #32.** A two-stat row at zero growth is the only thing that fits.  Pattern of §22.1 — `軍神オーディン` → *the war god Ｏｄｉｎ*, `魔神ティール` → *the demon god Ｔｙｒ*. ⚠️ **This line discharges the §9 `石版` → `ｔａｂｌｅｔ` row** |
| ~~『カルボナイト』~~ | `“Ｃａｒｂｏｎｉｔｅ”` | script DATA 880 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 11 columns with §12 quotes. DATA 880 ×2 — exhausted. Original note follows:  A **named crafting material**; `『…』` → `“…”` per §12 |
| ~~『ジェムストーン』~~ | `“Ｇｅｍｓｔｏｎｅ”` | script DATA 880 | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 10 columns with §12 quotes, held distinct from the bare lowercase `ｇｅｍｓｔｏｎｅ` exactly as this row asked. DATA 880 — exhausted. Original note follows:  ⚠️ **Distinct from the bare `ｇｅｍｓｔｏｎｅ` already in §33's table** — the quoted form is the material's *name* (capitalised); the bare noun stays lowercase |
| ~~ヒーリング~~ | `ｈｅａｌｉｎｇ` | script DATA 908, 909 (×3) | ✅ **PROMOTED to §51 and STRUCK (PR #32, merged 2026-09-10) — used exactly as seeded.** 7 columns, lowercase. ⚠️ **Not a new form** — `batch_003.tsv:27, :29` already ship `ｈｅａｌｉｎｇ`; DATA 908 ×2 and 909 ×1 match them. Exhausted. Original note follows:  Common noun (`ヒーリング能力を持つ`), not a named spell — lowercase |
| ピクシー | `Ｐｉｘｉｅ` | script DATA 909 ✅ (PR #32) **and DATA 817 — OUTSTANDING, this is what keeps the row live** | 5 columns. Capitalised as a class **name** on §4's `フリーナイト` → `Ｆｒｅｅ　Ｋｎｉｇｈｔ` / `ビーストマスター` → `Ｂｅａｓｔ　Ｍａｓｔｅｒ`. ⚠️ **NOT a hapax and NOT exhausted — 2 script-unique lines, 0 battle, verified by census at PR #32's review**: DATA 909 (rendered) and DATA 817 (`わたしたちピクシーは、…`, untranslated). Held live per the `ルート` precedent (§29.1 / §30.1). Siblings `シルフ` → `Ｓｙｌｐｈ` and `セイレーン` → `Ｓｉｒｅｎ` ARE hapaxes and are fixed at §51.2 |
---

**Wave 9 seeds (2026-09-10) — script batches 011 (town/shop NPCs), 012 (main plot + casino) and
013 (tavern + tactics lectures).** Every width is `len()`-measured and **every "Where seen" DATA
number was verified by census against `dumps/script_unique.txt`, not carried over from a draft** —
four figures in the first draft of this table were wrong and were corrected before it was committed.
DATA = 1-based index among non-blank, non-comment lines of `script_unique.txt`; **FILE = DATA + 5**.

⚠️ **FOUR RULINGS THIS WAVE'S SOURCE NEEDS ARE ALREADY FIXED — do not re-decide them and do not
seed them again:** `ゲロゲロ` → **`Ｒｉｂｂｉｔ`** plus the frog merchant's blunt, article-dropping
katakana register (**§5** — and batch 011 *is* that scene); `妖精` → **`ｆａｉｒｙ`**, lowercase common
noun (**§1**); `ジュエル` → **`Ｊｅｗｅｌ`** held distinct from `ジェム` → **`Ｇｅｍ`** (**§3**); and
`『…』` / `「…」` → **`“…”`** (**§12**, §3).

⚠️ **TWO TERMS ARE RENDERED BY TWO DIFFERENT BATCHES OF THIS SAME WAVE.** Neither translator can
see the other's file, so the form must come from here or they will diverge and gate 6 will not
catch it (gate 6 pairs whole messages, and these are different messages):
1. **`『極上のワイン』` — batch 012 DATA 370, 371, 372, 373 *and* batch 013 DATA 934, 939.** It is
   **already seeded and live** at §9 / §38.1 as `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` (13), waiting since PR #20
   for "the unit that first renders it". **Both units render it; both use that exact form.** The
   bare noun `ワイン` → `ｗｉｎｅ` is already promoted and must not change.
2. **The Member Shop / Member Card complex** — see the two rows below.

| Japanese | Proposed English | Where seen (verified) | Alternatives if the reading is open |
|---|---|---|---|
| ~~メンバーカード~~ | ✅ **PROMOTED to §52 and STRUCK (PR #34, merged 2026-09-10) — NOT as seeded: the seed’s own listed Alt `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` (13) was taken instead of `Ｍｅｍｂｅｒ　Ｃａｒｄ` (11), which is exactly what this row asked for ("settle it on use, say which and why").** The two shops ARE one object under two Japanese names, and the test this row set is met on measurement: `会員証` (§51.1, shipped `Ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ’ｓ　ｍｅｍｂｅｒ’ｓ　ｃａｒｄ．` at DATA 310, a 21-instance row) lands in **bank 15**, which is `batch_011`’s own bank — so §25.3’s co-occurrence test **FAILS**, and a capitalised `Ｍｅｍｂｅｒ　Ｃａｒｄ` at the door beside a lowercase `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` in the item list would read as two different objects. Widths reproduced with `len()` at review: 13 vs 11, and D674’s row measures 14, well inside 24 — **width forced nothing.** ⚠️ **DATA 1348 is still untranslated and must take `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` too**; `batch_012` (PR #35) carries **0** `メンバーカード`, verified at review, so there is no cross-unit conflict. Original seed note follows:  ⚠️ **MAY ALREADY BE FIXED UNDER ANOTHER JAPANESE WORD.** §51 ships `会員証` → `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` (13, lowercase) for DATA 310, `ひみつの店の会員証。` **Genuinely open — settle it on use, say which and why, and flag it.** Alt `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` (13) |
| ~~メンバーショップ~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `Ｍｅｍｂｅｒ　Ｓｈｏｐ`, **used exactly as seeded**, 11 columns reproduced with `len()` at review. DATA 362 is the corpus's only instance, so the row is **exhausted**. ⚠️ **The question this row tied to the row above IS answered, and the answer is that `batch_012` deliberately declines to answer it**: D362's source is a bare `このカードを`, so the line ships as `Ｌｅｔ　ｍｅ　ｇｉｖｅ　ｙｏｕ　ｔｈｉｓ　ｃａｒｄ．` with **no name at all**, and the Member Card question stays entirely with §52's `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ`. `batch_012` carries **0** `メンバーカード`, re-verified at this review. Original seed note follows:  A **named** shop (`珍しいアイテムが一杯のメンバーショップ`), so capitalised on §12's `Ｂｅａｓｔ　Ｓｈｏｐ`, unlike §51's lowercase `ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ` |
| ~~ミュートフルーツ~~ | ✅ **PROMOTED to §52 and STRUCK (PR #34, merged 2026-09-10) — used exactly as seeded.** `Ｍｕｔｅ　Ｆｒｕｉｔ`, 10 columns, the seeded cell exact under `len()` at review. DATA 690 is the corpus’s only instance (census over both dumps at review), so the row is **exhausted** and struck outright rather than left live. Unquoted, beside the quoted `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”` four rows earlier — the source quotes one and not the other, and both are preserved as the source has them. Original note follows:  A named item |
| ~~ツェペリ卿~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `Ｌｏｒｄ　Ｚｅｐｐｅｌｉ`, **used exactly as seeded**, 12 columns. DATA 386 is the corpus's only line carrying it — **exhausted**. The `卿` → *Lord* ruling this seed set is now rendered and stands. Original seed note follows:  ⚠️ **`卿` HAS NO RULING ANYWHERE IN THIS GLOSSARY** — this seed sets one, on the `様` → *Lady* precedent (§11, `フィリス様` → `Ｌａｄｙ　Ｐｈｙｌｌｉｓ`). Bare `Ｚｅｐｐｅｌｉ` is 7. Alt readings *Ｚｅｐｅｌｉ*, *Ｔｚｅｐｅｌｉ*; alt title *Ｓｉｒ* — all three rejected |
| ~~ブラックジャック~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `Ｂｌａｃｋｊａｃｋ`, **used exactly as seeded**, 9 columns. ⚠️ **The TERM is not exhausted; the row is struck because the form is now FIXED at §54.** The seed's own warning is what carries forward: DATA 1390, 1395 and 1416 are untranslated and **the casino batch later in the run inherits `Ｂｌａｃｋｊａｃｋ`** — one word, not *Black Jack*. Original seed note follows:  The casino game, capitalised as its name |
| ~~ポーカー~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `Ｐｏｋｅｒ`, **used exactly as seeded**, 5 columns, rendered 4× byte-identically at DATA 370–373 — **exhausted**. Original seed note follows:  Those are the same four lines that carry `『極上のワイン』` — long multi-branch blocks |
| ~~ディーラー~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `ｄｅａｌｅｒ`, lowercase, **used exactly as seeded**, 6 columns, shipped as the possessive `ｔｈｅ　ｄｅａｌｅｒ’ｓ`. DATA 355 is the corpus's only instance — **exhausted**. Original seed note follows:  Lowercase common noun (§17.1) — a role, not a name |
| ~~クーデター~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `ｃｏｕｐ`, lowercase, **used exactly as seeded**, 4 columns. ⚠️ **NOT exhausted**: DATA 863 and 1373 are untranslated and inherit this form. The accent warning was heeded — no `ｃｏｕｐ　ｄ’ｅｔａｔ` anywhere in `tl/`. Original seed note follows:  ⚠️ `ｃｏｕｐ　ｄ’ｅｔａｔ` needs an accent the charset lacks — do not reach for it |
| ~~町長~~ | ✅ **PROMOTED to §54 and STRUCK (PR #35, merged 2026-09-11)** — `ｔｏｗｎ　ｅｌｄｅｒ`, **used exactly as seeded**, 10 columns, and **the `ｍａｙｏｒ` alternative was NOT needed and stays unspent** — it belongs to §1's `市長`, which this same unit renders at DATA 375, so two source words take two English forms **inside one unit**. ⚠️ **NOT exhausted**: DATA 1102 is untranslated. Determiner ruling at §54.2. Original seed note follows:  The head of a small port town (`こんな港町の町長`) |
| ~~ウエイト / ウエイト値 / `『ウエイト値』`~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded; matches the `chunk_000` incumbent.  `Ｗａｉｔ` (4) / `Ｗａｉｔ　ｔｉｍｅ` (9) / `“Ｗａｉｔ　ｔｉｍｅ”` (11) | script **DATA 960, 967, 968, 969, 970, 977 (all batch 013)**; DATA 833 (not in this wave) | ⚠️ **NOT A NEW FORM — THE INCUMBENT IS ALREADY SHIPPED AND MUST BE MATCHED.** `tl/battle/chunk_000.txt:5`, the battle tutorial, reads `ｕｎｉｔｓ　ａｃｔ　ｉｎ　ｏｒｄｅｒ，{FFFE}ｆｒｏｍ　ｔｈｅ　ｌｏｗｅｓｔ　Ｗａｉｔ{FFFE}ｔｉｍｅ．` **Batch 013 is the tactics-lecture NPC teaching that same system**, so it matches that wording rather than re-coining it (§AG6's mirror). Do **not** reach for *Delay*, *Speed* or *Initiative* |
| ~~「待ち時間」~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `“ｗａｉｔｉｎｇ　ｔｉｍｅ”` (15) | script **DATA 977 (batch 013)** — the corpus's only instance | ⚠️ **DO NOT COLLAPSE THIS INTO `“Ｗａｉｔ”`.** DATA 977 glosses `『ウエイト値』` *with* 「待ち時間」 — the two must stay visibly different in English or the sentence explains a term with itself. ⚠️ **And `“Ｗａｉｔ”` is already taken**: §15.1 fixes the *menu label* `「待機」` → `“Ｗａｉｔ”`, a different source word (standby) — holding three things apart, not two |
| ~~戦術講座（第Ｎ回） / 講座Ｎ~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded; the Alt `ｌｅｓｓｏｎ` was not needed.  `ｔａｃｔｉｃｓ　ｌｅｃｔｕｒｅ` (15) / `Ｌｅｃｔｕｒｅ　Ｎ` (9) | script **DATA 958–963 (batch 013)**; `講座` alone runs to DATA 972 | The tavern NPC's numbered tutorial series — **the spine of batch 013**, so one form must serve the menu rows *and* the prose. Alt `ｔａｃｔｉｃｓ　ｃｌａｓｓ` (13), `ｌｅｓｓｏｎ` (6) if a menu row is tight |
| ~~`『妖精のケーキ』`~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `“Ｆａｉｒｙ　Ｃａｋｅ”` (12) | script **DATA 932, 933, 934, 937 (all batch 013)** | `『…』` → `“…”` (§12). ⚠️ **The bare noun `妖精` stays lowercase `ｆａｉｒｙ` (§1)** — only the *named item* is capitalised, exactly the `ｇｅｍｓｔｏｎｅ` / `“Ｇｅｍｓｔｏｎｅ”` split at §51 |
| ~~`『北風のシロップ』`~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded; the Alt was not needed.  `“Ｎｏｒｔｈ　Ｗｉｎｄ　Ｓｙｒｕｐ”` (18) | script **DATA 933, 934, 950, 951 (all batch 013)**; DATA 852 (not in this wave) | ⚠️ **The faithful `“Ｓｙｒｕｐ　ｏｆ　ｔｈｅ　Ｎｏｒｔｈ　Ｗｉｎｄ”` measures 25 and CANNOT FIT the 24-column box** — measured, not guessed. That is why the compound is proposed. Alt `“Ｎｏｒｔｈｗｉｎｄ　Ｓｙｒｕｐ”` (17) |
| ~~`『スーパージュエル』`~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `“Ｓｕｐｅｒ　Ｊｅｗｅｌ”` (13) | script **DATA 945, 946 (batch 013)**; DATA 843, 849 (not in this wave) | Holds §3's `Ｊｅｗｅｌ`, not *Gem* |
| ~~バニシュジュエル~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11) — AND CORRECTED, NOT SILENTLY: this seed was WRONG ON SUBSTANCE.** D946's source is `『バニシュジュエル』` — **quoted** — so §12 applies and the shipped form is `“Ｖａｎｉｓｈ　Ｊｅｗｅｌ”`. Widths `len()`-measured at review: bare **12**, quoted **14**. It is the corpus's only occurrence. The note below ("unquoted in its source") is the error, kept visible: | `Ｖａｎｉｓｈ　Ｊｅｗｅｌ` (12) | script **DATA 946 (batch 013)** | Same; unquoted in its source, so unquoted in English |
| ~~ゲストユニット~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded; menu rows take the singular lemma.  `ｇｕｅｓｔ　ｕｎｉｔ` (10) | script **DATA 962, 969, 970 (all batch 013)** | ⚠️ **A SCREEN LABEL FOR THIS IS ALREADY PROMOTED AND IS A DIFFERENT SOURCE STRING:** `『ＧＵＥＳＴ　ＵＮＩＴ』` → `“ＧＵＥＳＴ　ＵＮＩＴ”`, already full-width Latin in the source and **reproduced, not re-cased**. The katakana `ゲストユニット` is the *prose* form — lowercase common noun, on `ユニット` → `ｕｎｉｔ` (16× in `tl/`). **Keep the two apart and say which each row is** |
| ~~インターミッション~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded; **still open against §Z1 / Blocked 7**.  `Ｉｎｔｅｒｍｉｓｓｉｏｎ` (12) | script **DATA 978 (batch 013)**; DATA 1005, 1053 (not in this wave) | The between-battle phase, capitalised as the screen's name. ⚠️ If it proves to name an on-screen menu, it falls under §Z1's open UI-label question (Blocked 7) — flag rather than assume |
| ~~パラメータ~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `ｓｔａｔ` (4) | script **DATA 975 (batch 013)**; DATA 1225, 1229 (not in this wave) | `パラメータの個別アップ` = raising individual stats. Alt `ｐａｒａｍｅｔｅｒ` (9) — wide, and *stat* is the register the tutorial already uses |
| ~~ＳＳ技能~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `ＳＳ　ｓｋｉｌｌ` (8) | script **DATA 945 (batch 013)**; DATA 1258, 1259 (not in this wave) | Keep `ＳＳ` full-width as the source has it |
| ~~ローテーション~~ | ✅ **PROMOTED to §53 and STRUCK (PR #36, merged 2026-09-11)** — used exactly as seeded.  `ｒｏｔａｔｉｏｎ` (8) | script **DATA 978 (batch 013)** — the corpus's only instance | Lowercase system term |

⚠️ **`素早さ` WAS DRAFTED AS A SEED AND IS DELIBERATELY NOT ONE.** A census puts it at DATA 4, 6, 9,
35, 73 (**all already translated**), 830, 1236 — and **none of those is in wave 9's source**; batch
013's DATA 977 carries only the adverb `素早く`. Its incumbent, for whoever later takes DATA 1236
(`素早さ。行動の素早さに関係する。`, the stat's own definition row), is the **lowercase prose**
`ｓｐｅｅｄ` / `ｓｗｉｆｔ` already shipped in the class table — `Ａ　ｓｗｏｒｄ　ｗａｒｒｉｏｒ，　ｇｒｅａｔ{FFFE}ｉｎ
　ｓｐｅｅｄ　ａｎｄ　ｓｋｉｌｌ．` and `Ａ　ｓｗｉｆｔ，　ｓｋｉｌｆｕｌ　ｍａｌｅ` — **not** a capitalised `Ａｇｉｌｉｔｙ`,
which was this table's first draft and would have contradicted five shipped rows.

**Wave 10 seeds (2026-09-11) — script batches 014 (DATA 707–758), 015 (759–814) and 016 (815–869).**
Proposed forms follow the conventions already fixed: the `『…』` → `“…”` rule (§12), the species /
class test (§17.1 — a named class is capitalised like §4's `フリーナイト` → `Ｆｒｅｅ　Ｋｎｉｇｈｔ`, a
species or trade stays lowercase), European readings (§11.4, §14) and **British spellings**
(§4: *defence*, *armour*). Widths below are `len()` of the full-width string, measured, not counted
by hand (§4.3, and wave 9's eighth-error near miss).

⚠️ **TABLE A FIRST — THESE ARE NOT PROPOSALS.** Every row in Table A is **already shipped English**
with **no glossary row of its own**, or a row whose Japanese is spelled differently in wave 10's
source. Gate 6 pairs whole messages on exact Japanese, so **not one of these is visible to it.**
Match the shipped form; do not re-coin. Where a row says *sample of one*, it is backed by a **single**
shipped instance — per wave 9's `いらっしゃいませ！！` finding, treat it as a lead to verify by
reading, not as a fixed distinction.

| Japanese | Shipped English — MATCH IT | Shipped where | Recurs in wave 10 at |
|---|---|---|---|
| `館の中は静まりかっている・・・。` | `Ｉｎｓｉｄｅ　ｔｈｅ　ｍａｎｓｉｏｎ{FFFE}ａｌｌ　ｉｓ　ｈｕｓｈｅｄ．．．．` | `batch_011` D700 (§52, `静まりかえる` row) | **D711, D714, D716** — ⚠️ the source spells it **`静まりかっている`** here and **`静まりかえっている`** at D700. **Not byte-identical, so gate 6 is blind to all three.** ⚠️ **DOT COUNT CORRECTED 2026-09-11 (PR #37): this row's single English string is right for D711 and D714 only.** Measured tails: **D711 `・・・。` = 4, D714 `・・・。` = 4, D716 `・・・。。` = 5** — D716 carries a **doubled 。**. §3.1 takes the source's count, so D716 ships **five** stops. Shipped that way in `batch_014`. |
| `館の中は静寂に　包まれている・・。` | — **a THIRD variant, not yet rendered anywhere** | — | **D717, D720.** ⚠️ *The mansion is wrapped in silence* — a **different Japanese sentence** from the two above, not a spelling variant, so it may legitimately take different English; decide deliberately rather than by default. **D717 and D720 carry identical readable text** (their tags differ, which is why they are two unique rows) and **must take byte-identical English.** |
| `貼り紙がしてある・・・` | `Ａ　ｎｏｔｉｃｅ　ｉｓ　ｐｏｓｔｅｄ．．．` | `batch_006` D633, `batch_011` D647 | **D724** (and D870, deferred to wave 11) |
| `親衛隊` | `ｇｕａｒｄ` (in `Ｈｅｌｆｅｒ’ｓ　ｇｕａｒｄ`) | `batch_010` — ⚠️ **sample of one**, and **no glossary row exists** | **D789, D791, D792, D793, D794 — five**, all in `batch_015`. Wave 10 takes the corpus from 1 rendered instance to 6, so this unit, not the incumbent, effectively fixes the term. Read D791 (`かつてのカーライン…`) and D794 (`親衛隊だか何だか知らねえが` — hostile, colloquial) before fixing on it. ⚠️ **FULL CENSUS, corrected 2026-09-11 (PR #39): 7 script-unique lines, 0 battle** — the five above (bank 20), **D898** (bank 28, shipped in `batch_010`), and **D1330 (bank 40)**. **Bank 40 has 75 bytes free**, i.e. a spendable budget of zero under §F2, so D1330 may never land without an engine-side fix. **This row therefore STAYS LIVE after wave 10 merges.** |
| `素早さ` | lowercase `ｓｐｅｅｄ` / `ｓｗｉｆｔ` | `batch_001` ×3, `batch_003` — **five shipped rows** | **D830.** ⚠️ §9's wave-9 block **already names D830**. `Ａｇｉｌｉｔｙ` was that table's rejected first draft — do not revive it. |
| `機械兵` | `ｍａｃｈｉｎｅ　ｓｏｌｄｉｅｒ` | 13 shipped messages (`batch_003/005/010/012`) | **D726, D739, D744** (`batch_014`) and **D835, D836** (`batch_016`) — 5 lines, **8 occurrences**. Cross-unit. |
| `材料` | `ｍａｔｅｒｉａｌｓ` (weapon-crafting sense) | §54's sense-split row | **D726, D737, D744, D746** (`batch_014`) and **D807** (`batch_015`) — 5 lines, **8 occurrences**. Cross-unit. ⚠️ wave 10 adds a **third** sense (machine-soldier parts); §54 splits only cake vs weapon. Read before assuming. |
| `功績` | `Ｍｅｒｉｔ` (capitalised) | §38 row, `batch_007` | D758 ×2, D769 |
| `ジェムストーン` | `“Ｇｅｍｓｔｏｎｅ”` | `batch_013` D880 | D744 |
| `極上のワイン` | `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` | `batch_012` ×6 | **D765, D770, D772** (`batch_015`) and **D857** (`batch_016`) — 4 occurrences. Cross-unit. |
| `カジノ` | `ｃａｓｉｎｏ`, lowercase | `batch_010` ×2 | D747, D750, D812 |
| `マーベラス` | `Ｍａｒｖｅｌｌｏｕｓ` | `batch_010`; §21.1 | D797, D806 |
| `カッフィ` | `Ｃａｆｆｉ` / `Ｃａｆｆｉ　Ｐｏｒｔ` | §39 (promoted wave-6 seed) | **D867** |
| `踊り子` | `ｄａｎｃｅｒ` | `batch_012` ×2 | **D719** (`batch_014`), **D773, D774** (`batch_015`), **D863** (`batch_016`) — 4 lines, **8 occurrences**. ⚠️ **The only term in this wave that spans all three units**, and D719 spells it in **kana** (`踊り子さん` vs `おどりこ` in the D715 item name). |
| `館` | `ｍａｎｓｉｏｎ` | `batch_009`, `batch_011` | D711, D714, D716, D717, D720 |

**Table B — genuinely new: in wave 10's source, absent from `glossary.md`. Proposed, not fixed.**

| Japanese | Proposed English | Where seen | Alternatives / note |
|---|---|---|---|
| `“ヘルグレイブ”` | `“Ｈｅｌｇｒａｖｅ”` (10) | D712, a weapon found in the dark | ⚠️ **The source already writes this in `“ ”`, not `『 』`** — reproduce the source's own quotes, do not convert. Alt `Ｈｅｌｌｇｒａｖｅ` |
| `『おどりこの指輪』` | `“Ｄａｎｃｅｒ’ｓ　Ｒｉｎｇ”` (15) | D715 | `踊り子` already ships `ｄａｎｃｅｒ`; the source spells it **kana** here. Alt `“Ｒｉｎｇ　ｏｆ　ｔｈｅ　Ｄａｎｃｅｒ”` (20) |
| `『暗黒の指輪』` | `“Ｄａｒｋ　Ｒｉｎｇ”` (11) | D722 | `暗黒` → *dark* is already fixed (§ダークナイト row). Alt `“Ｒｉｎｇ　ｏｆ　Ｄａｒｋｎｅｓｓ”` (18) |
| `『コアプラント』` | `“Ｃｏｒｅ　Ｐｌａｎｔ”` (12) | D744 ×3 — the machine soldier's power core, which `ブラックボックス` sits inside | Alt `“Ｃｏｒｅｐｌａｎｔ”` (11) |
| `ブラックボックス` | `ｂｌａｃｋ　ｂｏｘ` (9) | D744 | lowercase — a common noun, not a named part (§17.1) |
| `ボネット平原` | `Ｂｏｎｎｅｔ　Ｐｌａｉｎ` (12) | D745, where the airship came down | A **place**. Alt `Ｂｏｎｎｅｔ　Ｐｌａｉｎｓ` (13) |
| `『虹のドレス』` | `“Ｒａｉｎｂｏｗ　Ｄｒｅｓｓ”` (15) | D748, a casino prize | — |
| ~~`バウアーの砦`~~ | ⛔ **SEED WITHDRAWN 2026-09-11 (PR #37) — use the INCUMBENT `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` (12) / `Ｂａｕｅｒ` (5).** My `Ｆｏｒｔ　Ｂａｕｅｒ` would have split a shipped proper noun. | D757 (`batch_014`), **D1300 (a later wave inherits this)** | ⚠️ **Why the seed missed it: a KANA SPELLING VARIANT.** §2 has carried `バウワーの砦` → `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` since ch.40, and `tl/battle/chunk_040.txt` **ships** `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` and `Ｂａｕｅｒ`. Census: `バウアー` script **2** / battle **1**; `バウワー` script **0** / battle **1**. I searched the glossary for `バウアー`, found nothing, and never searched `バウワー` — **§AG6's mirror exactly: I measured the alternative and never looked for the incumbent.** An exact-key grep cannot see this and gate 6 cannot catch it. Caught by `batch_014`'s translator. |
| `『功績レベル』` | `“Ｍｅｒｉｔ　Ｌｅｖｅｌ”` (13) | D758 ×2 | Built from the fixed `功績` → `Ｍｅｒｉｔ` and lowercase prose `ｌｅｖｅｌ` |
| `能力値` | `ａｂｉｌｉｔｙ　ｓｃｏｒｅｓ` (14) | D758 | Alt `ｓｔａｔｓ` (5) if the row is tight |
| `隠れ家` | `ｈｉｄｅｏｕｔ` (7) | D714, the pickpocket's | `スリ` → `ｐｉｃｋｐｏｃｋｅｔ` is **binding** (3 shipped, `batch_012`) |
| `「只今、研究開発中」` | `“Ｒｅｓｅａｒｃｈ　ｉｎ　ｐｒｏｇｒｅｓｓ”` (22) | D724, the workshop's sign | The `貼り紙` row (§34) fixes the frame; only the sign text is open |
| `戒厳令` | `ｍａｒｔｉａｌ　ｌａｗ` (11) | D787 | — |
| `エクスカリバー` | `Ｅｘｃａｌｉｂｕｒ` (9) | D803, `伝説の剣` | — |
| `ヘヴィメイル` | `Ｈｅａｖｙ　Ｍａｉｌ` (10) | D801, armour worn by an imperial soldier | Capitalised: a named item. Alt `ｈｅａｖｙ　ｍａｉｌ` |
| `旅芸人の一座` | `ａ　ｔｒａｖｅｌｌｉｎｇ　ｔｒｏｕｐｅ` (19) | D760, D774 | British `‐ll‐`. Alt `ａ　ｔｒｏｕｐｅ　ｏｆ　ｐｌａｙｅｒｓ` (19) |
| `幽霊` | `ｇｈｏｓｔ` (5) | D762 | — |
| `仙人` | `ｈｅｒｍｉｔ` (6) | **D756 and D782 — and the two are NOT the same construction** | ⚠️ **CORRECTED 2026-09-11 (PR #37). My seed asked for a compound `生き返りの仙人` at "D756, D782"; that compound is at neither, as written.** **D756** reads `死んだ人を　生き返らせる術を使う　仙人` — a *verb phrase* plus a bare `仙人`, not a compound. **D782** reads `生き返りの{FFFE}仙人さん` — the compound **is** in the readable text, but a `{FFFE}` sits inside it, so it is **0 hits on a raw grep of every dump** and invisible to any exact-key search. **That split is method note 1 in miniature**: the term is real, and only a Japanese-side sub-message sweep finds it. `ｈｅｒｍｉｔ` shipped at D756 (`batch_014`); **D782 belongs to `batch_015`** and must match. Alt `ｓａｇｅ` (4) |
| `アーマーナイト` | `Ａｒｍｏｕｒ　Ｋｎｉｇｈｔ` (13) | D828, a unit class | ⚠️ **British `ａｒｍｏｕｒ`** — the corpus ships `ａｒｍｏｕｒ` **10 times and `ａｒｍｏｒ` 0 times**. `Ａｒｍｏｒ　Ｋｎｉｇｈｔ` **REJECTED** on that count. Capitalised per §4's `フリーナイト` |
| `腕力` | `ｓｔｒｅｎｇｔｈ` (8) | D829 | lowercase prose, like `attack power` / `speed`. Alt `ｐｏｗｅｒ` (5) — **rejected**: `パワー` already ships as `ｐｏｗｅｒ` (`batch_001`, `ｂｏｔｈ　ｐｏｗｅｒ　ａｎｄ　ｓｐｅｅｄ`), so reusing it here would merge two distinct source words |
| `頑丈さ` | `ｔｏｕｇｈｎｅｓｓ` (9) | D831 | Alt `ｓｔｕｒｄｉｎｅｓｓ` (10) |
| `移動力` | `ｍｏｖｅｍｅｎｔ` (8) | D827 | ⚠️ §4 fixes **`機動力` → `ｍｏｂｉｌｉｔｙ`**, a *different* word. **Do not collapse the two.** |
| `体力` | `ｓｔａｍｉｎａ` (7) | D834, restored in castles and forts | Alt `ｈｅａｌｔｈ` (6), `ＨＰ` (2) |
| `保険屋` | `ｉｎｓｕｒａｎｃｅ　ｏｆｆｉｃｅ` (16) | D840, a shop you enter | Alt `ｉｎｓｕｒｅｒ` (7) |
| `保険金` | `ｉｎｓｕｒａｎｃｅ　ｐａｙｍｅｎｔ` (17) | D842 | — |
| `慰霊金` | `ｃｏｎｄｏｌｅｎｃｅ　ｐａｙｍｅｎｔ` (18) | D845 — paid for soldiers killed in service | Alt `ｓｏｌａｔｉｕｍ` (8) — accurate but rare; `ｄｅａｔｈ　ｂｅｎｅｆｉｔ` (13) |
| `「本日休業」` | `“Ｃｌｏｓｅｄ　ｔｏｄａｙ”` (14) | D839 | §34's `貼り紙` row already fixes `休業いたします` → `Ｃｌｏｓｅｄ` |
| `終止符をうつ` | `ｐｕｔ　ａｎ　ｅｎｄ　ｔｏ` (13) | D821 | An **idiom**, not a term; no row is being asked for |
| `荷揚げ` | `ｕｎｌｏａｄｉｎｇ` (9) | D851 | — |

⚠️ **`勝ってカブトの・・・` (D783) is a PROVERB, not a term** — `勝って兜の緒を締めよ`, *tighten your
helmet-cords after the victory*. The speaker trails off mid-idiom, so the English must trail off too;
**no glossary row is proposed and none should be coined.**

---

## 10. Open questions

1. ~~**リオン — Lion or Leon.**~~ ✅ **RESOLVED 2026-09-08 (PR #7 review).** The character appears
   in battle chunk 6 and is rendered **`Ｌｅｏｎ`**; §1's row now carries the decided form instead
   of the placeholder. This question had been open since the glossary was written. See §24.1.
2. ~~**Class/unit name table.**~~ **PROSE FORMS RESOLVED 2026-08-06 (§17.1); the table itself is
   still untouched.** The ≤ 20-character label forms still need fixing, but the rule that decides
   their capitalisation — and every prose mention of a class in the description table — is now
   settled. §13.12 and §13.17 are resolved by the same rule.
3. **Description window row count.** 3 or 4 rows is unconfirmed; §3.2 of the prompt keeps
   descriptions to 2 lines + Gem Type until someone checks in-game. `batch_003` holds every one
   of its 102 entries to that shape. ⚠️ **`batch_001` does not** — five entries there render three
   description rows plus the Gem Type row, i.e. four rows. They were shipped before this rule was
   written down. If the window turns out to be three rows, those five need re-cutting; nothing in
   `batch_003` does. Listed in `FLAGS.md`.
4. **`{FCC0}{FFFE}` leading break.** Whether it wastes a top row is unconfirmed. Preserve for now.
   Related: a page carrying a leading blank *and* four text rows *and* a trailing blank has never
   appeared in the source — tier E avoided producing one. Worth settling with the same in-game check.
5. **`ダミーぶきです` padding.** The source pads to 11 columns with trailing `　`; the English is 23
   and drops the padding. If that field turns out to be fixed-width, shorten to
   `Ｄｕｍｍｙ　ｗｐｎ．` / `Ｄｕｍｍｙ　ａｒｍ．`.
6. ~~**`ほう` may already be rendered in chunk 0.**~~ **RESOLVED 2026‐08‐06.** Chunk 0 line 14
   renders Rimul's `ほう・・・。` as `Ｏｈ．．．．`. Per this entry's own rule chunk 0 wins, so
   **ほう / ほお → `Ｏｈ`**, and §6's `Ｈｏｈ` entry is superseded. Used as `Ｏｈ` in script 1234.
   ✅ **`tl/battle/chunk_035.txt` is now fixed** (2026-08-06, batch 003 session): the line reads
   `Ｏｈ，`. Same width, no re-flow; the chunk went 557 → 555 bytes. **No `Ｈｏｈ` remains anywhere
   in `tl/`,** so §11.5's "distinct from ほう → Ｈｏｈ" should be read as *distinct from ほう → Ｏｈ*. Same width, so no re‐flow is needed.
7. **Player gender.** Ch.12 renders Shiron's `あんちゃん` as `ｌａｄ`, which assumes a male player
   character. If the name is free-entry with no fixed gender, swap to `ｆｒｉｅｎｄ` — same 18
   columns.
8. ~~**Numerals in prose.**~~ ✅ **RESOLVED 2026-09-09 (PR #18 review). Cardinals in running prose
   are SPELLED OUT; full-width digits stay in fixed names and in tables of numbers.** Two agreeing
   prose instances now: `chunk_012` message 1's `あと３時間だ。` → `Ｔｈｒｅｅ　ｈｏｕｒｓ　ｒｅｍａｉｎ．`
   and `chunk_021` line 10's `１０年前に` → `ｔｅｎ　ｙｅａｒｓ　ａｇｏ`. The two exceptions were already
   fixed and are what the rule must not disturb: **§2's army numbers** (`９ｔｈ　Ａｒｍｙ`,
   `２ｎｄ　Ａｒｍｙ` — both in chunk 21, on the same rows as the spelled-out `ｔｅｎ`), the `Ｕｎｉｔ　４` /
   `ＣｌａｓｓＮＮ` label slots (§4, §11.2), and **§15.1's table of numbers** (`１・２着`, `３−６`,
   `１２３４５`), which narrowed this question in the first place. The formulation fits every shipped
   line in `tl/`. See §36.6.
9. **`これ以上砂は増やしたくないな`** (ch.14) is rendered literally as "I do not want to add any
   more to the sand" because it is unclear whether the sand grows by petrified victims or this is a
   figure for casualties. Check the map in-game.
10. **`訊ねたい` vs `尋ねたい`** — chunk 0 uses both spellings for the same phrase in Rimul's two
    variant speeches. Probably a source typo; it will matter to whoever dedupes chunk 0.
11. **The ch.35 mansion speaker is unnamed.** Portrait 8, confident, two lines, no name anywhere in
    the chunk. If a later chunk names him, re-check his register.

---

## 11. Added by the chunk 43 spike (tier A feasibility, chunk 43)

Rendered in `pending/chunk_043.txt`. Chunk 43 is the final chapter: the Helfer confrontation in
the sky-fortress control room, Rimul's revenge for Guilford, the self-destruct, and the airship
epilogue.

### 11.1 People

| Japanese | English | Note |
|---|---|---|
| ヘルファー | Helfer | final boss, commander of the floating island. Alt *Hellfar*; Helfer chosen to match the game's German/European naming (Bauer, Carline). 6 chars, clears the ≤ 16 unit cap |
| ティミー | Timmy | **promoted from §9 PROVISIONAL** — rendered in ch.43, where she is addressed by name and told to flee |

### 11.2 Places, factions, ranks

| Japanese | English | Note |
|---|---|---|
| フェリスランド | Ferisland | the land the island's lasers threaten. Alt *Felisland*, *Ferrisland*. ⚠️ **CORRECTED 2026-09-08 (§4.3, PR #8 review): this row said “appears nowhere else in either dump”, and that is false** — **2 battle + 11 script occurrences**, including script 1001 (`フェリスランドへ行ったんだが` → `Ｉ　ｗｅｎｔ　ｔｏ　Ｆｅｒｉｓｌａｎｄ`, now shipped in `batch_005`) and `ホアグ王子はフェリスランドだ`. **The rendering `Ｆｅｒｉｓｌａｎｄ` is unchanged, so no translated line needs revisiting** — only the note was wrong. See §26.1 |
| ハイランド / 古代ハイランド | Highland / ancient Highland | the vanished civilisation that built the fortress |
| 浮遊島 | the floating island | |
| 空中要塞 | sky fortress | keep distinct from 要塞 → fortress |
| 指令官 | Commander | the source spells it 指令官, not 司令官 — treated as the same word |
| ４号機 | Ｕｎｉｔ　４ | the machine the 9th Army destroyed; digit stays full-width |

### 11.3 Items and mechanics

| Japanese | English | Note |
|---|---|---|
| 自爆装置 | ｓｅｌｆ‐ｄｅｓｔｒｕｃｔ | uses ‐ (U+2010); 13 columns |
| 解除装置 | the switch | "shutoff device" is 15 columns and will not share a line — **switch** is the fixed short form |
| レーザー兵器 | lasers / laser weapons | |
| コントロール室 | control room | |

### 11.4 Classes

| Japanese | English | Note |
|---|---|---|
| 魔導師 | wizard | Guilford. Distinct from 魔術師 → mage and 女魔術師 → sorceress |

### 11.5 Tics and interjections

| Japanese | English | Note |
|---|---|---|
| くっ / クッ | Ｔｃｈ | vexation. **Distinct** from ムムッ / ふっ / フンッ → Ｈｍｐｈ and from ほう → Ｏｈ (§10.6). ✅ **`tl/battle/chunk_000.txt` line 20 is now fixed** (2026-09-08): it rendered `くっ・・・` as `Ｕｇｈ．．．` against `chunk_007.txt` line 12's `Ｔｃｈ．．．` — identical Japanese, divergent English. Same 6 columns, no byte change. **No `Ｕｇｈ` for くっ remains anywhere in `tl/`**, which frees `Ｕｇｈ` for ううっ. See §18.3 |
| グワアアアァァ | Ｇｗａａａａａｈ | death cry; extends the existing ぐわっ → Ｇｗａｈ |
| フハハハ… | Ｆｕｈａｈａｈａ… | Helfer's laugh; length tracks the source's kana count |
| 雑草ども | weeds | Helfer's contemptuous term for the 9th Army; recurs, keep it |
| 命の恩人 | your rescuer | 9 columns; "the man who saved you" never fits |

### 11.6 Register

| Who | Register |
|---|---|
| Helfer | grandiose and archaic, no contractions; calls the party **weeds** and **rabble**. His register is what makes him expensive to translate — see FLAGS |

---

## 12. Added by chunk 33 (the sanctuary / class-change trial)

Rendered in `tl/battle/chunk_033.txt`. Chunk 33 was missing from `battle_dump.txt` until the
dumper's `{FC51}`-only detector was fixed (`findings.md` §23) — it is the sanctuary map: an
unnamed sorceress tests the party's mage and grants the “Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”.

### 12.1 Places and items

| Japanese | English | Note |
|---|---|---|
| 聖堂 | sanctuary | 9 columns. Not “cathedral” / “sacred hall” — both are too wide to share a line and the place is a mages' preserve, not a church |
| 『知識の書』 | “Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ” | `『…』` → `“…”`; 20 columns with the quotes, so it never shares a line with anything but a short article |
| 魔道の力 | the power of magic | 魔道 here is the art, not a person — do not confuse with 魔導師 |

### 12.2 Classes

| Japanese | English | Note |
|---|---|---|
| ウィザード | Ｗｉｚａｒｄ | **capitalised** — a named class, like フリーナイト → Free Knight. The advanced class a 魔術師 changes into. ⚠️ collides with 魔導師 → wizard from §11.4 — see §13.12 |

### 12.3 Tics and interjections

| Japanese | English | Note |
|---|---|---|
| ふふ | Ｆｕｆｕ | soft, amused feminine chuckle. Transliterated to match フハハハ → Ｆｕｈａｈａｈａ (§11.5). **Distinct** from ムムッ/ふっ → Ｈｍｐｈ and ほう → Ｈｏｈ. Alt `Ｈｅｈ　ｈｅｈ` — see FLAGS |

### 12.4 Register

| Who | Register |
|---|---|
| The sanctuary sorceress (ch.33) | poised and imperious, no contractions; `Ｉ　ｓｈａｌｌ`, `Ｖｅｒｙ　ｗｅｌｌ`, `Ｃｏｍｅ　ａｔ　ｍｅ`. Close to Rimul's register but warmer once the party wins — she is a teacher, not an enemy. Unnamed in this chunk |
| Deployment-restriction boxes (`{=FA1000300030}`) | as §7 tutorial boxes — plain instructional second person, no personality |

---

## 14. Added by chunks 5 and 7 (the fairy forest; the Black Knights and Nacol)

Chunk 7 is rendered in `tl/battle/chunk_007.txt`. Chunk 5 is rendered in
`pending/chunk_005.txt` and **does not ship** — it misses its slot by 487 bytes (see
`FLAGS.md` and `pending/README.md`). The names below are decided regardless, because
chunk 7 uses several of them and later chunks will use the rest.

### 14.1 People

| Japanese | English | Note |
|---|---|---|
| キャビア | Ｃａｖｉａ | The Princess's given name, first revealed here (ch.5 `キャビア王女`, ch.7 `キャビア様`). 5 columns, so `Ｐｒｉｎｃｅｓｓ　Ｃａｖｉａ` fits at 15. Alt *Caviar*, *Kyabia* — Cavia chosen as the plainer name-like form, matching Bauer / Carline / Helfer. ⚠️ see §13.14 |
| フェイ | Ｆｅｉ | Female 氷龍使い, warden of the fairy forest; joins the party in ch.5 |
| ナコール | Ｎａｃｏｌ | Cavia's aged former tutor (ch.7). Alt *Nakor*, *Nacoll*. ⚠️ see §13.15 |
| ティータ | Ｔｉｔａ | ch.5 line 1, `ティータ、合流して。戦うわよ。` — **one occurrence in the whole battle dump, zero in the script dump**. ⚠️ see §13.16 |
| フィリス様 | Ｌａｄｙ　Ｐｈｙｌｌｉｓ | 様 → Lady per the Rimul precedent. ch.5 reveals Phyllis is the 妖精の村の長. Does **not** change her §1 entry — only adds the honorific form |

### 14.2 Places, factions, ranks

| Japanese | English | Note |
|---|---|---|
| 黒の騎士団 | Ｂｌａｃｋ　Ｋｎｉｇｈｔｓ | Parallels 紅の騎士団 → Crimson Knights. 13 columns |
| ベルナールの教会 / ベルナール教会 | Ｂｅｒｎａｒｄ’ｓ　ｃｈｕｒｃｈ | Possessive form per バウワーの砦 → Bauer's fort. Alt *Bernal* |
| 妖精の森 | the fairy forest | 妖精 stays a lowercase common noun (§1) |
| 番人 | warden | Fei's role. Kept **distinct** from 守り神 → guardian |
| 守り神 | guardian | The forest's tutelary spirit, not a person |
| 妖精の村の長 | village elder | Phyllis's title |

### 14.3 Classes and roles

| Japanese | English | Note |
|---|---|---|
| 氷龍使い | ice dragon tamer | |
| 獣使い | beast tamer | 使い → *tamer* throughout, not *user* / *handler* |
| オーク | orc | **Promoted from §9 PROVISIONAL.** Lowercase common noun in prose, per the バジリスク → basilisk precedent. The class-table form is still open (§10.2) |
| 機械兵 | machine soldier | Unchanged from §4; recorded here because ch.7 is its first rendering |

### 14.4 Items and figures of speech

| Japanese | English | Note |
|---|---|---|
| 嘘ツキ先生 | the lying teacher | ch.7. Nacol, who lied about being cured to send Cavia home; the falling stars are read as his bouquet |
| 切り札 | ace | `帝国の切り札` → *their ace*. Not “trump card” — 11 columns saved and no card-game register in English |
| エチュード | etude | **No `é`** — the accented form is outside the §3.1 charset |
| ゴミ (as an insult) | rubbish | British, consistent with the existing spelling policy |

### 14.5 Tics and interjections

| Japanese | English | Note |
|---|---|---|
| クックックッ | Ｋｕｋｕｋｕ | Cold, clipped villain laugh. Kana beats tracked, as with フハハハハ → Ｆｕｈａｈａｈａ (§11.5) |
| ククククク | Ｋｕｋｕｋｕｋｕｋｕ | Same laugh, five beats — the length is doing work, so it is preserved |
| フハハハハハ | Ｆｕｈａｈａｈａｈａｈａ | Five ハ. Extends §11.5's four-beat entry; the entry itself is unchanged |
| ぐふっ | Ｇｕｆｆ | Struck-down grunt. Distinct from グッ → Ｇｕｈ and ぐわっ → Ｇｗａｈ (§11.5) |
| へっ | Ｈｅｈ | Ridge's cocky scoff. Distinct from ふっ / フンッ → Ｈｍｐｈ |
| ゴホッ | Ｃｏｕｇｈ | Nacol's sickbed cough. Rendered as an English word, not transliterated — `Ｇｏｈｏ` reads as a name |
| ええい | Ｅｎｏｕｇｈ！ | Exasperated officer's bark |
| うひょーっ | Ｗｈｏａａ！ | Delighted whoop |

### 14.6 Register

| Who | Register |
|---|---|
| Cavia (the Princess) | Warm, direct, **no contractions** — `Ｉ　ｓｈａｌｌ`, `ｌｅｔ　ｕｓ`, `Ａｒｅ　ｔｈｅｙ　ｎｏｔ`. Young and impulsive, not stiff. One deliberate exception, see `FLAGS.md` |
| Fei | Gentle but firm; light contractions. Speaks plainly about the forest and formally to Phyllis |
| Lady Phyllis | Formal, warm, maternal, no contractions |
| Nacol | Frail and deferential — `Ｌａｄｙ　Ｃａｖｉａ`, `Ｙｏｕ　ｍｕｓｔ　ｎｏｔ`. Never contracts, never commands except to send her home |
| The Black Knights commander (ch.7) | Cold and mocking; `Ｋｕｋｕｋｕ`, calls people rubbish. No contractions — the flatness is the menace |
| Anselmo-type Imperial officers (ch.7) | Blustering and superior; `Ｆｕｈａｈａｈａｈａｈａ`, rhetorical questions |

---

## 13. Open questions (continued from §10)

12. ~~**`ウィザード` vs `魔導師`.**~~ **RESOLVED 2026-08-06 — see §17.1. Both existing entries
    stand unchanged and nothing needs revisiting**, including `pending/chunk_043.txt`. They are
    the same class named two ways, and the species test explains why they are written differently:
    魔導師 names *what Guilford is* (a man who works magic → lowercase *wizard*), ウィザード names
    *the class conferred at the sanctuary trial* (→ `Ｗｉｚａｒｄ`).
13. **The ch.33 sorceress is unnamed.** No name anywhere in the chunk. If a later chunk names her,
    re-check her register.
14. **`キャビア` — Cavia or Caviar?** The kana are exactly the loanword for caviar, so the pun may
    be deliberate; but the game treats it as an ordinary royal name and the fish-roe reading is
    unusable in English. Rendered *Cavia*. Revisit only if a chunk plays on the food.
15. **`ナコール` — Nacol, Nakor or Nacoll?** No in-game romanisation found. *Nacol* chosen for width
    (5 columns, fits `Ｌａｄｙ　Ｃａｖｉａ`-length lines beside it).
16. **`ティータ` is a hapax.** One occurrence in `battle_dump.txt`, none in `script_dump.txt`.
    Not a typo for ティミー: in ch.5 line 10 Fei is *surprised* by Timmy's arrival, so she cannot
    have been calling her in line 1. Plausibly Fei's beast, since Fei is a 獣使い, or a cut
    character. Rendered *Tita* pending an in-game look.
17. ~~**`オーク` capitalisation.**~~ **RESOLVED 2026-08-06 — see §17.1.** Both halves, as the
    question asked: prose keeps lowercase *orc* (§14.3, unchanged), and the class-name table takes
    **`Ｏｒｃ`** — every entry in that table is capitalised, because it is a column of labels.

---

## 15. Added by script batch 002 (the war-council pool; the horse-race tutorial)

Rendered in `tl/script/batch_002.tsv` — `script_dump.txt` lines 1234 and 8604, the two
messages that blocked `assemble.py build` (`FLAGS.md` §A1–A2, now resolved).

### 15.1 Horse racing

The betting parlour tutorial. The four bracketed display headings are quoted in the source
with `「…」`, which becomes `“…”` per the `『…』` precedent in §3.

| Japanese | English | Note |
|---|---|---|
| 脚質 | “ｒｕｎｎｉｎｇ　ｓｔｙｌｅ” | 13 columns bare, 15 with the quotes — it will not share a row with much. The real racing term; not “leg quality” or “running type” |
| 前走までの順位 | “ｐａｓｔ　ｐｌａｃｉｎｇｓ” | 14 bare. The five-digit strip of finishing positions. **Placings**, British, consistent with the defence/armour spelling policy |
| 今回の調子 | “ｆｏｒｍ　ｔｏｄａｙ” | 12 bare. **form** is the racing word for condition |
| 調子 (bare, of a horse) | ｆｏｒｍ | 4 columns |
| 逃げる | ｌｉｋｅｓ　ｔｏ　ｌｅａｄ | The front-runner style. Not “runs away” |
| 追い込む | ｌｉｋｅｓ　ｔｏ　ｃｌｏｓｅ　ｆｒｏｍ　ｂｅｈｉｎｄ | The closer style. Needs two rows; kept in full because it is the paired opposite of *lead* and abbreviating one of the pair breaks the contrast |
| １・２着 | １ｓｔ　ａｎｄ　２ｎｄ | Digits stay full-width — this whole message is a table of numbers (`３−６`, `１２３４５`) and spelling them out would be unreadable. Narrows §10.8 |
| ３−６ | ３−６ | `−` is U+2212, which **is** in the §3.1 set. Reproduced exactly |

### 15.2 The war council

| Japanese | English | Note |
|---|---|---|
| 責任はどうとるつもりだ | ｈｏｗ　ｄｏ　ｙｏｕ　ｉｎｔｅｎｄ　ｔｏ　ａｎｓｗｅｒ　ｆｏｒ　ｔｈｉｓ | |
| 体面が保てる | ｋｅｅｐ　ｙｏｕｒ　ｆａｃｅ | |
| 恥さらし | ａ　ｄｉｓｇｒａｃｅ | |
| 黒幕 | ｗｈｏ　ｉｓ　ｂｅｈｉｎｄ　ｉｔ | Rendered as a clause, not the noun “mastermind”, because the source segment is a bare `黒幕が。` fragment standing alone |

### 15.3 Register

| Who | Register |
|---|---|
| The racetrack guide (script 8604) | Friendly and plain-spoken, light contractions (`ｉｔ’ｓ`, `ｌｅｔ’ｓ`, `ｙｏｕ’ｌｌ`). **Not** a §7 tutorial box — those are keyed to `{=FA1000300030}` and have no personality; she does, and the source's `～の` / `～よ` / `ゆー` carry it |
| Anselmo | Blustering and superior, no contractions — consistent with the “Anselmo-type Imperial officers” entry already in §14.6 |
| Alfred | Formal, defensive of his men, no contractions |
| The 9th Army side (script 1234) | Rough and clipped; `ぜ` / `てめえ` / `ねえ` carried by contractions |

---

## 16. The `×` button decision (FLAGS.md §A3 — settled 2026-08-06)

**Decision: `×ボタン` → `Ｃｒｏｓｓ　ｂｕｔｔｏｎ`.** Entered in §3. Option 1 of the two on the table.

**Why not the glyph (option 2).** `tools/riotfont.py` was checked before deciding, and the
answer is in two parts:

- **Space exists.** `SJIS_TO_ASCII` holds 88 codes; the compact routine stores 8 bytes per glyph
  plus a 2-byte code and a 4-byte pointer, so the whole table is about 1,232 bytes inside an
  8,704-byte `AUTO_WINDOW` (`0x800F3E00`–`0x800F6000`). One more glyph costs 14 bytes. **The font
  is not full** — that is worth recording, because §A3 assumed it might be.
- **But there is no ✗ to put in it.** Every glyph is derived from `font8x8(ch)`, which is indexed
  `ord(ch) - 0x20` into a 95-entry ASCII bitmap covering only U+0020–U+007E. SJIS `0x817E` (`×`)
  is not in `SJIS_TO_ASCII`, and nothing in the pipeline can supply a bitmap that is not an ASCII
  character. Adding ✗ means hand-authoring an 8×8 bitmap **and** changing `SJIS_TO_ASCII` /
  `font8_rows_msb` to accept raw glyph data instead of a character — then re-proving the hook on
  hardware. That is a tooling session, not a translation one, and it would not have round-tripped
  today.

**Why *Cross* and not *X*.** §3 already fixes ○ → `Ｃｉｒｃｌｅ　ｂｕｔｔｏｎ` and
□ → `Ｓｑｕａｒｅ　ｂｕｔｔｏｎ` — by **shape name**. `Ｘ　ｂｕｔｔｏｎ` would make ✗ the only
button named after the letter on the keycap, and §4.3 forbids restyling the other two silently to
match. *Cross* is also Sony's own European name for the button, so it is not an invention.
Width is not the deciding factor (`Ｘ　ｂｕｔｔｏｎ` is 8 columns, `Ｃｒｏｓｓ　ｂｕｔｔｏｎ` is 12);
both fit a 24-column row with room to spare, and there is no byte pressure in bank 43.

**Consequence.** △ → `Ｔｒｉａｎｇｌｅ　ｂｕｔｔｏｎ` is fixed in §3 at the same time, so the
question cannot be reopened one button at a time. If the font work is ever done, all four
entries change together, as a single §4.3 correction.

---

## 17. Added by script batch 003 (the monster / class / weapon description table)

Rendered in `tl/script/batch_003.tsv` — `script_unique.txt` lines 53–216: every remaining line
ending `ジェムタイプ：<colour>` (101 of them), plus the `クラス７０` placeholder. 2,142 message
instances. The vocabulary entries are in **§4**; this section carries the reasoning.

### 17.1 The class-name rule — the species test (resolves §10.2 prose forms, §13.12, §13.17)

The descriptions name other classes constantly, and get one wrong and it is wrong 21 times in a
table the player reads side by side. The rule, which fits **every** decision already made and
therefore requires no rework anywhere:

> **In the class-name TABLE, every entry is capitalised** — `Ｏｒｃ`, `Ｄｒａｇｏｎ`,
> `Ｋｉｌｌｅｒ　Ｗｏｌｆ`, `Ｗｉｚａｒｄ`. It is a column of labels, and a label column is
> capitalised throughout or not at all.
>
> **In description PROSE, apply the species test**: a class word is lowercase when it names
> *what a creature is* — a species, a kind, a trade — and capitalised only when it names *a title
> an individual holds*.

The test explains the existing entries rather than overriding them:

| Already fixed | Test says | Status |
|---|---|---|
| バジリスク → basilisk, オーク → orc, 妖精 → fairy, 武闘家 → martial artist | species / trade | ✅ unchanged |
| フリーナイト → Free Knight, ビーストマスター → Beast Master | conferred titles, coined | ✅ unchanged |
| 魔導師 → wizard (§11.4, Guilford) | what he *is* | ✅ unchanged |
| ウィザード → `Ｗｉｚａｒｄ` (§12.2, the sanctuary class) | the title *awarded* | ✅ unchanged |

So every creature named in this batch is **lowercase**: orc, ogre, giant, hobbit, brownie, fiend,
dragon, fairy, skeleton, slime, golem, roper, wraith, succubus, basilisk, dark elf, dark mage,
dark knight, killer wolf, grey ooze, gelatinous cube, angel beast, sea anemone, lizard warrior.
The single capitalised creature word in the batch is **Ｎｅｒｇａｌｉ**, which is a name, not a kind.

**Why not capitalise the coinages** (Killer Wolf, Gelatinous Cube, Grey Ooze)? Because the line
would then run between "coined in katakana" and "not", which puts サキュバス → Succubus and
バジリスク → Basilisk on the capitalised side and contradicts §4 and §14.3 directly. The species
test is the only line that leaves every prior decision standing.

### 17.2 Class and creature names first rendered here

| Japanese | English | Note |
|---|---|---|
| ホビット | hobbit | lowercase in prose (§17.1); `Ｈｏｂｂｉｔ　Ｖｉｌｌａｇｅ` in §2 is unaffected — that is a place name |
| ブラウニー | brownie | **promoted from §9 PROVISIONAL**, lowercase |
| 鬼 / 悪鬼 | ogre / fiend | **promoted from §9.** 悪鬼 is the 豚顔 one → *a pig‐faced fiend* |
| オーガ | ogre | same English as 鬼, deliberately — same creature, two source spellings, and only the weapon entry 192 uses the katakana |
| 巨人 | giant | **promoted from §9** |
| ダークエルフ / ダークメイジ / ダークナイト | dark elf / dark mage / dark knight | lowercase; 暗黒 → *dark* already fixed in §4 |
| 魔術戦士 | mage warrior | **kept distinct** from 魔法戦士 → *magic warrior* (§4), on the same 魔術 → mage / 魔法 → magic split the glossary already draws. 女魔術戦士 → *a female mage warrior* |
| 暗黒剣士 | dark swordsman | |
| サキュバス | succubus | |
| キラーウルフ | killer wolf | |
| スケルトン / レイス | skeleton / wraith | |
| 生霊 | the living spirit | the wraith's 異名 |
| ゴーレム | golem | |
| スライム / グレイウーズ / ゼラチナスキューブ / ローパー | slime / grey ooze / gelatinous cube / roper | four distinct classes; British *grey* |
| ドラゴン | dragon | 12 near-identical entries — see 17.5 |
| 竜人 | dragonfolk | same English as 龍人族 (§2); the kanji differ, the word does not |
| ネルガリ | Ｎｅｒｇａｌｉ | the dark elemental. A name, so capitalised. Alt **Ｎｅｒｇａｌ** (the Babylonian god the kana point at) — *Nergali* chosen as the plain transliteration; see FLAGS |
| エンゼルビースト | angel beast | the light elemental, and by the species test a kind, not a name — so lowercase where Ｎｅｒｇａｌｉ is not. Deliberate, not an oversight |
| トカゲ戦士 | lizard warrior | extends トカゲ → lizard (§2) |
| 王様トカゲ | king lizard | the basilisk's own entry |
| オリジナルＮ号機 | Ｏｒｉｇｉｎａｌ　Ｕｎｉｔ　Ｎ | the four unique machines, as against the 量産型 line |
| 機構車両 | vehicle | *mechanical* dropped for width — see FLAGS |

### 17.3 Weapons, and the names on them

| Japanese | English | Note |
|---|---|---|
| 妖刀 | “ｄｅｍｏｎ　ｂｌａｄｅ” | `「…」` → `“…”`, per the `『…』` precedent (§3) |
| 東洋の名刀 | a famed Eastern sword | |
| 神聖剣 / 神聖の名剣 / 神聖な弓 | holy sword / famed holy sword / holy bow | |
| 片刃の槍 | single‐edged spear | |
| 青龍 | blue dragon | lowercase — the scales of a kind of dragon, not a named individual |
| 水蛇 | sea snake | alt *water serpent*, which will not fit the row; see FLAGS |
| トクロフ | Ｔｏｋｒｏｆ | the tree the spear is cut from. Appears once in either dump. Alt *Tokurofu* |
| 魔神ルシファ | the demon god Ｌｕｃｉｆｅｒ | European form, matching Bauer / Carline / Helfer. Alt *Lucifa* |
| アポロン神 | the god Ａｐｏｌｌｏ | same rule |
| 女神アルテミス | the goddess Ａｒｔｅｍｉｓ | Ａｒｔｅｍｉｓ was already fixed in §1; this adds the epithet |
| こん棒 | club | |
| さく裂弾 / 火炎弾 | burst shells / flame shells | |

### 17.4 Fixed sentence frames

Identical Japanese must produce byte-identical English, and near-identical Japanese sitting side
by side in one table must not drift. Four frames carry most of the batch:

| Source shape | English frame |
|---|---|
| `Ｘが昇格したＹ` | **`Ａ　ｐｒｏｍｏｔｅｄ　Ｘ，　<Y>．`** — or `Ａ　Ｙ　ｐｒｏｍｏｔｅｄ　ｆｒｏｍ　ｔｈｅ　Ｘ．` where the row takes it. Both are in use; the short form is the default |
| `Ｘが進化したＹ` | **`Ａ　Ｙ　ｅｖｏｌｖｅｄ　ｆｒｏｍ　ｔｈｅ　Ｘ．`** |
| `Ｘの進化型` | **`Ａｎ　ｅｖｏｌｖｅｄ　Ｘ．`** (adjectival, as §4's *promoted* and *advanced* already are) |
| `〜のブレスを吐くドラゴン` | **`Ａ　ｄｒａｇｏｎ　ｂｒｅａｔｈｉｎｇ{FFFE}<element>．`** — all eight breath dragons, 強力な → *powerful*, 最強の → *the strongest* |

### 17.5 Register

There is none: this table is a reference list the player reads while choosing a class, so the
voice is the same flat catalogue voice as `batch_001` — noun phrase, one clause, full stop. The
only entries with any personality are the three unfinished dev slots (`自走砲１です！`), which
keep the `Ｔｈｉｓ　ｉｓ` frame of `ダミーぶきです` and their `！`.

---

## 18. Reviewer rulings — wave 1 (2026-09-08, reviewing PR #2, battle chunk 1)

Three cross-PR conflicts and two corrections to shipped work, settled together because battle
chunks 1, 2 and 3 were drafted in parallel and reached review before any of them merged. Recorded
here so the rulings bind the reviewers of PRs #3, #1 and #4, and every later unit.

### 18.1 The ノロ tic takes a space after the comma — `，　ｎｙｏｒｏ．`

**Ruling: §5 was wrong and is corrected.** The entry read `，ｎｙｏｒｏ．`; the correct form is
`，　ｎｙｏｒｏ．` with a full-width space. Three independent reasons, in order of weight:

1. **The font settles it.** `tools/riotfont.py` maps SJIS `0x8143` (`，`) through `SJIS_TO_ASCII`
   to the plain ASCII `,` of the 8×8 IBM VGA bitmap. Every permitted character renders as an
   8-pixel Latin glyph, so `，` is a Latin comma in an 8-pixel cell — it does **not** carry the
   built-in right-hand whitespace a real Japanese full-width comma has. Unspaced,
   `ｃａｍｅ，ｎｙｏｒｏ．` renders on screen as `came,nyoro.`.
2. **The corpus is unanimous.** Measured across every shipped file in `tl/`: a full-width comma is
   followed by a full-width space **153** times and by a tag **138** times. Before this ruling it
   was followed by a letter **exactly 10 times, all 10 of them the draft of chunk 1**. §5's
   spelling was the outlier in the corpus, not the drafts that spaced it.
3. **§5's own sibling entry is spaced.** The ゲロゲロ worked example in `translation_prompt.md` §5
   reads `ｎｏｔ　ｆｏｒｇｉｖｅｎ．　Ｒｉｂｂｉｔ！`.

**Lines this affects (§4.3).** The tic had not been rendered anywhere in `tl/` when this was
decided, so nothing shipped needs revisiting. Within wave 1: battle chunk 1 (PR #2) carried the
unspaced form ×10 and must change; battle chunk 2 (PR #3, ×2) and battle chunk 3 (PR #1, ×11)
already carry the spaced form and stand. Forward: about **70 further `ノロ` lines in
`script_unique.txt` and 7 more in `battle_dump.txt`** take the spaced form.

The respelling is a pure substitution — measured on chunk 1, the ten rows go 20→21, 21→22, 17→18,
19→20, 22→23, 20→21, 19→20, 19→20, 19→20, 15→16. **Widest 23, no re-flow, no page grows.** It
costs 2 bytes per instance.

### 18.2 `おお` → `Ｏｈ` plus the source's own punctuation

**Ruling: `Ｏｈ！`, not `Ｏｈｏ！`.** Chunk 1 argued that a fourth string on "Oh"/"Ah" flattens the
set; chunk 3 argued the punctuation keeps them apart. Chunk 3 is right, on the glossary's own
precedents:

- **§10.6 has already decided this exact question.** ほう / ほお was `Ｈｏｈ` and was resolved in
  favour of chunk 0's plain `Ｏｈ`; §10.6 records that **no `Ｈｏｈ` remains anywhere in `tl/`**.
  `Ｏｈｏ` is `Ｈｏｈ` reborn for the neighbouring interjection.
- **§5 states the mechanism that keeps them apart**: the *word* is fixed and the punctuation
  follows the source. So ほう / ほお → `Ｏｈ` (which always carries `．．．` or `，`),
  おや → `Ｏｈ？`, おお → `Ｏｈ！`, あ、 → `Ａｈ，` — four source strings, four distinct renderings,
  one word. That is the same deliberate collapse §6 already applies to ふっ / フンッ → `Ｈｍｐｈ`
  and §17.2 applies to 鬼 / オーガ → *ogre*.
- In English "Oho" carries a note of mock-triumph that a hobbit chief's warm greeting does not.

**Lines this affects.** One instance in battle chunk 1 (PR #2, must change), one in battle chunk 3
(PR #1, already `Ｏｈ！`, stands). Nothing shipped.

### 18.3 Two corrections to already-shipped `tl/battle/chunk_000.txt`

Both were raised by chunk 1's translator, who correctly did not touch files outside its unit
(CLAUDE.md §3). In both cases chunk 0 was the lone outlier against the glossary **and** against
other shipped work, so the fix is to chunk 0, not to the glossary. Applied in this commit.

| Line | Japanese | Was | Now | Cost |
|---|---|---|---|---|
| `chunk_000.txt` line 20 | `くっ・・・` | `Ｕｇｈ．．．` | **`Ｔｃｈ．．．`** (§11.5) | same 6 columns, 0 bytes |
| `chunk_000.txt` line 4 | `ああ。` | `Ｙｅｓ．` | **`Ｙｅａｈ．`** (§6) | 4 → 5 columns, +2 bytes |

The first was not merely a glossary divergence but a **CLAUDE.md §3 violation**: `chunk_007.txt`
line 12 already shipped `くっ・・・` → `Ｔｃｈ．．．`, so identical Japanese carried divergent
English across two shipped files. Fixing it also frees `Ｕｇｈ`, which chunks 1 and 2 both take for
**ううっ** — a different source string — so the form no longer does two jobs.

For the second, `Ｙｅａｈ` already stood in `tl/script/batch_002.tsv`. Note the widths are **not**
equal, as the PR assumed: `Ｙｅｓ．` is 4 columns and `Ｙｅａｈ．` is 5. It is a standalone row, so
nothing re-flows, but chunk 0 is the tightest file in the project and this spends 2 of its 29 spare
bytes: **8,163 → 8,165 / 8,192, slack 29 → 27.** `assemble.py check` passes. Chunk 0 has no room
left for another correction of this kind — the next one will need a re-cut.

### 18.4 `サイクス` → `Ｓｙｋｅｓ`

Reconciled between PRs #1 and #3 before review and verified in both pushed files. Promote out of
§9 PROVISIONAL when the first of those two merges. ✅ **Discharged 2026-09-08** — PR #3
(chunk 2) merged first, so the promotion is recorded in §20.1.

---

## 19. Added by chunk 001 (PR #2, merged 2026-09-08)

Rendered in `tl/battle/chunk_001.txt` — chapter 2: the hobbit village chief hires the 9th Army to
guard his food store, the party grumbles, an in-character tutorial on HP / villages / losing a
character, the pig-faced fiend boss, and the chief's thanks. 3,517 / 8,192 bytes, slack 4,675.

**This is the first chunk in which the `ノロ` tic is actually rendered.** §5 and §18.1 fix the form;
chunk 1 is where it first reaches `tl/`, ten times, in the spaced form `，　ｎｙｏｒｏ．` — and once
as `，　ｎｙｏｒｏ，` on `さっそくノロが、`, where the source clause ends in `、`. That is §5's stated
rule, not an exception, and it is the pattern every later `ノロ` line follows.

### 19.1 Tics and interjections

| Japanese | English | Note |
|---|---|---|
| ブヒ / ブヒィィィィ | `Ｏｉｎｋ` / `Ｏｉｎｋｋｋｋ` | **Promoted from §9 PROVISIONAL (wave-1 seeds).** The pig‐faced fiend's squeal, used with the source's own stop per the ゲロゲロ precedent (§5). The four `ィ` become four `ｋ` — kana beats tracked, as with フハハハ → Ｆｕｈａｈａｈａ (§11.5) |
| ううっ | `Ｕｇｈ` + the source's own punctuation | Groan of dismay. **Distinct** from くっ / クッ → `Ｔｃｈ` (§11.5) and from ぐふっ → `Ｇｕｆｆ` (§14.5). Free to take `Ｕｇｈ` only because §18.3 moved chunk 0's くっ to `Ｔｃｈ`; the form no longer does two jobs. Also in battle chunk 2 |
| それにしても | `Ｓｔｉｌｌ，` | Pivot to a new thought. Also in battle chunk 2, byte-identical |
| いやいや (before thanks) | `Ｗｅｌｌ　ｎｏｗ，` | The chief's opener at `いやいや、助かったノロ。` — deprecating warmth, **not** a refusal, so never “No, no” |
| そんなバカな | `Ｔｈａｔ’ｓ　ｉｍｐｏｓｓｉｂｌｅ` | Follows chunk 7's shipped `バ、バカな・・・` → `Ｉｍ，　Ｉｍｐｏｓｓｉｂｌｅ．．．`. Dot count follows the source |
| バカなやつら | `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ` | The other バカ — contemptuous plural address. **Distinct** from そんなバカな above; both are the fiend's in this chunk |
| たかが〜 | `Ｔｈｅｙ’ｒｅ　ｏｎｌｙ　．．．` | Dismissive. `たかがオーク。` → `Ｔｈｅｙ’ｒｅ　ｏｎｌｙ　ｏｒｃｓ．` |

### 19.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 謹慎処分を受ける / 謹慎中 | `ｃｏｎｆｉｎｅｄ` | The mages' squad leader struck a superior and is confined. Read as **singular** — the subject is 分隊長 — so `ｓｏ　ｈｅ’ｓ　ｃｏｎｆｉｎｅｄ．`. Recurs as 謹慎中 in battle chunk 3 (Shasta) |
| 上官 | superior officer | |
| 部隊 (魔術師の部隊) | squad | Matches 第３分隊 → 3rd Squad and 分隊長 → squad leader (§2); rendered `ａ　ｍａｇｅｓ’　ｓｑｕａｄ` |
| 作戦 (bare, “what's the plan?”) | `Ｔｈｅ　ｐｌａｎ？` | Kept **distinct** from 作戦会議 → war council (§2) |
| なぎ倒す | mow down | |
| キャラクター | character | Plain noun; no §17.1 species question arises |
| ＨＰ | `ＨＰ` | Left as the source's full-width caps — a genuine stat abbreviation the UI also shows. **Distinct from** ＨＩＴ → `ｈｉｔｓ` (§3), where the caps are only Japanese emphasis on a loanword |
| 「村」 / 「待機」 (map/menu labels) | `“Ｖｉｌｌａｇｅ”` / `“Ｗａｉｔ”` | `「…」` → `“…”` per the `『…』` precedent (§3, §15.1). Capitalised **in these two entries**; ⚠️ this is *not* a general rule for quoted tokens — the corpus holds both cases and the question is open, see `FLAGS.md` §I1. **Bare 村 in the same message stays lowercase `ｖｉｌｌａｇｅ`** — the source draws that distinction itself and the translation preserves it |

### 19.3 Register

| Who | Register |
|---|---|
| The hobbit village chief (portrait 0005) | Warm, fussy, grateful; the `ノロ` tic on every sentence. Deferential to the party without being servile |
| The 9th Army rank and file (portraits 0000–0002, 0004) | Grumbling and clipped; contractions throughout. The veteran (0001) is flat and unimpressed, the newcomer (0000) asks the questions, the anxious one (0004) carries `ううっ`, the sarcastic one (0002) gets `Ｑｕｉｔｅ　ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ．．．` |
| The pig‐faced fiend (portrait 0006) | Self-important and contemptuous, bracketed by `Ｏｉｎｋ`. `俺様` is flattened to `ｍｅ` for width — the swagger is carried by `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ．` and the squeal |
| The chunk 1 tutorial speaker (portrait 0003) | **Not** a §7 tutorial box. Its marker is `{=FA1000000000}`, not `{=FA1000300030}`, so it is a character explaining the rules: friendly and plain, light contractions, as §15.3's racetrack guide. The marker is what decides this |

---

## 20. Added by chunk 002 (PR #3, merged 2026-09-08)

Rendered in `tl/battle/chunk_002.txt` — chapter 3: Fernando's briefing on the south road, the 9th
Army's banter about army rankings, the cavalry and heavy-swordsman tactical boxes, the Melzario
hobbits' plea, and the Fernando/Albert coda, which exists as **two mutually exclusive variants**
(file lines 14 and 20). 5,839 / 8,192 bytes, slack 2,353.

### 20.1 People and places — four promotions out of §9

| Japanese | English | Note |
|---|---|---|
| アルベール | Ａｌｂｅｒｔ | **Promoted from §9 (wave-1 seeds).** Fernando's subordinate; deferential and formal, no contractions, answers `はっ！` → `Ｓｉｒ！`. 6 columns |
| サイクス | Ｓｙｋｅｓ | **Promoted from §9 PROVISIONAL** per §18.4 — chunk 2 is the first of PRs #1/#3 to merge, so the promotion lands here. 5 columns. Alt *Cyx* rejected |
| メルザリオ | Ｍｅｌｚａｒｉｏ | **Promoted from §9 PROVISIONAL, and §9's description corrected: it is a PLACE, not a person.** `息子がメルザリオに住んでる` (his son lives *in* Melzario) and `メルザリオの森` → `Ｍｅｌｚａｒｉｏ　ｆｏｒｅｓｔ` both settle it. 8 columns. Alt *Merzario* |
| 宮廷第２軍 / 宮廷２軍 | ２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ | **Promoted from §9 PROVISIONAL.** Both source spellings take one English form — they are the same unit spelled two ways nine segments apart. 16 columns, so it never shares a row with a verb |
| 村長 (ホビットの村の) | village chief | The hobbit village's head — the `ノロ` speaker of chunk 1. Kept **distinct** from 妖精の村の長 → village elder (§14.2) and 市長 → the mayor (§1); three different source words |
| 集落 | settlement | The northern hamlet the villagers come from. **Distinct** from 村 → village |
| 主力部隊 | ｔｈｅ　ｍａｉｎ　ｂｏｄｙ | Standard military English. Kept **distinct** from 本隊 → the main force (§2) and 精鋭部隊 → elite corps, on the principle those two already follow |

### 20.2 Classes

| Japanese | English | Note |
|---|---|---|
| 重剣士 | heavy swordsman / heavy swordsmen | Extends §4's 剣士 → swordsman. Lowercase in prose per the §17.1 species test. `ｈｅａｖｙ　ｓｗｏｒｄｓｍｅｎ` is 16 columns; the ≤ 20 class-table label form is still open (§10.2) |
| 騎兵 | cavalry | Bare form. Extends §4's 軽騎兵 → light cavalry |

### 20.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| ぬぬッ | **`Ｗｈｙ，`** | Fernando's grunt of indignant surprise. **Ruled 2026-09-08 (PR #3 round 1): `Ｗｈｙ，`, not `Ｇｒｒ，`** — the speaker is a blustering senior officer, so the word wanted is an officer's, not a growl, and English `Why，` carries exactly the affronted double-take of `ぬぬッ`. Held apart from all five fixed grunts: `Ｈｍｐｈ` (ムムッ/ふっ/フンッ), `Ｔｃｈ` (くっ), `Ｈｍ` (む/ん), `Ｏｈ` (ほう), `Ｏｈ？` (おや). Occurs twice, byte-identical in both coda variants |
| ん？ | `Ｈｍ？` | Same English as §6's む → `Ｈｍ`, **deliberately** — one short noticing grunt, two spellings, as 鬼 / オーガ → *ogre* already does (§17.2) |
| えーっ | `Ｅｈｈ，` | Drawn-out dismayed protest. Alt *Whaaat* |
| よいか、 | `Ｌｉｓｔｅｎ　ｗｅｌｌ，` | Fernando's stiffer form. Kept **distinct** from いいか、 → `Ｌｉｓｔｅｎ，` (`translation_prompt.md` §5 worked example) — different source strings, different register |
| わかっておるな！ | `Ｉｓ　ｔｈａｔ　ｃｌｅａｒ！` | **Distinct** from §6's わかったなっ！！ → `Ｇｏｔ　ｔｈａｔ！！` and いいな！！ → `Ｇｏｔ　ｉｔ！！`. §6 forbids reusing those for a different string; the `おる` form is a senior officer's, not a sergeant's bark |
| まったくだっ！ | `Ｉｎｄｅｅｄ　ｗｅ　ｈａｖｅ！` | Emphatic **agreement**, answering Albert. **Distinct** from §6's bare まったく → `Ｒｅａｌｌｙ，` (exasperation). The elided predicate is supplied per §2 |
| 当たり前だ！ / 当然だ！ / 当然だっ。 | `Ｏｆ　ｃｏｕｒｓｅ！` / `Ｎａｔｕｒａｌｌｙ！` / `Ｎａｔｕｒａｌｌｙ．` | Three source strings in one scene; the first two must not collapse. Punctuation follows the source |
| バカ者 (of a named officer) | `ｆｏｏｌ` — `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ，` | **A third バカ register.** Deliberately not chunk 1's そんなバカな → `Ｔｈａｔ’ｓ　ｉｍｐｏｓｓｉｂｌｅ` or バカなやつら → `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ` (§19.1) — different source strings, different speakers |
| ガセネタ | `ａ　ｆａｌｓｅ　ｌｅａｄ` | A bum steer. 12 columns, and it keeps the sense without importing an unrelated English idiom (§2). Alt *a false report* |
| 貧乏クジをひく | `ｄｒｅｗ　…　ａ　ｓｈｏｒｔ　ｓｔｒａｗ` | A genuine equivalent idiom — both are drawing the losing lot — not a substitution |
| カタがつく | `ｓｅｔｔｌｅ` — `ｈａｓ　ｓｅｔｔｌｅｄ　ｔｈｅｉｒｓ` | “Matters are concluded” |
| おいしい思いをする | `ｈａｖｅ　…　ｔｈｅ　ｓｐｏｉｌｓ` | To get the sweet part of it |
| 体中ドロだらけ | `ａｌｌ　ｍｕｄ，　ｈｅａｄ　ｔｏ　ｆｏｏｔ` | 体中 → *head to foot*, ドロだらけ → *all mud* |
| 敵を通してはならん | `ｌｅｔ　ｎｏ　ｅｎｅｍｙ　ｔｈｒｏｕｇｈ` | The literal “the enemy must not pass” is 25 columns; this is the ≤ 23 form |
| 救援に向かう / 救援に来る | `ｇｏ　ｔｏ　…　ａｉｄ` / `ｃｏｍｅ　ｔｏ　…　ａｉｄ` | **Distinct** from 援軍 → reinforcements / aid (§2). 救援 is the act of relieving, 援軍 the troops sent; §2's “use *aid* only where 24 columns will not take the full word” governs 援軍 only and does not apply here |

### 20.4 `帝国軍` — the two forms, and which is the default

§2 already reads `帝国軍` → *the Empire's men where 24 columns will not take “the Imperial army”*.
Chunk 2 is the first unit to make that choice with room to spare, so the rule is worth stating
plainly: **`ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` (21 columns) is the default and `ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ`
is the width fallback.** Chunk 2 uses the full form twice. Shipped `chunk_007.txt` uses the
fallback where the default would have fitted at 22 columns — recorded, **not** to be re-cut: that
file has 399 bytes of slack and the Japanese messages differ, so CLAUDE.md §3's identical-JP rule
is not engaged.

### 20.5 Register

| Who | Register |
|---|---|
| Fernando (portrait 0005) | Senior, stiff, self-important; **no contractions anywhere** — `Ｉ　ａｍ`, `ｗｅ　ａｒｅ`, `Ｉ　ｗｉｌｌ　ｎｏｔ`, `ａｒｅ　ｔｈｅｙ　ｎｏｔ`. Commands in the imperative (`ｈｏｌｄ　ｔｈｉｓ　ｒｏａｄ　ｔｏ　ｔｈｅ　ｄｅａｔｈ`), and his affront is `Ｗｈｙ，` |
| Albert (portrait 0006) | Deferential and formal, no contractions; reports rather than opines; `Ｓｉｒ！` |
| The 9th Army companions (portraits 0000–0003, 0009, 000A) | Casual, contractions throughout — the deliberate contrast that makes Fernando's flatness read as rank. Portrait 0009, the 重剣士, speaks with `僕` |
| The Melzario hobbits (portraits 0007, 000B) | 0007 carries the `ノロ` tic and the alarm; **0B is a second hobbit who does *not* use the tic** and speaks in plain polite Japanese (`お願いします`, `ありがとうございます`). Do not add the tic to 0B — the source withholds it |

---

## 21. Added by chunk 003 (PR #1, merged 2026-09-08)

Rendered in `tl/battle/chunk_003.txt` — chapter 4: Shasta rejoins the 9th Army from confinement
at Marvel's side, Sykes recognises him, the Melzario hobbits under Fiber attach themselves to the
squad, Korneff the explorer hands over a present, and the village sees the party off.
4,601 / 8,192 bytes, slack 3,591. **Eleven `ノロ` instances — the largest concentration shipped.**

### 21.1 People and places — five promotions out of §9 (wave-1 seeds)

| Japanese | English | Note |
|---|---|---|
| シャスタ | Ｓｈａｓｔａ | **Promoted from §9.** The 9th Army member confined for striking a superior (chunk 1), released here. **Male**, self-references with `僕`; casual, contractions. 7 columns |
| マーベル | Ｍａｒｖｅｌ | **Promoted from §9.** A **person** — the woman Shasta escorts. Formal, no contractions. 6 columns |
| マーベラス | Ｍａｒｖｅｌｌｏｕｓ | **Promoted from §9.** A **town** — Korneff's house is there. Deliberately kept visibly distinct from Ｍａｒｖｅｌ the person; both occur in this one chunk. 11 columns |
| ファイバー | Ｆｉｂｅｒ | **Promoted from §9.** The Melzario hobbit who leads the group that joins the squad. `ファイバーたち` → `Ｆｉｂｅｒ　ａｎｄ　ｔｈｅ　ｏｔｈｅｒｓ`. 5 columns |
| コーネフ | Ｋｏｒｎｅｆｆ | **Promoted from §9.** The 探検家 with a house in Marvellous. 7 columns |
| 探検家 | explorer | **Promoted from §9.** Lowercase — a trade, per the §17.1 species test. Kept **distinct** from 冒険者 → adventurer (`script_unique` 1001); the same man, two different source words, deliberately not merged |

### 21.2 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| げっ | `Ｇａｈ，` | Dismayed recoil. **Distinct** from グッ → `Ｇｕｈ`, ぐわっ → `Ｇｗａｈ` (§11.5) and ぐふっ → `Ｇｕｆｆ` (§14.5) |
| えっ？ | `Ｅｈ？` | Short startled query. Same family as chunk 2's えーっ → `Ｅｈｈ，` (§20.3); the length tracks the source |
| あれ・・・？ | `Ｗｈａｔ．．．？` | Puzzled double-take. **Distinct** from 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6) — that one is incredulous, this one is merely confused |
| わかりました。 | `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` | Polite assent. **A fourth member of the わかる family, all held apart**: いいな！！ → `Ｇｏｔ　ｉｔ！！`, わかったなっ！！ → `Ｇｏｔ　ｔｈａｔ！！`, 分かった → `Ｒｉｇｈｔ，` (§6), わかっておるな！ → `Ｉｓ　ｔｈａｔ　ｃｌｅａｒ！` (§20.3) |
| 了解ノロ！ | `Ｕｎｄｅｒｓｔｏｏｄ，　ｎｙｏｒｏ！` | 了解 → `Ｕｎｄｅｒｓｔｏｏｄ`, a fifth and distinct form |
| よろしく / よろしくね | `Ｇｏｏｄ　ｔｏ　ｍｅｅｔ　ｙｏｕ` | On first introduction. Rendered identically in both halves of the exchange so the greeting reads as one returned |
| よろしくお願いします | `Ｉ　ａｍ　ｉｎ　ｙｏｕｒ　ｈａｎｄｓ` | The formal request form — **distinct** from the greeting above, which is the same words doing a different job |
| 物好き | `ｏｄｄ　ｓｏｒｔｓ` | Korneff on the Royal Army. Used twice in two sentences and identical in both |
| 〜さん (on a personal name) | **dropped; carried in register** | `シャスタさん` → `Ｓｈａｓｔａ`, `マーベルさん` → `Ｍａｒｖｅｌ`. §2's rule for politeness levels with no English lexical equivalent: carry it in word choice, not in added words. Marvel's deference is in `Ｉ　ａｍ`, `Ｉ　ｄｏ　ｎｏｔ`, `Ｉ　ａｍ　ｉｎ　ｙｏｕｒ　ｈａｎｄｓ`. **Does not affect** トカゲさん → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ` (§2), which is a comic address to an animal, not a name |

### 21.3 The stolen-item message — one rendering binds seven instances

| Japanese | English |
|---|---|
| `アイテムを{FFFE}奪われました。` | **`Ａｎ　ｉｔｅｍ　ｗａｓ{FFFE}ｓｔｏｌｅｎ　ｆｒｏｍ　ｙｏｕ．`** |

Recurs **byte-identically seven times across chunks 3, 9 (×3), 28, 29 and 30** — counted in
`battle_dump.txt`, not taken from a report. Merging chunk 3 fixes all seven. Its marker is
`{=FA1000300030}`, the personality-free tutorial box of §7, so the register is plain instructional
second person and the English keeps the source's passive. Rows measure 17 and 20 columns, leaving
room in every chunk that inherits it. **Copy it; do not re-invent it.**

### 21.4 Register

| Who | Register |
|---|---|
| Shasta (portrait 0003) | Easy and apologetic; contractions throughout (`Ｉ’ｍ`, `ｃｏｕｌｄｎ’ｔ`, `ｙｏｕ’ｒｅ`). Self-references with `僕`. The one who cannot refuse a girl's request |
| Marvel (portrait 0004) | Formal and grateful, **no contractions** — `Ｉ　ａｍ`, `Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ`. The `さん` she attaches to every name is carried here, not transliterated |
| Sykes (portrait 0001) | Blunt and needling, like Ridge (§7): `Ｋｎｏｗ　ｈｉｍ？　Ｏｆ　ｃｏｕｒｓｅ．`, `Ｉｓｎ’ｔ　ｔｈａｔ　Ｓｈａｓｔａ．` |
| Korneff (portrait 0006) | Rough, warm, self-amused; contractions. Approves of “odd sorts” |
| The Melzario hobbits (portraits 0007, 0008) | The `ノロ` tic on every sentence, grateful and eager |
| Portrait 0002 | An **unnamed female** party member (`わ`) who also carries the map tutorial. If a later chunk names her, re-check her register — cf. §10.11, §13.13, FLAGS §G4 / §H1 |

---

## 22. Added by script batch 004 (PR #4, merged 2026-09-08)

Rendered in `tl/script/batch_004.tsv` — `script_unique.txt` lines 142–184: the sword and spear
entries of the equipment description table, every line ending `攻撃力＋ＮＮ` with no
`ジェムタイプ` suffix. 34 unique lines × 21 instances = **714 message instances**. The vocabulary
sits in §4 and §17.3; this section carries what is new.

**All four wave-1 script seeds promoted, used exactly as seeded.**

### 22.1 Gods, materials and weapon words first rendered here

| Japanese | English | Note |
|---|---|---|
| 魔神ティール | the demon god Ｔｙｒ | **Promoted from §9.** Follows the pantheon pattern of §17.3 (`魔神ルシファ` → *the demon god Ｌｕｃｉｆｅｒ*, `アポロン神` → *the god Ａｐｏｌｌｏ*). Ｔｙｒ is the Norse reading the surrounding pantheon points at. Alt *Tiel*, *Thiel* |
| 軍神オーディン | the war god Ｏｄｉｎ | **Promoted from §9.** Same pattern |
| 雷神 | the thunder god | **Promoted from §9.** Six entries — `雷神の雷` → *the thunder god’s bolt*, `雷神の電磁場` → *the thunder god’s field*. Identical in all six |
| 守護をもたらす | **`〜‐ｗａｒｄｉｎｇ`** | **Promoted from §9.** `持つ者に炎の守護をもたらす剣` → `Ａ　ｆｉｒｅ‐ｗａｒｄｉｎｇ　ｓｗｏｒｄ．` **Six entries, byte-identical in all six** as the seed required. ⚠️ `持つ者に` (“to the one who bears it”) is dropped — a §2.1 step 5 implication, accepted under bank 40's ceiling; see `FLAGS.md` §J1 |
| 冷気の剣 | a cold sword | `触れる者を凍らせる` → *freezing at a touch* |
| 火炎剣 | flame sword | `すべてを焼き尽くす` → *burning all up* |
| 電気の剣 / 電気の槍 | (rendered through the 雷神 clause) | The `電気` is carried by the thunder god's bolt/field rather than stated twice |
| 暗黒剣 / 暗黒の剣 / 暗黒の槍 | dark sword / dark spear | Consistent with 暗黒 → *dark* (§4) and 暗黒剣士 → *dark swordsman* (§17.2) |
| 闇の力 | shadow power | Kept **distinct** from 暗黒 → *dark*; both occur in one entry (`闇の力を秘めた暗黒の剣` → `Ａ　ｄａｒｋ　ｓｗｏｒｄ　ｈｉｄｉｎｇ　ｓｈａｄｏｗ　ｐｏｗｅｒ．`) and collapsing them would lose the distinction the source draws |
| 漆黒 | jet‐black | Distinct from both of the above. Uses ‐ (U+2010) |
| 黒騎士たち | black knights | Lowercase, per the §17.1 species test and matching `batch_003`'s shipped `暗黒騎士` → *dark knight’s*. **A different string** from §14.2's named order 黒の騎士団 → `Ｂｌａｃｋ　Ｋｎｉｇｈｔｓ`, which is unaffected |
| 名槍 | a famed spear | Extends §17.3's 東洋の名刀 → *a famed Eastern sword* |
| 伝説の名刀 | a legendary blade | `名` is absorbed into `伝説の` — *a legendary famed blade* is redundant in English (§2.1 step 3). The `名` survives wherever no competing adjective displaces it, as in 名槍 above |
| 三つ又の槍 | three‐pronged spear | Uses ‐ (U+2010) |
| 石に変える | turning foes to stone | Cf. 石化能力 → petrifying power / petrification (§4) |
| 月光 | moonlight | `神聖なる月光の光に守られた` → *guarded by holy moonlight* |
| 流星のごとくなぎ倒す | felling foes like meteors | なぎ倒す → *fell* here where §19.2 has *mow down*; the simile takes the shorter verb |

### 22.2 The frame this batch runs on

Every entry is **`Ａ　<adjective> <weapon> <participial clause>．{FFFE}Ａｔｋ＋ＮＮ`** — one noun
phrase, one clause, a full stop, then the stat row. It is the same flat catalogue voice as
`batch_001` and `batch_003` (§17.5), and every entry holds to **at most 2 description rows plus
the `Ａｔｋ` row**, so this batch adds none of the four-row entries glossary §10.3 flags in
`batch_001`.

---

## 23. Added by chunk 004 (PR #6, merged 2026-09-08)

Rendered in `tl/battle/chunk_004.txt` — chapter 5's lead-in, five scenes: the 9th Army grumbling
about being disbanded (Timmy, Ridge); a dragon attack on a girl who screams for help; her rescue
and her exit south toward the fairy forest; the enemy girl sent after the ring, and her death; and
a coda in which a watcher weighs whether to keep tailing the squad. 3,849 / 8,192 bytes, slack
4,343 — **the tag stream is byte-identical to the dump on all 25 lines, including every `{FFFE}`**,
the first unit in the project to ship with zero re-flow.

`ティミー` → `Ｔｉｍｍｙ` (§11.1) and `リッジ` → `Ｒｉｄｇｅ` (§1) are used unchanged; the stale §9
`ティミー` row is struck in this commit.

### 23.1 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 辺境 | ｆｒｏｎｔｉｅｒ | **Ruled 2026-09-08, PR #6 review.** Three occurrences here (`辺境の警備にきてる`, `辺境の警備兵`, `こんな辺境で`), one word in all three. ⚠️ Shipped `chunk_000.txt` line 4 renders the *phrase* `こんな辺境` — **twice** — as `ｓｕｃｈ　ａ　ｒｅｍｏｔｅ　ｐｌａｃｅ`. That is **recorded, not re-cut**, on the §20.4 precedent exactly: the Japanese *messages* differ, so CLAUDE.md §3's identical-JP rule is not engaged. Two further reasons the re-cut would be wrong rather than merely unnecessary — **no single word serves both** (`辺境の警備兵` cannot become *remote-place guards*, so "one word project-wide" could only mean editing chunk 0), and chunk 0 has **27 bytes of slack** (`FLAGS.md` §G1) with §18.3 recording that the next correction there needs a full re-cut |
| 警備兵 | ｇｕａｒｄｓ | `辺境の警備兵` → `Ｆｒｏｎｔｉｅｒ　ｇｕａｒｄｓ`. Kept **distinct** from §2's 守備兵 → garrison / garrison men — different source word, and the contempt in `なんて` wants the plainer noun |
| ガラクタ (as an insult) | ｊｕｎｋ | `ガラクタ部隊` → `ｊｕｎｋ　ｓｑｕａｄ`. A **fourth** contempt word, held apart from ゴミ → rubbish (§14.4), 雑草ども → weeds (§11.5) and 穀潰し → freeloaders (§2) |
| 解隊 | ｄｉｓｂａｎｄ | 4 occurrences, one word in all four |
| 気が早い | ｒｕｓｈ　ａｈｅａｄ | `気が早いな、ティミーは。` → `ｙｏｕ　ｒｕｓｈ　ａｈｅａｄ，　Ｔｉｍｍｙ．` |
| 群れ (of dragons) | ｈｏｒｄｅ | *Flock* rejected (bird-like), *swarm* rejected (insect-like) |
| 見殺しにする | ｌｅｔ　(someone)　ｄｉｅ | `見殺しにするつもり！？` → `Ｗｉｌｌ　ｙｏｕ　ｌｅｔ　ｈｅｒ　ｄｉｅ！？` |
| ボロを出す | ｓｌｉｐ　ｕｐ | |
| 食いっぱぐれる | ｇｏ　ｈｕｎｇｒｙ | He loses his meal ticket, not one meal |
| なかなかどうして | `Ｂｕｔ　ｗｈａｔ　ｄｏ　ｙｏｕ　ｋｎｏｗ，` | The "better than I was told" pivot, not a plain *quite* |
| 私の相手じゃない | ｂｅｎｅａｔｈ　ｍｅ | 私の相手 is *worth my time*; `ｎｏ　ｍａｔｃｈ　ｆｏｒ　ｍｅ` will not share the row with the `けど` clause |
| きっての | the superlative — `〜’ｓ　ｗｏｒｓｔ` / `〜’ｓ　ｆｉｎｅｓｔ`, polarity from the noun | `宮廷軍きってのガラクタ部隊` → `Ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ’ｓ　ｗｏｒｓｔ　ｊｕｎｋ　ｓｑｕａｄ`. Recurs on Ridge in chunk 6 (`カーラインきっての弓使い`), where the noun is complimentary |

### 23.2 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| あーあ | `Ａａｈ，` | Dejected sigh, twice in this chunk, byte-identical in both. **Distinct** from あ、 → `Ａｈ，`, ほう → `Ｏｈ`, おお → `Ｏｈ！`, おや → `Ｏｈ？` (§6, §18.2). The doubled `ａ` tracks the long vowel, as §11.5 tracks laugh beats |
| そうそう。 | `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` | Casual agreement. ⚠️ **`pending/chunk_005.txt` line 32 renders the byte-identical `そうそう。` as `Ｑｕｉｔｅ　ｓｏ．`** — verified. Accepted at review because `pending/` does not ship and the speaker here is Ridge, whose §7 register has no *Quite so*. **But chunk 4 has now shipped, so this form binds**: chunk 5's re-cut must adopt it or it *creates* a §3 violation the day the slot patch lands. Measured for that re-cut: 9 → 13 columns, **+8 bytes** |
| 何だ！？ | `Ｗｈａｔ　ｉｓ　ｉｔ！？` | A fifth member of the 何 family, all held apart: 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2), and chunk 0's shipped `な、何事だ！？` → `Ｗｈ‐ｗｈａｔ　ｉｓ　ｔｈｉｓ！？` and `こ、今度は何だ！？` → `Ｎ‐ｎｏｗ　ｗｈａｔ！？` (both carry the source's stutter) |
| 気にしない、気にしない。 | `Ｎｅｖｅｒ　ｍｉｎｄ，　ｎｅｖｅｒ　ｍｉｎｄ．` | The source's doubling is kept; 23 columns exactly. Same treatment as `早く、早く！！` → `Ｑｕｉｃｋ，　ｑｕｉｃｋ！！` in this chunk |
| 〜って (quotative, echoing back) | the echoed clause in `“　”` | `どうする？って` → `“Ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ？”`. The quotes carry the particle; `“ ”` is §3.1-legal and already the `『…』` form (§3) |

### 23.3 Ruling — `しかし` → `Ｈｏｗｅｖｅｒ，`

**Chunk 4 carries zero `しかし`.** This is ruled here so PRs #7 and #5 inherit a decision instead of
each inventing one, exactly as §18 bound wave 1's later reviewers.

| Japanese | English | Status |
|---|---|---|
| でも | `Ｂｕｔ，` | shipped — `chunk_007` line 19, and chunk 4 line 10. `Ｂｕｔ` is taken |
| それにしても | `Ｓｔｉｌｌ，` | fixed at §19.1; shipped `chunk_001` ×2, `chunk_002` ×1. `Ｓｔｉｌｌ` is taken |
| **しかし / しかしながら** | **`Ｈｏｗｅｖｅｒ，`** | **new, this ruling** |

Every collapse the glossary already records — ふっ/フンッ → `Ｈｍｐｈ`, 鬼/オーガ → *ogre*,
む/ん → `Ｈｍ` — is a **same-meaning, different-spelling** pair. `しかし` (plain adversative) and
`それにしても` (§19.1's own gloss: "pivot to a new thought") are **different connectives**, so
collapsing them is not that move and must not be recorded as one. `Ｈｏｗｅｖｅｒ，` is free and
suits the corpus, which skews formal: `しかし、残念ながら、` (ch.6), `しかしながら、` (ch.9 — the
explicitly formal variant), `しかし、リムル様・・・` (ch.30). **`しかしながら` takes the same
English** — *that* one is a same-meaning collapse of the documented kind.

**Lines this affects (§4.3).** One: **`tl/battle/chunk_003.txt` line 5**,
`しかし、敵は` → `Ｓｔｉｌｌ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` must become
`Ｈｏｗｅｖｅｒ，　ｔｈｅ　ｅｎｅｍｙ　ｉｓ` — measured **19 → 21 columns, +4 bytes**, chunk 3 slack
3,591 → 3,587. Not applied at review: `HANDOFF.md` queues `chunk_003:5` in the wave-3
`corrections/audit-wave1` unit, and the reviewer's remit is this file, `FLAGS.md`,
`pending/README.md` and `HANDOFF.md` — not `tl/`.

**Chunk 0's `はっ、しかし・・・` → `Ｓｉｒ，　ｂｕｔ．．．` is NOT an outlier and is not to be touched.**
It is a phrase-level rendering of a subordinate's interrupted protest, not a lexical choice about
`しかし` — the same distinction §20.4 draws, and the same one that leaves chunk 0's `こんな辺境`
alone in §23.1. Chunk 0's 27 bytes stay put.

### 23.4 Ruling — the `助かった` family

| Japanese | English | Note |
|---|---|---|
| 助かった (of one's own condition) | `Ｉ　ａｍ　ｓａｖｅｄ` / `Ｗｅ　ａｒｅ　ｓａｖｅｄ` | **The default.** `ありがとう、助かったわ。` → `Ｔｈａｎｋ　ｙｏｕ，　Ｉ　ａｍ　ｓａｖｅｄ．` (chunk 4), `助かったノロ、` → `Ｗｅ　ａｒｅ　ｓａｖｅｄ，　ｎｙｏｒｏ，` (chunk 3, shipped) |
| 助かった (turning to address the rescuer) | `Ｙｏｕ　ｓａｖｅｄ　…` | **Only where the source turns.** `助かったぜ、あんちゃん！` → `Ｙｏｕ　ｓａｖｅｄ　ｍｅ，　ｌａｄ！` (chunk 12, shipped) — the vocative `あんちゃん` plus `ぜ` is what licenses the active |

Every source string in the family genuinely differs, so CLAUDE.md §3 is not engaged and nothing
was forced. The rule exists because the family is about to spread (chunks 1, 3, 8, 12, 15, 23, 43).

⚠️ **One shipped line is already the wrong side of it, and neither wave-1 audit caught it.**
`tl/battle/chunk_001.txt` line 14 renders `いやいや、助かったノロ。` as
`ｙｏｕ　ｓａｖｅｄ　ｕｓ，　ｎｙｏｒｏ．` — active, with no vocative and no second-person address in
the source, while `chunk_003.txt` line 7 renders the near-identical `助かったノロ、` as
`Ｗｅ　ａｒｅ　ｓａｖｅｄ，　ｎｙｏｒｏ，`. Two hobbits thanking the party, in strings that differ only
in their final mark — and §5's mechanism says the stop is the *only* thing that should differ.
Correction: `ｗｅ　ａｒｅ　ｓａｖｅｄ，　ｎｙｏｒｏ．`, measured **20 → 20 columns, 0 bytes**. Added to
the wave-3 corrections unit; not applied at review, same reason as §23.3.

### 23.5 Register

| Who | Register |
|---|---|
| Timmy (portrait 0007) | Young and complaining; contractions, `Ａａｈ，`, open questions rather than statements |
| Ridge (portrait 0006) | §7 unchanged — blunt, needling, casual. Chunk 4 is his fullest scene so far and confirms it: `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`, `ｔｈｅｎ　ｓｏ　ｂｅ　ｉｔ．`, `Ｌｅｔ’ｓ　ｔａｋｅ　ｉｔ　ｅａｓｙ．` |
| The rescued girl (portrait 0004, unnamed) | Warm, direct, **no contractions** — written to §14.6's Cavia register across all 13 of her segments, which is also the safe reading if she is someone else. Nothing names her, so **no entry is proposed**; see `FLAGS.md` §K3 |
| The enemy girl (portrait 0005, unnamed) | Smug and bored; contractions (`Ｉ’ｌｌ`), contempt carried by `ｂｅｎｅａｔｈ　ｍｅ` and `Ｗｅａｋ，　ｙｅｔ　ｓｕｃｈ　ａｉｒｓ．`. Her `姉さん` is read as a literal sister — she cries it again as she dies — and rendered `Ｍｙ　ｓｉｓｔｅｒ` / `Ｓｉｓｔｅｒ，` |
| The line-21 watcher (portrait 0006) | Rough and self-amused. **Portrait 06 is Ridge's** — same id as line 3, differing only in the channel byte — and that agrees with §9's wave-2 seed, in which `リオン`/`Ｌｅｏｎ` sent Ridge and wants to stay anonymous. The English commits to neither reading; see `FLAGS.md` §K4 |

---

## 24. Added by chunk 006 (PR #7, merged 2026-09-08)

Rendered in `tl/battle/chunk_006.txt` — chapter 5 proper, five scenes: the orcs at Bernard's
church; Ridge attaching himself to the squad at Leon's request; Cavia reaching the church only to
learn Nacol has been moved to Capella; Fernando arriving to take her home, and her flight with the
9th Army; and the Black Knights overhearing where she is bound and carrying it to Kazarov.
5,899 / 8,192 bytes, slack 2,293 — 151 rows, widest 23, none at 24. Merged at round 2.

`しかし、残念ながら、` → `Ｈｏｗｅｖｅｒ，` is the first use of §23.3, and
`カーラインきっての弓使い` → `Ｃａｒｌｉｎｅ’ｓ　ｆｉｎｅｓｔ　ｂｏｗｍａｎ` the first use of §23.1's
`きっての`, exactly as that entry anticipated for this chunk.

### 24.1 People and places — five promotions out of §9 (wave-2 seeds)

`リオン` → `Ｌｅｏｎ` is promoted to **§1**, not here, because it replaces that table's stale
placeholder row and discharges §10.1.

| Japanese | English | Note |
|---|---|---|
| カペラ / カペラの村 | Ｃａｐｅｌｌａ / Ｃａｐｅｌｌａ　ｖｉｌｌａｇｅ | **Promoted from §9.** The village south of Farina where Nacol is convalescing. 8 columns. Alt *Kapera* rejected — Capella is a star name and reads as European |
| カザロフ | Ｋａｚａｒｏｖ | **Promoted from §9.** `カザロフ隊長` → `Ｃａｐｔａｉｎ　Ｋａｚａｒｏｖ`, the Imperial officer the Black Knights report to. 8 columns; 隊長 → captain per §2 |
| マーティン | Ｍａｒｔｉｎ | **Promoted from §9.** A Black Knight, ordered to pull back beside Percival. 6 columns |
| パーシバル | Ｐｅｒｃｉｖａｌ | **Promoted from §9.** The other Black Knight. 9 columns |
| 神父様 (vocative) | Ｆａｔｈｅｒ！ | Cavia calling into the church. Follows ナコール様 → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` below; §1's bare 神父 → *priest* is unchanged and still the noun form |
| ナコール様 | Ｆａｔｈｅｒ　Ｎａｃｏｌ | **Ruled 2026-09-08, PR #7 review.** 12 columns. 様 rendered as the English title of the man's station, exactly as 様 → **Lady** / **Lord** already does (リムル様, ヘルファー様, フィリス様, キャビア様 — §1, §14.1). `Ｌｏｒｄ　Ｎａｃｏｌ` is wrong in English for a cleric, and this chunk establishes the station: `先代の神父様です`. **The source's own split is preserved** — the priest and a 9th Army member say ナコール様 (→ `Ｆａｔｈｅｒ　Ｎａｃｏｌ`), Cavia says the bare ナコール (→ `Ｎａｃｏｌ`), which is also what shipped `chunk_007.txt` has from her. ⚠️ This is a **様** entry and stays clear of §21.2's `〜さん` rule, which drops the honorific — the two patterns are separate and must not be merged |

### 24.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 弓使い | ｂｏｗｍａｎ | **Promoted from §9, taking the seed's own alternative rather than its proposal.** Ratified at review. `archer` is already spent on 弓兵, and 弓の戦士 → *bow warrior* (§4); reusing it would collapse three source words into two, against the practice of §17.2 and §20.3. The §17.1 species test splits them: 弓兵 names *what a unit is*, a class label in the roster, while both occurrences here are an epithet on a named individual (`王国一の弓使い` is Ridge's own boast, `カーラインきっての弓使い` is Sykes recalling his renown). Width does not decide it — both are 6 columns. §14.3's 使い → *tamer* does not apply (creature handlers only) |
| 王国一の | Ｋｉｎｇｄｏｍ’ｓ　ｂｅｓｔ | Ridge's boast, 22 columns with `ｂｏｗｍａｎ，`. **Kept distinct from §23.1's きっての → `〜’ｓ　ｆｉｎｅｓｔ`**, which renders `カーラインきっての` in the very same chunk. Two source superlatives, two English superlatives, both on `ｂｏｗｍａｎ`; collapsing them would lose a distinction the source draws nine segments apart |
| おっさん | ｇｅｅｚｅｒ | 6 columns. Mildly dismissive “middle-aged bloke”. Twice, byte-identical: `匿名希望のリオンっておっさん` and `サイクスのおっさんか。` |
| 先代の神父 | ｍｙ　ｐｒｅｄｅｃｅｓｓｏｒ | 21 columns. The current priest on Nacol. 先代 is “the previous holder of this office”; the office was named one row earlier, so restating 神父 is the redundancy §2.1 step 3 covers |
| 世話役 | ｔｈｅ　ｏｎｅ　ｗｈｏ　ｃａｒｅｄ　ｆｏｒ　ｈｅｒ | Nacol's role to the child Cavia. Kept **distinct** from 嘘ツキ先生 → *the lying teacher* (§14.4) — same man, different source word |
| 恥さらしの (attributive) | ｓｈａｍｅｆｕｌ | 8 columns. **Does not change** §15.2's 恥さらし → `ａ　ｄｉｓｇｒａｃｅ`, which renders the bare noun standing alone as a fragment. Two forms of one word, as 石化能力 → *petrifying power* / *petrification* already is (§4). `ｄｉｓｇｒａｃｅｆｕｌ` is 12 and will not share the row with `Ｔｈｅ` and `９ｔｈ` |
| 札付きの悪党 | ｍａｒｋｅｄ　ｖｉｌｌａｉｎｓ | 札付き is literally “with a tag on it” — *marked* keeps the image where *notorious* (10 columns) does not fit the row |
| 無鉄砲な | ｒａｓｈ | 4 columns. `ｒｅｃｋｌｅｓｓ` (8) puts the row at 26 beside `Ｐｒｉｎｃｅｓｓ` |
| 増援 | ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ | Tutorial box, `敵の増援が　現れました。` **A different source word from 援軍** (§2) and from 救援 (§20.3); §2's “use *aid* only where 24 columns will not take the full word” governs 援軍 and does not reach here. A second row was the cheaper fix than a shorter word |
| 報奨金 | ｒｅｗａｒｄ | **Promoted from §9** — rendered here (`報奨金　どかーんがぁ・・`) before script 991 reached a batch |
| ヤバい (mild) | ｄｉｃｅｙ | Ridge on the Black Knights, `ちょっとヤバいぜ` → `ｉｓ　ａ　ｂｉｔ　ｄｉｃｅｙ` |
| とてつもなくヤバい | ｔｒｕｌｙ　ａｗｆｕｌ | The same adjective under a different intensifier, on a different speaker. Deliberately not collapsed with *dicey* — the source escalates and the English follows |

### 24.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| よし、 | Ｒｉｇｈｔ， | ⚠️ **Fixed here 2026-09-08 (PR #7 review) — it had never been in this glossary despite six shipped rows.** Byte-identical in `chunk_010` L14, `chunk_011` L9/L10/L11 and twice in chunk 6. Shares its English with §6's 分かった → `Ｒｉｇｈｔ，`, deliberately, on the ふっ/フンッ → `Ｈｍｐｈ` principle. See §24.5 for chunk 0's variant, which is a **different row** and is not re-cut |
| くくく | Ｋｕｋｕｋｕ， | Three kana beats → three `ku`, per §14.5's クックックッ → `Ｋｕｋｕｋｕ`. Same laugh, hiragana spelling; one English form, as 鬼 / オーガ → *ogre* already does (§17.2) |
| あ〜ん | Ａａａｈ， | The drawn-out wail of a man watching his reward evaporate. The `〜` lengthener becomes a repeated vowel, per the kana-beat convention (§11.5, §14.5). **Distinct** from §23.2's あーあ → `Ａａｈ，` and §6's あ、 → `Ａｈ，` — three source strings, three lengths |
| ちょっと、(protest) | Ｈｏｌｄ　ｏｎ， | An interruption. Kept **distinct** from this chunk's own すいません。 → `Ｅｘｃｕｓｅ　ｍｅ．` — two source strings, one an interruption and one an apology |
| ・・・聞いたな？ | ．．．Ｙｏｕ　ｈｅａｒｄ　ｔｈａｔ？ | **Distinct** from §6's 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` and §21.2's あれ・・・？ → `Ｗｈａｔ．．．？` |
| ま、待て！ | Ｗ，　Ｗａｉｔ！ | 8 columns. **Ruled 2026-09-08, PR #7 review.** The comma form, following shipped `chunk_007`'s `バ、バカな・・・` → `Ｉｍ，　Ｉｍｐｏｓｓｉｂｌｅ．．．` (§19.1). ⚠️ `pending/chunk_043.txt` line 14 renders the byte-identical string as `Ｗ‐ｗａｉｔ！`; it is parked, so §3 is not engaged today, and the re-cut is queued in `pending/README.md`. Chunk 0's `な、何事だ！？` → `Ｗｈ‐ｗｈａｔ　ｉｓ　ｔｈｉｓ！？` (§23.2) is a **different source string** and stays as it is |
| しかたねえ。 | Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ． | Twice here, byte-identical. **The same words as `pending/chunk_005`'s 仕方ない、 → `Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ，`** — which chunk 6 also carries, byte-identical — with the stop following the source, `．` against `，`. That is §5's stated mechanism for a fixed form under punctuation that is not its own, not a divergence |

### 24.4 Ruling — §18.2's four-way punctuation split does not hold, and `おお、` collides with `ほう、`

**§18.2 is corrected. It is right about the word and wrong about the mechanism.**

§18.2 records that four source strings are held apart “by their punctuation, not by four different
words”: ほう / ほお → `Ｏｈ` (with `．．．` or `，`), おや → `Ｏｈ？`, **おお → `Ｏｈ！`**,
あ、 → `Ａｈ，`. Counted across both dumps at this review, that is not what the corpus contains:

| Source | battle | script | total | Takes |
|---|---|---|---|---|
| `おお、` | 6 | 34 | **40** | `Ｏｈ，` |
| `おお！` | 3 | 4 | 7 | `Ｏｈ！` |
| `ほう、` / `ほお、` | 3 | 2 | **5** | `Ｏｈ，` |
| `おや` | 6 ⚠️ **4** | 23 | 29 | `Ｏｈ？` |

⚠️ **CORRECTION to this table's `おや` battle figure, 2026-09-09 (§4.3, PR #17 review) — see §35.3.**
**6 is the substring count; the interjection census is 4**, in chunks 1, 2, 31 and 35. The two false
positives are `おやさしい方です。` (chunk 7 message line 19 — the very line that carries
`あら・・・・？`) and `おやすいご用です。` (chunk 23). **Nothing turns on it**: `Ｏｈ？` is spent for
おや either way, which is the only load this row bears, and the ruling below is untouched.
**Lines this affects: none.**

**`おお、` is the majority form of おお by 40 to 7, and it renders `Ｏｈ，` — the same string `ほう、`
renders.** §18.2's split therefore separates おや and あ、 cleanly and does **not** separate おお
from ほう at all; it only appeared to because chunk 1's single instance happened to be `おお！`.

**Resolution: the collapse is real, wider than §18.2 admitted, and is accepted as deliberate** —
おお and ほう / ほお are one English word, `Ｏｈ`, plus the source's own punctuation, on exactly the
principle §6 already applies to ふっ / フンッ → `Ｈｍｐｈ` and §17.2 to 鬼 / オーガ → *ogre*. The
two alternatives were both already rejected on their merits: §10.6 rejected `Ｈｏｈ` for ほう and
§18.2 rejected `Ｏｈｏ` for おお, and reopening either would restyle shipped work in three files.

**Lines this affects (§4.3): none.** Every shipped instance already renders `Ｏｈ` plus the source's
stop — chunk 0 line 14 `ほう・・・。` → `Ｏｈ．．．．`, chunk 35 line 13 `Ｏｈ，`, chunk 1's `おお！`
→ `Ｏｈ！`, chunk 6's `おお、キャビア王女！！` → `Ｏｈ，　Ｐｒｉｎｃｅｓｓ　Ｃａｖｉａ！！`. **Nothing is
re-cut; what changes is the sentence in §18.2 that told future translators the punctuation was
keeping おお and ほう apart, when it is not.**

### 24.5 Recorded, not re-cut — two row-level variations that §3 does not reach

Both are the shape §20.4 (`帝国軍`) and §23.1 (`辺境`) already settled: **CLAUDE.md §3's
identical-JP rule engages on the message, not on the row**, because propagation and the dedupe
work on whole messages.

| Where | Japanese | The two renderings | Why it stands |
|---|---|---|---|
| chunk 6, lines 12 and 20 | `ファリーナの南、` | `ａｎｄ　ｓｏｕｔｈ　ｏｆ　Ｆａｒｉｎａ，` / `Ｓｏｕｔｈ　ｏｆ　Ｆａｒｉｎａ，` | Byte-identical **rows** in two entirely different messages. Line 12 is the priest's one continuous `病を患わされて、…静養しておられます。` sentence, where the て-form requires the English conjunction; line 20 is the Black Knight's bare fragment. Dropping the `ａｎｄ` would make line 12 ungrammatical, which §2 forbids |
| `chunk_000.txt` line 3 | `よし、` | `Ｇｏｏｄ，　{FC00}{=0000}．` there / `Ｒｉｇｈｔ，` in chunks 6, 10, 11 | Chunk 0's **row is `よし、{FC00}{=0000}。`** — the name insert is inside it, so it is not the same row and not the same message. Chunk 0 also has 27 bytes of slack (`FLAGS.md` §G1) and §18.3 records that its next correction needs a full re-cut. §24.3 fixes the bare form so nothing drifts forward |

⚠️ Note for future duplicate checks: a `さあ、` or `よし、` immediately followed by `{FC00}{=0000}`
is **not** the bare segment. `chunk_003.txt` line 4 (`さあ、{FC00}{=0000}、` →
`Ｃｏｍｅ　ｏｎ，　{FC00}{=0000}，`) and `chunk_000.txt` line 3 both look like bare-segment
divergences to a checker that splits on tags, and neither is one. The byte-identical bare `さあ、`
is `chunk_033.txt` line 20, which ships `Ｎｏｗ，` — the form chunk 6 correctly matches.

### 24.6 Register

| Who | Register |
|---|---|
| The Bernard's-church priest | Formal, humble, deferential, **no contractions** — `Ｈｅ　ｉｓ　ｍｙ　ｐｒｅｄｅｃｅｓｓｏｒ．`, `Ｉ　ｈａｄ　ｈｅａｒｄ　ｙｏｕ　ｒａｎ　ａｗａｙ`, `Ｈｏｗｅｖｅｒ，　Ｉ　ａｍ　ｓｏｒｒｙ　ｔｏ　ｓａｙ`. Matches Nacol's own register in chunk 7 |
| Cavia | §14.6 unchanged and held across every one of her segments — `Ｉ　ｗｉｌｌ　ｎｏｔ！`, `Ｗｈｅｒｅ　ｉｓ　Ｎａｃｏｌ？`, `Ｍｙ　ｅｒｒａｎｄ　ｈｅｒｅ　ｉｓ　ｎｏｔ　ｆｉｎｉｓｈｅｄ　ｙｅｔ．`, `Ｔｈａｔ　ｃａｎｎｏｔ　ｂｅ．．．`. No contraction anywhere |
| Fernando | §20.5 unchanged, nine segments, **no contraction anywhere** — `Ｉ　ｈａｖｅ　ｓｏｕｇｈｔ　ｙｏｕ．`, `Ｙｏｕ　ｍｕｓｔ　ｎｏｔ　ｋｅｅｐ　ｃｏｍｐａｎｙ　ｗｉｔｈ　ｓｕｃｈ　ｍｅｎ．`, `Ｓｏ　ｉｔ　ｉｓ　ｙｏｕ　ｍｅｎ　ｗｈｏ`. His `さ、` → `Ｃｏｍｅ，` and `さあ、` → `Ｎｏｗ，` are two source strings kept apart |
| Ridge and Sykes | §7 and §21.4 unchanged — blunt, needling, contractions throughout: `Ｈｅｙ，　Ｓｙｋｅｓ．`, `Ｉｔ’ｓ　ｂｅｅｎ　ａ　ｗｈｉｌｅ．`, `Ｄｏｎ’ｔ　ｔａｋｅ　ｈｉｍ　ｌｉｇｈｔｌｙ．` |
| The Black Knights (portraits 0009, 000A, 000C) | ⚠️ **Not the ch.7 commander of §14.6, and they read differently.** These are the rank and file — `だぜ` / `ぞ` / `じゃねえか` — so they take contractions (`ｌｅｔ’ｓ　ｒｅｐｏｒｔ`, `ｔｈｅｙ’ｒｅ`, `ｗｅ’ｒｅ　ｐｕｌｌｉｎｇ　ｂａｃｋ`) where the commander takes none. The `くくく` speaker keeps the flatness: `ｗｈａｔ　ａ　ｒａｓｈ　Ｐｒｉｎｃｅｓｓ．`, `ｓｏ　ｋｉｎｄ　Ｉ　ｃｏｕｌｄ　ｗｅｅｐ．` |
| Tutorial boxes (`{=FA1000300030}`, lines 6, 14, 17, 18) | §7 unchanged — plain instructional second person, no personality, and the passive of §21.3's shipped `村が襲われました。` → `Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．` |

---

## 25. Added by chunk 009 (PR #5, merged 2026-09-08)

Rendered in `tl/battle/chunk_009.txt` — chapter 9, the Empire's machine-soldier factory: Commander
Zephyr Krippen orders the place burned over his officer's objection that villagers are still
inside, then leaves with Guilford for Doctor Crimea in Westbury; the officer left in charge rallies
the garrison, boasts of the machine soldier and dies crying `ディール帝国、万歳！！！`; afterwards
the 9th Army takes stock, Seneca finds his father is not there, and two enslaved workers hand over
items. 3,973 / 8,192 bytes, slack 4,219 — 95 rows, widest 23, **none at 24**. Merged at round 2.

`しかし` and `しかしながら` → `Ｈｏｗｅｖｅｒ，` is §23.3's second and third use; `クッ` → `Ｔｃｈ`
(§11.5), `フン` → `Ｈｍｐｈ` (§6), `はっ` → `Ｓｉｒ` (§6), `行くぞ` → `Ｍｏｖｅ　ｏｕｔ` (§6) and
`よいか、` → `Ｌｉｓｔｅｎ　ｗｅｌｌ，` (§20.3) are used unchanged. The stolen-item message is copied
byte-for-byte from §21.3, three times.

### 25.1 People, places and ranks — two promotions out of §9, and one correction

`クリミア` is corrected **in §1**, not here, because it moves a fixed row out of §2.

| Japanese | English | Note |
|---|---|---|
| ディール帝国 | the `Ｄｉｅｌ` Empire | **Promoted from §9 (wave-2 seeds), used exactly as seeded.** 15 columns. The Empire's proper name, revealed for the first time in `ディール帝国、万歳！！！`. 2 battle occurrences, 0 script; the other is `ディール帝国紅の騎士団の将`, which agrees. Does **not** replace 帝国 → the Empire (§2) — that stays the common noun, and this chunk uses both. One voicing from 魔神ティール → `Ｔｙｒ` (§22.1) and deliberately spelled to stay visibly distinct from it |
| ワーウィック | `Ｗａｒｗｉｃｋ` | **Promoted from §9, used exactly as seeded.** 7 columns. A **place**, not a person: 2 battle + 6 script occurrences, all locational — `ワーウィックの要塞`, `ワーウィックの大要塞`, `ワーウィック攻略の拠点`, `ワーウィックという一大拠点`, `ワーウィック遠征` |
| クリミア博士 | `Ｄｏｃｔｏｒ　Ｃｒｉｍｅａ` | 13 columns. Built on §1's corrected `Ｃｒｉｍｅａ` row; only the title is new |
| 博士 | Ｄｏｃｔｏｒ | New rank word, spelled out like `Ｃｏｍｍａｎｄｅｒ` / `Ｃａｐｔａｉｎ` / `Ｂｉｓｈｏｐ` and never abbreviated `Ｄｒ．` — `．` is the full stop in this charset, so an abbreviating point would read as one |
| クリッペン司令官 (address) | `Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ．` | **18** columns (the PR body's 19 is one over — remeasured here). The direct-address form of §1's `Ｚｅｐｈｙｒ　Ｋｒｉｐｐｅｎ`, built like chunk 2's `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ`. 司令官 → Commander already stands (§11.2, and `batch_002`'s shipped `Ｃｏｍｍａｎｄｅｒ　ｏｆ　ｔｈｅ　Ｅｍｐｉｒｅ`) |
| 帝国兵 | `Ｉｍｐｅｒｉａｌ　ｓｏｌｄｉｅｒ` | 16 columns. Extends §20.4's default `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` for 帝国軍. Kept **distinct** from 帝国 → the Empire (§2); all three occur in this chunk |
| 全軍 | `Ａｌｌ　ｕｎｉｔｓ` | 9 columns. The form shipped in `chunk_007.txt` (`全軍　迎えうてッ！！` → `Ａｌｌ　ｕｎｉｔｓ，　ｉｎｔｅｒｃｅｐｔ！！`); recorded here because chunk 9 is the second use and it must not drift |
| 戦闘態勢に入れ | `ｔａｋｅ　ｂａｔｔｌｅ　ｓｔａｔｉｏｎｓ` | **20** columns (the PR body's 22 is two over — remeasured here). The military English for entering combat readiness; it still will not share a row with 全軍, which is why line 4 breaks mid-phrase |
| 化けモン | monster | Colloquial 化け物. `トカゲの化けモン` → *a lizard monster*, keeping §2's トカゲ → lizard |
| えじき | prey | `この兵器のえじきになりたいか` → *want … to become prey for this weapon* |
| 一片たりとも | `ｎｏｔ　ｏｎｅ　ｓｃｒａｐ` | 13 columns. Emphatic “not one fragment” |
| 逃げ遅れた者 | `ｔｈｏｓｅ　ｌｅｆｔ　ｂｅｈｉｎｄ` | 17 columns, a §2.1 step 4 shortening. The literal `ｔｈｏｓｅ　ｔｏｏ　ｌａｔｅ　ｔｏ　ｆｌｅｅ！！` measures **exactly 24** columns on a page already at the 4-row wall — verified at review |
| 浮かない顔して | `Ｙｏｕ　ｌｏｏｋ　ｄｏｗｎｃａｓｔ．` | **18** columns (the PR body's 19 is one over — remeasured here) |
| 気が抜けない | `ｃａｎ’ｔ　ｒｅｌａｘ` | Kept **distinct** from 油断は出来ない → `ｃａｎ’ｔ　ｌｅｔ　ｏｕｒ　ｇｕａｒｄ　ｄｏｗｎ`, which is two speaker turns earlier in the same scene — the source draws the distinction itself, so the English must |
| 甘くない (of an institution) | `ｈａｒｄｅｒ　ｔｈａｎ　…　ｔｈｉｎｋ` | 甘い of an institution is *soft / a soft touch*, whose exact antonym is *hard*, so a negated comparison and a positive one carry the same proposition — `softness < expected` and `hardness > expected` are one statement. **Ruled 2026-09-08, PR #5 round 2**: every literal split of `帝国は君たちが思うほど甘くない` either ends a row on `ａｓ` / `ｓｏ` or measures exactly 24, on a page at the 4-row wall, so the comparative is the only defect-free rendering. −4 bytes |

### 25.2 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| それでも | `Ｅｖｅｎ　ｓｏ，` | ⚠️ **Fixed here — it was missing from the glossary and from the PR's own additions table.** A **fourth** adversative, held apart from the three already fixed: でも → `Ｂｕｔ，`, それにしても → `Ｓｔｉｌｌ，` (§19.1), しかし / しかしながら → `Ｈｏｗｅｖｅｒ，` (§23.3). `Ｅｖｅｎ　ｓｏ` occurs nowhere else in `tl/`, so the form is free. `batch_002`'s `お前はそれでも、` is a **different source string** and is unaffected |
| 万歳！！！ | `Ｌｏｎｇ　ｌｉｖｅ　．．．！！！` | The salute, not a transliterated *banzai*. Punctuation follows the source per §5's word/punctuation rule |
| はっ・・・。 | `Ｓｉｒ．．．．` | §6's はっ → `Ｓｉｒ` carrying the source's own four stops — Guilford's flat assent. Distinct **in effect** from Albert's `Ｓｉｒ！` in chunk 2: one word, different punctuation, which is §5's mechanism, not a second entry |
| いや (deflection) | `Ｎｏ` + the source's punctuation | Seneca brushing a question aside. **Distinct** from §6's ああ → `Ｙｅａｈ` (assent) and はっ → `Ｓｉｒ` (military assent) |
| そのとおりだ。 | `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` | 13 columns. Firm agreement with a stated proposition. ⚠️ **Shares its English with §23.2's そうそう。 — ruled deliberate, see §25.3.** Held apart from 分かった / よし、 → `Ｒｉｇｈｔ，` (§6, §24.3), わかりました。 → `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` (§21.2) and まったくだっ！ → `Ｉｎｄｅｅｄ　ｗｅ　ｈａｖｅ！` (§20.3) |
| そうね。 | `Ｔｈａｔ’ｓ　ｔｒｕｅ．` | 12 columns. The female companion's softer agreement, one turn before そのとおりだ in the same scene. **Deliberately not collapsed into it** — this is the co-occurrence case, and it is exactly why §25.3 can leave the other one alone |
| ウワサ (`〜ってウワサだ`) | `ｔｈｅｙ　ｓａｙ` | The construction, not the noun — `襲われたってウワサだ` → *they say … got them*. `ｒｕｍｏｕｒ　ｉｓ　ａ　ｌｉｚａｒｄ　ｂｅａｓｔ` is 24 columns on a page at the 4-row wall. If a later unit needs the noun, *rumour* is still free |

### 25.3 Ruling — `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` renders two source strings, and that is accepted

`そうそう。` → `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` is fixed at §23.2 and shipped in `chunk_004.txt`; chunk 9
renders `そのとおりだ。` the same way. **Not a CLAUDE.md §3 violation** — §3 binds identical
Japanese. The question is whether house practice should split them anyway, and the answer is no.

**What decides it is a corpus fact, counted at this review across both dumps.** `そのとおり` occurs
**once in the entire project** — chunk 9, this line. `そうそう` occurs in battle chunks 4, 5, 17 and
43 and in 4 script lines. **No chunk and no bank contains both.** The collision can never be visible
to a player in one scene, and no future unit is forced into a re-cut by it.

With that, §24.3 governs, and it was ratified one PR earlier: `よし、` and `分かった` are two
genuinely different assent words that deliberately share `Ｒｉｇｈｔ，`, on the ふっ / フンッ →
`Ｈｍｐｈ` principle. §23.3's prohibition does **not** reach here — that ruling was about
*connectives*, and it turned on `Ｓｔｉｌｌ，` already being spent on `それにしても`, so collapsing
would have destroyed a live distinction. Nothing is spent here.

The practice of holding near-synonyms apart (§20.3, §21.2, §23.2) is stated for strings that
co-occur **in one scene**. Chunk 9 contains that case too, one turn away — `そのとおりだ` against
`そうね` — and it **is** held apart, as `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` / `Ｔｈａｔ’ｓ　ｔｒｕｅ．`.

**Lines this affects: none.** Reserve forms, both verified free across the whole corpus, if a later
chunk ever puts the two strings in one scene: **`Ｅｘａｃｔｌｙ．` (8 columns)** or
`Ｑｕｉｔｅ　ｒｉｇｈｔ．` (12). Prefer `Ｅｘａｃｔｌｙ．` — the speaker is a 9th Army companion who
contracts freely, `Ｑｕｉｔｅ　…` reads stiffer than his register, and it would sit awkwardly beside
`pending/chunk_005`'s `Ｑｕｉｔｅ　ｓｏ．`, which §23.2 is already retiring.

### 25.4 Ruling — `Ｆａｔｈｅｒ` carries both the priest and the parent, and English wants it to

§24.1 fixes `神父様` → `Ｆａｔｈｅｒ！` and `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` for the cleric.
Chunk 9 renders Seneca's `父さん・・・・` as `Ｆａｔｈｅｒ．．．．`, his actual parent. Different
source words, different messages, different scenes — and English has one word for both senses,
disambiguated by context in every instance (Seneca alone in a factory naming his missing parent;
Cavia calling into a church).

**Chunk 9 introduces nothing.** The parent sense is already the project's form, drafted
independently three times before this unit: `pending/chunk_005.txt` line 13 renders `お父様・・・・`
as `Ｆａｔｈｅｒ．．．．` — byte-identical to chunk 9's row — and `pending/chunk_043_abridged.txt`
lines 41–42 render a parent's notes as `Ｆａｔｈｅｒ’ｓ　ｎｏｔｅｓ　ｍｅｎｔｉｏｎ`. Splitting would
mean inventing a non-English form for one of the two senses.

⚠️ **Noted forward, not acted on.** `父さん` and `お父様` are now two source words sharing
`Ｆａｔｈｅｒ` — legitimate under §17.2's 鬼 / オーガ → *ogre*, but `お父様` is the formal one and is
the row to move if a chunk ever needs the distinction. `父さん・・・・` recurs untranslated in
chunks 16 and 39.

### 25.5 Register

| Who | Register |
|---|---|
| Zephyr Krippen (portrait 04) | Grandiose and absolute, **no contraction anywhere** — `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ！！`, `Ｉ　ｓｈａｌｌ　ｈｅａｄ　ｔｏ`, `Ｌｉｓｔｅｎ　ｗｅｌｌ，`. Commands in the bare imperative and never explains |
| Guilford (portrait 07) | One segment, flat assent — `Ｓｉｒ．．．．`. The four stops are the character: he does not object, and does not agree either |
| The officer left in command (portrait 08) | The same voice objects (line 2), rallies (line 4), boasts (line 7) and dies (line 8). Deferential upward (`Ｈｏｗｅｖｅｒ，　Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ．`), contemptuous downward (`ｔｏ　ｔｈｅ　ｌｉｋｅｓ　ｏｆ　ｙｏｕ，`), **no contractions** — §14.6 / §20.5's Imperial officers, unchanged |
| Seneca (portrait 05) | Quiet and deflecting; contractions (`Ｉｔ’ｓ　ｎｏｔｈｉｎｇ．．．．`, `ｗｅ　ｃａｎ’ｔ`). His one unguarded line is `Ｆａｔｈｅｒ．．．．`, and the chunk never explains it |
| The unnamed female companion (portrait 02) | Casual, contractions, the one who notices — `Ｗｈａｔ’ｓ　ｗｒｏｎｇ，　Ｓｅｎｅｃａ？`. Same portrait id as §21.4's unnamed female party member; if a later chunk names her, re-check both |
| The two enslaved factory workers (portraits 03, 09) | Beaten down and plain-spoken, contractions throughout — `Ｎｏｂｏｄｙ’ｓ　ｃｏｍｉｎｇ　ｔｏ　ｈｅｌｐ　ｕｓ．`, `Ｂｅｓｔ　ｎｏｔ　ｔｏ　ｒｅｓｉｓｔ．`. 09 is the blunter of the two and gives the party an item anyway |
| Tutorial boxes (`{=FA1000300030}`, lines 13–15) | §7 unchanged — plain instructional second person, the source's passive kept, byte-identical to §21.3 |

---

## 26. Added by script batch 005 (PR #8, merged 2026-09-08)

Rendered in `tl/script/batch_005.tsv` — `script_unique.txt` lines **984–1001 and 1040–1047**, 26
unique lines, 1 instance each. Three groups: the old tutor's five tutorial boxes (984–988, bank
29), the fortress-guard and rumour dialogue (989–1001, bank 30), the Bernard's-church scene
(1040–1047, bank 31). 1,980 JP → 4,004 EN characters, **2.02×**; 4,040 bytes; banks 29 / 30 / 31
left with 25,589 / 35,119 / 34,827 free. Widest row 23, **none at 24**, no page over 4 text rows.
Merged at round 2. Lines 1002–1039 and 1048–1100 are the developer debug menu and are deliberately
not in this batch.

`しかし、` → `Ｈｏｗｅｖｅｒ，` is §23.3's fourth use; `それにしても` → `Ｓｔｉｌｌ，` (§19.1),
`全く` → `Ｒｅａｌｌｙ，` (§6), `おお、` → `Ｏｈ，` (§24.4), `Ｂｅｒｎａｒｄ’ｓ　ｃｈｕｒｃｈ` (§14.2),
`Ｋｏｒｎｅｆｆ` / `adventurer` (§21.1), `Ｆｅｒｉｓｌａｎｄ` (§11.2), `Ｈｅｌｆｅｒ` (§11.1),
`Ｓｑｕａｒｅ　ｂｕｔｔｏｎ` (§3), `heavy swordsman` (§20.2) and `garrison` (§2) are used unchanged.
Script 1001 is the very line §21.1's `探検家` note pointed at, and it holds 冒険者 → *adventurer*
distinct from 探検家 → *explorer*, exactly as that note required.

### 26.1 People and places — three promotions out of §9, and one new name

| Japanese | English | Note |
|---|---|---|
| バトウ | `Ｂａｔｏｕ` | **Promoted from §9 (wave-2 seeds), used exactly as seeded.** 6 columns. The priest of Bernard's church, dead before the church scene. `神父のバトウと申します` → `Ｉ　ａｍ　ｔｈｅ　ｐｒｉｅｓｔ　Ｂａｔｏｕ．`; §1's bare 神父 → *priest* is unchanged. 3 battle + 8 script occurrences. Alt *Batow*, *Bathou* |
| バトウ様 | `Ｆａｔｈｅｒ　Ｂａｔｏｕ` | **Ruled 2026-09-08, PR #8 round 1; applied at round 2.** 15 columns with the possessive. 様 takes the English title of the man's station, exactly as §24.1 fixed `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` and as §1 / §14.1 fix Lady Rimul, Lord Helfer, Lady Phyllis, Lady Cavia. Line 1041 establishes the station in the same scene. ⚠️ **§21.2's drop-the-honorific rule reaches `〜さん` on a personal name and nothing else** — the `様` and `さん` patterns are separate and must never be merged. §24.1 is **unamended** by this entry; it is applied, not extended |
| クレウス司教 / 司教 | Bishop `Ｃｒｅｕｓ` / Bishop | **Both promoted from §9.** 13 columns; the possessive is `Ｃｒｅｕｓ’`. 司教 → **Bishop**, spelled out like `Ｃｏｍｍａｎｄｅｒ` / `Ｃａｐｔａｉｎ` / `Ｄｏｃｔｏｒ` (§25.1). Alt *Kreus* |
| リース文明 | the `Ｒｅｅｓｅ` civilisation | **Promoted from §9, used exactly as seeded.** British *‐isation*, per the defence / armour policy (§4). 20 columns, so it never shares a row. ⚠️ **§9's warning is discharged: `リース文明` is NOT `古代ハイランド`.** Counted at this review across both dumps — `リース` 8 script / 0 battle, `ハイランド` 2 script / 9 battle, and **zero lines in either dump contain both**. Script 1047 ties Reese to a legend, to documents found in Farina, to war among its own kind and to Bishop Creus's ancestors; §11.2 ties Highland to the floating island and the sky fortress. **Both the §9 row and the §11.2 row stay.** Alt *Riese*, *Lies* |
| アップミーズ | `Ａｐｕｍｉｚｕ` | **New — never in §9 at all**, surfaced by this batch. 8 columns. A **town**, not a person: 5 script + 0 battle occurrences, and `ホアグ王子がつくった街、アップミーズよ！` (*Apumizu, the town Prince Hoag built*) settles it outright, with `「アップミーズの街」` and `新しくできた街` agreeing. `Ａｐｕｍｉｚｕ` occurs nowhere else in `tl/`. Alt *Upmeeze*, *Apmiz* |
| 神殿 | temple | `謎の神殿` → `ａ　ｍｙｓｔｅｒｉｏｕｓ　ｔｅｍｐｌｅ`. Kept **distinct** from 教会 → church (§14.2) and 聖堂 → sanctuary (§12.1) — three source words, three English words |

⚠️ **A factual correction to §11.2 (§4.3).** That entry says `フェリスランド` "appears nowhere else
in either dump". **It does** — counted at this review, **2 battle + 11 script occurrences**, one of
them script 1001 in this very unit (`フェリスランドへ行ったんだが` →
`Ｉ　ｗｅｎｔ　ｔｏ　Ｆｅｒｉｓｌａｎｄ`), another `ホアグ王子はフェリスランドだ`. **The rendering
`Ｆｅｒｉｓｌａｎｄ` is unchanged and no translated line needs revisiting** — only the note was wrong.
The name is now shipped rather than parked; `pending/chunk_043.txt` and its abridgement also carry
it, byte-identically.

### 26.2 Ranks — `将軍` → `Ｇｅｎｅｒａｌ`, and §10 question 2 is CLOSED

| Japanese | English | Note |
|---|---|---|
| 将軍 | Ｇｅｎｅｒａｌ | **RATIFIED 2026-09-08, PR #8 review. This closes §10 question 2 and §9's correction 2.** `２軍のフェルナンド将軍` → `Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ　ｏｆ　ｔｈｅ　２ｎｄ　Ａｒｍｙ` (23 columns). Fernando holds two titles; it is the source that varies, not the translation |
| ２軍 (bare) | ２ｎｄ　Ａｒｍｙ | Line 992 writes the bare `２軍`, not `宮廷第２軍`, so §20.1's `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ` does **not** apply — already shipped practice in `chunk_002` line 3. Two source spellings, two English forms, deliberately |

**The corpus decides it, counted at this review across both dumps.** `フェルナンド将軍` occurs **17
times** (6 battle + 11 script); `フェルナンド隊長` occurs **2 times** (2 battle + 0 script). §2's
隊長 → *captain* is untouched. **Nothing shipped is re-cut, and this was verified rather than
assumed**: all three shipped `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ` were traced back to their source
strings — `chunk_002.txt` ×2 render `フェルナンド隊長`, `chunk_006.txt` ×1 renders
`この宮廷第２軍隊長、フェルナンドめが` — and **neither chunk contains a single `将軍`**.
`Ｇｅｎｅｒａｌ` appears nowhere else in `tl/`.

### 26.3 Tutorial and mechanics vocabulary — six promotions out of §9

| Japanese | English | Note |
|---|---|---|
| ＺＯＣ（支配地域） | `ＺＯＣ　（ｚｏｎｅ　ｏｆ　ｃｏｎｔｒｏｌ）` | **Promoted from §9, used exactly as seeded.** 21 columns, so it breaks across two rows at `ｏｆ`. The gloss is **not** the redundancy §3 struck from `待ち時間（Ｗａｉｔ）` — ZOC is opaque in English too |
| 中立ユニット | neutral unit | **Promoted from §9** |
| 前衛 / 後衛 | front line / rear line | **Promoted from §9.** ⚠️ One instance renders them `ｉｎ　ｆｒｏｎｔ` / `ｂｅｈｉｎｄ` for width — 985 page 3, where `ａ　ｍａｇｅ　ｔｏ　ｔｈｅ　ｒｅａｒ　ｃｏｖｅｒｓ` is 25 columns. Flagged; the full forms are used on page 1 of the same box |
| 『説得』 / 説得する | `“Ｐｅｒｓｕａｄｅ”` / persuade | **Promoted from §9.** Quoted and capitalised as the command (988 p2), bare lowercase verb where the source itself drops the quotes (988 p3). That is §I1's rule, settled at this review |
| 『ＧＵＥＳＴ　ＵＮＩＴ』 / 「ＥＮＴＥＲ」 | `“ＧＵＥＳＴ　ＵＮＩＴ”` / `“ＥＮＴＥＲ”` | **Promoted from §9.** Already full-width Latin in the source: **reproduced, not re-cased.** Bare `ＥＮＴＥＲ地点` → `ＥＮＴＥＲ　ｐｏｉｎｔ`, unquoted, because the source drops the quotes there too |
| 同盟 | alliance | **Promoted from §9.** `カーラインと帝国との同盟祝賀会` → `Ｔｈｅ　Ｃａｒｌｉｎｅ‐Ｅｍｐｉｒｅ　ａｌｌｉａｎｃｅ　ｂａｎｑｕｅｔ`, using `‐` (U+2010) |
| 『支援効果』 | `“Ｓｕｐｐｏｒｔ　Ｅｆｆｅｃｔ”` | Quoted **and** capitalised, because the source quotes it |
| 包囲効果 / 包囲される | the encircling effect / be encircled | **Unquoted and lowercase**, because the source leaves it unquoted where it quotes 『支援効果』 two sentences later in the same box. **The source's own quoting distinction is preserved deliberately** — that is the whole of §I1's rule inside one message. *Encircling*, not *encirclement*: 23 columns against 25 |
| 『ビーストテイム』 | `“Ｂｅａｓｔ　Ｔａｍｅ”` | Skill name, 13 columns. Capitalised to match ビーストマスター → `Ｂｅａｓｔ　Ｍａｓｔｅｒ` (§4), a coined conferred name under §17.1 |
| ヘクス | hex | The map cell. `隣接するヘクス` → `ａｎ　ａｄｊａｃｅｎｔ　ｈｅｘ` |
| クラスの相性 | class matchups | *Compatibility* is 13 columns and will not share a row |
| 戦士系 / 遠隔系 | warrior types / ranged ones | `〜系` → *types*; the second instance is `ｒａｎｇｅｄ　ｏｎｅｓ` to avoid *types* twice in one sentence |
| 編成 | form (your units) | Verbal. Kept **distinct** from 部隊 → squad (§19.2) and 分隊 → 3rd Squad (§2) |
| ゲスト / ゲームオーバー | guest / the game is over | Lowercase *guest* in prose (§17.1 species test) where the displayed label is `“ＧＵＥＳＴ　ＵＮＩＴ”`. The batch draws that line itself, unprompted, and it is exactly §I1's rule |

### 26.4 Words, phrases and proverbs

| Japanese | English | Note |
|---|---|---|
| 砦 | ｆｏｒｔ | **Ruled 2026-09-08, PR #8 round 1; applied at round 2.** Kept **distinct** from 要塞 → fortress, 大要塞 → great fortress (§2) and 空中要塞 → sky fortress (§11.2) — four source words, four English forms. It is also §2's own shipped form: `tl/battle/chunk_040.txt` line 2 ships `バウワーの砦` → `Ｂａｕｅｒ’ｓ　ｆｏｒｔ` **and** `「砦の戦い　再び」` → `“Ｔｈｅ　Ｂａｔｔｌｅ　ｏｆ　ｔｈｅ　Ｆｏｒｔ，　Ａｇａｉｎ．”`. Verified at review: `ｆｏｒｔｒｅｓｓ` occurs in `tl/` only for 要塞 |
| 犯人 | the culprit | |
| 反乱軍 | the rebels / the rebel army | Kept **distinct** from 帝国 → the Empire (§2), 本隊 → the main force and 主力部隊 → the main body (§20.1). The bare plural is the width form: `Ａｒｍｉｅｓ　ｆｅｌｌ　ｔｏ　ｔｈｅ　ｒｅｂｅｌｓ．` is 28 columns |
| 派の連中 | faction | `フェルナンド派の連中` → `Ｆｅｒｎａｎｄｏ’ｓ　ｆａｃｔｉｏｎ` |
| 復興 | rebuilding / rebuild | Used of both the church (1045) and Farina (1046) |
| 冒険者 | adventurer | **First actual rendering** — §21.1 fixed the word but nothing had used it. `冒険者のコーネフって男` → `ａ　ｍａｎ　ｃａｌｌｅｄ　Ｋｏｒｎｅｆｆ，　ａｎ　ａｄｖｅｎｔｕｒｅｒ`. Kept distinct from 探検家 → explorer, exactly as §21.1 required |
| うわさ (the noun) | rumours | **Takes up the reservation §25.2 left open** (“if a later unit needs the noun, *rumour* is still free”). Verified at review to be no collision: `〜ってウワサだ` occurs **once** in the whole project (battle chunk 9, → `ｔｈｅｙ　ｓａｙ`) and `うわさ` **once** (script 1044); two different source strings that never meet, and `ｒｕｍｏｕｒ` occurs nowhere else in `tl/`. `ご活躍の　うわさは聞いております` → `Ｉ　ｈａｖｅ　ｈｅａｒｄ　ｔｈｅ　ｒｕｍｏｕｒｓ　ｏｆ　ｙｏｕｒ　ｅｘｐｌｏｉｔｓ．` |
| 油を売る | ｌｏａｆ | `こんな所で油売ってないで` → `Ｒａｔｈｅｒ　ｔｈａｎ　ｌｏａｆ　ｈｅｒｅ`. A genuine equivalent, not a substituted idiom |
| 急がば回れ | `Ｍｏｒｅ　ｈａｓｔｅ，　ｌｅｓｓ　ｓｐｅｅｄ，　ｔｈｅｙ　ｓａｙ．` | English proverb carrying the same point, on the §20.3 貧乏クジをひく precedent |
| 石橋を叩いて渡る | `ｌｏｏｋ　ｂｅｆｏｒｅ　ｙｏｕ　ｌｅａｐ` | The genuine English equivalent — same act, same caution |
| バカとハサミは使いよう | `Ｉｔ　ｉｓ　ａ　ｐｏｏｒ　ｗｏｒｋｍａｎ　ｔｈａｔ　ｂｌａｍｅｓ　ｈｉｓ　ｔｏｏｌｓ，　ｔｈｅｙ　ｓａｙ．` | A **fourth** バカ register, beside §19.1's そんなバカな → `Ｔｈａｔ’ｓ　ｉｍｐｏｓｓｉｂｌｅ` and バカなやつら → `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ`, and §20.3's バカ者 → `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ`. ⚠️ **The loosest of this batch's three proverbs, accepted at review with the shift recorded**: the two share the premise *the outcome is in the user, not the tool*, but the Japanese is encouraging where the English chides. It stands because the page is at the 4-row wall (21 / 23 / 20 / 23) so no fuller rendering fits, and because the very next sentence, `Ｕｓｅｆｕｌ　ｏｒ　ｕｓｅｌｅｓｓ　ｉｓ　ｕｐ　ｔｏ　ｙｏｕ．`, restores the constructive sense. See `FLAGS.md` §N4 |

### 26.5 Interjections

| Japanese | English | Note |
|---|---|---|
| ふーむ | `Ｈｍｍ，` | Extends §6's む / ん → `Ｈｍ`; the lengthened kana takes the extra `ｍ`, per the kana-beat convention (§11.5, §14.5, §24.3). **Distinct** from `Ｈｍｐｈ` (ムムッ / ふっ / フンッ), `Ｔｃｈ` (くっ) and `Ｏｈ` (ほう / おお) |

### 26.6 Hearsay frames — `ｔｈｅｙ　ｓａｙ` and `Ｗｏｒｄ　ｉｓ` both render `らしい`

⚠️ **Recorded at review; the PR did not raise it.** This unit renders `らしい` two ways —
`ｔｈｅｙ　ｓａｙ` in 991 and 992, `Ｗｏｒｄ　ｉｓ` in 995 and 1000 — and also gives `ｔｈｅｙ　ｓａｙ` to
`〜って話だ`, `〜そうです`, `〜だってよ` and `と言うじゃろ`. **This is not a CLAUDE.md §3 violation**:
§3 engages on the **message**, not the row (§20.4, §23.1, §24.5), and every one of these sits in a
different message. It is recorded so it cannot drift:

- **`ｔｈｅｙ　ｓａｙ` is the default** for every hearsay evidential — it is also §25.2's fixed form
  for `〜ってウワサだ`, and one English hedge serving several Japanese ones is the deliberate
  collapse §17.2 makes for 鬼 / オーガ and §25.3 ratified for `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`.
- **`Ｗｏｒｄ　ｉｓ` is the sentence-initial variant**, taken where the hedge leads the sentence and a
  trailing `ｔｈｅｙ　ｓａｙ` would be the third in as many rows. Both forms are free elsewhere in `tl/`.
- §25.3's test is met: no two of these source strings appear in one scene, so no player can see
  the collapse.

### 26.7 Register — the tutorial row keys on the speech, not on a marker

| Who | Register |
|---|---|
| The old tutor (`じゃ` / `のじゃ` / `じゃろ`, script 984–988) | **New row, 2026-09-08, PR #8.** Plain, old-fashioned instructional English, **no contractions anywhere** — verified across all five boxes at review. The old-fashioned tinge sits in word choice (`ｔｈｅｙ　ｓａｙ`, `Ｂｅａｒ　ｉｔ　ｉｎ　ｍｉｎｄ`, `ｄｏ　ｔａｋｅ　ｃａｒｅ`), never in archaic spelling — the same rule §7 already gives "Village elders (じゃ / のう)". ⚠️ **This row keys on the SPEECH, not on any message marker.** An earlier draft keyed it on `{FB01}`; that premise was disproved at review (666 script + 148 battle occurrences of `{FB01}`, and only 47 of 342 opened lines carry `じゃ`) and has been removed. §7's `{=FA1000300030}` tutorial-box row is a **different** thing and is unchanged |
| The fortress guards and rank-and-file soldiers (script 989–1001) | Casual and grumbling, **contractions throughout** — `Ｔｈｅｒｅ’ｓ`, `Ｉ’ｖｅ`, `Ｗｅ’ｒｅ`, `Ｔｈｅｙ’ｖｅ`. §20.5 / §24.6's soldiers, unchanged. The one officer who says `貴官ら` (993) takes none — `Ｉｓ　ｉｔ　ｔｒｕｅ　ｔｈａｔ　ｙｏｕ`, `ｉｓ　ｎｏｔ　ｈａｌｆ　ｂａｄ` |
| The Bernard's-church clergy (script 1040–1047) | Formal, humble, **no contractions** — `Ｉ　ａｍ　ｔｈｅ　ｐｒｉｅｓｔ　Ｂａｔｏｕ．`, `Ｍａｙ　ｔｈｅ　ｂｌｅｓｓｉｎｇ　ｏｆ　Ｇｏｄ　ｂｅ　ｕｐｏｎ　ｙｏｕ．`, `Ｈｏｗ　ｐｏｗｅｒｌｅｓｓ　ａ　ｔｈｉｎｇ　ｍａｎ　ｉｓ．`, `Ｈｉｓｔｏｒｙ　ｄｏｅｓ　ｒｅｐｅａｔ　ｉｔｓｅｌｆ，　ｄｏｅｓ　ｉｔ　ｎｏｔ．` §24.6's Bernard's-church priest, unchanged and extended to his successors. `９軍のみなさん` → `ｇｏｏｄ　ｐｅｏｐｌｅ　ｏｆ　ｔｈｅ　９ｔｈ　Ａｒｍｙ` carries the polite plural vocative in word choice, per §2's politeness rule |

### 26.8 `助かりました` — a third member of the §23.4 family

| Japanese | English | Note |
|---|---|---|
| 助かりました (polite, of a past rescue) | `Ｙｏｕ　ｓａｖｅｄ　…` | **Ruled 2026-09-08, PR #8 round 1; the active stands.** `この前は　助かりました。ありがとうございます。` → `Ｙｏｕ　ｓａｖｅｄ　ｕｓ　ｔｈｅ　ｏｔｈｅｒ　ｄａｙ．　Ｔｈａｎｋ　ｙｏｕ．` The polite past form under `この前は` is a speaker **turning to thank his rescuer**, which is §23.4's own licence for the active, and the following `ありがとうございます` makes the address explicit where chunk 12's `あんちゃん` did. **A third row in §23.4, not an exception to it**: the plain 助かった of one's own condition still takes `Ｉ／Ｗｅ　ａｍ／ａｒｅ　ｓａｖｅｄ`, and `chunk_001` line 14's correction (§23.4) is unaffected. 9 occurrences of 助かりました across both dumps — this rule now governs them |

---

## 27. Added by the wave-1 corrections unit (PR #9, merged 2026-09-08)

Not a new unit of text: PR #9 applies `audits/wave1-reading-review.md` (its table of 8, **raw file**
line numbers) and `audits/wave-1-audit.md` items 3–5 and §9 (**message** line numbers = file
line − 1) to already-shipped work, plus three rulings made after those audits were written —
§23.3 (`しかし`), §23.4 (`助かった`) and `FLAGS.md` §N2 (`“ＥＮＴＥＲ”`). **Twelve edits across five
files**: `tl/script/batch_004.tsv` L12/L17/L29/L42, `tl/battle/chunk_001.txt` file L2/L15,
`chunk_002.txt` file L14, `chunk_003.txt` file L6 ×2 and L17 ×2, `chunk_034.txt` file L8.

Verified at review, re-derived rather than inherited: chunk 1 **3,519** · chunk 2 **5,855** ·
chunk 3 **4,605** · chunk 34 **1,587 (−4)**. `batch_004` **+38 bytes in each of 21 banks**; bank
40 **509 → 471** free, bank 41 **unchanged at 353**, no bank negative. `chunk_000.txt` (27 B
slack) and `chunk_007.txt` (399 B) are **byte-for-byte untouched** — identical blob hashes on both
sides. **The tag stream is byte-identical to the base on every line of all four chunks**: no
re-flow, no break added, moved or deleted, no `{FCC0}` touched. Widest row in the unit **23**,
none at 24. **No §9 PROVISIONAL row is promoted here — this unit renders no new name.**

### 27.1 Words and phrases first fixed here

| Japanese | English | Note |
|---|---|---|
| 愛用 | **`ｆａｖｏｕｒ`** — voice and tense follow the source | The wave-1 reading review's glossary finding 2: three shapes were shipped and the word had no entry. **After PR #9 all four shipped instances share the verb**, and what varies is grammar the source itself varies: `オーガの愛用するハンマー` → `ｆａｖｏｕｒｅｄ　ｂｙ　ｏｇｒｅｓ` and `女神アルテミスの愛用した光の弓` → `ｆａｖｏｕｒｅｄ　ｂｙ　ｔｈｅ　ｇｏｄｄｅｓｓ　Ａｒｔｅｍｉｓ` (`batch_003` 105, 109 — passive, the word modifying the weapon); `多くの兵士が愛用する一般的な剣` → `ｍａｎｙ　ｓｏｌｄｉｅｒｓ　ｆａｖｏｕｒ` (present) and `黒騎士たちの愛用した漆黒の槍` → `ｔｈｅ　ｂｌａｃｋ　ｋｎｉｇｈｔｓ　ｆａｖｏｕｒｅｄ` (past — contact relative clauses, the weapon being the object). ⚠️ **Counted at this review: `script_unique.txt` holds 13 unique lines containing 愛用 (273 dump instances ÷ 21), of which 4 are now rendered, so 9 remain untranslated — 189 message instances**, not the "13 remain" that both PR #9's body and the audit wrote. The nine are 雷神トール, 巨人の, 水の妖精, 天使, 魔術師, 伝説の聖者, 妖精フィリス, 軍神ヘルメス, 風の精. §22.2's stated frame (“a participial clause”) describes neither `batch_004` form and is widened by this row |
| 一般的な / もっとも一般的な | `ｃｏｍｍｏｎ` / `Ｔｈｅ　ｃｏｍｍｏｎｅｓｔ` | The positive and its superlative, now visibly a pair two rows apart in one table (`batch_004` L12 and L31). 一般的な had been dropped from L12 entirely and 多くの strengthened to *most*; both are restored. 126 script occurrences (6 unique lines × 21), so 4 unique lines still to come |
| 焼き尽くす | **`ｂｕｒｎ　…　ｔｏ　ａｓｈ`** | Burn-to-nothing, not *burn up*. Distinct from 燃やす. ⚠️ **This supersedes §22.1's 火炎剣 note — see §27.3.** Recurs in §9's `Ｉｆｒｉｔ` gloss (`紅蓮の炎で焼き尽くしてくれるわっ！`, chunk 15), so **any chunk 15 unit and wave 3's chunk 17 unit inherit this form** |
| すみません。 (as apologetic thanks) | `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` | 21 columns. Not an apology for wrongdoing: the speaker has just been rescued and says `ありがとうございます` in the next breath. Held **distinct** from §24.3's すいません。 → `Ｅｘｃｕｓｅ　ｍｅ．` (chunk 6) and from ちょっと、 → `Ｈｏｌｄ　ｏｎ，` — three source strings, three jobs. Counted at this review: `すみません。` **3 battle / 0 script**, one now rendered (`chunk_002` file L14), two still to come |
| 宮廷軍のみなさん | `Ｅｖｅｒｙｏｎｅ　ｉｎ　ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ` | の for membership is *in*, not *of*. A hapax — **1 battle / 0 script**, `chunk_003` file L17. Does **not** disturb §26.7's shipped `９軍のみなさん` → `ｇｏｏｄ　ｐｅｏｐｌｅ　ｏｆ　ｔｈｅ　９ｔｈ　Ａｒｍｙ`: that is the *citizens-of-Rome* vocative, idiomatic with *of*, and a different source string |

### 27.2 The village-attack message — one rendering binds thirteen instances

| Japanese | English |
|---|---|
| `村が襲われました。` | **`Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．`** |

A §21.3-style binding entry, which the wave-1 reading review's §9 asked for. Its marker is
`{=FA1000300030}`, the personality-free tutorial box of §7, so the register is plain instructional
second person. Rows measure **14 and 13**, so it fits anywhere.

**Counted in `dumps/battle_dump.txt` at this review, not taken from a report: 13 instances, 0 in
the script dump** — chunks 5, 7 ×2, 13, 15, 16 ×2, 17, 21, 23, 34, 38, 39. Three are now shipped
byte-identically (`chunk_007` L26 and L27, `chunk_034` L8) and **ten are still untranslated**.
**Copy it; do not re-invent it.**

This closes a **live CLAUDE.md §3 violation** that predates wave 1: `chunk_034` L8 shipped
`Ｔｈｅ　ｖｉｌｌａｇｅ　ｈａｓ　ｂｅｅｎ{FFFE}ａｔｔａｃｋｅｄ．` against chunk 7's wording. Chunk 34 moved
and chunk 7 was left alone because chunk 34 has 6,601 bytes of slack and chunk 7 only 399.
Verified at review by a positional duplicate scan at two granularities: **1 divergent rendering
before, 0 after — `tl/battle/` is free of divergent duplicate renderings for the first time in the
project.**

✅ **Already inherited correctly by both wave-3 siblings**, checked on their branches at this
review rather than taken on report: `tl/battle/chunk_013.txt` L8 (PR #10) and
`pending/chunk_017.txt` L21 (PR #12) both carry the wording byte-for-byte.

### 27.3 CORRECTION to §22.1 (§4.3) — the 火炎剣 row's gloss is superseded

§22.1's `火炎剣` row reads `すべてを焼き尽くす` → *burning all up*. **That is superseded by §27.1's
`焼き尽くす` → `ｂｕｒｎ　…　ｔｏ　ａｓｈ`.** `ｂｕｒｎｉｎｇ　ａｌｌ　ｕｐ` is not idiomatic English as a
participial modifier, and 焼き尽くす is burn-to-nothing rather than burn-up.

**Lines this affects: exactly one, and it is already applied.** `tl/script/batch_004.tsv` **L17**,
`すべてを焼き尽くす強力な火炎剣。` → `Ａ　ｐｏｗｅｒｆｕｌ　ｆｌａｍｅ　ｓｗｏｒｄ{FFFE}ｂｕｒｎｉｎｇ　ａｌｌ　ｔｏ　ａｓｈ．`
— 22 / 19 / 6 columns, **+8 bytes per bank**. Verified affordable and complete at this review:
`焼き尽く` occurs **1 battle (chunk 15, the Ifrit line, untranslated) and 21 script (this one
unique line × 21)**, so L17 is the only rendering anywhere in `tl/` and nothing else needs
revisiting. The `火炎剣` → *flame sword* half of §22.1's row is unchanged.

Recorded here rather than patched into §22.1 in place, per §4.3 and CLAUDE.md §6.7: an existing
entry is never altered silently. PR #9's Glossary-additions table proposed the new form with its
reason but stated “Nothing existing was changed” — something was, and this is the correction.

### 27.4 CORRECTION to §24.6 (§4.3) — the spaced and unspaced village lines are DIFFERENT strings

§24.6's register table (the `Tutorial boxes ({=FA1000300030}, lines 6, 14, 17, 18)` row) ends:
*“the passive of §21.3's shipped `村が襲われました。` → `Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．`”*.
**Three things in that clause are wrong. No rendering changes; only the note does.**

1. **The source string in chunk 6 is `村が　襲われました。` — with a full-width space between `村が`
   and `襲われました` — and it is NOT the string §27.2 governs.** Counted across both dumps at this
   review: the **unspaced** form occurs **13** times, the **spaced** form **once**, at
   `chunk_006.txt` file line 15. They are different lookup keys, so CLAUDE.md §3 is **not**
   engaged, chunk 6 is **not** re-cut, and the positional duplicate scan agrees — it reports zero
   divergences with both forms present. This is the メルザリオ / ファリーナ / クリミア shape
   (§20.1, §2, §1): the classification was wrong, the rendering was not.
2. **§21.3 is the stolen-item message** (`アイテムを{FFFE}奪われました。` →
   `Ａｎ　ｉｔｅｍ　ｗａｓ{FFFE}ｓｔｏｌｅｎ　ｆｒｏｍ　ｙｏｕ．`). It does not contain `村が襲われました。`
   at all. The binding entry for the village line is **§27.2**, not §21.3.
3. **The row's line list omits line 15**, which is the very line it is describing.

**Read that row as:** tutorial boxes at `{=FA1000300030}`, `chunk_006.txt` **lines 6, 14, 15, 17,
18** — §7 unchanged, plain instructional second person, no personality; **line 15 renders the
hapax `村が　襲われました。` (spaced) as `Ａ　ｖｉｌｌａｇｅ　ｗａｓ　ａｔｔａｃｋｅｄ．` and stands.**

⚠️ **Recorded because the two strings are one full-width space apart.** A future duplicate check
run by eye — or any tool that normalises whitespace — will read chunk 6 as a fourth violation of
§27.2 and try to “fix” it. It is not one. Same trap as §24.5's `さあ、` / `よし、` followed by
`{FC00}{=0000}`.

---

## 28. Added by chunk 013 (PR #10, merged 2026-09-08)

Rendered in `tl/battle/chunk_013.txt` — chapter 14's lead-in, seven scenes: Lord Irvine taunting
the captured Cress and promising her to General Guilford; the alarm as the 9th Army arrives; Cress
berating the player for disobeying orders, then thanking him and leaving for Leverk; the rescued
King's speech (**two mutually exclusive variants, message lines 4 and 5, verified byte-identical in
English — 365 characters including tags**, as chunk 2's coda variants already are); a boy who gives
the party an item; the village-attacked box; and the Leclerc soldier who is argued out of a fight
and joins the squad. **5,417 / 8,192 bytes, slack 2,775 — 132 rows, widest 23, none at 24**, no
page over 4 text rows. Merged at round 1.

⚠️ **Line numbers in this section are MESSAGE lines** (dump body index, 1-based), which is one less
than the `tl/` file line because the `=== CHUNK` header is kept. `HANDOFF.md` called the
village-attack line L8; it is **message line 7**. Same row. This is the third numbering convention
in play in this repo (`FLAGS.md` §O8) — locate by content.

`Ｔｃｈ` (§11.5), `Ｓｉｒ！` (§6), `Ｈｏｗｅｖｅｒ，` (§23.3 — its fifth use), `Ｌｉｓｔｅｎ，` (prompt §5),
`Ｎｏｗ，` (§24.5), `Ｉｎ　ａｎｙ　ｃａｓｅ，` (`chunk_012` L16), `Ｒｉｇｈｔ` (§6), `ｔｈｅ　Ｉｍｐｅｒｉａｌ
ａｒｍｙ` (§20.4 default), `ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ` (§2 full form), `Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ`
(§26.2 + §1), `Ｍｉｓｔｅｒ` (§2), `Ｃｒｅｓｓ` / `Ｃａｒｌｉｎｅ` / `Ｃａｕｃａｓｕｓ` (§1–§2) are used
unchanged. `助かりました！！` → `Ｙｏｕ　ｓａｖｅｄ　ｕｓ！！` is the **first battle-side application of
§26.8**, exactly as that ruling says it governs all nine occurrences; `助けてもらった` →
`ｄｉｄ　ｈｅｌｐ　ｍｅ` correctly stays out of the §23.4 family, being a different construction.
`村が襲われました。` is copied byte-for-byte from **§27.2** (message line 7), verified at review.

### 28.1 People and places — three promotions out of §9, and two description corrections

| Japanese | English | Note |
|---|---|---|
| アーバイン様 | `Ｌｏｒｄ　Ｉｒｖｉｎｅ` | **Promoted from §9 (wave-3 seed).** The enemy commander of message lines 1–2; his subordinate addresses him 様 and he answers `まあよい` / `叩き潰してやれ！！`. 様 → Lord per §14.1, held clear of §21.2's さん rule. ⚠️ **`Ｉｒｖｉｎｅ` is 6 columns and `Ｌｏｒｄ　Ｉｒｖｉｎｅ` is 11** — §9's seed said 7 and 12 and was wrong on both. The seed was the orchestrator's; the translator caught it and it was remeasured at review on the shipped row (`Ｌｏｒｄ　Ｉｒｖｉｎｅ！` = 12 with the mark). Rendering unchanged. **1 battle + 0 script** |
| ルクレール | `Ｌｅｃｌｅｒｃ` | **Promoted from §9, used exactly as seeded — but §9's description is CORRECTED (§4.3): it is a KINGDOM, not "a castle".** 8 columns. Evidence counted across both dumps at review: `ルクレールの兵士` (its soldiers) and `我がルクレール国王` (**our King of** Leclerc), both this chunk; and in the script dump `我ら　ルクレールの民は` (its people), `誉れ高き国、ルクレールよ！` (*Leclerc, the honoured country*), `ルクレール城` (its castle). **2 battle** (both this chunk — §9's "1" undercounts) **+ 4 script-unique.** The rendering is unchanged, so **no translated line needs revisiting** — the メルザリオ / ファリーナ / クリミア shape (§20.1, §2, §1). Alt *Luclere* |
| レバーク | `Ｌｅｖｅｒｋ` | **Promoted from §9 PROVISIONAL, taking the first of the two listed readings — and §9's description is CORRECTED the same way: a KINGDOM, not "a castle Maya has left".** 6 columns. Script-dump evidence: `予は　レバーク王` (*I am the King of Leverk*), `数百人のレバーク兵`, `東南の王国、レバークを解放した` (*liberated Leverk, the southeastern kingdom*), `レバーク城`, `レバークの広場`. **1 battle** (`レバークへ戻る`, this chunk) **+ 13 script-unique lines** — the PR body's 10 undercounts, which strengthens rather than weakens the case for settling it now. **`Ｒｅｂａｒｋ` rejected at review**, see §28.5. Alt *Leberk* |
| 国王 | `ｔｈｅ　Ｋｉｎｇ` | Capitalised on §2's 王女様 → *the Princess* precedent — a title an individual holds, per the §17.1 species test. 4 columns bare, 8 with the article. `私は、この国の国王です` → `Ｉ　ａｍ　ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｉｓ　ｌａｎｄ．`; `我がルクレール国王` → `ｏｕｒ　Ｋｉｎｇ　ｏｆ　Ｌｅｃｌｅｒｃ`. **6 battle** (4 of them this chunk, 2 in chunk 24) **+ 21 script-unique** — remeasured at review; the PR body's 4 + 10 counts only this chunk's own |
| 騎士団 (bare, of a kingdom's own) | `ｋｎｉｇｈｔｓ` | Lowercase common noun per the species test. `我が国の騎士団` → `Ｏｕｒ　ｋｎｉｇｈｔｓ`. **Distinct** from the named orders 紅の騎士団 → `Ｃｒｉｍｓｏｎ　Ｋｎｉｇｈｔｓ` (§2) and 黒の騎士団 → `Ｂｌａｃｋ　Ｋｎｉｇｈｔｓ` (§14.2), which are unaffected. Lowercase `ｋｎｉｇｈｔｓ` occurs nowhere else in `tl/` |
| 女隊長 | `ａ　ｗｏｍａｎ　ｃａｐｔａｉｎ` | Built on §2's 隊長 → captain; 女 marks the female form as it does for the classes in §4. Irvine on the captive Cress — and the line is also what fixes her sex |

### 28.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 指揮下 | **`ｃｏｍｍａｎｄ`** is the default; **`ｓｅｒｖｅ　ｕｎｄｅｒ`** is the possessive/width variant | ⚠️ **Recorded this way at review; the PR proposed `ｓｅｒｖｅ　ｕｎｄｅｒ` as the binding form and that would have forked a word already shipped twice.** Counted at review: `指揮下` occurs **6** times in `dumps/battle_dump.txt`, of which `指揮下に入る` is **one** — this chunk's own line. **Two of the six are already shipped and both render `ｃｏｍｍａｎｄ`**: `chunk_007.txt` L11 `黒の騎士団の指揮下だ。` → `ｕｎｄｅｒ　ｏｕｒ　ｃｏｍｍａｎｄ．` (and that one is the **enemy's** chain of command, not a squad member joining) and `chunk_014.txt` L3 `第９軍の指揮下に` / `入ります。` → `ｕｎｄｅｒ　ｔｈｅ　ｃｏｍｍａｎｄ　ｏｆ` / `ｔｈｅ　９ｔｈ　Ａｒｍｙ．` The remaining three are chunk 19's `では、俺たちの指揮下に入ってもらう`, untranslated. **CLAUDE.md §3 is not engaged** — three different source strings in three different messages (§20.4, §23.1, §24.5, §27.4) — so nothing is re-cut. `君の指揮下に入ろう。` → **`Ｉ　ｗｉｌｌ　ｓｅｒｖｅ　ｕｎｄｅｒ　ｙｏｕ．`** (23 columns) stands because the possessive form `ｃｏｍｅ　ｕｎｄｅｒ　ｙｏｕｒ　ｃｏｍｍａｎｄ．` measures **24** — remeasured at review, the PR body's 26 is two over — on a page already at 10 / 22 / 11 / 23. All three renderings share `ｕｎｄｅｒ`, so the family reads as one. **This is the §26.6 `らしい` shape: one default, one stated variant, recorded so it cannot drift.** Chunk 19 has room for `ｃｏｍｍａｎｄ` and should use it |
| 味方 | `ａｌｌｉｅｓ` | 6 columns. The boy's `だったら、味方だね。` → `Ｔｈｅｎ　ｙｏｕ’ｒｅ　ａｌｌｉｅｓ．` Kept **distinct** from 同盟 → *alliance* (§26.3) and 仲間 → *comrades* below |
| 仲間 | `ｃｏｍｒａｄｅｓ` | 8 columns. Four occurrences here across two speakers. Kept **distinct** from 部隊 → *squad* (§19.2) and 味方 → *allies*; `仲間同士で争う` → `ｆｉｇｈｔ　ｏｕｒ　ｏｗｎ` where the row will not take the noun. `ｃｏｍｒａｄｅｓ` occurs nowhere else in `tl/` |
| 解放 | `ｆｒｅｅ` (verb) | `この国の解放のために戦ってる` → `Ｗｅ’ｒｅ　ｆｉｇｈｔｉｎｇ　ｔｏ　ｆｒｅｅ　ｔｈｉｓ　ｌａｎｄ．` The noun *liberation* is 10 columns and will not share the row; the verb keeps the sense whole. 1 battle + 2 script |
| 他愛もない | `Ｈｏｗ　ｔｒｉｆｌｉｎｇ．` | Irvine on the 5th Army. 1 battle + 0 script |
| 上玉 (of a woman) | `ｔｈｅ　ｐｒｉｚｅ` | `なかなかの上玉ではないか。` → `Ｑｕｉｔｅ{FFFE}ｔｈｅ　ｐｒｉｚｅ，　ａｒｅ　ｙｏｕ　ｎｏｔ．` Objectifying, as the source is, and it sets up 献上 → *offer* two rows later. See §28.4. 1 battle + 0 script |
| 献上する | `ｏｆｆｅｒ` | 5 columns. Presenting as tribute to a superior — `ギルフォード将軍に献上してやる` → `Ｉ　ｓｈａｌｌ{FFFE}ｏｆｆｅｒ　ｙｏｕ　ｔｏ　Ｇｅｎｅｒａｌ{FFFE}Ｇｕｉｌｆｏｒｄ．` *Present* (8) does not fit the row |
| つべこべ言わず | `ｎｏ　ｍｏｒｅ　ｔａｌｋ` | Held clear of §14.5's ええい → `Ｅｎｏｕｇｈ！`, a different source string |
| 油断はするな | `Ｄｏ　ｎｏｔ　ｇｒｏｗ　ｃａｒｅｌｅｓｓ．` | 21 columns. Takes 油断 → *careless* from shipped `chunk_000.txt` L19 (`油断したか・・・` → `Ｗａｓ　Ｉ　ｃａｒｅｌｅｓｓ．．．`), so the word does not fork |
| お兄ちゃんたち (a child to a group) | `Ｍｉｓｔｅｒ，` (vocative) | The childish address has no English lexical equivalent, so §2's rule applies: carry it in word choice, once, as a vocative. The same solution §2 uses for トカゲさん → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ`. The plural survives in the next row's `Ｔｈｅｎ　ｙｏｕ’ｒｅ　ａｌｌｉｅｓ．` **Does not** touch §21.2's 〜さん-on-a-name rule |

### 28.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| あら、 | **`Ｍｙ，`** | 3 columns. A woman's mild, arch surprise. **Ratified at review, deliberately.** Deliberately **not** in the `Ｏｈ` family: §24.4 collapsed おお、/ ほう、 onto `Ｏｈ，` and おや onto `Ｏｈ？` outright, so `Ｏｈ` is spent and a fourth string cannot join them. `Ｍｙ` occurs **0** times elsewhere in `tl/`. ⚠️ **TWO CORRECTIONS to this row, 2026-09-09 (§4.3, PR #17 review) — see §35.1 and §35.2; the ruling stands unchanged and no rendering moves.** (a) Its reach was stated as "16 further occurrences (5 battle + 11 script-unique — both figures confirmed)"; **measured, it is 11 battle + 28 script-unique interjection instances = 39, i.e. 38 further than this one**. (b) ⚠️ **The alternative `Ｏｈ　ｍｙ，` was NOT free, and that sentence is struck: `chunk_011` L3 shipped `Ｏｈ　ｍｙ，` for `あら、` itself.** Retired by the wave-5 corrections unit (PR #17), after which `Ｏｈ　ｍｙ` occurs **0** times in `tl/` and `pending/`. `Ｍｙ，` is 3 columns to `Ｏｈ　ｍｙ，`'s 6, and あら is the milder of the pair |
| 馬鹿者！ (direct address) | `Ｙｏｕ　ｆｏｏｌ！` | **A fifth バカ register**, held apart from §19.1's そんなバカな → `Ｔｈａｔ’ｓ　ｉｍｐｏｓｓｉｂｌｅ` and バカなやつら → `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ`, §20.3's **バカ者** → `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ` (katakana, and *of* a third party) and §26.4's proverb. Same English root as §20.3 — this one is the vocative, and the kanji spelling is a different source string |
| ははっ！ | `Ｙｅｓ，　ｓｉｒ！` | 9 columns. The doubled, more emphatic military assent. **Distinct** from §6's はっ → `Ｓｉｒ`, which this chunk uses byte-identically **two segments earlier in the same message** — they genuinely stand side by side, so they must not collapse. ~~5~~ **4** battle + 1 script-unique **as a tic**, under §5's word-plus-source-punctuation mechanism (`ははっ・・・・！！` ch 16, `ははっ！！` ch 37, ~~`はははっっ！！` ch 38,~~ `ははっ・・・・` ch 42); the exact string `ははっ！` is 2 battle. ⚠️ **THE ch 38 ENTRY IS STRUCK — CORRECTED IN PLACE 2026-09-09 (§4.3, PR #33 review).** Chunk 38's string is **`はははっっ`**, and it was caught here as a *substring* `ははっ`. Read in context it is **Marana laughing while taunting the enemy, answering no one** — `Ｙｅｓ，　ｓｉｒ！！` there is nonsense — and it renders `Ｈａｈａｈａ！！` per §47.2. Verified at review over both dumps: `はははっ` is battle chunk **38 only, 0 script** — a hapax. **The four genuine instances are assents answering a superior's order (c13 L2, c16 L2, c37 L1, c42 L6) and this row's ruling for them is untouched and correct.** The §35.2 / §35.3 "a substring count is not a census" failure in a new place. ⚠️ **§29's `うん` co-occurrence argument cites this same list and is NOT disturbed**: `うん` is chunks 8, 20, 43, so striking 38 creates no overlap |
| まあよい、 | `Ｎｏ　ｍａｔｔｅｒ．` | 10 columns. A senior officer waving an objection aside. **Distinct** from §24.3's しかたねえ。 → `Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` (resignation) and §6's まったく → `Ｒｅａｌｌｙ，`. 2 battle + 0 script |
| 何っ！？ / 何ッ！？ | `Ｗｈａｔ！？` | 6 columns. ⚠️ **Corrected at review: the PR called this "a sixth member of the 何 family, all held apart", and it is not — `chunk_007.txt` L2 already ships the KATAKANA `何ッ！？` as `Ｗｈａｔ！？`.** The two are one full-width character apart, so they are different lookup keys and **CLAUDE.md §3 is not engaged** (the §24.5 / §27.4 shape). The collapse is the **documented** kind — one word, two kana spellings — which is exactly what §6 already does for 何だと？ / なんだと？, §6 for ふっ / フンッ and §17.2 for 鬼 / オーガ. §25.3's co-occurrence test is met: `何ッ！？` is chunk 7 only, `何っ！？` is chunks 13 and 18, and **no chunk holds both**. Chunk 7 has first use. The rest of the 何 family is still held apart: 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？` (§23.2), あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2), and chunk 0's two stuttered forms (§23.2) |
| 分かってる・・・ | `Ｉ　ｋｎｏｗ．．．` | 9 columns. The **progressive** form — a sixth member of the わかる family: いいな！！ → `Ｇｏｔ　ｉｔ！！`, わかったなっ！！ → `Ｇｏｔ　ｔｈａｔ！！`, 分かった / よし、 → `Ｒｉｇｈｔ，` (§6, §24.3), わかりました。 → `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` (§21.2), 了解 → `Ｕｎｄｅｒｓｔｏｏｄ` (§21.2). This chunk's `わかった・・・・。` takes §6's `Ｒｉｇｈｔ` with the source's own five stops, per §5 |
| 確かに、 | `Ｔｒｕｌｙ，` | 6 columns. Conceding a point. **Distinct** from §20.3's まったくだっ！ → `Ｉｎｄｅｅｄ　ｗｅ　ｈａｖｅ！` and §25.2's そのとおりだ。 → `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`; `Ｃｅｒｔａｉｎｌｙ` is 10 and puts the row at 26 |
| あいにく | `Ｓｏｒｒｙ，` | 6 columns. The Leclerc soldier's hedge before refusing to fight. **Distinct** from 残念ながら → `Ｉ　ａｍ　ｓｏｒｒｙ　ｔｏ　ｓａｙ` (chunk 6, formal register). ⚠️ **Recorded at review, and the PR did not raise it: this shares its English with shipped `ごめんね、`** — `chunk_010.txt` L10 and L12 both render `ごめんね、トカゲさん。` as `Ｓｏｒｒｙ，　Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ．` Two different source words on one English hedge. §3 is not engaged and §25.3's test is met (chunks 10 and 13 never meet); the alternative is width-blocked — `Ｕｎｆｏｒｔｕｎａｔｅｌｙ，` is 16 and puts that row at 28. Recorded so it cannot drift |

### 28.4 The `さんざんいたぶった後` / `上玉` scene — translated at the source's own temperature

Message line 1 page 4 is a threat of sexual menace: Irvine tells the captive he will hand her to
General Guilford `さんざんいたぶった後`, having called her `なかなかの上玉`. It is rendered
`Ａｆｔｅｒ　Ｉ　ｈａｖｅ　ｔｏｒｍｅｎｔｅｄ{FFFE}ｙｏｕ　ｗｅｌｌ，` and `Ｑｕｉｔｅ{FFFE}ｔｈｅ　ｐｒｉｚｅ，
ａｒｅ　ｙｏｕ　ｎｏｔ．` — **neither softened nor sharpened**, and `ｔｈｅ　ｐｒｉｚｅ` is chosen to keep
the objectification the scene turns on. The PR raised this itself rather than leaving it silent
(its Flag 11) and the decision is ratified at review. Recorded here so it reads as a decision, not
an oversight, to anyone who meets the line later.

### 28.5 Ruling — `レバーク` takes `Ｌｅｖｅｒｋ`, and `Ｒｅｂａｒｋ` is rejected

§9 offered two readings and this is the first-use promotion, so it is settled here rather than
drifting. **`Ｌｅｖｅｒｋ`.** Three reasons, in order of weight:

1. **`Ｒｅｂａｒｋ` reads as an English common word**, which is the failure mode §17.2 avoided for
   `Ｎｅｒｇａｌｉ` (not *Nergal*) and §1 avoided for `Ｌｅｏｎ` (not *Lion*, "would read as the
   animal"). This is a **kingdom whose king announces himself** — `予は　レバーク王` — which is the
   worst possible place for a name that reads as a verb.
2. **The European-reading convention** every other name in this project follows (§11.4, §14,
   §17.3): Bauer, Carline, Helfer, Albert, Fernando, Anselmo, Korneff, Kazarov, Percival, Creus.
   `Ｌｅｖｅｒｋ` sits in that set; `Ｒｅｂａｒｋ` does not.
3. It sits beside `Ｌｅｃｌｅｒｃ` in this very chunk — Cress leaves one kingdom for the other in
   consecutive scenes — and the two must read as peers.

**Reach, remeasured at review: 1 battle + 13 script-unique lines**, including a whole later scene
with its own King (`予は　レバーク王`, `レバーク城`, `レバークの広場`, `東南の王国、レバークを解放した`).
After this merge, changing it is a §4.3 correction. Alt *Leberk* recorded and not taken.

### 28.6 Register

| Who | Register |
|---|---|
| Lord Irvine (portrait 07) | Haughty, archaic, **no contractions** — `その方` / `〜しておれ` / `おったから` carried by `Ｙｏｕ　ｔｈｅｒｅ．`, `Ａｗａｉｔ　ｉｔ．`, `ｗａｓ　ｉｔ　ｎｏｔ．`, `ａｒｅ　ｙｏｕ　ｎｏｔ．` His only apostrophe in the chunk is the possessive `Ｃａｒｌｉｎｅ’ｓ`. §14.6 / §20.5 / §25.5's Imperial officers, unchanged, with the added cruelty of §28.4 |
| His subordinate (portrait 08) | Deferential, no contractions — `Ｓｉｒ！`, `Ｈｏｗｅｖｅｒ，`, `ｔｈｅｙ　ａｒｅ　ｒｉｇｈｔ　ｔｈｅｒｅ．．．`, `Ｙｅｓ，　ｓｉｒ！`. Albert's shape (§20.5) |
| **Cress (portrait 09)** | ⚠️ **Crisply formal and military, no contractions — §7's Beatrice column.** `Ｉ　ｓｈａｌｌ　ｒｅｔｕｒｎ`, `Ｄｏ　ｎｏｔ　ｇｒｏｗ　ｃａｒｅｌｅｓｓ．`, `Ｗｅｌｌ　ｔｈｅｎ，　ｆａｒｅｗｅｌｌ．`, `Ｌｅｔ　ｍｅ　ｓａｙ　ｏｎｅ　ｗｏｒｄ　ｏｆ　ｔｈａｎｋｓ．` **The speaker identification was verified from the tag stream at review, not assumed** — see §28.7 |
| The King (portrait 04) | Old-fashioned and grateful, **no contractions** — `おった` / `のです` carried by `Ｉ　ａｍ　ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｉｓ　ｌａｎｄ．`, `Ｉ　ｈａｄ　ｇｉｖｅｎ　ｕｐ，`, `Ｏｕｒ　ｌａｎｄ　ｗｉｌｌ　ｗｅｌｃｏｍｅ　ｙｏｕ`. §7's "Village elders (じゃ / のう)" row: plain and old-fashioned, never archaic spelling |
| The Leclerc soldier (portrait 02) | Formal and stiff at first, **no contractions** — `Ｗｈｏｓｅ　ｓｏｌｄｉｅｒ　Ｉ　ａｍ　ｉｓ　ｎｏ　ｃｏｎｃｅｒｎ　ｏｆ　ｙｏｕｒｓ．` — and unchanged when he yields: `Ｔｒｕｌｙ，`, `Ｉ　ｗｉｌｌ　ｓｅｒｖｅ　ｕｎｄｅｒ　ｙｏｕ．` The concession is in what he says, not in how he says it |
| The boy (portrait 03) | Childish and eager, contractions throughout — `Ｉ’ｌｌ　ｒｉｄｅ　ａ　ｈｏｒｓｅ`, `ｙｏｕ’ｒｅ　ａｌｌｉｅｓ`, `Ｈｅｒｅ，　ｔｈｉｓ　ｉｓ　ｆｏｒ　ｙｏｕ．` `Ｍｉｓｔｅｒ，` is his |
| The 9th Army (portraits 00, 05, and message line 8's `{FC50}` side) | §7 unchanged — casual, contractions throughout: `Ｉ　ｃｏｕｌｄｎ’ｔ`, `Ｓｈｅ’ｓ　ｇｏｔ　ａ　ｃｕｔｅ　ｓｉｄｅ，　ｈａｓｎ’ｔ　ｓｈｅ．`, `Ａｒｅｎ’ｔ`, `ｗｏｎ’ｔ`, `Ｗｅ’ｒｅ`, `Ｉ’ｖｅ`. The deliberate contrast that makes Irvine's and Cress's flatness read as rank. `Ｗｅ　ｗｉｌｌ　ｓａｖｅ　ｔｈｅ　Ｋｉｎｇ，` is uncontracted **for the emphatic 必ず**, not a slip |
| The unnamed female companion (portrait 06) | Casual and arch — `Ｍｙ，　ｗｈａｔ　ａ　ｈａｒｓｈ　ｔｈｉｎｇ　ｔｏ　ｓａｙ．` Same shape as §21.4's and §25.5's unnamed female party member. **If a later chunk names her, all three want re-checking together** |
| Tutorial box (`{=FA1000300030}`, message line 7) | §7 unchanged — plain instructional second person, byte-identical to §27.2 |

### 28.7 The portrait-09 reading, verified from the tag stream

Flag 8 asked the reviewer to sanity-check this, and it decides four pages of register, so the
check is recorded rather than left implicit. **Portrait 09 is Cress on both channels**, the §23.5
same-id / opposite-channel-byte pattern already recorded for chunk 4's Ridge:

- Irvine names the captive in message line 1 page 2 — `その方、クレスと申したな。` — and the reply
  `くっ・・・` comes on `{FCB0}{=00090001}{FC51}`. Message line 2's `あれは、９軍？` is the same id
  and the same channel.
- Message line 4 opens `{FCB0}{=00090000}{FC50}`, and **portrait 09 then holds the `{FC50}` channel
  for the whole farewell**: pages 3, 5, 6, 7 and 8 carry no new `{FCB0}`, so they revert to 09.
- Irvine's `女隊長と聞いておったから` independently fixes the captive as female, which agrees with
  §1's Cress row (少尉, court-martialled alongside Alfred).

So Cress speaks line 1 page 5, line 2 page 6, and all of line 4's farewell — which is what puts her
in the no-contraction military column beside Beatrice. **Nothing in the chunk names the King or
states his kingdom** (`私は、この国の国王です` only), and the English deliberately commits to
neither: `ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｉｓ　ｌａｎｄ` and `ｏｕｒ　Ｋｉｎｇ　ｏｆ　Ｌｅｃｌｅｒｃ` each render
exactly what their own line says. See `FLAGS.md` §P.

### 28.8 `FLAGS.md` §O7's five dropped wave-1 rows — written, not lapsed a third time

`FLAGS.md` §O7 hands these to "whoever owns the next glossary integration". That is this
integration, and **chunk 13 renders one of them**, which is what settles it. All five are already
shipped in `tl/`; these rows record the shipped form, they do not change it.

| Japanese | English | Note |
|---|---|---|
| さあ、 | **`Ｎｏｗ，`** | ⚠️ **Settled here. Chunk 13 is the THIRD shipped file to agree** — `さあ、つべこべ言わず` → `Ｎｏｗ，　ｎｏ　ｍｏｒｅ　ｔａｌｋ．`, beside `chunk_006` L12 and `chunk_033` L20, which ship the bare segment as `Ｎｏｗ，`. **16 battle + 10 script-unique occurrences**, so this is the largest single drift risk §O7 listed. Two row-level variants stand and are **not** re-cut: `chunk_011` L3's `さあ、私のかわいい` → `Ｎｏｗ　ｔｈｅｎ，　ｍｙ　ｄａｒｌｉｎｇ` (a longer vocative follows), and `chunk_003` L4's `さあ、{FC00}{=0000}、` → `Ｃｏｍｅ　ｏｎ，　{FC00}{=0000}，`, which **§24.5 already rules is a different row** because the name insert is inside it. Held **distinct** from Fernando's `さ、` → `Ｃｏｍｅ，` (§24.6) |
| ヘビー | `ｈｅａｖｙ` | Shipped `ちょっとヘビーだぜ。` → `ａ　ｂｉｔ　ｈｅａｖｙ．`, `chunk_003` file L6. **1 battle / 0 script.** A hapax; the row exists so the loanword cannot be re-invented |
| 洞窟 | `ｃａｖｅ` / `ｃａｖｅｓ` | Shipped in `chunk_003` file L6. **5 battle / 0 script** |
| 赤い屋根の家 / 赤い屋根の建物 | `ｒｅｄ‐ｒｏｏｆｅｄ　ｈｏｕｓｅｓ` / `ｒｅｄ‐ｒｏｏｆｅｄ　ｂｕｉｌｄｉｎｇｓ` | Shipped in `chunk_003` file L6, both forms. Uses `‐` (U+2010). **2 battle / 0 script.** The two are kept apart because the source keeps them apart |
| 謹慎中 / 謹慎がとける | `ｕｎｄｅｒ　ｃｏｎｆｉｎｅｍｅｎｔ` / `ｃｏｎｆｉｎｅｍｅｎｔ　ｅｎｄｅｄ` | The **noun** forms, shipped in `chunk_003` file L5. §19.2 records only the adjective `謹慎処分を受ける` → `ｃｏｎｆｉｎｅｄ` (`chunk_001`), which is unchanged. One word, three grammatical shapes the source itself varies — the §27.1 `愛用` pattern. **4 battle / 1 script** |

**§O7 is now DISCHARGED.** Bare `隊` → squad is the one entry not written: it has **no** shipped
rendering and **no** occurrence to point at (§O7's own row lists neither), so there is nothing to
fix, and the rejection is recorded here in terms, as §O7 asked.

---

## 29. Added by chunk 008 (PR #11, merged 2026-09-08)

Rendered in `tl/battle/chunk_008.txt` — chapter 8, five scenes: Alfred hands the 9th Army the
rearguard while the 7th and 5th Armies move out ahead, over Second Lieutenant Cress's doubts; the
battle opens; on the Imperial side the transport **Cargo** loses motive power while escorting the
prisoner **Seneca**, and its captain gives the battle plan; Seneca escapes and the captain counts
his pay cut; afterwards the squad takes stock of the cart-monster, Seneca returns, and they agree
to take him to Westbury. **7,437 / 8,192 bytes, slack 755 — 185 rows, widest 23, none at 24**, no
page over 4 text rows. Merged at **round 2**; both round-1 findings were reading findings, and the
rework was **byte-neutral**.

⚠️ **Line numbers in this section are `rowcheck` line numbers** — the index into the `tl/` file
counting the `=== CHUNK` header as line 0, which is what `rowcheck.py 8` prints. That is a
*fourth* numbering convention in this repo (`FLAGS.md` §O8, §P): it is the chunk-13 section's
message line **plus one**. Locate by content.

`Ｉ　ａｍ　ｓａｖｅｄ` (§23.4's stated default, and §23.4 named chunk 8 as one of the chunks the family
would reach), `Ｈｏｗｅｖｅｒ，` (§23.3), `Ｒｉｇｈｔ，` for `よし、` (§24.3), `Ｌｉｓｔｅｎ．` (prompt §5),
`Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ` (§24.3), `Ｐｈｅｗ，` / `Ｓｉｒ！` / `Ｙｅａｈ．` / `Ｅｈ？` (§6, §21.2),
`Ｎｏ，` (§25.2), `Ｇａｈ` (§21.2), `Ｔｃｈ` (§11.5), `ｍｏｎｓｔｅｒ` (§25.1), `ｃｏｍｂａｔ　ｐｏｗｅｒ` /
`ｍｏｂｉｌｉｔｙ` (§4), `Ｃａｐｔａｉｎ` / `ｔｈｅ　ｍａｉｎ　ｆｏｒｃｅ` / `Ｒｏｙａｌ　Ａｒｍｙ` (§2) and
`ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` (§20.4's default, used for **all four** `帝国軍`) are used unchanged.
`Ｗ，　Ｗｅｌｌ，` is the third use of §24.3's comma-stutter.

### 29.1 People and places — four promotions out of §9, and one row deliberately left live

| Japanese | English | Note |
|---|---|---|
| シェルビー | `Ｓｈｅｌｂｙ` | **Promoted from §9 (wave-3 seed), used exactly as seeded.** 6 columns. A **place** — the country town where the Empire built a weapons plant, which Seneca fled. **4 battle (all this chunk) + 1 script.** Alt *Shelbey*, *Sherbie* |
| カーゴ | `Ｃａｒｇｏ` | **Promoted from §9, used exactly as seeded.** 5 columns. ⚠️ **A proper name — the Imperial transport machine, never `ｔｈｅ　ｃａｒｇｏ`.** The trap §9 warned about was avoided: both renderings are possessive (`Ｃａｒｇｏ’ｓ　ｍｏｔｉｖｅ　ｐｏｗｅｒ`, `Ｃａｒｇｏ’ｓ　ｍｅｃｈａｎｉｓｍ`), which is only grammatical for a name. It is the `荷車のバケモノ` the squad picks apart afterwards, and the party rule `カーゴは、他のキャラクターとの混在はできません。` makes it a deployable unit. **2 battle + 1 script** |
| プロキオン | `Ｐｒｏｃｙｏｎ` | **Promoted from §9, used exactly as seeded.** 7 columns. A named deployable unit, not a person — `いざとなったら、プロキオンを出してもいい` → `Ｉｆ　ｎｅｅｄ　ｂｅ，　ｙｏｕ{FFFE}ｍａｙ　ｓｅｎｄ　ｏｕｔ　Ｐｒｏｃｙｏｎ．` **1 battle + 0 script** |
| スパイ | `ｓｐｙ` | **Promoted from §9, used exactly as seeded.** 3 columns, lowercase common noun per the §17.1 species test. Twice in one scene, both this chunk |
| ルート | `ｒｏｕｔｅ` | ⚠️ **RENDERED here twice — `進攻ルート` → `ａｄｖａｎｃｅ　ｒｏｕｔｅ`, `本来のルート` → `ｐｒｏｐｅｒ　ｒｏｕｔｅ` — exactly as seeded, and its §9 row is DELIBERATELY NOT STRUCK.** Chunk 17 (PR #12) renders it as well and merges second; the wave's cross-unit rule strikes such a row once, at the second merge, so that reviewer owns it. Lowercase confirmed in both units at this review |
| 兵器工場 | `ｗｅａｐｏｎｓ　ｐｌａｎｔ` | 14 columns. ⚠️ **Recorded with its measured reason, which the PR body left resting on the seed's wording.** `ａ　ｗｅａｐｏｎｓ　ｆａｃｔｏｒｙ　ｔｈｅｒｅ．` measures **exactly 24** — remeasured at review — which §25.1 has twice rejected, so `ｐｌａｎｔ` is a §2.1 step 4 shortening, not a free choice. Held **distinct** from bare `工場` → *factory* (`chunk_009.txt`, twice): different source strings, and counted at review `兵器工場` is **1 battle / 0 script** against bare `工場`'s 3, so the two can never collide in one line |
| 先発隊 | `ａｄｖａｎｃｅ　ｐａｒｔｙ` | 14 columns. A **fourth** unit word, kept distinct from 本隊 → *the main force* (§2, and both occur in this one speech), 主力部隊 → *the main body* (§20.1) and 精鋭部隊 → *elite corps* (§2) |
| 動力 | `ｍｏｔｉｖｅ　ｐｏｗｅｒ` | 12 columns. Kept distinct from 戦闘力 → *combat power* and 機動力 → *mobility* (§4) — **all three occur in this chunk**, which is why none may collapse |
| 機構 | `ｍｅｃｈａｎｉｓｍ` | 9 columns. `カーゴの機構` — the §9 seed's own gloss |

### 29.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 夢のまた夢 | `ａ　ｄｒｅａｍ　ｗｉｔｈｉｎ　ａ　ｄｒｅａｍ` | Literal, and a real English phrase, so §2's ban on importing an unrelated idiom is not engaged. `ａ　ｐｉｐｅ　ｄｒｅａｍ` was rejected by the translator on exactly that rule |
| 覚悟はしてる | `Ｉ’ｍ　ｒｅａｄｙ　ｆｏｒ　ｉｔ` | Seneca accepting the danger of travelling with the squad |
| 貴官らの隊 | `ｙｏｕｒ　ｓｑｕａｄ` | `貴官` is carried in **register**, not in an added word — Cress's contraction-free speech does the work, per §2 and the treatment §26.7 records for script 993's `貴官ら`. Does not disturb §19.2's 部隊 → *squad* |
| 大減棒 (＝ 大減俸) | `ａ　ｂｉｇ　ｐａｙ　ｃｕｔ` | ⚠️ **A source typo, ruled at review: `減棒` is not a word and `減俸` (a cut in pay) is.** Counted: **1 occurrence in `battle_dump.txt`** (this line) and **0 in `script_unique.txt`** — a hapax, so nothing else is affected. Rendered for the meaning the scene requires of an officer who has just lost his prisoner. `FLAGS.md` §Q4 |
| ついてねえぜ。 | `Ｊｕｓｔ　ｍｙ　ｌｕｃｋ．` | 13 columns. Twice, byte-identical (L7 and L14), one speaker — which is what the escort captain's two death/failure beats need. The related `ほんとについてねえなあ。` is a **different string** and keeps its intensifier: `Ｉ　ｒｅａｌｌｙ　ｈａｖｅ　ｎｏ　ｌｕｃｋ　ｅｉｔｈｅｒ．`, with `ｅｉｔｈｅｒ` rendering `俺も` |

### 29.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| やれやれ、 | `Ｇｏｏｄ　ｇｒｉｅｆ，` | 12 columns. Weary exasperation. **Distinct** from §6's まったく → `Ｒｅａｌｌｙ，` (contempt), ふう → `Ｐｈｅｗ，` (relief) and ふっ / フンッ → `Ｈｍｐｈ` (scoff). Free across `tl/` |
| くーっ、 / く〜っ、 | `Ｔｃｈｈ，` | 5 columns. The **lengthened** `くっ` → `Ｔｃｈ` (§11.5), the extra beat taking an extra letter as §26.5's ふーむ → `Ｈｍｍ` extends む → `Ｈｍ`. The two source spellings (`ー` and `〜`) take one English form per §17.2's 鬼 / オーガ; both are the same speaker, L10 and L14 |
| うーん、 | `Ｈｍｍ，` | 4 columns. The musing hum. Shares §26.5's ふーむ → `Ｈｍｍ，` deliberately — same length, same act — and §25.3's test is met: `ふーむ` is in script bank 31, `うーん` in battle chunk 8, so no scene shows both |
| あの・・・ | `Ｕｍ．．．` | 5 columns. Seneca's hesitant opener, twice (L9, L15), byte-identical. Held apart from §24.3's すいません。 → `Ｅｘｃｕｓｅ　ｍｅ．` and ちょっと、 → `Ｈｏｌｄ　ｏｎ，`, exactly as §24.3 holds those two apart |
| それに、 | `Ｂｅｓｉｄｅｓ，` | 9 columns. **Additive, not adversative**, and that is why it does not join the four already fixed: でも → `Ｂｕｔ`, それにしても → `Ｓｔｉｌｌ，` (§19.1), しかし / しかしながら → `Ｈｏｗｅｖｅｒ，` (§23.3), それでも → `Ｅｖｅｎ　ｓｏ，` (§25.2). Twice here, byte-identical. ⚠️ Note for duplicate checks: this chunk also contains `それでもいいかい？`, which is それ + でも and **not** §25.2's それでも — correctly not rendered `Ｅｖｅｎ　ｓｏ` |
| うん、 | `Ｙｅｓ，` | 5 columns. Seneca's soft assent. ⚠️ **Recorded with the licence that actually applies, not the PR body's.** §18.3 freed `Ｙｅｓ` from `ああ` **only**; `Ｙｅｓ` already carries `ええ。` → `Ｙｅｓ．` (`chunk_007` L19), `そうだ、` → `Ｙｅｓ，` (`chunk_000` L3) and now `ははっ！` → `Ｙｅｓ，　ｓｉｒ！` (§28.3). What licenses a fourth is §25.3's co-occurrence test, counted across `battle_dump.txt` at this review: `うん` in chunks 8, 20, 43; `ええ` in 7, 19, 32; `そうだ、` in 0, 5, 24, 39; `ははっ` in 13, 16, 37, 38, 42 — **no chunk contains うん with any of the other three.** Distinct from §6's ああ → `Ｙｅａｈ`, which this chunk also carries three times |
| げッ！？ | `Ｇａｈ！？` | §21.2's げっ → `Ｇａｈ` carrying the source's own punctuation — §5's mechanism, not a second entry |
| そ、それが、 | `Ｗ，　Ｗｅｌｌ，` | 8 columns. §24.3's comma-stutter form, after `ま、待て！` → `Ｗ，　Ｗａｉｔ！` and `chunk_007`'s `バ、バカな・・・` → `Ｉｍ，　Ｉｍｐｏｓｓｉｂｌｅ．．．` (§19.1) |
| 仕方ねえだろ。 | `Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` | A **third** member of §24.3's family beside しかたねえ。 and 仕方ない、 (both shipped in `chunk_006`, and 仕方ない、 also here at L10). The fixed word plus the source's own stop, which is §5's mechanism. `だろ` is carried in register: the tag question `Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ，　ｉｓ　ｔｈｅｒｅ．` measures **25** and does not fit |

### 29.4 Ruling — `よし、わかった。` collides `Ｒｉｇｈｔ，` with itself, and the reserve is fixed now

§24.3 fixes `よし、` → `Ｒｉｇｈｔ，` and §6 fixes `分かった` / `わかった` → `Ｒｉｇｈｔ，`; §25.3 ratifies
that sharing as deliberate. **Chunk 8 puts both words in one segment** — the first genuine
co-occurrence in the project — which §25.3 says forces a split but for which it names no reserve.

**Ruled: `よし、` keeps its fixed `Ｒｉｇｈｔ，` and `わかった` takes the reserve, giving
`Ｒｉｇｈｔ，　ｕｎｄｅｒｓｔｏｏｄ．` (18 columns).** §25.3's own test is met for this unit — counted
across `battle_dump.txt` at review, `了解` occurs in chunks **3, 17 and 19** and `わかった` in
**0, 5, 8, 13, 16, 18, 19, 22, 24, 27, 38 and 43**, so chunk 8 carries `わかった` and no `了解` and
the collision with §21.2's 了解 → `Ｕｎｄｅｒｓｔｏｏｄ` can never be visible in one scene. The wave
corroborates it three ways: `pending/chunk_017.txt` L6 (PR #12) renders `了解！よし、` as
`Ｕｎｄｅｒｓｔｏｏｄ！Ｒｉｇｈｔ，`, `tl/battle/chunk_013.txt` L8 (PR #10) keeps bare `わかった・・・・。`
as `Ｒｉｇｈｔ．．．．．` per §6, and this chunk splits the collided pair.

⚠️ **The test FAILS in chunk 19, which is why the reserve is written now rather than invented
later.** Chunk 19 contains **both** — bare `了解。` at message line 19 and `・・・わかった。` at line 24,
two lines of one map, both visible to a player.

> **A `わかった` standing beside `了解` takes `Ａｇｒｅｅｄ．` (7 columns).** `了解` keeps
> `Ｕｎｄｅｒｓｔｏｏｄ` — it is the older fixed entry (§21.2), is shipped in `chunk_003.txt` and ships
> again in chunk 17. `Ａｇｒｅｅｄ` is **verified free across all of `tl/`** at this review, checked
> again after PR #10 merged. The near neighbours are not free: `Ｉ　ｓｅｅ．` is spent in chunks 3, 4,
> 7 and 33, `Ｖｅｒｙ　ｗｅｌｌ` in 33 and 35, `Ｉ　ｋｎｏｗ．．．` in chunk 13 (§28.3), and §25.3 has
> already reserved `Ｅｘａｃｔｌｙ．` for `そのとおり` / `そうそう`.

**This makes the わかる family eight English forms wide**, extending §28.3's enumeration of six:
いいな！！ → `Ｇｏｔ　ｉｔ！！`, わかったなっ！！ → `Ｇｏｔ　ｔｈａｔ！！`, 分かった / わかった / よし、 →
`Ｒｉｇｈｔ，` (§6, §24.3), わかっておるな！ → `Ｉｓ　ｔｈａｔ　ｃｌｅａｒ！` (§20.3), わかりました。 →
`Ｉ　ｕｎｄｅｒｓｔａｎｄ．` (§21.2), 了解 → `Ｕｎｄｅｒｓｔｏｏｄ` (§21.2), 分かってる・・・ →
`Ｉ　ｋｎｏｗ．．．` (§28.3), and **わかった-beside-了解 → `Ａｇｒｅｅｄ．` (here)**.
**Lines this affects: none.** Nothing shipped is re-cut; the reserve applies only to a future unit.

### 29.5 CORRECTION to §1 and §2 (§4.3) — `少尉` is 17 columns, and "never on one row" is not quite true

§1's Cress row says `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ` is “18+5 columns, never on one row”,
and §2's 少尉 row says “18 columns”. **Both figures are one over.** Measured at this review:
`Ｓｅｃｏｎｄ` is 6, the space 1, `Ｌｉｅｕｔｅｎａｎｔ` 10, so `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` is **17**
and `Ｃｒｅｓｓ` is **5**. The translator caught this in the PR's Flag 4 and it is right.

The consequence is sharper than the note admits, so it is recorded rather than quietly patched:
**`Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ` is 23 columns and *would* fit one row**, so §1's blanket
“never on one row” is false as written. What makes it not fit here is the **vocative comma** —
`Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ，` is **24** — and the vocative is the only shape either
dump renders so far, so chunk 8's split across two rows stands and **no shipped line changes.**

**Read §1's row as:** 17 + 5 columns; 23 as a bare name, **24 with a following mark**, so it will
not share a row in the vocative, which is the only form yet seen.

⚠️ **§2's 中尉 → `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ` “17 columns” is the same arithmetic error** —
`Ｆｉｒｓｔ` is 5, so it is **16**, and `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` would be 25 and still
will not share a row. Flagged, not changed: nothing renders it yet, and the ruling it supports is
unaffected. Whoever first renders 中尉 should correct the figure in place.

### 29.6 Register

| Who | Register |
|---|---|
| Alfred (portrait 0005, `{FC50}`) | Senior and easy, the officer handing out an unwelcome job pleasantly — `Ｗｅｌｌ　ｔｈｅｎ，`, `Ａｎｄ　ｓｏ，`, `ｔｈｅ　ｒｅａｒｇｕａｒｄ　ｉｓ　ｙｏｕｒｓ．` Fixed by the next speaker naming him. §1's `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ａｌｆｒｅｄ` is **not** used — the source writes the bare `アルフレッド` everywhere in this chunk |
| Cress (portrait 0006, `{FC51}`) | Crisply formal, **no contraction anywhere** — `ｉｓ　ｔｈｉｓ　ａｌｌ　ｒｉｇｈｔ？`, `Ｄｏ　ｎｏｔ　ｐｕｓｈ　ｔｏｏ　ｈａｒｄ．`, and the `貴官` of §29.2 carried there rather than in a word. §28.7's reading of her — the no-contraction military column beside Beatrice — is confirmed independently here, in her first scene under her own name |
| The escort captain (portrait 0008) | Rough, unlucky and profane-adjacent; contractions (`Ｗｈａｔ’ｓ　ｗｒｏｎｇ．`, `ｉｔ’ｓ　ｆｉｘｅｄ？`, `ｗｅ’ｌｌ　ｉｎｔｅｒｃｅｐｔ`). **One voice across four separate messages** — he asks what is wrong (L10), gives the battle plan, dies (L7) and curses the escape (L14) — which is why `ついてねえぜ。` is byte-identical in L7 and L14. Commands in the bare imperative, like §25.5's Krippen, but complains like Ridge |
| His subordinate (portrait 0003) | Deferential and rattled, **no contractions** — `Ｗ，　Ｗｅｌｌ，`, `Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ．`, `ｙｏｕ　ｓｅｅ．．．`. Albert's shape (§20.5), and the same column §28.6 puts Irvine's man in |
| Seneca (portrait 0007) | §25.5 unchanged and confirmed three chapters earlier than it was written: quiet, hesitant, contractions (`Ｉ’ｍ　Ｓｅｎｅｃａ．`, `Ｉ　ｗｏｎ’ｔ　ｇｅｔ　ｉｎ`), opening twice with `Ｕｍ．．．`. His one formal row is `Ｉ　ａｍ　ｓａｖｅｄ．．．`, which is §23.4's fixed form and not a register slip |
| The 9th Army squad (portraits 0000, 0001, 0002, 0009, 000A) | §7, §21.4 and §25.5 unchanged — casual, contractions throughout, tag questions from the women (`ｄｏｅｓｎ’ｔ　ｉｔ．`, `ｄｏｅｓｎ’ｔ　ｉｔ？`, `ｄｉｄｎ’ｔ　ｔｈｅｙ．`). Portrait 0001 is the Ridge-shaped blunt one who needles about the spy and concedes `．．．Ｗｅｌｌ，　ｆｉｎｅ．`; his `Ｈｏｗｅｖｅｒ，` is §23.3 binding **over** register, as chunk 9 already does |
| The young companion (portrait 0002) | Her `てーこく` (a clipped, childish `帝国`) and `バケモノ` are carried in register, not spelled out — §2's rule — and her register is already doing it through contractions and tag questions |

---

## 30. Added by chunk 017 (PR #12, PARKED 2026-09-08)

Rendered in **`pending/chunk_017.txt`** — chapter 17, the defence of the fortress. Five scenes:
Rendol reports a Carline raid from the west and Rimul works out they crossed the Basilisk Desert;
Burgess falls silent and she reads it as Ifrit taken; she refuses to recall the Crossley garrison,
calls on Commander Krippen and wakes Original Unit 1; Mamu promises a grieving woman he will avenge
her sister; three alternative withdrawal outcomes; a villager's gift; and the death/spare lines.
**5,857 / 8,192 bytes, slack 2,335 — 154 rows, widest 23, none at 24**, no page over 4 text rows.
Merged at **round 2**; both round-1 findings were reading findings and the rework was **−16 bytes**.

⚠️ **THIS UNIT IS PARKED, AND NOT FOR BUDGET.** It is 2,335 bytes under its slot at 2.16× against a
3.19× ceiling. It cannot ship because message 19's item-grant tail carries the `FLAGS.md` §D1 dump
artifact and the charset and tag-parity gates are unsatisfiable together — `FLAGS.md` §R has the
proof, the scope and the unpark recipe. **The rows below are decided and binding now**, exactly as
if the file were in `tl/`: it will move with a `git mv` and a 0-byte re-tokenisation, and nobody
will re-read it when that happens.

⚠️ **Line numbers in this section are MESSAGE lines** (dump body index, 1-based) = the `tl/` file
line **minus one**, the §28 convention. That is the third of the four numbering conventions in this
repo (`FLAGS.md` §O8, §P, glossary §29). **Locate by content.**

`Ｌａｄｙ　Ｒｉｍｕｌ` / `Ｒｅｎｄｏｌ` (§1), `Ｃａｒｌｉｎｅ` / `Ｃｒｉｍｓｏｎ　Ｋｎｉｇｈｔｓ` / `ｆｏｒｔｒｅｓｓ` /
`ｇａｒｒｉｓｏｎ` / `９ｔｈ　Ａｒｍｙ` / `ｔｈｅ　Ｂａｓｉｌｉｓｋ　Ｄｅｓｅｒｔ` / `ｔｈｅ　Ｅｍｐｉｒｅ` (§2),
`Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ` / `Ａｌｌ　ｕｎｉｔｓ` (§25.1), `Ｏｒｉｇｉｎａｌ　Ｕｎｉｔ　１` (§17.2),
`Ｒｉｇｈｔ，` (§24.3), `Ｕｎｄｅｒｓｔｏｏｄ！` (§21.2), `Ｓｉｒ` / `Ｈｍｐｈ` / `Ａｈ，` (§6), `Ｔｃｈ`
(§11.5), `Ｇｕｆｆ` (§14.5), `Ｈｏｗｅｖｅｒ，` (§23.3 — its **sixth** use), `ｏｄｄ　ｓｏｒｔｓ` (§24.2),
`ｒｅｃｋｌｅｓｓ` (shipped `batch_002`) and `Ｔｈｅ　ｖｉｌｌａｇｅ　ｉｓ{FFFE}ｕｎｄｅｒ　ａｔｔａｃｋ．` (§27.2)
are used unchanged. `了解！よし、` → `Ｕｎｄｅｒｓｔｏｏｄ！Ｒｉｇｈｔ，` is the case **§29.4 anticipated**,
and `わかった` is confirmed absent from this chunk, so §29.4's `Ａｇｒｅｅｄ．` reserve is not engaged.

### 30.1 People and places — six promotions out of §9, and the cross-unit row struck

| Japanese | English | Note |
|---|---|---|
| クロスリー | `Ｃｒｏｓｓｌｅｙ` | **Promoted from §9, used exactly as seeded.** 8 columns. A **place**, used only locationally here — 5 renderings, across message lines 3, 4 ×2 and 6 ×2. **8 battle + 2 script.** Alt *Crosley* rejected |
| バージェス | `Ｂｕｒｇｅｓｓ` | **Promoted from §9, used exactly as seeded.** ⚠️ **7 columns, not §9's 8** — remeasured at review. **2 battle (this chunk) + 5 script** |
| バージェス峡谷 | `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` | **Promoted from §9.** ⚠️ **14 columns, not §9's 15.** §9 offered `Ｃａｎｙｏｎ` or `Ｇｏｒｇｅ`; the seed's own first form was taken, and the sole occurrence sits beside `ｔｈｅ　ｓｏｕｔｈｅｒｎ　ｄｅｓｅｒｔ` in a list of map routes, where the plainer map word reads better. **Both forms are 14, so this stays reversible at zero cost** while chunk 17 is the only unit rendering it — recorded rather than closed |
| イフリート | `Ｉｆｒｉｔ` | **Promoted from §9, used exactly as seeded.** 5 columns, **capitalised** — a named fortress gun, so §17.1's species test does not apply. `・・・イフリートが落とされたか。` → `．．．Ｓｏ　Ｉｆｒｉｔ　ｈａｓ{FFFE}ｂｅｅｎ　ｂｒｏｕｇｈｔ　ｄｏｗｎ．`; 落とされた is passive, so *brought down*, not *fell*. ⚠️ **§9's warning that the gloss lives in chunk 15, not here, stays live for chunk 15's translator** |
| マムー | `Ｍａｍｕ` | **Promoted from §9, used exactly as seeded.** 4 columns, **no `Ｌｏｒｄ`**. `あんたの妹の仇は、このマムー様がとってやるぜ。` → `Ｉ，　Ｍａｍｕ，　ｗｉｌｌ　ａｖｅｎｇｅ{FFFE}ｙｏｕｒ　ｓｉｓｔｅｒ{FFFE}ｆｏｒ　ｙｏｕ．` — the **appositive** carries the `この…様が` self-aggrandisement, which is §25.1's `このクリミアに` pattern applied exactly. **2 battle (this chunk, ch41) + 0 script**; ✅ `マムー兄さん` → `Ｂｒｏｔｈｅｒ　Ｍａｍｕ` **is now rendered — chunk 41 (PR #30, 2026-09-10), 12 columns, the form this row reserved. The term is exhausted** |
| フェミナ | `Ｆｅｍｉｎａ` | **Promoted from §9, used exactly as seeded.** 6 columns. A **person**, female, dead before the chunk opens. **1 battle + 0 script.** The relation §9 left open is settled at §30.5 |
| ルート | `ｒｏｕｔｅ` | **§9 row STRUCK HERE.** Lowercase common noun per §17.1's species test, rendered twice — `敵は別のルートから` → `ｂｙ　ａｎｏｔｈｅｒ　ｒｏｕｔｅ`, `ここへ抜けるルートは、` → `Ｔｈｅ　ｒｏｕｔｅｓ　ｔｏ　ｈｅｒｅ`. 5 columns. ⚠️ **This is the cross-unit row §29.1 deliberately left live**: chunk 8 (PR #11) rendered it first and merged first, chunk 17 renders it second and merges second, and the rule is that the *second* merge strikes the row. Both units were re-checked at this review and both are lowercase. **The plural `ｒｏｕｔｅｓ` is not a variant** — Japanese does not mark number and that sentence lists two |
| ネズミども | `ｒａｔｓ` | ⚠️ **Recorded at review; the PR's additions table omitted it, and it is the omission that mattered.** 4 columns. `カーラインのネズミどもを迎え撃て！！` → `Ｉｎｔｅｒｃｅｐｔ　ｔｈｅ{FFFE}Ｃａｒｌｉｎｅ　ｒａｔｓ！！` A **fifth** contempt word, held apart from 雑草ども → *weeds* (§11.5), ゴミ → *rubbish* (§14.4), ガラクタ → *junk* (§23.1) and 穀潰し → *freeloaders* (§2). Counted at review: **`ネズミ` occurs in battle chunks 17, 18, 25, 27, 41 and 42**, so this form will be reached five more times and had to be fixed now. `ｒａｔｓ` occurs nowhere else in `tl/` |

### 30.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 迎撃態勢 | `Ｉｎｔｅｒｃｅｐｔ　ｓｔａｔｉｏｎｓ` | ⚠️ **18 columns, not the PR's 19** — remeasured. Built on §25.1's 戦闘態勢に入れ → *take battle stations*: 態勢 → **stations**. Used in all three variant lines (message 11, 12, 13) so the three outcomes read as one phrase. Held **distinct** from 迎え撃つ → *intercept*, the verb, below |
| 迎え撃つ / 迎え撃て | `ｉｎｔｅｒｃｅｐｔ` | 9 columns. **Not a new form** — shipped `chunk_007.txt` already has `全軍　迎えうてッ！！` → `Ａｌｌ　ｕｎｉｔｓ，　ｉｎｔｅｒｃｅｐｔ！！`. Recorded because chunk 17 uses it **five** times and it must not fork |
| 出撃！ | `ｓｏｒｔｉｅ！` | ⚠️ **7 columns, not the PR's 8** (bare `ｓｏｒｔｉｅ` is 6). `紅の騎士団、出撃！` → `Ｒｉｇｈｔ，　Ｃｒｉｍｓｏｎ　Ｋｎｉｇｈｔｓ，{FFFE}ｓｏｒｔｉｅ！` A sortie is literally a sally by a besieged garrison, which is exactly this scene. Held **distinct** from §6's 行くぞ！ → `Ｍｏｖｅ　ｏｕｔ！`. Free across `tl/` |
| 連絡員 | `ｃｏｕｒｉｅｒ` | 7 columns. Held **distinct** from 伝令 → *messenger* — **both occur in this chunk** (message lines 5 and 6) and the source draws the distinction itself |
| 伝令 | `ｍｅｓｓｅｎｇｅｒ` | 9 columns. See above |
| 定期連絡 | `ｒｅｇｕｌａｒ　ｒｅｐｏｒｔｓ` | 15 columns |
| 退き時 | `ｔｉｍｅ　ｔｏ　ｗｉｔｈｄｒａｗ` | ⚠️ **16 columns, not the PR's 20.** `そろそろ、退き時か。` → `Ｉｔ　ｉｓ　ａｂｏｕｔ　ｔｉｍｅ{FFFE}ｔｏ　ｗｉｔｈｄｒａｗ．` — the break is added because Rimul takes no contraction and `Ａｂｏｕｔ　ｔｉｍｅ　ｔｏ　ｗｉｔｈｄｒａｗ．` is 24 |
| 立て直す | `Ｒａｌｌｙ` | 5 columns. See the note in §30.4 on the one line where 迎撃態勢 collapses into it |
| ハードウェア | `ｈａｒｄｗａｒｅ` | ⚠️ **8 columns, not the PR's 9.** Rimul on Ifrit: `なまじ強力なハードウェアがあっては` → `Ｗｈｅｎ　ｈａｒｄｗａｒｅ{FFFE}ｉｓ　ｔｏｏ　ｐｏｗｅｒｆｕｌ，`. The source's own katakana loanword; English has the same word and the same slightly clinical register, so nothing is imported |
| 油断が生じる | `ｃａｒｅｌｅｓｓｎｅｓｓ　ｓｅｔｓ　ｉｎ` | The **noun** form of §28.2's 油断 → *careless*, which took its word from shipped `chunk_000.txt` L19. One word, two grammatical shapes the source itself varies — the §27.1 `愛用` and §4 石化能力 pattern. Arrived at independently: §28.2 merged **after** this unit was drafted |
| 兵隊さん | `ｓｏｌｄｉｅｒｓ` | 8 columns. The villager's polite civilian address, carried in **register**, not in an added word (§2). ⚠️ Deliberately **not** §2's トカゲさん → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ` (a comic address to an animal) and **not** §21.2's `〜さん`-on-a-personal-name rule — this is `さん` on a **common noun**, a third pattern |
| 剣の使い手 | `ｓｋｉｌｌｅｄ　ｗｉｔｈ　ａ　ｂｌａｄｅ` | 20 columns. ⚠️ **Recorded at review; the PR omitted it.** `そいつも剣の使い手だ。` → `Ｓｈｅ　ｔｏｏ　ｉｓ　ｓｋｉｌｌｅｄ{FFFE}ｗｉｔｈ　ａ　ｂｌａｄｅ．` **§14.3's 使い → *tamer* does not reach here** — that rule is for creature handlers (獣使い, 氷龍使い) — and 剣士 → *swordsman* / 女剣士 → *swordswoman* (§4) are class labels, not this predicate. Same shape as §24.2's 弓使い → *bowman*: an epithet on an individual |
| 城内の様子 (two forms) | `ｈｏｗ　ｄｏ　ｔｈｉｎｇｓ　ｓｔａｎｄ` / `ｗｈａｔ　ｉｓ　ｔｈｅ　ｓｔａｔｅ` | **Two English forms, deliberately**, because the source has two strings four scenes apart: `城内の様子はどうだ？` (message 10) and `城内の様子はどうなっている。` (message 15). The English tracks the source's own punctuation too (`？` against `．`). §3 is not engaged — different messages (§20.4, §24.5, §27.4) |

### 30.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| ちッ | `Ｔｓｋ` + the source's own punctuation | 3 columns. A tongue click of contempt aimed at someone else. Held **distinct** from §11.5's くっ / クッ → `Ｔｃｈ`, which **this chunk also uses three times** — a strangled grunt of self-vexation is a different gesture, so §23.3's rule applies: a collapse is legitimate only for same-meaning, different-spelling pairs. `Ｔｓｋ` verified free across `tl/` |
| なるほど、 | `Ｉ　ｓｅｅ．` | 6 columns. **Not a new form** — shipped `chunk_033.txt` message 21 already renders `なるほど、この腕なら、` as `Ｉ　ｓｅｅ．　Ｗｉｔｈ　ｓｋｉｌｌ　ｌｉｋｅ`, and chunk 17 matches it, **stop included**, so the `、`→`．` is house practice and not a §5 departure. ⚠️ `Ｉ　ｓｅｅ．` now renders **three** source strings across `tl/` — `そうか` (chunks 4, 7), `そうですか` (chunk 3) and `なるほど` (chunks 33, 17). §25.3's test is met and was **counted at this review**: `そうか` is in chunks 4, 7, 23, 27, 30, 32 and **not in 17 or 33**, so no scene shows two of them |
| いえ、 | `Ｎｏ，` | 3 columns. The polite negation. Same English as §25.2's いや → `Ｎｏ` **plus the source's own punctuation**, which is §5's mechanism and the documented one-word/two-spellings collapse (§17.2 鬼 / オーガ). Shipped `chunk_004.txt` message 10 already has it. ⚠️ **This unit carries both** — `いや、` ×1 and `いえ、` ×2, all three `Ｎｏ，`; `chunk_009.txt`'s `いや・・・` → `Ｎｏ．．．` is the same rule with three stops. **Round 1 caught a `Ｎｏ．` on the `いや、`; it was corrected at round 2** |
| 何？ | `Ｗｈａｔ？` | 5 columns. ⚠️ **Byte-identical to shipped `chunk_008.txt`'s row**, verified at review — matched without obligation, since §3 engages on the message. A **seventh** member of the 何 family, all still held apart: 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？` (§23.2), 何っ／ッ！？ → `Ｗｈａｔ！？` (§28.3), あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2), chunk 7's `何？！` → `Ｗｈａｔ？！` (the same word under §5's punctuation rule) and chunk 0's two stuttered forms |
| そうよ。 | `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` | 13 columns. **A third source string on §23.2's form** — see §30.6, where the co-occurrence is ruled rather than assumed |
| ごめんね。 (standalone) | `Ｉ’ｍ　ｓｏｒｒｙ．` | 10 columns. ⚠️ **Recorded at review; the PR omitted it.** `フェミナ、ごめんね。` → `Ｆｅｍｉｎａ，　Ｉ’ｍ　ｓｏｒｒｙ．` — the vocative leads and the apology is a complete sentence. **A second English form for ごめんね beside shipped `chunk_010.txt` L10/L12's `ごめんね、トカゲさん。` → `Ｓｏｒｒｙ，　Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ．`**, where it is a comma-led hedge before a vocative. Different messages, so §3 is not engaged; recorded so the split does not drift into a third form. §28.3's あいにく → `Ｓｏｒｒｙ，` is unaffected |
| ダメです！ | `Ｉｔ　ｉｓ　ｎｏ　ｕｓｅ！` | 13 columns. ⚠️ **Recorded at review; the PR omitted it.** Rendol's despairing report, in his no-contraction register. **Recurs in chunk 16**, so the form is fixed now rather than re-invented there |
| せいぜい、 | (carried, not a standing row) | `せいぜい、時間をかせいでくれよ。` → `Ｂｕｙ　ｕｓ　ａｌｌ　ｔｈｅ　ｔｉｍｅ{FFFE}ｙｏｕ　ｃａｎ．` — せいぜい is absorbed into *all … you can* rather than given its own word, and the source's two rows stay two English rows. **Recurs in chunk 28**; noted so that unit knows the phrase was rendered whole and there is no bare-segment form to copy |
| グフッ | `Ｇｕｆｆ` | 4 columns. §14.5's ぐふっ in **katakana** — one word, two kana spellings, per §17.2's 鬼 / オーガ, exactly as §11.5 handles くっ / クッ and §29.3 handles くーっ / く〜っ. ⚠️ **The source is `グフッ・・・・・。` — five `・` plus `。` = six stops — and the English carries six.** That is `translation_prompt.md` §3.1's dot rule at the one place in this chunk where it is not three |

### 30.4 Ruling — `読みが甘い` takes `ｍｉｓｒｅａｄ`, and `ｕｎｄｅｒｅｓｔｉｍａｔｅ` is reserved

Message line 13, `読みが甘かったか。` → **`Ｉ　ｍｉｓｒｅａｄ　ｔｈｅｍ．`** (15 columns). Settled at
round 2, and worth writing out because **both parties changed position**.

The round-1 draft read `Ｉ　ｒｅａｄ　ｔｈｅｍ　ｔｏｏ　ｓｏｆｔｌｙ．` on the stated ground that it kept
甘い's *soft* in parallel with §25.1's 甘くない. **That parallel does not exist** — counted at review,
`chunk_009.txt` ships `ｈａｒｄｅｒ` and `ｓｏｆｔ` occurred **nowhere in `tl/`** — and *read someone
softly* is not English: *read* + *softly* collocates only with reading aloud, so the sense is
unrecoverable. `translation_prompt.md` §2 requires a departure exactly there.

The reviewer proposed `Ｉ　ｕｎｄｅｒｅｓｔｉｍａｔｅｄ　ｔｈｅｍ．` (22 columns) and **the translator
overturned it, correctly.** Counted in the dumps at round 2 and verified at review, three source
phrases genuinely mean *underestimate*:

| Japanese | Where | |
|---|---|---|
| `甘く見ない方がいいぞ。` | battle ×1 | |
| `彼らの力を{FFFE}見くびっていたようだ。` | battle ×1 | **the same speech act as this line** — a commander conceding they rated the enemy too low |
| `将軍、見くびってもらっては困る` | script-unique ×1 | |

Spending *underestimate* on 読みが甘かった would collapse two distinct source words the moment the
second of those is translated — the §25.3 / §29.4 trap this glossary keeps writing reserves to
avoid. **`ｕｎｄｅｒｅｓｔｉｍａｔｅ` is therefore RESERVED for 甘く見る / 見くびる** and is verified
unspent across `tl/`. `ｍｉｓｒｅａｄ` keeps 読み, which the source phrase is built on, is free across
`tl/`, and suits Rimul's contraction-free register; the *direction* of the error survives in her
next row, `Ｈｏｗｅｖｅｒ，　ｔｈａｔ　ｔｈｅｉｒ{FFFE}ｐｏｗｅｒ　ｗａｓ　ｓｏ　ｇｒｅａｔ．．．`.

Held **distinct** from §25.1's 甘くない (of an institution) → `ｈａｒｄｅｒ　ｔｈａｎ　…　ｔｈｉｎｋ`:
different construction, different subject, and neither now claims to keep *soft*. **`ｓｏｆｔ` is free
across `tl/` again.** −16 bytes; **lines this affects: none but this one.**

### 30.5 The three sisters, and what the chunk actually settles

§9's フェミナ row asked chunk 17's translator to confirm the relation from the full chunk rather
than lean on the seed. **Confirmed, from the tag stream and not from the prose:**

- Message line 7 page 1 is `{FCB0}{=00030000}` — portrait **03**, Mamu — asking
  `あんたの妹を殺した奴らってのは。`
- Page 2 is `{FCB0}{=00020000}` — portrait **02** — answering `そうよ。カーライン第９軍・・・`
  in feminine speech.
- Message line 24 is **the same portrait 02**: `フェミナ、ごめんね。あんたの仇、とれなかったよ・・・`

So **Femina is portrait 02's 妹 (younger sister)**, and portrait 02 is the elder sister, who dies
without avenging her. Rendered **plain `ｓｉｓｔｅｒ`**, unmarked for seniority: English does not
mark it, and shipped `chunk_004.txt` already renders the dying enemy girl's `姉さん` as
`Ｍｙ　ｓｉｓｔｅｒ` / `Ｓｉｓｔｅｒ，`. `仇をとる` → **`ａｖｅｎｇｅ`** in both halves of the thread
(message 7 `ｗｉｌｌ　ａｖｅｎｇｅ`, message 24 `Ｉ　ｃｏｕｌｄｎ’ｔ　ａｖｅｎｇｅ`), which is what makes
the echo audible.

⚠️ **Two threads left deliberately uncommitted, and they should stay that way until a chunk names
someone.** (a) §23.5 records that **chunk 4's dying enemy girl cries for her 姉さん**, an elder
sister; chunk 17 has an elder sister mourning a 妹 killed by the Carline 9th Army. The halves fit,
but nothing in either chunk names the chunk-4 girl, so **no glossary row is proposed for her** and
the English commits to nothing. (b) The unnamed enemy of message lines 22–23 says
`俺には妹がいる。そいつも剣の使い手だ。` — a **third** sister in one chunk, and possibly a fourth
thread. Recorded, not resolved. `FLAGS.md` §R.

### 30.6 Ruling — `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` renders a third source string, and it stands

`そうそう。` → `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` is fixed at §23.2 and shipped in `chunk_004.txt`; §25.3
ratified `そのとおりだ。` on the same form. Chunk 17 adds `そうよ。` (message 7) — **and the chunk
also contains `そうそう`** (message 19, `あ、そうそう`). §25.3 named `Ｅｘａｃｔｌｙ．` as the reserve
for exactly this. **It is not taken, and the reasoning is recorded so the question is not reopened
unit by unit:**

1. **The two surface forms differ.** Message 7 is `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`; message 19 is
   `Ａｈ，　ｔｈａｔ’ｓ　ｒｉｇｈｔ，` — §6's あ、 → `Ａｈ，` in front, and a comma. No player sees the
   same row twice, and no two rows in `tl/` are byte-identical here.
2. **They are two scenes and two acts.** Message 7 is the grieving sister confirming her sister's
   killers on the east side; message 19 is a villager's *"oh, by the way"* recall marker four
   scenes later. English "that's right" carries both senses natively — this is not a flattening.
   §25.3's stated test is **scene**-level, and it is met.
3. **`そうね。` → `Ｔｈａｔ’ｓ　ｔｒｕｅ．` (§25.2) never meets either.** Counted at this review:
   `そうね` is in battle chunks 9, 27 and 32 and **not in 17**.
4. **`Ｅｘａｃｔｌｙ．` would be wrong here even if a split were wanted.** §25.3 reserved it for *"a
   9th Army companion who contracts freely"*; on a woman confirming who killed her sister it reads
   cold. It **remains reserved and free** for the `そのとおり` / `そうそう` collision §25.3 describes.

**Lines this affects: none.**

### 30.7 Register

| Who | Register |
|---|---|
| Rimul (portrait 05, `{FC50}`) | §7 unchanged and held across **every** one of her segments — `Ｉｔ　ｉｓ`, `ｗｅ　ｓｈａｌｌ`, `Ｉ　ａｍ　ｇｒａｔｅｆｕｌ．`, `ｗｅ　ｃａｎｎｏｔ`, `Ｄｏ　ｎｏｔ`. ⚠️ **This departs from shipped `chunk_000.txt` L14/L18, which give her `ｃａｎ’ｔ`, `ｄｏｎ’ｔ`, `ｗｏｎ’ｔ`, `Ｉ’ｌｌ`.** The written rule is followed here and chunk 0 is **recorded, not re-cut** — §18.3 says its next correction needs a full re-cut and `FLAGS.md` §G1 leaves it 27 bytes. `FLAGS.md` §R |
| Rendol (portrait 06, `{FC51}`) | Formal, deferential, **no contractions** — `Ｓｉｒ，`, `Ｉｔ　ｉｓ　ｎｏ　ｕｓｅ！`, `ｗｅ　ｃａｎｎｏｔ　ｈｏｌｄ`, `Ｉｎｔｅｒｃｅｐｔ　ｓｔａｔｉｏｎｓ　ａｒｅ　ｆｕｌｌｙ　ｒｅａｄｙ．` Albert's shape (§20.5). ⚠️ **Portrait 06 on channel 1 is Rendol; portrait 06 on channel 0 is a different, unnamed enemy** (message lines 22–23) — the same id/channel distinction §23.5 records for chunk 4's Ridge and §28.7 for chunk 13's Cress |
| Mamu (portrait 03) | Rough and swaggering, contractions — `Ｉｓ　ｔｈａｔ　ｔｈｅｍ？`, `Ｒｅｓｔ　ｅａｓｙ．`, `Ｙｏｕ’ｒｅ　ｎｏｔ　ｂａｄ．．．`, and `Ｔｓｋ．．．` His boast is the appositive `Ｉ，　Ｍａｍｕ，`, not a title |
| The grieving elder sister (portrait 02, unnamed) | Casual, contractions — `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`, `Ｎｏ　ｍｉｓｔａｋｅ．`, `Ｉ’ｍ　ｓｏｒｒｙ．`, `Ｉ　ｃｏｕｌｄｎ’ｔ　ａｖｅｎｇｅ`. **Nothing names her**; see §30.5 |
| The unnamed enemy (portrait 06, `{FC50}`) | **No contractions in either of his two lines** — `Ｉ　ｈａｖｅ　ａ　ｓｉｓｔｅｒ．`, `Ｓｈｅ　ｔｏｏ　ｉｓ　ｓｋｉｌｌｅｄ`, `Ｉ　ｗｉｌｌ　ｎｏｔ　ｔｈａｎｋ　ｙｏｕ．` Internally consistent; verified at review because message 21's `ちッ` looks like his and is Mamu's |
| The villager (portrait 04) | Warm, worn and civilian, contractions throughout — `Ｉ’ｍ　ｃｏｕｎｔｉｎｇ　ｏｎ　ｙｏｕ，`, `Ｉ　ｄｏｎ’ｔ　ｋｎｏｗ　ｉｆ　ｉｔ’ｌｌ`. His `兵隊さん` is carried in that warmth, not in an added word |
| The 9th Army (portrait 00) | §7 unchanged — `Ｒｉｇｈｔ，　ｗｅ　ｓｔｏｒｍ　ｔｈｅ{FFFE}ｆｏｒｔｒｅｓｓ！！` |
| Tutorial box (`{=FA1000300030}`, message line 20) | §7 unchanged — plain instructional second person, **byte-identical to §27.2** |

---

## 31. Added by chunk 018 (PR #13, merged 2026-09-08)

Rendered in `tl/battle/chunk_018.txt` — chapter 18, the betrayal at the fortress. Five messages:
Guilford stops Rimul and relays what he says is Commander Krippen's order, sending her and the
Crimson Knights to Doctor Crimea in Crossley over her objection that the defence here will fall;
they part with `死ぬなよ` / `貴官もな`; alone, Guilford notes his pieces are secured and settles in
to watch Krippen's struggle. Then the fortress commander (portrait 08, unnamed) storms in looking
for Rimul, learns Guilford sent her out, works out the betrayal and swears revenge; the battle-open
taunt; his death line; and a coda in which Rimul confronts Guilford and he tells her all goes to
the script. **3,035 / 8,192 bytes, slack 5,157 — 78 text rows, widest 23, none at 24**, no page
over 4 text rows. Merged at **round 1**, with zero blocking findings.

⚠️ **Line numbers in this section are `tl/` FILE lines** — the `=== CHUNK` header counted as line
1, so the five text-bearing messages are file lines 5, 7, 8, 10 and 12. That is the `rowcheck`
convention of §29 shifted by one and the **fourth** numbering convention in this repo
(`FLAGS.md` §O8, §P; glossary §28, §29, §30). **Locate by content.**

⚠️ **The PR's "60 text rows" is wrong; the figure is 78** — recounted twice at review by
independent walks of the `{FFFE}`/`{FCC0}`/`{FC30}`/`{FC50}`/`{FC51}` boundaries (line 5 = 43,
line 7 = 22, line 8 = 4, line 10 = 2, line 12 = 7). Every substantive claim attached to it —
widest 23, none at 24, no page over 4 rows — was verified true.

`Ｇｕｉｌｆｏｒｄ` / `Ｌａｄｙ　Ｒｉｍｕｌ` (§1), `Ｄｏｃｔｏｒ　Ｃｒｉｍｅａ` / `Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ`
(§25.1), `Ｃｒｏｓｓｌｅｙ` (§30.1), `Ｃｒｉｍｓｏｎ　Ｋｎｉｇｈｔｓ` / `ｔｈｅ　Ｅｍｐｉｒｅ` (§2),
`Ｇｅｎｅｒａｌ` for 将軍 (§26.2), `Ｈｏｗｅｖｅｒ，` (§23.3 — its **seventh** use), `Ｎｏ` for いや
(§25.2), `Ｈｍｐｈ，` (§6), `Ｔｃｈ，` (§11.5), `Ｅｎｏｕｇｈ！` (§14.5), `Ｗｈａｔ！？` (§28.3),
`Ｙｏｕ　ｆｏｏｌ．` (§28.3), `Ｒｉｇｈｔ` (§6), `Ｕｎｉｔ　１` (§11.2, §17.2) and `ｒａｔｓ` (§30.1) are
used unchanged. **`Ｇｉｌｆｏｒｄ` occurs nowhere in `tl/` or `pending/`** — verified at review.
**No §9 PROVISIONAL row is promoted here**: none of the fifteen wave-4 seeds occurs in this chunk,
so the cross-unit rows held for chunks 19 and 20 are untouched.

`了解` is **absent** from this chunk and `わかった` occurs **once**, so §29.4's `Ａｇｒｅｅｄ．`
reserve is **not** engaged and §6's `Ｒｉｇｈｔ` governs — confirmed at review by counting the dump
body, not taken on report. ⚠️ **Chunk 19 does engage it**; the two rulings must not blur.

### 31.1 People, ranks and machines

| Japanese | English | Note |
|---|---|---|
| クリッペン司令 | `Ｃｏｍｍａｎｄｅｒ　Ｋｒｉｐｐｅｎ` | ⚠️ **17 columns, not the PR's 18** — remeasured at review; 18 is the form with a following stop, which is §25.1's own figure for `クリッペン司令官`. The source's **shorter** spelling: one English form for both, the documented same-meaning/two-spellings collapse (§17.2 鬼 / オーガ, §11.5 くっ / クッ). §11.2's 司令官 / 指令官 → Commander is unchanged. **2 occurrences, both this chunk**; `クリッペン司令官` is chunks 9 and 17 |
| １号機 (bare) | `Ｕｎｉｔ　１` | 6 columns, digit full-width. The bare form of §17.2's `オリジナルＮ号機` → `Ｏｒｉｇｉｎａｌ　Ｕｎｉｔ　Ｎ` and §11.2's `４号機` → `Ｕｎｉｔ　４`. Verified at review against `batch_003` L77/L82/L83/L87/L88 and `pending/chunk_017` msg 6's `オリジナル１号機` → `Ｏｒｉｇｉｎａｌ　Ｕｎｉｔ　１`. **4 battle** (chunks 16, 17, 18 ×2) **+ 84 script**, most of them the item-description table §17.2 already governs |

**Portrait 08 is deliberately unnamed.** He commands the fortress, holds Unit 1, is addressed by a
subordinate who calls Rimul `リムル様` and Guilford `ギルフォード将軍`, and is the map boss. The
evidence points to **Commander Krippen** — Guilford's soliloquy is
`クリッペン司令のご奮闘を拝見させてもらうとしよう`, i.e. he stays to watch Krippen fight — but **no line
in the chunk names him**, so no row of his carries a name, on the §28.7 / `FLAGS.md` §P practice
for chunk 13's King. Portraits 06 = Rimul and 07 = Guilford **were verified from the tag stream at
review**, not assumed: file line 5 opens `{FCB0}{=00070000}{FC50}待て、リムル。` answered by
`{FCB0}{=00060001}{FC51}ギルフォード！`, and file line 12 repeats the pair with the channels swapped.

### 31.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| シナリオ | **`ｓｃｒｉｐｔ`** | 6 columns. **Ruled 2026-09-08, PR #13 review — see §31.5.** `全てはシナリオ通りだ。` → `Ａｌｌ　ｇｏｅｓ　ｔｏ　ｔｈｅ　ｓｃｒｉｐｔ．` ⚠️ **NOT a hapax as the PR believed: 3 battle occurrences — this chunk ×1 and chunk 23 ×2 — 0 script.** The **word** is fixed; the frame is not, so chunk 23's `このシナリオ` takes `ｔｈｉｓ　ｓｃｒｉｐｔ` |
| 守備 (bare noun) | `ｔｈｅ　ｄｅｆｅｎｃｅ` | ⚠️ **11 columns, not the PR's 12.** British per §4. `ここの守備が・・・` → `ｔｈｅ　ｄｅｆｅｎｃｅ　ｈｅｒｅ．．．` Held **distinct** from §2's 守備兵 → *garrison* (shipped `chunk_000` ×2, and **chunk 19 carries it four times**), 守備隊 → *garrison* (`chunk_017`), and chunk 2's verbal 守備につく → *guard*. ⚠️ `ｄｅｆｅｎｃｅ` was already in `tl/` inside two compounds of **other** words — `ｄｅｆｅｎｃｅ　ｐｏｗｅｒ` for 防御力 (`batch_001` L12/L13, `batch_003`) and `ｓｅｌｆ‐ｄｅｆｅｎｃｅ` for 正当防衛 (`chunk_011` msg 8); recorded at review, no collision. **3 bare 守備 in battle** (chunks 2, 18, 23) **+ 6 script** |
| 配備につく | `ｄｅｐｌｏｙ` (verb) | 6 columns. `早速、貴官の隊も配備についてくれ。` → `Ｄｅｐｌｏｙ　ｙｏｕｒ　ｓｑｕａｄ　ｔｏｏ，` / `ａｔ　ｏｎｃｅ．` The same word as `pending/chunk_017` msg 6's noun 配備 → `ｄｅｐｌｏｙｍｅｎｔ` (×2, verified at review); one word, two grammatical shapes the source itself varies — the §27.1 `愛用` / §30.2 `油断` pattern. *Take up its deployment* is not English. **3 battle** (chunk 17 ×2, this chunk ×1) **+ 3 script**. ⚠️ **Recorded at review and omitted by the PR: `ｄｅｐｌｏｙ` already renders a second Japanese word** — `chunk_033` msg 2's 配置する / 配置して下さい. §3 is not engaged (different messages) and §25.3's test is met: 配置 is battle chunk 33 only (+2 script), 配備 is chunks 17 and 18 only, **disjoint** |
| 手駒 | `ｐｉｅｃｅｓ` | 6 columns. Guilford's board-game metaphor for the people he has moved. Not *pawns* — 駒 is the neutral piece and the contempt is his, not the word's. ⚠️ **Reach recorded at review; the PR gave none: 1 battle + 3 script**, so the form will be reached again. `ｐｉｅｃｅｓ` also stands in parked `chunk_043` msg 4 as `ｂｌｏｗｎ　ｔｏ　ｐｉｅｃｅｓ` (吹き飛ぶ) — an unrelated English idiom in a parked file, no collision |
| ご奮闘 | `ｓｔｒｕｇｇｌｅ` | 8 columns. The honorific ご is sardonic and is carried by `Ｉ　ｓｈａｌｌ　ｂｅ　ｐｅｒｍｉｔｔｅｄ　ｔｏ　ｗａｔｃｈ` (拝見させてもらう, humble-causative), not by an added word — §2's politeness rule. ⚠️ **Reach recorded at review: 2 battle, this chunk and chunk 28** |
| ただならぬ | `ｅｘｔｒａｏｒｄｉｎａｒｙ` | 13 columns. `ただならぬ損失` → `ａｎ　ｅｘｔｒａｏｒｄｉｎａｒｙ　ｌｏｓｓ`. Hapax — 1 battle / 0 script, confirmed |
| 不服そうだな | `Ｙｏｕ　ｓｅｅｍ　ｄｉｓｓａｔｉｓｆｉｅｄ．` | 22 columns. Hapax — 1 battle / 0 script, confirmed |
| 心強い | `Ｉ　ａｍ　ｒｅａｓｓｕｒｅｄ．` | 15 columns. Hapax — 1 battle / 0 script, confirmed |
| 〜め (contempt, on a personal name) | `Ｔｈａｔ　〜` | `ギルフォードめ。` → `Ｔｈａｔ　Ｇｕｉｌｆｏｒｄ．` (14 columns) and `ギルフォードめ・・・` → `Ｔｈａｔ　Ｇｕｉｌｆｏｒｄ．．．` — §5's mechanism, the word fixed and the stops from the source. Takes the contempt into the demonstrative exactly as §20.3's バカ者 → `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ` already does. ⚠️ Distinct from `chunk_006`'s `フェルナンドめが`, which **drops** め and carries the contempt elsewhere in a longer sentence — a different message, so §3 is not engaged. ⚠️ **SCOPE CORRECTED 2026-09-09 (§4.3, PR #18 review): this row governs `〜め` in THIRD-PERSON REFERENCE only, and its “Recurs as `この裏切り者め。` in chunk 21” clause is struck** — that line is direct address, it takes `Ｙｏｕ　〜` on §28.3's `馬鹿者！` model, and chunk 21 ships `Ｙｏｕ　ｔｒａｉｔｏｒｓ．`. No rendering changes; see §36.3 |

### 31.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| さて、 | `Ｎｏｗ　ｔｈｅｎ，` | ⚠️ **9 columns, not the PR's 10.** ⚠️ **Not a new rendering — recording one already shipped, and verified at review**: `tl/battle/chunk_033.txt` msg 6 ships `さて、果たして、` → `Ｎｏｗ　ｔｈｅｎ，` and had no glossary row. Held **distinct** from §28.8's さあ、 → `Ｎｏｗ，`, and that distinction is **proven, not theoretical**: `chunk_033` contains both source strings and ships them apart. ⚠️ **`Ｎｏｗ　ｔｈｅｎ` already serves two further source strings the PR did not name** — `それじゃ、` (`chunk_003` msg 4) and `おっと。` (`chunk_007` msg 11, as `Ｎｏｗ　ｔｈｅｎ．`). §25.3's test run at review: `さて、` is in chunks 18, 26, 33; `それじゃ` in 3, 7, 15, 32, 43; `おっと` in 7, 25, 43 — **no chunk holds `さて、` with either**. **3 battle + 5 script.** Recurs in chunk 26 |
| かかってくるがいい。 | `Ｙｏｕ　ｍａｙ　ｃｏｍｅ　ａｔ　ｍｅ．` | 19 columns. Deliberately **not** `Ｃｏｍｅ　ａｔ　ｍｅ．`, which `chunk_033` msg 20 already ships for the polite imperative `かかってきなさい。` The 〜がいい is condescending permission, not an imperative, so *You may* keeps them apart **and leaves the plain imperative かかってこい。 (chunks 16 ×2, 30) free to take chunk 33's shipped form.** ⚠️ **Binds chunk 23 L15**, which carries this string byte-identically — verified at review in `battle_dump.txt`, in the line `まさか、お前たち９軍と剣を交えることになろうとはな。かかってくるがいい。骨は拾ってやる。` **2 battle + 0 script** |
| ネズミども (bare vocative) | `ｙｏｕ　ｒａｔｓ` | 8 columns. §30.1 fixes ネズミども → `ｒａｔｓ` from `pending/chunk_017`'s attributive `カーラインのネズミども` → `ｔｈｅ　Ｃａｒｌｉｎｅ　ｒａｔｓ`; this is the bare vocative, so the ども plural-contempt takes `ｙｏｕ`. **Word unchanged.** §30.1 predicted five more uses — this is the first. `ネズミども` is **6 battle occurrences in chunks 17, 18, 41 and 42** |
| まさか、 | `Ｓｕｒｅｌｙ` | 6 columns. ⚠️ **Fixed here 2026-09-08 (PR #13 review) — it had never been in this glossary despite being shipped.** `pending/chunk_017.txt` msg 4 renders `まさか、奴らは` → `Ｓｕｒｅｌｙ　ｔｈｅｙ　ｄｉｄ　ｎｏｔ`, and this chunk renders `まさか、裏切る気か？` → `Ｓｕｒｅｌｙ　ｈｅ　ｄｏｅｓ　ｎｏｔ` / `ｍｅａｎ　ｔｏ　ｂｅｔｒａｙ　ｍｅ？`. This is §24.3's `よし、` shape — a form shipped repeatedly that the glossary never fixed. **18 battle occurrences across 13 chunks (0, 17, 18, 19, 23, 24, 25, 26, 27, 30, 32, 39, 43) + 10 script**, so it is the largest single drift risk this unit leaves behind. `Ｓｕｒｅｌｙ` is otherwise free across `tl/` |  ⚠️ **SCOPE WRITTEN IN 2026-09-11 (§4.3 in-place correction, PR #35 review). `Ｓｕｒｅｌｙ` IS UNCHANGED for every construction this row was set on; what is added is that it does NOT reach `まさか〜とは`.** This row's own two examples are both `まさか、〜ないだろう` / `〜気か？` — the negative-conjecture sense — and `Ｓｕｒｅｌｙ` is right there. The **exclamative** `まさか〜とは・・・` (*to think that…*) is a different construction and has its own **shipped incumbent**, counted over `tl/` at review: merged `chunk_024` L4 `まさか 穀潰しのお前たちに追われるとは` → `ｔｏ　ｔｈｉｎｋ　ｔｈａｔ　ｙｏｕ　ｆｒｅｅｌｏａｄｅｒｓ…` and merged `chunk_030` L4 `まさか、お前たちがここに流れ着いた` → `Ｔｏ　ｔｈｉｎｋ　ｔｈａｔ　ｙｏｕ　ｈａｄ　ｗａｓｈｅｄ　ｕｐ　ｈｅｒｅ．．．．`, with `pending/chunk_043` L29 taking the sibling `，　ｏｆ　ａｌｌ　ｔｈｉｎｇｓ，`. `batch_012` D380 matches that incumbent (`Ｔｏ　ｔｈｉｎｋ　ｔｈｅ　Ｐｒｉｎｃｅｓｓ　ｓｈｏｕｌｄ　ｖａｎｉｓｈ…`) and D377 matches the negative sense (`ｃｏｕｌｄ　ｎｅｖｅｒ`, the `chunk_000` `Ｉｔ　ｃａｎ’ｔ　ｂｅ` family). **A reviewer nearly raised this as a finding and measuring stopped it** — §AG6's mirror: search for the English the SOURCE WORD already has before charging a departure |
| ええい、 | `Ｅｎｏｕｇｈ！` | ⚠️ **Recorded at review so it is not "corrected" later.** §14.5's entry carries the `！` **as part of the fixed form**, and the source has `、` in every instance — so this is *not* §5's punctuation mechanism, and the `！` must not be re-derived from the source. `chunk_007` msg 2 ships `ええい、全軍　迎えうてッ！！` → `Ｅｎｏｕｇｈ！` / `Ａｌｌ　ｕｎｉｔｓ，　ｉｎｔｅｒｃｅｐｔ！！`, and this chunk's `ええい、この非常時に。` → `Ｅｎｏｕｇｈ！　Ｉｎ　ｔｈｉｓ　ｃｒｉｓｉｓ．` (23 columns) matches it byte-for-byte. Chunk 24 carries a third instance, untranslated |

### 31.4 Ruling — the source's comma yields to English sentence grammar, and §30.3 is unaffected

`いや、わかった。` → **`Ｎｏ．　Ｒｉｇｈｔ．`** (10 columns). Both words are the fixed ones — `Ｎｏ` for
いや (§25.2), `Ｒｉｇｈｔ` for わかった (§6). What departs is §5's punctuation mechanism, by one
character.

**This is not a new departure. It is already shipped.** `tl/battle/chunk_014.txt` message 10
renders `よし、ここまで来たら、一気に行こう。` as `Ｒｉｇｈｔ．　Ｗｅ’ｖｅ　ｃｏｍｅ　ｔｈｉｓ` /
`ｆａｒ，　ｓｏ　ｌｅｔ’ｓ　ｐｕｓｈ　ｏｎ．` — the source's comma after the fixed assent word promoted to
a full stop, for exactly this reason. The PR reasoned it out from first principles and was right;
the precedent settles it.

**The rule, written down because §30.3 looks like it says the opposite and does not:**

> **§5's punctuation mechanism governs whenever the source's own stop is renderable, and yields to
> English sentence grammar only where the material after the source's comma is a complete
> independent clause.**

- `pending/chunk_017.txt` — `いや、クロスリーまで伝令を送っていては、間にあわん。` is one sentence with a
  continuing clause, so `Ｎｏ，` is right and §30.3's round-2 correction of a `Ｎｏ．` there stands
  **unamended**.
- Chunk 18 — `いや、わかった。` is two complete utterances. `Ｎｏ，　Ｒｉｇｈｔ．` is a comma splice
  capitalised, and lowercased (`Ｎｏ，　ｒｉｇｈｔ．`) it inverts the sense into agreement, when Rimul
  is denying the imputation of dissatisfaction and *then* accepting the order.

Every avoiding reserve was checked and is spent: `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` on わかりました (§21.2),
`Ｕｎｄｅｒｓｔｏｏｄ` on 了解 (§21.2), `Ｉ　ｋｎｏｗ．．．` on 分かってる (§28.3), `Ａｇｒｅｅｄ．`
reserved by §29.4 for a case this chunk does not present, `Ｖｅｒｙ　ｗｅｌｌ` and `Ｉ　ｓｅｅ．` named
by §29.4 as not free. Both forms measure **10**, so nothing rode on width.

⚠️ **This chunk renders `いや、` both ways inside ONE message.** File line 5 has `Ｎｏ，` on
`いや、私は…来たのだ。` and `Ｎｏ．` on `いや、わかった。`, four pages apart in the same scene. That is
correct under the rule above — the *word* is `Ｎｏ` in both — but a positional duplicate check run
by eye will read it as a divergence. It is not one. Same trap as §24.5's `さあ、` / `よし、` before a
`{FC00}` and §27.4's spaced / unspaced village line. **Lines this affects: none.**

### 31.5 Ruling — `シナリオ` takes `ｓｃｒｉｐｔ`, because `ｐｌａｎ` is already spent on 作戦

`全てはシナリオ通りだ。全ては、な・・・。` is Guilford's reveal, and the source chose the katakana
loanword over 計画 (which is **absent** from the chunk). Rendered
`Ａｌｌ　ｇｏｅｓ　ｔｏ　ｔｈｅ　ｓｃｒｉｐｔ．` / `Ａｌｌ　ｏｆ　ｉｔ．．．．`, the echo of `全ては` preserved by
opening both rows with `Ａｌｌ`. Three reasons, in order of weight:

1. **`ｐｌａｎ` is not free.** §19.2 fixes bare 作戦 → `Ｔｈｅ　ｐｌａｎ？`, shipped in `chunk_001`;
   `ｐｌａｎｓ` also stands in `pending/chunk_017` msg 4. Spending it on シナリオ would collapse two
   distinct source words — the §25.3 / §29.4 / §30.4 trap this glossary keeps writing reserves to
   avoid.
2. **The transliteration-of-a-loanword precedent.** §30.2's `ハードウェア` → `ｈａｒｄｗａｒｅ`:
   English has the same word and the same slightly clinical register, so nothing is imported.
   *Script* also keeps the staged-drama sense Guilford's whole scheme turns on, where *plan* is
   merely administrative.
3. ⚠️ **`シナリオ` is NOT a hapax, and this is the argument the PR could not make.** Counted in the
   dumps at review: **3 battle occurrences — this chunk ×1 and chunk 23 ×2 — and 0 script.**
   Chunk 23's are `俺には、このシナリオがフェルナンドひとりの手で仕組まれたとは思えない。`, the party
   working out that the whole affair was staged. That is the **same metaphor**, five chapters
   later, and `ｓｃｒｉｐｔ` carries it in both places where `ｐｌａｎ` would flatten both. **The
   ruling binds chunk 23.**

⚠️ **Width does not decide this, and the PR's Flag 6 implied it did.** Remeasured at review:
`Ｅｖｅｒｙｔｈｉｎｇ　ｇｏｅｓ　ｔｏ　ｐｌａｎ．` is indeed **24** — but `Ａｌｌ　ｇｏｅｓ　ｔｏ　ｐｌａｎ．` is
**17** and would have fitted comfortably. Reason 1 carries it alone.

⚠️ **The article is recorded, not closed.** `Ａｌｌ　ｇｏｅｓ　ｔｏ　ｔｈｅ　ｓｃｒｉｐｔ．` is **23**;
`Ａｌｌ　ｇｏｅｓ　ｔｏ　ｓｃｒｉｐｔ．` is **19** and is the tighter English idiom, by analogy with *going
to plan*. Both are legal and both are §3.1-clean. This is the §30.1 `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` /
`Ｇｏｒｇｅ` treatment: reversible at **−8 bytes with no re-flow** against 5,157 bytes of slack.
**The word is what is fixed; the frame is chunk 18's row only.**

### 31.6 The four-row wall, and the one `この` that is dropped

File line 7's revenge speech is the only §2.1 step 5 departure in the unit:
`この私を裏切ったことを、` → `Ｆｏｒ　ｂｅｔｒａｙｉｎｇ　ｍｅ，` (17 columns), dropping the `この私`
self-importance of §25.1's `このクリミアに` and §30.1's `このマムー様が`.

**Verified at review rather than accepted on report.** That page carries **a leading blank *and* a
trailing blank** around 3 text rows, and `translation_prompt.md` §3.2 states that a page with both
plus four text rows is the one shape that has never appeared in the source — so no fourth row is
available. `Ｆｏｒ　ｂｅｔｒａｙｉｎｇ　ｍｅ，　ｏｆ　ａｌｌ` measures exactly **24**, which §25.1 has twice
rejected and §29.1 once. The swagger survives two rows earlier in `Ｙｏｕ　ｆｏｏｌ．` and
`Ｗｈｉｌｅ　Ｕｎｉｔ　１　ｒｅｍａｉｎｓ，` / `Ｉ　ｓｈａｌｌ　ｎｏｔ　ｂｅ　ｂｅａｔｅｎ` / `ｓｏ　ｅａｓｉｌｙ．`

The **single** `{FFFE}` this unit adds (file line 7, 19 → 20) is inside
`まさか、裏切る気か？` → `Ｓｕｒｅｌｙ　ｈｅ　ｄｏｅｓ　ｎｏｔ` / `ｍｅａｎ　ｔｏ　ｂｅｔｒａｙ　ｍｅ？` (18 / 18);
one row would be 37 columns. That page goes 2 → 3 text rows, still under the wall. **No `{FCC0}`
was added** — `FLAGS.md` §Q2's documented gate defect was not rediscovered.

### 31.7 Register

| Who | Register |
|---|---|
| **Guilford (portrait 07)** | ⚠️ **His first full scene, and the row §25.5 could not write from one segment.** Cold, formal and unhurried, **no contraction anywhere** — `Ｗａｉｔ，　Ｒｉｍｕｌ．`, `Ｎｏ，　Ｉ　ｈａｖｅ　ｃｏｍｅ　ｔｏ`, `Ｓｏ　Ｉ　ａｍ　ｔｏｌｄ．`, `ｗｅ　ｓｈａｌｌ　ｍａｎａｇｅ．`, `Ｙｏｕ　ｓｅｅｍ　ｄｉｓｓａｔｉｓｆｉｅｄ．`, `Ｈｍｐｈ，　ｄｏ　ｎｏｔ　ｗｏｒｒｙ．` §25.5's `Ｓｉｒ．．．．` is unchanged and reads as the same man. What makes him sinister is that he never raises his register: the betrayal is delivered in the same flat courtesies as the order, and `Ｉ　ｓｈａｌｌ　ｂｅ　ｐｅｒｍｉｔｔｅｄ　ｔｏ　ｗａｔｃｈ` is the whole character |
| Rimul (portrait 06) | §7 and §30.7 unchanged and held across **every** one of her segments — `Ｓｏ　ｙｏｕ　ｈａｄ　ｒｅｔｕｒｎｅｄ．`, `Ｉ　ａｍ　ｒｅａｓｓｕｒｅｄ．`, `Ｃｒｏｓｓｌｅｙ，　ｙｏｕ　ｓａｙ？`, `Ｉ　ｓｈａｌｌ　ｈｅａｄ　ｆｏｒ`, `ｄｏ　ｎｏｔ　ｄｉｅ．`, `Ｗｈａｔ　ｉｓ　ｔｈｅ　ｍｅａｎｉｎｇ　ｏｆ　ｔｈｉｓ！` **Zero contractions**, which is the written rule §30.7 chose over shipped `chunk_000`'s contracted Rimul. Two independent units have now followed it; `chunk_000` stays recorded and not re-cut |
| The fortress commander (portrait 08, unnamed) | Blustering, then vengeful; **no contractions** — `Ｗｈｅｒｅ　ｈａｓ　Ｒｉｍｕｌ　ｇｏｎｅ！`, `Ｅｎｏｕｇｈ！`, `Ｗｈａｔ　ｄｏｅｓ　ｈｅ　ｉｎｔｅｎｄ．`, `Ｉ　ｓｈａｌｌ　ｎｏｔ　ｂｅ　ｂｅａｔｅｎ`, `Ｉ　ｓｈａｌｌ　ｎｏｔ　ｆｏｒｇｉｖｅ．．．` §14.6 / §20.5 / §25.5 / §28.6's Imperial officers, unchanged. ⚠️ His rhetorical questions keep the source's own declarative stop (`どういうつもりだ。` → `Ｗｈａｔ　ｄｏｅｓ　ｈｅ　ｉｎｔｅｎｄ．`), which is §5 and matches shipped `chunk_013`'s `ｗａｓ　ｉｔ　ｎｏｔ．` / `ａｒｅ　ｙｏｕ　ｎｏｔ．` |
| His subordinate (portrait 05) | Deferential, no contractions — `Ｌａｄｙ　Ｒｉｍｕｌ　ｗａｓ　ｕｒｇｅｄ` / `ａ　ｓｈｏｒｔ　ｗｈｉｌｅ　ａｇｏ` / `ｂｙ　Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ，` / `ａｎｄ　ｗｅｎｔ　ｏｕｔｓｉｄｅ．．．．` Albert's shape (§20.5), the same column §28.6 and §29.6 put Irvine's and the escort captain's men in |

⚠️ **`貴官` appears three times and is carried in register, never in an added word** (§2, §26.7,
§29.2): `貴官の隊` → `ｙｏｕｒ　ｓｑｕａｄ`, `貴官には、` → `Ｙｏｕ　ａｒｅ　ｔｏ　ｐｒｏｔｅｃｔ`,
`貴官もな。` → `Ｙｏｕ　ｔｏｏ．` Rimul uses the informal `お前` to Guilford in one breath
(`お前がいてくれれば`) and the formal `貴官` in the next; English has one *you* and the shift is not
renderable. Recorded, not acted on.

---

## 32. Added by chunk 020 (PR #14, merged 2026-09-09)

Rendered in `tl/battle/chunk_020.txt` — chapter 20, the treasure dig at Farina, in six scenes: a
self-important would-be Imperial officer gloats that his rival Hugo is searching in the wrong
place; a burst ooze kills one of his men and he explodes at being called *Boss*; the 9th Army
arrives and he orders them scattered; the party finds the Crystal of Fire first and runs; the
bandits reach the site to find their chief dead (or alive, in the alternative outcome) and scarper
with the hoard; and in the two closing variants the party — or the enemy — digs a medal out of the
ground beside the gemstones, one of the bandit Kabala's treasures. **4,265 / 8,192 bytes, slack
3,927 — 94 text rows, widest 23, none at 24**, no page over 4 text rows the source did not already
exceed. Merged at **round 1**, with zero findings requiring a change to the unit.

⚠️ **This section claimed §32 at commit time.** Chunk 19's reviewer held an unpushed draft for the
same number; this commit landed first, so **chunk 19 takes §33**. Read the last heading immediately
before writing, never reserve — wave 3 lost work to two reviewers both holding §28.

⚠️ **Line numbers below are `tl/` FILE lines** (the `=== CHUNK` header is line 1), so the ten
text-bearing messages are file lines 2, 3, 4, 29, 31, 32, 34, 47, 48 and 49. That is §31's
convention and the **fifth** numbering convention in this repo. **Locate by content.**

`Ｆａｒｉｎａ` / `Ｃａｒｌｉｎｅ` / `Ｒｏｙａｌ　Ａｒｍｙ` / `ｔｈｅ　Ｅｍｐｉｒｅ` (§2), `Ｇｕｉｌｆｏｒｄ` (§1),
`Ｇｅｎｅｒａｌ` (§26.2), `Ｔｒｕｌｙ，` (§28.3), `Ｒｉｇｈｔ，` (§6, §24.3), `Ｙｅａｈ` for ああ (§6),
`Ｙｅｓ，` for うん (§29.3), `Ｗｈａｔ．．．？` for あれ (§21.2), `Ａａｈ，` (§23.2), `Ｆｕｆｕ，` (§12.3),
`Ｈｍ？` (§6) and `Ｙｏｕ　ｆｏｏｌ` for the バカ vocative (§28.3) are used unchanged.
**`まさか` is absent from this chunk** (counted in the dump body), so §31.3's known-over-broad
`Ｓｕｒｅｌｙ` ruling is not engaged here and this unit neither applies nor tests it.

### 32.1 People, ranks, creatures and items — four promotions out of §9

| Japanese | English | Note |
|---|---|---|
| おかしら | `Ｂｏｓｓ` | 4 columns. **Promoted from §9 (wave-4 seed), taking the seed's primary form over its `Ｃｈｉｅｆ` (5) alternative.** The bandit crew's address to their chief, **×5 in this chunk** (file lines 3, 31 ×3, 32), byte-identical every time; **0 script occurrences**, confirmed at review. Held clear of §9's `親方` → `ｔｈｅ　ｂｏｓｓ`: verified at review that lowercase `ｂｏｓｓ` occurs **nowhere** in `tl/` or `pending/`, and that `親方` is **not** in shipped `batch_002.tsv` — it belongs to a future batch, so the two forms have never met |
| おかしらぁ！ | `Ｂｏｓｓｓ！` | 6 columns. The drawn-out cry to a chief who does not answer (file line 31). **Ruled at review — see §32.6.** The extra kana beat takes an extra letter, per §29.3's くーっ → `Ｔｃｈｈ` and §26.5's ふーむ → `Ｈｍｍ` |
| 将校 | `ｏｆｆｉｃｅｒ` | 7 columns. **Promoted from §9.** `わしは帝国の将校だぞ！` → `Ｉ　ａｍ　ａｎ　ｏｆｆｉｃｅｒ　ｏｆ　ｔｈｅ` / `Ｅｍｐｉｒｅ！`. **1 battle + 0 script.** Held apart from §26.2's 将軍 → `Ｇｅｎｅｒａｌ` and §2's 隊長 / 少尉 / 中尉 — the gag depends on it (§32.4a). ⚠️ **Recorded at review and omitted by the PR: `ｏｆｆｉｃｅｒ` is not free** — `chunk_001` already ships `ａ　ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ，` for a different source word. Different collocation, different message, no collision; recorded so it cannot drift |
| 勲章 | `ｍｅｄａｌ` | 5 columns. **Promoted from §9.** `勲章のようだな。` → `Ｌｏｏｋｓ　ｌｉｋｅ　ａ　ｍｅｄａｌ．` ×2, byte-identical. ⚠️ **Both the seed's and the PR's reach figure ("2 battle") are wrong, and the メダル collision is LIVE, not discharged — see §32.5** |
| バーストウーズ | `ｂｕｒｓｔ　ｏｏｚｅ` | 10 columns. **Promoted from §9, used exactly as seeded, lowercase** by the §17.1 species test, derived from `グレイウーズ` → `ｇｒｅｙ　ｏｏｚｅ`. ⚠️ **That precedent is at §17.2, not §17.4** — the seed mis-cited it and the PR inherited the citation; the derivation is unaffected. **1 battle + 0 script** |
| ギルフォード様 | `Ｌｏｒｄ　Ｇｕｉｌｆｏｒｄ` | 13 columns. 様 → **Lord** for a male superior, per §1's ヘルファー様 → `Ｌｏｒｄ　Ｈｅｌｆｅｒ` and §28.1's アーバイン様 → `Ｌｏｒｄ　Ｉｒｖｉｎｅ`. **Does not disturb** §26.2's `ギルフォード将軍` → `Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ` (shipped, `chunk_018`): the man holds two titles and it is the source that varies — the Fernando shape §26.2 already ruled. **1 battle + 0 script.** ⚠️ **Confirmed at review against a shipped frame the PR did not cite**: `batch_002.tsv` L9 renders `ヘルファー様に何と報告すれば・・・` as `ｗｈａｔ　ａｍ　Ｉ` / `ｔｏ　ｒｅｐｏｒｔ　ｔｏ　Ｌｏｒｄ` / `Ｈｅｌｆｅｒ．．．`, and this unit's `ギルフォード様に何と報告すれば・・・` → `ｗｈａｔ　ａｍ　Ｉ　ｔｏ　ｒｅｐｏｒｔ` / `ｔｏ　Ｌｏｒｄ　Ｇｕｉｌｆｏｒｄ．．．` matches it frame for frame and stop for stop, arrived at independently |
| 宝石 | `ｇｅｍｓｔｏｎｅ` / `ｇｅｍｓｔｏｎｅｓ` | **8 / 9 columns** (⚠️ **corrected in place 2026-09-09, §4.3, PR #26 review — this cell read “9 / 10” and both halves were one too high.** `len('ｇｅｍｓｔｏｎｅ')` = 8, `len('ｇｅｍｓｔｏｎｅｓ')` = 9 — eight letters, not nine. Flagged by chunk 31's translator, re-measured at review. The same error is corrected at §33.1; see §45.4. **No rendering changes** — the form is used exactly as fixed and is 1 column *cheaper* than the glossary believed, which is the safe direction, but two sections stated the same wrong number and a future width decision could have been made on it). **A fifth cross-unit term the wave-4 seed missed** — see the §9 note. Ruled `ｇｅｍｓｔｏｎｅ` by chunk 19's reviewer; this unit's plural is consistent. Deliberately **not** `ｊｅｗｅｌｓ`: §3 fixes ジュエル → `Ｊｅｗｅｌ` (the currency, "do not translate as gem") and ジェム → `Ｇｅｍ` (the pickup). Verified at review: `ｇｅｍｓｔｏｎｅ` is **free** across `tl/` and `pending/`; `ｇｅｍ` occurs once (`batch_003`, §4's lowercase *a gem in its brow*) and `Ｇｅｍ` is the capitalised pickup — no collision either way. **6 battle (19 ×1, 20 ×4, 31 ×1) + 5 script-unique** |
| 宝 / お宝 | `ｔｒｅａｓｕｒｅ` / `ｔｈｅ　ｔｒｅａｓｕｒｅ` | 8 / 12 columns. Kept **distinct** from 宝石 → gemstone; the source draws the distinction itself inside file line 31. `お宝のひとつ` → `ｏｎｅ　ｏｆ　…　ｔｒｅａｓｕｒｅｓ`. `ｔｒｅａｓｕｒｅ` verified free. ⚠️ **3 in this chunk, not the PR's 2** (one bare `宝`, two `お宝`); **15 battle rows containing 宝 (16 ×3, 19 ×4, 20 ×7 of which 4 are 宝石, 31 ×1) + 12 script-unique.** Also in chunk 19 — cross-unit, see §9 |

### 32.2 Words and phrases

| Japanese | English | Note |
|---|---|---|
| 手柄 | `ｃｒｅｄｉｔ` | 6 columns. `今回の手柄` → `Ｔｈｅ　ｃｒｅｄｉｔ　ｔｈｉｓ　ｔｉｍｅ`, `手柄を独り占め` → `ｋｅｅｐ　ｔｈｅ　ｃｒｅｄｉｔ　ｔｏ　ｍｙｓｅｌｆ`. **3 battle (this chunk ×2, chunk 22 ×1) + 1 script.** Free across `tl/` |
| ずらかる | `ｓｃａｒｐｅｒ` | 7 columns. Thieves' cant, which is what the register wants; British, consistent with the defence / armour / grey policy. **The officer's `ずらかるぞ！` → `Ｌｅｔ　ｕｓ　ｓｃａｒｐｅｒ！` keeps the cant but drops the contraction** his men take (`ｌｅｔ’ｓ　ｓｃａｒｐｅｒ`) — a bandit's word in an officer's mouth, which is the joke. **1 battle + 0 script.** Free |
| 蹴散らす | `ｓｃａｔｔｅｒ` | 7 columns. `蹴散らせ！` → `ｓｃａｔｔｅｒ　ｔｈｅｍ！`. Free across `tl/` |
| 先客 | `ｓｏｍｅｏｎｅ　ｇｏｔ　ｈｅｒｅ　ｆｉｒｓｔ` | 23 columns as the full row. Rendered as a clause, not a noun — bare *an earlier guest* has no English use here. The §15.2 黒幕 precedent |
| 記念品 | `ａ　ｋｅｅｐｓａｋｅ` | 11 columns. Free across `tl/` |
| 見劣りする | `ｄｒａｂ`, with the comparison in the neighbouring row | `宝石に比べたら、ちょっと見劣りするけど、` → `Ｎｅｘｔ　ｔｏ　ｔｈｅ　ｇｅｍｓｔｏｎｅｓ` / `ｉｔ’ｓ　ａ　ｂｉｔ　ｄｒａｂ，　ｂｕｔ`. 見劣り is *to compare unfavourably*; `Ｎｅｘｔ　ｔｏ　…` carries the comparison so the adjective need only carry *inferior-looking*. ×2, byte-identical. `ｄｒａｂ` free |
| 決まってら、 | `Ｉｔ’ｓ　ｏｂｖｉｏｕｓ，` | 13 columns. The rough contracted 決まっている. Shares *obvious* with shipped `chunk_004`'s `決まってるでしょ！！` → `Ｉｓｎ’ｔ　ｉｔ　ｏｂｖｉｏｕｓ！！` so the family reads as one; different source strings, different messages |
| かまわん、 | `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ，` | 19 columns. **Not a new form** — `chunk_009` L2 ships the kanji `構わんっ！！` as `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ！！`. One word, two spellings, one English form (§17.2 鬼 / オーガ, §28.3 何っ／ッ), with the source's own punctuation per §5. Held **distinct** from §28.3's まあよい、 → `Ｎｏ　ｍａｔｔｅｒ．` |
| 何だろう・・・ | `Ｗｈａｔ　ｃｏｕｌｄ　ｔｈｉｓ　ｂｅ．．．` | 21 columns. A further member of the 何 family, held apart from 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？` (§23.2), 何っ／ッ！？ → `Ｗｈａｔ！？` (§28.3), 何？ → `Ｗｈａｔ？` (§30.3) and あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2). This chunk carries three of the family and all three are visibly distinct |
| そうだな | `Ｙｏｕ’ｒｅ　ｒｉｇｈｔ．` | 13 columns. Deliberately **not** a fourth string on `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` (§23.2 そうそう, §25.2 そのとおりだ, §30.3 そうよ). そうだな's な expresses *shared assessment with the addressee*, which `Ｙｏｕ’ｒｅ　…` renders and `Ｔｈａｔ’ｓ　…` does not — the distinction §25.2 already draws against そうね → `Ｔｈａｔ’ｓ　ｔｒｕｅ．`. Chunk 20 contains **none** of そうそう / そのとおり / そうよ / そうね, so §25.3's test is met and §25.3's reserved `Ｅｘａｃｔｌｙ．` is **not** spent. **7 battle (8, 18, 19, 20 ×2, 23, 27, 28) + 10 script-unique.** Verified free |
| 仕方ないな。 | `ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` | A fourth member of §24.3 / §29.3's family beside しかたねえ。, 仕方ない、 and 仕方ねえだろ。 Here it is a subordinate clause under `ああ、残念だけど、`, so English grammar requires the expletive: `ｔｈｅｒｅ’ｓ　ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` (23 columns). The fixed words are intact and contiguous; this is grammar, not addition — the §31.4 shape |
| 〜の奴 / 〜の奴ら | `ｔｈａｔ　〜　ｆｅｌｌｏｗ` / `ｍｅｎ` / `ｌｏｔ`, **register-selected** | ⚠️ **Recorded at review; the PR proposed no row and the word had none.** `奴ら` is **56 battle + 22 script** and already carried three English forms before this unit: `Ｔｈｏｓｅ　９ｔｈ　Ａｒｍｙ　ｆｅｌｌｏｗｓ` (`chunk_002` ×2), `Ｃａｒｌｉｎｅ’ｓ　ｍｅｎ` (`chunk_009`), `ｔｈｏｓｅ　Ｅｍｐｉｒｅ　ｍｅｎ` (`chunk_013`). This unit's singular `ヒューゴーの奴` → `ｔｈａｔ　ｆｅｌｌｏｗ　Ｈｕｇｏ` **matches `chunk_002`**; its plural `宮廷軍の奴ら` → `ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ　ｌｏｔ` is a fourth form and is **accepted as register-selected** — *lot* is a bandit's word where *Carline's men* is an officer's. **The word is not fixed; the register is.** Distinct from §31.2's 〜め → `Ｔｈａｔ　〜`, a different source string this unit does not carry |

### 32.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| ぬおっ | `Ｎｗｏｈ` + the source's own punctuation | 4 columns. A grunt of dismayed shock — `ぬおっ・・・・・！` → `Ｎｗｏｈ．．．．．！` (five stops) and `ぬおっ、しまった！` → `Ｎｗｏｈ，　ｄａｍｎ　ｉｔ！`. Transliterated, per グッ → `Ｇｕｈ` / ぐわっ → `Ｇｗａｈ` / ぐふっ → `Ｇｕｆｆ` (§11.5, §14.5). Held **distinct** from §20.3's ぬぬッ → `Ｗｈｙ，`. **3 battle (this chunk ×2, chunk 23 ×1) + 0 script.** Free |
| ああっ！ | `Ａｇｈ！` | 4 columns. A startled cry of alarm, built on §19.1's ううっ → `Ｕｇｈ` (the small っ takes `ｇｈ`). Held **distinct** from §6's ああ (assent) → `Ｙｅａｈ` — **which this chunk also carries**, in file line 49 — and from §23.2's あーあ → `Ａａｈ，`, **also in this chunk**, so none of the three could have been collapsed. **1 battle + 0 script.** Free |
| あ〜あ | `Ａａｈ，` | 4 columns. **Not a new form** — §23.2 fixes `あーあ` → `Ａａｈ，`, shipped ×2 in `chunk_004`. `ー` and `〜` are one word in two spellings, exactly as §29.3 handles くーっ / く〜っ → `Ｔｃｈｈ` |
| ねえ、 | `Ｓａｙ，` | 4 columns. A friendly call for attention. **`Ｈｅｙ，` is spent** — `chunk_006` L9 ships `よう、サイクスか。` → `Ｈｅｙ，　Ｓｙｋｅｓ．` — and §24.3's ちょっと、 → `Ｈｏｌｄ　ｏｎ，` is an interruption, a different act. **4 battle (5, 15, 20, 32) + 16 script.** `Ｓａｙ，` verified free |
| おい、 | `Ｏｉ，` | 3 columns. ⚠️ **Recorded at review; the PR rendered it and proposed no row.** **14 battle (0 ×3, 8, 16, 20, 23 ×2, …) + 10 script.** `Ｏｉ，` exists in `tl/` / `pending/` only in parked `chunk_043`, so this is its **first shipping use** and the form is fixed from here |
| ようし、 | `Ｒｉｇｈｔ，` | ⚠️ **Recorded at review; the PR collapsed it onto §6 / §24.3's `よし、` without a row.** The collapse is correct — one assent word, two spellings, the §11.5 くっ / クッ and §17.2 鬼 / オーガ shape — and the risk is small: **`ようし、` is 1 battle occurrence, this chunk, + 2 script**, against `よし、`'s 52 battle + 20 script. Written down so a later unit cannot "correct" it into a fourth assent string |
| ・・・あれ？ | `．．．Ｗｈａｔ？` | The **dots lead** here where §21.2's `あれ・・・？` → `Ｗｈａｔ．．．？` has them trail. §5's mechanism exactly: the word is fixed, the punctuation sits where the source puts it. Both forms are now shipped and neither corrects the other |

### 32.4 Ruling — `あら` takes `Ｍｙ` plus the source's punctuation, and three shipped files are outliers

**§28.3 stands and is extended: `あら？` → `Ｍｙ？` (3), `あら・・・？` → `Ｍｙ．．．？` (6).** The unit
ships both and is unchanged. But the question was live because shipped work disagrees, so the whole
corpus was gathered at review rather than the five data points the dispatch supplied:

| Chunk | Source | Portrait | Shipped English |
|---|---|---|---|
| 7 L19 | `あら・・・・？` | **02** | `Ｏｈ．．．．？` |
| 7 L24 | `あら、雪・・・？` | — | `Ｏｈ，　ｓｎｏｗ．．．？` |
| 11 L3 | `あら、お客様？` | 08 | `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` |
| 13 L4 | `あら、` | 06 | **`Ｍｙ，`** (§28.3's own instance) |
| 14 L3 | `あら？` | **02** | `Ｏｈ？` |

**12 `あら` rows in the battle dump across chunks 7, 8, 11, 13, 14, 16, 20 ×2, 27 and 29, plus ~30
in the script** — larger than §28.3's "16 further occurrences".

⚠️ **CORRECTION to that census, 2026-09-09 (§4.3, PR #17 review) — see §35.2.** **12 is the raw
substring count; the interjection census is 11.** The twelfth is `あらかた片付いたな。` (chunk 8
message line 15), which is 粗方, *for the most part* — a different word. The chunk list is right and
is unchanged. Measured with the same separation, the script side is **28** unique interjection lines
(the substring count is 31; the false positives are `あらんことを。` ×2, 有らん, and
`日を　あらためて、`, 改めて). **True reach: 11 battle + 28 script-unique = 39. Nothing turns on it
— the ruling below rests on what `Ｏｈ？` already is, not on the count.**

**What decides it is not the count but what `Ｏｈ？` already is.** §24.4 collapsed おや → `Ｏｈ？`
*outright*, on **29 occurrences (6 battle + 23 script)**. `chunk_014` L3's `あら？` → `Ｏｈ？` is
therefore byte-identical to a **different fixed source word**, and matching it would delete a member
of §24.4's set. `Ｍｙ` plus the source's own stop is the systematic move §5 prescribes and §28.3
already ratified. The same-speaker argument (portrait 02 in chunks 7, 14 and 20) is real and is what
made this worth ruling rather than assuming — but it argues for making *one* form consistent, not
for which form, and §24.4 settles which.

⚠️ **CORRECTION to §28.3 (§4.3).** Its sentence *"The alternative `Ｏｈ　ｍｙ，` is also free"* is
**false**, and in a way that matters more than it looks: `Ｏｈ　ｍｙ，` is shipped in `chunk_011` L3
**for `あら、` itself**. §28.3 was ratified on the true observation that `Ｍｙ` was free, while `あら`
had already been rendered three times in the `Ｏｈ` family. The ruling survives — it is the right one
— but its "the alternative is free" reasoning does not, and is struck.

**Lines this affects (§4.3) — ~~four rows in three shipped files~~ ⚠️ FIVE rows in FOUR shipped
files, all width-neutral or shorter. ✅ ALL FIVE APPLIED 2026-09-09 by PR #17 (§35).**

| File | Row | Now | Must become | Cost | |
|---|---|---|---|---|---|
| `tl/battle/chunk_007.txt` L19 | `あら・・・・？` | `Ｏｈ．．．．？` (7) | `Ｍｙ．．．．？` (7) | 0 bytes | ✅ |
| `tl/battle/chunk_007.txt` L24 | `あら、雪・・・？` | `Ｏｈ，　ｓｎｏｗ．．．？` (12) | `Ｍｙ，　ｓｎｏｗ．．．？` (12) | 0 bytes | ✅ |
| **`tl/battle/chunk_008.txt` L4** | **`あら？`** | **`Ｏｈ？`** (3) | **`Ｍｙ？`** (3) | **0 bytes** | ✅ |
| `tl/battle/chunk_011.txt` L3 | `あら、お客様？` | `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` (16) | `Ｍｙ，　ｖｉｓｉｔｏｒｓ？` (13) | −6 bytes | ✅ |
| `tl/battle/chunk_014.txt` L3 | `あら？` | `Ｏｈ？` (3) | `Ｍｙ？` (3) | 0 bytes | ✅ |

⚠️ **The `chunk_008` row was MISSING from this table and is added 2026-09-09 (PR #17 review).**
**§32.4 counted chunk 8 and then dropped it**: the census sentence above names "chunks 7, **8**, 11,
13, 14, 16, 20 ×2, 27 and 29" while this table listed only four rows and none of them was chunk 8's.
`FLAGS.md` §T1 and the wave-5 dispatch both inherited the omission; PR #17's translator found the row
independently and fixed it. It is the female 9th Army companion (portrait `{=000A0001}`, `{FC51}`)
spotting the Imperial advance — `{FFFD}あら？{FFFE}{FC00}{=0000}、来たわ！` — the identical defect on
the identical source string as `chunk_014` L3. See §35.

⚠️ **Deliberately NOT applied in this commit, and the reason is on the record rather than implied.**
PR #15 (script batch 006) is open and unreviewed and reaches this same question from the script side
with ~30 more instances; chunk 19 is mid-rework. Re-cutting three shipped files inside a
battle-chunk merge while two siblings are in flight is the wrong blast radius. This is the §27
corrections-unit shape: the **ruling** binds PR #15, chunk 19 and every later unit from now; the
**re-cut** is owed work, carried in `FLAGS.md` §T and `HANDOFF.md` with the lines and costs above.

✅ **DISCHARGED 2026-09-09 by PR #17** (`f25ff14`), the wave-5 `あら` corrections unit: **five rows in
four files, net −6 bytes, zero `{FFFE}` and zero `{FCC0}` changes, tag stream byte-identical on every
line**. Both blocking conditions held and then cleared exactly as this paragraph predicted — PR #15
merged and conforms (`batch_006` unique 630 ships `Ｍｙ，　ｃｏｌｄ　ｍｅｄｉｃｉｎｅ．．．`), chunk 19
merged and carries no `あら`. **`Ｏｈ　ｍｙ` now occurs 0 times in `tl/` and `pending/`**, and every
`あら` interjection in both trees renders `Ｍｙ`. See §35 and `FLAGS.md` §W.

#### 32.4a The `おかしら` / `将校` / `将軍` gag — three words, and they stayed three words

`Ｓｏｒｒｙ，　Ｂｏｓｓ！` → `Ｙｏｕ　ｆｏｏｌ，` / `Ｉ　ａｍ　ａｎ　ｏｆｆｉｃｅｒ　ｏｆ　ｔｈｅ` /
`Ｅｍｐｉｒｅ！　Ｃａｌｌ　ｍｅ` / `Ｇｅｎｅｒａｌ！　Ｇｅｎｅｒａｌ！！` (9 / 22 / 15 / 18). *Boss* is
unmistakably informal where *Chief* reads as a near-rank in English and would sit too close to
*General*; it is also 4 columns to *Chief*'s 5. The source's doubled `将軍と！！` is kept as the bare
repeat, because the repetition **is** the punchline. The one row ending on a two-letter word
(`Ｃａｌｌ　ｍｅ`) is forced — every alternative either overflows
(`Ｃａｌｌ　ｍｅ　Ｇｅｎｅｒａｌ！　Ｇｅｎｅｒａｌ！！` is 26) or drops the repeat — and *Call me / General!* is
idiomatic across a break.

### 32.5 Ruling — `勲章` → `ｍｅｄａｌ` stands, and the `メダル` collision is LIVE in banks 42–43

**The rendering is correct and unchanged. The justification under it is not, and is replaced.**

The PR discharged the collision with §3's racetrack `メダル` → `ｍｅｄａｌ` (shipped in
`batch_002.tsv`) on §25.3's co-occurrence test, reasoning from "**2 battle**" occurrences. Both
halves fail on measurement at review:

1. **The reach is 4 battle (chunk 20 ×2, chunk 22 ×2) and 59 in `script_dump.txt` / 39 in
   `script_unique.txt`.** The §9 seed said "2 battle" and the PR repeated it; neither mentions the
   script at all.
2. **`勲章` is a major plot item, not a trinket.** It is **`獅子の勲章`** (9×) and **`『獅子の勲章』`**
   (2×) — a royal decoration entrusted by the King, of which Fernando flies a forgery to stage a
   coup: `将軍は今、この勲章の偽物を掲げてクーデタ…`, `フェルナンド将軍の勲章は、偽物だ。`,
   `国王から、その勲章を託された指揮官は…`, and, bearing directly on this chapter,
   `…リーナを襲撃し、勲章を奪っていっただろう。` The medal this chunk's party digs up beside the
   gemstones **is that object**. `ｍｅｄａｌ` is the right base word and
   `Ｌｏｏｋｓ　ｌｉｋｅ　ａ　ｍｅｄａｌ．` is exactly right for characters who do not yet know what they
   hold. For whoever renders the full name: the `『』` takes `“…”` per §12, and 獅子 is the animal,
   which does **not** disturb §1's rejection of `Ｌｉｏｎ` for the katakana name リオン.
3. **§25.3's test, applied as this glossary actually states it, is NOT met.** §25.3's standard is
   "**No chunk and no bank contains both**". Counted at review:

```
banks containing メダル : [42, 43]
banks containing 勲章  : [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,23,25,32,33,40,41,42,43]
banks containing BOTH  : [42, 43]
messages containing both: 0
```

**No message holds both, so nothing is unreadable and no shipped line is re-cut — but banks 42 and
43 hold both, so the collision is LIVE for whoever translates them.** It is recorded here rather
than discharged. **Reserve, if that unit needs the split: `ｔｏｋｅｎ` (5 columns)** — verified free
across `tl/` and `pending/`, and the actual English for a betting token, so the racetrack side is
the one to move and §3's entry would change under §4.3 with `batch_002.tsv` named. Nothing is
changed today.

### 32.6 Ruling — `おかしらぁ！` → `Ｂｏｓｓｓ！`, and `Ｂｏｓｓ！！` is rejected

The PR offered both at 0 bytes and left it to the reviewer. **`Ｂｏｓｓｓ！` is right, and not on
width — both measure 6.** §5's mechanism fixes the **word** and takes the punctuation **from the
source**. The source is `おかしらぁ！`: one exclamation mark, and the lengthening carried in the kana
`ぁ`. `Ｂｏｓｓ！！` would invent a second `！` the source does not have **and** discard the
lengthening the source does — breaking §5 in both halves at once. `Ｂｏｓｓｓ！` puts the extra beat in
the word, which is settled convention (§29.3 くーっ → `Ｔｃｈｈ`, §26.5 ふーむ → `Ｈｍｍ`, §11.5 and
§14.5's laugh beats).

### 32.7 CORRECTION to §12.3 (§4.3) — `ふふ` is not feminine-only, and `ふふっ` joins it

§12.3 glosses ふふ → `Ｆｕｆｕ` as "soft, amused feminine chuckle". The gendering is a description of
where it was **first seen** (the ch.33 sorceress), not a restriction: this chunk's file line 2 opens
with `ふふっ、ヒューゴーの奴、` from a **male** Imperial officer, rendered `Ｆｕｆｕ，`. The note is
corrected to "soft, amused chuckle"; **the English form is unchanged and nothing is re-cut.**

`ふふっ` is also a **new source spelling** and is collapsed onto the same form — one word, two
spellings, the documented kind (§11.5 くっ / クッ, §28.3 何っ / 何ッ, §17.2 鬼 / オーガ). Counted at
review: **`ふふっ` is 1 battle (this chunk only) + 1 script; `ふふ` is 8 battle (20, 28, 31 ×5, 33)
+ 1 script.** Shipped `chunk_033` L20 renders `ふふ、ここまで` as `Ｆｕｆｕ，　ｙｏｕ　ｈａｖｅ　ｃｏｍｅ`, so
the two are byte-identical where they share a shape.

### 32.8 `何だ、` → `Ｗｈａｔ，` is a row-level rendering, not a fixed form

⚠️ **The PR's row called this "an eighth member of the 何 family" and it is not a family member at
all — it is a clause head that English absorbs differently every time.** Counted at review, `何だ、`
is **3 battle (chunks 0, 7, 20) + 5 script-unique**, and the corpus already renders it three ways:

| Where | Source | Shipped English |
|---|---|---|
| `chunk_007` L13 | `何だ、お前は？` | `Ｗｈｏ　ａｒｅ　ｙｏｕ？` |
| `batch_002.tsv` L9 | `何だ、作戦会議中だぞ！` | `Ｗｈａｔ　ｉｓ　ｉｔ？　Ｗｅ　ａｒｅ　ｉｎ` / `ａ　ｗａｒ　ｃｏｕｎｃｉｌ！` |
| `chunk_020` file line 4 | `何だ、カーライン軍か？` | `Ｗｈａｔ，　ｔｈｅ　Ｃａｒｌｉｎｅ` / `ａｒｍｙ？` |

All three are correct for their sentences and **none of them is wrong**; what would be wrong is a
glossary row telling the next translator to write `Ｗｈａｔ，` mechanically. **`何だ、` takes whatever
its own clause needs.** The rest of the 何 family stays fixed and held apart: 何だと？ →
`Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？` (§23.2), 何っ／ッ！？ → `Ｗｈａｔ！？`
(§28.3), 何？ → `Ｗｈａｔ？` (§30.3), あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2), 何だろう・・・ →
`Ｗｈａｔ　ｃｏｕｌｄ　ｔｈｉｓ　ｂｅ．．．` (§32.2). Separately, `どうした、` → `Ｗｈａｔ　ｉｓ　ｉｔ，` **is**
fixed and this unit matches `chunk_007` L19's `どうした、ティミー？` → `Ｗｈａｔ　ｉｓ　ｉｔ，　Ｔｉｍｍｙ？`
byte-for-byte.

### 32.9 Register

| Who | Register |
|---|---|
| **The would-be officer (portrait 09, unnamed)** | The chapter's comic villain, and the register is the joke. Grandiose and self-important, **zero contractions anywhere** — verified mechanically at review, not from the report: `ｉｓ　ｎｏ　ｄｏｕｂｔ　ｓｅａｒｃｈｉｎｇ`, `ｈｅ　ｉｓ　ｆａｒ　ｏｆｆ　ｔｈｅ　ｍａｒｋ．`, `Ｉ　ａｍ　ａｎ　ｏｆｆｉｃｅｒ　ｏｆ　ｔｈｅ　Ｅｍｐｉｒｅ！`, `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ，`, `Ａｎｄ　Ｉ　ｗａｓ　ａｂｏｕｔ　ｔｏ　ｋｅｅｐ　ｔｈｅ　ｃｒｅｄｉｔ　ｔｏ　ｍｙｓｅｌｆ．．．` — §14.6 / §20.5 / §25.5 / §28.6 / §31.7's Imperial-officer column, unchanged. ⚠️ **But his vocabulary is a bandit's** (`ずらかるぞ`, `独り占め`, `わし`), and that is left in the word choice rather than smoothed: a man who talks like a gang leader and demands to be called *General* |
| His men (portraits 0A, 0B) | Polite upward, rough in the mouth (`ましたぜ`, `だぜ`, `ちまった`) — contractions where the sentence offers one (`Ｉｔ’ｓ　ｏｂｖｉｏｕｓ，`, `ｌｅｔ’ｓ　ｓｃａｒｐｅｒ`). 0A carries none in this unit only because no line of his offers a contractible construction |
| **Aries (portrait 08)** | **Fixed from inside the chunk, not assumed** — portrait 02 calls `アリエスさんも、こっちへ来て` and portrait 08 answers on the very next page. Polite です／ます (`埋まってましたけど`), **no contractions** — `ｗｈｅｒｅ　ｔｈｅ　ｇｅｍｓｔｏｎｅｓ　ｌａｙ` / `ｔｈｅｒｅ　ｗａｓ　ａｌｓｏ　ｔｈｉｓ．`, `ｓｏｍｅｔｈｉｎｇ　ｌｉｋｅ　ｔｈｉｓ` / `ｗａｓ　ｂｕｒｉｅｄ　ｈｅｒｅ．．．` — matching §9's seed exactly. Her `{FC00}さん、` **drops the honorific** and carries it in register, per §21.2 |
| The 9th Army party (portraits 00, 01, 02, 0C) | §7 unchanged, contractions throughout. **Portrait 02 is §21.4 / §25.5 / §28.6's unnamed female companion and is again "the one who notices"** — both `あら` lines in this chunk are hers, exactly as §25.5's `Ｗｈａｔ’ｓ　ｗｒｏｎｇ，　Ｓｅｎｅｃａ？` was. She is still unnamed here; if a later chunk names her, re-check §21.4, §25.5 and §32.4 together |

⚠️ **A source oddity, not a typo: `ほーせき` (file line 49) is a childish, drawn-out `宝石`.**
Rendered as the plain word with the childishness carried in register, per §2's politeness rule and
the treatment §29.6 records for chunk 8's `てーこく`. **Not** spelled out as dialect, which §2
forbids. Likewise `おかしらぁ` is expressive lengthening, not a misspelling (§32.6).

⚠️ **Recorded at review, accepted, so they are not rediscovered as defects:** `こんなものが。` →
`ｔｈｅｒｅ　ｗａｓ　ａｌｓｏ　ｔｈｉｓ．` (the *also* is carried by `〜所に`, but it is unflagged);
`埋まっていた所に` → `ｗｈｅｒｅ　…　ｌａｙ` against the mirror message's `埋まってましたけど` →
`ｗａｓ　ｂｕｒｉｅｄ　ｈｅｒｅ` (a §2.1 step 4 width synonym — `ｗｈｅｒｅ　ｔｈｅ　ｇｅｍｓｔｏｎｅｓ　ｗｅｒｅ　ｂｕｒｉｅｄ`
is 30 columns; different source clauses, so §3 is not engaged); and `もんってことさ` → `ｏｕｒｓ　ｎｏｗ．`
(a mild step-5 implication).

---

## 33. Added by chunk 019 (PR #16, merged 2026-09-09)

Rendered in `tl/battle/chunk_019.txt` — chapter 19, Farina, in six scenes: the bridge conversation
between a 9th Army man and Aries; Hugo's mercenaries ambush the squad and drop the country's only
bridge, cutting the road out; the three mutually exclusive parley variants (the governor's envoy /
guard captain Ulf / the no-quarrel plea); the two Imperial soldiers who finish the castle garrison
and decide to kill a Carline prisoner; Governor Felix's long account of the Crystal of Fire, the
bandit Kabala and the treasure hunter Korneff in Marvellous; and Solon's reunion with his elder
brother. **8,065 / 8,192 bytes, slack 127 — 200 text rows, widest 23 with 14 at 23 and none at
24**, no page over 4 text rows. **The wave's tight unit**: 3,325 EN / 1,745 JP = **1.91×** against
a 1.94 ceiling. Merged at **round 2**; all four review findings were accepted and none contested,
and the rework was **−2 bytes**.

⚠️ **Line numbers in this section are MESSAGE lines** (dump body index, 1-based) = the `tl/` file
line **minus one**, the §28 / §30 convention. That is the **third** of the five numbering
conventions now in play in this repo (`FLAGS.md` §O8, §P; glossary §28, §29, §30, §31, §32).
**Locate by content.**

`Ｆａｒｉｎａ` / `Ｃａｒｌｉｎｅ` / `Ｒｏｙａｌ　Ａｒｍｙ` / `ｔｈｅ　Ｅｍｐｉｒｅ` / `ｇａｒｒｉｓｏｎ` /
`ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ` (§2), `Ｍａｒｖｅｌｌｏｕｓ` / `Ｋｏｒｎｅｆｆ` (§21.1), `Ｉｍｐｅｒｉａｌ　ｓｏｌｄｉｅｒ`
(§25.1), `ａｄｖａｎｃｅ　ｐａｒｔｙ` (§29.1), `ｃｏｍｍａｎｄ` for 指揮下 (§28.2), `Ｒｉｇｈｔ，` for よし、
×3 (§24.3), `Ｕｎｄｅｒｓｔｏｏｄ．` for 了解。 and `Ｉ　ｕｎｄｅｒｓｔａｎｄ` for わかりました ×4 (§21.2),
`Ｈｏｗｅｖｅｒ，` (§23.3 — its **eighth** use), `Ｏｈ．` for ほう。 (§24.4), `Ｉ　ｓｅｅ．` for なるほど、
(§30.3), `Ｎｏ，` for いえ、 (§30.3), `Ｙｅｓ．` for ええ。 (§29.3), `Ｙｅａｈ，` for ああ、 (§6),
`Ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ？` for bare どうする？ (chunk 4), `ｒｕｍｏｕｒ` (§26.4) and `ｔｈｅｙ　ｓａｙ`
(§26.6) are used unchanged.

**§29.4's `Ａｇｒｅｅｄ．` reserve is engaged here for the first and so far only time**, exactly as
that ruling anticipated: chunk 19 carries bare `了解。` (message 19) **and** `・・・わかった。`
(message 24) on one map, so 了解 keeps `Ｕｎｄｅｒｓｔｏｏｄ．` and わかった takes
`．．．Ａｇｒｅｅｄ．`. `Ａｇｒｅｅｄ` was re-verified free across `tl/` and `pending/` at this review —
it occurs in no translation file but this one.

### 33.1 People, places and things — eight promotions out of §9, and the cross-unit rule discharged

All eight wave-4 battle seeds are promoted here and struck in §9. **Every one was used exactly as
seeded**, in both units where the term is cross-unit.

| Japanese | English | Note |
|---|---|---|
| アリエス | `Ａｒｉｅｓ` | 5 columns. **Promoted from §9 (wave-4 seed), CROSS-UNIT, used exactly as seeded.** A **PERSON**, female, a travelling performer. **11 battle + 9 script.** ⚠️ **Corroborated from outside both chunks at this review**: `script_unique` carries `アリエスの故郷、ファリーナね。` — *Farina, Aries's home town* — which independently confirms the §9 seed's reading and explains message 1's `旅の巡業で何度か来たことが` |
| ソロン | `Ｓｏｌｏｎ` | 5 columns. **Promoted from §9, used exactly as seeded.** A **PERSON**, male — the Imperial soldier recognised by his elder brother in message 24. **3 battle + 0 script** |
| ヒューゴー | `Ｈｕｇｏ` | 4 columns. **Promoted from §9, CROSS-UNIT, used exactly as seeded.** `ヒューゴー様` → `Ｌｏｒｄ　Ｈｕｇｏ` (9 columns) — 様 → **Lord** for a male superior addressed by his own subordinate, on §28.1's アーバイン様 → `Ｌｏｒｄ　Ｉｒｖｉｎｅ`, the exactly parallel case. Held clear of §21.2's さん rule. **2 battle + 0 script** |
| ノーマン | `Ｎｏｒｍａｎ` | 6 columns. **Promoted from §9, used exactly as seeded.** A **PERSON**, male, of Farina. **1 battle + 3 script** — the script has him leading the rebuilding afterwards (`今は、ノーマンさんたちがふっこーにはげん…`), so the form will be reached again |
| カバラ | `Ｋａｂａｌａ` | 6 columns bare. **Promoted from §9, CROSS-UNIT, used exactly as seeded.** A **PERSON**, male, a dead bandit. `盗賊カバラ` / `カバラという盗賊` → `ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` (17) — see §33.4. **5 battle + 0 script** |
| 火の水晶 / 『火の水晶』 | `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` / `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”` | 15 / 17 columns. **Promoted from §9, CROSS-UNIT, the LONG form in all five instances across both units.** `『…』` → `“…”` per §12's `『知識の書』`. ⚠️ **§9's `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` contingency never fired** — the four chunk-19 rows measure 18 / 18 / 21 / 21 and the unit shipped with 127 bytes spare, so neither unit is re-cut. **5 battle + 22 script**, the script instances being the item-description row |
| トレジャーハンター | `ｔｒｅａｓｕｒｅ　ｈｕｎｔｅｒ` | 15 columns, **lowercase** by the §17.1 species test and the 探検家 → *explorer* precedent (§21.1). **Promoted from §9, used exactly as seeded.** ⚠️ The seed's warning held: the dump splits it `トレジャー|ハンター` across a `{FFFE}`, so a whole-word grep finds zero. **1 battle + 0 script** |
| 傭兵団 | `ｍｅｒｃｅｎａｒｙ　ｂａｎｄ` | 14 columns. **Promoted from §9, used exactly as seeded**, both occurrences byte-identical. The seed's shorter `ｍｅｒｃｅｎａｒｉｅｓ` (12) was **not** taken even in the wave's tightest unit: both instances read as a unit and one form across the chunk is worth 2 characters. **2 battle + 0 script** |
| フェリクス | `Ｆｅｌｉｘ` | 5 columns. **A PERSON**, male — Farina's civil governor, the speaker of message 23. ⚠️ **NOT in the glossary before this merge, despite the wave-4 dispatch telling the translator it was.** It occurred in `glossary.md` exactly once, inside §2's `ファリーナ` evidence note (`ファリーナの自治官フェリクス`), which names him only as evidence that *Farina* is a place and fixes **no English form**. This is a first-use promotion, not a reuse. Plain European reading per §11.4 / §14 / §17.3. **2 battle + 4 script** — the script scenes put him beside Bishop Creus, so the form will be reached again. Alt *Phelix*, *Ferikusu* |
| 自治官 | `ｇｏｖｅｒｎｏｒ` | 8 columns, **lowercase in prose** per the §17.1 species test — a station, not a title an individual holds. **2 battle + 0 script.** `ｍａｇｉｓｔｒａｔｅ` (11) and `ａｄｍｉｎｉｓｔｒａｔｏｒ` (14) both rejected on width and vagueness |
| フェリクス様 | `Ｇｏｖｅｒｎｏｒ　Ｆｅｌｉｘ` | 14 columns, 15 with the vocative comma. 様 takes the English **title of the man's station**, exactly as §24.1 fixed `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` and §26.1 `バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ`, and built like `Ｃｏｍｍａｎｄｅｒ` / `Ｃａｐｔａｉｎ` / `Ｄｏｃｔｏｒ` / `Ｂｉｓｈｏｐ` (§25.1). **Not** §21.2's `〜さん` rule, which drops the honorific — the two patterns stay separate, as §26.1 insists |
| ウルフ | **`Ｕｌｆ`** | 3 columns. A **PERSON**, male — Farina's guard captain, the speaker of the message-7 parley variant. ⚠️ **RULED at review; the PR proposed `Ｗｏｌｆ` and flagged it as the one call that could defensibly go either way. See §33.3.** Also **not** in the glossary before this merge despite the dispatch. **1 battle + 0 script.** Alt `Ｗｏｌｆ` recorded and **rejected** |
| 衛兵隊長 | `ｇｕａｒｄ　ｃａｐｔａｉｎ` | 14 columns. Built on §2's 隊長 → captain. Kept **distinct** from 守備兵 → *garrison* (§2) and 警備兵 → *guards* (§23.1) — three source words, three English forms, and 守備兵 occurs **four times in this very chunk**, so they could not collapse. **1 battle + 0 script** |
| 使いの者 | `ｅｎｖｏｙ` | 5 columns. Deliberately **not** `ｍｅｓｓｅｎｇｅｒ`, which §30.2 fixes for 伝令, nor `ｃｏｕｒｉｅｒ` (連絡員, §30.2). Consistent with `闇の使い` → `ｔｈｅ　ｄａｒｋ　ｅｎｖｏｙ` shipped in `batch_003` — 使い → *envoy* is already house practice. **1 battle + 0 script** |
| ファリーナ城 | `Ｆａｒｉｎａ　Ｃａｓｔｌｅ` | 13 columns, on §2's `カーライン城` → `Ｃａｒｌｉｎｅ　Ｃａｓｔｌｅ` |
| 財宝 | `ｈｏａｒｄ` | 6 columns. `このカバラの財宝` → `Ｋａｂａｌａ’ｓ　ｈｏａｒｄ．` Kept **distinct** from 宝 / お宝 → *treasure* (§32.1), which this chunk also carries — the source draws the distinction itself and *hoard* is what a dead bandit leaves |
| 宝石 | `ｇｅｍｓｔｏｎｅ` | **8 columns** (⚠️ **corrected in place 2026-09-09, §4.3, PR #26 review — this cell read “9”.** `len()` = 8. Same error as §32.1's, corrected with it; see §45.4). **Ruled at this review — see §33.5.** Never a §9 seed row; the entry is here and at §32.1. **6 battle (19 ×1, 20 ×4, 31 ×1) + 4 unique script lines.** ✅ **Chunk 31 has now rendered it** (PR #26, `ｂｒｏｗ` / `ｇｅｍｓｔｏｎｅ　ｓｅｌｌｓ　ｆｏｒ　ａ`), inheriting it exactly as this row directed |

### 33.2 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| 何てこった、 | `Ｗｈａｔ　ａ　ｍｅｓｓ，` | 15 columns. Dismay at a bad situation, not a curse. Held **distinct** from §29.3's やれやれ、 → `Ｇｏｏｄ　ｇｒｉｅｆ，` (weary exasperation), §6's まったく → `Ｒｅａｌｌｙ，` and §23.2's 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？`. `ｍｅｓｓ` verified free across `tl/` (`pending/chunk_017`'s hit is `ｍｅｓｓｅｎｇｅｒ`) |
| ああっ、 | `Ａｈｈ，` | 4 columns. Startled cry as the bridge falls. ⚠️ **A sixth member of the あ family and deliberately not `Ａａｈ，`**, which §23.2 fixed for あーあ and which is **shipped twice in `chunk_004`**. Kana beats tracked per §11.5 / §14.5 (two あ → the doubled letter), while staying clear of あ、 → `Ａｈ，` (§6), あーあ → `Ａａｈ，` (§23.2) and あ〜ん → `Ａａａｈ，` (§24.3). `Ａｈｈ` verified free |
| 申し訳ない。 | `ｆｏｒｇｉｖｅ　ｍｅ．` | 10 columns. ⚠️ **Held apart from three "sorry" forms already fixed**: §24.2's 残念ながら → `Ｉ　ａｍ　ｓｏｒｒｙ　ｔｏ　ｓａｙ` (the near-miss — same speaker type, same formality), §28.3's あいにく → `Ｓｏｒｒｙ，`, §30.3's ごめんね。 → `Ｉ’ｍ　ｓｏｒｒｙ．`. `Ｍｙ　ａｐｏｌｏｇｉｅｓ．` was rejected: it is free, but makes the row exactly **24** columns beside `Ｈｏｗｅｖｅｒ，`. ⚠️ **`ｆｏｒｇｉｖｅ` now renders two source words across `tl/`** — 許す → *forgive* is shipped in `chunk_007` L14 and `chunk_010` L3/L7. Different messages, so §3 is not engaged, and §25.3's co-occurrence test is met: chunk 19 contains no 許す at all. Different senses, too — refusing forgiveness against asking for it |
| はたして (rhetorical) | `ｗｈｏ　ｃａｎ　ｓａｙ` | 14 columns. `今ははたして、誰の手に渡っていることか・・・` → `Ｉｎｔｏ　ｗｈｏｓｅ　ｈａｎｄｓ　ｉｔ` / `ｈａｓ　ｐａｓｓｅｄ　ｎｏｗ，` / `ｗｈｏ　ｃａｎ　ｓａｙ．．．` |
| よりによって、 | **`ｏｆ　ａｌｌ　…`**, the complement following the source | ⚠️ **Recorded at review; neither PR proposed a row and the phrase had none, yet all three of its occurrences are now shipped.** `よりによって、厄介なところへ…` → `Ｏｆ　ａｌｌ　ｐｌａｃｅｓ，　ｗｅ’ｖｅ` / `ｌａｎｄｅｄ　ｉｎ　ａ　ｎａｓｔｙ　ｓｐｏｔ．` here; `chunk_008` ships the byte-identical row `よりによって、` as `Ｏｆ　ａｌｌ　ｔｉｍｅｓ，`; `chunk_004` ships `よりによって　この私を` as `ｔｏ　ｓｅｎｄ　ｍｅ，　ｏｆ　ａｌｌ`. **This is not a divergence to fix.** よりによって takes its complement from context and English does the same — chunk 19's is a place (`厄介なところ`), chunk 8's a time. **What is fixed is `ｏｆ　ａｌｌ`; the noun follows the source**, which is §5's word-plus-source-punctuation mechanism generalised one step. §3 is not engaged (different messages), and **all 3 battle occurrences are now rendered**, so the phrase is closed |
| どうやら、 | **`Ｌｏｏｋｓ　ｌｉｋｅ　…`** for a CASUAL speaker / **`…　ｓｅｅｍ(ｓ)　…`** for a FORMAL one | ⚠️⚠️ **SCOPE CORRECTED 2026-09-09 (§4.3, PR #23 review) — this row was written as a blanket form and the corpus does not support one; see §41.4. `Ｌｏｏｋｓ　ｌｉｋｅ` is right for the speakers it was written from and wrong for a contraction-free one, and three shipped `seem` renderings PREDATED it and were not counted.** The row's original text follows unchanged: ⚠️ **Fixed here at review rather than left open.** Chunk 19 absorbs it into `Ｌｏｏｋｓ　ｌｉｋｅ　ａ` / `ｍｅｒｃｅｎａｒｙ　ｂａｎｄ．` with no standing form, and the PR's Flag 15 asked for one because **it reaches four more chunks — 23, 25, 30 and 31**. Fixing it now rather than letting four units each invent one. Held **distinct** from the hearsay evidentials of §26.6 (`らしい` → *they say* / *Word is*): どうやら is the speaker's own **inference from what he can see**, not report of another's word — which is exactly why chunk 19's ambush line takes it |

### 33.3 Ruling — `ウルフ` takes `Ｕｌｆ`, because `ｗｏｌｆ` is already shipped for a creature

§9 offered no reading for this name at all — it was never seeded, and the wave-4 dispatch wrongly
told the translator it was already fixed. The PR proposed **`Ｗｏｌｆ`** with `Ｕｌｆ` recorded as the
alternative, and asked the reviewer to rule. **Ruled: `Ｕｌｆ`.** Three reasons, in order of weight:

1. **`ｗｏｌｆ` is not free — it is already shipped, for a monster.** Counted at review, and the
   figure is the translator's recount rather than the reviewer's first, looser one:
   `tl/script/batch_003.tsv` renders it across **2 unique lines at 21 instances each = 42 message
   instances** — L39 `鋭い爪と牙を持つ凶暴な狼のモンスター。` → `Ａ　ｓａｖａｇｅ　ｗｏｌｆ　ｍｏｎｓｔｅｒ，…`
   and L40 `キラーウルフが進化した狼の怪物。` →
   `Ａ　ｗｏｌｆ　ｍｏｎｓｔｅｒ　ｅｖｏｌｖｅｄ　ｆｒｏｍ　ｔｈｅ　ｋｉｌｌｅｒ　ｗｏｌｆ．` ⚠️ **L40's source key
   contains the katakana `ウルフ` itself**, so the mapping ウルフ → `ｗｏｌｆ` is *literally shipped*,
   not merely inferred from the kanji 狼.
2. **The project has rejected an English-common-word reading three times, and this is the sharpest
   case.** §1 rejected `Ｌｉｏｎ` for リオン ("would read as the animal"), §17.2 rejected `Ｎｅｒｇａｌ`
   for ネルガリ, and §28.5 rejected `Ｒｅｂａｒｋ` for レバーク, weighting it by context: "a kingdom
   whose king announces himself — the worst possible place for a name that reads as a verb."
   Chunk 19 is that context exactly — **a guard captain announcing himself by name**,
   `私は、ファリーナの衛兵隊長、ウルフと申します。` — and unlike those three the colliding word is not
   merely an English common noun but a **shipped creature name in this very project**.
3. **`Ｕｌｆ` is equally a genuine European name** — the Norse form, and also spelled ウルフ — and sits
   in the same Germanic set as Bauer, Helfer, Krippen, Leverk, Leclerc. `Ｕｌｆ` verified **free**
   across `tl/` and `pending/`. §17.4's plain-transliteration preference (ネルガリ → `Ｎｅｒｇａｌｉ`)
   is satisfied by either, so it does not decide against this.

**Cost: −2 bytes**, one row, no re-flow (`Ｗｏｌｆ．` 5 → `Ｕｌｆ．` 4). **Lines this affects: one**,
the only occurrence in either dump. After this merge, changing it is a §4.3 correction.

### 33.4 Ruling — `盗賊` takes `ｂａｎｄｉｔ` on a person and keeps §4's `ｔｈｉｅｆ` as the class label

§4 fixes 盗賊 → *thief* and the PR departed from it deliberately, asking for a ruling. **Ratified:
both forms stand, and the split is required rather than merely defensible.**

This is **§24.2's 弓兵 / 弓使い ruling applied to a new pair**. §4's row sits in the *Classes and
class descriptions* table — it is the label in the unit roster — while `カバラという盗賊` /
`盗賊カバラ` is an **epithet on a named individual**, which is the shape §24.2 split when it gave
弓兵 → *archer* (class) and 弓使い → *bowman* (epithet), taking the seed's own alternative.

**Counted at review across both dumps: 3 battle** (chunk 19 ×2, chunk 20 ×1) **+ 2 unique script
lines** — and both script lines are **class descriptions**, `村での略奪をなりわいとする盗賊。` and
`高い機動力を持つ馬に乗った盗賊。`, 21 instances each. Those two **must keep `ｔｈｉｅｆ`**: they are
roster entries in the very table §4 governs. So a single English form is not available in either
direction, and the split is forced by the corpus.

⚠️ **`ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` is rendered once, not twice** — the PR's additions table said
twice. Message 23's second mention, `カバラという盗賊は`, renders as bare `Ｋａｂａｌａ　ｗｏｕｌｄ　ｓｔｅａｌ…`,
dropping 盗賊 because the referent was identified one page earlier. That is the §2.1 **step 3**
redundant-gloss case (§24.2's `先代の神父` → *my predecessor* precedent), not a step-5 departure, so
it needed no flag. Recorded so the wording is not read as a §3 obligation.

### 33.5 Ruling — `宝石` takes `ｇｅｍｓｔｏｎｅ`, and shipped `ｇｅｍ` is recorded, not re-cut

Ruled at chunk 19's review and shipped consistently by chunk 20 in the same wave (§32.1). The
argument neither PR could make rests on the **untranslated** part of the corpus, counted here:
**6 battle occurrences** (19 ×1, 20 ×4, 31 ×1) **and 4 unique script lines, of which only one is
translated.**

The decisive line is one of the three still untranslated:
`なめらかな肌触りをした硬質な石。宝石として珍重する地方もある。` — **21 message instances** — where 宝石
is a bare **category noun** ("some regions prize it as a 宝石"). `ｇｅｍ` cannot serve it, because
that line, like every line in that table, ends `ジェムタイプ：…` → **`Ｇｅｍ　Ｔｙｐｅ：…`**. The one
shipped `ｇｅｍ` already demonstrates the hazard: `batch_003` L36 renders `額に宝石のはまった謎の生物。`
as `…ｗｉｔｈ　ａ　ｇｅｍ　ｉｎ　ｉｔｓ　ｂｒｏｗ．` and carries `Ｇｅｍ　Ｔｙｐｅ：Ｃｙｃｌｅ` **two rows later in
the same message.** `ｇｅｍｓｔｏｎｅ` is the only form that stays visibly clear of both `Ｇｅｍ`
(ジェム, the pickup, §3) and `Ｊｅｗｅｌ` (ジュエル, the currency, §3).

**Lines this affects: none.** `batch_003` L36 is **recorded, not re-cut** — the §20.4 / §23.1 /
§24.5 / §27.4 shape, a different message, and *a gem in its brow* is the right English for an
ornament set in a creature's head where *a gemstone in its brow* is clumsy. So 宝石 has **two
English forms split by function**: `ｇｅｍｓｔｏｎｅ` the default category noun, `ｇｅｍ` inside the
fixed phrase 額に宝石. That is the §4 石化能力 / §27.1 愛用 / §30.2 油断 "one word, two shapes"
pattern. **Chunk 31 and the three untranslated script lines inherit `ｇｅｍｓｔｏｎｅ`.**

### 33.6 CORRECTION to §31.3 (§4.3) — `まさか` → `Ｓｕｒｅｌｙ` is over-broad, and two of its stated facts are wrong

§31.3 was written one PR earlier (chunk 18, PR #13) and fixes `まさか、` → `Ｓｕｒｅｌｙ`, naming
chunk 19 among the 13 chunks it binds. **Chunk 19 is the unit that tests it, and it does not hold
as written. No rendering changes anywhere; the entry does.**

**1. The word covers two constructions and `Ｓｕｒｅｌｙ` fits only one.** Counted across
`battle_dump.txt` at this review, the 18 occurrences split:

| Construction | Count | Chunks | Takes |
|---|---|---|---|
| incredulous / negative supposition — `まさか…か？`, bare `まさか・・・` | **8** | 0, 17, 18, 19, 25, 27, 39 ×2 | **`Ｓｕｒｅｌｙ`** |
| exclamative — `まさか…とは / とはな` | **10** | 19, 23 ×2, 24, 26, 27, 30, 32 ×2, 43 | **not `Ｓｕｒｅｌｙ`** |

Chunk 19 carries one of each, and renders them correctly:
`その声は、まさか・・・` → `Ｔｈａｔ　ｖｏｉｃｅ，　ｓｕｒｅｌｙ．．．` (conforming), and
`まさか、帝国の兵士になっているとはな。` → `Ａｎ　Ｉｍｐｅｒｉａｌ` / `ｓｏｌｄｉｅｒ，　ｏｆ　ａｌｌ　ｔｈｉｎｇｓ．`
`Ｓｕｒｅｌｙ` would invert the sense there — *"Surely you have become an Imperial soldier"* asserts
what 〜とはな marks as astonishing. **The 〜とは construction means *to think that…!* and takes the
English that fits its own clause**; `ｏｆ　ａｌｌ　ｔｈｉｎｇｓ` is chunk 19's, and the ten exclamative
instances are **not** bound to a single form by this entry.

**2. "`Ｓｕｒｅｌｙ` is otherwise free across `tl/`" is false.** Three shipped lowercase
`ｓｕｒｅｌｙ` already render two *other* Japanese words: `指輪を　渡したはずだ。` →
`ｔｈｅ　ｒｉｎｇ，　ｓｕｒｅｌｙ．` (`chunk_000` file L14, はずだ) and `あなたは　きっと` →
`ｙｏｕ　ｗｉｌｌ　ｓｕｒｅｌｙ　ｂｅｃｏｍｅ` (`chunk_007` file L20), `きっと俺たちを倒しに` →
`ｔｈｅｙ’ｖｅ　ｓｕｒｅｌｙ　ｃｏｍｅ` (`chunk_034` file L2). All are lowercase, mid-sentence, in
different messages, so §3 is not engaged and none is re-cut — but the form was never free.

**3. §31.3 lists chunk 0, and chunk 0 contradicts it.** `chunk_000.txt` file L14 already ships
`まさか、` / `お前たちが・・・・` as **`Ｉｔ　ｃａｎ’ｔ　ｂｅ，`** / `ｔｈａｔ　ｙｏｕ．．．．` — an
incredulous instance that does *not* take `Ｓｕｒｅｌｙ`. The row was contradicted by shipped work at
the moment it was written. Chunk 0 stays **recorded, not re-cut**: it has 27 bytes of slack and
§18.3 records that its next correction needs a full re-cut.

**Read §31.3's row as:** `まさか` → **`Ｓｕｒｅｌｙ`** where the clause is an incredulous question or
negative supposition, which is the use both shipped instances have (`chunk_018`,
`pending/chunk_017`) and the use it was written for; **the `まさか…とは` exclamative is a different
construction and takes the English its own clause needs**, recorded per instance. `Ｓｕｒｅｌｙ` is
shared with はずだ and きっと in three shipped rows. **Lines this affects: none.**

### 33.7 Register

| Who | Register |
|---|---|
| Aries (portrait 05) | Polite, warm, **no contractions** — `Ｎｏ．　Ｉ　ｈａｖｅ　ｔｏｕｒｅｄ　ｈｅｒｅ`, `Ｉｔ　ｉｓ　ｓｍａｌｌ，　ｂｕｔ　Ｉ　ｌｏｖｅ　ｔｈｉｓ　ｃｏｕｎｔｒｙ．`, `Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ　ｉｔｓ　ｎａｍｅ，`, `Ｗｉｔｈ　ｔｈｉｓ，　ｗｅ　ｃａｎ　ｍａｎａｇｅ．` ⚠️ **Her speaker identification was verified from the tag stream at review, not assumed**: message 23's `名前は知らないのですが、` opens `{FCB0}{=00050001}{FC51}`, and portrait **05** is fixed as Aries by message 1's `{FCB0}{=00050000}{FC50}` — same id, opposite channel byte, the §23.5 / §28.7 / §30.7 pattern. She is also portrait 05 in message 20. That is what puts her contraction-free voice beside a player character who contracts freely |
| Governor Felix (portrait 09) | Formal, courteous and self-effacing, **no contractions** — `Ｉ　ａｍ　Ｆａｒｉｎａ’ｓ　ｇｏｖｅｒｎｏｒ，`, `Ｔｒｕｌｙ，　ｗｉｔｈｏｕｔ　ｙｏｕｒ　ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ`, `Ｈｏｗｅｖｅｒ，　ｆｏｒｇｉｖｅ　ｍｅ．`, `Ｉ　ｒｅｃｏｍｍｅｎｄ　ｉｔ．`, `Ｔｈｉｓ　ｍｕｃｈ　ｉｓ　ｎｏｔｈｉｎｇ．` §24.6's Bernard's-church priest column, extended to a civil official |
| The envoy and Ulf (the two named parley speakers) | Formal and pleading, **no contractions** — `Ｉ　ｂｅｇ　ｙｏｕ．`, `Ｗｉｌｌ　ｙｏｕ　ｎｏｔ　ｌｅｎｄ　ｕｓ　ｙｏｕｒ　ｈｅｌｐ？`, `Ｉ　ｕｎｄｅｒｓｔａｎｄ！` The three variants are mutually exclusive and share six segments; **every shared segment is byte-identical across all three**, verified positionally at review |
| Hugo and his mercenaries (portraits 07, 0C) | Curt and commanding — `Ｒｉｇｈｔ，　ｄｒｏｐ　ｔｈｅ　ｂｒｉｄｇｅ！`, `Ｃｕｔ　ｔｈｅｍ　ｏｆｆ　ｆｒｏｍ　ｔｈｅ　ｏｕｔｓｉｄｅ．` His subordinate is deferential, `Ｌｏｒｄ　Ｈｕｇｏ，`, Albert's shape (§20.5) |
| The 9th Army (portraits 00, 01, 06, 0E) | §7 unchanged — casual, contractions throughout: `ｗｅ’ｄ　ｄｏ　ｂｅｓｔ　ｔｏ`, `ｔｈｅｙ’ｒｅ　ｃｏｍｉｎｇ`, `Ｉ’ｄ　ｒａｔｈｅｒ　ｈｉｄｅ`, `ｓｅｅｍｓ　ｗｅ　ｃａｎ’ｔ．`, `Ｗｈｏｓｅ　ｍｅｎ，　Ｉ　ｃａｎ’ｔ　ｓａｙ．` |
| Solon and his elder brother (portraits 03, 04) | Rough and warm, contractions — `Ｉｓｎ’ｔ　ｔｈａｔ　Ｓｏｌｏｎ！！`, `Ｎｏｗ　ｔｈａｔ　Ｉ’ｍ　ｈｅｒｅ，`, `Ｉ’ｌｌ　ｌｅｎｄ　ａ　ｈａｎｄ．` Solon's one formal beat is `．．．Ａｇｒｅｅｄ．`, which is §29.4's reserve and not a register slip |

### 33.8 Two duplicate-check traps this unit leaves behind

Both were predicted by the PR and **both were independently reproduced by the reviewer's own
checker**, which is why they are written down rather than left to bite the next sweep.

1. **`どうする？` reads as DIVERGENT to any index-based row checker.** Message 19 re-flows
   `あのカーライン兵は` / `どうする？` into `Ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ　ａｂｏｕｔ` / `ｔｈａｔ　Ｃａｒｌｉｎｅ
   ｓｏｌｄｉｅｒ？` (the unit's single §2.1 step-6 reorder, deliberate — it removes a lowercase
   `ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ？` row that would have sat one character from the fixed form). The row
   index shifts, so a positional checker pairs the wrong rows. **Chunk 19 does carry
   `Ｗｈａｔ　ｄｏ　ｗｅ　ｄｏ？` byte-identically** at message 3. ⚠️ Counted at review: that string is
   shipped in **five** files — `chunk_000`, `chunk_004`, `chunk_008`, `chunk_019` and
   `pending/chunk_005` ×2 — so it is among the most entrenched fixed rows in the project.
2. **Ellipsis checkers that STRIP tags instead of SPLITTING on them report a false failure at
   message 24.** Stripping glues `ｌｅｔ’ｓ　ｆｉｇｈｔ．` onto the next message's `．．．Ａｇｒｅｅｄ．`
   and invents a run of four dots. Split on tags and the profile matches on every message,
   including the deliberate **two**-dot `ｏｆ　Ｆｉｒｅ．．` (message 23, `火の水晶を・・`). Same class
   of trap as §24.5's `さあ、` / `よし、` before a `{FC00}` and §27.4's spaced / unspaced village line.

⚠️ **Also recorded, so a later reviewer does not "fix" them:** three rows end in a one- or
two-letter word — `…ｂｕｔ　Ｉ` (message 1), `Ｌｏｏｋｓ　ｌｉｋｅ　ａ` (message 3) and
`ｂｕｔ　Ｉ　ｈｅａｒ　ｉｔ　ｉｓ　ａ` (message 23). Each mirrors the source's own break segment for
segment, which `translation_prompt.md` §3.2 says should normally be preserved, and none is
compounded by an orphan row or a page at the four-row wall. **They stand.** The one row-final lone
`ａ` that *was* corrected at review stacked all three faults at once — it also orphaned a 5-column
`ｌｅａｄ．` and sat on a page carrying a leading blank plus four text rows.

---

## 34. Added by script batch 006 (PR #15, merged 2026-09-09)

Rendered in `tl/script/batch_006.tsv` — `script_unique.txt` unique lines **319, 335 and 599–646**,
50 unique lines / **53 message instances**, banks **12–15**: the shop and merchant dialogue. Four
speakers share one skeleton (greeting · buy/sell/leave menu · "which one?" · price confirm · thanks ·
declined · not enough money · pack full · "you shouldn't sell that" · nothing to sell · "anything
else?" · goodbye), so **register is the only thing holding them apart** — the keigo shop (599–612),
the shopkeeper's daughter minding the shop for her sick father (613–628, and 630–631 for the cure and
his gift), a rough male shopkeeper (629), the odd-job lad (632) and the hobbit shop (335, 633–646).
**1,332 JP → 2,513 EN readable characters = 1.89×**; banks 12/13/14/15 **10,321 / 13,449 / 13,493 /
13,433 → 8,639 / 12,727 / 13,455 / 13,395** free, −2,480 bytes, no bank negative; **banks 41 (353) and
40 (471) byte-for-byte untouched**. Widest row **23, none at 24**. Merged at **round 1**, with zero
findings requiring a change to the unit.

⚠️ **This section claimed §34 at commit time**, read off the file's last heading immediately before
writing and not reserved — glossary ended at §33 and `FLAGS.md` at §U. Wave 3 lost work to two
reviewers both holding §28 and wave 4 nearly repeated it at §32.

⚠️ **Numbering here is `script_unique.txt` DATA index** (the file carries five header lines, so data
index = file line − 5). That is the script convention and the **sixth** numbering convention in this
repo (`FLAGS.md` §O8, §P; glossary §28, §29, §30, §31, §32, §33). **Locate by content.**

`Ｉ　ｓｅｅ．` for そうですか。 (§30.3, ×4), `Ｍｙ，` for あら、 (§32.4), `Ｏｈ？` for おや？ and
`Ｏｈ，` for おお、 (§24.4), `Ｂｕｔ，` for でも、 (§23.3), `Ｔｒｕｌｙ，` for 確かに、 (§28.3),
`Ｗｈａｔ．．．？`/`Ｗｈａｔ？` for あれ (§21.2 under §5's punctuation rule), `Ｗｅｌｌ　ｔｈｅｎ，` for
それでは、 (`chunk_008`), `Ｈｅｙ，` for よう、 (`chunk_006` L9), `ｉｔｅｍ` for アイテム (`batch_005`,
§21.3), `Ｆａｔｈｅｒ` for お父さん (§25.4), `ｌｏｏｋｓ　ｌｉｋｅ` for みたい, `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．`
matching `chunk_010` L11, `Ｔｈａｎｋ　ｙｏｕ　ｖｅｒｙ　ｍｕｃｈ` matching `chunk_003` L4, and
`Ｂｙ　ｔｈｅ　ｗａｙ，` matching `chunk_009` L10 **byte-for-byte** are used unchanged. The `ノロ` tic is
rendered **22 times, every one in §18.1's spaced form `，　ｎｙｏｒｏ．` carrying the source's own stop**
(`．`×8, `？`×8, `！`×3, `！！`×2, plus the notice's `．”`).

**The three rulings that post-date this PR's draft, checked one by one at review:**
**(a)** §32.4's `あら` → `Ｍｙ` + the source's punctuation **binds and the unit conforms** — `あら`
occurs exactly once (unique 630) and ships `Ｍｙ，　ｃｏｌｄ　ｍｅｄｉｃｉｎｅ．．．`; the PR reached the same
answer independently from the script side and its five-row census corroborates §32.4's twelve.
**(b)** §33.6's narrowed `まさか`: **`まさか` count in this unit is 0**, so it is not engaged.
**(c)** §33.5's `宝石` → `ｇｅｍｓｔｏｎｅ`: **`宝石`, `宝` and `ジェム` are all 0** here. What the unit
carries is `ジュエル`, §3's currency, and it is kept clear of both — see §34.1.

### 34.1 Shop vocabulary first rendered here

| Japanese | English | Note |
|---|---|---|
| ジュエル | `Ｊｅｗｅｌｓ` | 6 / 7 columns. **FIRST RENDERING IN THE PROJECT — promoted, and the form is §3's, not new.** §3 fixed ジュエル → *Jewel*, "do not translate as gem", but `Ｊｅｗｅｌ` in any casing occurred **nowhere** in `tl/` or `pending/` until now. ⚠️ **Seven instances, not the PR's six** — recounted at review against seven `ジュエル` in the source (unique 600, 603, 606, 616, 622, 636, 641), all plural. Held clear of ジェム → `Ｇｅｍ` (§3, **147×** in `tl/`) and 宝石 → `ｇｅｍｓｔｏｎｅ` (§33.5) |
| いらっしゃいませ / いらっしゃい / いらっしゃいノロ | `Ｗｅｌｃｏｍｅ` + the source's own punctuation (+ tic) | 7 columns. Three source spellings, one English word — the §17.2 鬼 / オーガ collapse. `Ｗｅｌｃｏｍｅ！` (613), `Ｗｅｌｃｏｍｅ！！` (632), `Ｗｅｌｃｏｍｅ，　ｎｙｏｒｏ！！` (634). ⚠️ **Shares its English with `ようこそ` → `Ｗｅｌｃｏｍｅ，` (`chunk_007` L15, shipped) and §25.3's test is NOT met — see §34.5.** The collapse stands on other grounds; the collision is live in bank 26 |
| お客様 / お客さん (vocative) | **dropped; carried by the second person** (`ｙｏｕ` / `ｙｏｕｒ`) | §2's rule for politeness with no English lexical equivalent, and **§30.2's `兵隊さん` → `ｓｏｌｄｉｅｒｓ` third pattern** — `さん` on a common noun, so neither §21.2's `〜さん`-on-a-personal-name rule nor §2's comic トカゲさん → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ`. 4 instances (603, 610 keigo; 619, 626 the daughter). ⚠️ **`ｖｉｓｉｔｏｒｓ` is NOT available**: verified at review by positional pairing — `chunk_011` L3 `あら、お客様？` → `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` and `chunk_035` L2 `お客様とはめずらしい。` → `Ｖｉｓｉｔｏｒｓ　…　ｍａｎｓｉｏｎ？　Ｈｏｗ　ｒａｒｅ．`, both the *guest-at-a-house* sense, plus `chunk_033` L2's `Ｎｅｗ　ｖｉｓｉｔｏｒｓ，` for a supplied subject. **§32.4's owed re-cut of `chunk_011` L3 keeps `ｖｉｓｉｔｏｒｓ`**, so the form stays spent. **No gendered vocative** (`ｓｉｒ`) was introduced, correctly — §10.7 leaves player gender open. The keigo/plain contrast survives message-wide in the syntax: `Ｉ　ｂｅｇ　ｙｏｕｒ　ｐａｒｄｏｎ，　ｂｕｔ　ｙｏｕ　ｓｅｅｍ　ａ　ｌｉｔｔｌｅ　ｓｈｏｒｔ` against `Ｉｔ　ｌｏｏｋｓ　ｌｉｋｅ　ｙｏｕ　ｄｏｎ’ｔ　ｈａｖｅ　ｅｎｏｕｇｈ` |
| 品 | `ａｒｔｉｃｌｅ` | 7 columns. **Held distinct from アイテム → `ｉｔｅｍ` (§21.3, `batch_005`), and the split is FORCED — see §34.4.** `ａｒｔｉｃｌｅ` verified free across `tl/` and `pending/`. 3 instances (605, 609, 640) |  ⚠️ **REACH NOTE ADDED 2026-09-11 (§4.3, PR #35 review) — the ruling and the rendering are UNCHANGED, and §34.4's split is intact.** This row's own reach cell names three lines, all in the keigo shop's sell branch. **`tl/script/batch_012.tsv` DATA 376 is a fourth occurrence and it ships `ｇｏｏｄｓ`, not `ａｒｔｉｃｌｅ`** — `奴の　盗んだ品が` → `Ｔｈｅ　ｇｏｏｄｓ　ｈｅ　ｓｔｏｌｅ　ａｒｅ`. **This is NOT a §34.4 violation**: §34.4 forbids collapsing `品` onto `アイテム` → `ｉｔｅｍ`, and that unit keeps them apart (`アイテム` → `ｉｔｅｍｓ` at DATA 362). It is a second English for one sense, and it is **recorded as §4.3 debt rather than reworked**, because PR #35 was at round 3 and the variance is one noun in one row. **Measured both ways with `len()` at review and width forced nothing:** `ｇｏｏｄｓ` 5, `ａｒｔｉｃｌｅｓ` 8; the page wraps **three rows either way** — shipped 22/20/10, the conforming form 21/20/14 at the ≤23 preference — so the fix is **+6 bytes into bank 0, which has 31,431 free, with no re-flow and no tag change**. A corrections unit should take it. See `FLAGS.md` §AP |
| 失礼ですが | `Ｉ　ｂｅｇ　ｙｏｕｒ　ｐａｒｄｏｎ，` | 18 columns. The **phrase** is byte-identical in both instances; ⚠️ **the ROWS are not, and the PR's "twice, byte-identical" overstates it** — 603 renders `お客様、失礼ですが` as `Ｉ　ｂｅｇ　ｙｏｕｒ　ｐａｒｄｏｎ，　ｂｕｔ` (22) and 610 renders `失礼ですが、` as `Ｉ　ｂｅｇ　ｙｏｕｒ　ｐａｒｄｏｎ，` (18). Two different source strings, both correct. Held **distinct** from §24.3's すいません。 → `Ｅｘｃｕｓｅ　ｍｅ．` and §27.1's すみません。 → `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` — three source strings, three jobs. Free across `tl/` |
| 残念です (a shop's regret) | `ａ　ｓｈａｍｅ` | Three source strings, three renderings, one noun: `それは　残念です。` → `Ｔｈａｔ　ｉｓ　ａ　ｓｈａｍｅ．` (602, 16), `誠に　残念です。` → `Ａ　ｇｒｅａｔ　ｓｈａｍｅ．` (608, 14), `そりゃ、残念ノロ。` → `Ｔｈａｔ’ｓ　ａ　ｓｈａｍｅ，　ｎｙｏｒｏ．` (335, 22). Held **distinct** from 残念ながら → `Ｉ　ａｍ　ｓｏｒｒｙ　ｔｏ　ｓａｙ` (chunk 6) and chunk 12's `ｍｏｓｔ　ｒｅｇｒｅｔｔａｂｌｅ`. `ａ　ｓｈａｍｅ` free. ⚠️ `Ｔｒｕｌｙ　ａ　ｓｈａｍｅ．` was correctly rejected for 608: §28.3 spends `Ｔｒｕｌｙ，` on `確かに、`, **which this very batch renders at 624** — the collision would have been inside one unit |
| 毎度あり (+ tic) | `Ｍａｎｙ　ｔｈａｎｋｓ` | 11 columns; `毎度ありノロ！！` → `Ｍａｎｙ　ｔｈａｎｋｓ，　ｎｙｏｒｏ！！` (20), twice and byte-identical (642, 646). Free across `tl/`. Held **distinct** from the three ありがとう forms this batch also carries — `Ｔｈａｎｋ　ｙｏｕ　ｆｏｒ　ｙｏｕｒ　ｐｕｒｃｈａｓｅ` (お買い上げ〜, 601/617) and `Ｔｈａｎｋ　ｙｏｕ　ｖｅｒｙ　ｍｕｃｈ` (ありがとうございました, matching `chunk_003` L4). ⚠️ **Binds `毎度あり！！` (unique 592, 596) and `毎度アリ、ゲロゲロ。` (unique 651)** |
| やめておく (menu option) | `　Ｌｅａｖｅ　ｉｔ` | 9 columns with the cursor gutter. Twice, byte-identical (600, 606). **`Ｎｅｖｅｒ　ｍｉｎｄ` correctly not used** — §23.2 spends it on `気にしない、気にしない。` (`chunk_004` L3, shipped, verified at review) |
| 店を出る / はい / いいえ / 買う / 引き取ってもらう | `　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ` / `　Ｙｅｓ` / `　Ｎｏ` / `　Ｂｕｙ` / `　Ｓｅｌｌ　ｉｔ` | All keep the leading `　` cursor gutter (§7, prompt §7). **Verified mechanically at review: 19 source segments begin with a full-width space and 0 lost it.** `　はい` / `　いいえ` recur in four messages and are byte-identical in all four |
| 貼り紙 / 棚卸し / 休業いたします | `ａ　ｎｏｔｉｃｅ` / `ｓｔｏｃｋｔａｋｉｎｇ` / `Ｃｌｏｓｅｄ` | The shop-closed sign (633). `「…」` → `“…”` per §19.2 / §15.1. **The source's two-space indent on the second quoted row is preserved**, and so is its missing `。` before `」` (the tic absorbs the stop). ⚠️ The English inverts the clause order — `本日、棚卸しのため／休業いたします` → `Ｃｌｏｓｅｄ　ｔｏｄａｙ　ｆｏｒ／ｓｔｏｃｋｔａｋｉｎｇ，　ｎｙｏｒｏ．”` — which is the English shop-notice register and loses nothing, but is a reorder the PR did not flag. Recorded, accepted. ⚠️ **Binds unique 647 (the frog shop's copy, `。` present and a four-space indent) and unique 333 (the plain copy)** |
| 下働き | `ｄｏｇｓｂｏｄｙ` | 9 columns. The odd-job lad, twice (632). British and colloquial, which is his register. **`ｔｈｅ　ｈｅｌｐ` correctly rejected**: `ｈｅｌｐ` already renders 助け across nine shipped chunks and the servant sense would sit inside it. Free |
| 親方 | `ｔｈｅ　ｂｏｓｓ` | 7 columns, lowercase, twice (632). **Used exactly as seeded (§9, wave 4) — struck from §9 at this merge.** ⚠️ **§32.1's forward warning is DISCHARGED**: §25.3's test **MET**, counted at review — `おかしら` is **battle chunk 20 only (×5), 0 script**; `親方` is **script bank 12 only (×2), 0 battle**. No shared chunk, no shared bank, no shared message. The two forms coexist without ever meeting, and `Ｂｏｓｓ` (§32.1) stays capitalised for the bandits' chief |
| デビルズラック | `Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ` | 12 columns. **Used exactly as seeded, in the seed's own preferred BARE form — struck from §9 at this merge.** `デビルズラックだ！！` → `Ｉｔ’ｓ　Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ！！` is a predicate nominal, not a title, so §9's quoted `“…”` alternative correctly did not fire. `’` is U+2019, verified |
| ハッピー | `ｈａｐｐｙ` | 5 columns. **Used exactly as seeded — struck from §9** — and **lowercase in both instances so the repetition is byte-identical**: `ハッピーかい？` → `Ａｒｅ　ｙｏｕ　ｈａｐｐｙ？`, `見てのとおりハッピーさ！` → `Ｉ’ｍ　ｈａｐｐｙ！`. The obvious `Ｈａｐｐｙ？` was rejected precisely so the two would not differ by capitalisation, which is what §9's "the joke is that he keeps saying it" required |
| オイラ | carried as register, **not rendered as a word** | **Seed followed exactly — struck from §9.** All four instances carried by dropped subjects and contractions (`Ａｓ　ｙｏｕ　ｃａｎ　ｓｅｅ，　Ｉ’ｍ　ｈａｐｐｙ！`, `Ｉ’ｍ　ｔｈｅ　ｄｏｇｓｂｏｄｙ`, `Ｙｏｕ　ａｎｄ　ｍｅ　ｇｏ　ｂａｃｋ．`). No dialect spelling, no rendered pronoun — §2's ban on inventing, upheld |
| 売約済み | `ｓｐｏｋｅｎ　ｆｏｒ` | `それは　売約済みなんだ。` → `Ｔｈａｔ　ｏｎｅ’ｓ　ｓｐｏｋｅｎ　ｆｏｒ．` (22). Free |
| 買い取り金額 | `ｗｈａｔ　…　ｉｓ　ｗｏｒｔｈ` | The daughter cannot price an item (625). *Buying‐in price* is 20 columns and will not share the row. ⚠️ `ｗｏｒｔｈ` is not free — `chunk_012` L15 ships `必ず役に立ってみせるぜ。` → `Ｉ’ｌｌ　ｐｒｏｖｅ　ｍｙ　ｗｏｒｔｈ．` Different word, different collocation, different chunk and bank; recorded so it cannot drift |
| 荷物 (the player's inventory) | `ｐａｃｋ` | 4 columns. `お荷物がいっぱい` → `Ｙｏｕｒ　ｐａｃｋ　ｓｅｅｍｓ　ｔｏ　ｂｅ　ｆｕｌｌ．` (604), `荷物がいっぱい　みたいノロ。` → `Ｂｕｔ，　ｙｏｕｒ　ｐａｃｋ　ｌｏｏｋｓ　ｆｕｌｌ，　ｎｙｏｒｏ．` (639). ⚠️ **Not free, and the PR said it was**: `chunk_007` L13 ships `ｉｎ　ａ　ｐａｃｋ．` for `もんなんだよ` — the *herd* sense, a different word in a different chunk. No collision; recorded |
| 屋敷 | `ｍａｎｓｉｏｎ` | 7 columns (632). ⚠️ Shares its English with `館` → `ｍａｎｓｉｏｎ` (`chunk_035` L2, shipped) — two source words for one kind of building, the §17.2 shape. **§25.3's test MET, counted at review**: `館` is battle chunk 35 + banks 8, 18, 31, 32, 38, 40; `屋敷` is script bank 12 only. **Disjoint** |
| 兄さん (friendly address to a young man) | carried by the second person | `よう、いつかの兄さん。` → `Ｈｅｙ，　ｉｔ’ｓ　ｙｏｕ　ａｇａｉｎ．`; `オイラと兄さんの仲だ。` → `Ｙｏｕ　ａｎｄ　ｍｅ　ｇｏ　ｂａｃｋ．` §2's rule, as §28.2 handles `お兄ちゃんたち`. **Does not touch** §25.4's 父さん / お父様 → `Ｆａｔｈｅｒ`, which this batch also uses (613, 630) for a **third** source spelling, `お父さん`, on that ruling's own terms |
| なあに、 | `Ｎｏｗ　ｎｏｗ，` | 8 columns. The father brushing off thanks (631). Free. Held **distinct** from §28.8's さあ、 → `Ｎｏｗ，` and §31.3's さて、 → `Ｎｏｗ　ｔｈｅｎ，`, which chunks 3, 7, 11, 18 and 33 already spend on `それじゃ、` / `おっと。` / `さて、` |
| これは、これは！ | `ｗｅｌｌ，　ｗｅｌｌ！` | The doubled greeting, doubling preserved as §23.2 preserves `気にしない、気にしない。`. `おお、これは、これは！` → `Ｏｈ，　ｗｅｌｌ，　ｗｅｌｌ！` (15), taking §24.4's おお → `Ｏｈ，`. Free |
| えーと | `Ｅｒｍ，` | 4 columns. The daughter's filler, twice, byte-identical (616, 622). **`Ｕｍ` correctly unavailable** — §29.3 spends it on `あの・・・` (`chunk_008` L9/L15). Free |
| 悪いな！ | `ｓｏｒｒｙ！` | The rough shopkeeper's apology (629), inside `Ｏｏｐｓ，　ｓｏｒｒｙ！`. Held apart from the four sorry-forms already in `tl/` by punctuation and by never co-occurring: `Ｓｏｒｒｙ，` (あいにく §28.3; ごめんね、 chunk 10), `Ｉ’ｍ　ｓｏｒｒｙ．` (ごめんね。 §30.3), `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` (ごめんなさいね。 chunk 10), `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` (すみません。 §27.1) |
| ごめんなさい。 | `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` | 13 columns (625). **Matches shipped `chunk_010` L11**, which renders `ごめんなさいね。` the same way — same word, §5's punctuation mechanism |
| 感謝のしるし | `ａ　ｔｏｋｅｎ　ｏｆ　ｍｙ　ｔｈａｎｋｓ` | 22 columns (631). ⚠️ **This spends §32.5's named reserve — see §34.7.** The reserve survives; §32.5's freeness sentence does not |

### 34.2 Ruling — `そうだ、` splits, `Ｓａｙ，` stays with `ねえ、`, and the reserve is `Ｙｏｕ　ｋｎｏｗ，`

The PR proposed `そうだ、` → **`Ｓａｙ，`** on a grammatical argument and verified the form free. **The
argument is ratified; the freeness was true when drafted and is not true now** — PR #14 merged
`ねえ、` → `Ｓａｙ，` at **§32.3** on 2026-09-09, shipped in `chunk_020` L48, while this PR sat open.

**The grammatical split is real and is ratified.** Counted across both dumps at review, `そうだ、`
carries two distinct acts:

| Use | Instances | Takes |
|---|---|---|
| confirmation / emphatic assertion | `そうだ、お前だ。` (chunk 0, **shipped `Ｙｅｓ，`**, §29.3), `そうだ、僕は男だ。` (chunk 24), `そうだ、完成させたのだ` (chunk 39) | `Ｙｅｓ，` |
| **recall marker introducing an offer** | `そうだ、オイラあそこの屋敷で…` (unique 632, this unit), `そうだ、{FFEC}{=00}{=00}、王女様を探…` (bank 41), `そうだ、フェイさんも、一緒に…` (chunk 5) | **not `Ｙｅｓ，`** |

Nobody is being answered in the second group, so `Ｙｅｓ，` would not be correct English and
`translation_prompt.md` §2 requires the departure. This is the §32.8 `何だ、` shape one step short:
the *use* is fixed, not a single word for the whole string.

**§25.3's test, counted at review:**

```
ねえ、   battle 4 in chunks [5, 15, 20, 32] | script 16 in banks [0, 18, 20, 28, 40, 41]
そうだ、  battle 4 in chunks [0, 5, 24, 39] | script 2  in banks [12, 41]
SHARED chunks [5]   SHARED banks [41]   messages holding both: 1   → NOT MET
```

> **Ruled, on the §32.5 precedent set one PR earlier in this same wave** (rendering stands, collision
> recorded LIVE, reserve named, nothing re-cut today):
>
> 1. **`Ｓａｙ，` stays with `ねえ、`.** It is shipped; it has **20 occurrences** against the recall
>    `そうだ、`'s three; and *Say,* is the canonical English for a friendly call for attention.
> 2. **The recall `そうだ、` → `Ｓａｙ，` is the default and STANDS in this unit.** Bank 12 contains
>    **no `ねえ、` at all**, so §25.3's test is met for every scene this unit reaches.
> 3. **Where a `ねえ、` shares the bank or the chunk, the recall `そうだ、` takes `Ｙｏｕ　ｋｎｏｗ，`
>    (10 columns), verified free across `tl/` and `pending/`.** That is §29.4's shape — a default plus
>    a conditional reserve — and it fits bank 41's `そうだ、{FC00}，` row at 19 columns, which matters
>    because **bank 41 has 353 bytes free**.

**The live locus is bank 41 and only bank 41** — six `ねえ、` and one `そうだ、`, all untranslated. The
one message holding both is parked `chunk_005` msg 28, and it renders **neither** with `Ｓａｙ，`
(`ねえ、あなたたち、` is re-flowed away; `そうだ、` is dropped and carried by
`Ｆｅｉ，　ｗｏｎ’ｔ　ｙｏｕ　ｃｏｍｅ…`), so nothing is visible today.

Rejected alternatives, each checked at review: **`Ｔｈａｔ　ｒｅｍｉｎｄｓ　ｍｅ，` is spent** —
`pending/chunk_005` **L14 and L17** both ship `Ａｈ，　ｔｈａｔ　ｒｅｍｉｎｄｓ　ｍｅ，` for `あ、それはそうと`
(the PR named L17; it is both). **`Ｈｅｙ，` is spent** on `よう、` and this batch uses it **two rows
earlier in the very same message**. `Ｏｈ　ｒｉｇｈｔ，` compounds two already-spent forms, the §31.4
hazard. `Ｃｏｍｅ　ｔｏ　ｔｈｉｎｋ　ｏｆ　ｉｔ` stands in chunks 2, 8 and `batch_002`.

### 34.3 Ruling — `おっと` is a clause head, not a fixed form, and `Ｏｏｐｓ，` stands

The PR flagged `おっと` rather than silently adding a third form, which was the right instinct. **The
answer is that there was never a first one.** Paired positionally against the dump at review:

| Where | Japanese | Shipped English |
|---|---|---|
| `chunk_007` L11 | `おっと。` | `Ｎｏｗ　ｔｈｅｎ．` |
| **`chunk_007` L13** | **`おっと、`** | **`Ｎｏｔ　ｓｏ　ｆａｓｔ，`** |
| `pending/chunk_043` L6 | `おっと、動くなよ。` | `Ａｈ　ａｈ，　ｄｏｎ’ｔ　ｍｏｖｅ．` |

⚠️ **There are THREE prior renderings, not the PR's two, and two of them are in ONE shipped chunk** —
so the co-occurrence test did not merely fail here, it failed inside `chunk_007` before this PR
existed, and no unit has ever treated `おっと` as fixed.

> **Ruled: `おっと` takes whatever its own clause needs** — the **§32.8 `何だ、` shape**, ruled at chunk
> 20's review on identical evidence. **`Ｏｏｐｓ，` (6 columns, verified free) is right for both of this
> unit's instances**, which are the plain caught-out *whoops*: `おっと、悪いな！` when an item turns out
> reserved (629) and `おっと　親方が来た！` when the boss walks in (632). **Nothing is re-cut** — chunk
> 7's two and chunk 43's one are each correct for their own sentence and none was the same speech act.

`Ｎｏｗ　ｔｈｅｎ` was in any case unavailable in practice: §31.3 records it already serving `さて、`,
`それじゃ、` **and** `おっと。` across chunks 3, 7, 11, 18 and 33. **Reach: `おっと` is 4 battle (chunks
7 ×2, 25, 43) + 6 script (banks 12 ×2, 20, 23 ×3)**, so it will be reached seven more times.

### 34.4 Ruling — `品` → `ａｒｔｉｃｌｅ` is FORCED apart from `アイテム` → `ｉｔｅｍ`

The PR said §25.3's test fails and must not collapse. **Verified, and the specific justification
holds.** The keigo shop's block is unique **597–612**: 597 is its greeting, **598 its own
buy/sell/leave menu (`　アイテムを買う`)**, and **605 its `どの品を売ってもらえますか？`** — one shop, one
scene, both words, four lines apart. Corpus-wide:

```
品      battle 1 (chunk 20) | script 44 across 23 banks
アイテム  battle 12          | script 55 across 14 banks
SHARED banks [0, 8, 12, 13, 14, 15, 16, 18, 20, 25, 40]   messages holding both: 0   → NOT MET
```

**Eleven shared banks, including this unit's own 12–15.** `ａｒｔｉｃｌｅ` (7 columns) verified free
across `tl/` and `pending/`; `ｉｔｅｍ` is §21.3's and `batch_005`'s and is used unchanged here seven
times. The two must never collapse.

### 34.5 Ruling — the `Ｗｅｌｃｏｍｅ` collapse stands, but on different grounds, and bank 26 is LIVE

**The rendering is correct and unchanged. The justification under it is not, and is replaced.** The
PR's row reads *"§25.3's co-occurrence test is met and was counted: `ようこそ` is battle chunk 7 only;
`いらっしゃい〜` is script banks 12–15 and 43; no scene shows both."* Both halves fail on measurement:

```
ようこそ    battle 1 (chunk 7) | script 3 in banks [4, 26]
いらっしゃい  battle 4 (chunks 5, 6, 33) | script 21 in banks [12,13,15,16,17,18,19,22,25,26,43]
SHARED bank [26]   messages holding both: 1   → NOT MET
```

The message is bank 26's casino greeter, with both words on **adjacent rows of one message**:
`いらっしゃいませ！！{FFFE}カジノへ　ようこそ！{FFFE}店の準備があるから、{FFFE}ちょっと待っててね。`

> **The collapse still stands, on the merits rather than the test.** The source itself doubles two
> near-synonyms for one act; English has one word for both; that is §17.2's 鬼 / オーガ shape — a
> deliberate collapse, not the flattening of a distinction the source draws. `chunk_007` L15's
> `ようこそ、プリンセス。` → `Ｗｅｌｃｏｍｅ，　Ｐｒｉｎｃｅｓｓ．` is confirmed shipped and untouched.
>
> ⚠️ **The collision is LIVE in bank 26**, whose translator needs a second form for one of the two
> rows. **The reserve is on the `いらっしゃいませ` side — `Ｃｏｍｅ　ｉｎ` (7 columns), verified free** —
> because `Ｗｅｌｃｏｍｅ　ｔｏ　ｔｈｅ　ｃａｓｉｎｏ` is the one rendering English cannot avoid.

### 34.6 Ruling — bare `ノロ？` → `Ｎｙｏｒｏ？`, and it binds `ゲロゲロ？`

The tic's first non-suffixed rendering in the project (unique 638, 644 — 6 columns, byte-identical in
both). §5 fixes ノロ as a trailing `，　ｎｙｏｒｏ．` **appended to the final clause of each sentence**,
which presupposes a clause; here there is none — the hobbit uses the bare tic as an interjection, in
exactly the slot where the parallel shops put `おや？` (594), `あれ？` (626, this batch) and `ゲロゲロ？`
(652). §5's own sibling entry states the mechanism for that case: for ゲロゲロ **the word is fixed and
the punctuation follows the source**.

> **Ruled: `Ｎｙｏｒｏ？` — the word fixed, the source's own mark, capitalised because it opens a
> sentence.** `Ｎｙｏｒｏ` capitalised is verified free elsewhere in `tl/`.
>
> ⚠️ **This binds unique 652 — `ゲロゲロ？` standing alone takes `Ｒｉｂｂｉｔ？`** (`Ｒｉｂｂｉｔ` is
> §5's fixed word, shipped 7× in `chunk_010`) — and every later bare-tic interjection in either shop.

### 34.7 CORRECTION to §32.5 (§4.3) — `ｔｏｋｅｎ` is no longer free, and the reserve survives anyway

§32.5 names **`ｔｏｋｅｎ` (5 columns)** as the reserve for the racetrack `メダル` if the `勲章` collision
in banks 42–43 ever has to be split, and states it is *"verified free across `tl/` and `pending/`"*.
**That was true on 2026-09-09 and stops being true with this merge**: unique 631 ships
`感謝のしるしだよ！！` → `ａ　ｔｏｋｅｎ　ｏｆ　ｍｙ　ｔｈａｎｋｓ！！`, the form's first use anywhere in `tl/`.

**Nothing changes, and the reserve remains usable.** `感謝のしるし` is an idiom — *a token of my
thanks*, where しるし is literally a sign — not the countable betting token; it sits in **bank 12**
while §32.5's collision is live in **banks 42–43**, so §25.3's test is met between them and no player
can see both. **What is corrected is §32.5's sentence, not its ruling**, exactly as §32.4 struck
§28.3's "the alternative `Ｏｈ　ｍｙ，` is also free" while upholding §28.3 itself.

**Read §32.5's reserve line as:** `ｔｏｋｅｎ` remains the reserve for the racetrack `メダル`; it is
**no longer unspent** — `batch_006.tsv` unique 631 uses it in the fixed idiom *a token of my thanks*
(bank 12), which does not reach banks 42–43. **Lines this affects: none.**

### 34.8 Two more shared-English forms, checked and recorded so they do not drift

Neither was raised by the PR; neither requires a change.

| English | The two source strings | Status |
|---|---|---|
| `Ｗｈａｔ？` | `あれ？` (unique 626, this unit) and `何？` (§30.3, shipped `chunk_008` L10, `pending/chunk_017`) | **This unit conforms rather than introduces** — `chunk_020` L30 already ships `・・・あれ？` → `．．．Ｗｈａｔ？` under §5's punctuation rule (§32.3). Counted at review: `あれ？` chunk 20 + banks [1,12,16,17,19,23,41]; `何？` chunks [7,8,17,28] + bank [19]. **Shared bank 19, 0 shared chunks, 0 messages hold both.** Live for bank 19 only |
| `Ｂｙ　ｔｈｅ　ｗａｙ，` | `ところで、` (unique 631) and `トコロデ、` (`chunk_010` L13) | **Not a collision and not a new form.** Unique 631 **matches shipped `chunk_009` L10 byte-for-byte** (`ところで` → `Ｂｙ　ｔｈｅ　ｗａｙ，`), and chunk 10's is the same word in katakana — the documented one-word/two-spellings collapse (§17.2). Good unflagged consistency |

Also checked clean at review: `ａｌｌ　ｒｉｇｈｔ` — `いいノロか？` → `ａｌｌ　ｒｉｇｈｔ，　ｎｙｏｒｏ？` (636,
641) shares its English with `大丈夫` in **five** shipped/parked files (chunks 3, 7, 8, 43 ×2 — the PR
named two), and **§25.3's test is MET**: `大丈夫` is chunks [3,4,5,7,8,16,22,25,26,27,32,39,43] +
banks [1,4,10,19,23,41]; `いいノロか` is banks [3,13,25] only; **disjoint in both dimensions**.

### 34.9 Three duplicate-check traps this unit leaves behind

1. **Unique 319 and 614 are byte-identical readable text with different `{FFF6}` jump arguments**
   (`{=03}/{=09}/{=10}` against `{=24}/{=2A}/{=31}`). **Their English is byte-identical — verified
   mechanically at review**, readable text equal, full field correctly unequal. ⚠️ **A third copy,
   unique 598, is NOT in this batch** and belongs to whichever batch takes 592–598. It **must reuse
   `　Ｂｕｙ　ａｎ　ｉｔｅｍ` / `　Ｓｅｌｌ　ａｎ　ｉｔｅｍ` / `　Ｌｅａｖｅ　ｔｈｅ　ｓｈｏｐ` byte-for-byte** —
   strictly CLAUDE.md §3 does not force it (three different keys), but the player meets one menu in
   three shops.
2. **Unique 601 and 630 carry the byte-identical ROW `ありがとうございます。` and render it differently**
   — `ｐｕｒｃｈａｓｅ．` in 601, `Ｔｈａｎｋ　ｙｏｕ　ｖｅｒｙ　ｍｕｃｈ．` in 630. **Not a divergence**: §3
   engages on the message (§20.4, §24.5, §27.4, §31.4), and in 601 `お買い上げ` sits on the preceding
   row so the English redistributes across the break. A positional row checker will report it. Same
   class of trap as §24.5's `さあ、` before a `{FC00}` and §27.4's spaced / unspaced village line.
3. **Five EN-only leading full-width spaces (unique 606, 616, 622, 636, 641) are NOT lost or stray
   gutters.** They are the separator after the `{FFEC}{=00}{=01}` price insert — `{FFEC}　Ｊｅｗｅｌｓ．`
   — which Japanese does not need and English does. The real gutter check is clean: **19 source
   segments begin with `　` and 0 lost it.**

### 34.10 Register

| Who | Register |
|---|---|
| **The keigo shop (unique 599–612, portrait unstated)** | Formal and deferential, **no contraction anywhere** — verified line by line across all fourteen: `Ｉ　ｓｈａｌｌ　ｄｕｌｙ　ｒｅｃｅｉｖｅ　ｉｔ　ｆｒｏｍ　ｙｏｕ．`, `Ｉ　ｂｅｌｉｅｖｅ　ｉｔ　ｗｏｕｌｄ　ｂｅ　ｂｅｔｔｅｒ　ｎｏｔ　ｔｏ　ｓｅｌｌ　ｔｈａｔ　ａｒｔｉｃｌｅ．`, `Ｓｅｌｌ　ｏｒ　ｄｉｓｃａｒｄ　ｗｈａｔ　ｙｏｕ　ｄｏ　ｎｏｔ　ｎｅｅｄ`, `Ｉ　ｓｈａｌｌ　ａｗａｉｔ　ｙｏｕｒ　ｎｅｘｔ　ｖｉｓｉｔ．` Its `なさいますか` / `ございます` / `存じますが` are carried in syntax, never in an added word — §2's politeness rule, and the same column §24.6 / §26.7 give the Bernard's-church clergy |
| **The shopkeeper's daughter (613–628, 630; portrait `{FB00}{=01}{=61}`)** | Polite but young, **light contractions** — `Ｉ’ｍ　ｍｉｎｄｉｎｇ　ｔｈｅ　ｓｈｏｐ．`, `ｙｏｕ　ｄｏｎ’ｔ　ｈａｖｅ　ｅｎｏｕｇｈ　ｍｏｎｅｙ．`, `Ｉ’ｌｌ　ｔａｋｅ　ｉｔ　ｆｏｒ`, `Ｅｒｍ，`, `Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` — and **uncontracted where the source is polite**: 630's `Ｗｉｔｈ　ｔｈｉｓ，　Ｆａｔｈｅｒ　ｍａｙ　ｇｅｔ　ｂｅｔｔｅｒ．` for `治るかもしれません`. §15.3's racetrack-guide shape |
| The rough male shopkeeper (629) | Blunt, contractions — `Ｏｏｐｓ，　ｓｏｒｒｙ！`, `Ｔｈａｔ　ｏｎｅ’ｓ　ｓｐｏｋｅｎ　ｆｏｒ．`, `Ｃｏｕｌｄ　ｙｏｕ　ｐｉｃｋ　ａｎｏｔｈｅｒ？` ⚠️ **Unassignable to a shop, correctly**: its register is the rough male of 592–596 but its jump target `{FFF8}{=00}{=04}` matches the hobbit block. Rendered in the plain rough-casual register the line itself carries; **if a later batch places it, re-check** |
| The recovered father (631; portrait `{FB00}{=01}{=53}`) | Hearty and warm, contracts freely — `Ｉｔ’ｓ　ｎｏｔ　ｍｕｃｈ　ｏｆ　ａ　ｔｈａｎｋ‐ｙｏｕ，　ｂｕｔ`, `Ｉｔ’ｓ　Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ！！`, `Ｎｏｗ　ｎｏｗ，`. ⚠️ **The daughter/father link (613 → 630 → 631) is confirmed from the TAG STREAM at review, not the prose**: 613 and 630 carry portrait `{=01}{=61}`, 631 carries `{=01}{=53}`, and 631's `この前もらったかぜ薬のおかげで` answers 630's `これで、お父さん治るかもしれません` directly |
| The odd-job lad (632; portrait `{FB00}{=01}{=54}`) | Breezy, dropped subjects, contractions throughout — `Ｈｅｙ，　ｉｔ’ｓ　ｙｏｕ　ａｇａｉｎ．`, `Ｈｏｗ’ｖｅ　ｙｏｕ　ｂｅｅｎ？`, `Ｉ’ｍ　ｏｎｌｙ　ｔｈｅ　ｄｏｇｓｂｏｄｙ．`, `Ｓｅｅ　ｙｏｕ！` This is where `オイラ` lives and it is never written |
| The hobbit shop (335, 633–646) | The `ノロ` tic on every sentence, **22 instances, all in §18.1's spaced form**, plus the two bare-interjection `Ｎｙｏｒｏ？` of §34.6. Warm and plain otherwise — §19.3 / §21.4's hobbits, unchanged |

⚠️ **Recorded at review, accepted, so they are not rediscovered as defects:** unique 600's
`になりますが？` → `Ｊｅｗｅｌｓ．　Ｗｏｕｌｄ　ｔｈａｔ　ｄｏ？` renders the sentence-final hedging `が` as an
explicit tag question — §2's *"constructions ungrammatical if traced word-for-word"*, not an addition,
and the parallel lines 616 / 636 have their own explicit `いいノロか？` and take it differently. Unique
632's `ｈｏｌｄ　ｏｆ　ａ　ｒａｒｅ` / `ｗｅａｐｏｎ．` breaks between adjective and noun where the source
breaks between object and verb; §3.2 forbids neither, no lone one- or two-letter word is left, and
merging them would change a second line's `{FFFE}` count for a cosmetic gain — **it stands**, on
§33.8's disposition of the same question. Unique 633's notice inverts its clause order for the English
sign register, which the PR did not flag; content is complete and it is recorded above instead.

---

## 35. Added by the wave-5 `あら` corrections unit (PR #17, merged 2026-09-09)

Not a new unit of text and **not a new entry**: PR #17 applies §32.4's ruling (`あら` → `Ｍｙ` plus
the source's own punctuation) to the shipped outliers. **Five rows in four files** —
`tl/battle/chunk_007.txt` L19 and L24, **`chunk_008.txt` L4**, `chunk_011.txt` L3,
`chunk_014.txt` L3 — squash-merged as `f25ff14`. The §27 / PR #9 corrections-unit shape.

**Verified at review, re-derived rather than inherited:** chunk 7 **7,793 / 8,192 (slack 399,
unchanged)** · chunk 8 **7,437 / 8,192 (755, unchanged)** · chunk 11 **1,561 / 8,192 (6,631, was
6,625, −6 bytes)** · chunk 14 **2,203 / 8,192 (5,989, unchanged)**. Net **−6 bytes**, all of it in
chunk 11. **The tag stream is byte-identical to the base on every line of all four files**: zero
`{FFFE}` changes, zero `{FCC0}` changes, no break added, moved or deleted; line counts unchanged at
34 / 21 / 15 / 14. Exactly **five readable runs** differ across the four files and every one is an
`あら` row. Every `rowcheck` warning was re-run against the pre-edit files and is **INHERITED**.
`assemble.py check` passes. **No §9 PROVISIONAL row is promoted and no new term is rendered.**

**After this merge `Ｏｈ　ｍｙ` occurs 0 times in `tl/` and `pending/`**, and every `あら`
interjection in either tree renders `Ｍｙ`: `chunk_007` L19/L24, `chunk_008` L4, `chunk_011` L3,
`chunk_013` L4, `chunk_014` L3, `chunk_020` L47/L48, `batch_006` unique 630. Chunks 16, 27 and 29
are untranslated and inherit the form. `FLAGS.md` §T1 is **DISCHARGED**; see `FLAGS.md` §W.

### 35.1 CORRECTION to §28.3 (§4.3) — the `Ｏｈ　ｍｙ，`-is-free sentence is struck

§28.3's `あら、` row ended *"The alternative `Ｏｈ　ｍｙ，` is also free but is 6 columns to `Ｍｙ，`'s
3"*. **It was false when written**: `chunk_011` L3 had already shipped `Ｏｈ　ｍｙ，` **for `あら、`
itself**. §32.4 struck the sentence in §32.4's own body but left §28.3's row unamended, so a
translator looking up `あら` — which is where they would look — still met the false claim. `FLAGS.md`
§T1 asked for the correction; it is applied here **and** marked in place on the row itself, so the
change is not silent.

**§28.3's ruling survives untouched** — it was ratified on the true observation that `Ｍｙ` was free,
and `Ｍｙ` was and is free. What is struck is one clause of its justification. **Lines this affects:
none beyond the five this unit already applied**; `chunk_011` L3 is the row that made the sentence
false and is now the row that retires it.

### 35.2 CORRECTION to §28.3's and §32.4's reach figures (§4.3) — substring counts, not censuses

Both entries counted the **substring** `あら` and reported it as the interjection. Measured at this
review across both dumps, separating the two:

| | substring rows | **interjection rows** | false positives excluded |
|---|---|---|---|
| `dumps/battle_dump.txt` | 12 | **11** | `あらかた片付いたな。` (chunk 8 msg-line 15 — 粗方) |
| `dumps/script_unique.txt` | 31 | **28** | `あらんことを。` ×2 (有らん), `日を　あらためて、` (改めて) |

- **§28.3 said "16 further occurrences (5 battle + 11 script-unique — both figures confirmed)".**
  The true reach is **11 battle + 28 script-unique = 39**, i.e. **38 further** than §28.3's own
  chunk-13 instance. Out by more than a factor of two, and "both figures confirmed" was not true.
- **§32.4 said "12 `あら` rows in the battle dump".** The interjection census is **11**. Its chunk
  list — 7, 8, 11, 13, 14, 16, 20 ×2, 27, 29 — is **right and unchanged**, and matches the census
  run for run.
- The 28 script-unique interjection lines are data indices 478, 479, 482, 489, 490, 499, 500, **630**,
  665, 682, 685, 701, 707, 708, 719, 723, 784, 923, 951, 953, 954, 1141, 1144, 1327, 1355, 1391,
  1406, 1427. **Only 630 is translated** (`batch_006`, conforming); the other 27 inherit `Ｍｙ`.

**Lines this affects: none.** Neither ruling rested on the count — §32.4's decisive ground is that
§24.4 spent `Ｏｈ？` on おや outright — so both stand exactly as written.

### 35.3 CORRECTION to §24.4's `おや` battle figure (§4.3) — 4 interjection, not 6

§24.4's corpus table gives `おや` **6 battle**. That is the substring count; **the interjection is 4**,
in chunks **1, 2, 31 and 35** — precisely the three shipped renderings §32.4 cites (`chunk_001` L1,
`chunk_002` L14, `chunk_035` L2) plus chunk 31's untranslated `おや。`. The two false positives are
`おやさしい方です。` (chunk 7 message line 19) and `おやすいご用です。` (chunk 23).

⚠️ **`おやさしい方です。` sits on the very message line that carries `あら・・・・？`** — chunk 7's line
19 — so the one line in the project where both of §24.4's miscounts could be seen at once is a line
this unit edits. Coincidence, recorded so it is not mistaken for a cause.

**Nothing turns on it.** `Ｏｈ？` is spent for おや at 4 occurrences as surely as at 6, which is the
only load that figure bears in §24.4's argument and in §32.4's. The script figure (23) is unchecked
and is left as it stands. **Lines this affects: none.**

### 35.4 The `chunk_008` row — how a counted row fell out of its own ruling's table

Worth writing down because the mechanism is reusable, not because the row is interesting. §32.4
gathered the corpus correctly, wrote the chunk list correctly (chunk 8 named), and then built its
*Lines this affects* table from the **five data points the dispatch had supplied** rather than from
its own census. The two disagreed by one row and nothing reconciled them. `FLAGS.md` §T1 copied the
table, the wave-5 dispatch copied §T1, and the omission travelled three documents intact until PR
#17's translator scanned the dump itself rather than trusting any of them.

**The lesson is the same one §32.5 and `HANDOFF.md`'s 2026-09-09 entry already record in the other
direction**: a census and the table built from it must be reconciled against each other before the
section is committed, because after that they are copied, not re-derived.

### 35.5 Speaker attributions — one PR flag corrected, and a caveat on §32.4's own aside

⚠️ **PR #17's Flag 7 identifies `chunk_007` L19's speaker as "portrait 02 (§21.4/§25.5/§28.6/§32.9's
unnamed female companion, 'the one who notices')". In chunk 7 portrait 02 is Timmy** — verified from
the tag stream at review, not from prose: the segment immediately after is
`{FCB0}{=00010001}{FC51}{FFFD}どうした、ティミー？` → `Ｗｈａｔ　ｉｓ　ｉｔ，　Ｔｉｍｍｙ？`, and the next
speaker names her again. §11.1 fixes ティミー → `Ｔｉｍｍｙ`; §23.5 gives her register.

**Portrait ids are per-chunk and do not carry identity across chunks** — §23.5 has Timmy at portrait
**0007** in chunk 4, and §29.6 has the 9th Army squad at ids that differ again in chunk 8. So
§32.4's own aside, *"The same-speaker argument (portrait 02 in chunks 7, 14 and 20) is real"*, does
not hold either: chunk 20's portrait 02 is fixed as the unnamed female companion **from inside chunk
20** (§32.9), chunk 7's portrait 02 is Timmy, and chunk 14's is unnamed.

**Nothing changes.** §32.4 already says the same-speaker argument "argues for making *one* form
consistent, not for which form, and §24.4 settles which" — so the ruling never rested on it, and
`Ｍｙ` is the fixed form for `あら` whatever the speaker. Recorded so the inference is not reused as
though it were established. The register of all five rows was checked independently and `Ｍｙ` suits
every one: chunk 7 L19 Timmy (young, female); chunk 7 L24 the old woman granting an item (`のよ`,
`ね`, `もっておいきなさい`); chunk 8 L4 a woman of the 9th Army squad (`来たわ！`, §29.6); chunk 11 L3
**Maya**, whose §7 register is arch and coquettish and for whom `Ｍｙ，　ｖｉｓｉｔｏｒｓ？` is a
straight improvement on `Ｏｈ　ｍｙ，`; chunk 14 L3 portrait 02, unnamed.

⚠️ **`ｖｉｓｉｔｏｒｓ` is deliberately kept in `chunk_011` L3**, as §34.1's `お客様` row requires in
terms ("§32.4's owed re-cut of `chunk_011` L3 keeps `ｖｉｓｉｔｏｒｓ`"): only `Ｏｈ　` is removed, so
the form stays spent and §34.1 needs no amendment.

### 35.6 No register or geometry consequence

No page grew, no row grew, no break moved, no orphan was created, and `{FC50}`/`{FC51}` alternation
is untouched in all four files — proven by the zero tag-stream diff rather than argued. The two rows
that change width both **shrink** (`Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` 16 → 13) or stay equal. Chunk 7's two
`> 4 rows` warnings on lines 23 and 24 are the `FLAGS.md` §D3 / §L2 pages that carry no
`{FC50}`/`{FC51}` at all, are already queued for the in-game check, and are byte-identical to base.

---

## 36. Added by chunk 021 (PR #18, merged 2026-09-09)

Rendered in `tl/battle/chunk_021.txt`, squash-merged as **`6276b4b`**. Chapter 21 — the 9th Army
flees the Farina incident with the Royal Army behind it, an old villager tells what happened to
Farina ten years ago, Second Lieutenant Ryan accuses the 9th of colluding with the Empire, and
Father Batou agrees to travel to Farina and is arrested.

**Figures, all re-derived at review rather than taken from the PR.** **4,431 / 8,192, slack
3,761.** 863 JP → 1,809 EN readable characters = **2.096×** against the **4.280** tier-D ceiling
(`tag_bytes` 803, `english_budget` 3,694 characters), **49.0 %** of the English budget spent —
every one of those matches the PR exactly, and 863 / 5,663 / 4.28 match `translation_prompt.md`
§0.3's own table. **105 text rows** (source 100), widest **23**, none at 24, **no page over 4 text
rows** and none the source did not already have at 4. `{FFFE}` **81 → 86 (+5)** on four lines;
`{FCC0}` **7 → 7**, unchanged on every line and none added. `bankmeasure` not required (nothing
under `tl/script/` changed) but run: no bank negative, banks 41 (353) and 40 (471) byte-for-byte
untouched. ⚠️ **Three PR figures were wrong and are corrected in §36.7; not one of them touches the
file, and the per-line `{FFFE}` table — which is what CLAUDE.md §6 gate 4 actually requires — is
complete and correct.**

### 36.1 People, places and words first rendered here — one promotion out of §9, one left live

| Japanese | English | Note |
|---|---|---|
| ライアン | `Ｒｙａｎ` | 4 columns. `ライアン少尉` → **`Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ`**, 22 bare and **23 with the vocative comma — one row**, measured on the shipped row. **Used exactly as seeded.** ⚠️ **CROSS-UNIT with chunk 22 (PR #19), which is still open — so §9's row is DELIBERATELY LEFT LIVE** for that reviewer to strike, per the `ルート` precedent (§29.1 / §30.1). **2 battle (21, 22) / 0 script**, counted at review. ✅ **DISCHARGED 2026-09-09: PR #19 merged (`6423083`) with `ライアン隊長` → `Ｃａｐｔａｉｎ　Ｒｙａｎ`, and §9's row is struck there.** ⚠️ **The promotion reading behind "21 → 22" is NOT ratified — see §37.4**; both renderings are correct either way |
| バトウ神父 | `Ｆａｔｈｅｒ　Ｂａｔｏｕ` | 12 columns. **Promoted from §9; not a new reading** — §26.1 already fixes `バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ`, and this is the 〜神父 appellation taking the same English on §24.1's `ナコール様` pattern. Rendered ×3. **Not cross-unit**: `バトウ` is battle chunk **21 only** (+8 script), so §9's row is struck. The bare vocative `神父、` → **`Ｆａｔｈｅｒ，`** and the attributive `ファリーナ出身の神父` keeps §1's common noun `ｐｒｉｅｓｔ` — all three forms occur in this one chunk and are held apart correctly |
| 追っ手 | `ｐｕｒｓｕｅｒｓ` | 9 columns. `追っ手は？` → `Ｐｕｒｓｕｅｒｓ？`, keeping the source's 5-character clip. Hapax — 1 battle / 0 script |
| うろつく | `ｐｒｏｗｌ` | `オークがうろついてやがる` → `ｔｈｅ　ｏｒｃｓ　ａｒｅ　ｏｕｔ　ｐｒｏｗｌｉｎｇ`; the やがる contempt is carried by `ｏｕｔ`, not by an added word (§2). Free |
| 相変わらず | `Ｓａｍｅ　ａｓ　ｅｖｅｒ，` | 17 columns. ⚠️ **NOT a new form, and the PR's row understated itself — see §36.7.3.** `pending/chunk_005.txt` L29 already renders `相変わらずだな、` as `Ｓａｍｅ　ａｓ　ｅｖｅｒ，` / `ｔｈａｔ　ｓｅｌｆｉｓｈ　ｓｔｒｅａｋ．`, and **this unit agrees with it byte-for-byte on the phrase.** A parked form matched, not a form coined. **3 battle (5, 21, 41) + 1 script (bank 41)**; two are now rendered, so it will be reached **two** more times |
| 交戦中 | `ｅｎｇａｇｅｄ` | 8 columns. `すでに交戦中だ` → `ａｌｒｅａｄｙ　ｅｎｇａｇｅｄ．` Held **distinct** from §30.2's 迎え撃つ → `ｉｎｔｅｒｃｅｐｔ` and 迎撃態勢 → `Ｉｎｔｅｒｃｅｐｔ　ｓｔａｔｉｏｎｓ`. Free |
| 先回りする | `ｈｅａｄ　…　ｏｆｆ` | `先回りされたのか？` → `Ｄｉｄ　ｔｈｅｙ　ｈｅａｄ　ｕｓ　ｏｆｆ？` Hapax — 1 battle / 0 script |
| キナ臭い | `ｓｍｅｌｌ　ｆｉｓｈｙ` | `何やらキナ臭くなってきたぜ` → `Ｓｏｍｅｔｈｉｎｇ’ｓ　ｓｔａｒｔｉｎｇ` / `ｔｏ　ｓｍｅｌｌ　ｆｉｓｈｙ．` The katakana `キナ` is emphasis, not a name — carried as register, not transliterated (§2, and the §32.9 `ほーせき` / §29.6 `てーこく` treatment). Hapax |
| 街道 | `ｒｏａｄ` | 4 columns. ⚠️ **Not a new form — matching shipped `chunk_002.txt`**, which renders `南側の街道` / `この街道` / `南の街道` as `ｔｈｅ　ｓｏｕｔｈ　ｒｏａｄ` / `ｔｈｉｓ　ｒｏａｄ` / `Ｔｈｅ　ｓｏｕｔｈ　ｒｏａｄ`. Recorded because `ｈｉｇｈｗａｙ` is the obvious first choice and would have forked the word. **4 battle (2 ×3, 21 ×1) + 1 script** |
| 連行する | `ｔａｋｅ　…　ｔｏ` | `城へ連行するぞ！` → `ｔａｋｅ　Ｆａｔｈｅｒ` / `Ｂａｔｏｕ　ｔｏ　ｔｈｅ　ｃａｓｔｌｅ！` Held **distinct** from this chunk's own 捕まえろ → `ｓｅｉｚｅ　ｔｈｅｍ！`, four segments earlier. Hapax |
| 裏切り者 | `ｔｒａｉｔｏｒ` | 8 columns. `この裏切り者め。` → `Ｙｏｕ　ｔｒａｉｔｏｒｓ．` — see §36.3 for the `〜め` ruling and the number. Hapax — 1 battle / 0 script. Free |
| 思し召し | `ｔｈｅ　ｗｉｌｌ　ｏｆ　Ｇｏｄ` | `これも、神の思し召しなのですか。` → `Ｉｓ　ｔｈｉｓ，　ｔｏｏ，　ｔｈｅ` / `ｗｉｌｌ　ｏｆ　Ｇｏｄ．` `神` → `Ｇｏｄ` is already house practice — `batch_005` ships `Ｍａｙ　ｔｈｅ　ｂｌｅｓｓｉｎｇ　ｏｆ　Ｇｏｄ　ｂｅ　ｕｐｏｎ　ｙｏｕ．` for the same clergy. Hapax |
| 司教一族 | `ｔｈｅ　Ｂｉｓｈｏｐ’ｓ　ｋｉｎ` | `ｋｉｎ` is 3 columns and, checked as a **whole word** rather than as a substring, occurs nowhere else in `tl/` or `pending/`. Capitalised `Ｂｉｓｈｏｐ` on §26.1, which fixes 司教 → Bishop and identifies the man (Creus of Farina, named two lines later). ⚠️ **A §2.1 step-4 width choice, flagged in the PR and confirmed at review**: `ｔｈｅ　Ｂｉｓｈｏｐ’ｓ　ｆａｍｉｌｙ　ｗｅｒｅ` measures **25** on a page already at the 4-row wall |
| ぐおっ | `Ｇｗｏｈ` + the source's own punctuation | 4 columns. A struck-down grunt. Derived on the **exact** §32.3 template `ぬおっ` → `Ｎｗｏｈ`, and held distinct from グッ → `Ｇｕｈ`, ぐわっ → `Ｇｗａｈ` (§11.5), ぐふっ → `Ｇｕｆｆ` (§14.5) and `Ｎｗｏｈ` itself. Verified free across `tl/` and `pending/`. Hapax |
| ええっ | `Ｅｈｈ` + the source's own punctuation | 3 columns. ⚠️ **Not a new rendering** — `pending/chunk_043.txt` L43 already renders `ええっ・・・` as `Ｅｈｈ．．．`; this unit renders `ええっ！？` as `Ｅｈｈ！？`, which is §5's mechanism. Shares its English with §20.3's `えーっ` → `Ｅｈｈ，` — the documented one-word/two-spellings collapse (§17.2 鬼 / オーガ) — and **§25.3's test is MET on both axes, re-counted at review**: `ええっ` is battle 21, 43 + banks 1, 28, 32; `えーっ` is battle chunk 2 only, 0 script. No shared chunk, no shared bank, no line holds both. **Every figure in the PR's row is correct as stated** |
| ちっ / チッ | `Ｔｓｋ` + the source's own punctuation | 3 columns. **Not a new form** — §30.3 fixes `ちッ` → `Ｔｓｋ`. Two further kana spellings collapse onto it, per §11.5's くっ / クッ and §17.2's 鬼 / オーガ. ⚠️ **This chunk carries `ちっ、`, `チッ・・・・` AND `くっ・・・`, so §30.3's `Ｔｓｋ` / `Ｔｃｈ` distinction is load-bearing inside a single unit for the first time** — and it holds: `Ｔｓｋ，` (L6), `Ｔｓｋ．．．．` (L22), `Ｔｃｈ．．．` (L14) |
| フン、 | `Ｈｍｐｈ，` | ⚠️ **Recorded at review; the PR rendered it and proposed no row.** §6 fixes `ふっ / フンッ` → `Ｈｍｐｈ`; this is a **third kana spelling** of the same scoff, collapsing onto it per §17.2's 鬼 / オーガ and §11.5's くっ / クッ. Written down so a later unit cannot "correct" it into a fourth grunt |
| いいでしょう | `Ｖｅｒｙ　ｗｅｌｌ．` | 10 columns. Batou's formal assent. **A third source string on this form** — see §36.5 |
| とにかく | `Ｉｎ　ａｎｙ　ｃａｓｅ，` / `Ａｎｙｗａｙ，` | **Register-selected, not spelling-selected** — see §36.2, which is the row's real content |

### 36.2 Ruling — `とにかく` splits on REGISTER, and the comma has nothing to do with it

`とにかく` carries two English forms across five shipped and parked rows and had **no glossary row at
all**. The PR flagged it and proposed that the split is register-selected; the reviewer traced all
five instances positionally with the speaker of each, and the proposal is not merely defensible —
**it is the only reading that fits every instance.**

| Where | Source | English | Speaker, and the evidence |
|---|---|---|---|
| `chunk_002` L14 | `とにかく、` **comma** | **`Ａｎｙｗａｙ，`** | portrait 0000, a 9th Army soldier — `Ｗｅ　ｃａｎ’ｔ　ａｂａｎｄｏｎ　ｔｈｅｍ．`, contracts |
| `chunk_012` L17 | `とにかく` break | **`Ｉｎ　ａｎｙ　ｃａｓｅ，`** | the Caucasus mayor — §7's "polite, slightly fussy; `Ｉ　ａｍ`, not `Ｉ’ｍ`" |
| `chunk_013` L05 | `とにかく` break | **`Ｉｎ　ａｎｙ　ｃａｓｅ，`** | `Ｉ　ｓｈａｌｌ　ｒｅｔｕｒｎ　ｔｏ　Ｌｅｖｅｒｋ　ｆｏｒ　ｎｏｗ．`, no contractions |
| **`chunk_021` L19** | `とにかく、` **comma** | **`Ｉｎ　ａｎｙ　ｃａｓｅ，`** | Batou, §26.7 clergy — `Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ　ｍｙｓｅｌｆ．`, `ｉｔ　ｉｓ` |
| `pending/chunk_043` L26 | `とにかく、` **comma** | **`Ａｎｙｗａｙ，`** | `Ｒｅａｓｏｎｓ　ｌａｔｅｒ．` … `Ｆｏｌｌｏｗ　ｍｅ！！`, casual and urgent |

> **Ruled: contraction-taking, casual speakers take `Ａｎｙｗａｙ，` (8 columns); contraction-free,
> formal speakers take `Ｉｎ　ａｎｙ　ｃａｓｅ，` (14).** The orthographic reading is **refuted**:
> register predicts 5 of 5, the comma predicts 2 of 5. And the comma "split" is illusory in the
> first place — a `とにかく` followed by `{FFFE}` is the same word with the hard break standing
> where the comma would; §27.4 records the identical trap for the spaced village line.

This is the §32.2 `〜の奴` shape: one source word, two English forms, held apart by something the
glossary can state. **Lines this affects: none** — all five instances are already on the right side.
**10 battle occurrences across chunks 2, 5, 12, 13, 16, 21, 24, 26, 29, 43 + 12 script** (banks 1,
23, 32, 41), so five more battle chunks inherit this row.

### 36.3 Ruling — §31.2's `〜め` is scoped to THIRD-PERSON reference, and `Ｙｏｕ　ｔｒａｉｔｏｒｓ．` stands

§31.2 fixes `〜め (contempt, **on a personal name**)` → `Ｔｈａｔ　〜` and names `この裏切り者め。` as a
plain recurrence. **It does not govern that line, on the glossary's own axis**, and the PR's argument
for this is right in every particular:

- **§31.2's model is third-person.** It builds `Ｔｈａｔ　〜` explicitly on §20.3's `バカ者` →
  `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ`, and both are contempt aimed at a man who is not present.
- **§28.3 already draws the line, in its own words.** It fixes `馬鹿者！ (direct address)` →
  `Ｙｏｕ　ｆｏｏｌ！` and holds it apart from §20.3's form "(katakana, and *of* a third party) …
  **this one is the vocative**". Same 者-suffixed contempt noun, same axis.
- `裏切り者` is a **common noun**, so §31.2's stated scope ("on a personal name") excludes it anyway.
- `Ｔｈａｔ　ｔｒａｉｔｏｒ．` would also **invert the deixis**: `この` in this abuse frame is
  addressee-proximal and English `Ｔｈａｔ` is distal.

> **Ruled: contempt marker + direct address → `Ｙｏｕ　〜`; contempt marker + third-person reference
> → `Ｔｈａｔ　〜`.** §31.2's row is re-scoped in place and its "Recurs as `この裏切り者め。`" clause
> struck. **Lines this affects: none** — nothing shipped renders a vocative `〜め` except this one.

**On the number, which the PR correctly called its own judgement, the reviewer adds evidence the PR
did not have.** The tag stream of line 14 carries **two distinct 9th Army portraits on `{FC51}`
inside that single message**: 0000 speaks `俺たちは、戦うつもりなんてありません！` before Ryan, and
**0009** answers `くっ・・・話しても無駄か。` after him. Ryan is not facing one man. With `９軍が…落とした`
and `最初から帝国とつるんでいた` both aimed at the unit, and the soldier's own `俺たち`, the plural is
the better reading and not merely a defensible one. **`Ｙｏｕ　ｔｒａｉｔｏｒｓ．` (13 columns) stands;
`Ｙｏｕ　ｔｒａｉｔｏｒ．` (12) is the reserve** if a later reading makes the single addressee decisive —
a 2-byte, no-re-flow change on a row that measures 23 either way.

### 36.4 CORRECTION to §1 and §2 (§4.3) — the rank widths are patched IN PLACE, and here is why

§29.5 measured this in wave 3, recorded it and deliberately did not patch, telling "whoever first
renders 中尉" to fix §2 in place. The consequence: **the wrong figure travelled two waves and was
restated in the wave-5 §9 seed as if it were a new discovery**, which chunk 21's translator then had
to correct. Three independent measurements now agree — §29.5's, the PR's (with `rowcheck`'s own
algorithm, as its dispatch asked), and the reviewer's. Deferring it a third time is what this
correction is for, so **§1's クレス row, §1's アンゼルモ row and both §2 rank rows are corrected in
place**, each marked, with this record beside them.

| Where | Was | Is |
|---|---|---|
| §2 少尉 | `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` **18** columns | **17** (`Ｓｅｃｏｎｄ` 6 + space + `Ｌｉｅｕｔｅｎａｎｔ` 10) |
| §2 中尉 | `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ` **17** | **16** (`Ｆｉｒｓｔ` 5 + space + 10) |
| §1 アンゼルモ | `Ａｎｓｅｌｍｏ` **8** | **7**, so `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` is **24**, not §29.5's 25 |
| §1 クレス, §2 少尉 | "will not share a line with a name" / "never on one row" | **False as a blanket claim.** `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ，` is **23 and ships as one row here** |

**§29.5's conclusion was reasoned on Cress and holds for Cress only.** `Ｃｒｅｓｓ` is 5 columns, so
the vocative reaches 24; **`Ｒｙａｎ` is 4**, so it reaches 23 — one column is the whole difference.
The rule to apply is arithmetic, not a blanket prohibition: **rank + 1 + name, checked against 23.**
**Lines this affects: none.** No rendering anywhere changes; chunk 8's Cress split still stands.
⚠️ **PR #20 (script batch 007) is the project's first 中尉 rendering** and now inherits a correct §2
instead of the trap; nothing is left for its reviewer to patch.

### 36.5 Ruling — `Ｖｅｒｙ　ｗｅｌｌ．` renders a THIRD source string, and §25.3's test is met on both axes

§29.4 lists `Ｖｅｒｙ　ｗｅｌｌ` as "not free (chunks 33 and 35)". Traced positionally: `chunk_033`
renders `いいわ。` and `chunk_035` renders `よし、ひとつ`. This unit adds **`いいでしょう。`** — Batou's
formal assent, line 19. **Counted at review across both dumps rather than taken from the PR**,
because a co-occurrence discharge is only as good as its counts:

```
いいでしょう   battle [21]                script bank 41  (1 hit)
いいわ        battle [3, 4, 5, 28, 33]   script bank 19  (1 hit)
よし、ひとつ    battle [35]                script  none
→ chunk sets disjoint, bank sets disjoint, and no single dump line holds two of them.
```

**Every figure in the PR's Flag 5 is correct as stated, including the two bank numbers.** The
collapse is also the mild kind — `いいわ` and `いいでしょう` are one word in two politeness registers,
the §17.2 鬼 / オーガ shape rather than the flattening of a distinction. **Reserve, if a later unit
ever needs the split: `Ｉ　ｃｏｎｓｅｎｔ．` (11), re-verified free across `tl/` and `pending/` at this
review.** The obvious candidates are all spent and were checked: `Ａｓ　ｙｏｕ　ｗｉｓｈ` and
`ｓｏ　ｂｅ　ｉｔ` (`chunk_000` L14, `chunk_004` L4), `ｇｌａｄｌｙ` (`chunk_019` L24), `Ａｇｒｅｅｄ．`
(§29.4). **Lines this affects: none.**

### 36.6 `１０年前` → `ｔｅｎ　ｙｅａｒｓ　ａｇｏ`, and §10.8 is CLOSED

The second prose instance in the project, agreeing with `chunk_012`'s `あと３時間だ。` →
`Ｔｈｒｅｅ　ｈｏｕｒｓ　ｒｅｍａｉｎ．`, and §15.1 had already narrowed the digits-stay-full-width note to the
horse-race table of numbers. Ruled at §10 question 8: **cardinals in running prose are spelled out;
full-width digits stay in fixed names and in tables of numbers.** The rule had to be stated in that
shape because **this very chunk carries both sides on adjacent rows** — `ｔｅｎ　ｙｅａｒｓ　ａｇｏ` in
line 10 against §2's `９ｔｈ　Ａｒｍｙ` (L19) and `２ｎｄ　Ａｒｍｙ` (L5). Spelling out cost 1 column here
(`ｔｅｎ` 3 against `１０` 2) and nothing rode on it.

### 36.7 Three PR figures corrected, and what each is worth

**None of them touches the file, and the per-line `{FFFE}` table — which is what CLAUDE.md §6 gate 4
actually requires — is complete and correct.** Recorded because §6.7 and §4.3 do not distinguish
between a wrong rendering and a wrong record, and because two of the three would have been copied
forward into the wave-5 summary.

1. **`{FFFE}` "55 → 59 (+4)" is wrong; the totals are 81 → 86, delta +5.** The PR's own per-line
   table sums to +5 (7→8, 17→19, 0→1, 2→3), so the summary contradicts its own evidence. Five
   counting definitions were probed at review — raw tags, non-trailing, followed-by-text,
   row-separating, text-on-both-sides — and **all five give 81 → 86 (+5)**; no chunk in the dump has
   a source total of 55, so it is not a scratch-file mix-up either (§W's trap family). Unexplained,
   and corrected rather than rationalised.
2. **"57 text rows" and "nine rows at 23".** Under `rowcheck`'s own definition — pages bounded by
   `{FCC0}`/`{FC30}`/`{FC51}`/`{FC50}`/`{FFFF}`, non-empty segments between `{FFFE}` — the unit has
   **105** text rows against the source's 100, and **10** rows at 23. "Widest 23, none at 24" is
   correct and is the figure the gate turns on.
3. **The `相変わらず` row's "free across `tl/`" is true but hides the better fact.** The form is
   already rendered in `pending/chunk_005.txt` L29 and **this unit matches it byte-for-byte**; and
   the reach over-counts, since two of the three battle occurrences are now rendered, leaving chunk
   41 + one script line. Corrected in §36.1. ⚠️ This is the §W3 / §W4 blind spot again from the
   other side: `pending/` is outside `tl/`, so a `tl/`-scoped freshness check reports a form as new
   when it has in fact already been drafted. **Here the outcome is agreement, not divergence** —
   worth recording as the counter-example to the village line in `FLAGS.md` §X2.

### 36.8 Recorded, not re-cut — four things checked that are not defects

- **`これも、神の思し召しなのですか。` → `Ｉｓ　ｔｈｉｓ，　ｔｏｏ，　ｔｈｅ　ｗｉｌｌ　ｏｆ　Ｇｏｄ．`** keeps
  interrogative syntax under the source's `。`. Swept at review across every `か。` in `tl/battle/`:
  **interrogative syntax plus `．` is established shipped practice** — `chunk_002` L15 and L21
  (`ａｒｅ　ｔｈｅｙ　ｎｏｔ　ｃｈａｔｔｉｎｇ　ａｍｉａｂｌｙ　ｗｉｔｈ　ａ　ｗｏｍａｎ．`) and `chunk_006` L3 and L4
  (`Ｓｈａｌｌ　ｗｅ　ｔｅａｃｈ　ｔｈｅｍ　ｔｈｅｉｒ　ｐｌａｃｅ，　ｔｈｅｎ．`). This is the fifth instance.
  The chunk's other two `か。` — `あれは・・・２軍か。` and `取り逃がしたか。` — are realisations and go
  declarative, which is a principled split; **the punctuation follows the source in all three.**
  Recorded so a later reader does not "fix" the full stop into a `？` and break §5.
- **`ｕｎｄｅｒ　ａｔｔａｃｋ` occurs twice in this chunk.** Once as §27.2's binding village line (L11,
  byte-identical) and once for `攻撃を受けてる` in L5 (`ｔｈｅ　ｏｎｅ　ｕｎｄｅｒ　ａｔｔａｃｋ`). Different
  source strings, different messages, §3 not engaged, and no distinction is flattened. Recorded so a
  future positional sweep does not read L5 as a fourteenth §27.2 instance.
- **The intra-chunk duplicate is byte-identical in both directions.** JP
  `フェルナンド将軍に{FFFE}報告せねば・・・` and EN
  `Ｉ　ｍｕｓｔ　ｒｅｐｏｒｔ　ｔｏ{FFFE}Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ．．．` both appear in lines 13 and 22 —
  the same portrait 08 carrying the defeat line and the escape line.
- **`{FC70}{=00D1}` (L10), `{FCA8}{=01D3}` (L22) and `{FCB7}{=001E}` (L21)** sit outside readable text
  and constrained nothing. ⚠️ **`{FCA8}` is the §D1 artifact tag**, but chunk 21 is not one of the
  ten affected chunks and `check` passes — recorded so the coincidence is not mistaken for §D1.

### 36.9 Register

| Who | Register |
|---|---|
| Ryan (portrait 08, `{FC50}`) | The §14.6 / §20.5 / §25.5 / §28.6 / §31.7 officer column — **zero contractions** in any of his four messages (`Ｉ　ｈａｄ　ｔｈｏｕｇｈｔ　ｉｔ　ｓｔｒａｎｇｅ`, `Ｈｏｗｅｖｅｒ，`, `Ｉ　ｍｕｓｔ　ｒｅｐｏｒｔ`), and the contempt sits in `Ｈｍｐｈ，` and `Ｙｏｕ　ｔｒａｉｔｏｒｓ．` rather than in added words. ⚠️ **Nothing in the chunk states which army he serves** — he is `宮廷軍` by the surrounding dialogue and reports to General Fernando of the 2nd, and the English commits to nothing beyond what each line says, on the §28.7 / `FLAGS.md` §P practice for chunk 13's King |
| Father Batou (portrait 03) | §26.7's Bernard's-church clergy, confirmed here in his first battle-script scene: **no contractions** (`Ｉ　ｄｏ　ｎｏｔ　ｋｎｏｗ　ｍｙｓｅｌｆ．`, `Ｉ　ｓｈａｌｌ　ａｃｃｏｍｐａｎｙ　ｙｏｕ．`, `ｉｔ　ｉｓ　ｗｈｙ`), and the formal `Ｉｎ　ａｎｙ　ｃａｓｅ，` of §36.2 |
| The old villager (portrait 05) | §7's "Village elders (じゃ / のう)" column — old-fashioned diction, **no contractions, no archaic spelling**: `Ｆａｒｉｎａ，　ｔｏｏ，　ｗａｓ　ｏｎｃｅ　ａ　ｐｒｏｓｐｅｒｏｕｓ　ｌａｎｄ．．．．`, and `死んだように静かに` carried as `ａｌｌ　ｉｓ　ｄｅａｄ　ｑｕｉｅｔ．` rather than glossed |
| The 9th Army squad (portraits 00, 01, 02, 09, 0A) | §7 and §21.4 unchanged — contractions throughout (`Ｔｈｅｙ’ｒｅ`, `ｗｅ’ｖｅ`, `Ｉ’ｄ`, `ｉｔ’ｓ`, `ｌｅｔ’ｓ`). Portrait **02** is §21.4 / §25.5 / §28.6 / §32.9's unnamed female companion and again "the one who notices" — `{FC00}，　ｌｏｏｋ！` is hers. ⚠️ Per §W5, **portrait ids are per-chunk**; this attribution is made from within chunk 21 and is not carried from another chunk |
| The soldier pleading with Ryan (portrait 00, `{FC51}`) | Polite ます/ません to a superior, carried by **no contractions** (`Ｗｅ　ｈａｖｅ　ｎｏ　ｉｎｔｅｎｔｉｏｎ　ｗｈａｔｅｖｅｒ　ｏｆ　ｆｉｇｈｔｉｎｇ！`) — the same soldier contracts freely elsewhere in the chunk, so the shift is the source's, not a slip |

---

## 37. Added by chunk 022 (PR #19, merged 2026-09-09)

Rendered in `tl/battle/chunk_022.txt`, squash-merged as **`6423083`**. Chapter 22 — the fort parley.
Jake reports the 9th Army's arrival to Captain Cress; Captain Ryan, told the 5th Army is holding
back, decides Cress is friendly with the 9th and orders the assault so the credit is his alone
(L01). **L05 and L06 are the two mutually exclusive outcomes of the same parley** and L07 is the
battle-open line after the hostile one: in L05 the player explains Fernando's forged medal, the real
one falling into the squad's hands and the frame-up, Cress believes him over Jake's objection, a
messenger brings word that Carline Castle has fallen, and Cress splits the work; in L06 Cress does
not believe him.

**Figures, all re-derived at review rather than taken from the PR.** **4,153 / 8,192, slack 4,039**
— 81× the 50-byte floor. 799 JP → 1,643 EN readable characters = **2.0563×** against the **4.5857**
tier-D ceiling (`tag_bytes` 863, `english_budget` 3,664 characters), **44.8 %** of the English budget
spent; 799 / 5,731 / 4.59 all match `translation_prompt.md` §0.3's own table. **108 text rows**
(source 104), widest **23**, **eight at 23**, none at 24, **no page over 4 text rows** and none the
source did not already have. `{FFFE}` **87 → 89 (+2)**, on **L05 only** (52 → 54); `{FCC0}` **11 →
11**, unchanged on every line and none added. Per-line bytes L01 448→786 · L05 1,482→2,544 ·
L06 290→528 · L07 142→196; L05 alone JP 518 → EN 1,047 = **2.0212×**. `assemble.py check` → "All
checks passed"; `rowcheck.py 22` prints **no `!!` at all**. `bankmeasure` not required (nothing under
`tl/script/` changed) but run: no bank negative, banks 41 (353) and 40 (471) byte-for-byte untouched.
**Every figure above except one matches the PR exactly** — the exception is `{FCC0}` "untouched at
8", where *untouched* is right and the count is 11 (§37.6.1).

### 37.1 People, ranks and words first rendered here — four promotions out of §9, one row struck

| Japanese | English | Note |
|---|---|---|
| ジェイク | `Ｊａｋｅ` | 4 columns. **Promoted from §9 (wave-5 seed), used exactly as seeded.** Cress's subordinate: he reports the 9th Army's arrival (L01), questions the order to open the fort (`隊長！よいのですか？` → `Ｃａｐｔａｉｎ！` / `Ａｒｅ　ｙｏｕ　ｓｕｒｅ？`), objects once more (`しかし・・・`) and answers `はっ！`. **2 battle / 0 script, both in this chunk** — counted at review. **Not cross-unit**, so §9's row is struck |
| クレス隊長 | `Ｃａｐｔａｉｎ　Ｃｒｅｓｓ` | **13 columns, 14 with the vocative comma** — the seed's 13 confirmed. **Promoted from §9.** §1 fixes クレス → `Ｃｒｅｓｓ` and §2 隊長 → captain; a new **appellation**, not a new reading, so §1's `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ` for `クレス少尉` (shipped in `chunk_008`) is untouched. `クレス隊長` is battle chunk **22 only**. See §37.4 |
| リオン将軍 | `Ｇｅｎｅｒａｌ　Ｌｅｏｎ` | **12 columns.** **Promoted from §9, used exactly as seeded.** §1 fixes リオン → `Ｌｅｏｎ` (rendered in `chunk_006`), §26.2 将軍 → `Ｇｅｎｅｒａｌ` — matching the shipped `Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ` (chunks 13, 18) and `Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ` (chunk 21 ×2, this chunk). `リオン将軍` is battle chunk **22 only** |
| ５軍 / 第５軍 | `５ｔｈ　Ａｒｍｙ` | 8 columns, on §2's `第９軍 / ９軍` series; `５` full-width. **Promoted from §9.** ⚠️ **NOT a new form — see §37.3.** `chunk_013` L2 already ships bare `５軍` → `ｔｈｅ　５ｔｈ　Ａｒｍｙ` and this unit **matches it byte-for-byte**; `chunk_008` L4/L9 ship the coordinated plural `７ｔｈ　ａｎｄ　５ｔｈ　Ａｒｍｉｅｓ` / `ｔｈｅ　５ｔｈ　ａｎｄ　７ｔｈ　Ａｒｍｉｅｓ’`, and `chunk_013` L1 ships `宮廷５軍` → `ｔｈｅ　５ｔｈ　Ｒｏｙａｌ　Ａｒｍｙ` on §20.1's prefixed series. **5 battle (8 ×2, 13 ×2, 22 ×1) + 3 script** (unique 524, 995); `batch_005` renders 995 as a coordinated plural. **All five battle instances are now rendered** |
| 実権 | `ｒｅａｌ　ｐｏｗｅｒ` | 10 columns. `宮廷軍の実権を握っていたんだ。` → `ａ　ｆｏｒｇｅｄ　ｍｅｄａｌ　ｔｏ　ｈｏｌｄ` / `ｔｈｅ　ｒｅａｌ　ｐｏｗｅｒ　ｉｎ　ｔｈｅ` / `Ｒｏｙａｌ　Ａｒｍｙ．` Political power, held **distinct** from §4's 攻撃力 / 防御力 / 戦闘力 → attack / defence / combat *power*, §29.1's 動力 → *motive power* and §12.1's 魔道の力 → *the power of magic* — a different collocation each time. **1 battle + 2 script-unique** (`宮廷軍の実権を握った。`, `当時、ファリーナの実権を`), so the form will be reached again. Verified free at review |
| 誤解 | `ｍｉｓｕｎｄｅｒｓｔｏｏｄ` (the verb) | 13 columns. `それは誤解だ。` → `Ｙｏｕ’ｖｅ　ｍｉｓｕｎｄｅｒｓｔｏｏｄ．` (L05) and `クレス、誤解だ。` → `Ｃｒｅｓｓ，` / `ｙｏｕ’ｖｅ　ｍｉｓｕｎｄｅｒｓｔｏｏｄ．` (L06) — **one form, both instances, the two branches of one scene**, so the player says the same thing whichever way the parley goes. The noun is 18 columns, not the PR's 16 (§37.6.3), and `Ｔｈａｔ’ｓ　ａ　ｍｉｓｕｎｄｅｒｓｔａｎｄｉｎｇ．` is **26** — it cannot share a row on a page already at four. `ｍｉｓｔａｋｅ` was rejected because `pending/chunk_017` spends it on `まちがいない` → `Ｎｏ　ｍｉｓｔａｋｅ．`. **2 battle / 0 script, both here.** Verified free across `tl/` **and** `pending/` |
| 見損なう | `ｍｉｓｊｕｄｇｅ` | 9 columns. `私はお前を見損なっていたようだ。` → `ｉｔ　ｓｅｅｍｓ　Ｉ　ｈａｖｅ` / `ｍｉｓｊｕｄｇｅｄ　ｙｏｕ．` Deliberately **not** §30.4's reserved `ｕｎｄｅｒｅｓｔｉｍａｔｅ` (held for 甘く見る / 見くびる) and not its `ｍｉｓｒｅａｄ` (読みが甘い) — three source words, three English forms, which is what §30.4 wrote that reserve to protect. ⚠️ **Stronger than the PR argued, and confirmed at review**: 見損なう here is the *disappointment* sense — Cress thought too **well** of the player — so `ｕｎｄｅｒｅｓｔｉｍａｔｅ` would invert the direction of the error, not merely spend a reserve. **1 battle / 0 script.** Verified free |
| 鎮圧 | `ｐｕｔ　…　ｄｏｗｎ` | 8 columns. **Not a new form — recording one already rendered.** `pending/chunk_043.txt` L4 ships `地上の反乱を鎮圧するための` → `ｌａｓｅｒ　ｗｅａｐｏｎｓ　ｔｏ　ｐｕｔ` / `ｄｏｗｎ　ｒｅｖｏｌｔ　ｏｎ　ｔｈｅ` / `ｇｒｏｕｎｄ　ｂｅｌｏｗ．`, and this chunk's `ここで鎮圧させてもらう。` → `ｐｕｔ　ｙｏｕ　ｄｏｗｎ　ｈｅｒｅ．` matches it. **2 battle / 0 script — both now rendered, so the word is closed** |
| 反乱 (bare) | `ｒｅｖｏｌｔ` | 6 columns. Same source as above: `pending/chunk_043` already ships `ｒｅｖｏｌｔ` for bare 反乱, and `俺たちは反乱なんて起こすつもりはない。` → `Ｗｅ　ｈａｖｅ　ｎｏ　ｉｎｔｅｎｔｉｏｎ` / `ｏｆ　ｒａｉｓｉｎｇ　ａ　ｒｅｖｏｌｔ．` matches. Held **distinct** from §26.4's 反乱軍 → *the rebels*, which this chunk also carries (`反乱軍に仕立て上げ、` → `ｂｒａｎｄｅｄ　ｕｓ` / `ａｓ　ｒｅｂｅｌｓ`) — **both words appear in one message**, so they could never have collapsed. ⚠️ **COUNT ADDED 2026-09-09 (PR #33 review) — an ADDITION, not a §4.3 correction: this row never carried a count or a closure claim.** Measured over both dumps with `反乱(?!軍)`: **3 battle (c22 L6, c38 L4, c43 L4) + 4 script (DATA 443, 785, 896, 1383)** — chunk 38 renders the third battle instance, `反乱となれば` → `Ｗｈｅｒｅ　ｔｈｅｒｅ　ｉｓ　ｒｅｖｏｌｔ，`, matching this row. ⚠️ **SCOPE: this row is the BATTLE store's form. §38.3 fixes the same bare word to `ｒｅｂｅｌｌｉｏｎ` from `batch_007` (script banks 2/3), and both stand** — §25.3's co-occurrence test is met (different stores; no shared chunk, bank or message), but a script batch reaching DATA 443/785/896/1383 must take §38.3's form, not this one. ⚠️ **The "2 battle / 0 script — closed" clause belongs to the `鎮圧` row directly above, where it is TRUE** (chunks 22 and 43, verified at this review); PR #33's Flag 4 quoted it against this row, and that misattribution is recorded rather than acted on — see `FLAGS.md` §AI |
| 責任をとる | `ａｎｓｗｅｒ　ｆｏｒ　…` | `責任は、私がとる。` → `Ｉ　ｗｉｌｌ　ａｎｓｗｅｒ　ｆｏｒ　ｉｔ．` (21 columns). **Not a new form**: §15.2 fixes `責任はどうとるつもりだ` → `ｈｏｗ　ｄｏ　ｙｏｕ　ｉｎｔｅｎｄ　ｔｏ　ａｎｓｗｅｒ　ｆｏｒ　ｔｈｉｓ` (shipped, `batch_002` L9) and `pending/chunk_005` L28 ships `私が責任を持ちます。` → `Ｉ　ａｎｓｗｅｒ　ｆｏｒ　ｉｔ．` This is the third member and it matches both. **3 battle + 4 script-unique** |
| 犠牲者 | `ｃａｓｕａｌｔｉｅｓ` | 10 columns. `これだけの犠牲者を出しておきながら、` → `Ａｆｔｅｒ　ｃａｕｓｉｎｇ　ｔｈｉｓ　ｍａｎｙ` / `ｃａｓｕａｌｔｉｅｓ，`. Military English for battle dead; *victims* would read as civilians, which is not what Cress means. **1 battle + related 犠牲 forms elsewhere** (`かなりの犠牲を` battle, `甚大な兵力を犠牲にした` script), so the noun is fixed here. Verified free |
| 援護する | `ｓｕｐｐｏｒｔ` | 7 columns, **lowercase**. `リオン将軍とアルフレッドを援護してくれ。` → `９ｔｈ　Ａｒｍｙ，　ｓｕｐｐｏｒｔ` / `Ｇｅｎｅｒａｌ　Ｌｅｏｎ　ａｎｄ` / `Ａｌｆｒｅｄ，　ｗｈｏ　ｒｅｍａｉｎ` / `ｉｎ　ｔｈｅ　ｃａｓｔｌｅ．` A hapax — **1 battle / 0 script** — but fixed so it cannot drift. Held **distinct** from §2's 援軍 → *reinforcements / aid*, §20.3's 救援 → *go to … aid* and §24.2's 増援 → *reinforcements*: four source words, four English forms. ⚠️ Lowercase `ｓｕｐｐｏｒｔ` verified free at review; §26.3's `“Ｓｕｐｐｏｒｔ　Ｅｆｆｅｃｔ”` (支援効果) is capitalised, quoted and script-only, and §25.3's test is met (支援 script-only, 援護 battle chunk 22 only) |
| 取り巻きの連中 | `ｈａｎｇｅｒｓ‐ｏｎ` | 10 columns, uses `‐` (U+2010). Fernando's circle of followers. **1 battle / 0 script.** Verified free |
| 招集をかける | `ｓｕｍｍｏｎ` | `取り巻きの連中に招集をかけているだろう。` → `Ｈｅ　ｗｉｌｌ　ｂｅ　ｓｕｍｍｏｎｉｎｇ` / `ｈｉｓ　ｈａｎｇｅｒｓ‐ｏｎ．` **2 battle / 0 script** — the other is `兵士の招集と配備を`, untranslated, and it takes the noun; `ｄｅｐｌｏｙ` for 配備 is already fixed at §31.2. Verified free |
| 血祭りにあげる | `ｐｕｔ　…　ｔｏ　ｔｈｅ　ｓｗｏｒｄ` | `奴らを血祭りにあげるのだ！！` → `Ｗｅ　ｓｈａｌｌ　ｐｕｔ　ｔｈｅｍ` / `ｔｏ　ｔｈｅ　ｓｗｏｒｄ！！` A **genuine English equivalent** — both phrases mean *slaughter them* — so §2's ban on importing an unrelated idiom is not engaged, on the §20.3 貧乏クジをひく and §26.4 石橋を叩いて渡る precedent. A hapax, 1 battle / 0 script |
| つるむ | `ｉｎ　ｌｅａｇｕｅ　ｗｉｔｈ` | 14 columns. ⚠️ **NOT a new form and CROSS-UNIT with chunk 21 — see §37.2, which is this section's most consequential entry.** `chunk_021` L13 already ships `帝国とつるんでいたと聞けば、` → `ｗｅｒｅ　ｉｎ　ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ` / `Ｅｍｐｉｒｅ　ａｌｌ　ａｌｏｎｇ，`, and this unit's `お前が帝国とつるんでいる` → `ａｒｅ　ｉｎ　ｌｅａｇｕｅ　ｗｉｔｈ` / `ｔｈｅ　Ｅｍｐｉｒｅ？` **agrees byte-for-byte on the phrase**, tensed to its own source (`〜ていた` past, `〜ている` present). The PR's "`ｌｅａｇｕｅ` verified free" was **true when written** and is stale. **2 battle (21, 22) + 1 script-unique** (`俺たちが帝国とつるんで`) — all three the same accusation, so the form is fixed now |
| 仕立て上げる | `ｂｒａｎｄ　…　ａｓ` | `反乱軍に仕立て上げ、` → `ｂｒａｎｄｅｄ　ｕｓ` / `ａｓ　ｒｅｂｅｌｓ，`. A hapax. `ｂｒａｎｄ` verified free |
| 始末する | `ｄｏ　ａｗａｙ　ｗｉｔｈ` | The euphemism kept as a euphemism, not flattened to *kill*: `始末しようとしたんだ。` → `ｔｏ　ｄｏ　ａｗａｙ　ｗｉｔｈ　ｕｓ．` A hapax in this sense. Verified free |
| いくらなんでも | `Ｂｅｙｏｎｄ　ａｌｌ　ｂｅｌｉｅｆ，` | 18 columns. **A §2 departure, ratified at review — see §37.5.** A hapax; `ｂｅｙｏｎｄ` verified free in both cases |
| やはり、 | `ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ` | **Not a new form.** `pending/chunk_043` L12 ships `やはりな。` → `Ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ．` and this unit's L07 `くっ、やはり、` → `Ｔｃｈ，　ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ，` matches it, with the source's own `、` per §5. **5 battle / 0 script** (`くっ、やはり、`, `やはり反乱軍の`, `・・・やはり、`, `やはり本当だっ`, `やはりな。`), so the form is fixed now rather than re-invented four more times |
| フン、 | `Ｈｍｐｈ，` | ⚠️ **Recorded here only because it is the second half of a cross-unit pair.** §36.1 fixed this same third kana spelling **one merge earlier**, from chunk 21; chunk 22 renders it independently and identically. No new decision — see §37.2's table |

### 37.2 ⚠️ A SECOND cross-unit term between chunks 21 and 22 — `つるむ` — and the units agree

The wave-5 dispatch named five cross-unit terms; §X5 corrected it to one (`ライアン`). **Both counts
are wrong, and the reason is that both looked only at seeded proper nouns.** Swept at this review
over every kanji/katakana run of ≥2 characters shared by the two chunk sources, plus the kana-bearing
phrase families that filter cannot see:

| term | c21 | c22 | c21 English | c22 English | |
|---|---|---|---|---|---|
| `フェルナンド` | 2 | 7 | `Ｆｅｒｎａｎｄｏ` | `Ｆｅｒｎａｎｄｏ` | ✓ §1 |
| `ライアン` | 1 | 1 | `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｒｙａｎ` | `Ｃａｐｔａｉｎ　Ｒｙａｎ` | ✓ each with its own source rank |
| `宮廷軍` | 4 | 2 | `Ｒｏｙａｌ　Ａｒｍｙ` | `Ｒｏｙａｌ　Ａｒｍｙ` | ✓ §2 |
| `将軍` | 2 | 2 | `Ｇｅｎｅｒａｌ` | `Ｇｅｎｅｒａｌ` | ✓ §26.2 |
| `帝国` | 1 | 1 | `ｔｈｅ　Ｅｍｐｉｒｅ` | `ｔｈｅ　Ｅｍｐｉｒｅ` | ✓ §2 |
| **`つるむ`** | **1** | **1** | `ｗｅｒｅ　ｉｎ　ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ　Ｅｍｐｉｒｅ` | `ａｒｅ　ｉｎ　ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ　Ｅｍｐｉｒｅ` | ✓ **byte-identical on the phrase** |
| `フン、` | 1 | 1 | `Ｈｍｐｈ，` | `Ｈｍｐｈ，` | ✓ §6 / §36.1 |
| `〜つもり(は/なんて)ない` | 1 | 1 | `Ｗｅ　ｈａｖｅ　ｎｏ　ｉｎｔｅｎｔｉｏｎ　ｗｈａｔｅｖｅｒ　ｏｆ　ｆｉｇｈｔｉｎｇ！` | `Ｗｅ　ｈａｖｅ　ｎｏ　ｉｎｔｅｎｔｉｏｎ　ｏｆ　ｒａｉｓｉｎｇ　ａ　ｒｅｖｏｌｔ．` | ✓ same frame, independently |

**Eight shared terms, zero divergences, no re-cut.** Two units drafted in parallel by different
agents agreed on every one, including three the coordination machinery never mentioned.

> **The lesson, and it is not "count better": a translator's freshness sweep can only ever be a
> snapshot.** `つるむ`'s row says "`ｌｅａｇｕｅ` verified free", which was **true at 02:37Z** when both
> PRs were open and neither was in `tl/`. It became false when #18 merged, before #19 was reviewed.
> **A sibling PR's forms enter `tl/` between drafting and review, so re-running gate 7 against the
> tree as it stands at merge is the reviewer's job and cannot be delegated upward to a better
> dispatch.** §X3 recorded `pending/` as the blind spot in a freshness claim; this is the same claim
> failing on **time** instead of on tree. Both have the same fix — say *what* the sweep covered and
> *when*.

**What the dispatch could reasonably have caught** is narrower and worth stating: it listed only
seeded proper nouns. `つるむ`, `フン` and the `つもり` frame are ordinary vocabulary, and no seed list
will ever contain them. The general defence is the one that worked here — both translators reached
for the same English — plus the reviewer's own lexical sweep of the sibling pair, which took one
script. **Recommended for every future wave that ships two battle chunks: run the ≥2-character
run intersection between them at the second merge.**

### 37.3 `５軍` and `ありがとう。` — two more reach figures that pointed at the wrong tree

Neither changes a rendering; both agree with shipped work. Recorded together because they are one
mistake made twice, and it is §35.3's "a substring grep is not a census" seen from the other side —
the counts were fine, the **trees searched** were not.

- **`５軍`.** The §9 seed said "**`tl/script/batch_005.tsv` already carries a `５軍` line, so grep it
  before writing**". The translator did exactly that, found `５軍と６軍が、反乱軍に` →
  `Ｗｏｒｄ　ｉｓ　ｔｈｅ　５ｔｈ　ａｎｄ　６ｔｈ` / `Ａｒｍｉｅｓ　ｆｅｌｌ　ｔｏ　ｒｅｂｅｌｓ．`, reported no
  conflict, and was right. **But `５軍`'s five battle occurrences are chunks 8, 13 and 22, and two of
  those were already shipped**: `chunk_013` L2 ships the bare form as `ｔｈｅ　５ｔｈ　Ａｒｍｙ` — the
  exact string this unit uses. The row records a **match**, not a coinage.
- **`ありがとう。`** The PR's Flag 12 names `chunk_004` L10 as the shipped `Ｔｈａｎｋ　ｙｏｕ．` its
  lowercase continuation differs from. There are **seven**: `chunk_004` L10, `chunk_007` L19,
  `pending/chunk_005` L28, `pending/chunk_043` L41 + L42 and `pending/chunk_043_abridged` L41 + L42.
  The ruling is unchanged and correct — `わかった。` / `クレス、` / `ありがとう。` →
  `Ｒｉｇｈｔ．` / `Ｃｒｅｓｓ，` / `ｔｈａｎｋ　ｙｏｕ．` is a vocative with its clause, and §31.4's
  comma-to-stop promotion does not reach a vocative — only the number was short, and four of the
  seven are in `pending/`.

Same shape in the duplicate table, where every named match is right and several are partial:
`まったく、` → `Ｒｅａｌｌｙ，` also `chunk_012`; `・・・・・` also `chunk_010`; `・・・・` also
`chunk_018`; `はっ！` → `Ｓｉｒ！` also `chunk_013`.

### 37.4 The `ライアン` two-title question — the RENDERINGS are ratified, the PROMOTION READING is not

§9's seed proposed rendering each occurrence with its own source rank (correct, and §26.2 already
permits it) **and** that "a promotion between chapters is the likelier reading for ライアン (21 →
22)"; the PR agreed. **The first half is ratified. The second is not, on evidence neither had.**

| | who is speaking | what they call him |
|---|---|---|
| `chunk_021` L13 | portrait **0000** on `{FC51}` — a 9th Army soldier pleading with an officer over him (§36.9: "Polite ます/ません to a superior") | `ライアン少尉` |
| `chunk_022` L01 | portrait **0006** on `{FC50}` — **Ryan's own subordinate**, reporting to him | `ライアン隊長` |

**An outsider using the substantive rank and his own man using the functional address accounts for
both with no promotion at all**, and §2's own 隊長 row says in its own words that 隊長 is a function
("how the player character is addressed"). Chapter order supports promotion; speaker relationship
supports function; neither is decisive. The PR's third support — that commanding the assault fits a
captaincy — is weak: `全軍、攻撃開始！` takes §25.1's `Ａｌｌ　ｕｎｉｔｓ`, a field command.

> **Ruled: both renderings stand, and the reading behind them is left OPEN.** Nothing rides on it —
> §26.2's source-rank rule is correct either way, which is precisely why the record must not harden
> a guess into a fact. **The test**: a chunk that puts `ライアン少尉` and `ライアン隊長` in one scene,
> or one that gives him a third rank. `ライアン` is battle chunks 21 and 22 only, so unless the
> script dump yields one, the question stays open permanently and harmlessly.

The same caution applies to `クレス隊長` beside §1's `クレス少尉`: chunk 22 is the first 隊長 for
Cress, both forms are rendered per source, and no reading of the rank is asserted.

### 37.5 `いくらなんでも、` → `Ｂｅｙｏｎｄ　ａｌｌ　ｂｅｌｉｅｆ，` — §2 departure RATIFIED

`いくらなんでも、正面から乗り込んでくるとは・・・。` →
`Ｂｅｙｏｎｄ　ａｌｌ　ｂｅｌｉｅｆ，` / `ｔｏ　ｃｏｍｅ　ｍａｒｃｈｉｎｇ　ｉｎ` / `ｆｒｏｍ　ｔｈｅ　ｆｒｏｎｔ．．．．`
(18 / 19 / 18) — the source's three rows, its four stops and its trailing-off astonishment, all kept.

The literal ("no matter how much", "even allowing for anything") is not idiomatic English standing
before an exclamative 〜とは, which is `translation_prompt.md` §2's own licence. **§33.6 governs the
construction and puts it outside `Ｓｕｒｅｌｙ`'s scope**: the 〜とは exclamative "takes the English
that fits its own clause", and `Ｓｕｒｅｌｙ` is §31.3's まさか form. The alternatives are spent or
worse — `Ｅｖｅｎ　ｓｏ` on それでも (§25.2, verified at review), `ｏｆ　ａｌｌ　ｔｈｉｎｇｓ` on chunk
19's まさか…とはな (§33.6).

⚠️ **One correction to the PR's own mitigation, which does not change the ruling.** It says the faint
`belief` / `believed` echo with L06's `ｃａｎ　ｂｅ　ｂｅｌｉｅｖｅｄ．` is "four scenes away **and in the
other branch of the parley**". L01 is not in either branch — **it plays before the L05/L06 fork**, so
a player on the hostile path sees both in one run and the echo is real, not hypothetical. It is
benign: the Japanese words differ (`いくらなんでも` / `信じられる`), §3 is not engaged, and whether
Cress believes the 9th Army is the whole subject of the chapter.

### 37.6 Four PR figures corrected, and one under-described mechanism

**None of them touches the file**, and the per-line `{FFFE}` table that CLAUDE.md §6 gate 4 actually
turns on is complete and correct. This is §X1's shape a second time, and the standing recommendation
there — state a summary as the tool reports it or omit it — is repeated with a second instance behind
it.

1. **`{FCC0}` "untouched at 8" — the count is 11** (L01 3, L05 6, L06 2), identical in source and
   translation. *Untouched* is right and verified line by line; only the number is wrong. It is the
   figure that gets copied into `HANDOFF.md`.
2. **Flag 2's two rejected three-row splits measure 23, not 24**, because `Ｅｍｐｉｒｅ` is 6 columns:
   `ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ　Ｅｍｐｉｒｅ？` = **23** and `ｔｈｅ　Ｅｍｐｉｒｅ？　Ｉｓ　ｉｔ　ｔｒｕｅ？` =
   **23**. A legal three-row split therefore exists —
   `{FC00}{=0000}，` (8) / `ｉｓ　ｉｔ　ｔｒｕｅ　ｙｏｕ　ａｒｅ　ｉｎ` (21) /
   `ｌｅａｇｕｅ　ｗｉｔｈ　ｔｈｅ　Ｅｍｐｉｒｅ？` (23) — so the added `{FFFE}` was **elective, not
   forced**. **It stands**: §3.2 says a break is cheap above ratio 2.5 and to spend free bytes on
   breaks rather than longer words, and the shipped 8 / 19 / 18 / 11 has headroom on every row where
   the alternative sits on the 23 ceiling. The choice is right; the reason given for it was not.
3. **`ａ　ｍｉｓｕｎｄｅｒｓｔａｎｄｉｎｇ` is 18 columns, not 16.** Conclusion unaffected —
   `Ｔｈａｔ’ｓ　ａ　ｍｉｓｕｎｄｅｒｓｔａｎｄｉｎｇ．` is 26.
4. **Flag 9's "three-way echo of 話" is a two-way echo.** L05 p01's `という話は` correctly dissolves
   into `ｉｓ　ｉｔ　ｔｒｕｅ　ｔｈａｔ…` and renders no *story*; only p16 (`Ｔｈａｔ　ｓｔｏｒｙ　ｏｆ　ｙｏｕｒｓ．`)
   and p26 (`{FC00}{=0000}’ｓ　ｓｔｏｒｙ`) carry the word. Dissolving it is right, but it is one of the
   two supports the possessive was chosen on, so that support is weaker than stated. The possessive
   is accepted on other grounds (`FLAGS.md` §Y1).

**Flag 7's `ｌｅｄ　ｂｙ　Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ！` = 24 is CORRECT** — but the departure to
`ｕｎｄｅｒ` was **not forced**, as the Flag claims. A four-row recut of the same page keeps the
literal inside 23: `Ｉ，　Ｉｔ　ｉｓ　ｔｅｒｒｉｂｌｅ！` (18) /
`Ｃａｒｌｉｎｅ　Ｃａｓｔｌｅ　ｉｓ　ｔａｋｅｎ` (23) / `ｂｙ　ｔｈｅ　２ｎｄ　Ａｒｍｙ，　ｌｅｄ　ｂｙ` (23) /
`Ｇｅｎｅｒａｌ　Ｆｅｒｎａｎｄｏ！` (17) — same four rows, no new `{FFFE}`, no `{FCC0}`. **`ｕｎｄｅｒ`
stands**: it is standard military English for the identical relation, the plot fact is intact, and
the alternative ends a row on the two-letter `ｂｙ`, which §3.2 asks you to avoid. It is a choice
between two soft constraints, not a forced §2.1 step 4, and is recorded as the former.

**Flag 10's speaker attributions are all correct; its mechanism is under-described.**
`{FCB0}{=00PP00SS}` assigns portrait **PP** to **slot SS**, and `{FC50}` / `{FC51}` speak from slot
**0** / slot **1**. "Same id on both channels" restates Cress's two rows; the slot model *predicts*
them — Cress holds slot 0 until Jake takes it at L05 p24, moves to slot 1 for p26–p31, and returns to
slot 0 at p42 the moment Jake is done — and it is the only reading that covers **L05 p06**
(`フェルナンドを？どういうことだ。`), which carries **no `{FCB0}` at all** and is Cress purely because
slot 0 still holds him. ⚠️ Per §W5 this is derived inside chunk 22 and is **not** carried to any
other chunk; it is an observation consistent with §23.5 / §28.7 / §30.7, not a settled engine fact,
and belongs to `findings.md` if a later chunk corroborates it.

### 37.7 Recorded, not re-cut — checked and not defects

- **The two branches keep Cress's register apart correctly.** L05 (he believes) and L06 (he does not)
  are mutually exclusive, and Cress is contraction-free in both — `Ｉｔ　ｉｓ　ａｌｌ　ｒｉｇｈｔ．`,
  `Ｉ　ｗｉｌｌ　ａｎｓｗｅｒ　ｆｏｒ　ｉｔ．`, `Ｉ　ｓｈａｌｌ　ｈｏｌｄ　ｂａｃｋ．` against
  `ｄｏ　ｙｏｕ　ｔｈｉｎｋ　ｓｕｃｈ　ｗｏｒｄｓ　ｃａｎ　ｂｅ　ｂｅｌｉｅｖｅｄ．`,
  `ｉｔ　ｓｅｅｍｓ　Ｉ　ｈａｖｅ　ｍｉｓｊｕｄｇｅｄ　ｙｏｕ．`, `Ｉ　ｓｈａｌｌ　ｐｕｔ　ｙｏｕ　ｄｏｗｎ　ｈｅｒｅ．`
  **One man's register carrying two outcomes**, with the difference in content, not in voice. The
  player contracts throughout in both, so the channels read as two voices.
- **L07 is Cress**, on its own `{FCB0}{=00050000}` (slot 0, portrait 05) — Flag 10 does not name it.
  `Ｔｃｈ，　ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ，` / `ｍｕｓｔ　ｉｔ　ｃｏｍｅ　ｔｏ` / `ｆｉｇｈｔｉｎｇ．．．` is
  contraction-free with a formal inversion, so his register holds into the battle-open line.
- **Rhetorical questions ending `。` stay declarative**: `どういうことだ。` →
  `Ｗｈａｔ　ｄｏ　ｙｏｕ　ｍｅａｎ．` and `信じられると思うのか。` → `…ｃａｎ　ｂｅ　ｂｅｌｉｅｖｅｄ．` The
  punctuation follows the source, which is §5's mechanism and §36.8's `か。` sweep.
- **All six vocatives take a lowercase continuation** and are consistent with each other:
  `Ｃａｐｔａｉｎ　Ｃｒｅｓｓ，` / `ｔｈｅｙ`, `Ｃａｐｔａｉｎ　Ｒｙａｎ，` / `ｔｈｅ`, `Ｊａｋｅ，` / `ｏｐｅｎ`,
  `Ｃｒｅｓｓ，` / `ｙｏｕ’ｖｅ` and / `ｔｈａｎｋ`, and all four `{FC00}{=0000}，` rows. §31.4's
  comma-to-stop promotion is scoped to a fixed assent word followed by an independent clause and does
  not reach a vocative, which is not a clause.
- **`ｄｏ　ｎｏｔ　ｐｕｓｈ　ｔｏｏ　ｈａｒｄ．` differs from `chunk_008` L4's by one capital, and §3 is not
  engaged in either direction** — the source strings genuinely differ (`あまりムチャはするなよ。` here,
  `あまり無理はするなよ。` there), verified in the dump. `chunk_013` L4's third form for the same act
  (`くれぐれも無理はするなよ。` → `ｐｕｓｈ　ｙｏｕｒｓｅｌｆ　ｔｏｏ　ｆａｒ．`) is correctly untouched.
- **`１人占め` against `chunk_020`'s `独り占め`** is one idiom in two spellings, and both ship
  §32.2's `ｋｅｅｐ　ｔｈｅ　ｃｒｅｄｉｔ　ｔｏ　ｍｙｓｅｌｆ` — byte-identical, verified at review.
- **`勲章` ×2 → `ｍｅｄａｌ`** (§32.1), matching `chunk_020` L47/L48. This chunk is the first place the
  plot explains the item, but it reaches **no bank**, so §32.5 / `FLAGS.md` §T2's live `メダル`
  collision in banks 42–43 is neither worsened nor discharged.
- **`了解` 0, `わかった` 1, `まさか` 0** — counted in the source at review, so §29.4's `Ａｇｒｅｅｄ．`
  reserve is correctly not engaged (`わかった。` → `Ｒｉｇｈｔ．` per §6, matching `pending/chunk_005`
  L10) and §31.3 / §33.6's `まさか` is neither applied nor tested by this unit.
- **`{FCA8}` appears once** (L07, `{FCA8}{=01C9…}`) but chunk 22 is **not** one of §D1's ten affected
  chunks and `check` passes — the same coincidence §36.8 recorded for chunk 21.
- **§Q2 not re-discovered.** No `{FCC0}` was added; the three pages at the four-row wall (L01 p12,
  L05 p34, L05 p44) were solved inside the source's own page structure.

### 37.8 ⚠️ Cress's gender is unfixed, unrendered, and chunk 37 will reach it

§1's `クレス` row does not state a gender. This PR's own prose uses **both** — "he holds Fernando's
circle" in the Unit summary, "the first 隊長 for **her**" in the `クレス隊長` row. **No shipped
English anywhere genders Cress**: not `chunk_008` L4, not `chunk_013` L1/L2, not this unit, whose
Cress lines are all first-person or vocative. So there is no defect and nothing to change today.

Recorded because **battle chunk 37 carries `クレス` and is untranslated** (the term appears in battle
chunks 8, 13, 22 and 37), and a third-person line there would force the pronoun. What the corpus
offers so far: Cress's speech in this chunk is `私` / `お前` / `〜のか` / `〜てくれ` / `よい` — the
neutral-to-masculine register of §7's officer column, with nothing feminine-marked. **Not enough to
fix it**, which is why it is a flag and not an entry. Whoever takes chunk 37 settles it, and a wrong
choice there would be a §4.3 correction reaching three shipped files.

### 37.9 Register

| Who | Register |
|---|---|
| Cress (portrait 05, both slots) | The §14.6 / §20.5 / §25.5 / §28.6 / §31.7 / §36.9 officer column — **zero contractions in either branch**, `Ｉ　ｓｈａｌｌ` / `Ｉ　ｗｉｌｌ` / `Ｉｔ　ｉｓ` / `ｄｏ　ｎｏｔ`. Warmer than Fernando or Ryan: he takes responsibility (`Ｉ　ｗｉｌｌ　ａｎｓｗｅｒ　ｆｏｒ　ｉｔ．`), overrides his own subordinate gently, and closes with `ｄｏ　ｎｏｔ　ｐｕｓｈ　ｔｏｏ　ｈａｒｄ．` The hostile branch changes **what he says, not how he says it** |
| Ryan (portrait 03) | §36.9's Ryan, unchanged and confirmed from a second chunk — no contractions, contempt carried by `Ｈｍｐｈ，` and `ｔｈｅｙ　ａｒｅ　ｆｏｏｌｓ` / `ｐａｓｔ　ａｌｌ　ｓａｖｉｎｇ．` rather than by added words, and the self-interest stated plainly (`Ｉ　ｃａｎ　ｋｅｅｐ　ｔｈｅ　ｃｒｅｄｉｔ` / `ｔｏ　ｍｙｓｅｌｆ．`) |
| Jake (portrait 07) | Deferential and clipped, **no contractions** — `Ｃａｐｔａｉｎ！` / `Ａｒｅ　ｙｏｕ　ｓｕｒｅ？`, `Ｈｏｗｅｖｅｒ．．．`, `Ｓｉｒ！` (§6). The §20.5 Albert column: he reports and objects, he does not opine |
| Portrait 06 — **two men in one chunk** | In L01 he is Ryan's subordinate (`ライアン隊長、５軍は手を…`); in L05 he is the messenger from Carline Castle, on Cress's side of the map. Both are deferential です / ます and take the same contraction-free register, so nothing rides on the identification — but ⚠️ **per §W5, portrait ids are per-chunk, and here one id is two people inside a single chunk.** Recorded so a later reader does not merge them |
| The player's side (portrait 00) | §7's Kain column unchanged — contractions throughout in **both** branches (`ｙｏｕ’ｖｅ`, `ｗｅ　ｄｏｎ’ｔ`, `Ｉｔ’ｓ　ｔｒｕｅ．`, `Ｉ’ｍ　ａｓｋｉｎｇ　ｙｏｕ．`), which is the contrast that makes Cress's flatness read as rank |

---

## 38. Added by script batch 007 (PR #20, merged 2026-09-09)

Rendered in `tl/script/batch_007.tsv` — `script_unique.txt` **file lines 318 and 421–469**, 50
unique lines / **70 message instances**, banks **2** and **3** plus unique 318 replicated across 19
further banks. 3,015 JP → 6,306 EN = **2.092×**; **7,074 bytes**; bank 2 **7,505 → 3,365**, bank 3
**10,591 → 8,113**, bank 40 **471 → 447**, **bank 41 byte-for-byte untouched at 353**. 367 text
rows, widest 23, seventeen at 23, **none at 24**, no page over 4 text rows the source did not
already exceed. `{FFFE}` **+6 net (12 bytes)** on unique 427, 430, 439, 449 and 460; **`{FCC0}`
untouched and the non-`{FFFE}` tag stream byte-identical on all 50 lines**. Merged at round 1.

The content is the recruitment machinery: one item-description row (318), the tail of a rough human
recruiter's copy of the skeleton (421–426), Leon's introduction (427), two refusals to enter the
castle (428–429), the Hobbit Village chief's potatoes and the Princess's trail (430), Lord Helfer's
briefing and the handover to Anselmo (431), the troop-type menu and its four replies (432–436),
Anselmo on forming units (437), and **three copies of one hobbit-recruiter skeleton** (438–448 /
449–459 / 460–469).

`Ｃｏｍｅ　ｔｏ　ｔｈｉｎｋ　ｏｆ　ｉｔ，` (§19.1 / shipped `chunk_002` L12), `ｍｏｎｓｔｅｒ`
(`batch_001` L33), `ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ` (§19.2), `Ｗｅｌｌ　ｎｏｗ，` (§19.1),
`Ｌｏｒｄ　Ｈｅｌｆｅｒ` (§1), `Ｌｅｏｎ` (§1), `ｔｈｅ　Ｋｉｎｇ` (§28.1), `ｔｈｅ　Ｅｍｐｉｒｅ` /
`ｃａｓｔｌｅ` / `９ｔｈ　Ａｒｍｙ` (§2), `ｔｈｅ　ｍａｙｏｒ` (§1), `ｔｈｅ　ｆａｉｒｙ　ｖｉｌｌａｇｅ`
(§14.2), `ａｌｌｉａｎｃｅ` / `ｆｏｒｍ　（ｙｏｕｒ　ｕｎｉｔｓ）` (§26.3), `Ｒｉｇｈｔ，` (§6, §24.3),
`Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ` (§24.3), `Ｔｈａｔ’ｓ　ｒｉｇｈｔ，` (§23.2), `Ｏｈ，` / `Ｏｈ！` /
`Ｏｈ？` / `Ａｈ，` (§18.2, §24.4), `Ｈｍ？` (§20.3), `Ｅｈ！` (§21.2), `Ｍｏｖｅ　ｏｕｔ！` (§6),
`ｔｈｅｙ　ｓａｙ` (§26.6) and the `，　ｎｙｏｒｏ．` tic in §18.1's spaced form are used unchanged.

### 38.1 Twelve promotions out of §9 (wave-5 seeds) — every one used exactly as seeded

| Japanese | English | Note |
|---|---|---|
| リムローズ | `Ｌｉｍｒｏｓｅ` | **Promoted from §9**, 4 renderings. **7 columns — §9's figure is right** (the PR hand-counted 8 and corrected itself). A **TOWN**. ⚠️ Reach remeasured at review: **10 further `script_dump` instances** (banks 18, 20, 40, 41) **+ 2 battle (chunk 38)** — the PR's "9 further" is one low; its bank and battle figures are exact |
| リムローズの市長 | `ｔｈｅ　Ｌｉｍｒｏｓｅ　ｍａｙｏｒ` | 17 columns. §1 fixes 市長 → *the mayor* lowercase and `chunk_012` L17 ships `Ｉ　ａｍ　ｔｈｉｓ　ｔｏｗｎ’ｓ　ｍａｙｏｒ．`; this is that noun with the town attributive. **Width does not decide it** — the possessive `Ｌｉｍｒｏｓｅ’ｓ　ｍａｙｏｒ，　ｎｙｏｒｏ？` also measures 23 — the attributive was chosen so the break falls where the source's own `の` falls. Reversible at 0 bytes |
| イートン / イートンの森 | `Ｅａｔｏｎ` / `Ｅａｔｏｎ　Ｆｏｒｅｓｔ` | **Promoted from §9**, 5 / 12 columns, 3 renderings in unique 430. Capitalised `Ｆｏｒｅｓｔ` on §2's `カーライン城` and §33.1's `ファリーナ城`, deliberately **unlike** §14.2's 妖精の森 → *the fairy forest* — and unique 430 carries both, correctly split. Reach: **1 further script instance (bank 40), 0 battle**, so §9's "4 script" is right |
| チェコットの丘 | `Ｃｈｅｋｏｔ　Ｈｉｌｌ` | **Promoted from §9**, 11 columns. **A true hapax — 0 further occurrences in either dump**, verified |
| レバーク城 | `Ｌｅｖｅｒｋ　Ｃａｓｔｌｅ` | **Promoted from §9**, 13 columns, on §28.1's `Ｌｅｖｅｒｋ` (a KINGDOM) plus §2's `カーライン城`. **1 further script instance (bank 41), 0 battle** |
| 第２王子のトリフ様 | `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ` | **Promoted from §9**, 12 columns, used exactly as seeded. **The ordinal is dropped — ruled at review and it stands; see §38.5** |
| 第１軍 | `１ｓｔ　Ａｒｍｙ` | **Promoted from §9**, 8 columns, §2's army-number series, digit full-width. `第１軍隊長のリオン` → `Ｉ　ａｍ　Ｌｅｏｎ，　ｃａｐｔａｉｎ` / `ｏｆ　ｔｈｅ　１ｓｔ　Ａｒｍｙ．` — the apposition inverted as §26.2 already does for `２軍のフェルナンド将軍`, and rendered with **the rank the source gives it**, which is §26.2's own rule |
| 兵舎 | `ｂａｒｒａｃｋｓ` | **Promoted from §9**, 8 columns, lowercase (§17.1). Held distinct from 砦 → *fort* (§26.4), 要塞 → *fortress* and 城 → *castle* (§2). `ｂａｒｒａｃｋｓ` verified free across `tl/` and `pending/`. ⚠️ **§9's "4 script" is RIGHT and the PR's correction to it is wrong — see §38.6** |
| ジャガイモ / イモ | `ｐｏｔａｔｏｅｓ` / `ｐｏｔａｔｏ` | **Promoted from §9**, **8 / 6 columns — §9's figures are right** (the PR hand-counted 9 and corrected itself). Lowercase (§17.1). Both verified free. **0 further occurrences of ジャガイモ** |
| バター | `ｂｕｔｔｅｒ` | **Promoted from §9**, 6 columns, lowercase. Verified free. 0 further occurrences |
| ワイン | `ｗｉｎｅ` | **The BARE noun promoted from §9, and only that** — the titled `『極上のワイン』` → `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` ✅ **is now rendered and PROMOTED to §54 (PR #35, merged 2026-09-11); the §9 row is struck there.** ⚠️ **NOTHING IN THIS ROW'S RULING CHANGES** — `ｗｉｎｅ`, 4 columns, lowercase, is the bare noun's form and is untouched. Only this row's forward-looking “stays live in §9 for the unit that first renders it” clause is **discharged**, and it is written out here rather than quietly deleted (§4.3). Verified free (`tl/`'s only hits are *swine*). ⚠️ Reach remeasured: **41 further `script_dump` instances, 0 battle** — the PR's “35” is six low; §9's own “44 script-dump instances” is right |
| とかいじん (都会人) | `ｃｉｔｙ　ｆｏｌｋ` | **Promoted from §9**, 9 columns, lowercase. The hiragana lightness is carried in **register**, not in a misspelling, exactly as the seed directs |
| ナンダイ (難題) | `ａ　ｒｅａｌ　ｐｒｏｂｌｅｍ` | **Promoted from §9**, and **14 columns, not §9's 16** — remeasured twice at review. The katakana emphasis rendered as weight in the English, not transliterated, as the seed directs |
| 『編成』 / 『キャラクター育成』 / 『キャラを入れる』 | `“Ｆｏｒｍａｔｉｏｎ”` / `“Ｃｈａｒａｃｔｅｒ　Ｇｒｏｗｔｈ”` / `“Ａｄｄ　ａ　Ｃｈａｒａｃｔｅｒ”` | **Promoted from §9** — 11 / 18 / 17 columns with the quotes, **all three §9 figures correct as remeasured**. `『…』` → `“…”` per §12. ⚠️ **Raised as a FLAG, not settled — `FLAGS.md` §Z1 and the Blocked list.** §26.3's *verbal* 編成 → *form (your units)* is used unchanged where the source is verbal (unique 437 ×2); the split is the source's own |

**`殿` on the `{FFEC}` player-name insert — §9's decision is EXECUTED and ratified.** Unique 427's
`９軍の隊長に任命された{FFEC}{=00}{=00}殿。` renders `Ｏｈ？　Ｙｏｕ　ｍｕｓｔ　ｂｅ` /
`{FFEC}，　ａｐｐｏｉｎｔｅｄ` / `ｃａｐｔａｉｎ　ｏｆ　ｔｈｅ` / `９ｔｈ　Ａｒｍｙ．` — **carried in
register, no word added**, on §2's 貴官 rule. Leon's contraction-free formality does the work and
the same sentence names the rank, so an added title would say it twice. The `Ｓｉｒ　{FFEC}`
alternative is not taken and stays on record.

### 38.2 Words and phrases first fixed here

| Japanese | English | Note |
|---|---|---|
| 何かの木の木の実。 | `Ａ　ｎｕｔ　ｆｒｏｍ　ｓｏｍｅ　ｔｒｅｅ．` | 21 columns, one row. The item-description table's flat catalogue voice (§17.5); no `ジェムタイプ` suffix. **21 instances across 21 banks**, so +24 bytes in each, 504 in total. `ｎｕｔ` verified free — the only hit in `tl/` / `pending/` is *minute* |
| 補充 (of soldiers) | `ｒｅｃｒｕｉｔ` / `ｒｅｃｒｕｉｔｉｎｇ` | 7 / 10 columns. ⚠️ **`ｒｅｃｒｕｉｔ` is NOT free**: `chunk_000.txt` L4 ships the **noun** `ａ　ｒｅｃｒｕｉｔ！` for a different word. Different part of speech, different message, different bank — recorded so it cannot drift |
| 共同作戦 | `ｊｏｉｎｔ　ｏｐｅｒａｔｉｏｎｓ` | 16 columns, verified free. Held distinct from bare 作戦 → `Ｔｈｅ　ｐｌａｎ？` (§19.2), 作戦会議 → *war council* (§2) and シナリオ → *script* (§31.5) |
| よろしく　頼む / よろしく頼むぞ | `Ｉ　ｓｈａｌｌ　ｃｏｕｎｔ　ｏｎ　ｙｏｕ．` | 21 columns, used twice byte-identically (427, 431). **A third member of §21.2's よろしく family**, held apart from よろしく / よろしくね → `Ｇｏｏｄ　ｔｏ　ｍｅｅｔ　ｙｏｕ` (a first introduction) and よろしくお願いします → `Ｉ　ａｍ　ｉｎ　ｙｏｕｒ　ｈａｎｄｓ` (a formal request). This one is neither: a superior entrusting a future task |
| 手配しておこう。 | `Ｉ　ｓｈａｌｌ　ａｒｒａｎｇｅ　ｉｔ．` | 19 columns, `ａｒｒａｎｇｅ` verified free. Byte-identical in all four replies (433–436), as is `わかった。それでは、` → `Ｒｉｇｈｔ．　Ｗｅｌｌ　ｔｈｅｎ，` |
| そうかい。 | `Ｉ　ｓｅｅ．` | 6 columns. **A fourth source string on §30.3's form**; §25.3's test is MET and counted at review with this unit's own keys excluded — そうか, そうですか and なるほど are **in no bank 2 or 3**. ⚠️ `そうかい` recurs **6 more times (banks 12, 17, 20, 23, 24)**; this binds them. Independently corroborated: `chunk_004` L11 ships the same two-clause shape, `そうか、気をつけてな。` → `Ｉ　ｓｅｅ．　Ｔａｋｅ　ｃａｒｅ．` |
| じゃ、気を付けてな！ | `Ｔａｋｅ　ｃａｒｅ，　ｔｈｅｎ！` | 16 columns. `chunk_004` L11's `気をつけてな。` → `Ｔａｋｅ　ｃａｒｅ．` with the source's own stop and its `じゃ、` carried as a trailing *then* — different source string, same fixed words |
| おいおい、 | `Ｏｉ，　ｏｉ，` | 7 columns. §32.3 fixes おい、 → `Ｏｉ，`; the doubling is preserved per §23.2's `気にしない、気にしない。` and §34.1's `これは、これは！`. §25.3's test MET: おい、 is in banks [5, 41] + **11** battle chunks (the PR's 12 is one high) and **not bank 2**. ⚠️ `おいおい` recurs **twice more (banks 29, 41)** — exact as the PR states |
| 欲張りな　奴だな。 | `Ｗｈａｔ　ａ　ｇｒｅｅｄｙ　ｆｅｌｌｏｗ．` | 21 columns. `ｆｅｌｌｏｗ` for 奴 follows §32.1's register-selected `ｔｈａｔ　〜　ｆｅｌｌｏｗ`; `ｇｒｅｅｄｙ` verified free |
| 地殻の変動 | `ｔｈｅ　ｅａｒｔｈ　ｉｓ　ｓｈｉｆｔｉｎｇ` | Rendered as a clause, not a noun, on §15.2's 黒幕 precedent — *crustal movement* has no place in a rough guard's mouth |
| まったく (as an intensifier) | `Ｒｅａｌｌｙ` + the source's own punctuation | `まったく　恐ろしいぜ。` → `Ｒｅａｌｌｙ　ｔｅｒｒｉｆｙｉｎｇ．` (18). §5's mechanism: §6 fixes the **word** and the punctuation follows the source — no comma here because まったく modifies the adjective directly, so §6's `Ｒｅａｌｌｙ，` (exasperation, standing alone) is untouched |
| 争い | `ｓｔｒｉｆｅ` | 6 columns, verified free. Held distinct from 戦乱 → *war* (unique 460) and 戦闘 → *battle* (unique 437) — **all three occur in this unit** |
| おたずね者 | `ｗａｎｔｅｄ　ｍｅｎ` | 10 columns, verified free |
| 大歓迎 | ⚠️ **NOT a single fixed string — CORRECTED IN PLACE 2026-09-09 (§4.3, PR #22 review); see the RULING at §40.3.** Ironic use takes a *warm / most welcome* phrasing that fits its row; sincere use takes `Ｍｏｓｔ　ｗｅｌｃｏｍｅ` | 12 / 17 columns, built on `translation_prompt.md` §2's own worked example `歓迎しますぞ！` → `Ｙｏｕ　ａｒｅ　ｍｏｓｔ　ｗｅｌｃｏｍｅ！`. Held **distinct** from §34.1's いらっしゃい〜 → `Ｗｅｌｃｏｍｅ` (`batch_006` L58). §25.3's test MET and counted: 大歓迎 banks [0, 3] chunks [7, 15, 26] against いらっしゃい banks [12, 13, 15–19, 22, 25, 26, 43] chunks [5, 6, 33] — **disjoint**. ⚠️ **This row fixed ONE form and its own chunk list names chunk 7, but `tl/battle/chunk_007.txt` body L3 (file line 5) ALREADY SHIPS `Ｓｕｃｈ　ａ　ｗａｒｍ　ｗｅｌｃｏｍｅ！` (19 columns) — verified at the PR #22 review.** The three source messages differ, so CLAUDE.md §3 (which engages on the message, not the phrase) is not violated and **nothing is re-cut**: chunk 7 and chunk 26 both stand. Chunk 15's two remaining instances are **sincere** and take `Ｍｏｓｔ　ｗｅｌｃｏｍｅ`; reach re-measured **4 battle (7, 15, 26) + 6 script (banks 0, 3)** |
| 他に　用はないノロか？ | `Ｎｏｔｈｉｎｇ　ｅｌｓｅ，　ｎｙｏｒｏ？` | 20 columns. **A fourth "anything else?" form, keeping the source's own negative**, held apart from `batch_006`'s three (L35 `Ｉｓ　ｔｈｅｒｅ　ａｎｙｔｈｉｎｇ　ｅｌｓｅ？`, L51 `Ａｎｙｔｈｉｎｇ　ｅｌｓｅ　ｆｏｒ　ｙｏｕ？`, L69 `Ａｎｙｔｈｉｎｇ　ｅｌｓｅ，　ｎｙｏｒｏ？`). The rough human's `他にも用はあるかい？` takes bare `Ａｎｙｔｈｉｎｇ　ｅｌｓｅ？` (14), a fifth. ⚠️ **Binds unique 470** — see `FLAGS.md` §Z2 |
| 兵の数が　いっぱい | `Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ` | 19 columns, `ｒａｎｋｓ` verified free. Deliberately **not** §34.1's 荷物 → `ｐａｃｋ`, which is the inventory; this is the unit roster |
| 念のため忠告しておくが、 | `Ａ　ｗｏｒｄ　ｏｆ　ｃａｕｔｉｏｎ：` | 18 columns; `：` is §3.1-legal |
| 健闘を祈るぞ。 | `Ｉ　ｐｒａｙ　ｙｏｕ　ｆｉｇｈｔ　ｗｅｌｌ．` | 22 columns; keeps both 健闘 and 祈る. `Ｉ　ｐｒａｙ　ｆｏｒ　ｙｏｕｒ　ｓｕｃｃｅｓｓ．` measures **exactly 24** and was rejected on that ground, which §25.1 has twice done and §29.1 once |
| よく参った。 | `Ｗｅｌｌ　ｍｅｔ．` | 9 columns. Helfer's archaic greeting, twice in unique 431, byte-identical. **A genuine hapax pair — 0 occurrences of よく参った outside this line**, verified. ⚠️ Shares its English with `はじめまして。` in **parked** `pending/chunk_005.txt` L23. §25.3's test is MET — はじめまして is script bank 10 and battle chunk 5 only, disjoint from banks 2 and 3 — and the file is parked, so §3 is not engaged either way |
| 上官 | `ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ` | 16 columns. **Not a new form — recording a reuse and one departure.** §19.2 fixes it and `chunk_001.txt` L6/L7 ship `ａ　ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ，`. ⚠️ **Used unchanged TWICE here, not three times as the PR states — see §38.6** |

### 38.3 Interjections

| Japanese | English | Note |
|---|---|---|
| 何だい、 | `Ｗｈａｔ，` | An **eighth** 何-family member, held apart from 何だと？ → `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` (§6), 何だ！？ → `Ｗｈａｔ　ｉｓ　ｉｔ！？` (§23.2), 何？ → `Ｗｈａｔ？` and 何っ！？ → `Ｗｈａｔ！？` (§28.3, §30.3), あれ・・・？ → `Ｗｈａｔ．．．？` (§21.2) and chunk 0's two stuttered forms. **Recorded at review; the PR did not propose a row.** `Ｗｈａｔ，` occurs elsewhere only inside longer redistributed rows (`chunk_020` L4, parked `chunk_005` L29), never as a standalone 何 rendering, so §3 is not engaged |
| 何だぁ。 | `Ｗｈａｔ’ｓ　ａｌｌ　ｔｈｉｓ．` | A **ninth**. **Recorded at review.** Shares its English with parked `pending/chunk_043.txt` L20's `何の騒ぎだ、これは？` → `Ｗｈａｔ’ｓ　ａｌｌ　ｔｈｉｓ　ｎｏｉｓｅ？` — parked and a different string, so §3 is not engaged |
| だめよ。 (refusal) | `Ｔｈａｔ　ｗｉｌｌ　ｎｏｔ　ｄｏ．` | 17 columns, verified free. **Recorded at review.** Held **distinct** from §30.3's ダメです！ → `Ｉｔ　ｉｓ　ｎｏ　ｕｓｅ！`, which is Rendol's despair; this is a refusal. Two senses of だめ, two English forms |
| うーん、 | `Ｈｍｍ，` | **Recorded at review.** A second source string on §26.5's ふーむ → `Ｈｍｍ，` — the same grunt in two kana spellings, the §17.2 鬼 / オーガ shape, and the kana-beat convention gives both the double `ｍ` |
| ふむ、 | `Ｈｍ，` | Verified free. Extends §6's む / ん → `Ｈｍ`; two kana beats, two letters, per §11.5 / §26.5 |
| やめる (giving up) | `ｇｉｖｉｎｇ　ｕｐ` | **Not new, and the PR did not claim it.** `tl/battle/chunk_014.txt` L3 already ships `やめるか、オヤジ？` → `Ｇｉｖｉｎｇ　ｕｐ，　ｏｌｄ　ｍａｎ？`, and **all three of this unit's やめる occurrences match it** — `やめるのかい？` → `Ｗｈａｔ，　ｇｉｖｉｎｇ　ｕｐ？` (421) and `やめるノロか？` → `Ｇｉｖｉｎｇ　ｕｐ，　ｎｙｏｒｏ？` (454, 465). Verified positionally at review |
| 〜ない方がいい | `Ｂｅｔｔｅｒ　ｎｏｔ` | **Not new, and the PR did not claim it.** `batch_006` L67 ships `そいつは　売らない方が` → `Ｂｅｔｔｅｒ　ｎｏｔ　ｔｏ　ｓｅｌｌ　ｔｈａｔ`; unique 429's `やめた方がいい。` → `Ｂｅｔｔｅｒ　ｎｏｔ．` matches it |
| 反乱 / レベルアップ / 功績 / 納得いかない / のんき | `ｒｅｂｅｌｌｉｏｎ` / `ｌｅｖｅｌ　ｕｐ` / `Ｍｅｒｉｔ` / `ｉｔ　ｎａｇｓ　ｍｅ` / `ｅａｓｙ‐ｇｏｉｎｇ` | **Recorded at review**; all five verified free across `tl/` and `pending/`. 反乱 held distinct from §26.4's 反乱軍 → *the rebels / the rebel army*; `‐` in *easy‐going* is U+2010 |

### 38.4 RULING — `ｃｈｉｅｆ` stays lowercase, and the decision binds nothing forward

The PR raised this as its most important open call and it is ruled here on a measurement rather
than on taste. **Every `村長さん` in the game is inside this unit** — 3 occurrences in
`script_dump.txt`, 0 in `battle_dump.txt`, all three inside unique 430. Counted at review.

| Where | Japanese | English |
|---|---|---|
| descriptive | `ホビットの村長さんか。` | `ｈｏｂｂｉｔ　ｖｉｌｌａｇｅ　ｃｈｉｅｆ．` |
| vocative | `そ、村長さん、` | `Ｃ，　ｃｈｉｅｆ，` |
| vocative | `村長さんは。` | `ｃｈｉｅｆ．` |

**All three stay lowercase.** The descriptive one is settled outright: shipped `chunk_002.txt` L12
has `ｔｈｅ　ｈｏｂｂｉｔ　ｖｉｌｌａｇｅ’ｓ` / `ｃｈｉｅｆ` in word **and** case, and §20.1 fixes
村長 → *village chief*. The two vocatives follow it because §17.1's species test reads `chief` here
as **what he is**, not a title conferred on an individual, and because §21.2's drop-the-honorific
rule plus §2's politeness rule put `さん` into register rather than into an added English word.

⚠️ **The counter-case is real and is recorded so it is not lost**: §24.3's shipped comma-stutter
rows all capitalise (`Ｗ，　Ｗａｉｔ！`, `Ｗ，　Ｗｅｌｌ，`, `Ｉｍ，　Ｉｍｐｏｓｓｉｂｌｅ．．．`), and
§28.2's `お兄ちゃんたち` → `Ｍｉｓｔｅｒ，` and §2's トカゲさん → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ` are
capitalised vocatives on non-name nouns. Against that: in all three of §24.3's rows the capital is
purely **sentence-initial** on a word that is not a role noun, and here `Ｃ，` already carries the
sentence-initial capital. **Reserve, at 0 bytes either way: `Ｃ，　Ｃｈｉｅｆ，` and `Ｃｈｉｅｆ．`**
Because this unit exhausts the corpus, adopting the reserve later would touch these two rows and
nothing else. `Ｈｏｂｂｉｔ　Ｖｉｌｌａｇｅ！` two segments earlier **is** capitalised, correctly — there
it is §2's place name (`ホビットの村のじいさん`), not a description.

### 38.5 RULING — the Torif ordinal is dropped, and the measurement is what settles it

`第２王子のトリフ様` → `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ` uses §9's seed exactly and **drops 第２王子**. The
translator flagged it and declined to overrule a seed unilaterally, which was right; the call is the
reviewer's. **It stands**, on three counted facts:

1. **`第２王子` occurs exactly ONCE in the entire script dump — this very line — and zero times in
   the battle dump.** Nothing else in the game inherits the drop.
2. **The same fact is carried twice more by `弟のトリフ`** (2 script occurrences), which is the
   evidence §9's own `ホアグ王子` row cites for Torif being the younger brother. **No plot fact is
   lost from the game**, only from one hobbit's travel gossip, where the name alone identifies him.
3. **Restoring it costs a page re-flow in either form.** The page carries 4 text rows already, and
   ⚠️ **the one-row swap the PR floats does not in fact fit**: the row is
   `ｔａｋｅｎ　Ｐｒｉｎｃｅ　Ｔｏｒｉｆ　ａｎｄ` at 22, and `ｔａｋｅｎ　Ｓｅｃｏｎｄ　Ｐｒｉｎｃｅ　Ｔｏｒｉｆ　ａｎｄ`
   measures **29**, not the 19 the seed quotes for the bare title form. Remeasured at review.

⚠️ **Forward obligation.** The two `弟のトリフ` lines are now the **only** place Torif's birth order
lives. Whoever renders them must keep the younger-brother fact. Recorded in `FLAGS.md` §Z3.

### 38.6 Corrections to this PR's own figures (§4.3) — none touches a line of the file

Six subsidiary figures are wrong. Every headline figure — 50 / 70, 2.092×, 7,074 bytes, all 21 bank
movements, 367 rows, widest 23, 17 at 23, none at 24, `{FFFE}` +6 on the five named lines, `{FCC0}`
untouched — is **correct as stated** and was re-derived at review.

| # | Claim | Measured |
|---|---|---|
| 1 | `兵舎` "2 further script instances … 3 in total, where §9 says 4" | **4 in `script_dump.txt`, 1 of them this unit's own → 3 further, 4 in total. §9's "4 script" is RIGHT and this correction to it is wrong.** The PR's 3 is the *unique-line* count, not the dump-instance count §9 uses |
| 2 | `ワイン` "35 further script-dump instances" | **41 further** (44 total − 3 own), 18 unique lines. §9's own "44 script-dump instances" is right |
| 3 | `リムローズ` "9 further script-dump instances" | **10 further** (14 − 4 own). Banks [18, 20, 40, 41] and 2 battle in chunk 38 are exact |
| 4 | `上官` "used unchanged 3× here" | **2×.** Unique 431 carries 上官 three times; two render `ｓｕｐｅｒｉｏｒ　ｏｆｆｉｃｅｒ`, and the third (`貴官の上官となる`) renders the **bare** `ｙｏｕｒ　ｓｕｐｅｒｉｏｒ，　Ｆｉｒｓｔ`. Forced — the full form gives 28 columns — and it is §2.1 step 3 on a word the same message has already fixed twice, so **the rendering stands**; the departure was unflagged and is recorded here |
| 5 | `ｖｉｓｉｔｏｒ` "in chunks 11, 33, 35" | **11 and 33.** `chunk_035.txt` contains no `ｖｉｓｉｔ` in any form |
| 6 | `おい、` "12 battle chunks" | **11** (0, 8, 16, 20, 23, 27, 31, 32, 37, 38, 43; 14 instances). Banks [5, 41] correct, **not bank 2**, so §25.3's test still passes. `おいおい` "twice more (banks 29, 41)" is exact |

⚠️ **A seventh correction, to Flag 7 rather than to a figure: the unit DOES contain one §2.1 step-6
reorder, at unique 422.** The PR states it "contains no §2.1 step-6 reorder at all". The source is
`最近、[地殻の変動が激しいのか][あちこちで妙な噂を　聞くぜ]。` — conjecture first, main clause
second, one sentence; the English is `Ｉ　ｈｅａｒ　ｏｄｄ　ｒｕｍｏｕｒｓ　ａｌｌ` /
`ｏｖｅｒ　ｌａｔｅｌｙ．　Ｍａｙｂｅ　ｔｈｅ` / `ｅａｒｔｈ　ｉｓ　ｓｈｉｆｔｉｎｇ　ｈａｒｄ．` — main clause
first, conjecture second, two sentences. **The rendering stands**: nothing is added or dropped, the
page keeps its four rows and its `{FCC0}` where the source has it, and fronting a Japanese
parenthetical `〜のか` is close to forced in English. The flag was owed and is recorded here.

**Flag 7's other content is verified and correct**: `ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ，　ｎｙｏｒｏ．` measures
**22**, and unique 444 / 454 / 465 all follow the source's own clause order. Apart from 422 the unit
is clean of step-6 reorders, and **the five §2.1 step 3 / step 5 departures the PR does list are all
genuine and all flagged**.

### 38.7 What the review confirmed rather than corrected

- **`{FFEC}` inserts.** The PR's correction to its own dispatch is right: `rowcheck.py` defines
  `SCRIPT_NAME = '{FFEC}{=00}{=00}'` with `NAME_COST = 7` and substitutes it in `_script_cols`,
  and `assemble.py`'s `validate_body` does the same — the tool prints it in its own banner. **The
  player-name insert IS counted, at 7 columns**, and all five gate-visible rows passed the real
  column gate. The **insert+8 bound** on the three price-confirm lines is verified: `　Ｊｅｗｅｌｓ，`
  is 8 against `ジュエルに`'s 5, and `，` is 1 against 0 — byte-for-byte the overhead §34.9 records
  `batch_006` L60 already shipping, and **no `{FFFE}` was spent on those rows**, as §V1 requires.
- **The identity map and the fourth skeleton copy** (§9's dispatch was wrong, the PR right): 421–426
  is the tail of a rough human recruiter's copy whose head at unique **416–420 is untranslated**.
  ⚠️ And **unique 417 is one of the nine menu lines this unit binds**, so that head inherits both
  the menu strings *and* the register contrast — `Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ` / `ｔｉｍｅ！`
  against `…ｔｉｍｅ，　ｎｙｏｒｏ．`, with `Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ` in both.
- **All nine within-batch duplicate groups byte-identical, 0 divergences**, re-verified mechanically.
- **`そういえば、` → `Ｃｏｍｅ　ｔｏ　ｔｈｉｎｋ　ｏｆ　ｉｔ，` is byte-identical to shipped
  `chunk_002.txt` L12** — the one live cross-store form, checked positionally.
- **`ノロ` count == `ｎｙｏｒｏ` count on all 50 lines**; ellipsis dot runs match the source
  everywhere (the source's ellipsis is `・・・`, U+30FB ×3, and the two four-dot runs are `・・・。`
  and `。・・・`); **19 source segments open with the cursor gutter and 0 lost it**, the three EN-only
  leading `　` being §34.9's recorded price-insert word-space.
- **§29.5's stale "25"**: §1 and §2 were already corrected in place at PR #18's review (§36.4), which
  states in terms that PR #20 "now inherits a correct §2 … nothing is left for its reviewer to
  patch". **Nothing was double-patched.** §29.5's own body still reads "would be 25 … still will not
  share a row"; it is a historical ruling record and is left as written, with §36.4 and this section
  as its correction. Re-measured a fourth time: `Ｆｉｒｓｔ`(5) + 1 + `Ｌｉｅｕｔｅｎａｎｔ`(10) + 1 +
  `Ａｎｓｅｌｍｏ`(7) = **24**, at the hard limit and over the ≤23 preference, so the two-row split in
  unique 431 is right.
- **§29.4's `Ａｇｒｅｅｄ．` reserve is now SPENT** — `tl/battle/chunk_019.txt` L25 ships
  `・・・わかった。` → `．．．Ａｇｒｅｅｄ．`, which is exactly what §29.4 prescribed for chunk 19.
  Not a violation and nothing here relies on it, but **the わかる family has no reserve left**, and
  this unit correctly does not need one: it renders `わかった。` → `Ｒｉｇｈｔ．` (§6, source's own
  stop) and contains **no `了解`** — 了解 is script bank 5 only, battle chunks 3, 17, 19.

### 38.8 Register — verified from the tag stream, not assumed

| Who | Register |
|---|---|
| Lord Helfer (unique 431, portrait `{=00}{=07}`) | §11.6 unchanged — grandiose and archaic, **no contraction anywhere**: `Ｗｅｌｌ　ｍｅｔ．`, `Ｆｏｒｇｅｔ　ｎｏｔ．`, `ｌｅｔ　ｕｓ　ｔａｌｋ　ａ　ｌｉｔｔｌｅ`. Identified from the portrait stream and confirmed by Anselmo addressing him `ヘルファー様` two segments later |
| Anselmo (unique 431 `{=00}{=08}`, 437) | §14.6 / §15.3's blustering Imperial officer, **no contractions** — `Ｔｈａｔ　ｉｓ　ａｌｌ．`, `ｔｈｅｙ　ｃａｎｎｏｔ　ｊｏｉｎ　ｂａｔｔｌｅ`, `Ｉ　ｐｒａｙ　ｙｏｕ　ｆｉｇｈｔ　ｗｅｌｌ．` |
| Leon (unique 427) | Formal and **uncontracted** — `Ｆｏｒｇｉｖｅ　ｍｙ　ｌａｔｅｎｅｓｓ．`, `Ｉ　ａｍ　Ｌｅｏｎ`, `ｌｅｔ　ｕｓ　ｍｅｅｔ　ａｇａｉｎ．` §1's `Ｌｅｏｎ` unchanged |
| The rough human recruiter (421–426) | `だぜ` / `かい` carried by contractions and by `ｙｏｕ　ｋｎｏｗ！` / `ａｒｅｎ’ｔ　ｔｈｅｙ！`. Held apart from his three hobbit twins **by register and the missing `ノロ` alone**, with the shared beats deliberately parallel |
| The three hobbit recruiters (438–469) and the Hobbit Village chief (430) | §19.3 / §21.4's hobbits unchanged — warm and plain, light contractions (`Ｄｏｎ’ｔ　ｌｉｋｅ　ｉｔ`, `ｙｏｕ　ｗｏｎ’ｔ　ｅａｔ`), the `，　ｎｙｏｒｏ．` tic on every sentence in §18.1's **spaced** form, with the source's own stop each time (`，　ｎｙｏｒｏ？`, `，　ｎｙｏｒｏ！`, `，　ｎｙｏｒｏ！！`, `，　ｎｙｏｒｏ，`) |
| Unique 428's speaker (female, `よ` / `の` / `わ`) | §14.6's Cavia column — **no contractions** (`Ｔｈａｔ　ｗｉｌｌ　ｎｏｔ　ｄｏ．`, `Ｉ　ａｍ　ｇｏｉｎｇ`, `Ｉ　ｗｉｌｌ　ｎｏｔ　ｒｅｔｕｒｎ`). **Nothing names her, so no glossary row is proposed** — §23.5's and §31.1's practice, correctly followed |
| Unique 430's female party member | A **different** woman from 428's and correctly written so: light contractions (`ｃａｎ’ｔ`, `Ｔｈａｔ’ｓ`, `ｗｅ’ｖｅ　ｇｏｔ`). `私の生まれた村があるの` places her birth village in Eaton, which §9's own seed note anticipates. Unnamed, so no row |
| The superior officer of unique 430's opening | `貴官` and `おった` carried in register, **no contractions** — `ｙｏｕ　ｈａｖｅ　ａ　ｖｉｓｉｔｏｒ．`, `Ｈｅ　ｈａｓ　ｂｅｅｎ　ｓｈｏｗｎ　ｔｏ　ｔｈｅ　ｂａｒｒａｃｋｓ，　Ｉ　ｅｘｐｅｃｔ．` §2's politeness rule |

⚠️ **Two source oddities recorded so they are not rediscovered as defects.** Unique 449's
`受けたって聞いたてたから` is a **suspected source typo** for `聞いてた` (one kana transposed); the
sense is unambiguous and it renders as *I heard*. Unique 430's `そ、村長さん、` stutters a `そ` that
does **not** prefix the following word — a bare hesitation — so §24.3's pattern (repeat the
following word's first letter) gives `Ｃ，`.

---

## 39. Added by chunk 024 (PR #24, merged 2026-09-09)

Chapter 24, six scenes: the Imperial officer's ship comes down after someone tampers with it;
Aries finds the kill unfinished and hides; Fernando is run down and dies half-naming the patron who
betrayed him; Aries kills him with Creus's magic; Aries at the grave; Helfer and Prince Hoag send
the squad to Caffi Port because the King is dead and Prince Torif has claimed the throne; and the
reveal — Aries is Bishop Creus's grandchild, and a man raised as a girl.

**5,913 / 8,192, 2,279 slack** — 1,210 JP → 2,478 EN readable characters, **2.0479×** against the
**2.9913×** ceiling, 68.5 % of the English budget spent. 157 text rows (source 155), widest **23**,
twelve at 23, **none at 24**, no page over 4 text rows. `{FFFE}` 132 → 134 on two lines; `{FCC0}`
14 → 14, **none added**; the non-`{FFFE}` tag stream byte-identical on all 20 lines. Every figure
in the PR body was re-measured at review and is **exact**, except the labelling errors at §39.3.

### 39.1 People, places and words first rendered here — four promotions out of §9

| Japanese | English | Note |
|---|---|---|
| ホアグ王子 / ホアグ | `Ｐｒｉｎｃｅ　Ｈｏａｇ` / `Ｈｏａｇ` | **Promoted from §9's wave-2 seed, used exactly as seeded.** ~~13 / 4 columns~~ **11 / 4 columns** (corrected in place 2026-09-09, §4.3, PR #23 review; `len('Ｐｒｉｎｃｅ　Ｈｏａｇ')` = 11. ⚠️ **The phrase had THREE different figures in this file — §9's 10, this row's 13 and the true 11** — measured twice; both wrong rows are now patched. No rendering changes). Carline's elder prince, Cavia's brother. **The first rendering in the project** — `Ｈｏａｇ` occurred nowhere in `tl/` or `pending/` before this unit. 6 battle + 16 script |
| カッフィ / カッフィの港 | `Ｃａｆｆｉ` / `Ｃａｆｆｉ　Ｐｏｒｔ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** 5 / 11 columns. **A PORT, not a person.** `Ｘの<feature>` → capitalised compound on §38.1's `チェコットの丘` → `Ｃｈｅｋｏｔ　Ｈｉｌｌ` and `イートンの森` → `Ｅａｔｏｎ　Ｆｏｒｅｓｔ`, **not** the possessive of §2's `バウワーの砦`. Both `カッフィの港` render `Ｃａｆｆｉ　Ｐｏｒｔ` byte-identically. 3 battle (all here) + 3 script |
| ゴードン将軍 | `Ｇｅｎｅｒａｌ　Ｇｏｒｄｏｎ` | **Promoted from §9's wave-6 seed.** 16 columns; `Ｇｏｒｄｏｎ` alone 6. `ファリーナのゴードン将軍` → `Ｇｅｎｅｒａｌ　Ｇｏｒｄｏｎ` / `ｏｆ　Ｆａｒｉｎａ．` 将軍 → `Ｇｅｎｅｒａｌ` is §26.2's, unchanged. A hapax: 1 battle + 0 script |
| ホアグ王子派 / トリフ王子派 | `ｔｈｅ　Ｈｏａｇ　ｆａｃｔｉｏｎ` / `ｔｈｅ　Ｔｏｒｉｆ　ｆａｃｔｉｏｎ` | **Promoted from §9's wave-6 seed, on the seed's own named short alternative — the long form does not fit; see §39.3.** **16 / 17 columns** as phrases. 派 → `ｆａｃｔｉｏｎ` matches shipped `batch_005.tsv` L32's `フェルナンド派の連中` → `Ｆｅｒｎａｎｄｏ’ｓ　ｆａｃｔｉｏｎ` (§26.4). Both shortened together, as the seed directs. Both princes are titled `Ｐｒｉｎｃｅ` three times elsewhere in the same message, so the title is not lost from the scene — §2.1 step 3's redundant-gloss case, not a dropped fact. 1 battle each, 0 script |
| おじいさん / じいさん | `Ｇｒａｎｄｆａｔｈｅｒ` / `ｍｙ　ｇｒａｎｄｆａｔｈｅｒ` | 12 columns. **Vocative capitalised, referential lowercase** — the split §25.4 already draws for `Ｆａｔｈｅｒ`. Free across `tl/` and `pending/`, verified at review |
| 孫 | `ｇｒａｎｄｃｈｉｌｄ` | 12 columns, **deliberately gender-neutral** — the L15 exchange turns on it; see §39.2. Free across `tl/` and `pending/`, verified at review |
| 恨み | `ｇｒｕｄｇｅ` | 6 columns. **Not a new form** — `pending/chunk_043.txt` 13.3 ships `我が部下たちの恨み・・・` → `ｍｙ　ｓｏｌｄｉｅｒｓ’　ｇｒｕｄｇｅ．．．`. ⚠️ **CROSS-UNIT with chunk 25 (PR #23), which also ships `ｇｒｕｄｇｅ` — verified at this review. ~~The row stays LIVE until chunk 25 merges~~ ✅ **DISCHARGED and STRUCK 2026-09-09 at chunk 25's merge (PR #23)** — chunk 24 merged first and deliberately left it live, chunk 25 merged **second** and strikes it, which is the whole of what the `ルート` precedent (§29.1 / §30.1) prescribes. Both units ship `ｇｒｕｄｇｅ`, verified positionally against the merged tree rather than assumed. 3 battle (24, 25, 43) + 0 script |
| 王位 (継承) | `ｔｈｅ　ｔｈｒｏｎｅ` | 10 columns. `王位継承を巡って…名乗りを挙げられた` → `ｈａｓ　ｐｕｔ` / `ｈｉｍｓｅｌｆ　ｆｏｒｗａｒｄ　ｔｏ` / `ｓｕｃｃｅｅｄ　ｔｏ　ｔｈｅ　ｔｈｒｏｎｅ．` — keeps **both** 王位 (*throne*) and 継承 (*succeed*). ⚠️ **CROSS-UNIT with chunk 25, which ships `ｔｈｅ　ｔｈｒｏｎｅ` for bare `王位` — verified at this review. ~~The row stays LIVE until chunk 25 merges.~~ ✅ **DISCHARGED and STRUCK 2026-09-09 at chunk 25's merge (PR #23)** — chunk 25 ships bare `王位` → `ｏｎ　ｔｈｅ　ｔｈｒｏｎｅ　ｗｈａｔｅｖｅｒ．` and chunk 24 the compound `王位継承` → `ｓｕｃｃｅｅｄ　ｔｏ　ｔｈｅ　ｔｈｒｏｎｅ．`; both verified against the merged tree. ⚠️ **This pair is the standing counter-example to a maximal-kanji-run cross-unit sweep** — `王位継承` never matches `王位`, which is why neither unit's dispatch list carried it (`FLAGS.md` §Y2). 2 battle (24, 25) + 0 script. `ｓｕｃｃｅｅｄ` also renders 成功した in `batch_007.tsv` L67; §25.3's test is met — 成功 is bank 3 only, 王位継承 is battle chunk 24 only |
| 計画する (of a killing) | `ｐｌｏｔ` | `殺害を計画した３人のうちの１人` → `ｏｎｅ` / `ｏｆ　ｔｈｅ　ｔｈｒｅｅ　ｗｈｏ` / `ｐｌｏｔｔｅｄ　ｍｙ` / `ｇｒａｎｄｆａｔｈｅｒ’ｓ　ｍｕｒｄｅｒ．` **`ｐｌａｎ` is not free** — §19.2 spends it on 作戦 and §31.5 turns on that. ⚠️ **`ｐｌｏｔ` renders THREE source words, not two** (corrected at review, §39.3): 計画 here, 企てた in `batch_007.tsv` L50, and a third already shipped as the noun in `batch_005.tsv` L36 (`Ｈｅｌｆｅｒ’ｓ　ｐｌｏｔ．`). §25.3's test is still met — 計画 is script banks [5, 41] + battle chunk 24, 企て is banks [1, 3, 23]; no shared bank, no shared chunk |
| 容赦しない / 容赦せん | `ｓｈｏｗ　ｎｏ　ｍｅｒｃｙ` / `ｎｏ　ｍｅｒｃｙ` | 3 instances here across two speakers, one echoing the other (`容赦しない・・・？` / `それは、こっちのセリフだ。`), so one word throughout. `ｍｅｒｃｙ` free across `tl/` and `pending/`, verified at review |
| 話が違う | `Ｔｈｉｓ　ｉｓ　ｎｏｔ` / `ｏｕｒ　ｂａｒｇａｉｎ，` | `ｂａｒｇａｉｎ` free, verified at review. A hapax — 1 battle, 0 script |
| 返り討ちにあう | `ａｎｄ　ｈｅ’ｌｌ　ｋｉｌｌ　ｙｏｕ．` | The counter-kill: the target kills the attacker instead. Rendered as a clause on §15.2's 黒幕 precedent. Hapax |
| 名乗りを挙げる | `ｐｕｔ　…　ｆｏｒｗａｒｄ` | The claimant sense, distinct from 名乗る *to give one's name*. Hapax |
| 素性 | `ｍｙ　ｂｉｒｔｈ` | Hapax. ⚠️ **`ｂｉｒｔｈ` is NOT free** (corrected at review, §39.3): `batch_007.tsv` L31 ships `ｍｙ　ｂｉｒｔｈ　ｖｉｌｌａｇｅ`. Different sense — birthplace against parentage — no co-occurrence, and both are the plain English; the rendering stands |
| とどめを刺す | `ｄｅａｌ　ｔｈｅ　ｆｉｎａｌ　ｂｌｏｗ` | 2 instances here (`しとめそこなった` L1, `とどめが刺せなかった` L12), rendered so they echo. ⚠️ **`ｂｌｏｗ` is NOT free** (corrected at review, §39.3): `batch_001.tsv` L10 ships §4's fixed `一撃必殺` → `ｋｉｌｌｉｎｇ　ｗｉｔｈ　ｏｎｅ　ｂｌｏｗ．` A stat-table phrase against battle dialogue; §25.3's test is met and the rendering stands |
| 穀潰し | `ｆｒｅｅｌｏａｄｅｒｓ` | **Not a new form — recording a reuse.** §2 fixes it and `batch_002.tsv` L9 already ships `Ｙｏｕ　ｆｒｅｅｌｏａｄｅｒｓ．`; this unit matches the word. 1 battle (the only one in the dump) + 5 script |

### 39.2 The L15 gender exchange — `孫` is gender-neutral so that the reveal can land

`孫` → **`ｇｒａｎｄｃｈｉｌｄ`**, never *grandson*. If the first mention gendered him, the question two
pages later would be nonsense. The four beats, all explicit, none smoothed:

- `１０年前に一族を皆殺しにされた、ファリーナの司教、クレウスの孫だ。` → `Ｔｅｎ　ｙｅａｒｓ　ａｇｏ　ａｌｌ　ｔｈｅ` / `ｋｉｎ　ｏｆ　Ｆａｒｉｎａ’ｓ　Ｂｉｓｈｏｐ` / `Ｃｒｅｕｓ　ｗｅｒｅ　ｓｌａｕｇｈｔｅｒｅｄ．` / `Ｉ　ａｍ　ｈｉｓ　ｇｒａｎｄｃｈｉｌｄ．`
- `えっ、でも、クレウス司教の孫って男だったんじゃ・・・` → `Ｅｈ，　ｂｕｔ` / `ｗａｓ　Ｂｉｓｈｏｐ　Ｃｒｅｕｓ’` / `ｇｒａｎｄｃｈｉｌｄ　ｎｏｔ　ａ　ｂｏｙ．．．`
- `・・・・・そうだ、僕は男だ。` → `．．．．．` / `Ｙｅｓ，　Ｉ　ａｍ　ａ　ｍａｎ．`
- `僕は素性を隠すため、女として育てられた。` → `ｔｏ　ｈｉｄｅ　ｍｙ　ｂｉｒｔｈ，` / `Ｉ　ｗａｓ　ｒａｉｓｅｄ　ａｓ　ａ　ｇｉｒｌ．`

`ａ　ｂｏｙ` and `ａ　ｇｉｒｌ` are paired deliberately, on the axis the Japanese uses. `そうだ、` takes
`Ｙｅｓ，` per **§34.2, whose confirmation column cites this very line**. Aries is `彼女` / `ｓｈｅ`
before the reveal (L9) and `僕` / male after it, and the English follows the source both times. The
massacre is the one `tl/battle/chunk_021.txt` L10 already ships, and the vocabulary matches it:
`一族` → `ｋｉｎ`, `皆殺し` → `ｓｌａｕｇｈｔｅｒｅｄ` (§36.1), `１０年前` → `ｔｅｎ　ｙｅａｒｓ　ａｇｏ` (§36.6).

⚠️ **This is クレウス / Aries and is DISTINCT from `FLAGS.md` §Y6, which concerns クレス / Cress.
§Y6 is untouched and stays open.**

### 39.3 Corrections to this PR's own figures (§4.3) — none touches a line of the file

1. **The faction figures are ROW widths, labelled as phrase widths.** Flag 4 and the additions table
   give "`ｔｈｅ　Ｈｏａｇ　ｆａｃｔｉｏｎ` (20) / `ｔｈｅ　Ｔｏｒｉｆ　ｆａｃｔｉｏｎ` (18)". Measured with
   `len()`, the **phrases** are **16 / 17**; the **shipped rows** are `ｔｈｅ　Ｈｏａｇ　ｆａｃｔｉｏｎ　ａｎｄ`
   (20) and `ｔｈｅ　Ｔｏｒｉｆ　ｆａｃｔｉｏｎ．` (18). The numbers are right, the label is wrong, and
   §39.1 records **16 / 17**. Flag 4's page figures **23 / 22 / 20 / 18** are exact, and the seed's
   long form genuinely does not fit: 4 × 23 = 92 columns available against 97 for the full sentence.
2. **Three "verified free" claims are false.** `ｂｌｏｗ` (`batch_001` L10, plus `chunk_006` and
   `pending/chunk_043` as the verb), `ｂｉｒｔｈ` (`batch_007` L31), and — unclaimed, but missed by the
   `ｐｌｏｔ` accounting — `batch_005` L36's `Ｈｅｌｆｅｒ’ｓ　ｐｌｏｔ．` **All three survive §25.3's
   co-occurrence test, so no line changes**, but a "free" claim is a measurement and these were not
   measured. This is the §Y3 failure mode in its other direction: not stale, simply unchecked.
3. **`ｍｙ　ａｐｏｌｏｇｉｅｓ．` ships lowercase.** The additions table capitalises it; the file has
   `{FC00}{=0000}，{FFFE}ｍｙ　ａｐｏｌｏｇｉｅｓ．`, correctly, because it continues the sentence after
   the vocative. 14 columns either way. Held apart from 申し訳ない → `ｆｏｒｇｉｖｅ　ｍｅ．` (§33.2),
   あいにく / ごめんね、 → `Ｓｏｒｒｙ，` (§28.3), ごめんね。 → `Ｉ’ｍ　ｓｏｒｒｙ．` (§30.3) and
   すみません。 → `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ　ｙｏｕ．` (§27.1). §33.2 named it free and reserved it
   in terms. 2 battle (24, 39) + 5 script.
4. **`うむ。` → `Ｈｍ．`: the census misses chunk 4.** The flag's list ("む chunk 12, ん？ chunks 2 and
   20, ふーむ script bank 31, うーん chunk 8, うむ chunks 23 and 24") omits `chunk_004` 4.6, which
   already ships `Ｈｍ．．．？` for `ん・・・？`. **§25.3's test still passes** — different strings,
   chunks 4 and 24 — so the fifth kana spelling on §6's む / ん → `Ｈｍ` stands and binds chunk 23.
   3 columns.
5. **"No step-6 reorder within a page" is slightly overstated.** L5's `私は、こんなところでは` /
   `まだ　死なんぞ・・・。` ships as `Ｉ　ｗｉｌｌ　ｎｏｔ　ｄｉｅ　ｙｅｔ，` / `ｎｏｔ　ｉｎ　ｓｕｃｈ　ａ　ｐｌａｃｅ．．．．`,
   which swaps the two rows relative to the source. It is the natural English — fronting the
   locative is not grammatical here — so it falls under §2's "constructions that are ungrammatical
   if traced word-for-word" rather than §2.1 step 6, and **nothing is added or dropped**. Recorded
   so the next reader does not find it unlabelled.
6. **`・・・あとの２人は？` → `．．．Ａｎｄ　ｔｈｅ　ｏｔｈｅｒ　ｔｗｏ？` adds a discourse connective.**
   The bare form is 17 columns and would fit. The `は` genuinely carries *as for the remaining two*
   and English idiom wants the connective on a follow-up question, so it stands — recorded, not
   re-cut, on §32.8's row-level principle.

### 39.4 RULING — `しまった` splits on POSITION, and the shipped form is lowercase `ｄａｍｎ　ｉｔ`

The PR's Flag 12 asked for this ruling and its census is wrong in three ways. Measured over
`battle_dump.txt`, `script_unique.txt`, all of `tl/` and all of `pending/` at this review:

| Where | Japanese | English |
|---|---|---|
| `chunk_000` 16.1 | `しまった、` line-initial | `Ｏｈ　ｎｏ，` |
| `pending/chunk_005` 0.8 | `しまった。` line-initial | `Ｏｈ　ｎｏ．` |
| `chunk_024` 1.1 | `しまった・・・` line-initial | `Ｏｈ　ｎｏ．．．` |
| `chunk_008` 13.1 | `げッ！？・・・しまった。` after a grunt | `Ｄａｍｎ　ｉｔ．` |
| `chunk_014` 7.1 | `グッ、しまった・・・` after a grunt | `ｄａｍｎ　ｉｔ．．．` |
| `chunk_020` 45.1 | `ぬおっ、しまった！` after a grunt | `ｄａｍｎ　ｉｔ！` |

**RULING, on §5's mechanism — the word is fixed, the punctuation follows the source:**
line-initial `しまった` → **`Ｏｈ　ｎｏ`**; `しまった` following a grunt → **`ｄａｍｎ　ｉｔ`**,
**lowercase**, capitalised only where it opens a sentence (which is why `chunk_008` has `Ｄａｍｎ`,
after a sentence-closing `．．．`). Flag 12 writes the second form capitalised and cites page
indices 13.0 / 7.0 / 45.0; the true indices are **13.1 / 7.1 / 45.1**.

⚠️ **The reach is not "13 battle chunks + 8 script".** Of 13 battle substring hits, **five are the
verbal auxiliary `〜てしまった`** (chunk 16 L16, 19, 30, 34, 41), and of 7 script hits, **six** are.
The interjection reaches **8 battle chunks — 0, 5, 8, 14, 16, 20, 24, 37 — and 1 script line**
(`{FB01}しまった！{FFFE}４号機・・・ノトスを`). Six are rendered; this ruling binds the two that are
not, **chunk 16 L2 (`しまった・・・敵の`) and chunk 37 L0 (`しまった・・・！？`)** — both line-initial,
both `Ｏｈ　ｎｏ．．．`. `pending/chunk_005` 3.0's `Ｄａｍｎ　ｉｔ．` renders **`何てこった。`** and is
not a member of this family at all.

### 39.5 `それに` between two vocatives is a list conjunction, not §29.3's connective

`ヘルファー司令官、それに・・・ホアグ王子！！` → `Ｃｏｍｍａｎｄｅｒ　Ｈｅｌｆｅｒ，` / `ａｎｄ．．．` /
`Ｐｒｉｎｃｅ　Ｈｏａｇ！！`. §29.3 fixes **`それに、`** — with a comma, sentence-initial, additive —
as `Ｂｅｓｉｄｅｓ，`. This is a **different source string** (`それに・・・`) doing a **different job**:
it joins two vocatives inside one exclamation, where `Ｂｅｓｉｄｅｓ，` would be flatly wrong. The
unit rendered it correctly but did not record it; written down here so it is not re-litigated.
§29.3 is unaffected, and so are the four adversatives it holds itself apart from.

### 39.6 Recorded, not re-cut — checked and not defects

- **The honorific on a name insert drops; a rank does not.** `{FC00}{=0000}君、` → `{FC00}{=0000}，`
  ×2 follows shipped `chunk_020` 47.5 (`{FC00}{=0000}さん、` → `{FC00}{=0000}，`), while `chunk_014`
  2.13 keeps and preposes the rank (`{FC00}{=0000}隊長！` → `Ｃａｐｔａｉｎ　{FC00}{=0000}！`).
  English has no `-kun`; it has *Captain*.
- **`ところが` → `Ｂｕｔ　ｎｏｗ，`** — 8 columns, a hapax (1 battle, 0 script), so it binds nothing.
  Held apart from でも → `Ｂｕｔ，`, それにしても → `Ｓｔｉｌｌ，` (§19.1), しかし → `Ｈｏｗｅｖｅｒ，`
  (§23.3, used on the very next page), それでも → `Ｅｖｅｎ　ｓｏ，` (§25.2), それに、 → `Ｂｅｓｉｄｅｓ，`
  (§29.3), なのに → `Ａｎｄ　ｙｅｔ，`. Free, verified at review.
- **`Ｎ，` opens two consecutive Fernando messages** (`ま、まだだ！` → `Ｎ，　Ｎｏｔ　ｙｅｔ！`;
  `こ、ここまでか・・・` → `Ｎ，　Ｎｏ　ｆｕｒｔｈｅｒ，　ｔｈｅｎ．．．`) because §24.3's stutter rule repeats
  the **following word's** first letter, mechanically. Not a flattening.
- **`ええい、` → `Ｅｎｏｕｇｈ！`** is the third instance §31.3 predicted, byte-identical to `chunk_007`
  and `chunk_018`; the `！` is part of the fixed form and is not re-derived from the source's `、`.
- **`ここまでか` → `Ｎｏ　ｆｕｒｔｈｅｒ`** keeps ここまで's own *this far* image and is held apart from
  the three shipped "it is over" forms — 万事休すか → `Ｔｈｉｓ　ｉｓ　ｔｈｅ　ｅｎｄ` (`chunk_000`),
  もう　おしまいよ → `ｉｔ　ｅｎｄｓ　ｈｅｒｅ` (`chunk_011`), そこまでだ → `ｉｔ　ｅｎｄｓ　ｈｅｒｅ`
  (`pending/chunk_043`).
- **`まさか…とはな`** is the exclamative §33.6 puts outside `Ｓｕｒｅｌｙ`'s scope, and takes
  `ｔｏ　ｔｈｉｎｋ`. **§29.4's `Ａｇｒｅｅｄ．` reserve is correctly not engaged** — 了解 0, わかった 1,
  so §6's `Ｒｉｇｈｔ` governs. **`あら` count is 0**, so §32.4 is not engaged.
- **`ｄｅｓｃｅｎｄａｎｔ` is 10 columns**, `len()`-measured. PR #23's Flag 15 says 11; it is a
  hand-count one high, the seed was right, and the correction is **not** propagated into §9.

### 39.7 Register — verified from the tag stream, not assumed

Portrait **08** is **Fernando**: he rages on the ship (`{FC51}`), is hunted (`{FC50}`) and dies, and
Aries names him two messages later (`フェルナンドは死んだよ`) — same id, opposite channel byte, the
§23.5 / §28.7 / §30.7 pattern. Portrait **03** is **Aries**. Portrait **06** is **Helfer**, named by
the next speaker; portrait **04** is **Prince Hoag**, named in the same breath. Per `FLAGS.md` §W5
these readings are derived inside chunk 24 and are **not** carried to any other chunk.

Fernando: §20.5 / §24.6, **zero contractions** across all four messages. Aries: §32.9 / §33.7,
**zero contractions**, including through the reveal — the third shipped unit to hold that row.
Helfer: §11.6, grandiose and uncontracted. Prince Hoag: formal, uncontracted. The 9th Army: §7,
contractions throughout (`Ｉ　ｗｏｎ’ｔ`, `ｈｅ’ｌｌ`, `Ｔｈａｔ’ｓ`) — the contrast that makes the
officers' flatness read as rank. **`残念だけど` → `ａｆｒａｉｄ` is the fixed WORD; the contraction
follows the speaker** — `chunk_011` 6.1 and `chunk_020` 47.3 both contract, Aries does not, so this
unit's `Ｉ　ａｍ　ａｆｒａｉｄ` is right. §34.1's `残念です` → `ａ　ｓｈａｍｅ` is a different source string.

## 40. Added by chunk 026 (PR #22, merged 2026-09-09)

Chapter 26, the landing on the demon island: the party makes shore at the wrong-looking village and
finds it long dead; low-rank demons ambush them; a proud dark elf declares his blood and is killed;
the survivor **Annette**, Dolgan's daughter, recognises Prince Hoag and tells what happened to the
island; and the scene closes on **Seti** and **Yuiti** murdering the wounded **Treize** and setting
off to hunt the party.

**5,325 / 8,192, 2,867 slack** — 1,085 JP → 1,999 EN readable characters, **1.84×** against a
**3.357×** ceiling. 139 text runs, widest **23**, **none at 24**, no page over 4 text rows.
`{FFFE}` +3 on two lines (body L11 1→2, L14 58→60); `{FCC0}` unchanged, **none added**; the
non-`{FFFE}` tag stream byte-identical on all 18 lines. 18 / 18 ellipsis dot counts exact.
**Every measured figure in the PR body was re-measured at review and is exact** — all reach counts,
all bank lists, all column widths. Nothing was corrected at merge, the first unit this run for
which that is true.

### 40.1 People and words first rendered here — six promotions out of §9

| Japanese | English | Note |
|---|---|---|
| アネット | `Ａｎｎｅｔｔｅ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** **7 columns.** Dolgan's daughter; the survivor who guides the party to the mountain settlement. Reach re-measured at review: **5 battle (chunk 26 only) + 4 script (banks 10, 41)** — the seed is exact |
| ドルガン | `Ｄｏｌｇａｎ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** **6 columns.** Annette's father, alive among the survivors; never on screen here. **4 battle (chunks 26, 32) + 8 script (banks 10, 40, 41)** — seed exact. ⚠️ **Chunk 32 addresses him as `ドルガンさん`**, so §21.2's `〜さん`-on-a-personal-name rule applies there: bare `Ｄｏｌｇａｎ` |
| セティ | `Ｓｅｔｉ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** **4 columns. FEMALE — see §40.2.** The matched pair with `Ｙｕｉｔｉ` is preserved (`‑ｉ` / `‑ｉ`), as §9 directs. **6 battle (chunks 26, 27, 28, 29, 38) + 0 script** — seed exact |
| ユイティ | `Ｙｕｉｔｉ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** **5 columns. MALE — see §40.2.** **7 battle (chunks 26, 27, 29, 32, 38) + 0 script** — seed exact |
| トレーズ | `Ｔｒｅｉｚｅ` | **Promoted from §9's wave-6 seed, used exactly as seeded.** **6 columns.** The standard katakana for French *Treize*, so the European reading. **6 battle (chunks 26, 27, 28, 29) + 0 script** — seed exact. **He is also the dark elf of L10/L11 — confirmed at this review, §40.5** |
| 魔族 | `ｄｅｍｏｎ` / `ｄｅｍｏｎｓ` — **lowercase** | **Used exactly as §9 seeds it**, 4× in this chunk. Lowercase by the §17.1 species test, the exact case of `ホビット` → hobbit. **Not** `Ｄｅｍｏｎ`. **5 / 6 columns.** Reach re-measured: **13 battle (chunks 26, 27, 28, 29, 30, 32) + 21 script (banks 4, 10, 21, 30, 31, 40, 41)** — seed exact. Kept distinct from 魔物 → `ｍｏｎｓｔｅｒ` (chunk 26 carries no 魔物, verified). ⚠️ **The §9 row STAYS LIVE — see §40.7** |
| キャハハハハ | `Ｋｙａｈａｈａｈａｈａ` + the source's own punctuation | Seti's laugh as she kills Treize. **11 columns**, free across `tl/` and `pending/`. Kana beats tracked per §11.5's `フハハハ` → `Ｆｕｈａｈａｈａ`: キャ+ハ×4 → `Ｋｙａ`+`ｈａ`×4. ⚠️ **Binds chunk 32**, whose `キャハハハハハハ` (six ハ) becomes `Ｋｙａｈａｈａｈａｈａｈａｈａ` (15 columns) under the same rule. 2 battle (26, 32), 0 script |
| オッケー | `Ｏｋａｙ` + the source's own punctuation | Seti's assent. **4 columns**, free. Spelled out rather than `ＯＫ` on §3's `ＨＩＴ` → *hits* rule: full-width caps are Japanese emphasis on a loanword and English needs none. Held **distinct** from よし、/ 分かった → `Ｒｉｇｈｔ，` (§6, §24.3) and わかりました。 → `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` (§21.2). ⚠️ **Binds chunk 38** (`オッケー！` → `Ｏｋａｙ！`). 2 battle (26, 38), 0 script |
| 船長 (address) | `Ｃａｐｔａｉｎ，` | The ship's captain, addressed by a party member. `さん` on a **common noun** — §30.2's third pattern (`兵隊さん` → `ｓｏｌｄｉｅｒｓ`), so neither §21.2's name rule nor §2's comic `トカゲさん` → `Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ`. ⚠️ **Shares its English with §2's 隊長 → captain and §25.3's test is only HALF met** — re-measured at review: 船長 **1 battle [26] + 3 script banks [23, 28, 41]**; 隊長 **24 battle [1, 2, 3, 6, 7, 8, 13, 14, 16, 19, 22, 23] + 10 script banks [2, 10, 28, 32, 34, 41]**. Chunks disjoint, so **nothing shipped is affected**; **banks 28 and 41 hold both**. FLAGS §AB5 |
| 無様だな。 | `Ｈｏｗ　ｐａｔｈｅｔｉｃ．` | Yuiti over the dying Treize. **13 columns**, `ｐａｔｈｅｔｉｃ` verified free. Hapax: 1 battle, 0 script |
| ただものじゃない | `ａｒｅ　ｎｏ　ｏｒｄｉｎａｒｙ　ｆｏｅｓ` | Treize on the party. **20 columns.** Hapax: 1 battle, 0 script |
| 獲物 | `ｑｕａｒｒｙ` | Yuiti's last line. **6 columns**, free. Deliberately **not** `ｐｒｅｙ`, which `chunk_009.txt` L4 ships for `えじき` — two source words, two English forms, on the 伝令 / 連絡員 / 使いの者 pattern (§30.2, §33.1). Both are hapaxes, so §25.3 would have permitted the collapse; held apart anyway |
| うっ・・・ | `Ｕｇｈ．．．` | **6 columns.** Shares its English with §19.1's `ううっ`, and §25.3's test is **MET in both dimensions**, verified positionally at review: the raw `うっ・・・` count of 3 battle is **2 substring hits inside `ううっ・・・`** (chunks 1, 2) plus this one, and **all 6 script hits are likewise inside `ううっ`** (banks 18, 41), so bare `うっ・・・` is **chunk 26 only, 0 script**. Disjoint. The documented one-word/two-spellings collapse (§17.2, §38.3) |

**Reuses recorded, not new forms** — 集落 → `ｓｅｔｔｌｅｍｅｎｔ` (§11.2, also `chunk_002` ×2; first
use here for a *different* settlement), 伝令 → `ｍｅｓｓｅｎｇｅｒｓ` (§30.2, plural here), 仇をとる →
`ａｖｅｎｇｅ` (§30.5, also `pending/chunk_017` ×2), ダークエルフ → `ｄａｒｋ　ｅｌｆ` **lowercase**
(§17, shipped in `batch_003.tsv` L20), ホアグ王子 → `Ｐｒｉｎｃｅ　Ｈｏａｇ` (§39.1).

### 40.2 Register — verified from the tag stream, and Seti's and Yuiti's genders fixed here

Every attribution below is taken from the `{FCB0}` id **paired with the `{FC50}`/`{FC51}` channel
byte**, per PR #23's ruling that portraits are not speakers — never from the prose. Note the ids are
**scene-local**: id 0007 on `{FC50}` is the pidgin mook in L7's scene and **Seti** in L15's, which
is itself the proof, and matches Annette's `あれは魔族の中でも下級の者たち`.

| id · channel | Who | Register |
|---|---|---|
| 05 · FC50 | **Annette** | Polite, frightened, formal — `です`/`ます` throughout, **no contraction anywhere**: `Ｉｔ　ｉｓ　ｍｅ！`, `Ｔｈｅ　ｄｅｍｏｎｓ　ｄｉｄ　ｔｈｉｓ．`, `Ｉ　ｕｎｄｅｒｓｔａｎｄ．` §24.6 / §26.7's clergy column, on a civilian |
| 04 · FC51 | **Prince Hoag** | Warm and courteous, **no contractions** — `Ｓｏ　ｉｔ　ｉｓ　ｙｏｕ．`, `Ｅｈ？　Ｙｏｕ　ａｒｅ．．．` Uses `君` to Annette |
| 02 · FC50/51 | **the ship's captain** | Rough and casual, contracts — `Ｔｈａｔ’ｓ　ｏｄｄ．`, `Ｓｅｅｍｓ　ｌｉｋｅ　ｗｅ’ｒｅ`, `Ｓｏ　ｔｈｅｎ，`. `俺たち`, `〜だぜ` |
| 03 · FC50/51 | a female party member | Warm, contracts — `Ｗｅ　ｒｅａｌｌｙ　ｈａｖｅ` / `ｎｏ　ｌｕｃｋ，　ｄｏ　ｗｅ．`, `ｉｔ’ｓ　ａｌｌ　ｒｉｇｈｔ　ｎｏｗ．` |
| 07 · FC50 | **Seti — FEMALE** | Casually rough and gleefully cruel, contracts — `Ｄｏｎ’ｔ　ｔｅｌｌ　ｍｅ　ｙｏｕ`, `Ｒｅｓｔ　ｅａｓｙ．`, `Ｏｋａｙ．` Fixed by `あんた`, **`〜の？`**, **`〜わけ？`**, **`〜ね`** and `キャハハハハ` |
| 08 · FC50/51 | **Yuiti — MALE** | Laconic and blunt, **no contractions** — `Ｈｏｗ　ｐａｔｈｅｔｉｃ．`, `Ｎｏｗ　ｔｈｅｎ，　ｓｈａｌｌ　ｗｅ　ｇｏ．`, `Ｙｅａｈ．` Fixed by **`〜んだ`**, **`〜だな`**, **`行くか`**, **`〜がな`**, and Treize's vocative `ユイティ、気をつけろ` on that channel |
| 06 · FC51 | **Treize**, and the dark elf of L10/L11 (§40.5) | Haughty, archaic, contemptuous of humans, **no contractions even while begging** — `Ｗｅ　ａｒｅ　ｔｈｅｙ　ｉｎ　ｗｈｏｓｅ`, `Ｙｏｕ　ｌｏｗｌｙ　ｈｕｍａｎｓ，`, `Ｃａｒｅｌｅｓｓｎｅｓｓ　ｕｎｄｉｄ　ｍｅ．` |
| 07 · FC50 (L7's scene) | the low-rank demon | §5's broken-katakana register — dropped articles, dropped copula: `Ｈｕｍａｎｓ　ｗｅ　ｎｏｔ　ｆｏｒｇｉｖｅ！`, `Ｓｏ，　ｙｏｕ　ｏｕｒ　ｅｎｅｍｙ！` |

**The two demon registers are deliberately different and were confirmed not levelled at review.**
L7 is a low-rank mook in katakana pidgin; L10 is a high-born dark elf in formal archaic contempt
(`我々`, the attributive `誇り高き`, `〜者`, and the imperious `消え去るがいい` →
`ｙｏｕ　ｗｏｕｌｄ　ｄｏ　ｗｅｌｌ　ｔｏ　ｖａｎｉｓｈ`). **Chunks 27, 29, 32 and 38 inherit Seti's and
Yuiti's pronouns from this file.**

### 40.3 RULING — `大歓迎` is CONTEXT-SENSITIVE, not a fixed string. §38.2 is corrected; no line changes

PR #22's Flag 7 is **confirmed on both halves**, verified at review against the tree. §38.2 fixes
`大歓迎` → `Ｍｏｓｔ　ｗｅｌｃｏｍｅ` / `ｍｏｓｔ　ｗｅｌｃｏｍｅ　ｈｅｒｅ` (12 / 17 columns) and its own
reach note lists chunk 7 — but **`tl/battle/chunk_007.txt` body L3 (file line 5) already ships
`Ｓｕｃｈ　ａ　ｗａｒｍ　ｗｅｌｃｏｍｅ！`** (19 columns) and §38.2 did not notice. Reach re-measured:
**4 battle (chunks 7, 15, 26) + 6 script (banks 0, 3)**.

**The ruling.** `大歓迎` is ordinary vocabulary, not a coined term, and it takes the English its
clause needs. The binding precedent is this run's own `残念だけど` decision (§39.7): **CLAUDE.md §3
engages on the MESSAGE, not the phrase.** The three source messages are distinct
(`大歓迎してくれてるよ！` / `大歓迎されてるようだぜ！` / `そう言うことなら大歓迎だ！！`), so **gate 6 is
not engaged, chunk 7 is not re-cut, and chunk 26 is not re-cut.** The sense splits cleanly:

| Sense | Instances | Takes |
|---|---|---|
| **ironic** — enemies "welcoming" you with weapons | chunk 7 L3 (shipped `Ｓｕｃｈ　ａ　ｗａｒｍ　ｗｅｌｃｏｍｅ！`), chunk 26 L5 (shipped `ｍｏｓｔ　ｗｅｌｃｏｍｅ　ｈｅｒｅ！`) | a *warm / most welcome* phrasing that fits the row; **both shipped forms stand** |
| **sincere** — welcoming a person in | chunk 15, twice, **untranslated** | `Ｍｏｓｔ　ｗｅｌｃｏｍｅ` (12) |

**For chunk 15, whose dispatch this unblocks:** `そう言うことなら大歓迎だ！！` →
`Ｉｎ　ｔｈａｔ　ｃａｓｅ，` (13) / `ｙｏｕ’ｒｅ　ｍｏｓｔ　ｗｅｌｃｏｍｅ！！` (21). ⚠️ **Chunk 15's two
instances are ONE sentence: its dump L11 text is a strict SUFFIX of its L10 text** (a scene with two
entry points, measured at review), so the sentence **must be rendered byte-identically in both** —
they are different messages, but the shared sentence is not a place to vary.

### 40.4 RULING — `そして、` → `Ａｎｄ，` is conditioned on POSITION, and does not reach a list-final `そして`

The wave-6 ruling records `そして、` → `Ａｎｄ，` from `chunk_024` and `pending/chunk_043`. Measured at
this review, **both ruled instances have `そして、` standing ALONE on its own display row**, and that
is what licenses keeping the comma:

```
chunk_024 L15 seg15  |そして、|             → |Ａｎｄ，|   opens a NEW sentence (僕は素性を隠すため…)
chunk_043 L13 seg2   |そして、|             → |Ａｎｄ，|   own row, between two noun phrases
chunk_026 L14 row3   |そして、極めて残忍です。|  → |ａｎｄ　ｕｔｔｅｒｌｙ　ｃｒｕｅｌ．|
```

Chunk 26's is the **final conjunct of a three-item predicate list** opened three rows earlier by
`彼らは、` — `恐ろしく強大で、` / `驚くほど頭が回り、` / `そして、極めて残忍です。` → `Ｔｈｅｙ　ａｒｅ`
/ `ｆｅａｒｓｏｍｅｌｙ　ｍｉｇｈｔｙ，` / `ａｓｔｏｎｉｓｈｉｎｇｌｙ　ｃｌｅｖｅｒ，` /
`ａｎｄ　ｕｔｔｅｒｌｙ　ｃｒｕｅｌ．` The English is a matching tricolon whose row breaks fall on the
source's own commas. `Ａｎｄ，　ｕｔｔｅｒｌｙ　ｃｒｕｅｌ．` would capitalise a conjunction mid-sentence,
put a comma after "And" that no English style permits, and break a list the source explicitly
builds.

**The rule, stated with its condition:** `そして、` **alone on its display row** (equivalently:
opening a new sentence, or standing as its own coordinating row) takes `Ａｎｄ，`. `そして`
**continuing into its own clause** takes lowercase `ａｎｄ` with no comma. `Ａｎｄ　ｔｈｅｎ` stays
reserved for `それから` (absent from chunk 26). Shipped work already agrees with the second half:
`pending/chunk_005` 15.10 `そして　くれぐれも` → `Ａｎｄ　ａｂｏｖｅ　ａｌｌ，` and
`pending/chunk_043` 3.7 / 32.0 → `Ａｎｄ　ｔｈｉｓ　ｉｓ　ｔｈｅｉｒ` / `Ａｎｄ　ｔｈｅ　ｌｅａｄｅｒｓ　ｗｈｏ`,
all three with **no comma after `Ａｎｄ`**. Reach re-measured and **exact as briefed**: **10 battle
(chunks 5, 16, 24, 25, 26, 39, 43) + 9 script (banks 1, 9, 32, 41)**.

### 40.5 Treize IS the dark elf of L10/L11 — confirmed on the channel test, not the portrait id

PR #22's Flag 2 proposed it from the portrait id. Re-tested at review on the **channel**, as PR #23
requires, and it **strengthens**: the triple **(id 0006, channel `{FC51}`, selector `FA11`) is
constant across L3, L10, L11 and L15**, and in L15 Seti addresses that exact speaker by the vocative
`トレーズ、` and it answers `セ、セティ・・・助けてくれ。` The content chains independently: L11's
`この私が、人間などに・・` is a defeat by humans, and L15's `傷だらけになって` /
`新しく来た人間どもだ` / `油断して、不覚をとった` each presuppose that defeat. One voice throughout.

**Consequence:** Treize is not a grovelling minion but a proud dark elf whose hauteur survives his
defeat, and **chunks 27, 28 and 29 inherit that voice.** ⚠️ **Residual caveat, unchanged:** chunk 26
contains **no `{FB00}` portrait-graphic tag at all**, so no id is tied to an image here, and
L10/L11 carry different `{FCE0}` arguments. Chunks 27–29 can still overturn it.

Note the corollary the chunk establishes: **dark elves are a kind of `魔族`.** Treize is called a
`ダークエルフ` at L10 and is one of the demons Annette describes; L5's `魔族とやらの歓迎` covers the
same enemies. The two terms are not exclusive, and both stay lowercase (§17, §17.1).

### 40.6 Recorded, not re-cut — checked at review and not defects

- **`まさか、` diverges from `chunk_000`'s `Ｉｔ　ｃａｎ’ｔ　ｂｅ，` and is PRE-AUTHORISED.** §33.6's
  exclamative row **names chunk 26 by number** and rules that `〜とは` "takes the English that fits
  its own clause". L14's `まさか、こんな形で会えるとは・・` is the exclamative →
  `Ｔｏ　ｔｈｉｎｋ　ｗｅ　ｗｏｕｌｄ` / `ｍｅｅｔ　ｉｎ　ｓｕｃｈ　ａ　ｗａｙ．．`; chunk 0 sits in §33.6's
  *incredulous* row. Nothing to reconcile.
- **`な、何をするっ！？` — a SECOND row divergence the PR did not declare, and chunk 26 is right.**
  `pending/chunk_043` L27 ships `Ｗ‐ｗｈａｔ…` (22) against this unit's `Ｗ，　ｗｈａｔ…` (23). All 12
  stutter rows in the corpus were surveyed: the `Ｘ，　` form is the shipped convention **8 to 1**
  and the `Ｘ‐` outliers are one line of `chunk_000` (internally inconsistent with its own
  `Ａｈ，　`) and two in **parked** chunk 43, which `assemble.py` never reads. FLAGS §AB3.
- **`はい。` → `Ｙｅｓ．` shares its English with `ええ。`; §25.3 MET.** Re-measured: `はい。` battle
  [26, 29] + bank [5]; `ええ。` battle [7, 19] + banks [33, 41] — disjoint in both dimensions.
- **`許サナイ` keeps chunk 10's word and changes its voice.** `chunk_010` renders
  `沼ヲオカス者、許サナイ、` passively; L7's `人間許サナイ！` is active with 人間 as object, and
  `Ｈｕｍａｎｓ　ａｒｅ　ｎｏｔ　ｆｏｒｇｉｖｅｎ！` measures **exactly 24** (verified). Rendered
  `Ｈｕｍａｎｓ　ｗｅ　ｎｏｔ　ｆｏｒｇｉｖｅ！` (**22**, verified) — object-fronted as the Japanese is,
  dropping the auxiliary *do* rather than the negated verb, which is §5 read precisely.
- **`恐ろしい` takes two English forms one sentence apart, deliberately** — `本当に恐ろしいのは` →
  `Ｔｈｅ　ｔｒｕｌｙ　ｄｒｅａｄｆｕｌ　ｏｎｅｓ`, adverbial `恐ろしく強大で` → `ｆｅａｒｓｏｍｅｌｙ　ｍｉｇｈｔｙ，`.
  No glossary row fixes 恐ろしい, so the "one word, two grammatical shapes" pattern (which governs
  *fixed terms*) is not engaged. `ｄｒｅａｄｆｕｌｌｙ　ｍｉｇｈｔｙ` reads as a bare intensifier and loses
  the fear the sentence is about.
- **`奴ら` / `やつら` are rendered per row**, as §32.8 shapes it — the project has never fixed them
  and shipped work varies widely. L15's `やつら` (humans) → `Ｔｈｏｓｅ　ｍｅｎ`, matching `chunk_006`
  L11; L14's `さっきの奴ら` (**demons**, so *men* would be wrong) → `Ｔｈｅ　ｏｎｅｓ　ｆｒｏｍ　ｊｕｓｔ
  ｎｏｗ，`.
- **`Ｔｈｅｓｅ　ｓｏ‐ｃａｌｌｅｄ　ｄｅｍｏｎｓ’` / `ｗｅｌｃｏｍｅ，`** breaks between possessive and head
  noun where the source breaks after `歓迎、`. §34.9 ruled this shape acceptable; no lone one- or
  two-letter word is stranded. `‐` is U+2010, in the allowed set.
- **37 short EN rows were checked for orphaning and none is orphaned** — each answers an equally
  short source row (`はい。`→`Ｙｅｓ．`, `いえ、`→`Ｎｏ，`, `トレーズ、`→`Ｔｒｅｉｚｅ，`).

### 40.7 Cross-unit rows LEFT LIVE — chunk 26 is the FIRST of its pair to merge

Verified **by reading the integration branch's tree** at merge time, not assumed (the wave-5 lesson,
FLAGS §Y2): `tl/battle/chunk_025.txt` and `tl/script/batch_008.tsv` are both **absent**.

- ⚠️ **`魔族`'s §9 row STAYS LIVE.** It pairs this unit with `batch_008` (PR #21), which has **not**
  merged. Per the `ルート` precedent (§29.1 / §30.1) **PR #21's reviewer strikes it**, having
  verified the merged chunk 26 rather than assuming.
- **`場所` has NO §9 row at all** — `grep -c 場所 glossary.md` = **0**. It was briefed as a
  cross-unit pair with `batch_008`; there is nothing to strike or leave live. Recorded so the next
  reviewer does not hunt for it.
- **`末えい` does not occur in chunk 26** and is untouched by this unit.
- **`フフ` / `ふふ` do not occur in chunk 26**, so §12.3 / §32.7's `Ｆｕｆｕ` is not engaged here.
- **`ｄｅｓｃｅｎｄａｎｔ` does not occur in chunk 26**, so nothing propagated PR #23's Flag 15
  miscount (it is **10** columns; §9 already carries the measurement).

---

## 41. Added by chunk 025 (PR #23, merged 2026-09-09)

Rendered in `tl/battle/chunk_025.txt` — chapter 25, the flight to the ship and the unmasking:
Hoag runs for the harbour; Torif catches him and the brothers discover each has been told the other
wants him dead; Helfer greets them both and blames "someone"; Aries breaks cover and names Helfer as
the man who deceived them, goaded Fernando and used Fernando to destroy her kin; Guilford appears,
Rimul reports every port on the continent sealed, Helfer drops the mask; Aries attacks Guilford with
Aura Smasher and is struck down; the party sails; Helfer and Guilford close on the light-elf seal.

**5,403 / 8,192 bytes, slack 2,789** — 1,039 JP → 2,220 EN characters = **2.1367×** against a
**3.4837** tier-C ceiling, 61.3 % of the English budget. **129 text rows** (source 124), widest
**23**, ten at 23, **none at 24**, no page over four text rows. `{FFFE}` **101 → 106 (+5)**, all on
one message line; `{FCC0}` **11 → 11**, none added or removed; `{FFFF}` 14, `{FC50}` 27, `{FC51}`
23, `{FC00}` 2, `{PAD 5161}` — every one unchanged, and the non-`{FFFE}` tag stream is
byte-identical to the dump on all 18 lines. **Merged at round 2**, with two findings, both fixed
and both independently re-verified by the translator before pushing.

`Ｔｏｒｉｆ` (§38.1) ×4, `Ｈｏａｇ` (§39.1), `Ａｒｉｅｓ` (§33.1), `Ｇｕｉｌｆｏｒｄ` / `Ｒｉｍｕｌ` /
`Ｆｅｒｎａｎｄｏ` (§1), `Ｈｅｌｆｅｒ` (§11.1), `Ｃａｕｃａｓｕｓ` / `ｔｈｅ　Ｅｍｐｉｒｅ` (§2),
`Ｃｏｍｍａｎｄｅｒ` (§11.2), `Ｔｃｈ，` (§11.5), `Ｈｍｐｈ` ×3 (§6), `Ｒｉｇｈｔ，` (§24.3),
`ｍｏｖｅ　ｏｕｔ！` (§6), `Ｉ　ｓｅｅ．` (§30.3), `Ｔｒｕｌｙ，` (§28.3), `Ｈｏｗｅｖｅｒ，` (§23.3, its
ninth use), `Ｗｈａｔ　ｄｏ　ｙｏｕ　ｍｅａｎ．` (§37.4), `Ｎｏｔ　ｓｏ　ｆａｓｔ．` (§34.3),
`ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ` (§25.5), `Ｙｏｕ　ｍａｙ　〜` (§31.2), `Ｙｏｕ　〜` on a contempt vocative
(§36.3), `ｋｉｎ` / `ｐｕｒｓｕｅｒｓ` (§36.1), `ａｌｌ　ｒｉｇｈｔ` (§34.8), `Ｆｏｒ　ｎｏｗ，` (§33.2),
`ｏｎｌｙ` for `たかが` (§19.1), `ｄｕｔｙ`, `ｐｉｅｃｅ` (§31.2), `ｇｒｕｄｇｅ` (§39.1) and §24.3's
comma-stutter shape are used unchanged. **Three §9 wave-6 seeds are promoted below, all three used
exactly as seeded, not one improved on unilaterally.**

### 41.1 People, words and things first rendered here — three promotions out of §9

| Japanese | English | Note |
|---|---|---|
| ライトエルフ | `ｌｉｇｈｔ　ｅｌｆ` / `ｌｉｇｈｔ　ｅｌｖｅｓ` | **Promoted from §9's wave-6 seed and STRUCK there — chunk 25 carries BOTH battle instances, so the term is exhausted and no cross-unit row survives.** 9 / 11 columns confirmed. Lowercase per §17.1's species test and §17.2's shipped `ｄａｒｋ　ｅｌｆ`. `ライトエルフの末えい` takes the English genitive plural `ｏｆ　ｔｈｅ　ｌｉｇｈｔ　ｅｌｖｅｓ`, `ライトエルフの封印` the attributive singular `ａ　ｌｉｇｈｔ　ｅｌｆ　ｓｅａｌ`. **2 battle + 0 script** |
| オーラスマッシャー | `Ａｕｒａ　Ｓｍａｓｈｅｒ` | **Promoted from §9 and STRUCK there.** 12 columns. A true hapax — 1 battle / 0 script. **Aries's spell**, confirmed on the channel byte (§41.2) |
| 末えい | `ｄｅｓｃｅｎｄａｎｔ` | **Promoted from §9, used exactly as seeded**, rendered `ａ　ｄｅｓｃｅｎｄａｎｔ　ｏｆ　ｔｈｅ` (**19** columns, not the PR's 20). **10 columns**, `len()`-measured — PR #23's own Flag 15 proposed 11 and **the author formally withdrew it at round 2**; the seed was right. ⚠️ **The §9 row is DELIBERATELY LEFT LIVE** for `batch_008` (PR #21), which renders it too and had not merged; chunk 25 is the first of that pair. **Not a new form**: `chunk_010` 12.2 already ships it for the full-katakana `マツエイ` (§5) |
| 王家 | `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ` | **15** columns (not the PR's 16). **Ruled at review — see §41.5.** ⚠️ Parked `pending/chunk_005.txt` renders it `ｔｈｅ　ｃｒｏｗｎ’ｓ`; that file does not ship, so gate 6 is not engaged, and the re-cut is queued in `pending/README.md`. **4 battle (chunks 5 ×2, 25 ×2) + 7 script** |
| 王位 | `ｔｈｅ　ｔｈｒｏｎｅ` | 10 columns. **CROSS-UNIT with chunk 24 and struck at §39.1 by this merge.** `王位なんか狙ってはいない` → `Ｉ　ｈａｖｅ　ｎｏ　ｄｅｓｉｇｎｓ` / `ｏｎ　ｔｈｅ　ｔｈｒｏｎｅ　ｗｈａｔｅｖｅｒ．`, the `なんか` carried in `ｗｈａｔｅｖｅｒ` on shipped `chunk_021` L11's precedent |
| 王子 (bare vocative) | `ｍｙ　Ｐｒｉｎｃｅ` | 9 columns. Helfer's deferential address to Hoag (`〜ですぞ、王子。`) |
| 王子様 (vocative) | `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ` | **13** columns (not the PR's 14). The 様 rendered as the English title of the station, on §24.1's `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ` and §33.1's `フェリクス様` → `Ｇｏｖｅｒｎｏｒ　Ｆｅｌｉｘ`. **Held distinct from the bare `王子` above — two source strings, two English forms, separated by the honorific; see §41.6.** ⚠️ **The 8 script instances read REFERENTIAL and are NOT ruled here** |
| 王子たち | `ｔｈｅ　Ｐｒｉｎｃｅｓ` | 11 columns. Already on the referential side of §41.6's split. 2 battle (25, 30) + 6 script |
| 大陸 | `ｔｈｅ　ｃｏｎｔｉｎｅｎｔ` | **13** columns (not the PR's 14). ⚠️ **CROSS-UNIT with `batch_008`**: 1 battle (this) + 6 script (banks 4, 5, 41). No §9 row exists, so there is nothing to strike — recorded here instead, and **PR #21 must match this form** |
| 踊り子 | `ｄａｎｃｅｒ` | 6 columns. Aries, whom §33.1 already fixes as a travelling performer. **Largest reach of anything new here: 1 battle + 18 script** (banks 1, 18, 20, 23, 41) |
| 家臣 | `ｒｅｔａｉｎｅｒｓ` | **9** columns (not the PR's 10). Hoag's household men waiting on the ship. 1 battle + 2 script |
| 野ネズミ | `ｆｉｅｌｄ　ｍｉｃｅ` | **10** columns (not the PR's 11). Helfer's contempt for the party. **A fifth contempt word**, held apart from 雑草ども → weeds (§11.5), ゴミ → rubbish (§14.4), 穀潰し → freeloaders (§2) and ガラクタ → junk (§23.1). **4 battle (25, 41, 42 ×2) + 1 script (bank 41)** |
| 小娘 | `ｔｈａｔ　ｇｉｒｌ` | 9 columns. Contempt carried by the demonstrative, per §31.2's mechanism. 2 battle (25, 31) — **chunk 31 inherits it** |
| 弱小種族 | `ｐｕｎｙ　ｒａｃｅ` | **9** columns (not the PR's 10). Direct address, so `Ｙｏｕ　〜` per §36.3. Hapax |
| 知に溺れた | `ｄｒｏｗｎｅｄ　ｉｎ　（ｙｏｕｒ　ｏｗｎ）　ｃｌｅｖｅｒｎｅｓｓ` | Hapax. Post-posed because English requires it |
| 張本人 | `ｔｏ　ｂｌａｍｅ` | `ヘルファーが張本人よ。` → `Ｈｅｌｆｅｒ　ｉｓ　ｔｏ　ｂｌａｍｅ．` (**19** columns, not the PR's 20). Held **distinct** from 黒幕 → `ｗｈｏ　ｉｓ　ｂｅｈｉｎｄ　ｉｔ` (§15.2, shipped `batch_002` L9). Hapax |
| 企み | `ｐｌｏｔ` | 4 columns. ⚠️ **`ｐｌｏｔ` now renders FOUR source words** — 企み here, 計画 (chunk 24), 企てた (`batch_007` L50) and the noun in `batch_005` L36. §25.3's test re-run at this review and **MET**: 企み is battle chunk 25 only + 0 script; 計画 is battle chunk 24 only + banks 5, 41; no shared chunk, no shared bank, no message holds two |
| そそのかす | `ｇｏａｄ` | **4** columns (not the PR's 5). Hapax. Held distinct from 操る below |
| 操る | `ｍｏｖｅ` | `フェルナンドを操り、` → `ｈｅ　ｍｏｖｅｄ　Ｆｅｒｎａｎｄｏ`. Chosen to chime with §31.2's `手駒` → `ｐｉｅｃｅｓ` and this chunk's own `駒` — the same speaker's board metaphor |
| 駒 | `ｐｉｅｃｅ` | 5 columns. **Not a new form** — §31.2 fixes Guilford's `手駒` → `ｐｉｅｃｅｓ` in shipped `chunk_018`; same man, same metaphor, and this is the line where it starts. 2 battle (18, 25) + 3 script (bank 41) |
| 封印 | `ｓｅａｌ` | 4 columns. 2 battle (25, 32) + 4 script (bank 41) |
| もろとも | `〜　ａｎｄ　ａｌｌ` | `王子もろとも` → `Ｔｈｅ　Ｐｒｉｎｃｅｓ　ａｎｄ　ａｌｌ，`. Hapax |
| 番狂わせ | `ｕｐｓｅｔｓ` | 6 columns. Hapax |
| 計算違い | `ｍｉｓｃａｌｃｕｌａｔｉｏｎ` | **14** columns (not the PR's 15). Hapax |
| 出航 | `ｓｅｔ　ｓａｉｌ` | **8** columns (not the PR's 9). Hapax |
| 追手 | `ｐｕｒｓｕｅｒｓ` | **8** columns (not the PR's 9). **Not a new rendering — a second SOURCE SPELLING** of §36.1's `追っ手`, shipped in `chunk_021` L3 as `Ｐｕｒｓｕｅｒｓ？`, collapsing onto it per §17.2's 鬼 / オーガ. `追手` is battle 25, 29; `追っ手` is battle 21 only. ⚠️ **A gate-6 grep on the exact Japanese will not pair them, and a lowercase grep of `tl/` will not find the chunk-21 instance either** — it is sentence-initial. **Chunk 29 inherits it** |
| なんか (dismissive) | `ｗｈａｔｅｖｅｒ` | The particle carried in a word English already uses for it, matching shipped `chunk_021` L11's `ｎｏ　ｉｎｔｅｎｔｉｏｎ　ｗｈａｔｅｖｅｒ` |
| うわああっ | `Ｕｗａａａｈ` + the source's own punctuation | **6** columns (not the PR's 7). A scream, on §32.3's `ぬおっ` → `Ｎｗｏｈ` transliteration template and held distinct from `Ｇｕｈ` / `Ｇｗａｈ` / `Ｇｕｆｆ` / `Ｎｗｏｈ` / `Ｇｗｏｈ` / `Ｕｇｈ`. Verified free. Hapax |

### 41.2 Portrait id is NOT speaker — this chunk proves it twice, and the CHANNEL is what decides

Both of this unit's long messages put **two different speakers under one `{FCB0}` portrait id** and
separate them only by the `{FC50}`/`{FC51}` channel byte. This is the §23.5 / §28.7 / §30.7 pattern
at its most load-bearing, and §40.5 independently used the same test on chunk 26's Treize.

```
port 0006 ch0  おっと、そうはさせん。                            Guilford
port 0006 ch1  どけっ！どかないと貴様も殺すぞ！                    Aries
port 0006 ch0  フフ・・、おもしろい。やってみろ。                   Guilford
port 0006 ch1  死ねっ！！                                     Aries
port 0006 ch0  フッ・・・・なるほど、確かにライトエルフの末えいのようだな。 Guilford
port 0006 ch1  そ、そんな・・・オーラスマッシャーがきかない・・・？       Aries
port 0006 ch0  フン、滅びるがいい。知に溺れた弱小種族め！              Guilford
```

**This settles §9's attribution from inside the chunk**: Aries is the light-elf descendant and Aura
Smasher is *her* spell. Torif is not in the exchange at all. Two further readings the PR's own flag
did not carry, both from the channel:

- **Portrait 0002 channel 0 is HOAG, not Torif.** `何を言ってるんだ、トリフ。お前こそ、私の命を狙って・・・`
  is Hoag borrowing his brother's portrait; the English is right (`Ｉｔ　ｉｓ　ｙｏｕ　ｗｈｏ` /
  `ｓｅｅｋ　ｍｙ　ｌｉｆｅ．．．`, `私`, contraction-free).
- **Portrait 0008 channel 0 in the final message is GUILFORD, not Helfer.** Helfer (ch1) apologises
  `すまぬことをしたな、ギルフォード。`; ch0 answers `なに、かまわん。…私が一人で解いてみせる。` — the man
  who undoes a seal is the 魔導師 (§11.4), and Helfer has just addressed him by name.

### 41.3 Register

| Who | Register |
|---|---|
| Aries (portrait 0B, and 06 ch1 in the duel) | §33.1 / §33.7 **unchanged and held across all six turns** — `Ｄｏ　ｎｏｔ　ｂｅ　ｄｅｃｅｉｖｅｄ！`, `Ｈｅｌｆｅｒ　ｉｓ　ｔｏ　ｂｌａｍｅ．`, `Ｉ　ｗｉｌｌ　ｄｅｆｅａｔ　Ｈｅｌｆｅｒ！`, `Ｏｕｔ　ｏｆ　ｍｙ　ｗａｙ！`, `Ｄｉｅ！！`, `Ｔｈ，　Ｔｈａｔ　ｃａｎｎｏｔ　ｂｅ．．．` ⚠️ **Her SOURCE register shifts here and the English does not follow it into contractions.** §33.1 fixes her polite です／ます from chunks 19 and 20; this chunk drops it entirely (`だまされちゃダメよ！`, `どけっ！`, `死ねっ！！`). **Ruled at review: the force goes in the words, not in newly granted contractions**, so §33.1's no-contraction row stands unbroken across all three of her chunks. The shift is the source's and is characterisation, not a register error |
| Helfer (portrait 08) | §11.6 unchanged — **no contraction anywhere**: `Ｉｔ　ｓｅｅｍｓ，　ｍｙ　Ｐｒｉｎｃｅ，`, `Ｉ　ｓｈａｌｌ　ｓｅｎｄ　ｙｏｕ　ｔｏ`, `Ｉ　ｈａｖｅ　ｄｏｎｅ　ｙｏｕ　ｗｒｏｎｇ，`. His `あの世へ送ってやる。` deliberately does **not** copy shipped `chunk_000`'s `Ｉ’ｌｌ　ｓｅｎｄ　ｙｏｕ` — different message, and the contraction is not his |
| Guilford (portrait 06 ch0, 08 ch0) | **No contraction anywhere** — `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ　ａｔ　ａｌｌ．`, `Ｉ　ｓｈａｌｌ　ｕｎｄｏ　ｉｔ　ａｌｏｎｅ．`, `ｗｉｌｌ　ｎｅｖｅｒ　ｄｅｆｅａｔ` / `ｏｎｅ　ｓｕｃｈ　ａｓ　Ｉ！！`. His boastful `この私` takes `ｏｎｅ　ｓｕｃｈ　ａｓ　Ｉ`, the §25.1 `このクリミアに` shape, and his `Ｆｕｆｕ．．，` is §12.3's fixed laugh |
| Hoag (portrait 03, and 02 ch0) | Formal and measured, `私`, **no contractions** — `Ｗｈａｔ　ａｒｅ　ｙｏｕ　ｓａｙｉｎｇ，　Ｔｏｒｉｆ．`, `ｗｈａｔ　ｉｎ　ｔｈｅ　ｗｏｒｌｄ` / `ｉｓ　ｔｈｅ　ｍｅａｎｉｎｇ　ｏｆ　ｔｈｉｓ？`, `Ｔｈａｔ　ｓｈｉｐ　ａｔ　ｔｈｅ　ｂａｃｋ．` |
| **Torif (portrait 02 ch1) — FIXED HERE, first full scene** | Formal, earnest and young, `僕`, **no contractions** — `Ｂｒｏｔｈｅｒ，` / `ｉｓ　ｉｔ　ｔｒｕｅ　ｔｈａｔ　ｙｏｕ` / `ａｒｅ　ｓｅｅｋｉｎｇ` / `ｍｙ　ｖｅｒｙ　ｌｉｆｅ？`, `Ｉ　ｈａｖｅ　ｎｏ　ｄｅｓｉｇｎｓ`, `Ｉ，　ａｆｔｅｒ　ｙｏｕ，　Ｂｒｏｔｈｅｒ？` He addresses Hoag as `兄さん` → **`Ｂｒｏｔｈｅｒ`**, capitalised as a vocative on §25.4's `Ｆａｔｈｅｒ` / §39.1's `Ｇｒａｎｄｆａｔｈｅｒ` split. **Chunks 26 and 42 carry him** |
| Rimul (portrait 07) | §7 / §30.7 unchanged — `Ｇｕｉｌｆｏｒｄ，　ａｓ　ｐｌａｎｎｅｄ，`, `ｉｓ　ｓｅａｌｅｄ．`, `Ｎｏｔ　ｏｎｅ　ｋｉｔｔｅｎ　ｇｅｔｓ　ｉｎ．` — no contractions, and the `ネコの子一匹` image kept rather than idiom-swapped |
| The Caucasus townsman (portrait 05, L6) and the enemy soldier (portrait 05, L13) | Civilian and rank-and-file, contractions throughout (`Ｉｔ’ｓ`, `Ｉ’ｖｅ`, `Ｉ’ｌｌ`, `ｄｏｎ’ｔ`) — the deliberate §7 contrast that makes the royal and imperial flatness read as rank. **Two different speakers on one portrait id in different messages**, which is normal for this dump |
| Portraits 01 and 09 | **Deliberately unnamed and no row is proposed.** 09 says only `誰だ、貴様！`; 01 knows Rimul by sight, uses blunt `お前` to her and polite `ですか` to a 司令官 who is present. Fernando fits and nothing in the chunk names him, so the English supplies no name — the §28.7 / §31.1 practice. A later chunk may settle it |

### 41.4 CORRECTION to §33.2 (§4.3) — `どうやら` splits on REGISTER, and three shipped rows predated the row that claimed to fix it

§33.2 fixes `どうやら、` → `Ｌｏｏｋｓ　ｌｉｋｅ　…` and names chunk 25 among four chunks it binds.
**Chunk 25 renders it `Ｉｔ　ｓｅｅｍｓ，` and that is correct; the row is what is wrong.** Counted
across the tree at this merge — twice, once at each review round, with chunk 26 arriving between:

| where | speaker | register | English |
|---|---|---|---|
| `chunk_002` ×2 | Albert | §20.5 deferential, formal, **no contractions** | `ｉｔ　ｓｅｅｍｓ` / `Ｉｔ　ｓｅｅｍｓ　ｔｈｅｙ　ａｒｅ` |
| `chunk_002` (other coda variant) | Albert | as above | `Ｔｈｅｙ　ｗｏｕｌｄ　ｓｅｅｍ　ｔｏ　ｂｅ` |
| `pending/chunk_017` | Rendol | §30.7 formal, **no contractions** | `Ｔｈｅｙ　ｓｅｅｍ` |
| **`chunk_025`** | **Helfer** | **§11.6 grandiose, archaic, no contractions** | **`Ｉｔ　ｓｅｅｍｓ，`** |
| `chunk_014` | `〜みたいだぜ` | casual | `Ｌｏｏｋｓ　ｌｉｋｅ` |
| `chunk_019` | 9th Army, `Ｉ　ｃａｎ’ｔ　ｓａｙ` | casual | `Ｌｏｏｋｓ　ｌｉｋｅ　ａ` |
| **`chunk_026`** | **`敵のようだな`, plain `だな`** | **casual** | **`Ｌｏｏｋｓ　ｌｉｋｅ　ｅｎｅｍｉｅｓ．`** |

> **Ruled: contraction-taking, casual speakers take `Ｌｏｏｋｓ　ｌｉｋｅ　…`; contraction-free, formal
> speakers take a `seem` clause.** **Register predicts 8 of 8, with no exceptions.**

This is the §36.2 `とにかく` shape exactly, and §36.3's scoping of §31.2's `〜め` before it. Two
things are worth keeping beyond the ruling itself:

1. **§33.2's claim to be "fixing it now rather than letting four units each invent one" was false
   when it was written.** `chunk_002` (wave 1) and `chunk_014` had already shipped **three**
   `seem` renderings; the row counted only the *untranslated* chunks it would bind. A reach count
   that looks forward and not backward is the §37.3 / §38.6 failure in a new place.
2. **Chunk 26 is the decisive instance precisely because nobody was arguing about it.** An
   independent unit and an independent reviewer put a plain `だな` speaker on the `Ｌｏｏｋｓ　ｌｉｋｅ`
   side, between this PR's two review rounds, with no knowledge of this question.

**Lines this affects: none.** All eight instances are already on the right side. §33.2's row is
patched in place with the condition; the English forms are unchanged.

### 41.5 RULING — `王家` takes `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ`, and `ｔｈｅ　ｃｒｏｗｎ` cannot do the job

`pending/chunk_005.txt` renders `宮廷軍は王家のもの` as `Ｔｈｅ　Ｒｏｙａｌ　Ａｒｍｙ　ｉｓ` /
`ｔｈｅ　ｃｒｏｗｎ’ｓ．` Chunk 5 is **parked**, so it is not in `tl/`, gate 6 does not bind it and §3 is
not engaged. The question is which form to fix forward, and it is settled by what the other
construction will take rather than by seniority:

- `王家を狙う何者か` → `ｓｏｍｅｏｎｅ　ｐｌｏｔｓ　ａｇａｉｎｓｔ` / `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ．`
- `王家の人間がおらずとも` → `Ｅｖｅｎ　ｗｉｔｈｏｕｔ　ｏｎｅ　ｏｆ` / `ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ，`

***one of the crown* is not English.** A single form has to serve both, and only
`ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ` (15) does. **Reach: 4 battle (chunks 5 ×2, 25 ×2) + 7 script** (banks 1,
23, 41), so this needed deciding rather than drifting. `ｔｈｅ　ｃｒｏｗｎ` is **not** reserved — it is
the natural English for 王権 or 王室 should either appear. **`pending/chunk_005.txt`'s two rows are
queued for the re-cut in `pending/README.md`**, on the §23.2 precedent, and cost +8 columns there.

### 41.6 RULING — `王子` and `王子様` split on the HONORIFIC, and only the vocative is decided

Two source strings, two English forms, held apart exactly as §1 and §24.1 hold 様 apart:

| source | who says it | English | why |
|---|---|---|---|
| bare `王子。` | Helfer, to Hoag | `ｍｙ　Ｐｒｉｎｃｅ` (9) | the plain deferential address of a courtier |
| `王子様、` | Aries, to Hoag | `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ` (13) | 様 takes the English title of the station — §24.1's `ナコール様` → `Ｆａｔｈｅｒ　Ｎａｃｏｌ`, §26.1's `バトウ様` → `Ｆａｔｈｅｒ　Ｂａｔｏｕ`, §33.1's `フェリクス様` → `Ｇｏｖｅｒｎｏｒ　Ｆｅｌｉｘ`. **Not** §21.2's `〜さん` rule, which drops the honorific |

The scene supports it: the schemer defers, the outsider uses the full title. ⚠️ **The referential
question is NOT ruled here and must not be treated as settled.** The **8 script instances** read
referential (`王子様を連れて、`, `王子様も、王女様も`, `王子様たちをかくま…`, `王子様が`,
`王子様を・・・！？`), and §1 already fixes the parallel `王女様` → **the Princess** referentially, so
the likely full entry is *referential `ｔｈｅ　Ｐｒｉｎｃｅ` / vocative `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ`` — but
this unit renders no referential instance and a reviewer does not rule on lines that are not in
front of him. **`batch_008` (PR #21) and later script units decide it**; this unit's
`王子たち` → `ｔｈｅ　Ｐｒｉｎｃｅｓ` is already on the referential side.

### 41.7 RULING — `どけっ` takes `Ｍｏｖｅ`, and chunk 25's emphatic is licensed by a repetition

Counted at review: **`どけっ` is 2 battle instances, chunks 24 and 25 only, 0 script** — the dump's
third `どけ` hit is `お城にとどけて` (chunk 0), a substring false positive that any bare grep will
report. Nobody's cross-unit list carried this term; it surfaced only from a positional sweep.

| where | source | English |
|---|---|---|
| `chunk_024` | `どけっ、` | `Ｍｏｖｅ！` |
| `chunk_025` | `どけっ！どかないと貴様も殺すぞ！` | `Ｏｕｔ　ｏｆ　ｍｙ　ｗａｙ！` / `Ｍｏｖｅ，　ｏｒ　ｙｏｕ　ｄｉｅ　ｔｏｏ！` |

> **Ruled: `どけ` → `Ｍｏｖｅ` is the fixed word. Chunk 25 stands and nothing is re-cut.** Its source
> is one speaker, one breath, **the verb repeated** — imperative then negative-conditional. English
> that used `Ｍｏｖｅ！` twice would flatten a repetition the source is using to escalate into a
> threat, so the first takes the emphatic and the second the fixed word. **The emphatic is licensed
> only by that repetition**; a bare `どけ` elsewhere takes `Ｍｏｖｅ`.

§3 is not engaged (different messages, and the source strings differ in their own stop), and the two
chunks are different scenes, so §25.3's co-occurrence test is not reached.

### 41.8 The two round-1 findings, and what each is worth keeping

Both were fixed at round 2 in **one line, one commit**, and both were re-verified by the translator
against the tree rather than taken on the reviewer's word.

**1. `フフ・・、` was `Ｈｅｈ　ｈｅｈ．．，` and is now `Ｆｕｆｕ．．，`.** §12.3 fixes `ふふ` → `Ｆｕｆｕ`
and §32.7 already collapsed `ふふっ` onto it as "a new source spelling … one word, two spellings,
the documented kind". `フフ` is the **third** spelling of that same word, and the project has never
given a kana-script variant its own English — §30.3 did precisely this for `グフッ` → `Ｇｕｆｆ`
("§14.5's ぐふっ in **katakana**"), §11.5 for `くっ` / `クッ`, §28.3 for `何っ` / `何ッ`, §29.3 for
`くーっ` / `く〜っ`. Counted: **`ふふ` 8 battle (chunks 20, 28, 31, 33) + 1 script; `ふふっ` 1 + 1;
`フフ` 2 (chunks 25, 39) + 1; `フフッ` 1 (chunk 39) + 1.** `Ｆｕｆｕ，` is shipped in `chunk_020` and
`chunk_033`, both merged. **23 → 20 columns, −6 bytes, no re-flow**; the two dots and the comma
still follow the source per §5.

⚠️ **Two things worth more than the fix.** First, **§12.3's own row already listed
`Ａｌｔ　Ｈｅｈ　ｈｅｈ　—　ｓｅｅ　ＦＬＡＧＳ`**, so the shipped form was the alternative that row had
rejected — the translator found this itself at round 2 and it is a sharper account than the review's.
Second, its stated cause: it grepped `フフ`, `フッ` and `フン` in **katakana** and never `ふふ` in
hiragana. **A kana-script search finds only its own script.** That is the blind spot §17.2 exists to
close and it is now the third distinct search failure this run, after §Y2's maximal-kanji-run
intersection and §9's full-katakana `マツエイ`. See `FLAGS.md` §AC.

**2. bare `そして、` was `Ａｎｄ　ｔｈｅｎ，` and is now `Ａｎｄ，`.** Merged `chunk_024` and parked
`chunk_043` both ship `Ａｎｄ，` for the byte-identical bare segment, **from the same speaker, Aries,
in the adjacent chapter of one continuous revelation**. Nothing forced the divergence (4 columns
against 9, on a standalone row, with 2,773 bytes of slack), the outlier was the unmerged file rather
than shipped work, and **`Ａｎｄ　ｔｈｅｎ` was already spent** on `それから、` in `pending/chunk_017` —
where §25.3's test *fails*, since chunk 5 holds both source words. **9 → 4 columns, −10 bytes.**
✅ **With this change `Ａｎｄ　ｔｈｅｎ` occurs exactly once in the whole corpus and the collision is
DISCHARGED, not merely recorded.** §40.4's positional narrowing — `そして、` alone on its display row
takes `Ａｎｄ，`, a `そして` continuing into its own clause takes lowercase `ａｎｄ` — is correct and
leaves this instance squarely inside the rule.

### 41.9 Corrections to this PR's own figures (§4.3) — fourteen, and none touches a line of the file

The translator re-measured **all 37** width figures in its PR body at round 2 and reported **14
wrong, 13 of them exactly one too high**; it also **formally withdrew its own Flag 15**
(`ｄｅｓｃｅｎｄａｎｔ` is 10, not 11 — the seed was right). Every one is re-measured here with `len()`
and carried into §41.1 above: `ｄｅｓｃｅｎｄａｎｔ` 11→**10**, `Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ` 14→**13**,
`ｔｈｅ　ｒｏｙａｌ　ｈｏｕｓｅ` 16→**15**, `ｔｈｅ　ｃｏｎｔｉｎｅｎｔ` 14→**13**, `ｒｅｔａｉｎｅｒｓ` 10→**9**,
`ｆｉｅｌｄ　ｍｉｃｅ` 11→**10**, `ｐｕｎｙ　ｒａｃｅ` 10→**9**, `Ｈｅｌｆｅｒ　ｉｓ　ｔｏ　ｂｌａｍｅ．` 20→**19**,
`ｇｏａｄ` 5→**4**, `ｍｉｓｃａｌｃｕｌａｔｉｏｎ` 15→**14**, `ｓｅｔ　ｓａｉｌ` 9→**8**, `Ｕｗａａａｈ` 7→**6**,
`ｐｕｒｓｕｅｒｓ` 9→**8**, `ａ　ｄｅｓｃｅｎｄａｎｔ　ｏｆ　ｔｈｅ` 20→**19**.

Two of this file's own rows were wrong about the same phrase in **opposite** directions and are
patched in place above: **§9 said `Ｐｒｉｎｃｅ　Ｈｏａｇ` is "10 columns with the title" (one LOW) and
§39.1 said 13 (two HIGH); it is 11.**

**The pattern is the finding, not the fourteen instances.** Across both review rounds and both
agents, **every figure either party argued from was exact** — `Ｐｒｉｎｃｅｓ　Ｈｏａｇ　ａｎｄ　Ｔｏｒｉｆ，`
23, the rejected `Ｐｒｉｎｃｅ　Ｈｏａｇ，　Ｐｒｉｎｃｅ　Ｔｏｒｉｆ，` 26,
`Ｒｉｇｈｔ，　ｇｅｔ　ｔｈｅ　ｓｈｉｐ　ｏｕｔ！` 24, `Ｓｕｒｅｌｙ　ｎｏｔ．．．．！？` 16 — **and every wrong
figure was a table cell typed rather than measured.** No rendering anywhere is affected; the risk
is that a *later* unit budgets a row from one of these cells. `FLAGS.md` §AC states the method rule.

### 41.10 Recorded, not re-cut — checked at review and not defects

1. **`まさか・・・・！？` → `Ｓｕｒｅｌｙ　ｎｏｔ．．．．！？` conforms to a ruling the PR did not know
   existed.** §33.6 splits `まさか` into the incredulous / negative-supposition use (takes
   `Ｓｕｒｅｌｙ`) and the `まさか…とは` exclamative (does not), and **its table already lists chunk 25
   among the seven chunks on the `Ｓｕｒｅｌｙ` side.** The supplied `ｎｏｔ` is the negative supposition
   made explicit, which §2 requires because English cannot leave the negative elided. **Ratified.**
2. **`Ｉ　ｓｅｅ．　Ｔｒｕｌｙ，` on one row** is §30.3's `なるほど、` plus §28.3's `確かに、`, both
   unchanged and both with the `、`→`．`/`，` the corpus already uses.
3. **`ｄｕｔｙ` has a THIRD instance the PR did not name** — `batch_007.tsv` renders
   `任務に向かってもらう` → `ｇｏ　ｔｏ　ｙｏｕｒ　ｄｕｔｙ　ａｔ　ｏｎｃｅ`, the **same word 任務** as
   `chunk_001` L0 and this unit. Extra agreement, not a collision. `務め` → `ｄｕｔｙ` in parked
   `chunk_005` is a different word and §25.3's test is met.
4. **`ｏｎｅ　ｓｕｃｈ　ａｓ　Ｉ` is a fifth English form for `この私`** beside `ｍｅ，　ｏｆ　ａｌｌ　ｐｅｏｐｌｅ`
   (chunk 4), bare `ｍｅ` (chunk 18) and `ｔｈｅ　ｌｉｋｅｓ　ｏｆ　ｍｅ` (chunk 43). `この私` is a boastful
   emphatic that takes whatever its clause needs — the §32.8 `何だ、` shape — not a fixed form.
5. **Flag 20's `{FCC0}` rule is right and its stated mechanism is not.** `rowcheck.py` **splits** on
   `{FCC0}` and honours it as a page boundary; what forbids adding or removing one is
   `assemble.py:tag_parity`. **`FLAGS.md` §Q2 already cites `tag_parity` correctly** — checked at
   this merge, and chunk 26's reviewer had already declined to "patch" it for the same reason. The
   wave briefing's framing was the only thing wrong, and §AA7 records that.
6. **Two bare `　` rows** in the final message are the source's own and are reproduced verbatim.

### 41.11 Cross-unit rows after this merge — what is struck and what is LEFT LIVE

Verified **by reading the integration branch's tree** at merge time, not assumed (§Y2):
`tl/battle/chunk_024.txt` and `tl/battle/chunk_026.txt` are present, `tl/script/batch_008.tsv` is
**absent**.

- ✅ **`王位` and `恨み` are STRUCK at §39.1.** Chunk 24 merged **first** and deliberately left both
  live; chunk 25 is the **second** of the pair and strikes them, which is the whole of what the
  `ルート` precedent (§29.1 / §30.1) prescribes. Both units agree byte-for-byte.
- ✅ **`ライトエルフ` and `オーラスマッシャー` are STRUCK at §9 outright** — chunk 25 carries **every**
  battle instance of both, so there is no pair and no second merge to wait for.
- ⚠️ **`末えい`'s §9 row STAYS LIVE.** It pairs this unit with `batch_008` (PR #21), which has not
  merged. **PR #21's reviewer strikes it**, after verifying the merged chunk 25.
- ⚠️ **`大陸` has NO §9 row** — it was never seeded. It is nonetheless cross-unit with `batch_008`
  (1 battle + 6 script, banks 4, 5, 41) and **PR #21 must match `ｔｈｅ　ｃｏｎｔｉｎｅｎｔ`**, 13 columns.
  Recorded at §41.1 rather than in §9, so nobody hunts for a row to strike.
- ⚠️ **`魔族`'s §9 row STAYS LIVE and is NOT mine to strike.** Chunk 26 merged **first** of its pair
  with `batch_008`; §40.7 left it live and **PR #21's reviewer strikes it**. `魔族` does not occur in
  chunk 25 at all — counted: battle chunks 26, 27, 28, 29, 30, 32.
- **`場所` has no §9 row** — confirmed again here after §40.7 recorded the same thing. Nothing to
  strike; the wave briefing's pairing was wrong.

---

## 42. Added by script batch 008 (PR #21, merged 2026-09-09)

Rendered in `tl/script/batch_008.tsv` — `script_unique.txt` **DATA lines 470–516**, 47 unique lines
/ **47 message instances**, all count 1, banks **4 (32) and 5 (15) only**. Two recruit-and-gossip
interfaces sharing one skeleton: the fairy camp in the fairy forest (470–501, **Phyllis**) and the
court of Leverk (502, a retainer; 503–516, **King Leverk**), plus the nine world-gossip lines the
two speakers give under "Ask for information".

**Figures, all re-derived at review rather than taken from the PR.** Bank 4 **11,781 → 10,179**
free (+1,602 used), bank 5 **3,357 → 2,007** (+1,350), banks 3 and 40 **byte-for-byte untouched**,
no bank negative — measured by moving the file aside, re-merging and re-running `bankmeasure`.
**1,577 JP → 3,052 EN visible characters = 1.9353×** (⚠️ the PR body's 2,932 / 1.86× are wrong;
the true figure closes exactly on the bank deltas — `(3052−1577)×2 + 2 = 2,952 = 1,602 + 1,350`).
47 lines, **32 distinct translations**, **190 text rows, widest 23 with 20 rows there and none at
24**, no page over 4 text rows the source did not already exceed. `{FFFE}` **+1, on DATA 470 only**;
`{FCC0}` **19 → 19, none added**; the non-`{FFFE}` tag stream **byte-identical on all 47 lines**.
`{FC50}` 0 / `{FC51}` 9 in both columns. Zero `・` in the unit, so §3.1's dot rule is vacuous.
Merged at **round 1**, with zero findings requiring a change to the unit.

⚠️ **Numbering here is `script_unique.txt` DATA index** (file line = data + 5), the §34 convention.
⚠️ **`FLAGS.md` §Z2 numbers the same lines in FILE index and the two differ by exactly 5** — see
§42.5. **Locate by content.**

`Ｉ　ｓｅｅ．` (§30.3, §38.2), `Ｍｙ？` / `Ｍｙ，` for あら (§32.4), `Ｈｏｗｅｖｅｒ，` for しかし and
しかしながら (§23.3 — its tenth and eleventh uses), `Ｗｅｌｃｏｍｅ` for ようこそ (§34.5),
`Ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` (§24.3), `　Ｙｅｓ` / `　Ｎｏ` (§34.1), `Ｊｅｗｅｌｓ` (§34.1),
`ｒｅｃｒｕｉｔ` and `Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ` (§38.2), `ｇｒｅａｔ　ｆｏｒｔｒｅｓｓ` /
`ｆｏｒｔｒｅｓｓ` / `ｅｌｉｔｅ　ｃｏｒｐｓ` / `ｔｈｅ　Ｅｍｐｉｒｅ` (§2), `ｔｈｅ　Ｋｉｎｇ` (§28.1),
`〜’ｓ　ｆｉｎｅｓｔ` for きっての (§23.1), `ｆｒｅｅ` for 解放 (§28.2), `ｍｏｎｓｔｅｒ` for モンスター
(`batch_001` L33), `ｓｕｒｅｌｙ` for きっと (§33.6), `ｒｕｍｏｕｒ` (§26.4), `ｔｈｅｙ　ｓａｙ` for
らしい / と聞きます (§26.6), `ｄｅｓｃｅｎｄａｎｔ` (§41.1), `ｄｅｍｏｎｓ` (§40.1) and `ａｆｒａｉｄ`
(§39.7) are used unchanged.

### 42.1 People, places and words first rendered here — seven promotions out of §9

| Japanese | English | Note |
|---|---|---|
| キエーザ | `Ｋｉｅｓａ` | **Promoted from §9's wave-2 seed, used exactly as seeded.** **5 columns.** The first rendering anywhere; rendered twice in DATA 512 (`キエーザの沼` → `ｔｈｅ　ｓｗａｍｐ` / `ｏｆ　Ｋｉｅｓａ．`, `キエーザの南` → `ｓｏｕｔｈ　ｏｆ` / `Ｋｉｅｓａ．`). `Ｋｉｅｓａ` verified **free** across `tl/` and `pending/` at review. ⚠️ **The `Ｃｈｉｅｓａ` (Italian *church*) reading is NOT ruled out, only unsupported here**: this unit names a swamp and a direction and gives no religious evidence either way. `キエーザ城` (script 1090/1092) is still unrendered and is where the question actually lives — §9's row is struck, but the question is carried forward in `FLAGS.md` §AD |
| レバーク王 | `Ｋｉｎｇ　ｏｆ　Ｌｅｖｅｒｋ` | **14 columns.** Built on two fixed entries, not invented: §28.1's レバーク → `Ｌｅｖｅｒｋ` (a **kingdom**, as §28.1 corrected) and the **form** already shipped in `tl/battle/chunk_013.txt` L8 for `我がルクレール国王` → `ｏｕｒ　Ｋｉｎｇ　ｏｆ　Ｌｅｃｌｅｒｃ`. `予は　レバーク王。` → `Ｉ　ａｍ　Ｋｉｎｇ　ｏｆ　Ｌｅｖｅｒｋ．` (20), articleless as that precedent is. Bare `王は` → `Ｔｈｅ　Ｋｉｎｇ` (8) on §28.1's 国王 row — the speaker of DATA 502 is a **retainer** in honorific third person (`おられる`), not the King |
| 砲台 (prose) | `ｂａｔｔｅｒｙ` | **7 columns.** DATA 514, `炎の雨を　降らせる砲台`. **First prose rendering.** §4's `無人砲台` → `turret` is a *class-label* row and is **untouched** — the class-vs-prose split §17.1 makes for ウィザード / 魔導師 and §24.2 for 弓兵 / 弓使い. ⚠️ **The two do share banks 4 and 5**, because the 21-instance item table is replicated everywhere and `batch_003` L91/L92 ship `ｔｕｒｒｅｔ`; that is the split working as designed, not a collision. ⚠️⚠️ **CORRECTED AT MERGE, and this one changes an inherited decision:** the PR's row tells chunk 15's translator that `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` is **25** columns and does not fit. Measured with `len()` it is **23**, and `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ` is **17**, not 20. **It fits** — inside the box, at the ≤23 preferred limit. Chunk 15 is not steered away from the full form |
| 暗礁 | `ｒｅｅｆ` / `ｒｅｅｆｓ` | 4 / 5 columns. DATA 488, `かたい暗礁に　守られた` → `ｇｕａｒｄｅｄ　ｂｙ　ｈａｒｄ　ｒｅｅｆｓ，`. Verified **free** at review |
| 財産 | `ａｓｓｅｔ` | 5 columns. DATA 506, `兵士は　立派な財産` → `ｓｏｌｄｉｅｒｓ` / `ａｒｅ　ａ　ｆｉｎｅ　ａｓｓｅｔ．` Kept **distinct** from お宝 / 宝 → `ｔｒｅａｓｕｒｅ` (§32.1), 宝石 → `ｇｅｍｓｔｏｎｅ` (§33.5), 財宝 → `ｈｏａｒｄ` (§33.1) and ジュエル → `Ｊｅｗｅｌ` (§3). Verified free |
| 立派な | `ｆｉｎｅ` | 4 columns. Two instances, two messages, **one word deliberately**: DATA 506 `立派な財産` → `ａ　ｆｉｎｅ　ａｓｓｅｔ`, DATA 513 `立派な国` → `ｍａｎｙ　ｆｉｎｅ　ｃｏｕｎｔｒｉｅｓ`. Held **distinct** from 素晴らしい → `ｓｐｌｅｎｄｉｄ` (chunk 7) |
| 大陸 | `ｃｏｎｔｉｎｅｎｔ` | **9 columns.** DATA 488 and 498, both `この大陸` → **`ｔｈｉｓ　ｃｏｎｔｉｎｅｎｔ`** (14). ⚠️ **CROSS-UNIT with chunk 25, and byte-identity is NOT owed — the determiner follows the source.** `tl/battle/chunk_025.txt` L13 renders the **bare** `大陸` as `ｅｖｅｒｙ　ｐｏｒｔ　ｏｎ　ｔｈｅ` / `ｃｏｎｔｉｎｅｎｔ　ｉｓ　ｓｅａｌｅｄ．` (§41.1's 13-column `ｔｈｅ　ｃｏｎｔｉｎｅｎｔ`); this unit's two are demonstrative. **The fixed word matches in all three**, which is what §3 — engaging on the message — actually requires. Verified against the merged tree at this review. **1 battle + 6 script (banks 4, 5, 41)**; no §9 row exists, so there is nothing to strike |
| 場所 | `ｐｌａｃｅ` / `ｐｌａｃｅｓ` | 5 / 6 columns. DATA 512 `危険な場所` → `Ｂｏｔｈ　ｐｌａｃｅｓ　ａｒｅ` / `ｐｅｒｉｌｏｕｓ．`, DATA 514 `危険な場所です` → `ｉｓ　ａ　ｄａｎｇｅｒｏｕｓ　ｏｎｅ，` — **the second is carried anaphorically so the word does not repeat inside one message**, that same row also rendering 所 → `Ｔｈｅ　ｐｌａｃｅ　ｙｏｕ　ａｒｅ　ｂｏｕｎｄ`. Agrees with `tl/battle/chunk_026.txt` L1's `ｇｏｔ　ｔｈｅ　ｗｒｏｎｇ　ｐｌａｃｅ？`, verified in the merged tree. Already the shipped form for 所 (`chunk_014` L2) and inside a phrase for 辺境 (`chunk_000` L3, §23.1 — recorded, not re-cut). ⚠️ **No §9 row, and there never was one** (§AB7) |
| 司教様 | `ｔｈｅ　ｌａｔｅ　Ｂｉｓｈｏｐ　ｏｆ　Ｆａｒｉｎａ` | **Not a new reading** — §26.1 fixes 司教 → `Ｂｉｓｈｏｐ` and the man is Creus. DATA 498, `亡くなられたファリーナの司教様` → `ｔｈｅ　ｌａｔｅ　Ｂｉｓｈｏｐ` (15) / `ｏｆ　Ｆａｒｉｎａ．` (10); `亡くなられた` is carried by *the late*, which is the massacre `tl/battle/chunk_021.txt` L10 already ships (`一族` → `ｋｉｎ`, `皆殺し` → `ｓｌａｕｇｈｔｅｒｅｄ`) and chunk 24 L15 turns on |
| 宝庫 | `ｔｒｅａｓｕｒｅ‐ｈｏｕｓｅ` | 14 columns, `‐` is U+2010. **Recorded at review; the PR rendered it and proposed no row.** DATA 488, `古代文明の　宝庫` → `ａ　ｔｒｅａｓｕｒｅ‐ｈｏｕｓｅ　ｏｆ` / `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ．` **A true hapax — 1 occurrence in the whole `script_dump.txt`, bank 4, this line, and 0 battle** (counted at review). Held **distinct** from 宝 / お宝 → `ｔｒｅａｓｕｒｅ` (§32.1, battle chunk 20 only) and 財宝 → `ｈｏａｒｄ` (§33.1, battle chunk 19 only); **all three sets are disjoint in both chunks and banks**, so §25.3 is met three ways |
| 亡霊 | `ｇｈｏｓｔｓ` | 7 columns, verified free. **Recorded at review.** DATA 512, `亡霊が出る` → `ｇｈｏｓｔｓ　ｗａｌｋ` — a §2.1 **step 4** shortening the PR flags (`ａｐｐｅａｒ` is 6 and pushes the row to 25). Held distinct from 魔物 → `ｍｏｎｓｔｅｒ` and 魔族 → `ｄｅｍｏｎ` |
| 軍隊 | `ａｒｍｙ` | **Recorded at review.** DATA 506, `軍隊にとって` → `Ｔｏ　ａｎ　ａｒｍｙ，`. The generic noun, lowercase; §2's `９ｔｈ　Ａｒｍｙ` series and §20.4's `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` are untouched |
| しょうがない | `ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ` | **Recorded at review.** DATA 476/487/497, `じゃ、しょうがないわね。` → `Ｗｅｌｌ，　ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` (21). **A fifth source spelling on §24.3 / §29.3 / §32.2's family** (しかたねえ。, 仕方ない、, 仕方ねえだろ。, 仕方ないな。) — one word, several spellings, the §17.2 鬼 / オーガ shape. §25.3 counted at review: `しょうがない` banks [4, 41]; 仕方ない banks [3, 19, 20, 23] + chunks [2, 5, 6, 8, 20]; しかたねえ bank [23] + chunk [6]; 仕方ねえ bank [2] + chunk [8] — **bank 4 holds none of the others.** `じゃ、` → `Ｗｅｌｌ，` |
| 噂 (kanji) | `ｒｕｍｏｕｒ` | **Recorded at review.** DATA 512, `との噂` → `ｒｕｍｏｕｒ　ｈａｓ　ｉｔ`. §26.4 fixes the kana `うわさ` → `ｒｕｍｏｕｒｓ` (`batch_005` L43); one word, two spellings. §25.3 counted: `うわさ` is bank 31 only, `ウワサ` battle chunk 9 only, kanji `噂` banks [0,1,2,**5**,8,20,23,28,29,33,40,41] + chunk 19 — **disjoint from bank 31 and from chunk 9** |
| で、 | `Ｎｏｗ，` | **Recorded at review.** DATA 482 `で、どんな　用かしら？` → `Ｎｏｗ，　ｗｈａｔ　ｄｏ　ｙｏｕ　ｎｅｅｄ？` (22) and DATA 492 `で、どんな　ご用かしら？` → `Ｎｏｗ，　ｗｈａｔ　ｉｓ　ｙｏｕｒ　ｎｅｅｄ？` (23) — **two source strings held apart, the ご‐ politeness carried by the stiffer clause.** `Ｎｏｗ，` is §28.8's さあ、; §25.3 counted at review — `で、どんな` is **bank 4 only** and `さあ、` is banks [1, **5**, 16, 23, 24, 41, 42, 43], **so bank 4 holds neither collision.** Held distinct from さて、 → `Ｎｏｗ　ｔｈｅｎ，` (§31.3) |

### 42.2 The four `ご用` questions, and the three blessings — held apart on purpose

Four "what do you want?" openers, four different source strings, four renderings, and the register
climbs with the politeness of each: `今日は　どんなご用？` → `Ｗｈａｔ　ｂｒｉｎｇｓ　ｙｏｕ　ｔｏｄａｙ？`
(471), `で、どんな　用かしら？` → `Ｎｏｗ，　ｗｈａｔ　ｄｏ　ｙｏｕ　ｎｅｅｄ？` (482),
`で、どんな　ご用かしら？` → `Ｎｏｗ，　ｗｈａｔ　ｉｓ　ｙｏｕｒ　ｎｅｅｄ？` (492),
`今日は　何のご用か？` → `Ｙｏｕｒ　ｅｒｒａｎｄ　ｔｏｄａｙ？` (503, the King's).

Likewise the three fairy blessings, all optative `Ｍａｙ　…`, none collapsed:
`力に　なりますように！` → `Ｍａｙ　ｔｈｅｓｅ　ｆａｉｒｉｅｓ` / `ｂｅ　ｏｆ　ｈｅｌｐ` / `ｔｏ　ｙｏｕ　ａｌｌ！`
(475), `いやして　くれますように！` → `Ｍａｙ　ｔｈｅｙ　ｈｅａｌ` / … (486),
`幸運を　もたらしますように！` → `Ｍａｙ　ｓｈｅ` / `ｂｒｉｎｇ　ｌｕｃｋ` / `ｔｏ　ｙｏｕ　ａｌｌ！` (496).
And the two recruit prompts: `どの妖精が　いいかしら？` → `Ｗｈｉｃｈ　ｆａｉｒｙ　ｗｉｌｌ　ｉｔ　ｂｅ？` (23)
against the King's `どれが　よろしいかな？` → `Ｗｈｉｃｈ　ｗｏｕｌｄ　ｓｕｉｔ　ｙｏｕ？` (21).

### 42.3 ⚠️ `ｍｏｎｓｔｅｒｓ` renders 魔物 AND モンスター in ONE bank and ONE speaker's gossip

**Recorded at review; the PR did not raise it. The rendering stands and nothing is re-cut.**
Measured: `魔物` is banks **[5, 40]**, 0 battle; `モンスター` is **24 banks including 4 and 5** plus
battle chunk 31, **214 script instances**. This unit renders **both**, in bank 5, from **King
Leverk**, two gossip messages apart — DATA 512 `キエーザの沼には魔物が住む` →
`Ｍｏｎｓｔｅｒｓ　ａｒｅ　ｓａｉｄ` / `ｔｏ　ｄｗｅｌｌ…` and DATA 514 `西にはモンスターの砂漠` →
`ａ　ｄｅｓｅｒｔ　ｏｆ` / `ｍｏｎｓｔｅｒｓ．` **§25.3's test therefore fails outright and visibly**, which
is sharper than any previous instance of it.

> **Ruled: the collapse stands, and it is the documented kind.** §9's wave-6 seed fixed
> `魔物` → `ｍｏｎｓｔｅｒ` *knowing* `モンスター` → `ｍｏｎｓｔｅｒ` was already shipped
> (`batch_001` L33, and §9's own wave-5 note "**`モンスター` is NOT a seed — it is already
> SHIPPED**"), and the unit used the seed exactly. One native word and one loanword for one
> concept is precisely §17.2's 鬼 / オーガ shape — a deliberate collapse, not the flattening of a
> distinction the source draws; a player reading both lines loses nothing, because the Japanese
> draws none either. **The distinction the seed was written to protect — 魔族 / 魔物 — IS held**:
> `ｄｅｍｏｎｓ` and `ｍｏｎｓｔｅｒｓ` never meet.
>
> ⚠️ **`モンスター` cannot move** (214 instances, 24 banks, byte-bound by `batch_001`), so if a later
> unit ever needs the split it is **`魔物` that moves**, and only banks 5 and 40 are affected.
> `ｃｒｅａｔｕｒｅ` (9 columns) is verified free across `tl/` and `pending/` and is the reserve.
> **Lines this affects: none.** `FLAGS.md` §AD.

### 42.4 ⚠️ `Ｉ　ｓｅｅ．` reaches FIVE source strings, and the bank test is not what discharged it

`そう。` (DATA 481, Phyllis, **bank 4**) is a **new fifth** string on §30.3's form, beside
`なるほど` (§30.3), `そうか` (`chunk_004` L11, shipped), `そうですか` (§34.1) and `そうかい` (§38.2).
Counted at review with this unit's own keys excluded, §25.3's stated standard — *no chunk and no
bank contains both* — is **met for `そう。`**: `そうか。` banks [5, 8, 9, 29, 33, 41], `そうですか`
[0, 7, 12, 16, 41], `そうかい` [2, 12, 17, 20, 23, 24], `なるほど` [1, 5, 8, 33, 36, 40] — **not one
of them is bank 4.**

⚠️ **But bank 5 is a different matter, and the PR's "different banks, different scenes, no message
holds both" applied the wrong grain.** This unit puts `そうか。` → `Ｉ　ｓｅｅ．` into bank 5 (DATA
507, 510) and **bank 5 also holds an untranslated `なるほど`** — inside two of the big pooled strings.
The pairing is **pre-existing**, not created here: §30.3 fixed `なるほど`, `chunk_004` shipped
`そうか`, and §30.3's discharge counted **chunks only, never banks**. Nothing shipped is affected and
no line changes; it is recorded LIVE for whoever translates that pool, on the §32.5 / §34.2 / §34.5
pattern. **§25.3's reserve `Ｅｘａｃｔｌｙ．` stays reserved for `そのとおり` / `そうそう` and is not
spent here.**

### 42.5 FORWARD BINDING — four of this unit's messages have sibling unique rows outside it

Measured mechanically over all 1,430 unique lines, comparing **visible text** rather than keys.
Different `{FFF6}` / `{FFF8}` arguments make them different keys, so CLAUDE.md §3 does not *force*
reuse — but the player meets one line, which is §34.9's reasoning for unique 598.

| This unit | Japanese | Siblings outside the unit |
|---|---|---|
| **472 / 483 / 493 / 504** | the recruiter menu | **5 untranslated: DATA 329, 330, 394, 400, 412**; 3 shipped identically in `batch_007` (DATA 435, 445, 456) |
| **481** | `そう。疲れたときはいつでもよってね。` | **DATA 326, count 2, untranslated** |
| **505** | `どれが　よろしいかな？` | **DATA 535, untranslated** |
| **506** | `軍隊にとって兵士は　立派な財産。大切にされよ。` | **DATA 403, untranslated** |

⚠️ **`FLAGS.md` §Z2 numbers the same menu lines in `script_unique.txt` FILE index, exactly +5 on
these** — its 440/450/461 are these 435/445/456, and four of its "nine untranslated"
(477, 488, 498, 509) are this unit's own 472, 483, 493, 504. **§Z2 is updated at this merge.**
`HANDOFF.md` already warned that `batch_007` and `batch_008` number differently; the same clash is
now shown to reach `FLAGS.md`, so **read the header before citing any line number** binds FLAGS
entries too.

### 42.6 Register — verified line by line, not assumed

| Who | Register |
|---|---|
| **Phyllis (DATA 470–501, portrait `{=01}{=79}`)** | §14.6 unchanged and held across **all 32 lines** — formal, warm, maternal, **no contraction anywhere**: `Ｉ　ａｍ　ａｆｒａｉｄ，`, `Ｉ　ｃａｎｎｏｔ　ｒｅｃｒｕｉｔ`, `Ｗｅ　ｆａｉｒｉｅｓ　ｃａｎ　ｕｓｅ`, `ｗｅ　ｓｈａｌｌ　ｇｌａｄｌｙ　ｈｅｌｐ`, `Ｗｅｌｌ，　ｎｏｔｈｉｎｇ　ｆｏｒ　ｉｔ．` **Bank 4 contains not one apostrophe.** The source's `かしら` / `〜わ` / `〜のよ` lightness is carried in word choice, never in a contraction — §2's politeness rule. She is the same character as `pending/chunk_005.txt` L22's `Ｌａｄｙ　Ｐｈｙｌｌｉｓ` (§14.1) and is contraction-free in both |
| **King Leverk (DATA 503–516, portrait `{=01}{=7B}`)** | `予` / `おりますぞ` / `来られよ` / `よろしかろう` / `いたす` carried as plain, old-fashioned English with **no contractions and no archaic spelling** — §7's "Village elders (じゃ / のう)" column, the same one §28.6 gives chunk 13's King. `Ｉ　ａｍ　ｔｒｕｌｙ　ｇｒａｔｅｆｕｌ．`, `Ｔｒｅａｔ　ｔｈｅｍ　ｗｅｌｌ．`, `Ｄｏ　ｔａｋｅ　ｃａｒｅ．`, `Ｉ　ｅｘｐｅｃｔ　ｇｒｅａｔ　ｔｈｉｎｇｓ！` His `貴官の隊` → `ｙｏｕｒ　ｓｑｕａｄ` carries 貴官 in register, per §2 / §26.7 / §29.2 / §31.7 |
| **The Leverk retainer (DATA 502)** | Correctly **not** the King: `おられる` is honorific *about* him, so `Ｔｈｅ　Ｋｉｎｇ　ｉｓ　ａｗａｙ` / `ａｔ　ｐｒｅｓｅｎｔ．` Deferential, no contractions |

### 42.7 Recorded, not re-cut — checked at review and not defects

- **`ｙｏｕ　ｗｏｕｌｄ　ｄｏ　ｗｅｌｌ　ｔｏ　ｆｏｒｇｏ`** (DATA 509, `見送られるがよろしかろう`) reaches
  **independently** the exact frame `tl/battle/chunk_026.txt` shipped for `消え去るがいい` (§40.2's
  `ｙｏｕ　ｗｏｕｌｄ　ｄｏ　ｗｅｌｌ　ｔｏ　ｖａｎｉｓｈ`). Two units, two agents, no coordination, one
  English shape for the condescending-permission 〜がいい / 〜がよろしかろう — beside §31.3's
  `Ｙｏｕ　ｍａｙ　ｃｏｍｅ　ａｔ　ｍｅ．` for かかってくるがいい。 **Extra agreement, not a collision.**
- **`ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ　ｔｉｍｅ．`** (478/489/499) matches `batch_007` L24/47/58/69's
  `Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ　ｔｉｍｅ` **lowercased**, because it continues the sentence after
  `Ｉ　ａｍ　ａｆｒａｉｄ，`. That is §39.3 item 3's `ｍｙ　ａｐｏｌｏｇｉｅｓ．` pattern, correct.
- **`Ｄｏ　ｔａｋｅ　ｃａｒｅ．` / `！`** (512, 515) agrees with `pending/chunk_005.txt` L17 and with
  §26.7's `ｄｏ　ｔａｋｅ　ｃａｒｅ`; the `なさい` is carried by the `Ｄｏ`, not by an added word. Held
  apart from `batch_007` L27's `Ｔａｋｅ　ｃａｒｅ，　ｔｈｅｎ！` (`じゃ、気を付けてな！`, a different key
  in a different bank).
- **`Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ．`** (479/490/500) reuses `batch_007` L25's phrase with this
  line's own stop — exactly what `FLAGS.md` §Z2 anticipated ("`Ｙｏｕｒ　ｒａｎｋｓ　ａｒｅ　ｆｕｌｌ`
  appears in both").
- **`ｌｏｏｋ　ｓｈｏｒｔ　ｏｆ　Ｊｅｗｅｌｓ`** matches `batch_007` L24/47's frame, and
  **`Ｎｏｔｈｉｎｇ　ｅｌｓｅ？`** holds §38.2's negative/affirmative split without the `ノロ` tic —
  this unit contains **no ノロ at all**, correctly.
- **`残念だけど` → `Ｉ　ａｍ　ａｆｒａｉｄ，` stands and the PR's offer to force `Ｉ’ｍ　ａｆｒａｉｄ` is
  DECLINED**, on §39.7 rather than on the reviewer's judgement: `ａｆｒａｉｄ` is the fixed **word** and
  the contraction follows the speaker. `tl/battle/chunk_024.txt` L14 renders it
  `Ｉ　ａｍ　ａｆｒａｉｄ　Ｉ　ｃｏｕｌｄ` for Aries, verified in the merged tree; `chunk_011` 6.1 and
  `chunk_020` 47.3 contract because their speakers do. ⚠️ **`Ｉ’ｍ　ａｆｒａｉｄ，` is 11 columns, not
  the PR's 10** — the −6-byte cost it quotes is nevertheless right.
- **Two §2.1 departures the PR's Flag 10 did not list**, both faithful and both width-forced:
  DATA 514's `北は…砲台に守られておると聞く` → `ａ　ｂａｔｔｅｒｙ　ｒａｉｎｉｎｇ　ｆｉｒｅ` /
  `ｇｕａｒｄｓ　ｉｔ，　Ｉ　ｈｅａｒ．` flips the source's passive to an active (`ｉｔ　ｉｓ　ｇｕａｒｄｅｄ
  ｂｙ　ａ　ｂａｔｔｅｒｙ` measures **24**, which §25.1 has twice rejected); and DATA 511's fronting
  folds `中心に`'s *as its centre* into `Ｆｒｏｍ　…`, a step-5 implication as well as the step-6
  flagged (`ｔｈｅ　ｎｏｒｔｈｅｒｎ　ｇｒｅａｔ　ｆｏｒｔｒｅｓｓ` is **28**, so the fronting is genuinely
  forced).
- **Two rows end on a two-letter word** — DATA 512 row 5 (`…ｓｏｕｔｈ　ｏｆ`) and DATA 514 rows 0/1
  (`…ｂｏｕｎｄ` / `ｆｏｒ…`). Both pages already carry **four** text rows against the source's four,
  and every alternative overflows (`Ｍｅａｎｗｈｉｌｅ，　ｒｕｍｏｕｒ　ｈａｓ　ｉｔ` = 26,
  `ｏｆ　Ｋｉｅｓａ．　Ｂｏｔｈ　ｐｌａｃｅｓ　ａｒｅ` = 26); a fifth row means adding a `{FCC0}`, which
  `assemble.py:tag_parity` forbids. **Forced; they stand**, on §33.8's disposition.
- **`ｔｈｅｙ　ｓａｙ` twice in one message** (DATA 498, for `と聞きます` and `らしいわ`) is §26.6's
  stated default for every hearsay evidential, ten rows apart and in different sentences.
  `Ｗｏｒｄ　ｉｓ` was not needed.
- **Three EN-only leading `　`** (474/485/495) are the price-insert word-space §34.9 trap 3 records
  for `batch_006` L60; **18 source cursor gutters, 18 kept, 0 lost.**
- **`ｇｌａｄｌｙ` is not free** (`chunk_019` L24) and neither are `Ｎｏｗ，`, `ｅｒｒａｎｄ`, `ｐｕｓｈ`,
  `ｅｘｐｅｄｉｔｉｏｎ` or `ｔｒｕｌｙ`; all are different words in different messages, §3 not engaged,
  §25.3 met. **Genuinely free, re-measured at review**: `ｂａｔｔｅｒｙ`, `ｒｅｅｆ`, `ａｓｓｅｔ`,
  `ｇｈｏｓｔｓ`, `Ｋｉｅｓａ`, `ｐｅｒｉｌｏｕｓ`, `ｓｕｉｔ`, `ｗｅａｒｉｎｅｓｓ`, `ｗｅａｒｙ`, `Ｍｅａｎｗｈｉｌｅ`.

### 42.8 Corrections to this PR's own figures (§4.3) — five, none touching a line of the file

**Every headline figure is correct as stated** — banks, byte deltas, 47/47, 32 distinct, widest 23,
none at 24, `{FFFE}` +1 on one line, `{FCC0}` untouched — and all three of Flag 5's line-citation
corrections were re-derived independently and confirmed.

| # | Claim | Measured |
|---|---|---|
| 1 | "2,932 EN visible chars … growth **1.86×**" | **3,052 and 1.9353×.** Closes exactly on the PR's own bank deltas: `(3052−1577)×2 + 2 = 2,952 = 1,602 + 1,350` |
| 2 | `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ　Ｉｆｒｉｔ` **25**, `ｔｈｅ　ｇｒｅａｔ　ｂａｔｔｅｒｙ` **20** | **23 and 17.** ⚠️ **The only correction that changes an inherited decision** — chunk 15's full form *does* fit; see the 砲台 row |
| 3 | `Ｗｅｓｔｗａｒｄ，　ａ　ｄｅｓｅｒｔ　ｏｆ` **22** (Flag 17) | **21.** The *rejected* `Ｔｏ　ｔｈｅ　ｗｅｓｔ，　ａ　ｄｅｓｅｒｔ　ｏｆ` is **24**, exactly as stated |
| 4 | `Ｉ’ｍ　ａｆｒａｉｄ，` **10** (Flag 2) | **11.** The −6-byte figure is right |
| 5 | `ｔｈｏｓｅ　ｇｉｆｔｅｄ　ｉｎ　ｗｉｓｄｏｍ` **20** (Flag 10) | **22**; `…ｉｎ　ｍｉｇｈｔ` is 21 as stated. Conclusion strengthened |

⚠️ **§AC3's pattern holds a second wave running: every figure either party argued from was exact,
and every wrong one was a table cell typed rather than measured.** The PR itself caught one of its
own before pushing (Flag 17's `ｄｅｓｅｒｔ`), which is the practice that should generalise.

❌ **`ｄｅｓｃｅｎｄａｎｔ` is 10 columns and was not reopened.** Five parties have now measured it.

---

## 43. Added by chunk 030 (PR #27, merged 2026-09-09)

Rimul's Crimson Knights recover the tablet from the temple; Rendol is sent ahead while Rimul holds
off the 9th Army. Victory / defeat / surrender branches, plus the pig-voiced (`ブヒ`) interloper.
**7,615 / 8,192, 577 bytes slack.** Three wave-7 seeds promoted, all three used exactly as seeded;
**only one of them (`遠征軍`) is exhausted** — see §43.5.

### 43.1 RULING — `ああ` splits on REGISTER, and Rimul's assent is `Ｉ　ｄｏ．`

PR #27 renders `ああ。貴官とは決着をつけねばならん。` (Rimul, answering Kain's
`じゃあ、どうあっても戦うんだな？`) as **`Ｉ　ｄｏ．`**, departing from §6's fixed `Ｙｅａｈ`, and
flagged it. **The departure is upheld and §6's row is conditioned in place (§4.3).**

- **§6's row already scoped itself** — "Casual agreement from a rough speaker." Rimul is neither.
  Her contraction-free register is fixed at §7, §30.7 and §41.3, and §30.7 chose the written rule
  **over** shipped `chunk_000`'s contracted Rimul.
- **Every shipped `Ｙｅａｈ` is a casual, contraction-taking speaker — 13 of 13, counted
  positionally at this review.** ⚠️ **PR #27's own count was low, in its own favour**: it listed
  eight and called them six. The three it missed are `chunk_002:b7`
  (`…城へ戻らせてもらうとしようぜ。`, renders `ｌｅｔ’ｓ`), `chunk_019:b0` (`…知恵だな。`) and
  `chunk_020:b47` (`ああ、残念だけど、`). All three are casual, so **the conclusion is stronger
  than the PR argued it**: register predicts 13 of 13 with no exceptions.
- **This is the §41.4 shape exactly** — a form fixed from casual mouths that does not reach a
  contraction-free one — and §41.4's precedent is that the translator who deviates and says so is
  upheld. §36.2 (`とにかく`) and §36.3 are the same pattern.
- **`Ｙｅｓ．` was correctly avoided.** §18.3 removed exactly that string from `tl/` for ああ;
  reintroducing it would restore the divergence that correction erased. `Ｉ　ｄｏ．` is **5
  columns**, identical in cost to `Ｙｅａｈ．`, sits on a standalone row, and was verified free
  across `tl/` and `pending/` (this file's only occurrence). It also answers the question's own
  verb, which is better English than either alternative.

**Lines this affects: none.** `Ｙｅａｈ` is unchanged everywhere it already stands.

### 43.2 New terms

| Japanese | English | Note |
|---|---|---|
| 遠征軍 | `ｅｘｐｅｄｉｔｉｏｎａｒｙ　ｆｏｒｃｅ` | **Promoted from §9's wave-7 seed, used exactly as seeded — the LONG form.** 19 columns, `len()`-confirmed. **1 battle + 0 script — exhausted, and the §9 row is struck.** The licensed short `ｅｘｐｅｄｉｔｉｏｎ` (10) was not needed and is **unspent**: the row is `Ｏｆ　ｔｈｅ　ｅｘｐｅｄｉｔｉｏｎａｒｙ` (20) / `ｆｏｒｃｅ，　ｔｈｉｓ　ｉｓ　ａｌｌ．．．．` (22), keeping the source's four rows |
| 石版 | `ｔａｂｌｅｔ` | **Promoted from §9's wave-7 seed, used exactly as seeded**; 6 columns confirmed. ×3 here. ⚠️ **The §9 row STAYS LIVE** — reach re-counted at review and PR #27's figures are exact: **5 battle (30, 36) + 25 script across 21 banks**. Struck by the last unit to land, per §29.1 / §30.1 |
| クロイツェル / リムル・クロイツェル | `Ｋｒｅｕｔｚｅｌ` / `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ` | **Promoted from §9's wave-7 seed, used exactly as seeded**; 8 / 14 columns confirmed. ⚠️ **NOT a hapax — the §9 row STAYS LIVE; see §43.5.** Does not disturb §1's `リムル` → `Ｒｉｍｕｌ` or `リムル様` → `Ｌａｄｙ　Ｒｉｍｕｌ`, both used unchanged ×8 here |
| 隠れ里 | `ｈｉｄｄｅｎ　ｖｉｌｌａｇｅ` | 14 columns, **lowercase** (§17.1 species/common-noun test — it is what the place *is*, not a name). **4 battle (27, 29, 30, 32) + 2 script (bank 41, unique 1384 and 1386)** — re-counted at review, exact. Reaches three further battle chunks, so it is fixed now rather than invented three times. Verified free across `tl/` and `pending/` |
| 本国 | `ｈｏｍｅｌａｎｄ` | 8 columns. ×2 here. ⚠️ **Shares its English with 祖国 → `ｈｏｍｅｌａｎｄ`, shipped in `batch_002.tsv`.** §25.3's test was **re-counted at review and is MET**: 本国 = **5 battle [23, 30, 42] + 1 script [bank 20]**; 祖国 = **0 battle + 1 script [bank 5]**. No shared chunk, no shared bank, no shared message |
| 回収 | `ｒｅｃｏｖｅｒ` / `ｒｅｃｏｖｅｒｅｄ` | ×4 here. ⚠️ **Shares its English with 回復 → `ｒｅｃｏｖｅｒ`, shipped in `chunk_001` (an HP tutorial box).** §25.3's test **re-counted and MET**: 回収 = **4 battle [chunk 30 only] + 0 script**; 回復 = **2 battle [chunk 1] + 24 script [banks 21, 29, 40]**. Disjoint in both dimensions. *Recover the tablet* is the natural military phrasing; not forked to `ｒｅｔｒｉｅｖｅ` |
| 完敗 | `ｃｏｍｐｌｅｔｅ　ｄｅｆｅａｔ` | 15 columns. **3 battle (chunk 30 only) + 0 script** — exhausted. Verified free elsewhere |
| 敗軍の将 | `ａ　ｂｅａｔｅｎ　ｇｅｎｅｒａｌ` | 16 columns. Hapax — 1 battle + 0 script |
| 将 (in `紅の騎士団の将`) | `ｇｅｎｅｒａｌ` — **lowercase** | 7 columns. A descriptive appositive inside a self-introduction, not a title before a name, so it is held **distinct** from §26.2's 将軍 → `Ｇｅｎｅｒａｌ`. ✅ **Confirmed at review as the §32.4a pattern applied**: that gag already splits 将校 → lowercase `ｏｆｆｉｃｅｒ` from 将軍 → capitalised `Ｇｅｎｅｒａｌ` on exactly this test. Lowercase `ｇｅｎｅｒａｌ` occurs **only** in `chunk_030` (×2); capitalised `Ｇｅｎｅｒａｌ` occurs in 8 other files and is **always** a title before a name. No collision |
| ブヒ — **sentence-FINAL tic** | trailing `，　ｏｉｎｋ．` — **lowercase**, with the source's own stop | ⚠️ **A new SHAPE, not a new word — see §43.3** |
| ブヒィ (sentence-final) | `ｏｉｎｋｋ` | 5 columns. §19.1's rule is "the four `ィ` become four `ｋ`"; one `ィ` gives one `ｋ`. Lowercase per the row above; the source's `！` is kept |
| とばっちり | `ｃａｕｇｈｔ　ｉｎ　ｔｈｅ　ｃｒｏｓｓｆｉｒｅ` | `ｃｒｏｓｓｆｉｒｅ` 9 columns, verified free. Hapax. The pig is hit by a blow meant for someone else, which is exactly とばっちり |
| 心配は無用だ | `Ｎｏ　ｎｅｅｄ　ｆｏｒ　ｃｏｎｃｅｒｎ．` | 20 columns. ×2 here, byte-identical. Contraction-free per Rimul's §7 / §30.7 register. `ｃｏｎｃｅｒｎ` occurs once elsewhere (`chunk_013`, `ｎｏ　ｃｏｎｃｅｒｎ　ｏｆ　ｙｏｕｒｓ．`) — a different word in a different message |
| 好きにしろ | `Ｄｏ　ａｓ　ｙｏｕ　ｌｉｋｅ．` | 15 columns. ×2 here, byte-identical. **Recurs in chunk 27**, so the form is fixed now. Free across `tl/` |
| どうかご無事で | `ｐｌｅａｓｅ　ｂｅ　ｓａｆｅ．` | 15 columns. ×4 here, byte-identical. Held **distinct** from the past-tense enquiry `ご無事でしたか` (`pending/chunk_005` L23, and chunk 23's `フェルナンド将軍、ご無事でしたか。`) — a different construction; the shared word is `ｓａｆｅ`. ⚠️ **CORRECTED at integration: PR #27's row said "Recurs in chunk 23", and it does NOT.** Counted at review: `どうかご無事で` is **battle chunk 30 only, 4 instances, 0 script**. What chunks 5 and 23 carry is `ご無事でしたか` — the very construction this row excludes. **Chunk 23 must NOT take `ｐｌｅａｓｅ　ｂｅ　ｓａｆｅ．`**; the row as written would have pushed it there |

### 43.3 RULING — `ブヒ` sentence-final is a new SHAPE of §19.1's tic, not a new word

§19.1 fixes ブヒ → `Ｏｉｎｋ` / ブヒィィィィ → `Ｏｉｎｋｋｋｋ`, "used with the source's own stop per
the ゲロゲロ precedent (§5)". **Verified from the source at review: chunk 1's two instances are
BOTH sentence-initial** (`ブヒ。`, `ブヒィィィィ。`). Chunk 30 is the first unit where ブヒ rides the
**end** of a clause, six times (`騒がしいブヒ。`, `無かったはずブヒが。`, `石版ブヒ。`,
`ちがいないブヒ。`, `いただくブヒ。`, `渡さんブヒ。`).

> **Ruled: sentence-INITIAL `ブヒ、` / `ブヒ！` keep §19.1's capitalised `Ｏｉｎｋ` plus the source's
> own punctuation. Sentence-FINAL ブヒ takes §5's ノロ mechanism — appended to the final clause,
> lowercase, comma-prefixed, replacing that sentence's own stop, mechanical so repeats stay
> byte-identical.** 4 columns either way.

This composes §19.1's *word* with §5's *placement*; it does not compete with either.
`translation_prompt.md` §5's ゲロゲロ worked example states the principle in as many words — "what
is fixed is the **word**; the punctuation follows the source … the two rules compose, they do not
compete." Chunk 30 renders 3 initial (capitalised) and 6 final (lowercase), correctly split.
**Chunk 1 is untouched and needs no revisiting.**

### 43.4 RULING — `争い` takes `ｓｔｒｉｆｅ`; `ｃｏｎｆｌｉｃｔ` is refused, and `batch_008` diverges

PR #27 offered `ｃｏｎｆｌｉｃｔ` as a third, scale-selected form and asked for a ruling. **Refused,
and the PR under-stated its own case.** This is not a choice between two shipped forms:

- **`争い` → `ｓｔｒｉｆｅ` is a FIXED ENTRY at §38**, which holds it distinct from 戦乱 → *war* and
  戦闘 → *battle* explicitly, and it ships at `batch_007.tsv` L67 (`Ｓｔｒｉｆｅ　ｉｓ　ｏｖｅｒ　ｆｏｒ　ｎｏｗ`)
  and `chunk_024` L14. Minting a third form would be a silent change to a fixed entry, which §4.3
  forbids. `ｃｏｎｆｌｉｃｔ` occurs nowhere in `tl/` or `pending/` and stays unspent.
- Reach re-counted at review, and PR #27's figures are exact: **4 battle (23, 24, 30, 32) + 10
  script across 7 banks (1, 3, 4, 21, 23, 33, 41)**.

⚠️ **A pre-existing divergence, recorded and NOT charged to PR #27.** `tl/script/batch_008.tsv`
L55 renders `知に長けた者と力に長けた者の　争いは` as `Ｔｈｅ　ｗａｒ　ｏｆ　ｔｈｅ　ｗｉｓｅ　ａｎｄ`
`ｔｈｅ　ｓｔｒｏｎｇ` — `ｗａｒ` for 争い, against §38's fixed entry, and §42 registers no row for it.
It is **live rather than harmless**: counted at this review, **争い and 戦乱 co-occur in bank 3**,
which is precisely the collision §38 held them apart to avoid. A corrections unit owes `batch_008`
L55 the re-cut; `FLAGS.md` §AE carries it.

### 43.5 CORRECTION (§4.3) — `クロイツェル` is NOT exhausted and its §9 row stays live

PR #27's glossary row read "Hapax — 1 battle (this chunk) + 0 script, so the row is struck
outright", and the reviewer's own dispatch repeated it. **Both are wrong.** Counted at review over
**both** dumps: **1 battle (chunk 30) + 1 script — bank 41, `script_unique` line 1391** — and the
script instance is the same construction chunk 30 renders:
`紅の騎士団の将、リムル・クロイツェルだな？`. A later script batch will render `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ`
and must match byte-for-byte, so the §9 row is struck by **that** unit.

**No rendering changes** — `Ｋｒｅｕｔｚｅｌ` / `Ｒｉｍｕｌ　Ｋｒｅｕｔｚｅｌ` are correct as shipped and both
widths (8 / 14) were re-measured and confirmed. Only the *exhaustion* claim was wrong.

⚠️ **The pattern is §41.4's item 1 in a new place: a reach count that looks at the battle dump and
not at the script one.** The wave's other two seeds were counted correctly over both — `遠征軍`
genuinely is 1 battle + 0 script and **is** struck, and `石版`'s 5 battle + 25 script / 21 banks is
exact. **`石版`'s unique-line ids are corrected in §9**: they are `script_unique` **305, 574 and
576**, not the "569/571" the §9 row and PR #27's Handoff both carried; **305**
(`軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`) was named by neither.

### 43.6 Confirmed without change

- **`どうやら` per §41.4**: all four instances in this chunk are Rimul's and all four take a `seem`
  clause. In `どうやら〜ようだ` the source has **one** evidential frame and English takes **one**
  `seems`; doubling it would read as two hedges. Correct.
- **`お前は・・・` → `Ｙｏｕ　ａｒｅ．．．`, not `chunk_006` L08's `Ｙｏｕ’ｒｅ．．．`.** Same segment,
  different speaker, different message — §3 is not engaged and §30.7's register is. Confirmed at
  review, and it is one of only **two** cross-file row-level exposures this unit has (the other is
  §43.1's ああ); both are declared in the PR.
- **`我々は、` is a row-initial fragment of four different sentences** here (`敵国の兵同士だぞ！`,
  `後から必ず戻る！` ×2, `カーライン第９軍に投降する。`). All open `Ｗｅ`; the predicates differ
  because the sentences do. The two that ARE the same sentence get byte-identical English. **Not a
  §3 violation** — §3 engages on the message.
- **`王子たち` → `Ｔｈｅ　Ｐｒｉｎｃｅｓ`** matches §41.6, which names chunk 25's referential form.
- **`FLAGS.md` §L2 confirmed from inside the chunk and not "fixed"** — file line 23 carries no
  `{FC50}`/`{FC51}` at all and 8 text rows; file line 21 has 5 rows with no channel tag after its
  `{FC30}`. Both inherited exactly (8 in / 8 out, 5 in / 5 out), verified against a pristine
  extraction. Still needs the in-game visit §L2 asks for.

---

## 44. Added by chunk 036 (PR #25, PARKED 2026-09-09)

⚠️ **The unit is PARKED, and the entries below are still binding.** `pending/chunk_036.txt` is a
finished, faithful, format-clean translation blocked by a tooling defect (`FLAGS.md` §AF), not by
anything in its own text. Every rendering here was reviewed line by line against the Japanese and
every term below is fixed from now on, exactly as if the file had shipped — a park is a placement
decision, not a lower standard.

**What chunk 36 is.** Of 986 source characters only **174 are dialogue**. The rest is a full-width
MIPS assembly listing, already-English machine output (`＞ＴＡＲＧＥＴ　ＲＥＣＯＧＮＩＺＥＤ`,
`＞ＳＥＣＲＥＴ　ＣＯＤＥ　ＣＯＮＦＩＲＭＥＤ`, `＞ＯＫ`) and a deliberate garbage block, **all of it
preserved byte-for-byte** — verified at review by diffing against a pristine `split_battle`
extraction: 9 of 10 body lines identical (including the 884-character MIPS listing), 23 replaced
runs on the tenth, **every one Japanese on the source side**, 1,154 characters carried through
unchanged, and the only residual Japanese anywhere in the file is `ケ` and `あ` inside the garbage
block.

### 44.1 New terms

| Japanese | English | Note |
|---|---|---|
| 『かげの石版』 | `“Ｓｈａｄｏｗ　Ｔａｂｌｅｔ”` | **Promoted from §9's wave-7 seed, used exactly as seeded. 13 columns bare, 15 with the §12 quotes** — both re-measured with `len()` at review, both exact. ⚠️ **THE §9 ROW STAYS LIVE**: `tl/script/batch_009.tsv` (PR #28) is the third unit of this wave to render it and is unreviewed. Struck by the **last** to land, per the `ルート` precedent (§29.1 / §30.1). §Y2's mixed-script check was done and is clean — `かげ` = *shadow* is battle chunk 36 and script DATA 569 **only**; every other battle `かげ` is `おかげ` (chunk 8), `影` is 0 battle, and all 4 battle `カゲ` are `トカゲ` → `ｌｉｚａｒｄ` (§2) |
| 石版 (inside the proper name) | `Ｔａｂｌｅｔ` | **Seed used exactly**; bare `ｔａｂｌｅｔ` = **6 columns**. ⚠️ **Chunk 36 renders 石版 ONLY inside `『かげの石版』`**, so the bare lowercase form is untouched here. ✅ **Cross-unit check done against the MERGED tree, not a report**: `tl/battle/chunk_030.txt` (merged `9548e73`) renders bare `石版` as lowercase `ｔａｂｌｅｔ` in all four places (`ｔｈｅ　ｔａｂｌｅｔ　ｅｎｓｈｒｉｎｅｄ`, `ｒｅｃｏｖｅｒｅｄ　ｔｈｅ　ｔａｂｌｅｔ！`, `ｔｈｅ　ｔｒｕｔｈ　ｏｆ　ｔｈａｔ　ｔａｂｌｅｔ`) and **never renders the proper name**. The two units are complementary, not divergent. **§9's row STAYS LIVE for PR #28** |
| 主人 (of a servant to the one it serves) | `ｍａｓｔｅｒｓ` | 8 columns. **First rendering in the project** — 主人 is battle chunks **32 and 36**, and 32 is tier-A blocked. ⚠️ **`ｍａｓｔｅｒ` is NOT free and the PR did not claim it was**: `chunk_012` ships 師範 → `ａ　ｍｅｒｅ　ｍａｓｔｅｒ　ｏｆ　ａ　ｔｏｗｎ　ｄｏｊｏ`, `batch_001` ships 騎士 → `ｍａｓｔｅｒ　ｏｆ　ｒｉｄｉｎｇ　ａｎｄ　ｃｏｍｂａｔ` and the §4 class name `Ｂｅａｓｔ　Ｍａｓｔｅｒ`, `chunk_000` has `ｍａｓｔｅｒｐｉｅｃｅ`. **§25.3's chunk test is met** (師範 is chunk 12 only). Four distinct source words on one English head word in four visibly different phrases; no distinction the source draws is flattened. ⚠️ **FORWARD BINDING, added at review — the PR did not name it**: script `ご主人様は　ただいま外出しておられます。` and `ご主人様がいなくなって` are the **same sense** and should take `ｍａｓｔｅｒ` when a batch reaches them |
| 認める (X を Y と) | `ｒｅｃｏｇｎｉｓｅ　Ｘ　ａｓ　Ｙ` | 9 columns. **Verified free across `tl/` and `pending/` at review** — 0 prior occurrences. British `‑ｓ‑` per §4. ⚠️ **The source's own preserved `＞ＴＡＲＧＥＴ　ＲＥＣＯＧＮＩＺＥＤ` two screens earlier is almost certainly the joke** (認める / RECOGNIZED, 仲間にしてほしい / ACCEPTED). The echo survives in the **word**; the spelling cannot match, because the American form is preserved source and §4 fixes translation as British. **Do not "fix" either side.** 1 battle + 2 script |
| だって (causal, sentence‑initial) | `Ｂｅｃａｕｓｅ` | 8 columns, **verified free**. Held apart from the **quotative** `だって`, already shipped as `ｔｈｅｙ　ｓａｉｄ` (`chunk_004`, `〜だって話だが`) and `ｔｈｅｙ　ｓａｙ．` (`batch_005`, `〜だってよ`). **This one chunk carries both senses**, so they could not have collapsed |
| ・・・だって。 (quotative report tag) | `．．．ｏｒ　ｓｏ　ｉｔ　ｓａｙｓ．` | 17 columns. Keeps §26.6's family verb *say* with the singular subject the scene requires — the reporter is a machine, not people — so it sits beside `ｔｈｅｙ　ｓａｙ` rather than colliding with it. Dot count 3 = 3 |
| そういうもんかな | `Ｉｓ　ｔｈａｔ　ｈｏｗ　ｉｔ　ｉｓ` | 17 bare, 21 with the source's four stops. A **new そう‑ form**, deliberately held apart from all five already fixed: `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．` (§23.2 / §25.2 / §30.3), `Ｔｈａｔ’ｓ　ｔｒｕｅ．` (§25.2), `Ｙｏｕ’ｒｅ　ｒｉｇｈｔ．` (§32.2), `Ｉ　ｓｅｅ．` (§30.3, §34.1, §38.2, §42.4), `Ｙｅｓ，` (§34.2). **Hapax — 1 battle, 0 script.** Interrogative syntax under the source's `。` per §36.8 / §37.7 |
| 目の光 | `ｔｈｅ　ｌｉｇｈｔ　ｉｎ　（ｉｔｓ）　ｅｙｅｓ` | Hapax — 1 battle, 0 script |

**Reuses, recorded not claimed as new** — `ティミー` → `Ｔｉｍｍｙ` (§11.1) · `ごめんなさい。` →
`Ｉ’ｍ　ｓｏ　ｓｏｒｒｙ．` (§34.1, byte-exact) · `あ、` → `Ａｈ，` (§6) · `でも、` → `Ｂｕｔ，`
(§23.3) · `きっと` → `ｓｕｒｅｌｙ` (§33.6) · `仲間` → `ｃｏｍｒａｄｅ` (§28.2) · `やさしい` →
`ｇｅｎｔｌｅ`, matching `chunk_007`'s `そのやさしい心` → `ｔｈａｔ　ｇｅｎｔｌｅ　ｈｅａｒｔ` ·
`『…』` → `“…”` (§12) · `とりあえず` → `Ｆｏｒ　ｎｏｗ` (§44.2).

### 44.2 RULING — `とりあえず` takes bare `Ｆｏｒ　ｎｏｗ` here, and the comma is the SOURCE's to give

`tl/battle/chunk_004.txt` and `chunk_025.txt` both ship `とりあえず、` → `Ｆｏｒ　ｎｏｗ，`, and
`chunk_019.txt` ships `よし、とりあえず、` → `Ｒｉｇｈｔ，　ｆｏｒ　ｎｏｗ，`. Chunk 36 ships bare
`Ｆｏｒ　ｎｏｗ` and **that is not a divergence.**

**Census re-run over the whole battle dump at review — 13 occurrences in 9 chunks:**

| Shape | Count | Chunks |
|---|---|---|
| `とりあえず、` — ends its row with the source's comma | **7** | 4, 19, 25, 28 ×3, 31 |
| `とりあえず…` — runs straight on into its clause on the same row | **5** | 18 (`手駒は`), 23 ×2 (`王子を`), 43 ×2 (`動いたから、`) |
| **`とりあえず{FFFE}` — ends its row with NO comma** | **1** | **36 only** |

`translation_prompt.md` §5's worked example (`ゲロゲロ` under `！`) fixes the **word** and takes the
punctuation **from the source**; the two rules compose, they do not compete. Adding a comma the
source does not have would be the error. **Lines this affects: none.**

⚠️ **`Ｆｏｒ　ｎｏｗ，` is not exclusively `とりあえず、`'s** — `chunk_024` renders `ここは、ひとまず`
as `Ｆｏｒ　ｎｏｗ，　ｉｔ　ｗｏｕｌｄ　ｂｅ`. Chunk 24 holds no `とりあえず`, so §25.3's chunk test is
met, and chunk 36's bare form collides with neither. Recorded at review — the PR's Flag 6 did not
name chunk 24 — so it cannot drift.

### 44.3 The speaker reading, and the portrait-id trap chunk 36 sets

Derived **inside the chunk from the tag stream**, per `FLAGS.md` §W5 and §41.2:

| Tag | Who | Register |
|---|---|---|
| `{FCB0}{=00020001}` on `{FC51}` | **Timmy** — named vocatively by the other speaker on the very next turn (`ティミー、`), and the one who translates and then confesses | §23.5: young, contractions (`ｉｔ’ｓ`, `Ｉ’ｍ`), `Ａｈ，` |
| `{FCB0}{=00000001}` on `{FC51}` | an unnamed 9th Army companion | §7 casual, contractions |
| `{FCB0}{=00070000}` on `{FC50}` | **the machine** | preserved source; no register |

⚠️ **§23.5 fixes Timmy on portrait 0007, and in chunk 36 portrait 0007 is the MACHINE.** Carrying
§23.5's id across chunks would have attributed the garbage block and the MIPS listing to Timmy.
The channel and the vocative decide, not the id — §41.2's ruling, and chunk 36 is its sharpest
instance yet. **This reading is scoped to chunk 36 and is not carried elsewhere.**

**The quoted fake translation is the one uncontracted passage in the chunk**
(`“Ｉ　ｒｅｃｏｇｎｉｓｅ　ｙｏｕ　ａｓ　ｍｙ　ｍａｓｔｅｒｓ．　Ｉ　ｗｉｓｈ　ｔｏ　ｂｅ　ｙｏｕｒ　ｃｏｍｒａｄｅ．”`)
— Timmy performing a machine, which is what makes it read as a quotation rather than as her own
voice. Deliberate, correct, and **not** a register inconsistency.

### 44.4 Recorded, not re-cut — checked at review and not defects

- **`今のは、ウソだけど。` → `Ｗｈａｔ　Ｉ　ｊｕｓｔ　ｓａｉｄ` / `ｗａｓ　ａ　ｌｉｅ，　ｔｈｏｕｇｈ．`**
  moves the comma: the source's topic `、` is dropped and a `，` appears before `ｔｈｏｕｇｈ`. Counts
  are 1 comma + 1 stop either way. English cannot put a comma between subject and verb, and §2
  names **topic-comment inversion** as a licensed departure. **§31.4 is not engaged** — that ruling
  governs the comma after a *fixed assent word*. `今のは` is rendered (*what I just said*), not
  dropped to a bare demonstrative.
- **`さっきより` moves to the end** (`ｇｅｎｔｌｅｒ　ｔｈａｎ　ｂｅｆｏｒｅ．`) — the English
  comparative's own word order, a §2 grammatical necessity, **not** a §2.1 step-6 reorder. §40.6's
  `さっきの奴ら` → `Ｔｈｅ　ｏｎｅｓ　ｆｒｏｍ　ｊｕｓｔ　ｎｏｗ` is a different construction and is
  undisturbed.
- **`ｓｈａｄｏｗ` is not free lowercase.** `batch_003` and `batch_004` spend it on 闇 / 暗黒
  (`ａ　ｄｒａｇｏｎ　ｏｆ　ｓｈａｄｏｗ`, `ｓｈａｄｏｗ　ｐｏｗｅｒ`, `ａ　ｓｈａｄｏｗ　ｂｏｗ`). Chunk 36's is
  **capitalised inside a quoted proper name** for `かげ`. Different source words, different case,
  different store, no shared chunk or bank. Recorded at review; the PR did not raise it.
- **Two rows end in a lone two-letter word** (`…ｗｈａｔ　ｗｅ`, `“Ｉ　ｒｅｃｏｇｎｉｓｅ　ｙｏｕ　ａｓ`),
  which §3.2 cautions against "if it can be avoided", and both **are** avoidable at zero byte cost
  (`ｂｕｔ　Ｉ　ｗｏｎｄｅｒ　ｗｈａｔ` 17 / `ｗｅ　ｄｏ　ａｆｔｅｒ　ｔｈｉｓ．` 17). **Raised at review and
  withdrawn on a census: 170 such rows exist across 24 of the 27 shipped battle chunks**,
  `chunk_030` included. Requiring it of chunk 36 would hold one unit to a standard no merged unit
  has met. **If the project wants the tighter rule it is a corrections-unit decision, not a single
  reviewer's on a single PR.**
- **Ellipsis dot counts are exact**: source `・・・` ×3 → `．．．`, `．．．`, `．．．．`. The four is
  `・・・。`, which **§3.1 spells out as four**. Zero `・`, `…`, `○` or ASCII in the delivered file.
- **Both `>4`-row pages are inherited**, byte-identical to a pristine extraction (45 and 33 rows),
  and are already enumerated in `FLAGS.md` §D2, which lists chunk 36 by name.

### 44.5 CORRECTION to §9 and §43.2 (§4.3) — the `石版` line ids are a CONVENTION difference, not an error

`FLAGS.md` §AE5 and §9's `石版` row both record that the script instances are "**305, 574 and 576**
— 574/576 right, 569/571 wrong". **Measured directly on `dumps/script_unique.txt` at this review:
the first data row is FILE 6, so FILE = DATA + 5**, and `石版` occurs at

> **DATA 300 / 569 / 571  =  FILE 305 / 574 / 576**

**569/571 and 574/576 are the same two lines in two conventions. Neither was wrong.** The substance
of §AE5 stands and is valuable — there genuinely is a **third** instance (DATA 300 / FILE 305,
`軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`) that no row had named. Only the "wrong"
verdict is withdrawn. `FLAGS.md` §AD5 flagged this exact convention clash one wave earlier and it
recurred immediately.

**§9's two rows were internally inconsistent** — the `石版` row listed FILE numbers while the
`『かげの石版』` row directly beneath it listed DATA 569 for the same physical line. Both now carry
an explicit convention label. **The reach itself is unchanged and exact: 5 battle (chunks 30, 36)
+ 25 script instances across 21 banks. No rendering changes; no translated line needs revisiting.**

### 44.6 Register

| Who | Register |
|---|---|
| Timmy (chunk 36, `{FCB0}{=00020001}`) | §23.5 confirmed in a second chunk: young, contracts freely, reasons from what she sees (`Ｂｅｃａｕｓｅ　ｔｈｅ　ｌｉｇｈｔ　ｉｎ　ｉｔｓ　ｅｙｅｓ　ｈａｓ　ｇｒｏｗｎ　ｇｅｎｔｌｅｒ`). **Drops contractions only inside the quoted machine voice** |
| The 9th Army companion (chunk 36, `{FCB0}{=00000001}`) | §7 unchanged — casual, contractions (`ｉｔ’ｓ　ｇｏｏｄ　ｗｅ　ｂｅａｔ　ｉｔ`, `Ｗｈａｔ’ｓ　ｉｔ　ｓａｙｉｎｇ`), musings under the source's `。` rather than questions |
| The machine (`{FC50}`) | preserved source. **Not translated, not translatable, and not to be "tidied"** |

---

## 45. Added by chunk 031 (PR #26, merged 2026-09-09)

Seven §9 wave-7 seeds promoted, **every one used exactly as seeded**, and every seeded width
confirmed correct with `len()`. Four new forms, one extended tic, one structural ruling, three
§4.3 corrections. Two review rounds; the single round-1 finding is described at §45.2.

### 45.1 Promotions out of §9 — seven wave-7 seeds, all as seeded

| Japanese | English | Note |
|---|---|---|
| カイザード | `Ｋａｉｚａｒｄ` | **7 columns**, confirmed. The imperial officer who runs the summoning. **Rendered only in the honorific form below** — the bare name is not spent anywhere yet |
| カイザード様 | `Ｌｏｒｄ　Ｋａｉｚａｒｄ` | **12 columns**, confirmed. ×4, byte-identical. 様 → **Lord** on the §1 ヘルファー様 / §28.1 アーバイン様 / §32.1 ギルフォード様 male-superior precedent, **not** §21.2's さん rule |
| ジュエルビースト | `Ｊｅｗｅｌ　Ｂｅａｓｔ` | **11 columns**, confirmed. ×2, capitalised as a creature **name**. §3's ジュエル → `Ｊｅｗｅｌ` is untouched, and the **currency** sense ships two messages later as `Ｊｅｗｅｌｓ` — the two senses stand side by side in one chunk and stay apart by capitalisation and context |
| カーバンクル | `Ｃａｒｂｕｎｃｌｅ` | **9 columns**, confirmed. ×2. Held visibly distinct from `Ｊｅｗｅｌ　Ｂｅａｓｔ`: `いや、カーバンクルとは少し違うようだが・・・。` → `Ｎｏ，　ｉｔ　ｌｏｏｋｓ　ａ　ｌｉｔｔｌｅ` / `ｄｉｆｆｅｒｅｎｔ　ｆｒｏｍ　ａ` / `Ｃａｒｂｕｎｃｌｅ．．．．` — the name is kept on the row rather than pronominalised, so the contrast the scene turns on survives |
| 『闇の紋章』 | `“Ｅｍｂｌｅｍ　ｏｆ　Ｄａｒｋｎｅｓｓ”` | **18 bare / 20 quoted — the seed is CORRECT**, re-measured at review. `『…』` → `“…”` per §12. Ships at 21 with its stop, alone on the row §45.2's rule freed. The `Ｄａｒｋ　Ｅｍｂｌｅｍ` alternative is **unspent** |
| 冥界の王 | `ｔｈｅ　Ｎｅｔｈｅｒｗｏｒｌｄ　Ｋｉｎｇ` | **20 columns — the seed is CORRECT**; `ｔｈｅ　Ｋｉｎｇ　ｏｆ　ｔｈｅ　Ｕｎｄｅｒｗｏｒｌｄ` measures **26** and cannot share a row. ×3: two take `ｏｕｒ` for `我らが` (20), the third is a vocative (§45.8) |
| リッチ | `Ｌｉｃｈ` | **4 columns**, confirmed. A transcription, not a choice — the game spells it itself in this chunk's own incantation (§45.7) |
| 召喚の儀式 | `ｓｕｍｍｏｎｉｎｇ　ｒｉｔｕａｌ` | **16 columns**, confirmed. **1 battle + 0 script — exhausted and struck.** `ｓｕｍｍｏｎｉｎｇ　ｒｉｔｅ` unspent |

**Inherited without change, verified at review:** `紅の騎士団` → `Ｃｒｉｍｓｏｎ　Ｋｎｉｇｈｔｓ` · `本隊` → `ｔｈｅ　ｍａｉｎ　ｆｏｒｃｅ` · `カーライン軍` → `ｔｈｅ　Ｃａｒｌｉｎｅ　ａｒｍｙ` (matching `chunk_009` and `pending/chunk_017`) · `帝国軍` → `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` (§20.4 default) · `リムル将軍` → `Ｇｅｎｅｒａｌ　Ｒｉｍｕｌ` (§26.2) · `宝石` → `ｇｅｍｓｔｏｎｅ` (§33.5, as that ruling directed) · `小娘` → `ｔｈａｔ　ｇｉｒｌ` (§41.1) · `３号機` → `Ｕｎｉｔ　３` (§4) · `アンデッドモンスター` → `ｕｎｄｅａｄ　ｍｏｎｓｔｅｒ` (§42.3; the reserved `ｃｒｅａｔｕｒｅ` is **not** spent — verified free of this unit, and deliberately avoided at `生者というものは` → `Ｔｈｅ　ｌｉｖｉｎｇ　ａｒｅ　ｔｈｉｎｇｓ`) · `よし。` → `Ｒｉｇｈｔ．` and `よし、` → `Ｒｉｇｈｔ，` (§24.3) · `確かに、` → `Ｔｒｕｌｙ，` (§28.2) · `ああ` → `Ｙｅａｈ` (§6 / §43.1, casual speaker) · `はっ！` → `Ｓｉｒ！` · `いや、` / `いえ、` → `Ｎｏ，` (§25.2) · `ほう、` → `Ｏｈ，` (§24.4) · `そうですか。` → `Ｉ　ｓｅｅ．` (§34.1 / §42.4) · `しかし、` → `Ｈｏｗｅｖｅｒ，` ×2 (§23.3) · `かまいません` → `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ` (§32.2) · `どうやら、` → a `seem` clause (§41.4) · `〜さん` on a name → dropped (§21.2).

### 45.2 RULING — a page's source-blank TRAILING segment may carry text, and a shape census is what settles it

Chunk 31 buys a text row on **seven** pages by redistributing text into a trailing segment the
Japanese left blank. **No tag is added, moved or deleted** — `{FFFE}` count and order are identical
on every line, the slot count per page is unchanged (2→2, 3→3, 4→4, 5→5), and the physical row
budget is therefore identical: a blank row becomes a filled row. The translator declared it the
only structural liberty in the file and asked for an explicit ruling. **It is ratified**, and the
ground is a census run over all 44 pristine chunks at review:

| shape | occurrences in `dumps/battle_dump.txt` |
|---|---|
| `TTTT` | **389** — the commonest page shape in the game |
| `TTT.` | 276 |
| `TT` | **262** |
| `.TTTT` | **182** |
| `.TTT.` | 132 |
| `TTT` | **115** |
| `TT.` | 98 |
| **`.TTTT.`** | **0** |

> **Ruled: a page's source-blank trailing segment MAY carry text, where no tag is added, moved or
> deleted and the resulting shape is attested in the pristine dump.** It buys a row for **0 bytes**
> against `{FFFE}`'s 2, and is strictly weaker than the re-flow §1 already licenses. It does **not**
> license the reverse — blanking a source text row — nor filling a trailing blank on a page that
> already carries four text rows.

⚠️ **§3.2's warning is about `.TTTT.` and is correct: that shape has 0 occurrences.** It does
**not** reach `.TTTT`, which has 182. Filling a trailing blank moves *away* from the never-attested
shape, not toward it. **This distinction cost a review round.** The PR's Flag 4 read §3.2 as
barring a fourth text row under a leading blank, and therefore compressed `百戦錬磨の将とはいえ、`
(*a general tempered in a hundred battles*) to `Ａ　ｖｅｔｅｒａｎ　ｇｅｎｅｒａｌ，　ｙｅｔ` as a §2.1
step-4 shorter synonym. With the census in hand the constraint vanished, and with it the licence:
§2 is literal-first and §2.1's ladder is conditioned on *“When a chunk is over budget”* — this
chunk had **2,837 bytes of slack**. The image is load-bearing, since Kaizard grants Rimul a
*hundred battles* precisely in order to reduce her to *that girl*. **Round 1 required the change;
round 2 applied it verbatim**, at +44 bytes:

```
{FCC0}{FFFE}Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ　ａｔ　ａｌｌ．{FFFE}Ａ　ｇｅｎｅｒａｌ　ｏｆ　ａ　ｈｕｎｄｒｅｄ{FFFE}ｂａｔｔｌｅｓ　ｔｈｏｕｇｈ　ｓｈｅ　ｉｓ，{FFFE}ｉｎ　ｔｈｅ　ｅｎｄ，　ｔｈａｔ　ｇｉｒｌ．{FCC0}
```

Rows 22/22/22/22, page `.TTT.` → `.TTTT`, 5,355 → **5,399 / 8,192**. **No §2.1 compression remains
in the file.**

### 45.3 RULING — `おや。` takes `Ｏｈ？`, and source-punctuation-wins does NOT reach おや

Chunk 31's source is `おや。`, with a full stop; §24.4's other three census instances (chunks 1, 2
and 35) are all `おや？`. §24.4 merged おお and ほう / ほお onto `Ｏｈ` **plus the source's own
punctuation**, so the question is whether that mechanism generalises. **It does not.**

§24.4's own resolution preserves that “§18.2's split therefore **separates おや and あ、 cleanly**”
— and the only thing separating おや from ほう is the `？`. Reading source-punctuation-wins into it
gives `おや。` → `Ｏｈ．`, which is exactly what `ほう。` would give, undoing the one separation §24.4
kept while merging the other two.

> **Ruled: the `？` in おや → `Ｏｈ？` is a FIXED DISCRIMINATOR, not inherited punctuation.** §5's
> word-plus-source-stop mechanism is scoped to おお / ほう / ほお (§24.4), ゲロゲロ and ノロ (§5) —
> it does not reach おや. `Ｏｈ？` renders every おや whatever stop the source gives it.

§35.3 corroborates: it had already identified chunk 31's instance as `おや。` and still counted
`Ｏｈ？` as spent for おや at all four occurrences. The English reads correctly — `Ｏｈ？` /
`Ｈａｓ　Ｇｅｎｅｒａｌ　Ｒｉｍｕｌ` / `ｆｉｎａｌｌｙ　ａｒｒｉｖｅｄ？` — and `ほう、そうですか。` →
`Ｏｈ，　Ｉ　ｓｅｅ．` sits two messages away in the same file without colliding. **Lines this
affects: none.**

### 45.4 CORRECTIONS (§4.3) — three, and none touches a line of any file

1. **`ｇｅｍｓｔｏｎｅ` is 8 columns and `ｇｅｍｓｔｏｎｅｓ` is 9, not 9 and 10.** Two cells stated the
   same wrong number and **both are patched in place**: §32.1's row (“9 / 10 columns”) and §33.1's
   row (“9 columns”). ⚠️ **The second cell is in §33.1's promotions table, not in §33.5's prose** —
   §33.5 carries no column figure at all; both the PR and the wave dispatch mis-attributed it, and
   only the line number was right. Flagged by the translator, confirmed with `len()`. No rendering
   changes, and the error is in the safe direction — the form is 1 column *cheaper* than believed.
2. **§32.7's `ふふ` census counts substrings, not laughs.** Its “8 battle (20, 28, **31 ×5**, 33)”
   overstates chunk 31, which has **three** ふ-runs — `ふふふ`, `ふふふふ`, `ふふふふふ`. Their
   non-overlapping `ふふ` substring count is 1 + 2 + 2 = **5**, which is the figure recorded. The
   §35.2 shape in a new place. Nothing turns on it — all three are rendered.
3. **§41.4's census was short by one when written, and the battle side is now 13 of 13.** Counted
   at this review over the whole battle dump: **19 `どうやら` occurrences — 13 rendered, 6
   untranslated** (chunks 15 ×3, 16 ×1, 23 ×2). §41.4's table listed **8** and missed
   **`chunk_008` line 14** (`いや、どうやら戻ってきたみたいだぞ。` → `Ｎｏ，　ｉｔ　ｌｏｏｋｓ　ｌｉｋｅ…`,
   a casual `みたいだぞ` speaker, on the correct side), so it was 9 of 9 when written. With chunk
   30's three and chunk 31's one it is now **13 of 13** — *seem*: c2 ×3, `pending/c17`, c25, c30 ×3,
   c31; *looks*: c8, c14, c19, c26. ⚠️ **But “with no exceptions” is still wrong, because the count
   was battle-only**: `batch_005.tsv` renders a plainly casual speaker (`俺たち`, `ラッキーだぜ`, and
   an English `ｈａｓｎ’ｔ`) as `，　ｉｔ　ｓｅｅｍｓ　ｗｏｒｄ　ｏｆ　ｕｓ　ｈａｓｎ’ｔ　ｒｅａｃｈｅｄ…`.
   Shipped, pre-existing, **no rendering changes** — the same forward-not-backward count §41.4
   itself criticised in §33.2, one section later. **Lines this affects: none.**

### 45.5 New forms first fixed here

| Japanese | English | Note |
|---|---|---|
| ふふふ / ふふふふ / ふふふふふ | `Ｆｕｆｕｆｕ` / `Ｆｕｆｕｆｕｆｕ` / `Ｆｕｆｕｆｕｆｕｆｕ` | 6 / 8 / 10 columns. **Extends §12.3's fixed `ふふ` → `Ｆｕｆｕ` beat for beat**, on §11.5's stated mechanism for `フハハハ` → `Ｆｕｈａｈａｈａ` — *“length tracks the source's kana count”* — the same derivation §9's `オーホホホ` → `Ｏｈｏｈｏｈｏ` seed already uses. Punctuation follows the source per §5, as shipped `chunk_025` does (`フフ・・、` → `Ｆｕｆｕ．．，`). ⚠️ **§12.3's Alt `Ｈｅｈ　ｈｅｈ` is a REJECTED option, not a menu.** Both kana scripts grepped per the §Y2 blind spot |
| 何だって？ | `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` | 14 columns. **A third spelling on §6's 何だと？ / なんだと？ row**, which already collapses two spellings of one expression. ⚠️ **See §45.6 — this leaves a LIVE bank pairing** |
| あーっ、 | `Ａｈｈ，` | 4 columns. **Collapsed onto §33.2's ああっ、 → `Ａｈｈ，`** — one lengthened あ plus a glottal cut either way, the ー/あ difference orthographic only. §25.3's test **met**: `ああっ、` is battle {19, 26}, `あーっ、` battle {31, 32}, neither in the script — **no chunk and no bank holds both.** `Ａａｈ，` is unavailable (§23.2, あーあ, shipped ×2 in `chunk_004`); `Ａｈ，` is §6's あ、 and `Ａａａｈ，` is §24.3's あ〜ん. **Binds chunk 32 ×2 forward** |
| どっちにしても、 | `Ｅｉｔｈｅｒ　ｗａｙ，` | 11 columns. **Collapsed onto `chunk_000.txt`'s shipped `いずれにしろ、`.** §25.3's test **met exactly**, on the そのとおり / そうそう shape: `いずれにしろ` is battle {0, 27} + script bank 41, `どっちにしても` battle {31} only and 0 script — **no chunk and no bank holds both.** ⚠️ The translator flagged honestly that **register does not separate them** (both speakers are casual) and invited a split instead; §25.3's ground is co-occurrence, not register, so the collapse stands on the stronger footing. Held distinct from §36.2's とにかく → `ａｎｙｗａｙ` and §29.3's connectives. **Binds chunk 27 forward** |
| だけど、 | `Ｂｕｔ，` | 4 columns. **Collapsed onto §23.3's でも → `Ｂｕｔ，` — but NOT on the reasoning the PR gave, which is wrong and is corrected here.** `でも` and `だけど` are **two different connectives**, not two spellings of one word, so this is *not* the 鬼 / オーガ move (§17.2) the PR cited, and §25.3's co-occurrence test **fails**: battle chunks **8 and 24** hold both, and script banks **4, 12, 19, 20, 21, 28, 29** hold both. What discharges it is **shipped practice**: `chunk_000` L3 already ships bare `だけど、` as `Ｂｕｔ`, and **`chunk_008` line 8 carries `でも` and `だけど` in ONE message and renders both “but”**, as do `chunk_020` L47 and `chunk_024` L12 / L15. Four independent units and reviewers have already collapsed them; English has one plain adversative and there is **no live distinction to destroy** — which is precisely what §23.3's refusal of `しかし` / `それにしても` turned on, and what is absent here. The conclusion stands; the argument is replaced so the false rule does not propagate |

### 45.6 ⚠️ LIVE — `何だって？` shares `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` with `何だと？` in script banks 5 and 41

The PR ran §25.3's test inside chunk 31 only and reported it met, which is true but incomplete.
Run at review on **interjection forms alone** (§35.2 discipline — the bare substrings coincide, but
`何だと思っている` in `chunk_013` is a false positive that must not be counted):

| | battle | script banks |
|---|---|---|
| `何だと？` / `何だと！` / `なんだと？` | chunks 7, 13\*, 43 ×2 | **5, 41** |
| `何だって？` / `何だって！` | chunks 15, 29, 31 | **5, 23, 41** |

\* `chunk_013`'s is the `何だと思っている` false positive.

**The battle side is clean — no chunk holds both.** But **banks 5 and 41 hold both**, and
`batch_002.tsv` already ships `Ｗｈａｔ　ｗａｓ　ｔｈａｔ？` and `Ｗｈａｔ　ｗａｓ　ｔｈａｔ！？` into that
pool while `何だって？` sits untranslated in the same banks. This is **§42.4's shape exactly**: the
pairing is **pre-existing, not created by this unit**, nothing shipped is affected, and no line
changes. **Recorded LIVE for whoever translates those pools**, on the §32.5 / §34.2 / §34.5 / §42.4
pattern. **Reserve, verified free across `tl/` and `pending/` at review:
`Ｗｈａｔ　ｄｉｄ　ｙｏｕ　ｓａｙ？` (17).**

### 45.7 The two Latin incantations — `・` is unrenderable and the mapping is forced

`assemble.py`'s charset gate rejects `・` (U+30FB) and §3.1 states *“There is no ellipsis character
and no `・`”*, so the wave dispatch's instruction to reproduce the incantations “exactly, character
for character” **was not satisfiable**, and the translator was right to refuse it and to say so.
Three `・` are mapped, each by an existing rule, and **every letter and its case is preserved byte
for byte**:

| source | shipped | rule |
|---|---|---|
| `ＨＥＫａＳ・ＨＥＫａＳ` | `ＨＥＫａＳ　ＨＥＫａＳ` (11) | `・` as **separator** → `　`, per §1's `ゼファー・クリッペン` → `Ｚｅｐｈｙｒ　Ｋｒｉｐｐｅｎ` |
| `ＥＳＴｉＶｅｂＲＯｉ・・` | `ＥＳＴｉＶｅｂＲＯｉ．．` (12) | trailing `・・` as **ellipsis dots** → `．．`, count matched per §3.1 |
| `ＥＬＡＧＬＡ・ＬｉＣＨ！` | `ＥＬＡＧＬＡ　ＬｉＣＨ！` (12) | separator → `　` |

The mixed case (`ＨＥＫａＳ`, `ｉ`, `Ｖ`, `ｅ`, `ｂ`, `ＲＯｉ`, `ＬｉＣＨ`) is untouched, and `ＬｉＣＨ`
is what fixes `リッチ` → `Ｌｉｃｈ` at §45.1. **In-game legibility of the separator is a human's
question** — `FLAGS.md` §AG.

### 45.8 Recorded, not re-cut — checked at review and not defects

- **`冥界の王、リッチよ！` → `Ｎｅｔｈｅｒｗｏｒｌｄ　Ｋｉｎｇ，　Ｌｉｃｈ！` (23) drops the fixed form's
  article.** English vocatives drop it, and `Ｏ　Ｎｅｔｈｅｒｗｏｒｌｄ　Ｋｉｎｇ，　Ｌｉｃｈ！` measures
  **25** and will not fit. The two non-vocative instances both keep a determiner (`ｏｕｒ`).
- **`お前たちの王` → lowercase `ｙｏｕｒ　ｋｉｎｇ`.** Same referent as `ｔｈｅ　Ｎｅｔｈｅｒｗｏｒｌｄ
  Ｋｉｎｇ`, but a possessive common-noun description rather than the title. §28.1's 国王 → *the
  King* is the title form and is undisturbed. Correct English; accepted.
- **`さあ、{FC00}{=0000}。` → `Ｃｏｍｅ　ｏｎ，　{FC00}{=0000}．` is NOT a divergence from the bare
  `さあ、` → `Ｎｏｗ，` of `chunk_006` / `chunk_033`.** §24.5 names this trap by name. Confirmed
  mechanically at review: the block is **byte-identical to `chunk_003.txt` L4's**, with the stop
  the source gives it (§5).
- **`カーライン軍が` renders `ｔｈｅ　Ｃａｒｌｉｎｅ　ａｒｍｙ` in all three of `chunk_009`,
  `pending/chunk_017` and here** — only the break position differs, which §24.5 rules is not a §3
  matter (the rule engages on the message, not on the row).
- **`Ｈ，　ｈｅｙ，` for `お、おい、` is fine, and the corpus is genuinely split** — see `FLAGS.md` §AG.
- **Speaker attribution verified off the tag stream, not assumed.** Portrait 6 on `{FC50}` is
  Kaizard throughout L2 / L4 / L6 / L8 / L12 / L13 / L14 — contraction-free in every one, with
  imperious-polite imperatives and mock-courteous killing (`葬って差し上げましょう` → *allow me to
  lay you to your rest*). The archaic `ｔｈｅｅ` / `ｔｈｏｕ` / `ｔｈｙ` is confined to the two spell
  blocks and does not leak into his ordinary speech. **The two Imperial rankers are casual to each
  other and formal to him — the register split in this chunk is per SPEECH, not per character**,
  and §41.4 keys on the line's register, which is what was applied.

### 45.9 Register

| Who | Register |
|---|---|
| Kaizard (portrait 6, `{FC50}`) | Formal, **no contraction anywhere**, imperious-polite: `Ｉｔ　ｍａｔｔｅｒｓ　ｎｏｔ　ａｔ　ａｌｌ．`, `Ｇｏ　ａｎｄ　ｈｕｎｔ　ｉｔ　ｄｏｗｎ．`, `ｙｏｕ　ａｒｅ　ｔｏ　ｂｕｙ　ｍｅ　ｔｉｍｅ．` Mock-courtesy is his signature — he kills in the polite volitional. Archaic `ｔｈｅｅ` / `ｔｈｏｕ` / `ｔｈｙ` **only** inside the two incantations |
| The two Imperial rankers (portraits 7, 8) | **Per speech, not per character.** Casual to each other (`ああ、何しろ`, `〜だからな`, `〜ほしいぜ` → `Ｙｅａｈ`, `ｔｈｅｙ’ｒｅ`, `ｌｅｔ’ｓ`); formal and contraction-free to Kaizard (`〜です`, `〜ます` → `Ｎｏ，　ｔｈｅｙ　ａｒｅ　ｅｎｅｍｉｅｓ．`, `Ｉｔ　ｓｅｅｍｓ　ｔｏ　ｂｅ`) |
| The player's party (portraits 0, 1, 2, 3, 4) | §7 unchanged — casual, contractions throughout (`ｔｈｅｙ’ｒｅ　ａｔｔａｃｋｉｎｇ`, `Ｉ　ｃａｎ’ｔ　ｆｏｒｇｉｖｅ　ｔｈａｔ．`, `Ｗｅ’ｖｅ　ｇｏｔ　ｔｏ　ｈｅｌｐ　ｆａｓｔ！`) |
| The villager (portrait 9) | Formal `です`, **no contraction** — `Ｔｈｉｓ　ｉｓ　ｔｅｒｒｉｂｌｅ！` — against the party's contractions on the same page |


## 46. Added by script batch 009 (PR #28, merged 2026-09-09)

`script_unique.txt` **DATA 534–583** (= FILE 539–588; FILE = DATA + 5, convention verified at
review by reading `tools/queue.py:script_rows()`). 50 unique lines / 50 instances / 2,913 JP →
5,925 EN visible characters = **2.0340×**, **+6,026 bytes** across banks 7, 8, 9, 10, 11, 12.
Town troop-recruitment and court/NPC dialogue: a Leclerc courtier, Prince Hoag's island town,
the elder of an ancient Reese town, the ruined village, fort guards, a shop greeting.

**Every figure in this section was re-measured at review with `len()` and the tool's own row
semantics. Where a PR-body cell disagreed, the measurement won and the cell is corrected below.**

### 46.1 Wave-7 seeds promoted (all nine used exactly as seeded, none improved on unilaterally)

| Japanese | English | Note |
|---|---|---|
| 鏡の神殿 | `Ｍｉｒｒｏｒ　Ｔｅｍｐｌｅ` | **13 columns**, exact. §9 row **STRUCK** — reach was DATA 569, 571 and both land here. 神殿 → *temple* stays distinct from 教会 → *church* and 聖堂 → *sanctuary* (this unit ships `ｓａｎｃｔｕａｒｙ` for 聖堂 at 575, so all three are live in one wave and stay apart) |
| リースの化身 / 化身 | `ｔｈｅ　ｉｎｃａｒｎａｔｉｏｎ　ｏｆ　Ｒｅｅｓｅ` / `ｉｎｃａｒｎａｔｉｏｎ` | **24 / 11 columns**, both exact. The 24 is the widest run in the unit; it stands alone on its row at 569 and 571 and takes **no mark or particle**, exactly as §9 warned. §9 row **STRUCK**, with its reach corrected from "569, 571" to **568, 569, 571** |
| リースの神々 | `ｔｈｅ　ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ` | **17 columns.** 560 splits it at `ｏｆ` across a break; **567 is a vocative and drops the article — `Ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ，`, which is 14 columns** (the PR body said 15; re-measured at review). §9 row **STRUCK** |
| 『かげの石版』 | `“Ｓｈａｄｏｗ　Ｔａｂｌｅｔ”` | **15 quoted / 13 bare.** `『…』` → `“…”` per §12. **§9 row STRUCK — this unit was the LAST of its instances to land** (battle chunk 36 + script DATA 569), discharging the `ルート` precedent |
| 石版 | `ｔａｂｌｅｔ` | **6 columns**, bare lowercase, byte-identical to chunk 30's four instances. ⚠️ **§9's row STAYS LIVE — DATA 300 (count 21, 21 banks) is untranslated.** See §46.4 |
| 選ばれし者 | `ｔｈｅ　ｃｈｏｓｅｎ　ｏｎｅ` | **14 columns.** Hapax (DATA 570). §9 row **STRUCK** |
| ビーストショップ / アイテムショップ | `　Ｂｅａｓｔ　Ｓｈｏｐ` / `　Ｉｔｅｍ　Ｓｈｏｐ` | **11 / 10 with the cursor gutter, 10 / 9 bare.** Both keep the leading `　` as menu options of 555's choice. ⚠️ **§9's row STAYS LIVE — `ビーストショップ` recurs at DATA 899.** See §46.4 |
| オーホホホ | `Ｏｈｏｈｏｈｏ` | **7 columns**, with the source's own four stops → `Ｏｈｏｈｏｈｏ．．．．`. Cavia's laugh, on §12.3's `ふふ` → `Ｆｕｆｕ` and §11.5's `フハハハ` → `Ｆｕｈａｈａｈａ`. §9 row **STRUCK** |

### 46.2 New terms

| Japanese | English | Note |
|---|---|---|
| なるほど (**beside `そうか` in one bank**) | `Ｉｎｄｅｅｄ．` | **7 columns.** The §25.3 collision ruling — see §46.3. §30.3's `なるほど` → `Ｉ　ｓｅｅ．` is **unchanged** for every unit not carrying `そうか` in the same bank |
| 騎士道 | `ｃｈｉｖａｌｒｙ` | 9 columns. Hapax — 1 script, 0 battle. 536 |
| 圧制 | `ｔｙｒａｎｎｙ` | 8 columns. Held **distinct** from 圧力 → `ｐｒｅｓｓｕｒｅ` (§42) and from 支配 — three source words for the Empire's grip |
| 独立する | `ｗｉｎ　ｆｒｅｅ　ｏｆ` | 538. Held distinct from §28.2's 解放 → `ｆｒｅｅ` (the transitive verb); the shared head word is deliberate |
| 詩 | `ｐｏｅｍ` | 4 columns. 568. `ｖｅｒｓｅ` is free but *poem* is the plainer word for a town's handed-down couplet |
| 大渓谷 | `ｇｒｅａｔ　ｇｏｒｇｅ` | 12 columns. 574. **Deliberately not `Ｃａｎｙｏｎ`** — §30.1 spends that on 峡谷 in `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` and records `Ｇｏｒｇｅ` as the untaken alternative. 大 → *great* matches §2's 大要塞 |
| 海岸 | `ｃｏａｓｔ` | 5 columns. 574. Distinct from §39.1's 港 → `Ｐｏｒｔ` |
| 戦況 | `ｈｏｗ　ｇｏｅｓ　ｔｈｅ　ｗａｒ` | 558 and 576, byte-identical. ⚠️ `ｗａｒ` is **not** free — §38.2 spends it on 戦乱 (bank 3) and §42 uses `ｗａｒｒｅｄ` for 争って (bank 4). Different source words, no shared bank with 8 or 10; §25.3 met. Recorded so it cannot drift |
| 参考にする | `ｔａｋｅ　…　ｉｎｔｏ　ａｃｃｏｕｎｔ` | 556/557. Deliberately **not** `ｂｅａｒ　…　ｉｎ　ｍｉｎｄ`, which §26.7 spends on the old tutor and which **this unit needs at 574** for `心に留めておきましょう` — the collision would have been inside one unit |
| はじめまして。 | `Ｈｏｗ　ｄｏ　ｙｏｕ　ｄｏ．` | 14 columns. 574. ⚠️ **`Ｗｅｌｌ　ｍｅｔ．` deliberately NOT reused** although `pending/chunk_005` L23 renders this string that way: that file is **parked**, so §3 does not engage, and this unit's own **560 needs `Ｗｅｌｌ　ｍｅｔ` for `よく参られた`** (same verb 参る, and §38.2's shipped `よく参った。`). §38.2 flagged this pair; **bank 10 was the live locus and this is it** |
| ほら、 | `Ｔｈｅｒｅ，` | 6 columns. 574, Annette urging her father. Distinct from §28.8's さあ、 → `Ｎｏｗ，`, §42.1's で、 → `Ｎｏｗ，`, §31.3's さて、 → `Ｎｏｗ　ｔｈｅｎ，`, §34.1's なあに、 → `Ｎｏｗ　ｎｏｗ，` |
| 中央 (spatial) | `ｍｉｄｓｔ` | 574. ⚠️ **Not free**: `chunk_024` L16 ships `Ｉｎ　ｔｈｅ　ｍｉｄｓｔ　ｏｆ　ｗａｒ` — a **temporal** midst against this **spatial** one; different message, different store, no shared bank or chunk. §25.3 met |
| 空き家 / うなり声 / 調査する / 拡張する / 誘致する | `ｅｍｐｔｙ　ｈｏｕｓｅ` / `ｇｒｏｗｌ` / `ｌｏｏｋ　ｉｎｔｏ` / `ｅｘｐａｎｄ` / `ｄｒａｗ　ｉｎ` | 552, 555; all five verified free across `tl/` and `pending/`. 館 → `ｍａｎｓｉｏｎ` is §34.1's, reused unchanged |
| ご用 (honorific) | `ｅｒｒａｎｄ` | ⚠️ Held apart from plain 用 → `ｂｕｓｉｎｅｓｓ` (§42.2, `batch_008` DATA 502). **534** `ご用が　あれば` → `Ｉｆ　ｙｏｕ　ｈａｖｅ　ａｎ　ｅｒｒａｎｄ，` (23) and **561** `で、ご用は何かな？` → `Ｎｏｗ，　ｙｏｕｒ　ｅｒｒａｎｄ？` (17); the plain 用 keeps *business* at 549, 566, 582/583. This unit adds the **fifth and sixth** `ご用` openers and neither collides with §42.2's four |

### 46.3 §25.3 RULING — `なるほど` → `Ｉｎｄｅｅｄ．` where it shares a bank with `そうか`

**§25.3's standing test ("no chunk and no bank contains both") finally fails, exactly where §42.4
predicted it would.** The census was recounted independently at review over both pristine dumps
and **reproduces the PR's cell for cell**:

```
そうか。      script banks [5, 8, 9, 29, 33, 41]   battle chunks [7, 27, 30]
そうか、      script banks [8, 19, 23, 33, 41]     battle chunks [4, 23, 32]
そうですか    script banks [0, 7, 12, 16, 41]      battle chunks [3, 5, 31]
そうかい      script banks [2, 12, 17, 20, 23, 24] battle chunks []
なるほど      script banks [1, 5, 8, 33, 36, 40]   battle chunks [0,6,16,17,19,25,29,32,33,42,43]
そう。       script banks [0, 4, 41]              battle chunks [0,4,5,16,19,29,43]
そうでしたか   script banks [10]                    battle chunks []
SHARED BANKS そうか x なるほど : [5, 8, 33]
```

⚠️ **THE CENSUS CELL ABOVE IS SHORT BY ONE BANK, AND THE MISSING CELL IS BANK 1 — corrected in
place 2026-09-11 (§4.3, PR #35 review). THE RULING IS UNCHANGED AND IS NOT REOPENED; only the
census is.** The block keys on `そうか。` and `そうか、` and therefore cannot see a `そうか` closed
with a **dot run**. `batch_012`'s DATA 390 is `そうか・・・・` (Prince Hoag), which sits in **bank 1**,
and that same unit's DATA 391 carries `ふむ、なるほど、` (the port-town elder), also **bank 1**.
Re-counted at that review over the pristine dump on the **bare substring**, which is what a census
of a word rather than of a spelling requires:

```
そうか   (bare substring)  script banks [1, 2, 5, 8, 9, 12, 17, 19, 20, 23, 24, 29, 33, 41]
なるほど (bare substring)  script banks [1, 5, 8, 33, 36, 40]
SHARED BANKS, corrected   : [1, 5, 8, 33]      (was [5, 8, 33])
```

**Bank 1 is therefore a second live locus, and `batch_012` is the unit that translates both of its
members** — two scenes a player reaches in one visit. §46.3's ruling was applied there exactly as
written: **`なるほど` is the member that moved.** DATA 391 ships `Ｈｍ，　Ｉｎｄｅｅｄ．` and DATA 390
keeps `Ｉ　ｓｅｅ．．．．`. `Ｉｎｄｅｅｄ．` is otherwise spent only in bank 8 (`batch_009`) and battle
chunks 2 and 38 — **disjoint from bank 1 on both §25.3 axes**, so the new spend is clean. Bank 0's
`そうですか` (DATA 358, 376) keeps `Ｉ　ｓｅｅ．`: **bank 0 holds no `そうか` and no `なるほど`**,
verified. ⚠️ **This is §AN2's shape a second time — a census matched on a SPELLING where the rule is
about a WORD.** The operational fix is the same one §AN2 records: census the bare substring, then
read the hits.


**Bank 8 is the live locus and `batch_009` is the unit that translates both of its members**:
`そうか` at DATA **550, 553, 554** and `なるほど` at **556, 557** — bank assignments verified
individually at review — **all five spoken by Prince Hoag, in one town interface, in adjacent
menu branches a player reaches in one visit.**

**`なるほど` is the member that moves.** `そうか` keeps `Ｉ　ｓｅｅ．`, on three counted grounds:

- `そうか` is 3 of the 5 rows to `なるほど`'s 2 — the smaller disturbance.
- **`そうか` → `Ｉ　ｓｅｅ．` is shipped one bank over in this same recruiter skeleton**, at
  `batch_008.tsv` L64/L67 (bank 5). Moving `そうか` would fork the skeleton's own voice.
- `なるほど` → `Ｉ　ｓｅｅ．` is shipped only in battle `chunk_033` and **parked** `chunk_017`;
  neither is bank 8, so **§30.3 stands unamended** for every unit not carrying both.

`Ｉｎｄｅｅｄ．` is **7 columns**. Its only other occurrence anywhere is `chunk_002` L15's
`Ｉｎｄｅｅｄ　ｗｅ　ｈａｖｅ！` for §20.3's `まったくだっ！` — different string, **battle** store,
chunk 2: disjoint from script bank 8 in both dimensions, so §25.3 is met for the new form too.

⚠️ **`Ｅｘａｃｔｌｙ．` (8) is NOT spent** — re-verified free across all of `tl/` and `pending/` at
review, and stays reserved for `そのとおり` / `そうそう` per §25.3.
⚠️ **Next reserve, verified free and unspent: `Ｑｕｉｔｅ　ｒｉｇｈｔ．` (12)**, §25.3's own
second choice, for a third member of the family in one bank.

**The other three members were checked, not assumed:** `そうですか` (537, 541) is **bank 7**, which
holds no other member; 567's `そうか` is **bank 9**, which holds no `なるほど`; 574's
`そうでしたか・・・。` → `Ｉ　ｓｅｅ．．．．` is a sixth source string on the form and a **true hapax**
(bank 10 only, 0 battle), and bank 10 holds none of the other six. **Lines affected outside this
unit: none.**

⚠️ **FORWARD GAP — the ruling is BANK-scoped and does not reach a battle CHUNK.** Battle
**chunk 32 holds both `そうか、` and `なるほど` and is untranslated**, while `chunk_033` already
ships `なるほど` → `Ｉ　ｓｅｅ．`. Chunk 32's translator will meet this same collision with no rule
covering it. Recorded at `FLAGS.md` §AH.

### 46.4 CORRECTIONS to §9 made at this review

1. **`石版` is NOT struck, and the wave-7 dispatch's "strike both rows" was wrong.** PR #28
   renders DATA 569 and 571, leaving **DATA 300** — `軍神ヘルメスが光の文字を刻んだとされる漆黒の石版。`,
   **count 21 across 21 banks**, an item description — which is in **no** wave-7 unit and is
   translated in **no** `tl/script/*.tsv`. Verified by direct lookup at review. The row is struck
   by whichever unit takes DATA 300. `『かげの石版』`, whose whole reach *is* exhausted, **is** struck.
2. **`ビーストショップ`'s §9 reach cell was incomplete and the row is held live.** It said
   "script 555"; the term also occurs at **DATA 899 (bank 28, untranslated)**,
   `『ビーストショップ』でドラゴンやゴーレムを売ってくれるぜ。` **Neither the dispatch nor the PR body
   caught this** — it was found by recounting the term's reach over the dump instead of trusting
   the cell. DATA 899 is **prose, not a menu**: it takes `“Ｂｅａｓｔ　Ｓｈｏｐ”` (§12 quotes, **no**
   cursor gutter). `アイテムショップ` alone is exhausted, but the two share one row.
3. **`リースの化身`'s reach was "569, 571" and is actually 568, 569, 571.** Corrected in §9.
4. **Three PR-body figures corrected under §9's "your measurement wins" rule; no rendering
   changes.** `ａｓｌｅｅｐ　ｉｎ　ｔｈｅ　Ｍｉｒｒｏｒ　Ｔｅｍｐｌｅ．` is **28**, not 30;
   `Ｇｏｄｓ　ｏｆ　Ｒｅｅｓｅ，` is **14**, not 15; the unit has **12** ellipsis runs, not 13.
   Flag 7's departure was re-tested the hard way and **is** forced: under an optimal greedy wrap
   that page needs **5 rows** with the proper name against a 4-row limit, and 4 without it.
5. **A correction the PR itself made to the dispatch, confirmed here by reading the files:**
   `Ｉ　ｓｅｅ．` for `そうかい` is **§38.2's, in `batch_007`** (banks 2/3). `batch_008` L64/L67
   render **`そうか。`**, not `そうかい`. The dispatch's attribution was wrong, and the correction
   *strengthens* §46.3 rather than weakening it.

### 46.5 Register and structure notes

- **`王` and `王子` name the same portrait (`0x14`, Prince Hoag) in bank 8 and the English commits
  to neither.** 542's retainer says `王は…` → `Ｔｈｅ　Ｋｉｎｇ　ｉｓ　ａｗａｙ`; 558's captain calls
  the same portrait `王子` → `ｍｙ　Ｐｒｉｎｃｅ`. Each row renders exactly what its own line says
  (§28.7). Hoag's father is dead (576), so *King* may be correct in-fiction, or 542 may be a
  generic door line. **No English here decides it; an in-game visit would.** `FLAGS.md` §AH.
- **`殿` and `さん` / `君` after the name insert are dropped**, per §21.2 and §9's ratified `殿`
  decision — carried in register, no word added.
- **Speaker register was traced through the tag stream, not assumed.** 574's six `{FB00}`
  portraits map to `{FCB0}` indices 0–5: Annette, Dolgan, Prince Hoag, the player-captain and two
  9th Army companions. Dolgan and the village woman are uncontracted (`Ｉ　ａｍ　ｔｒｕｌｙ
  ｇｒａｔｅｆｕｌ`, `Ｗｅ　ａｒｅ　ｏｆ　ｌｉｔｔｌｅ　ｈｅｌｐ`); the 9th Army ranker contracts
  (`ｗｅ’ｌｌ　ｍａｎａｇｅ　ｉｔ．．．` for 俺たち). Cavia is contraction-free per §14.6. Torif (576)
  uses 僕 and is earnest but not casual — no contractions, matching §41's princes.
- **The verse at 568 preserves the source's own indentation** — 2 full-width spaces on row 2 and
  7 on row 3, counted and reproduced exactly (§34.1's shop-notice precedent). `「…」` → `“…”`.
  Row 3 carries only `ｈｅｒ　ｆａｉｒ　ｆｏｒｍ”` because 7 of its 24 columns are gutter.
- **`頑張ってくれたまえ。` renders two ways and it is the §34.9 trap-2 shape, not a divergence.**
  573/576 give `ｂｕｔ　ｄｏ` / `ｂｅａｒ　ｕｐ．`; 577 gives `Ｄｏ` / `ｂｅａｒ　ｕｐ　ａ　ｗｈｉｌｅ　ｙｅｔ．`
  — the extra words render **577's own `今しばらく`**, which 573/576 do not contain. The fixed
  phrase `ｄｏ　ｂｅａｒ　ｕｐ` is byte-identical in all three. A positional row checker will report
  this pair; it is not a defect.
- **`ああ、` at 580 is rendered as a clause head, not a fixed interjection** — `ああ、…〜とは・・・`
  → `Ｔｏ　ｔｈｉｎｋ　ｔｈａｔ…`, a lament rather than §6's assent `ああ` → `Ｙｅａｈ` (which §6
  scopes to casual agreement from a rough speaker). ⚠️ **Measured at review: `Ａｌａｓ，` DOES fit**
  (4 rows at 22/20/17/7, inside the limit), so this is a lexical choice and not a geometric
  necessity — recorded rather than presented as forced. **`Ａｌａｓ，` is verified free** and is the
  reserve if a later unit wants a word for the lament `ああ`.

---

## 47. Added by chunk 038 (PR #33, merged 2026-09-09)

Squash `7bd8e76`. Merged at **round 2**; round 1 was CHANGES on two file findings and one PR-body
finding. **5,577 / 8,192, 2,615 slack** — 1,080 JP → 2,333 EN readable characters, **2.16×** against
a **3.37×** ceiling. 135 text rows (source 129), widest 23, twelve at 23, **none at 24**, no page
over 4 text rows, no never-attested `.TTTT.` shape. `{FFFE}` **105 → 108** (lines 1, 20, 22 only);
`{FCC0}` **12 → 12, none added**; the non-`{FFFE}` tag stream is byte-identical to the dump on all
24 body lines. Chapter 38: Limrose burnt out, Marana's return, the surrender parley, Seneca's
briefing on the Empire–Carline treaty, the townsman's parting gift, two tutorial boxes.

⚠️ **Numbering convention used throughout this section: `L<n>` is the `tl/` file index counting the
`=== CHUNK` header as line 0 — what `rowcheck.py 38` prints, i.e. dump body index + 1.**

### 47.1 People and places

| Japanese | English | Note |
|---|---|---|
| マラナ | `Ｍａｒａｎａ` | **Promoted to §1 and struck from §9.** 2 battle, 0 script — exhausted. ⚠️ **Gender unfixed and unrendered; the seed's `〜わ` → female inference is refuted** — see the struck §9 row and §47.5 |
| 焼け野原 | `ａ　ｂｕｒｎｔ　ｗａｓｔｅ` | 15 columns. `リムローズが焼け野原に・・・・。` → `Ｌｉｍｒｏｓｅ　ｒｅｄｕｃｅｄ` / `ｔｏ　ａ　ｂｕｒｎｔ　ｗａｓｔｅ．．．．．`. **2 battle, both this chunk (the two variant openings), 0 script — exhausted.** `ｗａｓｔｅｌａｎｄ` was the rejected longer head; both verified free at review |
| 独裁国 | `ａ　ｄｉｃｔａｔｏｒｓｈｉｐ　ｕｎｄｅｒ　…` | `ｄｉｃｔａｔｏｒｓｈｉｐ` is 12 columns and verified **free**. Deliberately **not** `ｔｙｒａｎｎｙ`, which §46.2 fixes for 圧制. ⚠️ **Count stated precisely at review**: the compound `独裁国` is **1 battle (this chunk), 0 script**; the bare stem **独裁** adds **1 script** (`独裁が`, untranslated). The row covers the stem, so a later script line inherits this head |
| 残兵 | `ｒｅｍｎａｎｔｓ` | ⚠️ **FORCED BY A GATE, NOT PREFERRED — measured at round 2.** The longer `ｒｅｍｎａｎｔ　ｓｏｌｄｉｅｒｓ` cannot be made to fit L18 page 2 in four rows in **any** §2-conformant wording (participial 98 cols → 5 rows; finite 100 → 5; possessive 95 → 5, at both 23 and 24). The **only** four-row packing that keeps it routes through `ｏｆ　ｏｌｄ　Ｃａｒｌｉｎｅ　Ｋｉｎｇｄｏｍ`, which breaks §2's fixed `カーライン王国` → `Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ` — a gate-7 failure, so not an option. **1 battle + 1 script (DATA 1357, untranslated), which inherits this shorter head.** `ｒｅｍｎａｎｔ` verified free across `tl/` and `pending/` |
| 同盟条約 / 調印 | `ａｌｌｉａｎｃｅ　ｔｒｅａｔｙ` / `ｓｉｇｎｉｎｇ` | 17 / 8 columns; both verified free. Built on §26.3's 同盟 → *alliance*, unchanged. 調印 is 1 battle + 2 script |
| 民衆 | `ｉｔｓ　ｐｅｏｐｌｅ` | Ordinary prose. 1 battle + 1 script |

### 47.2 Voice, tics and stock phrases

| Japanese | English | Note |
|---|---|---|
| はははっっ | `Ｈａｈａｈａ` + the source's own punctuation | 6 columns, verified **free**. Marana's boastful **laugh**, kana beats tracked per §11.5 / §14.5 / §40.1 (three は → three `ha`), the doubled small `っっ` carried by the source's own `！！` per §5. ⚠️ **NOT §28.3's military assent — that row's chunk-38 entry is a substring false positive and is struck.** A hapax: battle chunk 38 only, 0 script. Both rejected alternatives measured (§AG6): `Ｙｅｓ，　ｓｉｒ！！` is 10 columns and `Ｈａｈａｈａｈ！！` 9 — **width decided nothing; the reading did** |
| うわっ | `Ｕｗａｈ` | 4 columns, verified **free**. On §32.3's `ぬおっ` → `Ｎｗｏｈ` transliteration template and §41.1's `うわああっ` → `Ｕｗａａａｈ`; held distinct from `Ｇｕｈ` / `Ｇｗａｈ` / `Ｇｕｆｆ` / `Ｎｗｏｈ` / `Ｇｗｏｈ` / `Ｕｇｈ` / `Ａｇｈ` |
| おのれ | `Ｃｕｒｓｅ　ｙｏｕ` | 12 columns. **Not a new form — recording a reuse of a PARKED rendering**: `pending/chunk_043.txt` ships `おのれ・・・奴らめ。` → `Ｃｕｒｓｅ．．．ｃｕｒｓｅ　ｔｈｅｍ．` **4 battle (38, 41 ×2, 43) + 0 script**, re-measured at review. ✅ **PR #30 (chunk 41) reached `Ｃｕｒｓｅ` independently** — this is the term's first *shipping* use |
| 悪運が強い | `ｌｕｃｋｙ　ｄｅｖｉｌ` | 12 columns. `悪運の強い奴め！` → `Ｙｏｕ　ｌｕｃｋｙ　ｄｅｖｉｌ！` — §36.3's `Ｙｏｕ　〜` for a contempt marker in **direct address**. Kept clear of §34.1's `デビルズラック` → `Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ` (capitalised, a predicate nominal): §25.3 met — that is script bank 12, this is battle chunk 38. A hapax |
| 減らず口 | `ｂａｃｋ　ｔａｌｋ` | 10 columns, verified free. A hapax |
| 恥を知れ | `Ｈａｖｅ　ｙｏｕ　ｎｏ　ｓｈａｍｅ！！` | 19 columns. A hapax. `ｓｈａｍｅ` is not free (§20.3's 恥さらし → *a disgrace*) — different words, different messages, §25.3 met; recorded so it cannot drift |
| 恐れ入る | `ｄｏｅｓ　ｉｍｐｒｅｓｓ　…` | `そのしぶとさには恐れ入ったぜ。` → `ｔｈａｔ　ｔｅｎａｃｉｔｙ　ｏｆ　ｙｏｕｒｓ` / `ｄｏｅｓ　ｉｍｐｒｅｓｓ　ｍｅ．` — the emphatic `ｄｏｅｓ` keeps the source's topic-first order grammatical, a §2-licensed departure. A hapax |
| しぶとい / しぶとさ | `ｔｅｎａｃｉｏｕｓ` / `ｔｅｎａｃｉｔｙ` | 10 / 9 columns, both verified **free**. Kept audibly related because the source echoes itself twice in one chunk (L04 `しぶとい奴め`, L16 `そのしぶとさ`). **2 battle, both this chunk, 0 script — exhausted.** The §4 石化能力 / §27.1 愛用 / §30.2 油断 "one word, two grammatical shapes" pattern |
| ヒヨッ子 | `ｆｌｅｄｇｌｉｎｇｓ` | 12 columns, verified free. A hapax |
| ジ・エンド | `Ｔｈｅ　Ｅｎｄ` | 7 columns, capitalised as the loanword flourish; verified **free**. The `・` is a katakana **separator** and maps to `　` per §45.7, so **no ellipsis rule is engaged** — a dot-count checker will report this line and must not be believed. Deliberately not lowercase `ｔｈｅ　ｅｎｄ`, which is spent in `chunk_000`, `chunk_031`, `batch_002` and `pending/chunk_043`. A hapax |
| 苦戦する | `ｓｔｒｕｇｇｌｅ` | 9 columns. ⚠️ **Not free**: `chunk_018` ships `ご奮闘` → `ｓｔｒｕｇｇｌｅ` (§31.2). §25.3 **met** — 苦戦 is chunk 38 only; `ご奮闘` is chunk **18 only** (⚠️ corrected at review: chunk 28 carries the *bare* `奮闘ぶり`, not `ご奮闘`), and 38 is in neither set. A hapax |

### 47.3 Reuses recorded, not new forms

| Japanese | English | Where it was already shipped |
|---|---|---|
| とやら | `ｓｏ‐ｃａｌｌｅｄ` | `chunk_026` (`魔族とやらの歓迎、`). ⚠️ The bare grep reports chunks 13, 26, 38, but **chunk 13's two hits are the false positive `いた**ことやら**`** (こと+やら). Genuine `〜とやら` is **2 battle (26, 38) + 0 script — exhausted** |
| 助太刀 | `ｌｅｎｄ　…　ａ　ｈａｎｄ` | `chunk_006` L9. **2 battle (6, 38) + 0 script — exhausted.** Shares its English with §33.7's `手を貸そう` → `Ｉ’ｌｌ　ｌｅｎｄ　ａ　ｈａｎｄ．` (chunk 19) — a **pre-existing** pairing, different source words, disjoint chunks, §25.3 met |
| 避難 | `ｓｈｅｌｔｅｒ` | `chunk_003` L4. **2 battle (3, 38) + 0 script — exhausted** |
| 占拠 (passive — `占拠される`) | `ｔａｋｅｎ` | `chunk_022`. 3 battle (22, 37, 38) + 1 script. ⚠️ **SCOPE ADDED IN PLACE 2026-09-09 (§4.3, PR #29 review) — this row read a bare `占拠`, and the census it names includes chunk 37, which does NOT take `ｔａｋｅｎ`.** The two `ｔａｋｅｎ` instances are both **passive and punctual**, one place seized (`カーライン城が…占拠されました`, `この街もほぼ占拠された`); chunk 37's is **active, progressive and distributed** (`帝国兵が各地を占拠しているため`) and takes `ｏｃｃｕｐｙ` — see §48.4. **No line needs revisiting**: chunks 22 and 38 are both passive and keep `ｔａｋｅｎ`. The split is the §39.4 (`しまった`, split on position) and §48.1 (`始末`, split on sense) shape |
| 全滅 | `ｗｉｐｅｄ　ｏｕｔ` | `chunk_019` (`全滅か。` → `ｗｉｐｅｄ　ｏｕｔ．`), and chunks 2 and 9. **The fixed form, ruled at PR #29's round 1** |
| 餌食 | `ｐｒｅｙ` | The kanji spelling of §25.1's `えじき` → `ｐｒｅｙ` (`chunk_009`), same construction `〜のえじきになる`. §40.1 deliberately holds 獲物 → `ｑｕａｒｒｙ` apart. ⚠️ `chunk_000` renders 餌食 as a verb phrase (`Ｓｔａｙ，　ａｎｄ　ｔｈｅｙ　ｅａｔ　ｕｓ．`) — **recorded, not re-cut**: a different message, and chunk 0 has 27 bytes of slack (§18.3) |
| 抑える | `ｈｏｌｄ　…　ｄｏｗｎ` | New here; **2 battle, both this chunk, 0 script — exhausted, and both instances share the word.** Deliberately **not** `ｐｕｔ　…　ｄｏｗｎ`, which §37.1 fixes for **鎮圧** (chunks 22, 43 — neither is this chunk, so §25.3 is met and that reserve stays with 鎮圧) |
| 降伏 | `ｓｕｒｒｅｎｄｅｒ` | 10 columns, ×2 here, byte-identical in the verb and noun uses. Shares its English with **投降** → `ｓｕｒｒｅｎｄｅｒ` (`chunk_030`); §25.3 **met and counted**: 投降 is chunk 30 only, 降伏 is chunks 16 and 38 only, 0 script either way. The `ｃａｐｉｔｕｌａｔｅ` reserve is unspent |
| 刃を向ける | `ｔｕｒｎ　ａ　ｂｌａｄｅ　ｏｎ　…` | ✅ **PR #30 (chunk 41) reached this independently**; tense follows each source (`Ｔｏ　ｔｕｒｎ` here, `ｔｕｒｎｅｄ` there). **2 battle (38, 41) + 0 script — exhausted by the two units.** ⚠️ `ｂｌａｄｅ` is **not** free — `batch_003` L96/L99 and `batch_004` L21 use it for a physical sword blade (妖刀 / 刀身 / 名刀); **§25.3 met**: those are script bank 21, this is battle chunk 38 |

### 47.4 `反旗を翻す` — the ruling, and the geometry that did **not** decide it

| Japanese | English | Note |
|---|---|---|
| 反旗を翻す | `ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ` | **2 battle (38, 42) + 0 script.** Matches PR #31 (chunk 42), which shipped it first and did **not** move |

**PR #33 originally shipped `ｒｏｓｅ　ｉｎ　ｒｅｖｏｌｔ` and argued PR #31's form was *geometrically
impossible* in chunk 38's box** — L18 page 2 is shape `.TTTT` (a **leading**, unfillable blank plus 4
text rows), already at the four-row wall, with `{FCC0}` forbidden by `assemble.py:tag_parity`. Six
wordings were measured and every one keeping all four content elements needed a **fifth** row; the
only one that fitted deleted 王国, which CLAUDE.md §3 forbids. **The reviewer re-measured and the
claim does not hold.** The obstruction is a property of *one token order*, not of the wording: the
tail `ｒｅｖｏｌｔ．．．．．` is 11 columns, atomic and must end the page, but it **need not be
preceded by `ｔｈｅ　ｂａｎｎｅｒ　ｏｆ`** (13; 13 + 1 + 11 = 25 > 24). Moving `ｂａｎｎｅｒ　ｏｆ` onto
the last row — `ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ．．．．．` = **21** — fits four rows at ≤23 with every
element kept, by the same §2.1 step-6 clause reorder the PR already claimed for this page:

```
21 | Ａ　ｆｅｗ　ｒｅｍｎａｎｔｓ　ｏｆ　ｔｈｅ
22 | ｏｌｄ　Ｋｉｎｇｄｏｍ　ｏｆ　Ｃａｒｌｉｎｅ
23 | ｏｐｐｏｓｅｄ　ｉｔ，　ｒａｉｓｉｎｇ　ｔｈｅ
21 | ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ．．．．．
```

So the choice fell to be made **on the merits**, and it goes to the banner form under §2's
literal-first default: 反旗 *is* a flag of rebellion, English has the identical idiom, and the
source's image survives at no cost — while `ｒｏｓｅ　ｉｎ　ｒｅｖｏｌｔ` discards it. §2's ban on
importing an *unrelated* idiom is not engaged either way. **§25.3 met**: `ｂａｎｎｅｒ` renders §2's
旗印 in chunks 0 and 27, disjoint from 反旗's {38, 42} — no shared chunk, bank or message.

⚠️ **`ｒａｉｓｅ` is NOT free, and the near-miss is recorded rather than left to drift.** `chunk_022`
L6 ships `俺たちは反乱なんて起こすつもりはない。` → `Ｗｅ　ｈａｖｅ　ｎｏ　ｉｎｔｅｎｔｉｏｎ` /
`ｏｆ　ｒａｉｓｉｎｇ　ａ　ｒｅｖｏｌｔ．` So `ｒａｉｓｅ` now renders **反乱を起こす** (chunk 22) and
**反旗を翻す** (chunks 38, 42). §25.3 is met on disjoint chunks — and more to the point the two
English forms are held apart by **exactly what holds the two Japanese forms apart, the flag**:
`ｒａｉｓｅ　ａ　ｒｅｖｏｌｔ` against `ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ` mirrors 反乱
against 反**旗**.

⚠️ **The lesson, which is §AC3 / FLAGS §AG6 in a new place: MEASURE THE OPTION YOU ARGUE AGAINST —
and measure it in more than one word order.** The rejected alternative never enters the file, so no
gate ever checks it. Six measurements were made here and all six were arithmetically correct; what
was missing was a re-ordering, and a unit was one review round away from being parked on the
strength of it.

### 47.5 `帝国軍` must carry its article — and the fallback the glossary already names

`まずい、帝国軍だ！！` shipped at round 1 as `Ｂａｄ！　Ｉｍｐｅｒｉａｌ　ａｒｍｙ！！` (20 columns),
which is **neither** of §20.4's two fixed forms. Gate 7 failed. Every one of the **11** shipped
instances carries the article — `ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ` in chunks 2 ×2, 4, 8 ×4, 13, 31,
and the licensed fallback `ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ` in chunks 7 and 11 — and the closest
parallels pay for it: `chunk_008` L5 renders the same `〜、帝国軍だ！` shape across **two rows**, and
`chunk_031` L3 splits `Ｉｍｐｅｒｉａｌ` from `ａｒｍｙ` rather than drop `ｔｈｅ`.

**Ships as `Ｂａｄ，　ｔｈｅ　Ｅｍｐｉｒｅ’ｓ　ｍｅｎ！！` (23 columns)** — §20.4's **width fallback**,
because the default `Ｂａｄ！　ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ！！` measures **24**: legal at the hard
limit but over the ≤23 target of §3.2. This is the exact contingency §20.4 wrote the fallback for.

⚠️ **The reviewer's own prescription was wrong by one character and the translator corrected it —
recorded because the board preaches it.** The review prescribed `Ｂａｄ！　ｔｈｅ　…`, which is
**ungrammatical**: a lowercase word after a full-stop-strength `！`. The reviewer had prepended
`ｔｈｅ` to the existing `Ｂａｄ！` without re-reading the result. All three candidates
(`Ｂａｄ！　ｔｈｅ…`, `Ｂａｄ，　ｔｈｅ…`, `Ｂａｄ！　Ｔｈｅ…`) measure **23**, so width decided
nothing; the source's own mark is `、`, and round 1 had turned it into `！` only as a consequence of
the width problem the article fix removed. **`Ｂａｄ，` is both grammatical and faithful, and is the
only candidate that is both.** Flagged by the translator rather than applied silently — which is
what let it be ruled on.

### 47.6 The unbroken tutorial keys — a lookup key no row recorded

| Japanese (source key) | English | Note |
|---|---|---|
| `アイテムを奪われました。` (**no internal `{FFFE}`**) | `Ａｎ　ｉｔｅｍ　ｗａｓ{FFFE}ｓｔｏｌｅｎ　ｆｒｏｍ　ｙｏｕ．` | ⚠️ **A DIFFERENT KEY from §21.3's, and nothing recorded it until now.** §21.3 fixes the **broken** form `アイテムを{FFFE}奪われました。` and counts it "seven times across chunks 3, 9 ×3, 28, 29 and 30" — **that count is exact for the broken form, verified at this review.** The **unbroken** form is a separate 4 instances: **c38 L22, c39 L9, c41 L10, c41 L12**, none of them in §21.3's list. The `{FFFE}` in the English is **forced, not elective**: unbroken the line measures **28** columns, over the hard 24, and putting the break where §21.3 puts it makes the rendered rows identical too. The §27.4 trap (same readable text, different lookup key) in a new place |

⚠️ **`村が襲われました。` is the mirror image and is worth stating**: measured at this review, that
message is **always unbroken in the source** — 13 instances, **0** broken — so §27.2's fixed English,
which adds a `{FFFE}`, is the only form there has ever been. It too measures **28** on one row.

### 47.7 Departures, all §2.1-licensed and all flagged

Every departure in this unit is forced by the **4-row × 24-column geometry**, not by bytes — the
chunk landed with 2,615 spare, which is §0.2's "above about 4.0 the geometry takes over" in practice
at a 3.37× ratio. The rejected alternative was measured in each case:

1. **L03 p6** `まずい、帝国軍だ！！` — see §47.5.
2. **L03 p5** `各地に避難している。` → `ｓｃａｔｔｅｒｅｄ　ｆｏｒ　ｓｈｅｌｔｅｒ．` (22); 各地に is carried by *scattered*. `ｔａｋｅｎ　ｓｈｅｌｔｅｒ　ｅｌｓｅｗｈｅｒｅ．` = 24. ⚠️ `ｓｃａｔｔｅｒ` is not free — §32.2 spends it on 蹴散らす (chunk 20, transitive, of enemies); different sense, disjoint chunks, §25.3 met.
3. **L18 p1** renders the impersonal `調印式が行われているはず` actively; `ｔｈｅ　ｓｉｇｎｉｎｇ　ｏｆ　ｔｈｅ　ａｌｌｉａｎｃｅ` alone is 27 columns against a 92-column page.
4. **L18 p2** — the §2.1 step-6 reorder of §47.4.
5. **L19 p2** `そりゃ、` is dropped — the one place a *word* of the source is unrepresented, and the lightest available. ⚠️ **Verified at review by the test the PR did not run**: not merely appending but **re-wrapping the whole page** with `Ｓｕｒｅ，` or `Ｗｅｌｌ，` restored still needs **5 rows at ≤23** (it fits only at 24). `Ｅｖｅｎ　Ｉ` already carries the concession `俺だって` makes.
6. **L16 p3** keeps the source's topic-first order grammatical with an emphatic `ｄｏｅｓ`.
7. **L18 p9** `君の父さんの所へ。` → `Ｔｏ　ｙｏｕｒ　ｆａｔｈｅｒ．`; 所 is absorbed because *to your father* **is** *to where your father is*. `Ｔｏ　ｗｈｅｒｅ　ｙｏｕｒ　ｆａｔｈｅｒ　ｉｓ．` = 24.

**Three pages fill a source-blank TRAILING segment at 0 bytes** (§45.2 / FLAGS §AG1): L10 p3 and L18
p6 `TTT.` → `TTTT`, L15 p4 `.TTT.` → `.TTTT`. All attested shapes; the never-attested `.TTTT.` does
not occur anywhere in the file.

### 47.8 Register and speaker channels, derived inside chunk 38

Attributions were taken from the `{FC50}`/`{FC51}` **channel**, not the portrait id (§41.2, FLAGS
§W5), and confirmed at review. **Portrait 08 = Marana on both channels** (she self-names on
08·`{FC51}`, and 08·`{FC50}` carries the same voice through L11, L16, L17 — the §23.5 / §28.7 / §30.7
same-id/opposite-channel pattern). **05·`{FC50}` = Seneca**, named by the next speaker and confirmed
by `僕の父` (§25.5). **06·`{FC51}` = Seti** and **07·`{FC50}` = Yuiti**, matching §40.2's genders and
registers — Seti contracts (`Ｙｏｕ’ｒｅ`, `ｙｏｕ’ｖｅ`, `ｗｏｎ’ｔ`), Yuiti does not (`Ｉ　ｗａｓ`,
`ｓｈａｌｌ　Ｉ`). **Marana takes zero contractions anywhere in the unit** (verified line by line) —
the §14.6 / §20.5 / §25.5 / §28.6 Imperial-officer column, and the contrast with the 9th Army's
casual portraits 00/01/03 is what makes her flatness read as rank (§7).

⚠️ **`久しぶりだな！！` is uncontracted here where `chunk_006` contracts it** — Ridge's is
`Ｉｔ’ｓ　ｂｅｅｎ　ａ　ｗｈｉｌｅ．` (19), Marana's is `Ｉｔ　ｈａｓ　ｂｅｅｎ　ａ　ｗｈｉｌｅ！！` (21).
**Different messages, so CLAUDE.md §3 is not engaged**, and this is §39.7 / §42.7's ruling shape:
*the fixed WORD is shared; the contraction follows the speaker.* Recorded so a positional row checker
does not read it as a divergence.

### 47.9 Notes recorded rather than acted on

- **`それから、` between two vocatives is a list conjunction**, not §40.4/§41.8's reserved connective: `セティ！{FFFE}それから、ユイティ！！` → `Ｓｅｔｉ！` / `Ａｎｄ　Ｙｕｉｔｉ　ｔｏｏ！！`, because *And then, Yuiti!!* is not English between two names. §39.5's shape applied to a different connective. **The `Ａｎｄ　ｔｈｅｎ` reserve is not spent.**
- **`カーライン宮廷軍だって？` is a bare echo question**, `Ｔｈｅ　Ｃａｒｌｉｎｅ　Ｒｏｙａｌ　Ａｒｍｙ？` (23), not §23.2's quotative `“　”` — that rule renders an echoed **clause**; this is an incredulous echo of a bare **noun phrase**. Confirmed at review against §5099's `だって` row, which is scoped to *causal, sentence-initial* and whose reserved quotative forms (`ｔｈｅｙ　ｓａｉｄ` / `ｔｈｅｙ　ｓａｙ．`) are **reportative** and so do not apply to an echo addressed back at the speaker.
- **`Ｉｎｄｅｅｄ，　ｉｎｄｅｅｄ．` for `そうだろう、そうだろう。`** shares `Ｉｎｄｅｅｄ` with `chunk_002` (§20.3) and `batch_009` ×2 (§46.2, explicitly **bank**-scoped to script bank 8); neither source string is in chunk 38, so §25.3 is met. The source's doubling is preserved per §23.2's `気にしない、気にしない。`.
- ⚠️ **An open question left open: expressive lengthening.** `おのれっー！？` → `Ｃｕｒｓｅ　ｙｏｕ！？` and `はははっっ！！` → `Ｈａｈａｈａ！！` carry the extra kana beat on **the source's own punctuation** rather than an added letter. The precedent cuts both ways — §29.3's `くーっ` → `Ｔｃｈｈ` and §43.2's `ブヒィ` → `ｏｉｎｋｋ` give a beat a letter, while §32.6 forbids inventing punctuation for one. **Here the source already supplies the mark**, and `Ｃｕｒｓｅ　ｙｏｕｕ！？` / `Ｈａｈａｈａｈ！！` read as typos. Recorded as the working rule; a general ruling is still owed.
- **`ｈｏｎｏｕｒ`** (L11) — British spelling, consistent with `ｄｅｆｅｎｃｅ` ×11 across `tl/` and `ｈｏｎｏｕｒ` in `pending/chunk_005`.

---

## 48. Added by chunk 037 (PR #29, merged 2026-09-09)

Three review rounds. **Three gate-7 failures**, each found by a different method than the round
before, which is the reason §48.5 exists. Figures: **5,037 / 8,192, 3,155 slack**; JP 985, headroom
5,299, ratio 3.69, widest run 23. Numbering below: `rowcheck` lines (the `=== CHUNK 37` header is
line 0, the first body line is line 1); script citations are **FILE** lines of
`dumps/script_unique.txt` (FILE = DATA + 5).

### 48.1 New forms

| Japanese | English | Note |
|---|---|---|
| マザロー様 | `Ｌｏｒｄ　Ｍａｚａｒｏ` | 12 columns. **Promotes §9's wave-8 seed, used exactly as seeded; the §9 row is struck** — 1 battle + 0 script, a hapax, re-counted over both dumps. 様 → **Lord** on the ヘルファー様 / アーバイン様 precedent (§1, §28.1): male, and his own speech is a commander's blunt imperative (`おい、援軍を呼べ！！`, `馬を飛ばすんだっ！！`). Kept visibly distinct from `Ｍｅｌｚａｒｉｏ` (§20.1, a PLACE) |
| マーシュ | `Ｍａｒｓｈ` | 5 columns. **Promotes §9's wave-8 seed, used exactly as seeded — but the §9 row STAYS LIVE**, and its count is corrected there: **3 script lines / 4 instances**, FILE 870, 1330, 1379 (×2), none translated. ⚠️ **FILE 1379 establishes what he is: `俺はこの船の船長、マーシュってんでさ。` — the ship's captain**, which is what L14's `あの船は？` refers to |
| 小隊 | `ｐｌａｔｏｏｎ` | 8 columns. `そんな小隊で` → `Ｗｉｔｈ　ｓｕｃｈ　ａ　ｐｌａｔｏｏｎ，`. **A fifth unit-word, held apart from all four already fixed**: 部隊 → *squad* (§19.2), 分隊 → *Squad* (§2), 精鋭部隊 → *elite corps* (§2), 本隊 → *the main force* (§2). ⚠️ **Count corrected at review: 1 battle + 2 script LINES / 3 instances** — FILE 524 (`そのような小隊では`) and FILE 1389 (**twice**, `そのような小隊でか`), not the PR's 1. **Row stays LIVE** for both |
| 雑草軍団 | `ｗｅｅｄ　ｃｏｒｐｓ` | 11 columns, **lowercase**, on §23.1's `ガラクタ部隊` → `ｊｕｎｋ　ｓｑｕａｄ` — contempt-word plus unit-word, exactly this shape. Built on §11.5's 雑草ども → *weeds* and held distinct from it: `雑草ども` is chunk 43 ×2 (parked, ships `ｗｅｅｄｓ`), `雑草軍団` is **this chunk only, 1 battle + 0 script**. Cress turning Helfer's insult into a welcome. ⚠️ `ｃｏｒｐｓ` is **not** free — §2's 精鋭部隊 → `ｅｌｉｔｅ　ｃｏｒｐｓ` ships in `chunk_000`; **§25.3 counted at review and MET**: 軍団 is battle chunk 37 only (0 script), 精鋭部隊 is battle chunk 0 only (+2 script), no chunk holds both |
| 首謀者 | `ｒｉｎｇｌｅａｄｅｒｓ` | 12 columns. Held distinct from 黒幕 and from 親方 / おかしら → *Boss* (§32.1, §34.1). Verified free across `tl/` and `pending/` |
| 反発する | `ｔｕｒｎ　ａｇａｉｎｓｔ` | 15 columns. A hapax (1 battle, 0 script). ⚠️ **Three near-synonyms stand within 30 lines of each other in this chunk and are deliberately held apart**: 反発する → *turn against* (L12), 逆らう → *defy* (L11), 抵抗 → *resistance* (L18). A fourth, 反乱軍 → *the rebels* (§26.4), is also here |
| すまねえ。 | `Ｓｏｒｒｙ．` | 7 columns. Marsh's rough apology. ⚠️ **Deliberately NOT §33.2's 申し訳ない → `ｆｏｒｇｉｖｅ　ｍｅ`, which this very message pair also carries** (`申し訳ねぇ！` two messages earlier → `Ｆｏｒｇｉｖｅ　ｍｅ！`), and **NOT** `chunk_024`'s すまない → `ｍｙ　ａｐｏｌｏｇｉｅｓ．`, far too formal for `ねぇ`. Held distinct as a *string* from every shipped “sorry”: §28.3's あいにく → `Ｓｏｒｒｙ，`, §30.3's ごめんね。 → `Ｉ’ｍ　ｓｏｒｒｙ．`, `chunk_002`'s `Ｓｏｒｒｙ　ｔｏ　ｔｒｏｕｂｌｅ`. **Bare `Ｓｏｒｒｙ．` occurs nowhere else in `tl/`** — counted at review |
| ああ。 (from a contraction-free speaker) | `Ｉｔ　ｉｓ　ｓｏ．` | 9 columns. **Not a new entry — the first instance of §6's existing speaker-conditional clause**, “a register-appropriate formal assent from a contraction-free one”. Alfred is contraction-free in merged `chunk_008` (four messages, zero contractions), so `Ｙｅａｈ` is barred for him; not `Ｙｅｓ．`, which §6 forbids reintroducing. `Ｉｔ　ｉｓ　ｓｏ` verified free. Distinct from §43.1's Rimul `Ｉ　ｄｏ．`. ⚠️ **`ああ。` therefore takes TWO English forms inside this one file** — Kain's `Ｙｅａｈ．` (L15, L18) and Alfred's — which §6 requires and a message-blind checker will misread |

### 48.2 Recordings and discharges — forms that already existed

| Japanese | English | Where it was already shipped |
|---|---|---|
| 全滅 | `ｗｉｐｅ(ｄ)　ｏｕｔ` | ⚠️ **A REVIEW FINDING, not a translator addition.** Round 1 shipped `ａｎｎｉｈｉｌａｔｅ` and proposed a glossary row for it; the row would have fixed a **fourth** English form against **three merged files** — `chunk_002` L3, `chunk_009` L9, `chunk_019` L19 — and against PR #33, open in the same wave. **The evidence in that row censused the ENGLISH (`ａｎｎｉｈｉｌ` free — true) and never the Japanese**: the §Y2 / §AC1 blind spot. Row withdrawn; `全滅にしてやれ！！` → `ｗｉｐｅ　ｔｈｅｍ　ｏｕｔ！！` (15). **7 battle (2, 9, 15, 19, 32, 37, 38) + 1 script (FILE 995).** Also recorded at §47.3 by chunk 38's merge. ⚠️ **Row stays LIVE** — chunks 15, 32 and FILE 995 are untranslated |
| 始末 (battle sense) | `ｆｉｎｉｓｈ　…　ｏｆｆ` | `chunk_009` L9 (`ｗｅ　ｆｉｎｉｓｈｅｄ　ｉｔ　ｏｆｆ．`) and `chunk_019` L19 (`Ｂｅｓｔ　ｔｏ　ｆｉｎｉｓｈ　ｈｉｍ．`). This unit's `始末しちまおうぜ！` → `ａｎｄ　ｆｉｎｉｓｈ　ｔｈｅｍ　ｏｆｆ！` (20) joins them. ⚠️ **§37's 始末する → `ｄｏ　ａｗａｙ　ｗｉｔｈ` is NOT wrong and is not corrected** — its own “a hapax **in this sense**” scopes it to chunk 22's political euphemism (`俺たちを始末しようとした`). **Two senses, two forms.** ⚠️ That row's “hapax” is now falsified as a *count* — this is a second instance of the euphemistic word, in the other sense — recorded, no rendering changes. The reviewer's round-1 note that this unit “matches the glossary-fixed form” read a scoped row as general and was wrong |
| やはり、 | `ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ` | **A DISCHARGE of §37's row, which names `やはり反乱軍の` — this unit's L6 — in its own five-instance list.** Round 1 shipped a loose `Ｓｏ　…`; **gate 7 passed it**, and the translator's own Japanese-side sweep caught it at round 2. Now `Ｊｕｓｔ　ａｓ　Ｉ　ｔｈｏｕｇｈｔ，` (18), matching `pending/chunk_043` L12 (sentence-initial) and `chunk_022` L7 (mid-sentence, lowercase) under §5. **Two of the five are shipped, three remain** |
| おい、 | `Ｏｉ，` | **A DISCHARGE of §32.3, whose row says “the form is fixed from here”, re-affirmed by §34.1.** Rounds 1 and 2 shipped `Ｈｅｙ，`; `Ｏｉ，　ｃａｌｌ　ｆｏｒ　ａｉｄ！！` (18) now joins merged `chunk_020` L29's `Ｏｉ，　Ｂｏｓｓ，`. **14 battle across 11 chunks (0, 8, 16, 20, 23, 27, 31, 32, 37, 38, 43) + 10 script across 9 lines** — the row is **very** live. ⚠️ **`Ｈｅｙ，` is spent on `よう、`** (§32.3's own `ねえ、` row and §38 both say so). ⚠️ See `FLAGS.md` §AJ3 for the §4.3 debt this leaves in three merged files |
| 援軍 | `ａｉｄ` (width form) | §2 permits `ａｉｄ` only where 24 columns will not take `ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ`, **and requires flagging each use**. Used once, L1: `Ｏｉ，　ｃａｌｌ　ｆｏｒ　ａｉｄ！！` (18). Re-measured against the round-3 opener: `Ｏｉ，　ｃａｌｌ　ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ！！` = **25**, `Ｏｉ，　ｇｅｔ　…` = **24**, `Ｏｉ，　ｓｅｎｄ　ｆｏｒ　…` = **29**; the page is at its 4-row wall so no break buys the room. **Two segments later the same word fits and takes the full form** (`ｉｆ　ｒｅｉｎｆｏｒｃｅｍｅｎｔｓ　ｃｏｍｅ`, 22) — both forms stand in one file, which is exactly what §2 prescribes |
| 〜さん on a name | dropped | §21.2. `{FC00}{=0000}さん！` → `{FC00}{=0000}！`. Recorded because it reads as an omission and is the fixed rule |

**Inherited without change, verified at review by reading the row and the shipped line:**
`ムムッ` → `Ｈｍｐｈ` (§6) · `ははっ！！` → `Ｙｅｓ，　ｓｉｒ！！` (**§28.3 names chunk 37 in its own
instance list**, and §AI5 confirms the four genuine assents stand) · `しまった・・・！？` →
`Ｏｈ　ｎｏ．．．！？` (**§39.4**, message-initial) · `容赦はしないぞ` → `ｓｈｏｗ　ｎｏ　ｍｅｒｃｙ`
(§39) · `確かに、` → `Ｔｒｕｌｙ，` (§28.2, matching chunks 13, 20, 31) · `どうした、` →
`Ｗｈａｔ　ｉｓ　ｉｔ，` (**byte-identical to `chunk_007` L19 and `chunk_020` L2**) · `えっ！？` →
`Ｅｈ！？` (§21.2 + §5) · `いや、` → `Ｎｏ，` (§25.2) · `分かった` / `よし、` → `Ｒｉｇｈｔ` (§6,
§24.3 — shared deliberately, glossary line 1482) · `ああ` → `Ｙｅａｈ` (§6, casual speaker) ·
`反乱軍` → `ｔｈｅ　ｒｅｂｅｌ　ａｒｍｙ` / `ｔｈｅ　ｒｅｂｅｌｓ` (§26.4 fixes **both**) · `帝国兵` →
`Ｉｍｐｅｒｉａｌ　ｓｏｌｄｉｅｒｓ` (§25.1) · `警備兵` → `ｇｕａｒｄｓ` (§23.1) · `フェリスランド` →
`Ｆｅｒｉｓｌａｎｄ` (§11.2, whose note cites this very line) · `ホアグ王子` → `Ｐｒｉｎｃｅ　Ｈｏａｇ`
(§39.1) · `宮廷軍` → `Ｒｏｙａｌ　Ａｒｍｙ` · `カーライン城` → `Ｃａｒｌｉｎｅ　Ｃａｓｔｌｅ` (§2) ·
`の奴ら` → `ｍｅｎ` (§41's register-selected row).

### 48.3 RULING — `掌握` → `ｓｅｉｚｅ`, and §25.3's test is about SCENES, not spend

**Cross-PR with chunk 41 (PR #30), which shipped `ｔｏ　ｇｒａｓｐ`. `ｓｅｉｚｅ` wins; PR #30 moves.**

The case against `ｓｅｉｚｅ` was that it is already spent — and it is, on three other source words,
verified by reading the pairs: `chunk_006` L12 `取り押さえろっ`, `chunk_021` L5 `捕まえろ`,
`chunk_022` L5 `取り押さえ`. `ｇｒａｓｐ` occurs nowhere in `tl/` or `pending/`. Both facts hold.

**But §25.3's test is not “is the English spent” — it is whether a player can see the collision in
one scene**, in that ruling's own words: *“No chunk and no bank contains both.”* Counted here:
`取り押さえ` = chunks **6, 22**; `捕まえ` = chunk **21** + script FILE 804, 952, 1307; `掌握` =
chunks **37, 41** + script FILE 870. **Three disjoint sets; no chunk, no bank and no line holds two
of them — the test is MET**, on the same licence §28.3 used to let `Ｙｅｓ，` carry `ええ。` /
`そうだ、` / `ははっ！` / `うん、`.

§2 decides the rest: `ｇｒａｓｐ　Ｉｍｐｅｒｉａｌ　ｓｔｒｅｎｇｔｈ` is not idiomatic English for taking
control of a force — `ｇｒａｓｐ` reads as *comprehend* or *physically grip* — while
`ｓｅｉｚｅｄ　ｔｈｅ　ａｒｍｙ` is the ordinary English of a coup. **The swap in chunk 41 is free**:
`Ｇｅｎｅｒａｌ，　ａｎｄ　ｔｏ　ｇｒａｓｐ` and `Ｇｅｎｅｒａｌ，　ａｎｄ　ｔｏ　ｓｅｉｚｅ` are both **21**
columns; both words are 5. ⚠️ **CORRECTED IN PLACE 2026-09-10 (§4.3, PR #30's merge): this cell
read 22.** Measured with `len()` three times — by chunk 41's reviewer at round 1, independently by
its translator at round 2, and again at merge. **No rendering changes**: the swap is free at either
figure, and the ruling is untouched. §AC3's pattern a third wave running — a cell typed rather than
measured.

| Japanese | English | Note |
|---|---|---|
| 掌握 | `ｓｅｉｚｅ` | 5 columns. `軍を掌握したんだ` → `ａｎｄ　ｓｅｉｚｅｄ　ｔｈｅ　ａｒｍｙ．` (23). **2 battle (37, 41) + 1 script (FILE 870).** ⚠️ **ROW LEFT LIVE ON PURPOSE, per the `ルート` precedent (§29.1 / §30.1)** — chunk 37 merges first and leaves it standing; **chunk 41's merge strikes it**. It stays live for FILE 870 regardless, which carries `軍を掌握したんだ` verbatim. ✅ **THE CROSS-UNIT HALF IS DISCHARGED 2026-09-10 at chunk 41's merge (PR #30, squash `3721e4d`)** — chunk 41 shipped `ｔｏ　ｇｒａｓｐ` at round 1, its review raised this ruling as a gate-7 failure, and round 2 applied `ｔｏ　ｓｅｉｚｅ` verbatim. **`ｇｒａｓｐ` now occurs nowhere in `tl/` or `pending/`**, verified at merge by reading the tree. ⚠️ **THE ROW ITSELF STAYS LIVE**: script **FILE 870** carries `軍を掌握したんだ` verbatim and is untranslated, so the unit that renders it strikes this row |

### 48.4 RULING — `占拠` splits on construction, and §47.3's row was under-scoped

§47.3, written at chunk 38's merge, fixed `占拠` → `ｔａｋｅｎ` with a census naming chunks 22, 37 and
38 — but chunk 37 was unmerged and its rendering was not in front of that reviewer. Read at this
review:

| Where | Japanese | Construction | English |
|---|---|---|---|
| `chunk_022` L5 | `カーライン城が…２軍に占拠されました！` | passive, punctual | `ｉｓ　ｔａｋｅｎ　ｂｙ` |
| `chunk_038` L3 | `この街もほぼ占拠された。` | passive, punctual | `ｉｓ　ｎｅａｒｌｙ　ｔａｋｅｎ` |
| `chunk_037` L18 | `帝国兵が各地を占拠しているため` | **active, progressive, distributed** | `ｏｃｃｕｐｙ　ｅｖｅｒｙ　ｒｅｇｉｏｎ` |

The `ため` clause needs the **standing state** — it is why `とても近づけない`. *Have taken* names a
completed act; *occupy* names the condition that blocks approach.

⚠️ **The rejected option was measured in FIVE word orders, per `FLAGS.md` §AI's new rule that a
greedy row count is a minimum only for the ordering it was given.** `But Imperial soldiers have /
taken every region, so / none can draw near.` = 26 / 22 / 19 · `But every region is taken / by
Imperial soldiers, so / …` = 25 / 24 / 19 · `But Imperial soldiers / have taken every region, / …` =
21 / **24** / 22 · `But with every region taken / by Imperial soldiers, / …` = 27 / 21 / 19 · `Every
region is taken by / Imperial soldiers, so / …` = 24 / 21 / 19. **The shipped page is 15 / 21 / 20 /
22 — no row over 22.** `ｏｃｃｕｐｙ` (7) is shorter than `ｈａｖｅ　ｔａｋｅｎ` (11), and `ｔａｋｅｎ` is
already spent in seven files while `ｏｃｃｕｐｙ` is free.

| Japanese | English | Note |
|---|---|---|
| 占拠 (progressive — `占拠している`) | `ｏｃｃｕｐｙ` | 7 columns. `帝国兵が各地を占拠しているため` → `Ｉｍｐｅｒｉａｌ　ｓｏｌｄｉｅｒｓ` / `ｏｃｃｕｐｙ　ｅｖｅｒｙ　ｒｅｇｉｏｎ，`. Held apart from §47.3's passive `占拠される` → `ｔａｋｅｎ`, whose scope is corrected in place. **No line needs revisiting** — chunks 22 and 38 are both passive. ⚠️ **Row stays LIVE: script FILE 870 carries this clause verbatim** and must take `ｏｃｃｕｐｙ`. The split is the §39.4 (`しまった`, on position) and §48.2 (`始末`, on sense) shape |

### 48.5 The lesson this unit paid for three times — gate 6 cannot see terms, and gate 7 must run key-first

**Three gate-7 failures in one unit, each caught by a different method than the round before:**

| Round | Term | Caught by | Missed by |
|---|---|---|---|
| 2 | `やはり` (§37) | the translator's Japanese-side sweep | the reviewer's gate 7, run as “do the terms I noticed match?” |
| 2 | `始末` (§37, scoped) | the same sweep | the reviewer, who read a scoped row as general |
| 3 | `おい、` (§32.3) | **the reviewer's glossary-KEY-driven sweep** | gate 7 twice, **and** the translator's own Japanese-side sweep |

`おい、` is the decisive case: a **three-character particle phrase**. No content-word sweep reaches
it, from either side of the review. Only enumerating the glossary's own keys does. **1,127 keys
enumerated (969 unique); 46 occur in chunk 37's source; all 46 adjudicated**, with the enumerator
controlled in both directions (a planted key present in the source is reported, a planted key absent
from it is not). §AI4 records the method from chunk 38's review; this unit is the evidence for
*why* it is not optional. Six of the 46 were sweep artifacts and three were out of scope by their
own wording — **adjudicated by reading, not passed over**.

⚠️ **And the separate structural point, which belongs to gate 6 rather than gate 7:** CLAUDE.md §6's
gate 6 pairs whole **messages**, so a term recurring inside *differently worded* messages is
invisible to it. **It passed cleanly at round 1 while four terms were wrong** — `全滅`, `始末`,
`やはり`, `おい、`. The Japanese-side sub-message sweep is a separate check and **is not in §6**.
See `FLAGS.md` §AJ1.

---

## 49. Added by chunk 041 (PR #30, merged 2026-09-10)

Rendered in `tl/battle/chunk_041.txt`, squash-merged as **`3721e4d`**. Chapter 41, the return to
Carline Castle: Adjutant Anselmo raises the alarm and orders battle stations; Mamu's sibling and a
second officer are fought and die; the party demands Helfer be handed over; a starved Carline warder
explains Helfer's plot, the alliance banquet and Guilford's disappearance, and gives them an item;
two stolen-item tutorial boxes close the chunk.

**Figures, all re-derived at review with `len()` and the tools' own semantics, on an isolated
checkout of the merged tree.** **3,035 / 8,192, slack 5,157** — 593 JP → 1,293 EN readable
characters = **2.1804×** against a **6.535** tier-E ceiling (headroom 6,565, `tag_bytes` 441,
english_budget 3,876), **33.4 %** of the English budget spent. Widest run **23, eight rows there,
none at 24**; **no page over 4 text rows**, and none the source already exceeded. `{FFFE}` **58 → 62
(+4)** on lines 4, 10 and 12 only; `{FCC0}` **8 → 8, none added or removed**; header and `{PAD 6565}`
byte-identical. Merged at **round 2**; round 1 was CHANGES on **two gate-7 failures**, both fixed
verbatim with the tag stream byte-identical on both lines.

⚠️ **Numbering convention in this section: `rowcheck` lines — the `=== CHUNK 41` header is line 0,
the first body line is line 1.** That is §47's and §48's convention. **Locate by content.**

`Ｈｅｌｆｅｒ` (§11.1) ×5 · `Ａｎｓｅｌｍｏ` (§1) ×2 · `Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ` (§26.2 + §1) ·
`Ｍａｍｕ` (§30.1) · `Ｃａｒｌｉｎｅ　ｓｏｌｄｉｅｒ` / `９ｔｈ　Ａｒｍｙ` / `ｆｏｒｔｒｅｓｓ` /
`ｔｈｅ　Ｅｍｐｉｒｅ` (§2) · `ｔｈｅ　ｒｅｂｅｌ　ａｒｍｙ` (§26.4) · `ａｌｌｉａｎｃｅ` (§26.3) ·
`Ａｌｌ　ｕｎｉｔｓ` / `ｔａｋｅ　ｂａｔｔｌｅ　ｓｔａｔｉｏｎｓ` (§25.1, byte-identical to `chunk_009` L4) ·
`ｉｎｔｅｒｃｅｐｔ` (§30.2) · `Ｌｉｓｔｅｎ　ｗｅｌｌ，` (§20.3) · `Ｎｏｗ，` for さあ、 (§28.8) ·
`Ｗｈｙ，` (§20.3) · `Ｓａｍｅ　ａｓ　ｅｖｅｒ，` (§36.1) · `Ｃｕｒｓｅ　ｙｏｕ` (§47.2) ·
`ｔｕｒｎ　ａ　ｂｌａｄｅ　ｏｎ` (§47.3) · `ｓｅｔｔｌｅ` (§43) · `ｗａｒｄｅｎ` (§14.2) ·
`Ｂｒｏｔｈｅｒ　Ｍａｍｕ` (§30.1 + §41.3) · `Ａｎｄ　ｙｅｔ，` for なのに (§39.6) ·
`Ｗａｉｔ` for 待て · `ｇｅｔｔｉｎｇ　ｉｎ　ｏｕｒ　ｗａｙ` (`chunk_012` L12) and the stolen-item box
(§21.3 / §47.6) are used unchanged, **each verified against the shipped line rather than from memory**.

### 49.1 The two round-1 findings, and why they are worth keeping

Both were gate-7 failures found by running the gate **from the glossary side, key by key** — 1,748
keys enumerated (1,044 unique), **57 occur in this chunk's source, all 57 adjudicated by reading**,
the enumerator controlled in both directions at each round with different planted keys. Neither term
is a content word a translator's own sweep would have reached for.

| Line | Was | Is | Cost |
|---|---|---|---|
| L9 | `Ｇｅｎｅｒａｌ，　ａｎｄ　ｔｏ　ｇｒａｓｐ` | **`Ｇｅｎｅｒａｌ，　ａｎｄ　ｔｏ　ｓｅｉｚｅ`** | 0 bytes, 0 re-flow, both rows **21** |
| L1 | `ｌｅｔ　ｎｏ　ｒａｔ　ｃｏｍｅ　ａ　ｓｔｅｐ` | **`ｌｅｔ　ｎｏ　ｒａｔｓ　ｃｏｍｅ　ａ　ｓｔｅｐ`** | +2 bytes, row 22 → 23, no re-flow |

**The tag stream is byte-identical on both lines, `{FFFE}` included**, and the two pages keep their
shapes (L1 p3 `.TTTT` at 22/22/23/21 = 88 of 92; L9 p5 `TTTT` at 20/23/21/22).

### 49.2 RULING — the `ネズミども` plural stands, and the impossibility that argued against it was false

§30.1 fixes ネズミども → **`ｒａｔｓ`** and §31.3 calls ども the **plural**-contempt in its own words;
both are shipped (`chunk_018` L8 `Ｔｃｈ，　ｙｏｕ　ｒａｔｓ！`, `pending/chunk_017` L6
`ｔｈｅ　Ｃａｒｌｉｎｅ　ｒａｔｓ`). Round 1 shipped a distributive singular and justified it **solely** on
a measurement: `Ｌｉｓｔｅｎ　ｗｅｌｌ，　ｄｏ　ｎｏｔ　ｌｅｔ　ｔｈｅ　ｒａｔｓ　ｃｏｍｅ　ｏｎｅ　ｓｔｅｐ　ｎｅａｒｅｒ
ｔｈｅ　ｆｏｒｔｒｅｓｓ！！` = **68** columns, against the fixed `Ａｌｌ　ｕｎｉｔｓ，　ｔａｋｅ　ｂａｔｔｌｅ
ｓｔａｔｉｏｎｓ！`'s **32**, on a `.TTTT` page whose leading blank cannot be recovered: 32 + 1 + 68 =
**101 > 92**, and still over the 96 hard wall.

**Every one of those figures reproduces, and none of them licensed the conclusion.** Eleven orderings
were measured at review, at 23 and at 24; **four fit**, and the cheapest is the unit's own shipped
sentence with one letter added:

```
22 | Ａｌｌ　ｕｎｉｔｓ，　ｔａｋｅ　ｂａｔｔｌｅ
22 | ｓｔａｔｉｏｎｓ！　Ｌｉｓｔｅｎ　ｗｅｌｌ，
23 | ｌｅｔ　ｎｏ　ｒａｔｓ　ｃｏｍｅ　ａ　ｓｔｅｐ
21 | ｎｅａｒｅｒ　ｔｈｅ　ｆｏｒｔｒｅｓｓ！！
```

> **The lesson, in the translator's own round-2 words, which are sharper than `FLAGS.md` §AI1's:**
> *"I tested the plural only in the orderings I had already discarded, never in the one I had chosen."*

**This is the second false impossibility of wave 8 and both have that shape** — chunk 38's `反旗`
(§47.4) and this one. In both, all arithmetic was correct and the counterexample was the unit's own
shipped sentence with a minimal edit. See `FLAGS.md` §AK.

⚠️ **Forward: `ネズミども` is battle chunks 17, 18, 41 and 42 (×3), 0 script** — chunk 42 inherits
this plural.

### 49.3 New forms first fixed here

| Japanese | English | Note |
|---|---|---|
| 副官 | `Ａｄｊｕｔａｎｔ` | **8 columns**; `Ａｄｊｕｔａｎｔ　Ａｎｓｅｌｍｏ，` is **17**. A **true hapax — 1 battle (this chunk) + 0 script**, re-counted over both dumps at review. Spelled out like `Ｃｏｍｍａｎｄｅｒ` / `Ｃａｐｔａｉｎ` / `Ｄｏｃｔｏｒ` / `Ｂｉｓｈｏｐ` / `Ｇｏｖｅｒｎｏｒ` (§25.1, §33.1). Held **distinct** from every rank already fixed: 中尉 → `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ`, 少尉 → `Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ` (§2), 隊長 → *captain* (§2), 将校 → *officer* (§32.1), 将軍 → `Ｇｅｎｅｒａｌ` (§26.2), 司令官／指令官 → `Ｃｏｍｍａｎｄｅｒ` (§11.2), 分隊長 → *squad captain* (§2), 小隊 → *platoon* (§48.1). ⚠️ **The source word is 副官, NOT 中尉** — §1's `アンゼルモ` row fixes `Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ` for `アンゼルモ中尉`, a different string absent from this chunk. `Ａｄｊｕｔａｎｔ` verified **free** across `tl/` and `pending/` |
| 無念 (negated) | `ｂｉｔｔｅｒｎｅｓｓ` | 10 columns. `今さら無念な気持ちはない。` → `Ｎｏｗ，　ａｔ　ｔｈｅ　ｌａｓｔ，` / `Ｉ　ｆｅｅｌ　ｎｏ　ｂｉｔｔｅｒｎｅｓｓ．` **Not a new root** — `chunk_012` L11 ships `クソッ、無念だ・・・。` → `Ｄａｍｎ，　ｈｏｗ　ｂｉｔｔｅｒ．．．．`; this is the noun of that adjective, the §4 石化能力 / §27.1 愛用 / §30.2 油断 "one word, two grammatical shapes" pattern. ⚠️ `pending/chunk_043` L14 renders 無念 as `ｒｅｇｒｅｔ`: **pre-existing, parked, not created here**, and this unit follows the shipped chunk 12. **4 battle (12, 27, 41, 43) + 0 script** — chunk 27 will reach it. `ｂｉｔｔｅｒｎｅｓｓ` verified free |
| 本望 | `ｃｏｎｔｅｎｔ` | `兄も本望だったろう。` → `Ｍｙ　ｂｒｏｔｈｅｒ　ｔｏｏ　ｍｕｓｔ` / `ｈａｖｅ　ｂｅｅｎ　ｃｏｎｔｅｎｔ．` A true hapax — **1 battle + 0 script**. `ｃｏｎｔｅｎｔ` occurs once elsewhere (`batch_009.tsv`), a different sense in a different bank; §25.3 met |
| 衰弱 | `ｔｏｏ　ｗｅａｋ` | `私は衰弱のため` → `Ｉ　ａｍ　ｔｏｏ　ｗｅａｋ　ｔｏ　ｆｉｇｈｔ`. Hapax — **1 battle + 0 script**. Verified free |
| 口だけは達者 | `ａｌｌ　ｔａｌｋ` | 8 columns, verified **free**. `口だけは達者な野郎だぜ。` → `ｔｈａｔ　ｏｎｅ’ｓ　ａｌｌ　ｔａｌｋ．` (20). Both halves hapaxes — **1 battle + 0 script** each |
| せめてもの協力の証 | `ａｓ　ａｔ　ｌｅａｓｔ　ａ　ｔｏｋｅｎ　ｏｆ　ｈｅｌｐ` | 協力の証 is a hapax (**1 battle + 0 script**). ⚠️ **`ｔｏｋｅｎ` is NOT free** — `batch_006` unique 631 spends it on 感謝のしるし (§34.7), and §32.5 reserves it on the **racetrack** side of 勲章 / メダル in banks 42–43. **§25.3 met**: this is battle chunk 41, those are script banks 12 and 42–43. **The §32.5 reserve is NOT spent by this unit** |
| よくぞ | `Ｓｏ　ｙｏｕ　ｈａｖｅ　…` | `よくぞ戻ってきおったな。` → `Ｓｏ　ｙｏｕ　ｈａｖｅ　ｃｏｍｅ　ｂａｃｋ．` (22). The admiring-ironic force of よくぞ and the haughty `おった` carried in **register and word order**, not in an added word (§2). ⚠️ **The rendering of よくぞ is new; the English string is NOT free** — merged `chunk_037` L15 ships `Ｓｏ　ｙｏｕ　ｈａｖｅ` for **`やっと`**. §25.3 met on disjoint chunks (37 / 41). ⚠️ **よくぞ recurs: 1 battle (this) + 2 script (banks 0 and 41)** — a script unit reaching them must not collide with 37's `やっと` |
| 一歩たりとも〜な | `ｌｅｔ　ｎｏ　…　ｃｏｍｅ　ａ　ｓｔｅｐ　ｎｅａｒｅｒ` | Hapax — **1 battle + 0 script**. The `たりとも` "not even one" is carried by *a step*, which is what lets the fixed plural stand (§49.2) |

### 49.4 Recordings — forms that already existed, and the one that did not move

| Japanese | English | Where it already was |
|---|---|---|
| 番人 (of a castle) | `ｗａｒｄｅｎ` | §14.2 fixes it for Fei and `pending/chunk_005` renders it; chunk 5 is **parked**, so **this is the first SHIPPING rendering**. `ｏｎｃｅ` / `ｗａｒｄｅｎ　ｏｆ　ｔｈｉｓ　ｃａｓｔｌｅ．` (22). **2 battle (5, 41) + 0 script** — exhausted once chunk 5 unparks. Held distinct from 守り神 → *guardian* (§14.2). `ｗａｒｄｅｎ` verified free |
| 陰謀 | `ｐｌｏｔ` | **Already shipped** — `batch_005.tsv` L36 renders `ヘルファーの陰謀だったらしいぜ` as `Ｈｅｌｆｅｒ’ｓ　ｐｌｏｔ．`, and this chunk reuses it word for word, ×2. ⚠️ **See `FLAGS.md` §AK — §41.1's §25.3 clearance was run on 企み vs 計画 and does NOT cover 陰謀 vs 計画, which share bank 41** |
| 同盟祝賀会 / 祝賀会 | `ａｌｌｉａｎｃｅ　ｂａｎｑｕｅｔ` / `ｂａｎｑｕｅｔ` | **Already shipped** — `batch_005.tsv` L35 renders `カーラインと　帝国との同盟祝賀会` as `Ｔｈｅ　Ｃａｒｌｉｎｅ‐Ｅｍｐｉｒｅ` / `ａｌｌｉａｎｃｅ　ｂａｎｑｕｅｔ`, on §26.3's 同盟 → alliance. Bare 祝賀会 takes bare `ｂａｎｑｕｅｔ`. **3 battle (this chunk) + 1 script (bank 30)** |
| 処刑される | `ｂｅ　ｅｘｅｃｕｔｅｄ` | **Not a new stem** — `chunk_012` ships 処刑 as `ｅｘｅｃｕｔｉｏｎ` twice; this is the passive verb of that noun, the §27.1 愛用 pattern. **4 battle (12 ×3, 41) + 0 script** |
| おのれ | `Ｃｕｒｓｅ　ｙｏｕ` | §47.2, fixed at chunk 38's merge one PR earlier. ×2 here — `Ｃｕｒｓｅ　ｙｏｕ，　ｍｙ　ｂｒｏｔｈｅｒ’ｓ` / `ｋｉｌｌｅｒｓ！` and the stuttered `Ｃ，　Ｃｕｒｓｅ　ｙｏｕ．．．，`. **The two units reached it independently** (§47.2 records the same) |
| ぬぬっ | `Ｗｈｙ，` | **Not a new form** — `chunk_002` ×2 ships `ぬぬッ` (katakana ッ) as `Ｗｈｙ，`; this chunk's `ぬぬっ` is hiragana, so a grep on the exact Japanese will not pair them — the `ウエストバリー` / `ウェストバリー` shape (§2), the §Y2 / §AC1 kana blind spot. **3 battle (2 ×2, 41) + 0 script** |
| かんねんして | `ｇｉｖｅ　ｉｎ　ａｎｄ` | **Same word as 観念 in kana** — the same blind spot. `pending/chunk_043` renders `観念しろ！` → `Ｇｉｖｅ　ｉｎ　ｑｕｉｅｔｌｙ！`; parked, so **this is the first SHIPPING rendering**. **かんねん 1 battle (41); 観念 1 battle (43 ×2); 0 script either way.** A kanji search finds neither from the other. `ｇｉｖｅ　ｉｎ` verified free |
| ともども | `〜　ａｎｄ　ａｌｌ` | 7 columns. `ヘルファーともども` → `Ｈｅｌｆｅｒ　ａｎｄ　ａｌｌ，`. ⚠️ **Shares its English with §41.1's もろとも** (`chunk_025`, `Ｔｈｅ　Ｐｒｉｎｃｅｓ　ａｎｄ　ａｌｌ，`). **§25.3 counted at review and MET**: ともども = 1 battle [41] + 0 script; もろとも = 1 battle [25] + 0 script. No shared chunk, bank or message. Two near-synonyms, one English idiom, deliberately |
| 掌握 | `ｓｅｉｚｅ` | §48.3's ruling, **applied here at round 2**; see §48.3, whose cross-unit half this merge discharges and whose column figure this merge corrects |

**Also recorded, checked at review and not defects:** `あの世へ送ってやるわ！` → `Ｉ　ｓｈａｌｌ　ｓｅｎｄ　ｙｏｕ　ｔｏ` /
`ｔｈｅ　ｎｅｘｔ　ｗｏｒｌｄ！` is **byte-identical on both rows** to `chunk_025` L12, with the stop from
the source (§5); `chunk_000`'s contracted `Ｉ’ｌｌ　ｓｅｎｄ　ｙｏｕ` is correctly not copied — §39.7's
*the fixed WORD is shared, the contraction follows the speaker*, and this speaker takes none anywhere.
`ｋｉｌｌｅｒｓ` is **not free** (`batch_003` spends lowercase `ｋｉｌｌｅｒ` on キラーウルフ); different
word, different store, §25.3 met. `Ａｌｌ　ｏｆ　ｉｔ` (何もかも) shares its English with `chunk_018`'s
`全ては` (§31.5), and `Ｐｌｅａｓｅ　ｈｕｒｒｙ．` (急いでください) with `chunk_025`'s `急いでくれ。` —
disjoint chunks in both cases.

### 49.5 RULING — `助かりました` keeps the frame and supplies its own object; `Ｙｏｕ　ｓａｖｅｄ　ｍｅ！！` stands

§26.8 fixes 助かりました → **`Ｙｏｕ　ｓａｖｅｄ　…`** and leaves the object; §2 requires English to
supply an elided one. Chunk 41's speaker is `私` throughout and alone in the castle awaiting
execution (`私は昔　この城の番人をしていたカーライン兵`, `私は衰弱のため`), so the object is **`ｍｅ`**.
Every prior instance has a genuinely plural referent — `chunk_003` (hobbits), `chunk_013` L4/L5 (a
King for his kingdom), `chunk_026` L15 (Annette among survivors), `batch_005` L42.

⚠️ **This is NOT the corpus's first singular referent, and the correction favours the shipped form**:
`chunk_012` already ships `助かったぜ、あんちゃん！` → `Ｙｏｕ　ｓａｖｅｄ　ｍｅ，　ｌａｄ！` (§23.4).

⚠️ **The gate-6 line that appeared to argue against this was an alignment artifact, proved by a
reverse-direction control at review.** Setting `ｍｅ` → `ｕｓ` does **not** clear the report:

```
c013 L04  JP |助かりました！！|   EN |Ｙｏｕ　ｓａｖｅｄ　ｕｓ！！|
c041 L09  JP |助かりました！！|   EN |Ｙｏｕ　ｓａｖｅｄ　ｍｅ！！　Ｉ　ａｍ　ａ|
```

c041's slot carries the following clause because the English re-flowed across the break, so its
segment text can never equal c013's **whatever the object is**. The §33.8 / §34.9 trap family in a
new place. **§3 engages on the message**, and gate 6 reports **0 message-level and 0 page-level
divergences**. **Lines this affects: none.**

### 49.6 RULING — `乗り込む` is collocation-driven, not fixed

The §32.8 `何だ、` shape. Three source clauses, three jobs, and no glossary row: `乗り込んでくる`
(motion toward the speaker) → `ｔｏ　ｃｏｍｅ　ｍａｒｃｈｉｎｇ　ｉｎ` (`chunk_022` L1); `要塞へ乗り込む`
(explicit object) → `ｗｅ　ｓｔｏｒｍ　ｔｈｅ　ｆｏｒｔｒｅｓｓ！！` (parked `chunk_017` L27); bare volitional
`乗り込むぞ！！` → **`Ｗｅ’ｒｅ　ｇｏｉｎｇ　ｉｎ！！`** (16, this unit). No chunk holds two, so §25.3 is
met; `pending/` does not ship, so gate 6 is not engaged on chunk 17 (§41.5's `王家` precedent). The
speaker is the player-side captain and §7 gives him contractions. The measured alternative
`Ｗｅ　ｓｔｏｒｍ　ｉｔ！！` (13) also fits, so fit decided nothing. **Lines this affects: none.**

### 49.7 The `帝国兵` drop is FORCED, and the order-independent proof is what settles it

L9 p5 renders `帝国兵の力も掌握するつもりなのです。` as `Ｇｅｎｅｒａｌ，　ａｎｄ　ｔｏ　ｓｅｉｚｅ` /
`Ｉｍｐｅｒｉａｌ　ｓｔｒｅｎｇｔｈ　ｔｏｏ．`, **dropping 兵** — §25.1 fixes 帝国兵 → `Ｉｍｐｅｒｉａｌ　ｓｏｌｄｉｅｒ`
and holds it distinct from 帝国 → *the Empire*. A §2.1 **step-5 implication**, and it is genuinely
forced: the page is shape `TTTT` with no blank to recover and `{FCC0}` forbidden by
`assemble.py:tag_parity`, so the budget is 4 × 23 = **92** (hard 4 × 24 = 96).

⚠️ **An enumeration of orderings is the wrong instrument here — it is the evidence shape that failed
twice this wave.** The shortest wordings keeping 兵 + 力 + も measure **89–92 columns, UNDER budget**,
so no total settles it either. Packed at review: **all ten need 5 rows at ≤ 23.** At the 24 hard
limit exactly one packs — `Ｈｅｌｆｅｒ　ｈｏｌｄｓ　ｔｈｅ　ｂａｎｑｕｅｔ` / `ｗｉｔｈｏｕｔ　ｔｈｅ　Ｇｅｎｅｒａｌ，　ａｎｄ` /
`ｓｅｉｚｅｓ　Ｉｍｐｅｒｉａｌ` / `ｓｏｌｄｉｅｒｓ’　ｓｔｒｅｎｇｔｈ　ｔｏｏ．` at 24 / 24 / 15 / 23 — and it is
**not admissible**: it drops `つもり`, so Helfer no longer *intends* anything, and the warder's whole
speech is a report of Helfer's plan (CLAUDE.md §3, a plot fact). It also puts two rows at the hard
wall and orphans a 15 against them.

> **Read the constraint as: keeping 兵 costs either a fifth row or the modal. The drop stands, and
> the loss is 兵 rather than `つもり` because 力 is 掌握する's own object.**

### 49.8 Speakers and register — read off the channel byte, not the portrait id (§41.2)

| Who | Register |
|---|---|
| Adjutant Anselmo (portrait 08, `{FC51}` in L1) | §14.6 / §15.3's blustering Imperial officer, **no contractions** — `Ｗｈｙ，　ｔｈａｔ　ｉｓ`, `Ｓｏ　ｙｏｕ　ｈａｖｅ　ｃｏｍｅ　ｂａｃｋ．`, `Ｌｉｓｔｅｎ　ｗｅｌｌ，`. In L8 he answers `Ｃ，　Ｃｕｒｓｅ　ｙｏｕ．．．，` / `ｄｏ　ｎｏｔ` / `ｔｈｉｎｋ　ｉｔ　ｅｎｄｓ　ａｔ　ｔｈｉｓ！`, still uncontracted |
| Mamu's sibling (portrait 06, `{FC50}`, **L4 and L5 are one speaker**) | **No contractions.** Avenges `兄の仇` in L4 and dies calling `マムー兄さん` in L5 — the pairing §30.1 predicted for this chunk. `Ｉ　ｆｅｅｌ　ｎｏ　ｂｉｔｔｅｒｎｅｓｓ．`, `ｈａｖｅ　ｂｅｅｎ　ｃｏｎｔｅｎｔ．`, `ｎｏｗ　Ｉ　ｇｏ．．．．` |
| The second officer (portrait 08, L6) | Uncontracted — `Ａｔ　ａ　ｃｒｉｔｉｃａｌ　ｍｏｍｅｎｔ，`, `Ｉ　ｓｈａｌｌ　ｔａｋｅ　ｙｏｕ　ｏｎ！` |
| The player-side captain (portrait 00, `{FC50}`, L8 pages 1 and 5) | §7 unchanged — contractions (`Ｉ’ｌｌ`, `Ｗｅ’ｒｅ`), which is why `望むところだ。` takes `chunk_030`'s form and `決着をつけてやる` takes `Ｉ’ｌｌ` where Rimul's takes `Ｉ　ｗｉｌｌ` (§43.1) |
| A 9th Army voice (portrait 01, `{FC51}`, L8 page 4, `だぜ`) | Casual, contracted — `ｔｈａｔ　ｏｎｅ’ｓ　ａｌｌ　ｔａｌｋ．` |
| The Carline warder (portrait 03, `{FC51}`, L9) | Polite です／ます, **no contractions anywhere** — `Ｉ　ａｍ　ａ`, `Ｉ　ｗａｓ　ｔｏ`, `Ｔｈｅｒｅ　ｉｓ　ｎｏ　ｔｉｍｅ．`, `Ｉ　ａｍ　ｔｏｏ　ｗｅａｋ` |
| Tutorial boxes (`{=FA1000300030}`, L10 and L12) | §7 unchanged — plain instructional second person, byte-identical to merged `chunk_038` L22 |

⚠️ **`〜わ` in L4 and L6 is the emphatic male `〜てやるわ`, not the feminine sentence-final** — both
speakers use it beside `おのれ`, `お前たち`, `やがって` and plain `だ`. **No rendering depends on it**;
recorded because §1's corrected `マラナ` row settles the same question for chunk 38, and the two must
not be harmonised on a `〜わ` inference.

### 49.9 Recorded, not re-cut — checked at review and not defects

- **`この野ネズミが。` → `Ｔｈｅｓｅ　ｆｉｅｌｄ　ｍｉｃｅ．` stands.** Raised at review against §36.3
  (contempt marker + direct address → `Ｙｏｕ　〜`) and against `chunk_025` L12's shipped
  `お前たち野ネズミには` → `Ｙｏｕ　ｆｉｅｌｄ　ｍｉｃｅ`, then **withdrawn**: §36.3 is scoped to the
  `〜め` suffix, chunk 25's source carries an explicit `お前たち` that this one does not, and §36.3's
  own deixis point (`この` is addressee-proximal, English `Ｔｈａｔ` is distal) is **satisfied** by
  `Ｔｈｅｓｅ`. §2 is literal-first. The person-shift into `Ｉ　ｓｈａｌｌ　ｔａｋｅ　ｙｏｕ　ｏｎ！` mirrors
  the source's own. 野ネズミ → `ｆｉｅｌｄ　ｍｉｃｅ` (§41.1) is unchanged.
- **`野郎` has no glossary row and four collocation-selected treatments**, and this unit spends **no
  noun at all**: `ｌｏｗ　ｓｗｉｎｅ` (`chunk_007`, 下衆な野郎), `Ｔｈｅ　ｗｒｅｔｃｈ，` (`chunk_037` L15,
  bare vocative), **contempt in the demonstrative** (this unit, `ｔｈａｔ　ｏｎｅ’ｓ`), `ｃｕｒ` (parked
  `chunk_043`). Chunks 7 / 37 / 41 / 43 are disjoint, §25.3 met, and this unit cannot collide by
  construction. **Recorded as a drift risk** — the §32.2 `〜の奴` shape — for whoever needs a fifth.
- **`待てっ！！` → `Ｗａｉｔ！！`** takes the majority shipped form (`chunk_002` ×2, `chunk_018`,
  `chunk_025`) with the source's own stops per §5. Merged `chunk_037` L1 renders `待てっ、何者だ！？`
  as `Ｈａｌｔ，　ｗｈｏ　ｇｏｅｓ　ｔｈｅｒｅ！？` — a **different source string**, a sentry's challenge, a
  different message; §3 is not engaged and neither is re-cut.
- **The two clause-order departures are grammatical, not budgetary** — `要塞の中で{FFFE}迎え撃つつもりだな。`
  → `Ｈｅ　ｍｅａｎｓ　ｔｏ　ｉｎｔｅｒｃｅｐｔ` / `ｕｓ　ｉｎｓｉｄｅ　ｔｈｅ　ｆｏｒｔｒｅｓｓ．` and
  `ヘルファーを{FFFE}引き渡せ！！` → `ａｎｄ　ｈａｎｄ　ｏｖｅｒ` / `Ｈｅｌｆｅｒ！！`. The chunk is 5,157
  bytes under its slot and neither row is near the limit.
- **Two pages fill a source-blank TRAILING segment at 0 bytes** (§45.2): L5 p2 `.TTT.` → `.TTTT`,
  L8 p2 `TTT.` → `TTTT`. Census re-run over all 44 pristine chunks at review — `.TTTT` **182**,
  `TTTT` **389**, the never-attested `.TTTT.` **0**, and none is produced. **No leading blank is
  filled anywhere in the file.**
- **Ellipsis dot counts checked mechanically per line**: L1 [4]→[4], L5 [4]→[4] (`今　逝くよ・・・。`
  is four per §3.1), L8 [3,3]→[3,3]. Zero `・`, `…`, `○` or ASCII.
- **The stutter follows the shipped comma form**, `Ｃ，　Ｃｕｒｓｅ　ｙｏｕ．．．，` (16), not parked
  `chunk_043`'s hyphen — the §40.6 census (`Ｘ，　` 8 to 1) settles it.

---

## 50. Added by chunk 042 (PR #31, merged 2026-09-10)

Three review rounds, **three findings, and not one of them was visible to gate 6** — each is a term
recurring inside a differently-worded message, which is exactly the blind spot §48.5 and
`FLAGS.md` §AJ1 describe. Figures: **3,627 / 8,192, 4,565 slack**; JP 698, headroom 6,225, ratio
5.46 (tier D), widest run 24, four rows at 24. Numbering below is `rowcheck`'s (the `=== CHUNK 42`
header is line 0, the first body line is line 1). Every width is `len()`-measured.

Chunk 42 is Helfer's banquet in the new Carline: Guilford's recall by imperial edict, the toast,
Anselmo bursting in, the "rat-hunt" framing of the 9th Army's attack, Anselmo left to fight alone,
and Helfer's escape downriver.

### 50.1 RULING — `くそ` / `クソ` → `Ｄａｍｎ`, and the incumbent is what settles it

**Round 3.** The unit shipped `くそっ・・・！！` → `Ｂｌａｓｔ　ｉｔ．．．！！` (13), a word verified free.
It is now **`Ｄａｍｎ．．．！！`** (9).

| Japanese | English | Note |
|---|---|---|
| くそ / クソ (interjection) | `Ｄａｍｎ` + the source's own punctuation | 4 columns bare. **The whole corpus is three battle instances and zero script**, censused over the pristine dump at review and independently by the translator, which widened the sweep to `ちくしょう` / `こんちくしょう`: `chunk_012` L11 `クソッ、無念だ・・・。` → `Ｄａｍｎ，　ｈｏｗ　ｂｉｔｔｅｒ．．．．` (shipped first, so it fixes the word); `chunk_016` L2 `クソッ・・・・。` (**untranslated, tier A**); this unit's `くそっ・・・！！` → `Ｄａｍｎ．．．！！`. One word, two kana spellings, one English form — the §17.2 鬼／オーガ shape, and §5's mechanism for the stop. Held **distinct** from §39.4's two-word `ｄａｍｎ　ｉｔ` for `しまった`-after-a-grunt exactly as §6's はっ → `Ｓｉｒ` is held apart from §28.3's ははっ → `Ｙｅｓ，　ｓｉｒ` |

**Why the collapse and not a fourth word.** The house rule collapses kana variants without
exception — §17.2 鬼／オーガ, §11.5 くっ／クッ (the *neighbouring* interjection), §28.3 何っ／何ッ,
§29.3 くーっ／く〜っ, §30.3 ぐふっ／グフッ, §2 ウエストバリー／ウェストバリー, and
**§49.4's ぬぬっ／ぬぬッ → `Ｗｈｙ，` and かんねん／観念**, which applied it across **disjoint
chunks** (2 and 41) and so removes the "§25.3 permits it" escape. `chunk_012` shipped first;
§18.3 / §10.6 / §29.1 all put the later unit on the moving side.

⚠️ **Taking `Ｄａｍｎ` here does not add a third source string to the form — it removes a fourth
English word from the corpus.** `Ｂｌａｓｔ` now occurs nowhere in `tl/` or `pending/`, verified by
reading the tree after the merge.

⚠️ **The forward reason this had to be settled now: `chunk_016` holds BOTH `クソッ・・・・。` (L2) and
`しまった・・・敵の` (L3)**, is untranslated and tier-A blocked, and would otherwise inherit two
shipped candidates for one word. §39.4 already binds its `しまった` to the line-initial `Ｏｈ　ｎｏ`,
so nothing in chunk 16 collides.

> ⚠️ **The lesson, in the translator's own words, and it is the sharpest formulation this wave
> produced:** *"I asked whether `Ｄａｍｎ　ｉｔ` was free, found it wasn't, and reached for a new
> word — without ever asking what English `くそ` itself already had. **I measured the rejected
> alternative and never looked for the incumbent.**"*
>
> **That is §AG6's mirror. §AG6 says measure the option you argue against; this says search for the
> form the SOURCE WORD already has before reaching for a new one.** The unit's Flag 6 reasoning —
> that §39.4 and `pending/chunk_005` speak for `Ｄａｍｎ　ｉｔ` — was **correct throughout and is
> preserved by the fix**; the error sat one question upstream of everything it measured, which is
> why no gate caught it. Recorded at `FLAGS.md` §AL.

### 50.2 RULING — `ははっ` does not collapse into `はっ`, and §28.3 named this line

**Round 1.** The unit shipped `ははっ・・・・` → `Ｓｉｒ．．．．` (7). It is now
**`Ｙｅｓ，　ｓｉｒ．．．．`** (12), with the four dots from the source per §5.

§28.3 fixes `ははっ！` → `Ｙｅｓ，　ｓｉｒ！` and says in its own words that it is *"**Distinct** from
§6's はっ → `Ｓｉｒ` … they genuinely stand side by side, so they must not collapse."* Its instance
list, corrected in place at PR #33's merge, **names `c42 L6`** among the four assents it governs.

| Where | Japanese | English |
|---|---|---|
| `chunk_013` L2 | `ははっ！` | `Ｙｅｓ，　ｓｉｒ！` |
| `chunk_037` L1 | `ははっ！！` | `Ｙｅｓ，　ｓｉｒ！！` |
| `chunk_038` L11 | `はははっっ！！` | `Ｈａｈａｈａ！！` — the struck substring case (§28.3, §47.2), not a member |
| **`chunk_042` L6** | `ははっ・・・・` | **`Ｙｅｓ，　ｓｉｒ．．．．`** |

Two things the divergence had already produced, both now cleared: inside the file, L11 ships
`Ｓｉｒ！` for `はっ！`, so one chunk carried both source strings on one English word; and across
files, **`Ｓｉｒ．．．．` was already shipped in `chunk_009` L2 for the different string
`はっ・・・。`**. After the fix `Ｓｉｒ．．．．` is `chunk_009` alone.

### 50.3 `たかが` takes §19.1's `ｏｎｌｙ`, and `ｍｅｒｅ` stops doing two jobs

**Round 1.** `たかが、ネズミの侵入か。` shipped as `Ｍｅｒｅｌｙ　ｒａｔｓ　ｉｎｔｒｕｄｉｎｇ．` (22); it is
now **`Ｏｎｌｙ　ｒａｔｓ　ｉｎｔｒｕｄｉｎｇ．`** (20).

§19.1 fixes `たかが〜` → `Ｔｈｅｙ’ｒｅ　ｏｎｌｙ　．．．` and §41.10 records `ｏｎｌｙ` for `たかが` as
used unchanged by chunk 25. Both shipped instances use it: `chunk_001` L6 `たかがオーク。` →
`Ｔｈｅｙ’ｒｅ　ｏｎｌｙ　ｏｒｃｓ．`, and `chunk_025` L12 `たかが{FFFE}ライトエルフの封印だ。` →
`ｉｔ　ｉｓ{FFFE}ｏｎｌｙ　ａ　ｌｉｇｈｔ　ｅｌｆ　ｓｅａｌ．`.

⚠️ **chunk_025's instance is Helfer, in the same contraction-free register as this line**, and it
renders `ｏｎｌｙ` with the frame adapted. So §19.1's `Ｔｈｅｙ’ｒｅ` is the chunk-1 *sentence*, not
the fixed element; **the fixed element is `ｏｎｌｙ`**, and §11.6's no-contraction rule is no
obstacle to it. Recorded because the row as written invites the opposite reading.

Two further grounds, both counted: `ｍｅｒｅ` was already spent on a neighbouring dismissive
(`chunk_012` L2 `たかだか町道場の師範` → `ａ　ｍｅｒｅ　ｍａｓｔｅｒ　ｏｆ　ａ　ｔｏｗｎ`, and `chunk_026`
×2 on `なんかに`); and **inside chunk 42 itself `ｍｅｒｅ` also rendered `ごとき`** at L6, so §25.3's
test — *"no chunk and no bank contains both"* — was failing in its strictest form, one chunk with
two source dismissives on one English lexeme. `Ｍｅｒｅ` is now `chunk_041` only.

### 50.4 New forms first fixed here

| Japanese | English | Note |
|---|---|---|
| 同胞 | `ｂｒｅｔｈｒｅｎ` | **8** columns (the PR body's 9 is hand-counted). Helfer's address to the Imperial troops, `帝国軍の同胞たちよ！`. Held **distinct** from 仲間 → `ｃｏｍｒａｄｅｓ` (`chunk_020`, `pending/chunk_043`) — a different word, and `ｂｒｅｔｈｒｅｎ` suits §11.6's archaic register. Verified free. **1 battle + 0 script — exhausted** |
| 勅令 | `ｅｄｉｃｔ` | **5** columns; `ｄｅｃｒｅｅ` is 6. Ships as `ｓｕｄｄｅｎ　ｉｍｐｅｒｉａｌ　ｅｄｉｃｔ，` (**22**) — *imperial* is inside 勅's meaning, not an added word. `ｂｙ` sits on the preceding row (`Ｇｅｎｅｒａｌ　Ｇｕｉｌｆｏｒｄ，　ｂｙ`, 20) because `ｂｙ　ｓｕｄｄｅｎ　ｉｍｐｅｒｉａｌ　ｅｄｉｃｔ，` is **25**, one over; `ｂｙ　ｓｕｄｄｅｎ　ｉｍｐｅｒｉａｌ　ｄｅｃｒｅｅ，` is 26. `ｂｙ　ｓｕｄｄｅｎ　ｒｏｙａｌ　ｅｄｉｃｔ，` (22) rejected — 勅 is an **emperor's** rescript. **Recurs verbatim in L2 and L11 and is byte-identical in both.** `ｅｄｉｃｔ` verified free (`tl/`'s one hit is *predict*). **2 battle (both this chunk) + 0 script — exhausted** |
| 退治 | `ｅｘｔｅｒｍｉｎａｔｅ` (verb) / `ｒａｔ‐ｋｉｌｌｉｎｇ` (in ネズミ退治) | **11 / 11** columns (the PR body's 13 for the first is hand-counted). `ｅｘｔｅｒｍｉｎａｔ‐` verified free. `chunk_034` L6 renders 退治 phrase-level as `ｒｉｄ　ｕｓ　ｏｆ　ｔｈｅｍ．` — a different message, not a fixed form. **3 battle (34, 42 ×2) + 1 script** |
| 一匹残らず | `Ｎｏｔ　ｏｎｅ　ｏｆ　ｔｈｅｍ　ｌｅｆｔ，` | **21** columns. Hapax — 1 battle + 0 script |
| 無礼だぞ | `Ｉｎｓｏｌｅｎｃｅ，` | **10** columns (the PR body's 12 is hand-counted). Command register per §6's だまれ note. Verified free. **1 battle + 0 script — exhausted** |
| 静粛に！ | `Ｂｅ　ｓｉｌｅｎｔ！` | **10** columns. ⚠️ **Deliberately NOT §6's だまれ → `Ｓｉｌｅｎｃｅ`**, which `batch_002` L9 already ships as `Ｓｉｌｅｎｃｅ，　Ａｌｆｒｅｄ．` — a host calling a hall to order is a different act from an officer cutting a subordinate off, and §6's entry is not this unit's to spend. ⚠️ **`Ｂｅ　ｓｉｌｅｎｔ` is NOT free and the PR's Flag 5 never checked the form it shipped**: `pending/chunk_005` L28 renders `黙りなさい。` as `Ｂｅ　ｓｉｌｅｎｔ．`. **The conclusion survives on §25.3, not on freeness**: 黙りなさい is chunk 5 (parked) only, 静粛に is chunk 42 only — disjoint, and a parked file engages neither §3 nor gate 6. **1 battle + 0 script — a true hapax** |
| 新生 (新生カーライン) | `ｔｈｅ　ｎｅｗ　Ｃａｒｌｉｎｅ` | **15** columns. Matches the chunk's own `新しいカーライン` so the two read as one polity; the source varies the word, English has one. **1 battle + 0 script** |
| 保護している (of a prince) | `ｈｏｌｄ` | **4** columns. `トリフ王子も、保護している。` → `Ｉ　ｈｏｌｄ　Ｐｒｉｎｃｅ　Ｔｏｒｉｆ　ｔｏｏ．` (**24**). The English keeps the source's custody/protection euphemism. **2 battle (16, 42) + 0 script**; chunk 16 is tier-A blocked |
| 「勝てば正義」 | `“Ｗｉｎ　ａｎｄ　ｙｏｕ　ａｒｅ　ｒｉｇｈｔ”` | **21 bare** (the PR body's 22 is hand-counted), **24** quoted and with the source's `？`. `「…」` → `“…”` per §12. `Ｔｈｅ　ｗｉｎｎｅｒ　ｉｓ　ｒｉｇｈｔ` (22 quoted) rejected — it loses the conditional 勝てば that sets up the next entry about remaking history. 勝てば and 正義 are each **1 battle + 0 script — a true hapax pair** |
| 知恵 | `ｗｉｔ` | **3** columns. `知恵さえあればな。` → `Ｓｏ　ｌｏｎｇ　ａｓ　ｏｎｅ　ｈａｓ　ｗｉｔ．` (**23**). Held distinct from 魔道の力 → *the power of magic* (§12.1) |
| 万歳 | `Ｌｏｎｇ　ｌｉｖｅ　〜` | ⚠️ **NOT a new form, and the PR's `(§6)` citation is wrong — §6 has no 万歳 row.** The precedent is `chunk_009` **L8**, which renders `ディール帝国、万歳！！！` as `Ｌｏｎｇ　ｌｉｖｅ　ｔｈｅ　…` — **the same source word**, so this is a reuse, correctly made and never recorded. `ヘルファー様、万歳！！` → `Ｌｏｎｇ　ｌｉｖｅ　Ｌｏｒｄ　Ｈｅｌｆｅｒ！！` (**23**), ×3 in this chunk, byte-identical. **4 battle (9, 42 ×3) + 0 script** |
| ごとき | `ｍｅｒｅ` | 4 columns. `野ネズミごときに、` → `Ｆｏｒ　ｍｅｒｅ　ｆｉｅｌｄ　ｍｉｃｅ，` (**20**). ⚠️ **The PR's additions table did not record it**, which is how it came to share a lexeme with `たかが` inside one chunk (§50.3). `ｍｅｒｅ` also renders `たかだか` (`chunk_012`) and `なんか` (`chunk_026` ×2) — three source words, three disjoint chunks, §25.3 met. **1 battle + 0 script** |
| 何事 | (carried by the clause, no standing row) | `何事だっ！？` → `ｗｈａｔ　ｉｓ　ｔｈｉｓ！？` and `何事かと思えば` → `Ｉ　ｗｏｎｄｅｒｅｄ　ｗｈａｔ　ｉｔ　ｗａｓ．` — **two forms, deliberately**, because the two constructions differ. ⚠️ **Not a member of the 何 family** (§6, §23.2, §28.3, §30.3, §21.2, §32.2) — 何事 is a different word and must not be collapsed onto `Ｗｈａｔ！？`. **2 battle (both this chunk) + 0 script** |

### 50.5 Reuses recorded, not new forms

`Ｈｅｌｆｅｒ` (§11.1) · `Ｌｏｒｄ　Ｈｅｌｆｅｒ` (§1) · `Ｇｕｉｌｆｏｒｄ` / `Ａｎｓｅｌｍｏ` (§1) ·
`Ｃａｒｌｉｎｅ` / `９ｔｈ　Ａｒｍｙ` (§2) · `Ｇｅｎｅｒａｌ` (§26.2) · **`ｔｈｅ　Ｉｍｐｅｒｉａｌ　ａｒｍｙ`
with its article** (§20.4, §47.5) · `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ` (§38.1 — **referential, so §41.6's
vocative split is not engaged**) · `ｈｏｍｅｌａｎｄ` (§43.2, whose census already names chunk 42) ·
`ｒａｉｓｅ　ｔｈｅ　ｂａｎｎｅｒ　ｏｆ　ｒｅｖｏｌｔ` (§47.4, which ratifies this PR's form by name and
records that it did not move) · `ｙｏｕ　ｒａｔｓ` / `ｔｈｅ　ｒａｔｓ` (§30.1, §31.3) ·
`ｆｉｅｌｄ　ｍｉｃｅ` (§41.1) · `Ｈｏｗｅｖｅｒ，` (§23.3) · `Ｓｉｒ！` (§6) · `Ｎｏｗ，` (§28.8, §31.3) ·
`Ｉ　ｓｅｅ．` (§30.3) · `Ｏｈ，` (§24.4) · `Ｗｈａｔ．．．！？` (§28.3 + §5) · `ｔｈｅｙ　ｓａｙ` (§26.6) ·
`ｆｉｎｅ` (§46.2) · `ｆｉｎｉｓｈ` (§48.2, battle sense) · `ｉｎｔｒｕｄｅ` / `ｉｎｔｒｕｄｉｎｇ`
(`chunk_010` L2, same 侵入) · `ｓｐｏｒｔ` (`chunk_012` L4, same 余興) · `ｌｏｔ` (§32.2) ·
`Ｎｏ　ｍｏｒｅ　ｔａｌｋ．` (`chunk_013` L8) · `“…”` for `「」` (§12).

**`なるほど` → `Ｉ　ｓｅｅ．` is correct here and §46.3's forward gap does not reach this chunk** —
that ruling moves なるほど to `Ｉｎｄｅｅｄ．` only where it shares a **bank** with `そうか`, and
**chunk 42 contains `そうか` zero times**, recounted at review. §46.3's named forward risk is
chunk 32, which holds both and is tier-A blocked.

**`つべこべ申さず、` → `Ｎｏ　ｍｏｒｅ　ｔａｌｋ．` (13) is a deliberate reuse, ratified.**
`chunk_013` **rowcheck-line 8** ships `さあ、つべこべ言わず` → `Ｎｏｗ，　ｎｏ　ｍｏｒｅ　ｔａｌｋ．` — the
same idiom in a plain rather than humble-archaic verb form. Different source strings, so §3 is not
engaged, but a fresh word would leave one idiom with two Englishes for nothing.
**`Ｎｏ　ｍｏｒｅ　ｑｕｉｂｂｌｉｎｇ．` (18) is the reserve** if a later unit needs the split;
`ｑｕｉｂｂｌ‐` verified free. ⚠️ That pairing must be confirmed **by reading**: chunk_013's line is
one of the offset lines (§50.7), so a positional harvest mispairs it.

### 50.6 The single §2 departure, ratified

`ですが・・・！？` → **`Ｂｕｔ，　ｓｉｒ．．．！？`** (13). §2 puts politeness in register, not in added
words, and the project has twice declined an added `Ｓｉｒ` — §38.1's `殿` on the name insert and
§48.2's dropped `〜さん`. **What licenses it here is that neither of those reasons applies**:
§38.1's was *"the same sentence names the rank, so an added title would say it twice"*, and
`ですが・・・！？` names nothing, while bare `Ｂｕｔ．．．！？` (**8**, not the PR's 9) leaves a
subordinate's protest with no addressee. It also harmonises with §50.2 — the same speaker answers
`Ｙｅｓ，　ｓｉｒ．．．．` two segments later. Everywhere else in the unit です is carried in register
with no added word (`私がですか・・・。` → `Ａｍ　Ｉ　ｔｏ　ｄｏ　ｉｔ．．．．`; `きゅ、９軍です。` →
`Ｔｈ，　ｔｈｅ　９ｔｈ　Ａｒｍｙ．`, with `Ｔｈ，　ｔｈｅ　９ｔｈ　Ａｒｍｙ，　ｓｉｒ．` (22) rejected for
exactly that reason). **Flagged by the translator rather than applied silently, which is what let
it be ruled on.**

### 50.7 L11, and what `findings.md` §24.2 actually requires

L11 is one of `FLAGS.md` §L2 / `findings.md` §24's eight lines: **no `{FC50}`/`{FC51}` anywhere and
16 text rows against a four-row box.** `rowcheck` reports 21. **The overage is inherited** — 16 in
the pristine source — so CLAUDE.md §6 gate 4 is met, and the in-game question is Blocked 4.

**Verified specifically at review, against a pristine extraction: the source has 16 text entries
plus a trailing blank, the file has 21 plus a trailing blank, every one of the 16 entries survives
in order, and NO TWO ENTRIES ARE MERGED** — the one thing §24.2 forbids. The five extra rows are
splits **inside** single entries, each forced: `本国へ戻られた。` (`ｒｅｔｕｒｎｅｄ　ｔｏ　ｔｈｅ
ｈｏｍｅｌａｎｄ．` = 25), `新しいカーラインのために、乾杯しようではないか。` (27),
`反旗を翻そうというのだな？` (25), `「勝てば正義」…知っておるか？` (the quote alone is 24), and
`歴史など、…できるのだ。` (the source row is 24 JP characters). Precedent for splitting inside such
a line: `chunk_006` L21 (11 → 12 rows) and `chunk_007` L24 (6 → 8), both shipped.

⚠️ **Independent evidence for §L2's pool reading, from a different chunk than §AE6's, and stronger
than the PR claimed.** `はっ！` sits in L11 between two of Helfer's taunts, where a subordinate's
assent makes no narrative sense — yet CLAUDE.md §3 forces `Ｓｉｒ！`, because the form is **7 of 7**
across the shipped tree: `chunk_002` L14 and L20, `chunk_008` L10, **`chunk_013` L2**, `chunk_022`
L5, `chunk_031` L2, `pending/chunk_017` L6. The PR counted 6 of 6 and missed `chunk_013` because
**that line's English is offset by one** — it compresses JP rows 6–9 into EN rows 6–8 and leaves EN
row 9 blank, so from index 10 on `en[k−1]` answers `jp[k]`. Read with the offset,
`jp[11] はっ！ → en[10] Ｓｉｒ！` and `jp[12] しかし、 → en[11] Ｈｏｗｅｖｅｒ，`. **Carried to
`FLAGS.md` §AL for whoever makes the chapter 5/6 in-game visit.**

### 50.8 Recorded, not re-cut — checked at review and not defects

- **Four rows sit at exactly 24 columns and all four are ratified.** 24 is the hard limit and legal;
  §3.2's ≤ 23 is a preference. Each was named with a measured alternative and each alternative
  loses something the source has: `ｄｏ　ｓｏｍｅ　ｒａｔ‐ｋｉｌｌｉｎｇ．` (20) drops 少々;
  `Ｉ’ｍ　ｈｅｒｅ　ｆｏｒ　ｔｈａｔ　ｈｅａｄ！` (23) loses 来た;
  `Ｐｒｉｎｃｅ　Ｔｏｒｉｆ，　ｔｏｏ，　Ｉ　ｈｏｌｄ．` is 26; `“Ｔｈｅ　ｗｉｎｎｅｒ　ｉｓ　ｒｉｇｈｔ”？` (22)
  loses the conditional. The file's histogram is otherwise dominated by 22–23.
- **L2 page 2 goes `TTT.` → `TTTT` and §45.2 rules exactly this** — a source-blank **trailing**
  segment carrying text, no leading blank, no tag added, moved or deleted (L2's `{FFFE}` count is
  unchanged). See §AL on the census method.
- **`野ネズミども。` → `Ｔｈｅｓｅ　ｆｉｅｌｄ　ｍｉｃｅ．` (17) is now byte-identical to `chunk_041`
  L6's rendering of the DIFFERENT string `この野ネズミが。`** (§49.9 ruled chunk 41's side). Two
  source strings, one English row, across two files. No gate sees it, §3 binds identical Japanese
  and is not engaged, and **chunk 42's side is the plural §41.1 actually fixes** — so chunk 42 is
  the clean one. Recorded so it is not "corrected" later in the wrong direction.
- **`ｆｉｎｅ` carries both `立派な` (§46.2) and `いい` in the 余興 frame inside this one chunk** —
  `立派な兵器を` → `ａ　ｆｉｎｅ　ｗｅａｐｏｎ　ｔｏ　ｂｅａｒ，` and `いい余興になるだろう。` →
  `Ｉｔ　ｗｉｌｌ　ｍａｋｅ　ｆｉｎｅ　ｓｐｏｒｔ`, the second forced by `chunk_012` L4's shipped
  `Ｔｈｉｓ　ｗｉｌｌ　ｍａｋｅ　ｆｉｎｅ　ｓｐｏｒｔ`. Two correct rules meeting; recorded rather than re-cut.
- **§32.2's `の奴ら` row glosses `ｌｏｔ` as "a bandit's word where *Carline's men* is an officer's"
  while this line's speaker is an officer** (`９軍の奴らが・・・・！` → `Ｔｈｅ　９ｔｈ　Ａｒｍｙ’ｓ
  ｌｏｔ．．．．！`, 23). **The row explicitly does not fix the word — "the word is not fixed; the
  register is"** — so `ｌｏｔ` stands as one of its three named forms. Recorded so a later unit does
  not read the row as settled; `ｍｅｎ` (§48.2, chunk 37) is the same length.
- **`Ｃｕｒｓｅ　ｉｔ．．．！！` (13) was rejected for `くそっ` and that reason has only got stronger** —
  §47.2 fixes おのれ → `Ｃｕｒｓｅ　ｙｏｕ` and `chunk_041` now ships it twice (§49.4).
- **The stutter takes the comma form** (`きゅ、` → `Ｔｈ，　ｔｈｅ`), following `chunk_025` L13 and
  the direction §L3 sets, not `chunk_000` L2's older hyphen. ⚠️ `FLAGS.md` §AG3 records that stutter
  **capitalisation** is still unfixed and the corpus split 9 : 5; this unit does not settle it.
- **`ヘルファー様っっ！！` → `Ｌｏｒｄ　Ｈｅｌｆｅｒ！！`** — the doubled `っっ` is carried by Helfer's
  immediate rebuke, not by a third `！`, which would change the mark count against the source.
- **`皆で　新しい` carries an internal ideographic space in the source**; it is a mid-row space in a
  normal sentence, not a menu cursor gutter, and is correctly not reproduced as a leading space.
  No source row in this chunk starts with `　`.

### 50.9 Register and speakers — read off the channel byte, not the portrait id (§41.2)

| Channel / tag | Who | Register |
|---|---|---|
| 0, `{FCB0}{=00040000}` / `{=00070000}` | **Helfer** | §11.6 — grandiose and archaic, **no contraction anywhere**, verified line by line |
| 1, `{=00030001}` | **Anselmo** | §14.6 / §15.3 — blustering and superior, **no contractions**; deferential です／ます to Helfer |
| **0**, `{FCB0}{=00030000}` (L7) | **Anselmo again** | ⚠️ **The same portrait id on the other channel** — exactly the trap §41.2 documents |
| 0, `{=00000000}` | **the player side (Kain)** | §7 casual; **the unit's only contraction is his `Ｉ’ｖｅ`** |
| 1, `{=00020001}` (L10) | **unidentified, and deliberately not guessed** | `船よ、{FC00}！船で河を下ったわ！！` — addresses the player by name. ⚠️ **The PR's Flag 14 read the sentence-final `わ` as marking a FEMALE speaker; that inference is REFUTED** by §1's corrected `マラナ` row (40-instance census) and by §49.8, which reads chunk 41's `〜わ` as emphatic **male**. **No rendering depends on it** — the English names nobody and is deliberately neutral — but the inference must not be carried forward |

## 51. Added by script batch 010 (PR #32, merged 2026-09-10)

The item/equipment description table (12 lines × 21 instances = 252) and the Farina–Marvellous
prose window DATA 880–920 (41 lines × 1). 53 unique lines / 293 message instances. Two review
rounds; **five findings at round 1, all five gate-7 failures**, all five fixed. Every width below
is `len()`-measured at review, and every glossary row cited was **re-read on the moved base** —
the base moved twice under this review (§AL4).

### 51.1 Item-table terms — the ten §9 seeds, all promoted and struck

| Japanese | English | Note |
|---|---|---|
| 防御力＋ＮＮ (armour stat row) | `Ｄｅｆ＋ＮＮ` | **The first `防御力` stat rows ever shipped** — DATA 226, 239, 272. **Zero-growth verified by `len()` at review, not assumed: `防御力＋１` 5 → `Ｄｅｆ＋１` 5, growth +0**, and the same for every `攻撃力＋ＮＮ` → `Ａｔｋ＋ＮＮ` row. That property is what makes the armour entries affordable at all against bank 40's 447 bytes. Prose keeps *defence power* (§4) |
| ボウガン | `ｃｒｏｓｓｂｏｗ` | 8 columns. DATA 224 |
| ボウキャノン | `ｂｏｗ　ｃａｎｎｏｎ` | 10 columns, held audibly distinct from ボウガン |
| ひみつの店 | `ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ` | 15 columns. **Settled lowercase on use, as §9 asked, and the reason is recorded: it is NOT a named shop.** Its whole reach is DATA 310, where it appears only in `ひみつの店の会員証` — no `『　』`, no menu. Contrast `『ビーストショップ』` (§12 quotes) and §46.1's gutter-prefixed menu options. Rendered possessively `Ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ’ｓ` |
| 会員証 | `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` | 13 columns — **§9's own stated Alt, taken because the row is tight, which the seed licenses.** `ｍｅｍｂｅｒｓｈｉｐ　ｃａｒｄ` is 15 and costs +48 rather than +44 against bank 40's remaining 75 |
| 鋼鉄の手袋 | `ｓｔｅｅｌ　ｇａｕｎｔｌｅｔｓ` | 15 columns. DATA 272. `腕を守る` compressed to the attributive `ａｒｍ` (§2.1 step 5) — `Ｓｔｅｅｌ　ａｒｍ　ｇａｕｎｔｌｅｔｓ．`, flagged |
| 鉄製の鎧 | `ｉｒｏｎ　ａｒｍｏｕｒ` | 11 columns, British per §4. DATA 239. `動きやすい` → `Ｓｕｐｐｌｅ` (§2.1 step 4); `ｍｏｂｉｌｅ` deliberately avoided because 機動力 → *mobility* is a stat word |
| ダミーよろい１／２ | `ｄｕｍｍｙ　ａｒｍｏｕｒ　１` / `ｄｕｍｍｙ　ａｒｍｏｕｒ　２` | 14 columns. Inside §4's `です` frame → `Ｔｈｉｓ　ｉｓ　ｄｕｍｍｙ　ａｒｍｏｕｒ　Ｎ．`. The precedent was **read at review, not cited**: `batch_001.tsv:6` ships `ダミーぶきです　　　　` → `Ｔｈｉｓ　ｉｓ　ａ　ｄｕｍｍｙ　ｗｅａｐｏｎ．`, dropping the source's trailing full-width padding, which these rows also drop. The article goes on the `自走砲１です！` → `Ｇｕｎ　１` precedent |
| 『カルボナイト』 | `“Ｃａｒｂｏｎｉｔｅ”` | 11 columns with §12 quotes. A named crafting material, DATA 880 ×2 |
| 『ジェムストーン』 | `“Ｇｅｍｓｔｏｎｅ”` | 10 columns with §12 quotes, **held distinct from §33.5's bare lowercase `ｇｅｍｓｔｏｎｅ` for 宝石** exactly as §9 asked — the quoted form is the material's *name* |
| ヒーリング | `ｈｅａｌｉｎｇ` | 7 columns, lowercase common noun. ⚠️ **Not a new form** — `batch_003.tsv:27` and `:29` already ship it; DATA 908 ×2 and 909 ×1 match them byte-for-byte |
| 石版 | `ｔａｂｌｅｔ` | 6 columns, bare lowercase, byte-identical to chunk 30's four instances and `batch_009`'s two. **DATA 300 was the last outstanding instance and §9's row is STRUCK with this merge** |
| ビーストショップ | `“Ｂｅａｓｔ　Ｓｈｏｐ”` (prose) | 12 columns with the quotes. ⚠️ **DATA 899 is PROSE, not a menu — PR #28's correction predicted this and the shipped line confirms it**: `Ａｔ　ｔｈｅ　“Ｂｅａｓｔ　Ｓｈｏｐ”`, §12 quotes for `『　』`, **no leading `　` cursor gutter**. The bare name inside the quotes is byte-identical to §46.1's menu form minus its gutter. §9's row is STRUCK |

### 51.2 New terms first rendered here

| Japanese | English | Note |
|---|---|---|
| 『してんこうせき』 | `“Ｓｈｉｔｅｎ　Ｏｒｅ”` | 12 columns with §12 quotes. A named crafting ore, DATA 906. **Hapax — 1 script, 0 battle, bank 28 only.** `こうせき` is almost certainly 鉱石 → *ore*; `してん` is genuinely ambiguous and is left transliterated rather than guessed (§4.4). ⚠️ `紫電` is **excluded by the reading** — that is *shiden*, not *shiten*; 四天 is likeliest. **Ruled acceptable at review precisely because the reading is open and the alternatives are listed.** Alt *Shitenkouseki* (17), *Four Heavens Ore* (18) |
| シルフ | `Ｓｙｌｐｈ` | 5 columns. Capitalised as a class **name**, on §4's `フリーナイト` → `Ｆｒｅｅ　Ｋｎｉｇｈｔ` / `ビーストマスター` → `Ｂｅａｓｔ　Ｍａｓｔｅｒ`. Hapax — 1 script, 0 battle |
| セイレーン | `Ｓｉｒｅｎ` | 5 columns, same rule. Hapax — 1 script, 0 battle |
| ざます (sentence-final) | carried in **register**, not as a fixed suffix | **RULED at review.** `translation_prompt.md` §2 puts politeness levels with no English lexical equivalent into register and word choice, not added words; §5's ノロ / ゲロゲロ are fixed *words* because they are onomatopoeic tics. `ざます` is the first kind. Carried by affected diction — `ｏｆ　ｔｈｅ　ｖｅｒｙ　ｒｉｃｈｅｓｔ`, `Ｌｏｗｌｙ　ｓｏｌｄｉｅｒｙ　ｓｕｃｈ　ａｓ　ｙｏｕｒ　ｏｗｎ　ｇｏｏｄ　ｓｅｌｖｅｓ`, `ｈａｄ　ｂｅｓｔ　ｂｅ　ｇｏｎｅ`, `ｓｈｏｕｌｄ　ａｎｙｔｈｉｎｇ　ａｒｉｓｅ`, `Ｉ　ｓｈａｌｌ` — plus **one** explicit `，　ｉｆ　ｙｏｕ　ｐｌｅａｓｅ．` at DATA 913. Reach 4 script, 0 battle, bank 28 only, so the ruling binds nothing forward |
| チミ (= 君, affected) | `ｙｏｕｒ　ｏｗｎ　ｇｏｏｄ　ｓｅｌｖｅｓ` / `ｙｏｕ，　ｙｏｕ　ｔｈｅｒｅ` | Same speaker, same treatment. 3 script, 0 battle, bank 28 |
| ああ、 (lament, **not** assent) | `Ａｈｈ，` | 3 columns. **RULED at review.** §6's `ああ` row is scoped to **assent** and §43.1 made that scope binding, so no fixed form governs a lament. `Ｏｈ，` is **out on measurement**: §24.4 gives it to both `おお、` and `ほう、`, and this very message's own file renders `おお、` → `Ｏｈ，` twice at DATA 919/920 — an in-file collision. `Ａｈｈ，` passes §25.3: it is §33.2/§45.5's form for `ああっ、`/`あーっ、`, and **those two have 0 script occurrences in the entire dump** (battle only — re-measured at review), so they cannot meet this line in any bank. Collapsing a lengthened `ああ` onto `ああっ`'s English is the ちっ/チッ/ちッ → `Ｔｓｋ` shape (§36.1) |
| あ〜、 | `Ａｈ〜，` | 3 columns. Transliteration plus the source's own `〜`, which §3.1 permits unchanged. Held distinct from あ、→ `Ａｈ，` (§6), あーあ → `Ａａｈ，` (§23.2) and ああっ、/あーっ、 → `Ａｈｈ，` (§33.2/§45.5) |
| 大砲 | `ｃａｎｎｏｎ` | 6 columns, plural uninflected (`ｃａｎｎｏｎ　ａｒｅ　ｈｉｄｄｅｎ`). Held distinct from §4's 自走砲/固定砲 → `Ｓｅｌｆ‐ｐｒｏｐｅｌｌｅｄ　Ｇｕｎ` / `Ｆｉｘｅｄ　Ｇｕｎ` |
| 競馬場 | `ｒａｃｅｔｒａｃｋ` | **9 columns.** §15.1 fixes the horse-racing vocabulary but never named the venue |
| カジノ | `ｃａｓｉｎｏ` | 6 columns |
| 仇討ち事件 | `ｒｅｖｅｎｇｅ　ａｆｆａｉｒ` | 14 columns. `ｒｅｖｅｎｇｅ` is `chunk_024`'s word for the same Farina killings; `ａｆｆａｉｒ` is `chunk_008`'s for 事件 |
| （民家１） | `（Ｈｏｕｓｅ　１）` | 9 columns. A developer label; `（　）` are §3.1's permitted full-width parentheses |
| ＜アイテム名＞ | `（ｉｔｅｍ　ｎａｍｅ）` | 11 columns. ⚠️ **`＜` and `＞` are outside §3.1's permitted set**, so the brackets are re-cast as the permitted `（　）`. **Confirmed at review, and it sets the precedent for the untranslated `＜ダミーデータ＞` rows at DATA 127–130** |
| 古代文明 | `ａｎｃｉｅｎｔ　ｃｉｖｉｌｉｓａｔｉｏｎ` | Not a new form — `batch_008.tsv:45` already ships it, British `-s-`; matched byte-for-byte. Recorded because the source-word sweep at §AM3 found it, and a key-first sweep would not have |
| 軍人 | `ｓｏｌｄｉｅｒｙ` (collective) | 9 columns, DATA 913. Same root as `batch_002.tsv:9`'s `ａ　ｓｏｌｄｉｅｒ　ｏｆ　Ｃａｒｌｉｎｅ` for the same word, in the collective for a plural address. ⚠️ **Held apart from §30.2's 兵隊さん → `Ｓｏｌｄｉｅｒｓ，` by register**, not by root: `Ｌｏｗｌｙ　ｓｏｌｄｉｅｒｙ` is the snob's word, `Ｓｏｌｄｉｅｒｓ，` the villager's address. They do not co-occur in a message |

### 51.3 RULING — `復興` takes whichever member of its two-member row English wants, and `ｒｅｂｕｉｌｔ` stands

Round 1 found DATA 910 rendering `ファリーナの復興する日` as `ｔｈｅ　ｄａｙ　Ｆａｒｉｎａ　ｒｉｓｅｓ　ａｇａｉｎ`
— **outside §26's row entirely**, and invisible to gate 6 because the row is a unique message.
Round 2 shipped the **verbal `ｒｅｂｕｉｌｔ`** rather than `batch_005`'s nominal `ｒｅｂｕｉｌｄｉｎｇ`,
and offered to force the gerund. **It should not be forced, and the verbal form is ratified.**

> §26's row is `復興 | rebuilding / **rebuild**` — **two members, one nominal and one verbal**, and
> `ｒｅｂｕｉｌｔ` is `rebuild`'s past participle. The row is **not** source-part-of-speech-locked, and
> shipped work proves it: **`batch_009.tsv:72` renders the bare noun `この島の復興にも` verbally, as
> `Ｉ　ｍｕｓｔ　ｈｅｌｐ　ｒｅｂｕｉｌｄ`** — read at review, not cited. So the corpus already picks the
> member English wants. Forcing the gerund here would put this unit *out* of step with shipped work.
> Here the source is itself verbal (`復興する日`), so the verbal member is also the closer match and
> keeps 待ちどおしい's forward-looking sense. §27.1's `愛用` → **`ｆａｖｏｕｒ` — voice and tense follow
> the source** is the governing analogy.

`ｒｅｂｕｉｌｄｉｎｇ` (`batch_005.tsv:44`, `:45`), `ｒｅｂｕｉｌｄ` (`batch_009.tsv:72`) and `ｒｅｂｕｉｌｔ`
(`batch_010.tsv:61`) are **one row correctly conjugated three ways**. ⚠️ **This was the wave's
candidate fifth wrong correction and it was declined**: the round-1 finding was that *neither*
member was used, not that the nominal one was owed.

### 51.4 The four other round-1 gate-7 failures, and what each teaches

| Row | What shipped at round 1 | Fix | Why gate 6 was blind |
|---|---|---|---|
| §37.1 `実権` → `ｒｅａｌ　ｐｏｗｅｒ` | `ｗｈｏ　ｒｕｌｅｄ　Ｆａｒｉｎａ．` | Page repacked to 16/21/18/20, `TTTT` unchanged | ⚠️ **§37.1's own census NAMES THIS EXACT LINE** (`当時、ファリーナの実権を`) — re-measured at review: 2 script-unique lines, DATA 386 untranslated + DATA 891, plus 1 battle. **The third unit in wave 8 to fail on a row that names its own line.** The fix was a **repack, not a word-swap**, because the paraphrase had displaced the term rather than occupying a slot it could drop into |
| §30.2 `兵隊さん` → `ｓｏｌｄｉｅｒｓ` | singular `Ｓｏｌｄｉｅｒ，` ×2 | `Ｓｏｌｄｉｅｒｓ，` ×2 | The **byte-identical source fragment** `兵隊さん、` is already shipped plural in `tl/battle/chunk_026.txt` (`Ｓｏｌｄｉｅｒｓ，{FFFE}ｙｏｕ　ｓａｖｅｄ　ｕｓ！`, paired on the tag prefix at review) — but the whole messages differ, so gate 6 pairs nothing |
| §38.x `よろしく　頼む` → `Ｉ　ｓｈａｌｌ　ｃｏｕｎｔ　ｏｎ　ｙｏｕ．` | `Ｄｏ　ｌｏｏｋ　ａｆｔｅｒ　ｕｓ　ａｇａｉｎ` | The fixed form, 3 rows 16/22/21, no shape change | The row's own description — *a superior entrusting a future task* — describes this speaker exactly. Now the **4th** byte-identical instance. ⚠️ **Side effect, and it is an improvement:** `ざます` now carries one explicit marker rather than two, which is what §51.2's register-only ruling wants; a repeated fixed tag is what §5 reserves for *word* tics |
| §17.1 `ホビット` → lowercase in prose | `Ｗｅ　Ｈｏｂｂｉｔｓ` | `Ｗｅ　ｈｏｂｂｉｔｓ`, identical width, 0 bytes | §17.1 says *lowercase in prose* with no sentence-position carve-out, and §40.1's 魔族 row calls ホビット → hobbit **the canonical case**. ⚠️ **Exposed §4.3 debt in merged work — see §AM2** |

### 51.5 Confirmed without change

`Ｃｏｍｅ　ｉｎ！！` + `Ｗｅｌｃｏｍｅ　ｔｏ　ｔｈｅ　ｃａｓｉｎｏ！` at DATA 885 **spends §34.5's reserve exactly as
reserved** — §34.5 quotes this very message and names `Ｃｏｍｅ　ｉｎ` (7 columns) as the reserve on the
`いらっしゃいませ` side. Read at review. **The bank-26 `Ｗｅｌｃｏｍｅ` collision is now discharged and the
reserve is spent.** · `後衛` → `ｂｅｈｉｎｄ` is §26.3's recorded width variant, width-forced on a full
`.TTTT` page, and flagged. · `神父様たち` → `ｔｈｅ　Ｆａｔｈｅｒｓ` is not §24's vocative row but follows its
ナコール様 ruling — 様 as the title of the man's station. · `船長` at DATA 904 is the **common noun**,
lowercase `ａ　ｃａｐｔａｉｎ`, not §40.1's `(address)` row; and it is **not** one of §48's three
outstanding `マーシュ` lines (FILE 870 / 1330 / 1379), though whoever takes FILE 1330 should read it
beside this one. · `Ｉ　ａｍ　ｇｒａｔｅｆｕｌ．` at DATA 920 is **uncontracted deliberately and correctly** —
`batch_008.tsv:60` ships `Ｉ　ａｍ　ｔｒｕｌｙ　ｇｒａｔｅｆｕｌ．` for 感謝しております; a round-1 register nit
against it was **withdrawn** at round 2 when the source-word sweep found the incumbent.

---

## 52. Added by script batch 011 (PR #34, merged 2026-09-10)

The town and shop NPCs, `script_unique.txt` **DATA 647–706** (= FILE 652–711), banks 14–18: the
frog merchant, a woman's item shop and the members-only door, a keigo monster shop and the
fruit-tree shop across three visit states, a rough dealer, and Maya's undead shop. 60 unique lines
/ 60 instances, **+2,474 bytes** across five banks, none of them tight. Merged at round 2; round 1
returned one finding (§52.4).

**Every width below was measured with `len()` at review, not carried from the PR** — all fifteen of
the PR's own figures reproduced exactly, and are recorded here as verified rather than as claimed.

### 52.1 Shop and town vocabulary first rendered here

| Japanese | English | Note |
|---|---|---|
| メンバーカード | `ｍｅｍｂｅｒ’ｓ　ｃａｒｄ` | 13 columns, lowercase. **Promoted from §9's wave-9 seed onto the seed's own listed Alt, not onto its proposed `Ｍｅｍｂｅｒ　Ｃａｒｄ` (11)** — the seed asked for exactly this decision ("settle it on use, say which and why"). `ひみつの店` and `メンバーショップ` are one shop: DATA 674 (mine) is the members-only door, DATA 1348 says a `メンバーカード` is needed to enter, and §51.1's shipped `会員証` → `Ｔｈｅ　ｓｅｃｒｅｔ　ｓｈｏｐ’ｓ　ｍｅｍｂｅｒ’ｓ　ｃａｒｄ．` (DATA 310, count 21) lands in **21 banks including bank 15 — batch 011's own**, so §25.3's co-occurrence test **fails** and two casings of one object would meet in one bank. **Width forced nothing**: 13 vs 11, and D674's row measures 14 against 24. ⚠️ **DATA 1348 is untranslated and must take this form.** `batch_012` (PR #35) carries **0** `メンバーカード`, verified at review |
| ミュートフルーツ | `Ｍｕｔｅ　Ｆｒｕｉｔ` | 10 columns. **Promoted from §9's wave-9 seed, used exactly as seeded, and struck — DATA 690 is the corpus's only instance, so the term is exhausted.** Unquoted, because its source is unquoted |
| 『進化の木の実』 | `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”` | 18 columns with the quotes; `ａ　“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”．` is 21 on D689's row. `『…』` → `“…”` per §12. **The LONG `Ｙ　ｏｆ　Ｘ` form, on the corpus's two decided precedents for a `『Ｘの Ｙ』` item name** — §12's `『知識の書』` → `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”` (19) and §33.1's `『火の水晶』` → `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”` (17), where the short compound `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` was explicitly considered and **"never fired"**. ⚠️ **CROSS-UNIT AND LIVE — see §52.5. `batch_013` (PR #36) renders the same item `“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”` and must change to this form.** 2 script instances, banks **16** (here) and **29** (batch 013), 0 battle |
| 木の実 | `ｎｕｔ` | 3 columns, lowercase. **Not a new form — it records the shipped incumbent**: `batch_007.tsv:21` ships `何かの木の木の実。` → `Ａ　ｎｕｔ　ｆｒｏｍ　ｓｏｍｅ　ｔｒｅｅ．`, read at review. ⚠️ **Bare `実` stays `ｆｒｕｉｔ` (5)** — that split is load-bearing: it is what lets D689's tree "bear fruit" and still yield a "Nut", and D690's `ミュートフルーツ` sit beside both |
| 当店 | `ｏｕｒ　ｓｈｏｐ` | 8 columns. The shopkeeper's own formal word for the shop. D685, D686, D689, D690. **0 instances in `battle_dump.txt`**, counted at review — genuinely first rendered here. ⚠️ D690 compresses it to `ｕｓ` on a 23-column row where the full form cannot fit (the speaker *is* the shop); that variant is width-forced, flagged in the PR and recorded at §AN |
| 大繁盛 | `ｂｏｏｍｉｎｇ` | 7 columns. D689, D690. **0 battle instances.** ⚠️ **The additive `も` of `当店も大繁盛` is carried by `，　ｔｏｏ` in BOTH lines** — see §52.4 |
| 取り扱う | `ｄｅａｌ　ｉｎ` | 7 columns. `それは　うちでは取り扱ってないの。` → `Ｗｅ　ｄｏｎ’ｔ　ｄｅａｌ　ｉｎ　ｔｈａｔ　ｈｅｒｅ．` (D670), `かわいい　モンスターを取り扱っております。` → `ｗｅ　ｄｅａｌ　ｉｎ　ｃｕｔｅ　ｍｏｎｓｔｅｒｓ．` (D675). One verb, two registers, one English |
| 芽を出す | `ｓｐｒｏｕｔ` | 6 columns. D688. ⚠️ **The key is split across a `{FFFE}` in the source** (`木の実は、芽を{FFFE}出し始めました`), so a gate-6 exact-key grep cannot pair it — recorded here instead |
| 裏の庭 | `ｇａｒｄｅｎ　ｏｕｔ　ｂａｃｋ` | 15 columns. D688, the shop's back garden where the nut is planted |
| 静まりかえる | `ａｌｌ　ｉｓ　ｈｕｓｈｅｄ` | 13 columns. D700, the narration entering Maya's mansion: `館の中は静まりかえっている・・・。` → `Ｉｎｓｉｄｅ　ｔｈｅ　ｍａｎｓｉｏｎ　ａｌｌ　ｉｓ　ｈｕｓｈｅｄ．．．．` ⚠️ **`・・・。` is FOUR dots under §3.1 and the English has four** — verified by counter at review. `館` → `ｍａｎｓｉｏｎ` is §34.1's existing form (`chunk_035` L2), not a new one |
| 子 (of a monster) | `ｌｉｔｔｌｅ　ｏｎｅ` | 10 columns. `どの子に　なさいます？` → `Ｗｈｉｃｈ　ｌｉｔｔｌｅ　ｏｎｅ？` (D677, keigo), `どの子に　する？` → `Ｗｈｉｃｈ　ｌｉｔｔｌｅ　ｏｎｅ　ｉｓ　ｉｔ？` (D702, Maya), `他の子も` → `ｔｈｅ　ｏｔｈｅｒ　ｌｉｔｔｌｅ　ｏｎｅｓ` (D706). The shopkeepers call their stock *children*; `ｃｒｅａｔｕｒｅ` would lose the affection the whole scene runs on |
| かわいがる | `ｄｏｔｅ　ｏｎ` | 7 columns. D679 `Ｄｏ　ｄｏｔｅ　ｏｎ　ｉｔ，　ｗｏｎ’ｔ　ｙｏｕ．`, D694 `Ｄｏｔｅ　ｏｎ　ｉｔ　ｆｏｒ　ｍｅ，　ｗｉｌｌ　ｙｏｕ！！`, D704 `Ｔｈｉｎｋ　ｏｆ　ｉｔ　ａｓ　Ｍａｙａ　ａｎｄ　ｄｏｔｅ　ｏｎ　ｉｔ．` One verb across three registers, the register carried by the frame rather than by the verb. **0 battle instances** |
| ゼイタク | `ｅｘｔｒａｖａｇａｎｔ` | 11 columns. D653, in the frog's katakana: `オマエ、ゼイタク。` → `Ｙｏｕ　ｅｘｔｒａｖａｇａｎｔ．` — §5's article- and copula-dropping register, so no `ａｒｅ` |
| くれてやる (menu) | `　Ｇｉｖｅ　ｉｔ　ｔｏ　ｔｈｅｍ` | 16 columns **with the leading cursor gutter**, which is part of the string (prompt §7). D685 |
| やらない (menu) | `　Ｒｅｆｕｓｅ` | 7 columns with the gutter. D685. Held **distinct** from §34.1's `やめておく` → `　Ｌｅａｖｅ　ｉｔ` (9) and from `　いいえ` → `　Ｎｏ` — three menu refusals, three source strings, three jobs |

### 52.2 Incumbents this unit conformed to that the glossary had never recorded

Both were found by §AG6's mirror at review — searching for the English the **source word** already
has, before asking what a new one should be. Neither is a new decision; both are recorded so they
cannot drift, and the unit matches both.

| Japanese | English | Where it was already shipped |
|---|---|---|
| 不思議 | `ｓｔｒａｎｇｅ` | 7 columns. `tl/battle/chunk_034.txt` L5 ships `不思議なことが` → `ｓｔｒａｎｇｅ　ｔｈｉｎｇｓ　ｄｏ`, aligned to the dump at review. **1 battle + 1 script instance in the whole corpus**, and D685's `不思議な木の実ですね！` → `ａ　ｓｔｒａｎｇｅ　ｎｕｔ！` is the second — so the term is **exhausted** |
| またの機会に | `Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ　ｔｉｍｅ` | 22 columns. `batch_007.tsv` L24, L47, L58, L69 all ship `またの　機会に` → `Ｃｏｍｅ　ｂａｃｋ　ａｎｏｔｈｅｒ` / `ｔｉｍｅ．` D683 renders `残念ですが、またの機会に　お越しください。` as `Ｉ　ａｍ　ａｆｒａｉｄ．　Ｄｏ　ｃｏｍｅ` / `ｂａｃｋ　ａｎｏｔｈｅｒ　ｔｉｍｅ．` — the incumbent plus `Ｄｏ` for the keigo `ください`. `残念ですが` takes `Ｉ　ａｍ　ａｆｒａｉｄ．` on `batch_008.tsv:35`'s shipped `残念だけど、` → `Ｉ　ａｍ　ａｆｒａｉｄ，` |
| かわいい | `ｃｕｔｅ` (4) / `ｄａｒｌｉｎｇ` (7) | ⚠️ **A register SPLIT of one source word across two shipped incumbents, not a new word.** `ｄａｒｌｉｎｇ` for Maya's undead shop — her own shipped word, `chunk_011` L3 `さあ、私のかわいい` → `Ｎｏｗ　ｔｈｅｎ，　ｍｙ　ｄａｒｌｉｎｇ` (bank 18, D701/D705). `ｃｕｔｅ` for the keigo monster shop — `chunk_013` L5 `カワイイとこ` → `Ｓｈｅ’ｓ　ｇｏｔ　ａ　ｃｕｔｅ` (bank 16, D675). **Both verified against the battle dump at review, and the banks are disjoint**, so the two never meet. Neither word is invented |

### 52.3 CORRECTION to §42.1 (§4.3) — `で、` has TWO shipped Englishes, and the second was never recorded

**No rendering moves. §42.1's row is not wrong; it is incomplete, and its own clearance sentence
already said so.** The row fixes `で、` → `Ｎｏｗ，` and scopes the clearance to **bank 4**, noting
that `さあ、` (§28.8, also `Ｎｏｗ，`) occupies banks `[1, 5, 16, 23, 24, 41, 42, 43]`. Re-counted at
this review against `dumps/script_dump.txt`, that list is exact — and **bank 16 is in it**, while
`batch_011`'s D689 carries `さあ、これを` and `で、他にご用は？` **inside one message**. So `Ｎｏｗ，`
genuinely cannot serve `で、` in bank 16.

**What the record was missing is that the second English already ships.** Counted at review by
reading the aligned rows, not by positional inference:

```
で、今日はどんな用ノロ？  -> Ｓｏ，　ｗｈａｔ　ｃａｎ　Ｉ　ｄｏ / ｔｏｄａｙ，　ｎｙｏｒｏ？
                          batch_007.tsv L40, L50, L61   bank 3, 3 unique lines / 4 instances
で、どんな　用かしら？    -> Ｎｏｗ，　ｗｈａｔ　ｄｏ　ｙｏｕ　ｎｅｅｄ？        batch_008.tsv L39   bank 4
で、どんな　ご用かしら？  -> Ｎｏｗ，　ｗｈａｔ　ｉｓ　ｙｏｕｒ　ｎｅｅｄ？      batch_008.tsv L49   bank 4
で、今日は　どうした？    -> Ｎｏｗ，　ｗｈａｔ　ｉｓ　ｉｔ　ｔｏｄａｙ？        batch_009.tsv L39
で、ご用は何かな？        -> Ｎｏｗ，　ｙｏｕｒ　ｅｒｒａｎｄ？                batch_009.tsv L56
```

> **Recorded: `で、` → `Ｎｏｗ，` (4) in bank 4 and its siblings, and `Ｓｏ，` (3) where `Ｎｏｗ，` is
> already spent on `さあ、` in the same bank — the latter is an INCUMBENT since `batch_007`, not a
> coinage by this unit.** `batch_011` D687, D688, D689, D690 take `Ｓｏ，` in bank 16. `Ｓｏ，` is
> spent elsewhere only on `ダカラ、` (`chunk_026` L8 `ダカラ、俺タチノ敵！` → `Ｓｏ，　ｙｏｕ　ｏｕｒ
> ｅｎｅｍｙ！`), which is battle and disjoint from banks 14–18.
>
> ⚠️ **PR #34's Flag 3 said `Ｓｏ，` was spent "only on `ダカラ、` in battle chunk 26" and that is the
> incomplete half** — it missed its own strongest evidence. **This makes the choice stronger, not
> weaker**, so nothing changes in `tl/`; only the record does.
>
> ⚠️ **Method note, because it nearly went the other way.** The first census run at this review
> matched only segments *starting* with `で、` and reported the `batch_007` rows as `ｆｏｒｅｓｔ，
> ｎｙｏｒｏ．` — a **positional-alignment artifact**, `で、今日は` sitting mid-segment there. Had it
> been trusted, a correct record would have been overwritten with a wrong one. A second, direct
> census (`grep` on the whole row, then reading every aligned segment) found the real incumbent.
> **A census needs its splitter AND its reading.**

### 52.4 The round-2 finding, and what fixed it

Round 1 returned **one** finding: D689 dropped the additive `も` of `おかげで` / `当店も　大繁盛！！`
that the same speaker's near-twin D690 renders `，　ｔｏｏ` four rows later. Not budget- or
geometry-forced. The repack, measured independently at round 2:

```
round 1   Ｔｈａｎｋｓ　ｔｏ　ｙｏｕ，        (14) {FFFE} ｏｕｒ　ｓｈｏｐ　ｉｓ　ｂｏｏｍｉｎｇ！！     (21)  = 35 chars
round 2   Ｔｈａｎｋｓ　ｔｏ　ｙｏｕ，　ｏｕｒ   (18) {FFFE} ｓｈｏｐ　ｉｓ　ｂｏｏｍｉｎｇ，　ｔｏｏ！！  (22)  = 40 chars
delta +5 chars = +10 bytes ; bank 16 free 10,963 -> 10,953 ; {FFFE} 11 -> 11 ; 36 non-{FFFE} tags identical
```

All three additive `も` in the unit now carry — D689 and D690's `当店も` → `，　ｔｏｏ`, and D706's
`他の子も` → `ｔｈｅ　ｏｔｈｅｒ　ｌｉｔｔｌｅ　ｏｎｅｓ　ｔｏｏ．` A full sweep of the unit's twelve `も` at
round 2 found the other nine to be `でも` (conjunction, ×2), `〜てもらう` (auxiliary, ×2), `もの`
(noun), `とっても` (intensifier) and `他にも` in the shop's stock *anything else?* formula (×3), none
of them the additive particle.

### 52.5 ⚠️ LIVE cross-unit row — `『進化の木の実』` binds PR #36

`batch_013` (PR #36, **open and unreviewed at this merge**) renders the same named item
`“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”` at its DATA 952 / file L52, against this unit's `“Ｎｕｔ　ｏｆ
Ｅｖｏｌｕｔｉｏｎ”`. Neither form was in this glossary when either unit was written, so neither
translator was overriding a ruling.

> **Ruled for the LONG form, and `batch_013` changes.** The corpus's two *decided* `『Ｘの Ｙ』` item
> names both take `Ｙ　ｏｆ　Ｘ` — §12's `“Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ”` and §33.1's
> `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”`, the latter recording that the short compound `Ｆｉｒｅ　Ｃｒｙｓｔａｌ`
> was weighed and **"never fired"**. `batch_011` merged first and now *is* the shipped work.
> (§9's `“Ｆａｉｒｙ　Ｃａｋｅ”` and `“Ｎｏｒｔｈ　Ｗｉｎｄ　Ｓｙｒｕｐ”` are compounds but are **seeds, not
> decisions**, and the Syrup row documents its compound as width-forced at 25 columns.)
>
> ⚠️ **Width decides nothing, and both directions were measured with `len()` before ruling:**
> `batch_013`'s row becomes `“Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ”？` = **19** columns against its current
> 16 — inside the box, **no re-flow**; and conversely `ａ　“Ｅｖｏｌｕｔｉｏｎ　Ｎｕｔ”．` would have
> been 18 here against the shipped 21, so this unit could have gone either way too.
> The banks are **16 and 29 — disjoint**, so §25.3 is not engaged; this is a naming divergence only.

### 52.6 Confirmed without change

`いらっしゃいませ` / `いらっしゃい` / `イラッシャイ` → `Ｗｅｌｃｏｍｅ` + the source's own punctuation
(§34.1) across all **8** instances, including D688's `！！`. ⚠️ **§34.5's `Ｃｏｍｅ　ｉｎ` is a
*reserve*, scoped to the bank-26 `ようこそ` collision, and §51.5 records it as already spent and the
collision discharged — so it does not reach banks 14–18.** The wave-9 dispatch table asserted a
corpus distinction here that does not exist; see `FLAGS.md` §AN for the generic cause. ·
`貼り紙 / 棚卸し / 休業いたします` (§34.1) — that row *names* unique 647, and D647's first two rows
are **byte-identical** to `batch_006.tsv` L57, with the frog copy's own 4-space (not 2-space)
indent, its `。` → `．` where the hobbit's tic absorbs the stop, and its 7-space `ゲロゲロ」` →
`Ｒｉｂｂｉｔ”` row. · §34.1 `毎度あり` *names* unique 651 → `Ｍａｎｙ　ｔｈａｎｋｓ，　Ｒｉｂｂｉｔ．`, and
§34.6 *names* unique 652 → `Ｒｉｂｂｉｔ？`; both conform. · §34.1 `お客様` **dropped, carried by the
second person** at D688–D690, on that row's own terms. · §32.4/§35 `あら？` → `Ｍｙ？` ×2 and
`あら、` → `Ｍｙ，`. · `あれ？` → `Ｗｈａｔ？` matching `batch_006.tsv:50`. · §3/§34.1 `ジュエル` ×9 →
`Ｊｅｗｅｌｓ` ×9, **0** bare singular and **0** `Ｇｅｍ`. · §5 `ゲロゲロ` ×9 → `Ｒｉｂｂｉｔ` ×9, each
with the source's own mark. · §42.1/§42.2's `ご用` family: D661 and D701 both render
`どんな　ご用かしら？` as `Ｗｈａｔ　ｉｓ　ｙｏｕｒ　ｎｅｅｄ？`, byte-identical to each other and to
§42.1's shipped clause for DATA 492. · §17.2 kana-variant collapse `ええと` onto §34.1's `えーと` →
`Ｅｒｍ，` (D668, bank 15 against §34.1's bank 12 — disjoint). · §7 Maya's third-person
self-reference kept at D704 (`Ｔｈｉｎｋ　ｏｆ　ｉｔ　ａｓ　Ｍａｙａ`). · ⚠️ **The PR's "Reuses recorded"
list credits `妖精` → `ｆａｉｒｙ` and a `ジェム`/`ジュエル` split this unit's source does not contain
— measured at review, `妖精` 0, `ジェム` 0, `ｆａｉｒｙ` 0, `Ｇｅｍ` 0 — so neither is carried into this
section.**

## 53. Added by script batch 013 (PR #36, merged 2026-09-11)

The port town's tavern (Korneff), the item shop and cake girl, and the old tutor's numbered
`戦術講座` tactics-lecture series. DATA 921–978, banks 28 and 29. Section number taken by **reading
`glossary.md` at commit time** — it ended at §52; **PR #35 had not integrated.**

### 53.1 Promoted from §9 PROVISIONAL — all used exactly as seeded, except one corrected below

| Japanese | English | Note |
|---|---|---|
| ウエイト / ウエイト値 / `『ウエイト値』` | `Ｗａｉｔ` (4) / `Ｗａｉｔ　ｔｉｍｅ` (9) / `“Ｗａｉｔ　ｔｉｍｅ”` (11) | Seeded form used as seeded, matching the incumbent at `tl/battle/chunk_000.txt:5`. Census verified at review: bare `ウエイト` 7×, `ウエイト値` 2×, unquoted `Ｗａｉｔ　ｔｉｍｅ` **2** (D960, D977), quoted `“Ｗａｉｔ　ｔｉｍｅ”` **1** (D977, whose source `『ウエイト値』` is quoted — §12 applied) |
| 「待ち時間」 | `“ｗａｉｔｉｎｇ　ｔｉｍｅ”` (15) | 1×, D977, the corpus's only instance. Held apart from `Ｗａｉｔ　ｔｉｍｅ` in the same sentence, as the seed required |
| 戦術講座（第Ｎ回） / 講座Ｎ | `ｔａｃｔｉｃｓ　ｌｅｃｔｕｒｅ` (15) / `Ｌｅｃｔｕｒｅ　Ｎ` (9) | One form serves prose (6×) and the menu index. The Alt `ｌｅｓｓｏｎ` was **not** needed — no menu row was tight; the widest lecture row is `　Ｌｅｃｔｕｒｅ　６：ｎｅｕｔｒａｌ　ｕｎｉｔ` at **23** |
| `『妖精のケーキ』` | `“Ｆａｉｒｙ　Ｃａｋｅ”` (12) | D932–934, 937 |
| `『北風のシロップ』` | `“Ｎｏｒｔｈ　Ｗｉｎｄ　Ｓｙｒｕｐ”` (18) | D933, 934, 950, 951. At D951 the name is split across a `{FFFE}` **exactly at the word space** — verified at review, one name, not two forms |
| `『スーパージュエル』` | `“Ｓｕｐｅｒ　Ｊｅｗｅｌ”` (13) | D945, D946 |
| ゲストユニット | `ｇｕｅｓｔ　ｕｎｉｔ` (10) | D962, 969, 970 — the prose form. Kept apart from the promoted screen label `『ＧＵＥＳＴ　ＵＮＩＴ』` → `“ＧＵＥＳＴ　ＵＮＩＴ”`, which D970's lecture body reproduces unchanged. Menu rows take the **singular lemma**: `　Ｌｅｃｔｕｒｅ　５：ｇｕｅｓｔ　ｕｎｉｔ` = 21 against 22 plural |
| インターミッション | `Ｉｎｔｅｒｍｉｓｓｉｏｎ` (12) | D978 ×2, as a place/phase name. ⚠️ **Still open against §Z1 / Blocked 7** — nothing in DATA 921–978 settles whether it names an on-screen menu label. Flagged, not assumed; see FLAGS §AO5 |
| パラメータ | `ｓｔａｔ` (4) | D975, `パラメータの個別アップ` → `ｒａｉｓｉｎｇ　ｓｉｎｇｌｅ　ｓｔａｔｓ` |
| ＳＳ技能 | `ＳＳ　ｓｋｉｌｌ` (8) | D945, `ＳＳ` kept full-width as the source has it |
| ローテーション | `ｒｏｔａｔｉｏｎ` (8) | D978, the corpus's only instance |

⚠️ **`バニシュジュエル` — THE §9 SEED WAS WRONG ON SUBSTANCE AND IS CORRECTED HERE, NOT SILENTLY.**

| Japanese | English | Note |
|---|---|---|
| `『バニシュジュエル』` | `“Ｖａｎｉｓｈ　Ｊｅｗｅｌ”` (14) | The §9 seed read "unquoted in its source, so unquoted in English" and gave the bare figure. **That is wrong.** D946's source is `『バニシュジュエル』` — **quoted**, and it is the only occurrence in the corpus (`『バニシュジュエル』` = 1, bare `バニシュジュエル` = 1, i.e. the same instance). §12 therefore applies. Both widths `len()`-measured at review: bare `Ｖａｎｉｓｈ　Ｊｅｗｅｌ` = **12**, quoted `“Ｖａｎｉｓｈ　Ｊｅｗｅｌ”` = **14**. The translator caught this against its own seed; the §9 row is corrected as well as struck |

⚠️ **`『極上のワイン』` STAYS LIVE at §9 / §38.1.** That row is struck by whichever of PR #35 / #36
merges **second**, and **#35 had not merged when this section was written** — verified against
`git log` at commit time, not inferred from an agent's status. `batch_013` renders it
`“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` (14 quoted) at D934 and D939, exactly as the seed directs; `batch_012`
(DATA 370–373) still has to. **Whoever integrates #35 strikes it.**

### 53.2 New rows

| Japanese | English | Note |
|---|---|---|
| 編成画面 | `Ｆｏｒｍａｔｉｏｎ　ｓｃｒｅｅｎ` (16) | D974. The **screen name**, capitalised as a named screen. Distinct from the existing `編成` → "form (your units)", the **verb** sense that `batch_005` already ships as *put ... on the front line*. `編成` occurs once in this unit and only inside `編成画面` — verified at review |
| ナイト (as a class gloss) | `Ｋｎｉｇｈｔ` (in `Ｃａｖａｌｒｙ　（Ｋｎｉｇｈｔ）`, 16) | D976, `騎兵（ナイト）`. Capitalised on the `フリーナイト` → `Ｆｒｅｅ　Ｋｎｉｇｈｔ` convention, not the lowercase `ダークナイト` → dark knight one, because this glosses a named class. `騎兵` → `ｃａｖａｌｒｙ` matches the incumbent in `batch_001` and `chunk_002` |
| `『こおりのゆびわ』` | `“Ｉｃｅ　Ｒｉｎｇ”` (10) | D924, D947. Re-measured at review: **10**, not 12 |
| かぜ薬 | `ｃｏｌｄ　ｍｅｄｉｃｉｎｅ` (13) | D953. **Not a new form** — matches the incumbent already shipped in `batch_006`. Unquoted in its source, so unquoted here |
| 材料 | `ｉｎｇｒｅｄｉｅｎｔｓ` (11) / `ｍａｔｅｒｉａｌｓ` | **Sense split.** Cake sense → `ｉｎｇｒｅｄｉｅｎｔｓ` (D950, 953, 954); weapon-crafting sense → `ｍａｔｅｒｉａｌｓ` (D936, shipped as `Ｗｅａｐｏｎ　ｍａｔｅｒｉａｌｓ`, 16), which matches what `batch_010` already ships for the same crafting sense |
| `『貯まり』` | `“ｂｕｉｌｄ　ｕｐ”` (10) | D974. Quoted because the source is quoted; `batch_005` already ships `ｂｕｉｌｔ　ｕｐ` for the same mechanic |
| 棚からぼた餅 | `Ａ　ｔｒｕｅ　ｗｉｎｄｆａｌｌ．` (16) | D978. Idiom for idiom, and the same image class (an unearned good thing falling to you), not an unrelated English idiom |
| 犬猿の仲 | `Ｌｉｋｅ　ｃａｔｓ　ａｎｄ　ｄｏｇｓ` (18) | D976. The English idiom for the same relation. Split across a `{FFFE}` at the word space between `ｃａｔｓ` and `ａｎｄ` — confirmed at review |
| 幻の | `ｆａｂｌｅｄ` (6) | D939, `あの幻の酒` → `Ｔｈａｔ　ｆａｂｌｅｄ　ｄｒｉｎｋ` |
| 高くつく | `ｓｔｅｅｐ` (5) | D941 |
| ふんだくる | `ｆｌｅｅｃｅ` (6) | D941 |
| 鉄クズ | `ｓｃｒａｐ　ｉｒｏｎ` (10) | D921 |
| 出撃 | `ｓｏｒｔｉｅ` (6) | D978, `１回出撃を休ませれば` → `ｒｅｓｔ　ｔｈｅｍ　ｆｏｒ　ｏｎｅ　ｓｏｒｔｉｅ` |
| なあんだ | `Ｗｈｙ，` (4) | D951 |
| おう、 | `Ｏｈ，` (3) | D937. 0 incumbents in shipped work — verified at review |
| ん〜、 | `Ｈｍｍ，` (4) | D925, D948 |
| ＡＧＬ | `ＡＧＬ` (3) | D977, kept full-width and unexpanded, as the source leaves it. `素早さ` is **0×** in this source and no stat name was coined for it |
| − (U+2212) | matchup-chain separator | D976. The source's `→` arrows are outside the renderable charset. Rendered as a chain closed by repeating the first term (`Ｃａｖａｌｒｙ　（Ｋｎｉｇｈｔ）　−　ｓｗｏｒｄｓｍａｎ　−　ｍａｒｔｉａｌ　ａｒｔｉｓｔ　−　ｃａｖａｌｒｙ．`), with an explicit legend row `ｗｉｔｈ　ｅａｃｈ　ｂｅａｔｉｎｇ　ｔｈｅ　ｎｅｘｔ` so the **direction** the arrow carried is not lost. The legend is added text, and it is added **to compensate for a charset loss**, not to explain — that is the only ground on which §2 allows it |
| ・ as a list **bullet** | `＊` | D972. §45.7 gives `・`-as-separator → a space; this is `・` at the head of a list item, and `・` is not renderable. The three separator `・` in this unit (`緑・赤・青`, `武器・防具`) take English list punctuation instead, per §45.7 |

### 53.3 Recorded at review — the reviewer's rows, not the PR's

| Japanese | English | Note |
|---|---|---|
| まあ、 | `Ｍｉｎｄ　ｙｏｕ，` (9) — **concessive sense only** | D939, D941. ⚠️ **THE INCUMBENT IS RECORDED HERE DELIBERATELY, because §AL1 says a new word must be weighed against what the source word already carries.** `まあ、` has **no glossary row**, and two shipped lines render it `Ｗｅｌｌ，` — `chunk_004` `まあ、いいわ。` and `chunk_038` `まあ、協力するといっても`. It was **not** changed at review, on measurement: `Ｗｅｌｌ，` is not `まあ、`'s dedicated form but a **many-to-one sink serving seven different Japanese heads** (`じゃ、しょうがな` ×3, `では、仕方がない` ×2, `そりゃ、よかった`, `ま、でも、`, `どうだ、シロン？`, and the two `まあ`), and `batch_013` has already spent `Ｗｅｌｌ，` / `Ｗｅｌｌ　ｔｈｅｎ，` **nine times** on other Japanese, so collapsing `まあ、` into it would increase the overloading rather than reduce it. **A later unit may overturn this — but deliberately, from this row, not by accident** |
| おや、 | `Ｏｈ？` (3) | D956, the tutor's opener. **No prior row existed and the PR did not propose one** — recorded at integration. ⚠️ Note it renders a source **comma** as a question mark, which is what keeps it distinct from this unit's `おう、` → `Ｏｈ，` (§53.2). If a later unit needs `おや、` in a non-interrogative position, that distinction has to be re-made some other way |
| `『してんこう』` (bare, without 石) | `“Ｓｈｉｔｅｎ　Ｏｒｅ”` (12) | D943. **Takes the existing `『してんこうせき』` row's form unchanged** — one mineral, one English, which is right. Recorded only because that row's note reads "**Hapax — 1 script, 0 battle**" and **that is now stale**: the corpus has two instances under two source spellings, DATA 906 (`してんこうせき`) and DATA 943 (`してんこう`) |

---

## 54. Added by script batch 012 (PR #35, merged 2026-09-11)

**The unit:** `dumps/script_unique.txt` DATA **355–415** — 61 unique lines / 63 message instances /
5,797 readable JP characters. Banks 0, 1, 2, 42, 43; **bank 2 is the tight one and lands at 1,607
free (39,353 / 40,960 used)**. Instance-weighted growth **11,704 bytes**, realised ratio **1.991×**
JP characters — under the 2.10× planning model. Merged at round **3**, the last permitted, after
five gate-7 terminology fixes costing **+2 bytes** net. Section number taken by **reading
`glossary.md` at commit time** (it ended at §53), not reserved.

### 54.1 New entries

| Japanese | English | Note |
|---|---|---|
| 閣下 (`ヘルファー閣下`) | `Ｈｉｓ　Ｅｘｃｅｌｌｅｎｃｙ` / `Ｈｉｓ　Ｅｘｃｅｌｌｅｎｃｙ　Ｈｅｌｆｅｒ` | **14 bare, 21 with the name.** ⚠️ **`閣下` had NO ruling anywhere in this glossary and this sets one — deliberately NOT collapsed onto §1's `ヘルファー様` → `Ｌｏｒｄ　Ｈｅｌｆｅｒ`.** Two source honorifics, two English forms, on the split §41.6 makes for `王子` / `王子様`. With §24.1's `ヘルファー司令官` → `Ｃｏｍｍａｎｄｅｒ　Ｈｅｌｆｅｒ` that is **three source honorifics for one man and three English forms**, which is what the source does. `Ｅｘｃｅｌｌｅｎｃｙ` verified free across `tl/` and `pending/`. **A hapax — 1 script (DATA 392) + 0 battle**, so nothing inherits it. Alt `Ｙｏｕｒ　Ｅｘｃｅｌｌｅｎｃｙ` for a vocative, **unspent** |
| 『獅子の勲章』 / 獅子の勲章 | `“Ｍｅｄａｌ　ｏｆ　ｔｈｅ　Ｌｉｏｎ”` / `Ｍｅｄａｌ　ｏｆ　ｔｈｅ　Ｌｉｏｎ` | **17 bare, 19 quoted.** The plot item §32.5 named and left to whoever rendered it. `勲章` → `ｍｅｄａｌ` is §32.1's, unchanged; `『…』` → `“…”` is §12's. The `Ｘ　ｏｆ　Ｙ` shape follows `『火の水晶』` → `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”` (§33.1) and `『闇の紋章』` → `“Ｅｍｂｌｅｍ　ｏｆ　Ｄａｒｋｎｅｓｓ”` (§45.1), both of which took the long form. §32.5 states in terms that **獅子 is the animal, which does NOT disturb §1's rejection of `Ｌｉｏｎ` for the katakana name リオン** — and the two stand beside each other in this very unit, `Ｌｅｏｎ` at D386 and D410 against `Ｌｉｏｎ` at D386 and D390, and read distinctly. ⚠️ **THIS ROW STAYS LIVE: reach is 9 `script_dump` instances over 3 unique lines — DATA 386 and 390 (both rendered) and DATA 863, UNTRANSLATED.** Verified at review by the cross-file item-name gate: 2 quoted + 3 bare, all consistent, one file |
| 獅子の紋章 | `ｔｈｅ　ｌｉｏｎ　ｅｍｂｌｅｍ` / `ｌｉｏｎ　ｅｍｂｌｅｍｓ` | **15 columns.** ⚠️ **The source uses TWO words for one object and the distinction is kept.** `勲章` (medal) is what Hoag calls it; `紋章` (emblem) is what **Sykes and Cavia** call it, twice, both times while they do not yet understand what it is (`獅子の紋章・・・ですか？`, `獅子の紋章って２つあるの？`). `紋章` → `Ｅｍｂｌｅｍ` is already §45.1's; **lowercase here** because in these two lines it is not the item's name but the speakers' loose description — the `ｇｅｍｓｔｏｎｅ` / `“Ｇｅｍｓｔｏｎｅ”` split at §51. 2 script instances, both at DATA 386. `ｅｍｂｌｅｍ` verified free |
| 政務大臣 | `Ｍｉｎｉｓｔｅｒ　ｏｆ　Ｓｔａｔｅ` | **17 columns.** `政務大臣のツェペリ卿` → `Ｌｏｒｄ　Ｚｅｐｐｅｌｉ，　Ｍｉｎｉｓｔｅｒ　ｏｆ　Ｓｔａｔｅ` (appositive). A **hapax — 1 script, 0 battle**. `Ｍｉｎｉｓｔｅｒ` verified free |
| ホッジス (`ホッジス殿`) | `Ｈｏｄｇｅｓ` | **6 columns.** The retired officer who teaches tactics in the castle town (DATA 398). `殿` adds **no word**, per §9's `殿` ruling as executed by `batch_007` at unique 427. ⚠️ **A HAPAX, and the cross-unit worry HANDOFF raised is RESOLVED IN THE NEGATIVE at this review: `ホッジス` is 1 line in `script_unique.txt` and 0 in `tl/script/batch_013.tsv`.** batch 013's tactics-lecture NPC is a different, unnamed character, so there is nothing to reconcile. Alt *Hodgis*, *Hoggis* |
| スリ | `ｐｉｃｋｐｏｃｋｅｔ` | **10 columns**, lowercase — a trade, by §17.1's species test and the `探検家` → `ｅｘｐｌｏｒｅｒ` precedent (§21.1). ⚠️ **Reach is far larger than this unit: 27 `script_dump` + 8 `battle_dump` instances over unique DATA 286, 376, 379, 518, 520, 714** — later units inherit it. `スリの奴` at D376 renders the 奴 in the article, not as a second word. Verified free; ⚠️ a substring census will collide with `クロスリー` → `Ｃｒｏｓｓｌｅｙ` (§30.1) — **read the hits** |
| 詐欺師 | `ｓｗｉｎｄｌｅｒ` | **8 columns**, lowercase. A hapax: 1 script (DATA 385), 0 battle. Held **distinct** from `スリ` → `ｐｉｃｋｐｏｃｋｅｔ` — a different crime in a different town. Verified free |
| 行商 | `ｐｅｄｌａｒ` | **6 columns**, British spelling per §4. `行商のフリをして` → `ｈｅ　ｐｏｓｅｓ　ａｓ　ａ　ｐｅｄｌａｒ`. 2 script (DATA 385 here, **DATA 806 untranslated**), 0 battle. Verified free |
| 金の塊 / 銀の塊 / 鉄クズ | `　Ａ　ｇｏｌｄ　ｉｎｇｏｔ` / `　Ａ　ｓｉｌｖｅｒ　ｉｎｇｏｔ` / `　Ｓｃｒａｐ　ｉｒｏｎ` | Menu options at DATA 376, **13 / 15 / 11 columns with the leading `　` cursor gutter**, and the same three nouns reused in the reply branches 377 / 378 / 379. `ｉｎｇｏｔ` verified free; `ｓｃｒａｐ` occurs once elsewhere (`chunk_009`), a different sense in a different store. Held distinct from `ガラクタ` → `ｊｕｎｋ`, which D379 also carries |
| 別にない | `　Ｎｏｔｈｉｎｇ　ｒｅａｌｌｙ` | **15 columns with the gutter.** Held **distinct** from the recruiter menu's `何でもない` → `　Ｎｏｔｈｉｎｇ`, which this unit also ships three times. ⚠️ Its run is **joined to the reply that follows it** — the source has no `{FFFE}` between `　別にない` and `そうですか。` — so the pair must measure ≤ 24 together: measured at review, `　Ｎｏｔｈｉｎｇ　ｒｅａｌｌｙ` + `Ｉ　ｓｅｅ．` = **21** |
| 娯楽施設 | `ａｍｕｓｅｍｅｎｔ　ｈａｌｌ` | **14 columns.** 2 script (DATA 366, 374), 0 battle — both here. `ａｍｕｓｅｍｅｎｔ` verified free, and it also carries the same speaker's bare `娯楽` at DATA 361 (`Ｉｎ　ｌｉｆｅ，　ａｍｕｓｅｍｅｎｔ　ｉｓ　ｐａｒａｄｉｓｅ．`) |
| 工房 | `ｗｏｒｋｓｈｏｐ` | **8 columns.** `セネカ君の工房` → `Ｓｅｎｅｃａ’ｓ　ｗｏｒｋｓｈｏｐ`. ⚠️ **Reach: 6 `script_dump` instances over DATA 363 (here), 744, 788, 1346, 1364, 1365** — five later lines inherit it. Verified free |
| いやはや、 **and** いやあ、 | `Ｄｅａｒ　ｍｅ，` | **8 columns. ONE ROW, KEYED ON BOTH SPELLINGS** — §17.2's one-word/two-spellings shape, exactly as `ええっ` / `えーっ` share `Ｅｈｈ` (§36.1) and 鬼 / オーガ share *ogre*. `Ｄｅａｒ　ｍｅ，` serves **4 rows across the two source strings**: `いやはや、` at DATA 365, 380, 391 and `いやあ、` at DATA 360. A polite speaker's exclamation of strong feeling — **not a negation** — one word doing relief (365), delight (360), dismay (380) and comprehension (391), which is why one English serves it. ⚠️ **§25.3's test FAILS and the collapse is deliberate anyway**: censused over the pristine dump, `いやはや` is script banks **[0, 1]**, `いやあ` is script bank **[0]**, 0 battle each — **shared bank 0**, with DATA 360 / 365 / 380 all in bank 0, in one town, reachable in one visit. That is the point of the collapse, not an objection to it. Held **distinct** from §25.1's `いや` → `Ｎｏ` + punctuation (six times in this unit, including the polite `いえ` at D380), §32.4's `あら` → `Ｍｙ`, and §51's `ああ、` → `Ａｈｈ，` (also here, at D361). `Ｄｅａｒ　ｍｅ` verified free. **Reach 3 + 1 = 4, 0 battle, all four rendered — exhausted, but only once both spellings are counted** |
| 実に　残念です。 | `Ａ　ｒｅａｌ　ｓｈａｍｅ．` | **13 columns.** Held apart from `誠に　残念。` → `Ａ　ｇｒｅａｔ　ｓｈａｍｅ．`, which matches §34.1's shipped `誠に　残念です。` and which this same unit renders at DATA 368 and 370. **Two adverbs, two intensifiers, one noun** — §34.1's own "three source strings, three renderings, one noun" shape, now four. ⚠️ Verified at review that D370 (`誠に　残念。`) and D371–373 (`実に　残念です。`) are a **near-identical pair deliberately held apart**: they share every other segment, and the gate-6 internal group is therefore [371, 372, 373], not [370–373] |

### 54.2 `町長` — the determiner moves, the head noun does not

The seeded `ｔｏｗｎ　ｅｌｄｅｒ` ships bare at **DATA 381** (`Ｔｈｅ　ｔｏｗｎ　ｅｌｄｅｒ　ｉｓ　ｏｕｔ`,
10 columns). At **DATA 386** and **391** the source's own construction forces a genitive:
`この町の町長は、` → `Ｔｈｉｓ　ｔｏｗｎ’ｓ　ｅｌｄｅｒ`, `こんな港町の町長に` → `ａ　ｐｏｒｔ　ｔｏｗｎ’ｓ
ｅｌｄｅｒ`, and a bare repeated `町長がうまく` becomes the pronoun `ｈｅ` where Japanese repeats the
noun and English does not (§2). **The head noun `ｅｌｄｅｒ` is constant; only the determiner moves**
— §41.5's and §42.1's shape, and the same shape as §47's `民衆` → `ｔｈｅ　ｐｅｏｐｌｅ` and §44's
`主人` → `Ｔｈｅ　ｍａｓｔｅｒ`, both of which this unit also carries. A key-first gate 7 flags all
three and all three are conformance.

### 54.3 `王子` — §41.6's referential side is now settled, and the prediction held

§41.6 ruled the **vocative** pair and left the **referential** side open, predicting `ｔｈｅ
Ｐｒｉｎｃｅ`. This unit renders every side of it:

- vocative `王子、` → `Ｍｙ　Ｐｒｉｎｃｅ，` — DATA 390 ×2 (§41.6's `ｍｙ　Ｐｒｉｎｃｅ`, capitalised
  sentence-initially);
- vocative `王子様` → `Ｙ，　Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ！？` — DATA 386, **comma stutter** per §23.2 with
  the repeated word capitalised per §38.4, and the source's own break kept (5 / 18);
- **referential `王子様` → `ｔｈｅ　Ｐｒｉｎｃｅ`** — DATA 386, **exactly the form §41.6 predicted**;
- referential bare `王子` → `ｔｈｅ　Ｐｒｉｎｃｅ` — DATA 386, 390, 391;
- `王子たち` → `ｔｈｅ　Ｐｒｉｎｃｅｓ` (§41.1), used as fixed — ⚠️ **at DATA 390 it denotes Hoag *and
  Cavia*, a prince and a princess**, so the fixed English does slightly more work than it did in
  chunks 25/30. The source does the same thing and the fixed form was not departed from.

⚠️ **One defect the reading review caught that no mechanical gate could.** DATA 391's
`お、王女様・・・・！？` had been drafted as `Ｙ‐Ｙｏｕｒ　Ｈｉｇｈｎｅｓｓ．．．．！？` — but the source word
is **`王女様`, not `王子様`**, and §1 fixes it as *the Princess*. It ships `Ｐ，　Ｐｒｉｎｃｅｓｓ．．．．！？`.
**Gate 7 passed that row** because a row-granular checker sees a correct `Ｐｒｉｎｃｅｓｓ` elsewhere in
the same row; only reading the two lines side by side found it. Recorded because it is precisely
the failure mode a per-row checker cannot see.

### 54.4 Register over a fixed form — three instances, one rule

§43.1 made a **register scope binding over a fixed form**, and this unit exercises it three times
without inventing a word:

- **`そうよ。` → `Ｔｈａｔ　ｉｓ　ｒｉｇｈｔ．`** (D390, Cavia) against §30.6's `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`.
  §14.6 fixes Cavia as contraction-free. **The words of §30.6's form are kept; only the
  contraction is expanded.**
- **`あ、そうそう。` → `Ａｈ，　ｔｈａｔ　ｉｓ　ｒｉｇｈｔ．`** (D376) against §23.2's `Ｔｈａｔ’ｓ　ｒｉｇｈｔ．`.
  The speaker is the **Caucasus mayor**, whose §7 register is literally "`Ｉ　ａｍ`, not `Ｉ’ｍ`".
  ⚠️ `ｔｈａｔ　ｉｓ　ｒｉｇｈｔ` therefore renders **two** source strings inside one unit — `そうそう。`
  in **bank 0** and `そうよ。` in **bank 1**. **§25.3 is MET on both axes: different banks, and no
  message holds both.** §30.6's `Ｅｘａｃｔｌｙ．` reserve stays **unspent**.
- **`ああ、` split three ways by scope, not by three new words**: `Ｙｅａｈ，` for Kain's casual
  assent (D386), the §6 **formal assent** `Ｉｔ　ｉｓ　ｓｏ．` for contraction-free Hoag (D386), and
  §51's **lament** `Ａｈｈ，` at D361. All three are what §6 and §51 already prescribe.

Verified line by line at review: Hoag, Cavia, all three town elders, the Caucasus mayor and Helfer
carry **no true contraction** — Helfer's eighteen rows in bank 2 contain not one apostrophe. The
casino girl (355), the party's `{FC50}`/`{FC51}` voices (386–388) and the castle guard (411) do.

### 54.5 `とにかく` — §36.2's register split, applied and confirmed

`とにかく` → `Ａｎｙｗａｙ，` at **D386** (a speaker who contracts three times in the same message:
`Ｉｔ’ｓ`, `ｗｅ’ｖｅ`, `ｗｏｎ’ｔ`), and → `Ｉｎ　ａｎｙ　ｃａｓｅ，` at **D390** (Hoag) and **D391**
(the port-town elder), both contraction-free. §36.2 splits it on **register** and that is exactly
what the unit does.

### 54.6 Reuses that were verified, not assumed

- **`ベルナール教会` → `Ｂｅｒｎａｒｄ’ｓ　ｃｈｕｒｃｈ` is a REUSE, not a promotion, and it is NOT added
  here.** ⚠️ **A round-1 review asked for it as a promotion "so the integration commit strikes the
  §9 row"; the translator declined with evidence, twice, and the decline is CORRECT.** Checked
  independently at the merge review: the only `ベルナール` row in this glossary is the **§14.2
  main-table entry**, there is **no §9 row to strike**, and the form is already shipped at
  `batch_010.tsv:61` (the byte-identical `ベルナール教会の`) and `batch_005.tsv:28`. §4.6's
  promote-on-first-use is not engaged. **Adding it would have put an instruction into an
  integration commit for a row that does not exist.** ⚠️ A *reach* note is what §14.2 could use:
  `ベルナール教会` is 2 script-unique lines (DATA 391 here, **DATA 910 untranslated**) and
  `ベルナールの教会` 1 more.
- **`トリフ` → `Ｔｏｒｉｆ`** is rendered here at DATA 386 (`Ｐｒｉｎｃｅ　Ｔｏｒｉｆ`) and is **also a
  reuse, not a promotion** — censused at review, it is already shipped byte-identically in **four
  merged units**: `chunk_024`, `chunk_025`, `chunk_042` and `batch_007.tsv:56`. ⚠️ **§9's `トリフ`
  row says "promote in the wave that first renders it" and that wave was wave 6 at the latest; the
  row is STALE DEBT, not this unit's business, and it is deliberately left standing rather than
  struck by a unit that is the fifth renderer.** Flagged for an audit at `FLAGS.md` §AP.
- `よろしく頼むぞ` → §38.1's `Ｉ　ｓｈａｌｌ　ｃｏｕｎｔ　ｏｎ　ｙｏｕ．` at D410, held off §21.2's
  `よろしく` → `Ｇｏｏｄ　ｔｏ　ｍｅｅｔ　ｙｏｕ`; `一族` → `ｋｉｎ` and `皆殺し` → `ｓｌａｕｇｈｔｅｒｅｄ` at
  D390 match merged `chunk_021` L10 word for word, which is what §9's wave-8 note asked for;
  `競馬場` → `ｒａｃｅｔｒａｃｋ` matches `batch_010.tsv:37`; `宮廷第２軍` → `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ`
  takes §20.1's form, **not** §26.3's bare `２ｎｄ　Ａｒｍｙ`, because the source writes the long
  spelling; `ヘルファー司令官` → `Ｃｏｍｍａｎｄｅｒ　Ｈｅｌｆｅｒ` matches `chunk_024`.

### 54.7 `『極上のワイン』` — the cross-unit rule discharged, and the gate that proved it

`batch_012` renders `“Ｆｉｎｅｓｔ　Ｗｉｎｅ”` **four times** (DATA 370–373) and `batch_013` **twice**,
**byte-identical in all six**. `batch_013` (PR #36) merged first and deliberately left §9 / §38.1
live; `batch_012` (PR #35) merged second and **strikes it** — the whole of what the `ルート`
precedent (§29.1 / §30.1) prescribes. The proof is the **cross-file item-name gate**, wave 9's own
invention, re-run at this merge over **45 files (13 script TSV + 32 battle)**: 51 messages carrying
a `『…』`/`「…」`, **45 distinct bracketed names, 7 occurring in more than one file, 0 divergences**;
23 unambiguous one-to-one pairings, 0 divergences. ⚠️ **The naive cross-product returned five
"divergences" and every one was an artifact of a message carrying several names at once** —
`カルボナイト`/`ジェムストーン` (identical {Carbonite, Gemstone} in both files), `ジェム` (common
span `Ｇｅｍｓ`), `ＥＮＴＥＲ`, and `極上のワイン` itself. **Read, not counted**, which is §AO2's
lesson applied. The gate also confirms **§AN4's fix has landed**: `進化の木の実` is now
`Ｎｕｔ　ｏｆ　Ｅｖｏｌｕｔｉｏｎ` in **both** `batch_011` and `batch_013`.
