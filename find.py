#!/usr/bin/env python

"""
Find tweets that use a ` from users who say they are in the United States.
"""

import csv
import json
import json2csv

time_zones = [
    "Eastern Time (US & Canada)",
    "Central Time (US & Canada)",
    "Mountain Time (US & Canada)",
    "Pacific Time (US & Canada)"
]

output = csv.writer(open("tweets.csv", "w"))
output.writerow(json2csv.get_headings())

for line in open("apostrophe.json"):
    tweet = json.loads(line)
    if tweet.get('retweeted_status') == None \
            and tweet["user"]["time_zone"] in time_zones \
            and tweet["lang"] == "en":
        output.writerow(json2csv.get_row(tweet))
