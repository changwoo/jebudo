#!/usr/bin/python
# -*- encoding: utf-8 -*-
# copy U+3130 compatibility Hangul jamos to U+1100 Hangul jamos

import sys
import fontforge
import unicodedata

jamo_range = [unichr(c) for c in range(0x1100, 0x11FF + 1) +
              range(0xA960, 0xA97F + 1) + range(0xD780, 0xD7FF)]

# 호환자모를 NFKC 정규화하면 자모코드
jamo_to_comp = {}

for cjamo in [unichr(c) for c in range(0x3130, 0x318F + 1)]:
    jamo = unicodedata.normalize("NFKC", cjamo)
    if (jamo != cjamo):
        jamo_to_comp[jamo] = cjamo

name_to_jamo = {}

for jamo in jamo_range:
    try:
        name_to_jamo[unicodedata.name(jamo)] = jamo
    except ValueError:
        pass

# 종성에 대해서 초성에 대응하는 호환자모가 있으면 그걸 사용
for jamo in jamo_range:
    if jamo_to_comp.has_key(jamo):
        continue
    try:
        name = unicodedata.name(jamo)
    except ValueError:
        continue
    if not name.startswith('HANGUL JONGSEONG '):
        continue
    testname = 'HANGUL CHOSEONG ' + name[len('HANGUL JONGSEONG '):]
    try:
        jamo_to_comp[jamo] = jamo_to_comp[name_to_jamo[testname]]
    except KeyError:
        continue

# 채움
jamo_to_comp[u'\u115F'] = u'\u3164'
jamo_to_comp[u'\u1160'] = u'\u3164'

font = fontforge.open(sys.argv[1])

for jamo in sorted(jamo_to_comp.keys()):
    cjamo = jamo_to_comp[jamo]
    try:
        glyph = font[ord(jamo)]
        print "** WARNING: U+%04X already has a glyph, skipping" % ord(jamo)
    except TypeError:
        print "U+%04X: use glyph of U+%04X" % (ord(jamo), ord(cjamo))
        font.selection.select(ord(cjamo))
        font.copyReference()
        font.selection.select(ord(jamo))
        font.paste()

font.save()
