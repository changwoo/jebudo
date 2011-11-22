#!/usr/bin/python
# check the filenames

import os
import re
import sys

if len(sys.argv) != 2:
    print("Usage: %s <sfd>" % sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
basename = os.path.basename(filename)

# no Nanum
assert(not 'Nanum' in basename)

# JebudoXxxx(-Bold)?.sfd
assert(re.match(r'^Jebudo([A-Z][a-z]*)+(-Bold)?\.sfd$', basename))
