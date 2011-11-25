#!/usr/bin/python
# -*- encoding: utf-8 -*-
# check if there are glyphs for Hangul jamos (U+1100)

import fontforge
import os
import re
import sys

if len(sys.argv) != 2:
    print("Usage: %s <sfd>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]

font = fontforge.open(filename)

test_jamos = u'\u1100\u115F\u1160\u1161\u11A8'

for jamo in test_jamos:
    glyph = font[ord(jamo)]
