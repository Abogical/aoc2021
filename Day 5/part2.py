#!/usr/bin/python3
import re
from typing import Tuple

line_processor = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')


more_than_ones: set[Tuple[int, int]] = set()
ones: set[Tuple[int, int]] = set()
counter = 0


def between(n1, n2):
    return range(n1, n2+1) if n1 <= n2 else range(n1, n2-1, -1)


def set_ocean(index):
    global counter
    if index not in more_than_ones:
        if index in ones:
            counter += 1
            more_than_ones.add(index)
        else:
            ones.add(index)


with open("input.txt") as file:
    for x1,y1,x2,y2 in (map(int, line_processor.match(line).groups()) for line in file):
        if x1 == x2:
            for y in between(y1, y2):
                set_ocean((x1, y))
        elif y1 == y2:
            for x in between(x1, x2):
                set_ocean((x, y1))
        else:
            for x, y in zip(between(x1, x2), between(y1, y2)):
                set_ocean((x, y))

print(counter)
