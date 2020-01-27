import csv
import sys

inputFile = open(sys.argv[1])
bi = 0
wi = 0
ci = 0

rows = csv.reader(inputFile)
for row in rows:
    bi = row.index("business_id")
    wi = row.index("weekday")
    ci = row.index("checkins")
    break
next(rows)

for row in rows:
    print(row[bi] + "\t" + row[wi] + "\t" + row[ci])
