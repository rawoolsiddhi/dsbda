#!/usr/bin/env python

import sys

# input comes from standard input (stdin)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into fields
    fields = line.split()
    # extract username and login/logout time
    username = fields[0]
    action = fields[1]
    time = fields[2]
    # emit username and time with login/logout indicator
    print('%s\t%s\t%s' % (username, action, time))
