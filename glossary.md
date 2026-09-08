# Riot Stars — Translation Glossary

Paste this into every translation session, directly under `translation_prompt.md`.

**Every entry here is fixed.** Use the English form exactly as written, everywhere, forever. To
change one, follow §4.3 of the prompt: state the correction explicitly and list every previously
translated line that must be revisited.

Entries in **§9 PROVISIONAL** are *not* decisions — they are names seen in the dumps but not yet
rendered in any translated line. Promote one to its proper table the first time you use it.

Status: covers `script_unique.txt` lines 1–216 (unit, class, monster and equipment descriptions) and `battle_dump.txt`
chunks **0, 1, 2, 3, 4, 7, 10, 11, 12, 14, 33, 34, 35, 40** (prologue + chapters 2–5 + all of tier E).

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
| リオン | **unresolved — Lion or Leon** | pick on first use and record here |
| 王女様 | the Princess | |
| 神父 | priest | the fairy's ring-bearer |
| 妖精 | fairy | lowercase, common noun; referred to as *she* |
| 市長 | the mayor | Caucasus (ch.12); also `script_unique` 380 |
| クレス | Ｃｒｅｓｓ | 少尉 → **Ｓｅｃｏｎｄ　Ｌｉｅｕｔｅｎａｎｔ　Ｃｒｅｓｓ** (18+5 columns, never on one row). Court‐martialled alongside Alfred for the failed expedition (script 1236). Alt *Kress*, *Cres* |
| アンゼルモ | Ａｎｓｅｌｍｏ | 中尉 → **Ｆｉｒｓｔ　Ｌｉｅｕｔｅｎａｎｔ　Ａｎｓｅｌｍｏ**. **Promoted from §14.6**, which already used this form for his register but never fixed the name. 8 columns |
| ゼファー・クリッペン | Ｚｅｐｈｙｒ　Ｋｒｉｐｐｅｎ | 帝国の司令官 → Commander of the Empire. `・` has no glyph in §3.1 and becomes `　`. 14 columns. Alt *Zepher*, *Crippen*, *Klippen* |
| ヘルファー様 | Ｌｏｒｄ　Ｈｅｌｆｅｒ | 様 → **Lord** for a male superior, paralleling 様 → Lady (Rimul §1, Phyllis §14.1). 11 columns. Does not change the §11.1 bare-name entry |

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
| クリミア | Crimea | region |
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

| Japanese | Likely English | Where seen |
|---|---|---|
| ~~メルザリオ~~ | ✅ **PROMOTED to §20.1** — `Ｍｅｌｚａｒｉｏ`, and it is a **PLACE**, not the chief's son; this row's original description was wrong | battle chunk 2 (PR #3) |
| ~~ティミー~~ | ✅ **PROMOTED to §11.1** — `Ｔｉｍｍｙ`, rendered in ch.43 and again in `tl/battle/chunk_004.txt` (PR #6). This row was stale; struck 2026-09-08 | battle chunk 4, ch.43 |
| ~~サイクス~~ | ✅ **PROMOTED to §20.1** — `Ｓｙｋｅｓ` (§18.4) | battle chunk 2 (PR #3) |
| ~~宮廷第２軍~~ | ✅ **PROMOTED to §20.1** — `２ｎｄ　Ｒｏｙａｌ　Ａｒｍｙ`, both source spellings | battle chunk 2 (PR #3) |
| リザードマン | Lizardman | `script_unique` 1297; the ch.10 dragonfolk are presumably this class |
| レバーク | Leverk / Rebark | `script_unique` 1350, a castle Maya has left |
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
| **リオン** | **`Ｌｅｏｎ`** | battle chunk 6 — `匿名希望のリオンっておっさん`, a man who sent Ridge to help and wants to stay anonymous | **This settles §10.1**, which has been open since the glossary was written and says to decide before the character appears. He appears here. `Ｌｅｏｎ` over `Ｌｉｏｎ`: every other name in the game takes a European reading (Bauer, Carline, Helfer, Albert, Fernando, Anselmo), and `Ｌｉｏｎ` would read in English as the animal — the same failure §17.2 avoided for Ｎｅｒｇａｌｉ |
| カペラ | `Ｃａｐｅｌｌａ` | battle chunk 6 — `ファリーナの南、カペラの村`, a **village** | Ｋａｐｅｒａ. Capella is a star name and reads as European |
| カザロフ | `Ｋａｚａｒｏｖ` | battle chunk 6 — `カザロフ隊長`, an Imperial officer the Black Knights report to | Ｃａｓａｌｏｆ. The `‐ov` ending is the plainest reading |
| マーティン | `Ｍａｒｔｉｎ` | battle chunk 6 — a Black Knight, retreating with Percival | — |
| パーシバル | `Ｐｅｒｃｉｖａｌ` | battle chunk 6 — the other Black Knight | Ｐａｒｃｉｖａｌ; the Arthurian spelling is the obvious one |
| ディール帝国 | the `Ｄｉｅｌ` Empire | battle chunk 9 — `ディール帝国、万歳！！！`, **the Empire's actual name**, revealed for the first time | Ｄｉｅｈｌ, Ｄｉｒ, Ｔｈｉｅｌ. ⚠️ One voicing from 魔神ティール → `Ｔｙｒ` (§22.1) — keep them visibly distinct. Does **not** replace 帝国 → the Empire (§2); this is the proper name |
| ワーウィック | `Ｗａｒｗｉｃｋ` | battle chunk 9 — `ワーウィックまでは気が抜けないぜ`, a destination | — |
| 弓使い | `archer` | battle chunk 6 — `王国一の弓使い`, `カーラインきっての弓使い`, both of Ridge | A **third** bow word beside 弓兵 → archer and 弓の戦士 → bow warrior (§4). ⚠️ 使い → *tamer* (§14.3) does **not** apply — that rule is for 氷龍使い / 獣使い, creature handlers. Consider `bowman` to keep it distinct from 弓兵 |
| バトウ | `Ｂａｔｏｕ` | script 1041 — `神父のバトウ`, the priest of Bernard's church. Referred to posthumously as `バトウ様` in 1045 | Ｂａｔｏｗ, Ｂａｔｈｏｕ |
| リース文明 | the `Ｒｅｅｓｅ` civilisation | script 1047 — `伝説のリース文明`, a vanished people destroyed by war among their own kind | Ｒｉｅｓｅ, Ｌｉｅｓ. ⚠️ Probably the same vanished civilisation as 古代ハイランド → ancient Highland (§11.2) — check before fixing either |
| クレウス司教 | Bishop `Ｃｒｅｕｓ` | script 1047 | Ｋｒｅｕｓ. 司教 → **Bishop**, a new rank |
| キエーザ | `Ｋｉｅｓａ` | script 1090, 1092 — `キエーザ城`, a castle | Ｃｈｉｅｓａ — which is Italian for *church*, so the name may be deliberate; check whether the castle is a religious site before fixing |
| ルクレール | `Ｌｅｃｌｅｒｃ` | script 1090, 1096 — `ルクレール城`, a castle | Ｌｕｃｌｅｒｅ. The French reading matches the European naming |
| ＺＯＣ（支配地域） | `ＺＯＣ　（ｚｏｎｅ　ｏｆ　ｃｏｎｔｒｏｌ）` | script 984 | The gloss is **not** redundant here as `待ち時間（Ｗａｉｔ）` was (§3) — ZOC is opaque in English too |
| 中立ユニット | neutral unit | script 988 | |
| 前衛 / 後衛 | front line / rear line | script 985 | |
| 『説得』 / 『ＧＵＥＳＴ　ＵＮＩＴ』 / 「ＥＮＴＥＲ」 | `“Ｐｅｒｓｕａｄｅ”` / `“ＧＵＥＳＴ　ＵＮＩＴ”` / `“ＥＮＴＥＲ”` | script 986–988 | The last two are **already full-width Latin in the source** — reproduce them, do not re-case. ⚠️ These are the quoted-UI-token case `FLAGS.md` §I1 is open on; whatever settles §I1 settles `“Ｐｅｒｓｕａｄｅ”` |
| 司教 | Bishop | script 1047 | |
| 報奨金 | reward | script 991 | |
| 同盟 | alliance | script 999–1001 — `カーラインと帝国との同盟` | |

⚠️ **Two corrections the wave-2 units force, both of the メルザリオ kind (§20.1):**

1. ~~**`ファリーナ` is a PLACE, not only a person.**~~ ✅ **DISCHARGED 2026-09-08 (PR #6 review).**
   The row is moved from §1 (People) to §2 (Factions, places, ranks) with the dump evidence
   recorded there. It is a place **only** — no instance in either dump uses it as a personal
   name. `Ｆａｒｉｎａ` is unchanged, so nothing translated needs revisiting. **Moved once; PRs #7
   and #8 flagged it and must not move it again.**
2. **Fernando is `隊長` in the battle script but `将軍` in the main script** — script 992 reads
   `２軍のフェルナンド将軍`. `隊長` → captain is fixed (§2) and chunk 2 shipped
   `Ｃａｐｔａｉｎ　Ｆｅｒｎａｎｄｏ`. Either 将軍 → **General** and the man holds two titles, or one
   of them is loose usage. Decide before script 992 is rendered; do not silently pick.

---

## 10. Open questions

1. **リオン — Lion or Leon.** Unresolved. Decide before the character appears.
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
| フェリスランド | Ferisland | the land the island's lasers threaten. Alt *Felisland*, *Ferrisland*. Appears nowhere else in either dump — see FLAGS |
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
