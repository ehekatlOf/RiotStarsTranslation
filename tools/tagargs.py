"""Argument lengths for the control codes whose argument bytes can masquerade as text or as
another control code. Shared by riotbattle.py and riotscript.py — ONE table, both tools.

Both tokenisers test "is this byte a Shift-JIS lead?" before "is this a control code?", and
neither knew how many bytes a code's arguments occupy. So an argument byte in 0x81-0x9F/0xE0-0xEF
followed by a byte that completes a valid pair was emitted as a kanji (FLAGS.md §D1/§R4/§AP2),
and an argument byte in 0xFB-0xFF started a spurious control tag (§AY2). Consuming a code's
arguments unconditionally, as raw bytes, closes both holes at once.

The lengths below were MEASURED at byte level over every occurrence in both pristine dumps
(2026-09-11), not taken from the flag entries — two of which were wrong:

  FC70  2   37/37 occurrences: a u16 (item id) then a control code.
  FCA8  2   66/66: a u16 then a control code — NOT 8. The "8" in §R4/§AP2 is FCA8's two bytes
            plus a following six-byte FA 10/11 00 00 00 00 command that the tokeniser has never
            treated as a tag (it also follows FCA7, FCB2, FCB6, FB01). Two occurrences in chunk 28
            read FCA8 01 99 FC 20 …: forcing 8 would have hidden a real FC20 and the FFFF after
            it inside a data blob.
  FFED  2   5/5: a u16 amount (0x03E8 = 1000, 0x1388 = 5000, 0x00C8 = 200) then a control code
            — NOT 4. §AP2's "4" counted the first character of the following text (82 A8 = お)
            as an argument, which is why the shipped batch_012 row rendered a stray お.
  FFF3  4   129/129: 00 xx 00 yy; six occurrences have xx = FF (§AY2's {FF00}).

Codes not listed keep the old behaviour. Add a code only with a byte-level census like the
above; findings.md warns that argument lengths are NOT fixed per code in general.
"""

ARG_LEN = {
    0xFC70: 2,
    0xFCA8: 2,
    0xFFED: 2,
    0xFFF3: 4,
}
