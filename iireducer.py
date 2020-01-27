import sys

previous = None
b = []  # array to store business ids

out = open("inverted-index.txt", "w+")

for line in sys.stdin:
    key, value = line.split("\t")

    if key != previous:
        if previous is not None:
            out.write(previous + "\t" + str(b) + "\t")
            print(previous + "\t" + str(b) + "\t")
        previous = key
        b = []

    b.append(value.rstrip())

out.write(previous + "\t" + str(b) + "\t")
print(previous + "\t" + str(b) + "\t")

