#!/usr/bin/python3

with open('input.txt') as file:
    positions = list(map(int, next(file).split(',')))

minimum = positions[0]
maximum = positions[0]
for i in positions[1:]:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i


def distance(x, y):
    diff = abs(x - y)
    return (diff*(diff+1))//2


print(min(sum(distance(position, target) for position in positions) for target in range(minimum, maximum+1)))

