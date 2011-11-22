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
if 'Nanum' in basename:
    print(basename + ': filename should be renamed as other than Nanum')
    sys.exit(1)

# JebudoXxxx(-Bold)?.sfd
if not re.match(r'^Jebudo([A-Z][a-z]*)+(-Bold)?\.sfd$', basename):
    print(basename + ': filename should be named as JebudoBlah(-Bold)?.sfd')
    sys.exit(1)
