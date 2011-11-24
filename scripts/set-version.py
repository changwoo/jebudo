#!/usr/bin/python

import sys
import fontforge

if len(sys.argv) < 3:
    print("Usage: %s <version> <files>..." % sys.argv[0])
    sys.exit(1)

version = sys.argv[1]
filenames = sys.argv[2:]

for filename in filenames:
    font = fontforge.open(filename)
    font.version = version
    for index,item in enumerate(font.sfnt_names):
        if item[0] == 'English (US)' and item[1] == 'Version':
            font.sfnt_names = font.sfnt_names[:index] + ((item[0], item[1], version),) + font.sfnt_names[index+1:]
            break
    font.save(filename)
    font.close()
