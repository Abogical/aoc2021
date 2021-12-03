#!/usr/bin/python3

with open("input.txt") as lines:
    ones_count = [0] * 12
    lines_count = 0
    for line in lines:
        lines_count += 1
        for i in range(12):
            if line[i] == '1':
                ones_count[i] += 2

    gamma = 0
    for i in range(12):
        if ones_count[i] > lines_count:
            gamma |= 1 << (11-i)

    print(gamma * (~gamma & 0b111111111111))
