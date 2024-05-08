#!/usr/bin/env python

import sys
from datetime import datetime

current_user = None
login_time = None
total_time = 0

# input comes from standard input (stdin)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    user, action, time_str = line.split('\t', 2)
    
    # convert time_str to datetime object
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

    # if current user is different, or logout is encountered
    if current_user != user or action == 'logout':
        if current_user:
            # calculate time difference and add to total_time
            total_time += (time - login_time).total_seconds()
            # output user and total_time
            print('%s\t%s' % (current_user, total_time))
        # reset variables for new user
        current_user = user
        login_time = time
        total_time = 0
    elif action == 'login':
        login_time = time

# output the last user's total_time
if current_user:
    print('%s\t%s' % (current_user, total_time))
