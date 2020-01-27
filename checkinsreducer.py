import sys

previousBus = None
previousDay = None
weekdays = {'Sun': 0, 'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0}

out = open("checkinsbyday.txt", "w+")

for line in sys.stdin:
    bus, day, value = line.split("\t")

    if bus != previousBus:  # new business
        if previousBus is not None and previousDay is not None:
            for v in weekdays:
                if weekdays[v] != 0:
                    out.write(previousBus + ",\t" + previousDay + ",\t" + str(weekdays[v]) + "\n")
        previousBus = bus
        previousDay = day
        for key in weekdays:
            weekdays[key] = 0

    for weekday in weekdays.keys():
        if weekday == previousDay:
            weekdays[weekday] += int(value)

for v in weekdays:
    if weekdays[v] != 0:
        out.write(previousBus + ",\t" + previousDay + ",\t" + str(weekdays[v]) + "\n")
