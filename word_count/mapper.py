#!/usr/bin/env python

import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Emit key-value pairs to STDOUT (standard output)
    for word in words:
        # Output tab-delimited key-value pair
        print(f"{word}\t1}")
