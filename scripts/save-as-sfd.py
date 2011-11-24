#!/usr/bin/python

import sys
import fontforge

if len(sys.argv) != 3:
    print("Usage: %s <input> <output>" % sys.argv[0])
    sys.exit(1)

infilename = sys.argv[1]
outfilename = sys.argv[2]

font = fontforge.open(infilename)
font.save(outfilename)
