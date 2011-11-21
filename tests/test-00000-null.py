#!/usr/bin/python
# just open and close the SFD

import sys
import fontforge

if len(sys.argv) != 2:
    print("Usage: %s <sfd>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]

font = fontforge.open(filename)
font.close()
