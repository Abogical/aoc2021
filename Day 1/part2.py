#!/usr/bin/python3

with open("input.txt") as measurements:
    first_measurement = int(next(measurements))
    second_measurement = int(next(measurements))
    prev_sum = first_measurement + second_measurement + int(next(measurements))
    increases_count = 0
    for measurement in map(int, measurements):
        current_sum = prev_sum + measurement - first_measurement
        if current_sum > prev_sum:
            increases_count += 1
        first_measurement, second_measurement = second_measurement, prev_sum - first_measurement - second_measurement
        prev_sum = current_sum
    print(increases_count)
