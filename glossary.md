# Riot Stars — Translation Glossary

Paste this into every translation session, directly under `translation_prompt.md`.

**Every entry here is fixed.** Use the English form exactly as written, everywhere, forever. To
change one, follow §4.3 of the prompt: state the correction explicitly and list every previously
translated line that must be revisited.

Entries in **§9 PROVISIONAL** are *not* decisions — they are names seen in the dumps but not yet
rendered in any translated line. Promote one to its proper table the first time you use it.

Status: covers `script_unique.txt` lines 1–216 (unit, class, monster and equipment descriptions), 984–1001 and 1040–1047 (batch 005), and `battle_dump.txt`
chunks **0, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 20, 33, 34, 35, 40** (prologue + chapters
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
| クレス | Ｃｒｅｓｓ | 少尉 → **Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ** (18+5 columns, never on one row). Court‐martialled alongside Alfred for the failed expedition (script 1236). Alt *Kress*, *Cres* |
| アンゼルモ | Ａｎｓｅｌｍｏ | 中尉 → **Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ**. **Promoted from §14.6**, which already used this form for his register but never fixed the name. 8 columns |
| ゼファー・クリッペン | Ｚｅｐｈｙｒ　Ｋｒｉｐｐｅｎ | 帝国の司令官 → Commander of the Empire. `・` has no glyph in §3.1 and becomes `　`. 14 columns. Alt *Zepher*, *Crippen*, *Klippen* |
| ヘルファー様 | Ｌｏｒｄ　Ｈｅｌｆｅｒ | 様 → **Lord** for a male superior, paralleling 様 → Lady (Rimul §1, Phyllis §14.1). 11 columns. Does not change the §11.1 bare-name entry |
| クリミア | Ｃｒｉｍｅａ | ⚠️ **CORRECTED 2026-09-08 (§4.3, PR #5 review): a PERSON — `クリミア博士`, the designer of the Empire's machine soldiers — not the region §2 filed him as.** Verified in both dumps before moving, not taken from the PR: **5 battle + 64 script occurrences, not one of them a place.** He self-refers in the third person (`この砦は、このクリミアにお任せ下さい。` — *leave this fort to Crimea*, i.e. to me; `またこのクリミアの新型機械兵` — *this Crimea's new machine soldier*), is addressed vocatively twice (`クリミア博士、反乱軍です・・・！！`, `クリミア博士、事は計画通り進んで`), is located **inside** a place (`クロスリーにいるクリミア博士`), and the script's machine-soldier table credits him as their maker (`クリミアの量産型機械兵２号機`). **Already-shipped work agrees**: `tl/script/batch_003.tsv` lines 85, 86 and 94 render that table as `Ｃｒｉｍｅａ’ｓ　ｍａｓｓ‐ｐｒｏｄｕｃｅｄ　…`, `Ｃｒｉｍｅａ’ｓ　ｉｍｐｒｏｖｅｄ　…`, `Ｃｒｉｍｅａ’ｓ　ｆｉｎａｌ　ｍａｃｈｉｎｅ　ｓｏｌｄｉｅｒ．` — a person's possessive, written before anyone noticed the §2 row was wrong. The rendering `Ｃｒｉｍｅａ` is unchanged, so **no translated line needs revisiting** — only the classification was wrong. This is the メルザリオ / ファリーナ shape (§20.1, §2); `FLAGS.md` §K6 deliberately deferred it to this reviewer. 6 columns. See §25.1 |

## 2. Factions, places, ranks

| Japanese | English | Note |
|---|---|---|
| 第９軍 / ９軍 | 9th Army | the player's unit; `９` is full-width in source |
| 第７軍 | 7th Army | Alfred's; `７` full-width, same rule |
| 第３分隊 | 3rd Squad | `３` full-width |
| 分隊長 | squad captain | promoted from PROVISIONAL. Use **squad captain** where 隊長 is written out (ベアトリス, ch.14), **squad leader** for the bare 分隊長 |
| 隊長 | captain | how the player character is addressed. `Ｃａｐｔａｉｎ　{FC00}` = 15 columns; `Ｃｏｍｍａｎｄｅｒ` does not fit alongside the insert |
| 少尉 | Second Lieutenant | 18 columns — will not share a line with a name |
| 中尉 | First Lieutenant | 17 columns — same rule; put the name on the next row |
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
| ホビット / ホビットの村 | Hobbit / Hobbit Village | |
| 龍人族 | dragonfolk | one word, 11 columns. Will not fit a ≤20 class slot as "Dragonfolk descendant" — flag if it is ever needed there |
| トカゲ | lizard | 〜さん as address → **Ｍｉｓｔｅｒ　Ｌｉｚａｒｄ** |
| 司令部 | headquarters | 12 columns — only fits alone on a line |
| 守備兵 | garrison / garrison men | seed had "garrison soldier"; 8+8 columns rarely fits, so bare **garrison** is the default and **garrison men** the plural-personal form |
| 機械兵 | machine soldier | |
| 援軍 | reinforcements / **aid** | use "aid" only where 24 columns will not take the full word; flag each time |
| 要塞 | fortress | 8 columns |
| 旗印 | banner | |
| ウエストバリー | Ｗｅｓｔｂｕｒｙ | Town taken by the 9th Army. 9 columns. Alt *Westbarry* |
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
| ああ (assent) | Ｙｅａｈ | Casual agreement from a rough speaker. **Distinct** from はっ → Ｓｉｒ (military assent) and from 分かった → `Ｒｉｇｈｔ，`. ✅ **`tl/battle/chunk_000.txt` line 4 is now fixed** (2026-09-08): it rendered `ああ。` as `Ｙｅｓ．`. 4 → 5 columns, +2 bytes, standalone row so nothing re-flows. **No `Ｙｅｓ` for ああ remains in `tl/`.** See §18.3 |
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
| キエーザ | `Ｋｉｅｓａ` | script 1090, 1092 — `キエーザ城`, a castle | Ｃｈｉｅｓａ — which is Italian for *church*, so the name may be deliberate; check whether the castle is a religious site before fixing |
| ~~ルクレール~~ | ✅ **PROMOTED to §28.1** — `Ｌｅｃｌｅｒｃ`, used exactly as seeded, rendered in `tl/battle/chunk_013.txt` (PR #10). ⚠️ **This row's description was wrong: it is a KINGDOM, not "a castle"** — corrected at §28.1 with the dump evidence | script 1090, 1096 — `ルクレール城`, ~~a castle~~ | Ｌｕｃｌｅｒｅ. The French reading matches the European naming |
| ~~ＺＯＣ（支配地域）~~ | ✅ **PROMOTED to §26.3** — used exactly as seeded (PR #8) | script 984 | — |
| ~~中立ユニット~~ | ✅ **PROMOTED to §26.3** (PR #8) | script 988 | — |
| ~~前衛 / 後衛~~ | ✅ **PROMOTED to §26.3** — front line / rear line, with one width variant `ｉｎ　ｆｒｏｎｔ` / `ｂｅｈｉｎｄ` flagged (PR #8) | script 985 | — |
| ~~『説得』 / 『ＧＵＥＳＴ　ＵＮＩＴ』 / 「ＥＮＴＥＲ」~~ | ✅ **PROMOTED to §26.3** — used exactly as seeded (PR #8), the last two reproduced not re-cased. ⚠️ **`FLAGS.md` §I1 is now SETTLED** by that review, and these three are the rows that settled it | script 986–988 | — |
| ~~司教~~ | ✅ **PROMOTED to §26.1** — Bishop, spelled out like Commander / Captain / Doctor (PR #8) | script 1047 | — |
| ~~報奨金~~ | ✅ **PROMOTED to §24.2** — `ｒｅｗａｒｄ`, rendered in battle chunk 6 (PR #7) before script 991 reached a batch | script 991, battle chunk 6 | — |
| ~~同盟~~ | ✅ **PROMOTED to §26.3** — alliance (PR #8) | script 999–1001 | — |
| ホアグ王子 | Prince `Ｈｏａｇ` | **New seed, 2026-09-08 (PR #8 review)** — surfaced while verifying `アップミーズ`, and **not batch 005's business**: that batch does not render it. Carline's first prince, Cavia's elder brother (`私の兄でもあるホアグ王子`), the man who built Apumizu (`ホアグ王子がつくった街`), and a target of Helfer's (`奴らにはホアグとともに舞台から下りてもらう`). **6 battle + 16 script occurrences.** 10 columns with the title, 4 bare | Ｈｏａｇｕ, Ｈｏｇ. Promote in the wave that first renders it |
| トリフ | `Ｔｏｒｉｆ` | **New seed, 2026-09-08 (PR #8 review)**, same sweep. Hoag's younger brother (`弟のトリフ`), whom Helfer prefers as the more pliable heir. **9 battle + 6 script occurrences.** 5 columns | Ｔｒｉｆ, Ｔｏｌｉｆ. Promote in the wave that first renders it |
| ~~シェルビー~~ | ✅ **PROMOTED to §29.1** — `Ｓｈｅｌｂｙ`, a PLACE, rendered four times in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~カーゴ~~ | ✅ **PROMOTED to §29.1** — `Ｃａｒｇｏ`, the proper name of a machine, rendered twice in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded; the `ｔｈｅ　ｃａｒｇｏ` trap was avoided** | battle chunk 8 | — |
| ~~プロキオン~~ | ✅ **PROMOTED to §29.1** — `Ｐｒｏｃｙｏｎ`, rendered in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~ルート~~ | ✅ **PROMOTED to §29.1 (chunk 8) and STRUCK HERE at chunk 17's merge (PR #12).** `ｒｏｕｔｅ`, lowercase, rendered twice in **each** of the two units, exactly as seeded. **The cross-unit rule is discharged**: chunk 8 merged first and deliberately left this row live, chunk 17 merged second and strikes it, which is the whole of what that rule prescribes. See §30.1 | ~~**Wave-3 seed — CROSS-UNIT (chunks 8 and 17), lowercase common noun** per the バジリスク → basilisk precedent (§17.1 species test): `敵は別のルートから来たようです` (chunk 17 L3) and `ここへ抜けるルートは、バージェス峡谷か南の砂漠` (chunk 17 L4). **4 battle (ch8 L9 ×2, ch17 L3, L4) + 8 script.** 5 columns | Not `Ｒｏｕｔｅ`; not `ｐａｔｈ` where the source says ルート | ⚠️ **RENDERED by chunk 8 (PR #11, merged) as `ｒｏｕｔｅ`, twice, exactly as seeded — this row is DELIBERATELY LEFT LIVE.** Chunk 17 (PR #12) renders it too and merges second; per the wave's cross-unit rule it is struck once, by that reviewer. See §29.1
| ~~スパイ~~ | ✅ **PROMOTED to §29.1** — `ｓｐｙ`, lowercase, rendered twice in `tl/battle/chunk_008.txt` (PR #11). **Used exactly as seeded** | battle chunk 8 | — |
| ~~アーバイン様~~ | ✅ **PROMOTED to §28.1** — `Ｌｏｒｄ　Ｉｒｖｉｎｅ`, rendered in `tl/battle/chunk_013.txt` (PR #10). ⚠️ **This row's widths were both one too many** — `Ｉｒｖｉｎｅ` is **6** columns and `Ｌｏｒｄ　Ｉｒｖｉｎｅ` is **11**, not 7 and 12. The seed was mine and it was wrong; the translator caught it and I remeasured on the shipped row (`Ｌｏｒｄ　Ｉｒｖｉｎｅ！` = 12 with the mark). The rendering is unchanged | **Wave-3 seed** — an enemy commander (chunk 13 L2, `アーバイン様！敵襲です！！`), addressed 様 by a subordinate; masculine, authoritative register (`まあよい`, `叩き潰してやれ！！`). 様 → Lord on the `リムル` / `フィリス様` precedent (§14.1), **not** §21.2's さん rule. **1 battle + 0 script.** ~~7 columns bare, 12 with the title~~ | Ｕｒｂａｉｎ, Ｅｒｂｉｎｅ |
| ~~バージェス~~ | ✅ **PROMOTED to §30.1** — `Ｂｕｒｇｅｓｓ` / `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ`, rendered in `pending/chunk_017.txt` (PR #12), used exactly as seeded. ⚠️ **This row's widths are both one too many** — `Ｂｕｒｇｅｓｓ` is **7** columns and `Ｂｕｒｇｅｓｓ　Ｃａｎｙｏｎ` is **14**, not 8 and 15; remeasured at review. Rendering unchanged | ~~**Wave-3 seed** — a **PLACE**, on the §2 test: `バージェス峡谷か南の砂漠` (a route out, chunk 17 L4) and `バージェスからの定期連絡` (regular reports *from* it, chunk 17 L5). Capitalised as a place name on the `バジリスクの砂漠` → *the Basilisk Desert* precedent (§2). **2 battle (chunk 17) + 5 script.** 8 columns bare, 15 with Ｃａｎｙｏｎ | `Ｂｕｒｇｅｓｓ　Ｇｏｒｇｅ` also 15 — 峡谷 is literally a gorge; either fits. Rendered by chunk 17 — promote on merge |
| ~~イフリート~~ | ✅ **PROMOTED to §30.1** — `Ｉｆｒｉｔ`, capitalised, rendered in `pending/chunk_017.txt` (PR #12), **used exactly as seeded**; 5 columns confirmed. ⚠️ **The chunk-15 gloss warning stays live for whoever takes chunk 15** | ~~**Wave-3 seed. A named FORTRESS GUN, not a monster and not a person** — so the §17.1 species test does **not** apply and it stays capitalised. ⚠️ **The gloss is in chunk 15, not in chunk 17**: chunk 15 L1 has `この巨大砲台イフリートの前には、カーライン軍など風の前の塵に同じ！！` (*this giant gun emplacement Ifrit*) and `紅蓮の炎で焼き尽くしてくれるわっ！` (the fire association the name carries). **Chunk 17 L5 renders only `・・・イフリートが落とされたか。`** — without this row its translator cannot tell what Ifrit is. **2 battle (ch15 L1, ch17 L5) + 3 script.** 5 columns | Ｅｆｒｅｅｔ, Ｉｆｒｅｅｔ. Rendered by chunk 17 — promote on merge |
| ~~マムー~~ | ✅ **PROMOTED to §30.1** — `Ｍａｍｕ`, **with no `Ｌｏｒｄ`**, rendered in `pending/chunk_017.txt` (PR #12); 4 columns confirmed. The self-reference warning was heeded exactly, and the `マムー兄さん` note stays live for chunk 41 | ~~**Wave-3 seed** — a **PERSON**, male. ⚠️ **`このマムー様が` (chunk 17 L7) is boastful SELF-reference, not an honorific from a subordinate** — the `このクリミアに` pattern (§25.1) — so it takes **no** `Ｌｏｒｄ`; put the swagger in the verb (`ぜ`, §7), not in a title. `マムー兄さん` → `Ｂｒｏｔｈｅｒ　Ｍａｍｕ` is **chunk 41's** line, not chunk 17's. **2 battle (ch17 L7, ch41 L5) + 0 script.** 4 columns | Ｍａｍｍｏｏ, Ｍａｍｕｕ. Rendered by chunk 17 — promote on merge |
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

⚠️ **STATUS 2026-09-09 — chunk 20 (PR #14) merged FIRST, so all four rows below are DELIBERATELY
LEFT LIVE.** Verified at that review, in the file: `アリエス` → `Ａｒｉｅｓ` ×3, `盗賊カバラ` →
`ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` ×1, `ヒューゴー` → `Ｈｕｇｏ` ×1, `火の水晶` →
`Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` ×1 (**the long form**) — **all four used exactly as seeded, none improved
on unilaterally.** Chunk 19 (PR #16) was still open and in rework when this merged; **it merges
second and strikes these four rows.** ⚠️ **A FIFTH term belongs on this list and the seed missed
it: `宝石`** (c19 ×1, c20 ×4, c31 ×1), with `宝` / `お宝` beside it — ruled `ｇｅｍｓｔｏｎｅ` by chunk
19's reviewer and shipped consistently by chunk 20; see §32.1. ⚠️ **If chunk 19 (tier B, 1.94)
cannot fit `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` (15) and takes `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` (12), chunk 20 must follow
it** — that row is standalone with 3,927 bytes of slack behind it, so the change is −6 bytes and
re-flows nothing.

| Japanese | Proposed English | Where seen | Alternatives if the reading is open |
|---|---|---|---|
| アリエス | `Ａｒｉｅｓ` | **CROSS-UNIT — chunk 19 L1, chunk 20 L47/L48 (×3).** A **PERSON**, female, and a travelling performer: asked `アリエスさんは、ファリーナは初めて？` she answers `いいえ。旅の巡業で何度か来たことが。` (*no — I have come a few times, touring*). Polite です/ます register. **11 battle + 9 script occurrences — the most-used new name in this wave.** 5 columns | Ａｒｉｅｓｕ, Ａｌｉｅｓ. The zodiac reading is the plain one and matches the European convention |
| ソロン | `Ｓｏｌｏｎ` | chunk 19 L24 (×3). A **PERSON**, male — an imperial soldier recognised by his elder brother: `ソロン！？ソロンじゃねぇか！！` … `実の兄貴の頼みだ。手を貸そう。` **3 battle + 0 script.** 5 columns | Ｓｏｒｏｎ, Ｔｈｏｒｏｎ |
| ヒューゴー | `Ｈｕｇｏ` | **CROSS-UNIT — chunk 19 ×1, chunk 20 L1 ×1.** A **PERSON**, male, named dismissively by a rival imperial officer: `ふふっ、ヒューゴーの奴、今ごろ　ファリーナを探索しておるんだろうが、見当違いもいいところだ。` **2 battle + 0 script.** 4 columns | Ｈｕｇｈｏ, Ｈｕｇｏｒ. The long ー is the ordinary Japanese spelling of *Hugo*, not a separate syllable |
| ノーマン | `Ｎｏｒｍａｎ` | chunk 19 ×1 (`ほう。ノーマン、よければ、話して差し…`). A **PERSON**, male, of Farina; the main script has him leading the rebuilding afterwards (`今は、ノーマンさんたちがふっこーにはげん…`). **1 battle + 3 script.** 6 columns | Ｎｏｒｍａｎｎ |
| カバラ | `Ｋａｂａｌａ` | **CROSS-UNIT — chunk 19 ×4, chunk 20 L47 ×1.** A **PERSON**, male, a **dead bandit** whose hoard is this chapter's object: `カバラという盗賊の手に渡ったと聞きます`, `そのカバラも帝国に追われて、もうこの世に…`, `このカバラの財宝を捜しているトレジャーハンター`, `これも、盗賊カバラのお宝のひとつか。` `盗賊カバラ` → `ｔｈｅ　ｂａｎｄｉｔ　Ｋａｂａｌａ` (17 columns). **5 battle + 0 script.** 6 columns bare | Ｃａｂａｌａ, Ｋａｂｂａｌａ. ⚠️ カバラ is also the standard Japanese for *Kabbalah*; the `ネルガリ` → `Ｎｅｒｇａｌｉ` precedent (§17.4) chose the plain transliteration over the mythological source, and this row follows it |
| 火の水晶 / 『火の水晶』 | `Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ` / `“Ｃｒｙｓｔａｌ　ｏｆ　Ｆｉｒｅ”` | **CROSS-UNIT — chunk 19 ×4, chunk 20 L47 ×1.** The chapter's plot object, and **an inventory item whose description line is a 21-instance row of the untranslated description table**: `ファリーナに伝わる伝説の水晶。炎のような美しい光を放つ。` (*a legendary crystal handed down in Farina; it gives off a beautiful light like flame*). Chunk 19 carries one instance in `『』` and the rest bare. `『…』` → `“…”` per `『知識の書』` (§12). **5 battle + 22 script.** 15 columns bare, **17 quoted** | `Ｆｉｒｅ　Ｃｒｙｓｔａｌ` (12 bare / 14 quoted) if width bites — but chunk 20 is tier D (ratio 4.75) and chunk 19 tier B (1.94), so ⚠️ **chunk 19 is the one that may need the short form; if it takes it, chunk 20 must take it too.** The `Ｘ　ｏｆ　Ｙ` form matches the `Ｂｏｏｋ　ｏｆ　Ｋｎｏｗｌｅｄｇｅ` precedent for `〜の〜` |
| ~~バーストウーズ~~ | ✅ **PROMOTED to §32.1** — `ｂｕｒｓｔ　ｏｏｚｅ`, lowercase, rendered in `tl/battle/chunk_020.txt` (PR #14), **used exactly as seeded**; 10 columns confirmed at review. ⚠️ **This row's citation was wrong: the `グレイウーズ` → `ｇｒｅｙ　ｏｏｚｅ` precedent is at §17.2, not §17.4.** The derivation is unaffected | battle chunk 20 | — |
| トレジャーハンター | `ｔｒｅａｓｕｒｅ　ｈｕｎｔｅｒ` | chunk 19 ×1 — the people hunting Kabala's hoard in Marvellous. **Lowercase**: a trade, by the §17.1 species test and the `探検家` → `ｅｘｐｌｏｒｅｒ` precedent (§21.1). ⚠️ **In the dump it is SPLIT across a line break** — `トレジャー|ハンター` — so a naive grep for the whole word finds zero. **1 battle + 0 script.** 15 columns | — |
| 傭兵団 | `ｍｅｒｃｅｎａｒｙ　ｂａｎｄ` | chunk 19 L3 ×2 — `どうやら、傭兵団のようだな。` **2 battle + 0 script.** 14 columns | `ｍｅｒｃｅｎａｒｙ　ｃｏｍｐａｎｙ` (17), `ｍｅｒｃｅｎａｒｉｅｓ` (12) where the 団 is not doing work |
| ~~おかしら (vs 将校 / 将軍)~~ | ✅ **PROMOTED to §32.1** — `Ｂｏｓｓ` (4) and `将校` → `ｏｆｆｉｃｅｒ` (7), rendered in `tl/battle/chunk_020.txt` (PR #14), **the seed's primary form taken over its `Ｃｈｉｅｆ` alternative**. ⚠️ **The gag SURVIVED and was read against the source at review** — `Ｙｏｕ　ｆｏｏｌ，` / `Ｉ　ａｍ　ａｎ　ｏｆｆｉｃｅｒ　ｏｆ　ｔｈｅ` / `Ｅｍｐｉｒｅ！　Ｃａｌｌ　ｍｅ` / `Ｇｅｎｅｒａｌ！　Ｇｅｎｅｒａｌ！！`, three words still three words, the doubled repeat kept. See §32.4a | battle chunk 20 | — |
| ~~勲章~~ | ✅ **PROMOTED to §32.1** — `ｍｅｄａｌ`, rendered ×2 in `tl/battle/chunk_020.txt` (PR #14); 5 columns confirmed. ⚠️ **This row's reach was badly wrong and its silence on `メダル` cost a review: it is 4 battle (chunks 20 and 22) + 59 `script_dump` / 39 `script_unique`, not "2 battle", and it is the plot item `獅子の勲章` / `『獅子の勲章』`.** The clash with §3's racetrack `メダル` → `ｍｅｄａｌ` is **LIVE in banks 42 and 43** and is NOT discharged — see §32.5 | ~~chunk 20 L47/L48 ×2 — dug up beside the jewels~~ | `ｄｅｃｏｒａｔｉｏｎ` (12) rejected as too vague; `ｔｏｋｅｎ` (5) is the reserve, on the **racetrack** side |
| デビルズラック | `“Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ”` | **script batch 002, unique 631** — an item pressed on the player by a grateful NPC (`これを　もらってくれ！デビルズラックだ！！`). A coined item name, so capitalised. ⚠️ **`’` not `'`** (§3.1). **0 battle + 1 script.** 14 columns quoted, 12 bare | `Ｄｅｖｉｌｓ　Ｌｕｃｋ` (11) if the apostrophe proves awkward at width; the source has no `『』`, so the quotes are optional — **prefer bare `Ｄｅｖｉｌ’ｓ　Ｌｕｃｋ`** unless the line reads as a title |
| オイラ | first person, **rustic register — not a word to translate** | **script batch 002, unique 632 ×4** — a cheerful odd-job lad: `オイラは、見てのとおりハッピーさ！オイラ、ここで下働きしてるのさ！` Carry it as §7 register (dropped subjects, `ｓａ`-ish breeziness, contractions), **not** as a rendered pronoun or an accent spelling. Compare §21.2's さん rule: politeness with no English lexical equivalent goes into word choice | Do **not** write dialect spelling (`Ｏｉ’ｍ`, `Ａｈ`); §2 forbids inventing |
| ハッピー | `ｈａｐｐｙ` | **script batch 002, unique 632 ×2** — `その後どうだい？ハッピーかい？` … `見てのとおりハッピーさ！` The speaker is using the **English loanword** as slang, and the joke is that he keeps saying it. Render it *happy* both times so the repetition survives. **0 battle + 4 script.** 5 columns | — |
| 親方 | `ｔｈｅ　ｂｏｓｓ` | **script batch 002, unique 632 ×2** — the lad's master, from whom the gift must be kept secret (`だけど、親方には内緒だ`). **7 columns.** ⚠️ Distinct from `おかしら` → `Ｂｏｓｓ` above (battle chunk 20): different speakers, different scenes, no shared line, so §3 is not engaged — but do not let them drift into one capitalised form | `ｔｈｅ　ｍａｓｔｅｒ` (10), `ｔｈｅ　ｇｕｖ’ｎｏｒ` — the last is too British for this register |

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
8. **Numerals in prose.** Ch.12 spells out `３時間` / `３時の鐘` as "Three hours" / "three o'clock"
   rather than keeping the full-width `３`. Both are legal charset; the digits-stay-full-width note
   in §4 covers the `ＣｌａｓｓＮＮ` placeholder slots only. Confirm the house preference before a
   chunk with many numbers.
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
| `おや` | 6 | 23 | 29 | `Ｏｈ？` |

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
| あら、 | **`Ｍｙ，`** | 3 columns. A woman's mild, arch surprise. **Ratified at review, deliberately, because it binds 16 further occurrences (5 battle + 11 script-unique — both figures confirmed).** Deliberately **not** in the `Ｏｈ` family: §24.4 collapsed おお、/ ほう、 onto `Ｏｈ，` and おや onto `Ｏｈ？` outright, so `Ｏｈ` is spent and a fourth string cannot join them. `Ｍｙ` occurs **0** times elsewhere in `tl/`. The alternative `Ｏｈ　ｍｙ，` is also free but is 6 columns to `Ｍｙ，`'s 3, and あら is the milder of the pair |
| 馬鹿者！ (direct address) | `Ｙｏｕ　ｆｏｏｌ！` | **A fifth バカ register**, held apart from §19.1's そんなバカな → `Ｔｈａｔ’ｓ　ｉｍｐｏｓｓｉｂｌｅ` and バカなやつら → `ｗｈａｔ　ｆｏｏｌｓ　ｙｏｕ　ａｒｅ`, §20.3's **バカ者** → `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ` (katakana, and *of* a third party) and §26.4's proverb. Same English root as §20.3 — this one is the vocative, and the kanji spelling is a different source string |
| ははっ！ | `Ｙｅｓ，　ｓｉｒ！` | 9 columns. The doubled, more emphatic military assent. **Distinct** from §6's はっ → `Ｓｉｒ`, which this chunk uses byte-identically **two segments earlier in the same message** — they genuinely stand side by side, so they must not collapse. 5 battle + 1 script-unique **as a tic**, under §5's word-plus-source-punctuation mechanism (`ははっ・・・・！！` ch 16, `ははっ！！` ch 37, `はははっっ！！` ch 38, `ははっ・・・・` ch 42); the exact string `ははっ！` is 2 battle |
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
| マムー | `Ｍａｍｕ` | **Promoted from §9, used exactly as seeded.** 4 columns, **no `Ｌｏｒｄ`**. `あんたの妹の仇は、このマムー様がとってやるぜ。` → `Ｉ，　Ｍａｍｕ，　ｗｉｌｌ　ａｖｅｎｇｅ{FFFE}ｙｏｕｒ　ｓｉｓｔｅｒ{FFFE}ｆｏｒ　ｙｏｕ．` — the **appositive** carries the `この…様が` self-aggrandisement, which is §25.1's `このクリミアに` pattern applied exactly. **2 battle (this chunk, ch41) + 0 script**; `マムー兄さん` → `Ｂｒｏｔｈｅｒ　Ｍａｍｕ` is still chunk 41's to render |
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
| 〜め (contempt, on a personal name) | `Ｔｈａｔ　〜` | `ギルフォードめ。` → `Ｔｈａｔ　Ｇｕｉｌｆｏｒｄ．` (14 columns) and `ギルフォードめ・・・` → `Ｔｈａｔ　Ｇｕｉｌｆｏｒｄ．．．` — §5's mechanism, the word fixed and the stops from the source. Takes the contempt into the demonstrative exactly as §20.3's バカ者 → `Ｔｈａｔ　ｆｏｏｌ　Ａｎｓｅｌｍｏ` already does. ⚠️ Distinct from `chunk_006`'s `フェルナンドめが`, which **drops** め and carries the contempt elsewhere in a longer sentence — a different message, so §3 is not engaged. Recurs as `この裏切り者め。` in chunk 21 |

### 31.3 Interjections and set phrases

| Japanese | English | Note |
|---|---|---|
| さて、 | `Ｎｏｗ　ｔｈｅｎ，` | ⚠️ **9 columns, not the PR's 10.** ⚠️ **Not a new rendering — recording one already shipped, and verified at review**: `tl/battle/chunk_033.txt` msg 6 ships `さて、果たして、` → `Ｎｏｗ　ｔｈｅｎ，` and had no glossary row. Held **distinct** from §28.8's さあ、 → `Ｎｏｗ，`, and that distinction is **proven, not theoretical**: `chunk_033` contains both source strings and ships them apart. ⚠️ **`Ｎｏｗ　ｔｈｅｎ` already serves two further source strings the PR did not name** — `それじゃ、` (`chunk_003` msg 4) and `おっと。` (`chunk_007` msg 11, as `Ｎｏｗ　ｔｈｅｎ．`). §25.3's test run at review: `さて、` is in chunks 18, 26, 33; `それじゃ` in 3, 7, 15, 32, 43; `おっと` in 7, 25, 43 — **no chunk holds `さて、` with either**. **3 battle + 5 script.** Recurs in chunk 26 |
| かかってくるがいい。 | `Ｙｏｕ　ｍａｙ　ｃｏｍｅ　ａｔ　ｍｅ．` | 19 columns. Deliberately **not** `Ｃｏｍｅ　ａｔ　ｍｅ．`, which `chunk_033` msg 20 already ships for the polite imperative `かかってきなさい。` The 〜がいい is condescending permission, not an imperative, so *You may* keeps them apart **and leaves the plain imperative かかってこい。 (chunks 16 ×2, 30) free to take chunk 33's shipped form.** ⚠️ **Binds chunk 23 L15**, which carries this string byte-identically — verified at review in `battle_dump.txt`, in the line `まさか、お前たち９軍と剣を交えることになろうとはな。かかってくるがいい。骨は拾ってやる。` **2 battle + 0 script** |
| ネズミども (bare vocative) | `ｙｏｕ　ｒａｔｓ` | 8 columns. §30.1 fixes ネズミども → `ｒａｔｓ` from `pending/chunk_017`'s attributive `カーラインのネズミども` → `ｔｈｅ　Ｃａｒｌｉｎｅ　ｒａｔｓ`; this is the bare vocative, so the ども plural-contempt takes `ｙｏｕ`. **Word unchanged.** §30.1 predicted five more uses — this is the first. `ネズミども` is **6 battle occurrences in chunks 17, 18, 41 and 42** |
| まさか、 | `Ｓｕｒｅｌｙ` | 6 columns. ⚠️ **Fixed here 2026-09-08 (PR #13 review) — it had never been in this glossary despite being shipped.** `pending/chunk_017.txt` msg 4 renders `まさか、奴らは` → `Ｓｕｒｅｌｙ　ｔｈｅｙ　ｄｉｄ　ｎｏｔ`, and this chunk renders `まさか、裏切る気か？` → `Ｓｕｒｅｌｙ　ｈｅ　ｄｏｅｓ　ｎｏｔ` / `ｍｅａｎ　ｔｏ　ｂｅｔｒａｙ　ｍｅ？`. This is §24.3's `よし、` shape — a form shipped repeatedly that the glossary never fixed. **18 battle occurrences across 13 chunks (0, 17, 18, 19, 23, 24, 25, 26, 27, 30, 32, 39, 43) + 10 script**, so it is the largest single drift risk this unit leaves behind. `Ｓｕｒｅｌｙ` is otherwise free across `tl/` |
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
| 宝石 | `ｇｅｍｓｔｏｎｅ` / `ｇｅｍｓｔｏｎｅｓ` | 9 / 10 columns. **A fifth cross-unit term the wave-4 seed missed** — see the §9 note. Ruled `ｇｅｍｓｔｏｎｅ` by chunk 19's reviewer; this unit's plural is consistent. Deliberately **not** `ｊｅｗｅｌｓ`: §3 fixes ジュエル → `Ｊｅｗｅｌ` (the currency, "do not translate as gem") and ジェム → `Ｇｅｍ` (the pickup). Verified at review: `ｇｅｍｓｔｏｎｅ` is **free** across `tl/` and `pending/`; `ｇｅｍ` occurs once (`batch_003`, §4's lowercase *a gem in its brow*) and `Ｇｅｍ` is the capitalised pickup — no collision either way. **6 battle (19 ×1, 20 ×4, 31 ×1) + 5 script-unique** |
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

**Lines this affects (§4.3) — four rows in three shipped files, all width-neutral or shorter:**

| File | Row | Now | Must become | Cost |
|---|---|---|---|---|
| `tl/battle/chunk_007.txt` L19 | `あら・・・・？` | `Ｏｈ．．．．？` (7) | `Ｍｙ．．．．？` (7) | 0 bytes |
| `tl/battle/chunk_007.txt` L24 | `あら、雪・・・？` | `Ｏｈ，　ｓｎｏｗ．．．？` (12) | `Ｍｙ，　ｓｎｏｗ．．．？` (12) | 0 bytes |
| `tl/battle/chunk_011.txt` L3 | `あら、お客様？` | `Ｏｈ　ｍｙ，　ｖｉｓｉｔｏｒｓ？` (16) | `Ｍｙ，　ｖｉｓｉｔｏｒｓ？` (13) | −6 bytes |
| `tl/battle/chunk_014.txt` L3 | `あら？` | `Ｏｈ？` (3) | `Ｍｙ？` (3) | 0 bytes |

⚠️ **Deliberately NOT applied in this commit, and the reason is on the record rather than implied.**
PR #15 (script batch 006) is open and unreviewed and reaches this same question from the script side
with ~30 more instances; chunk 19 is mid-rework. Re-cutting three shipped files inside a
battle-chunk merge while two siblings are in flight is the wrong blast radius. This is the §27
corrections-unit shape: the **ruling** binds PR #15, chunk 19 and every later unit from now; the
**re-cut** is owed work, carried in `FLAGS.md` §T and `HANDOFF.md` with the lines and costs above.

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
