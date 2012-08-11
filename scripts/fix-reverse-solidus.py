#!/usr/bin/python
# -*- encoding: utf-8 -*-

# U+005C 백슬래시 문자에 원화 기호를 쓴 나눔 글꼴 수정. 나눔고딕은
# 0x10090, 나눔명조는 0x11248 위치에 백슬래시가 있음.

import os
import sys
import fontforge

print('blah...')

if len(sys.argv) < 2:
    print("Usage: %s <files>..." % sys.argv[0])
    sys.exit(1)

filenames = sys.argv[1:]

for filename in filenames:
    print('Fixing %s...' % filename)
    basename = os.path.basename(filename)
    if basename.startswith('JebudoSans'):
        glyphidx = 0x10090
    elif basename.startswith('JebudoSerif'):
        glyphidx = 0x11248
    else:
        print('Don not know how to fix %s' % filename)
        continue
    
    font = fontforge.open(filename)
    font.selection.select(glyphidx)
    font.copy()
    font.selection.select(0x005C)
    font.paste()
    font.save(filename)
    font.close()
