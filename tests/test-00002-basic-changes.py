#!/usr/bin/python
# -*- encoding: utf-8 -*-
# check basic metadata; branding, legal, etc.

import fontforge
import os
import re
import sys

if len(sys.argv) != 2:
    print("Usage: %s <sfd>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
basename = os.path.basename(filename)

# derive names based on filename

def put_space(match):
    aA = match.group(0)
    return aA[0] + ' ' + aA[1:]

if basename.endswith('-Bold.sfd'):
    style = 'bold'
    fontname = basename[:-len('-Bold.sfd')] + 'Bold'
    familyname = basename[:-len('-Bold.sfd')]
else:
    style = 'regular'
    fontname = basename[:-len('.sfd')]
    familyname = basename[:-len('.sfd')]

familyname = re.sub(r'[a-z][A-Z]', put_space, familyname)
fullname = re.sub(r'[a-z][A-Z]', put_space, fontname)

#print 'expected fontname: %s' % fontname
#print 'expected familyname: %s' % familyname
#print 'expected fullname: %s' % fullname

font = fontforge.open(filename)

def verify_copyright_appended(copy_str):
    lines = [l for l in copy_str.split('\n')
             if l.startswith('Copyright (c)') or l.startswith('Copyright ©')]
    return len(lines) > 1

### check PostScript names

assert(font.fontname == fontname)
assert(font.familyname == familyname)
assert(font.fullname == fullname)

if style == 'bold':
    assert(font.weight == 'Demi' or font.weight == 'Bold')
else:
    # regular
    assert(font.weight == 'Book')

# check whether the copyright notice has been appended (not replaced)
assert(verify_copyright_appended(font.copyright))

### check OS2 names

assert(font.os2_vendor == 'JEBD')

### check TTF names

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'Copyright'][0][2]
assert(verify_copyright_appended(val))

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'Family'][0][2]
assert(val == familyname)

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'Fullname'][0][2]
assert(val == fullname)

# check if OFL has been inserted to 'License' and the OFL URL to 'License URL'
val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'License'][0][2]
assert(verify_copyright_appended(val))
assert('SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007' in val)
assert(('with Reserved Font Name ' + familyname) in val)

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'License URL'][0][2]
assert(val == 'http://scripts.sil.org/OFL')

try:
    val = [t for t in font.sfnt_names
           if t[0] == 'English (US)' and t[1] == 'Preferred Family'][0][2]
    assert(val == familyname)
except IndexError:
    pass

# Jebudo branding

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'Vendor URL'][0][2]
assert(val == 'https://github.com/changwoo/jebudo')

val = [t for t in font.sfnt_names
       if t[0] == 'English (US)' and t[1] == 'Manufacturer'][0][2]
assert(val == 'Jebudo project')

