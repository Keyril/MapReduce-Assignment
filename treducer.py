import sys

previous = None
sum_ = 0

out = open("trigrams.txt", "w+")

for line in sys.stdin:
    key, value = line.split("\t")

    if key != previous:
        if previous is not None:
            out.write(str(sum_) + '\t' + previous + "\n")
        previous = key
        sum_ = 0

    sum_ = sum_ + int(value)

out.write(str(sum_)+"\t"+previous + "\n")
