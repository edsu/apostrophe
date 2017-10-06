#!/usr/bin/env python3

"""
Read the filter stream for some keywords and print out tweets that use a `.
"""

import sys
import json
import twarc

tweets = twarc.Twarc()

count = 0
for tweet in tweets.filter('trump,russia,fakenews,korea,nuclear,politics'):
    if count % 100 == 0:
        sys.stderr.write(".")
        sys.stderr.flush()

    count +=1 

    if 'text' in tweet and '`' in tweet['text']:
        sys.stderr.write("💥")
        sys.stderr.flush()
        print(json.dumps(tweet))
