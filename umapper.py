#!/usr/bin/python3

import csv
import sys
import re

inputFile = open(sys.argv[1])
bi = 0

rows = csv.reader(inputFile)
for row in rows:
    bi = row.index("text")
    break
next(rows)

for row in rows:
    text = row[bi].strip()
    line = re.sub(r'^\W+|\W+$', '', text)
    words = line.split()
    for word in words:
        print(word.lower() + "\t1")
