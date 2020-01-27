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
    offset = 0
    while offset < (len(words) - 2):
        string = words[offset] + " " + words[offset + 1] + " " + words[offset + 2]
        print(string.lower() + "\t1")
        offset += 1
