#!/usr/bin/env python3

"""

Find tweets that:

- use a `
- do not use a ' (appears to be legit quoting)
- is in the English language (as detected by Twitter0
- is sent from a user in a US timezone

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
            and tweet["lang"] == "en" \
            and "'" not in tweet["text"] \
            and "’" not in tweet["text"]:
        output.writerow(json2csv.get_row(tweet))
