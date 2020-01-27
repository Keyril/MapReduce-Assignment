import sys

rows = sys.stdin
next(rows)

for row in rows:
    row = row.strip()
    columns = row.split(',')
    categories = columns[12].split(';')
    for c in categories:
        print(c + "\t" + columns[0])
