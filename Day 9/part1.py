#!/usr/bin/python3
from math import inf
from typing import Union

result = 0
with open('input.txt') as file:
    next_row = [inf] + [int(x) for x in next(file)[:-1]] + [inf]
    prev_row: list[Union[int, float]] = [inf] * len(next_row)
    current_row = next_row

    def add_lows():
        global result
        for i in range(1, len(next_row) - 1):
            if current_row[i] < prev_row[i] and current_row[i] < current_row[i - 1] and \
                    current_row[i] < current_row[i + 1] and current_row[i] < next_row[i]:
                result += current_row[i] + 1

    for next_row in ([inf] + [int(x) for x in line[:-1]] + [inf] for line in file):
        add_lows()
        prev_row, current_row = current_row, next_row

next_row = [inf] * len(next_row)
add_lows()

print(result)
