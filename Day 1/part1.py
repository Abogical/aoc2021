#!/usr/bin/python3

with open("input.txt") as measurements:
    prev_measurement = int(next(measurements))
    increases_count = 0
    for measurement in map(int, measurements):
        if measurement > prev_measurement:
            increases_count += 1
        prev_measurement = measurement
    print(increases_count)
