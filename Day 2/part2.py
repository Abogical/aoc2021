#!/usr/bin/python3

with open("input.txt") as lines:
    horizontal = 0
    depth = 0
    aim = 0
    for (direction, distance) in (line.split() for line in lines):
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
            depth += aim*distance
        elif direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance
    print(horizontal * depth)
