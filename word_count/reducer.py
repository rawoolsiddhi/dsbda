#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # Ignore/discard invalid count
        continue

    # This IF-switch only works because Hadoop sorts map output by key
    # Ensure the words coming to reducer are sorted
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to STDOUT
            print(f"{current_word}\t{current_count}")
        current_count = count
        current_word = word

# Output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
