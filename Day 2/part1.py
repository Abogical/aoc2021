#!/usr/bin/python3

with open("input.txt") as lines:
    horizontal = 0
    depth = 0
    for (direction, distance) in (line.split() for line in lines):
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
        elif direction == 'down':
            depth += distance
        elif direction == 'up':
            depth -= distance
    print(horizontal*depth)

