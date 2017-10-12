#!/bin/bash

# A script to run from cron to update the CSV and collect user metadata
# and push them to GitHub. I guess this could happen as system calls in
# update.py but it seemed easier this way.

export HOME=/home/ed

PROJECT_DIR="$HOME/Projects/apostrophe"
cd $PROJECT_DIR

pipenv shell
./update.py

comment="latest content at `date`"
git add users
git commit -m "$comment" tweets.csv users && git push origin master
