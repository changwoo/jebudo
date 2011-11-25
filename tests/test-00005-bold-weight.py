#!/usr/bin/python
# -*- encoding: utf-8 -*-

import fontforge
import os
import sys

if len(sys.argv) != 2:
    print("Usage: %s <sfd>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
basename = os.path.basename(filename)

if not 'Bold' in basename:
    sys.exit(0)

font = fontforge.open(filename)

assert(font.os2_panose[2] == 8)
assert(font.os2_weight == 700)


