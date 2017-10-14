#!/usr/bin/env python3

"""

Find tweets that:

- use a `
- do not use a ' (appears to be legit quoting)
- are in the English language (as detected by Twitter)
- are sent from a user purporting to be in a US timezone

Write them out as a CSV.

Also, fetch the current metadata for any discovered users and append it to a 
file in the users directory so the users stats (follower, following, etc) 
can be tracked over time.

"""

import csv
import json
import twarc
import datetime
import json2csv

twitter = twarc.Twarc()

time_zones = [
    "Eastern Time (US & Canada)",
    "Central Time (US & Canada)",
    "Mountain Time (US & Canada)",
    "Pacific Time (US & Canada)"
]

output = csv.writer(open("tweets.csv", "w"))
output.writerow(json2csv.get_headings())
user_ids = set()

for line in open("apostrophe.json"):
    tweet = json.loads(line)
    if tweet.get('retweeted_status') == None \
            and tweet["user"]["time_zone"] in time_zones \
            and tweet["lang"] == "en" \
            and "'" not in tweet["text"] \
            and "’" not in tweet["text"]:
        output.writerow(json2csv.get_row(tweet))
        user_ids.add(tweet["user"]["id_str"])

t = datetime.datetime.utcnow().isoformat()
for user in twitter.user_lookup(user_ids=user_ids):
    fh = open("users/%s.tsv" % user['id_str'], "at")
    fh.write(t + "\t" + json.dumps(user) + "\n")
