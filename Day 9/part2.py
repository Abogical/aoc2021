#!/usr/bin/python3
from typing import Tuple, Union
from heapq import nlargest

basins: dict[Tuple[int, int], Union[int, Tuple[int, int]]] = {}
with open('input.txt') as file:
    prev_row = []
    current_basin = None
    for column, entry in enumerate(map(int, next(file)[:-1])):
        if entry == 9:
            current_basin = None
        else:
            if current_basin is None:
                current_basin = (-1, column)
                basins[current_basin] = 1
            else:
                basins[current_basin] += 1

        prev_row.append(current_basin)

    for row, line in enumerate(file):
        current_basin = None
        current_row = []
        for column, entry in enumerate(map(int, line[:-1])):
            if entry == 9:
                current_basin = None
            else:
                if current_basin is None:
                    if prev_row[column] is None:
                        current_basin = (row, column)
                        basins[current_basin] = 0
                    else:
                        current_basin = prev_row[column]
                        next_key = basins[current_basin]
                        while not isinstance(next_key, int):
                            current_basin = next_key
                            next_key = basins[current_basin]

                elif prev_row[column] is not None and prev_row[column] != current_basin:
                    # Merge basins
                    root_basin = prev_row[column]
                    next_key = basins[root_basin]
                    while not isinstance(next_key, int):
                        root_basin = next_key
                        next_key = basins[root_basin]

                    if root_basin != current_basin:
                        basins[root_basin] += basins[current_basin]
                        basins[current_basin] = root_basin
                        current_basin = root_basin
                basins[current_basin] += 1
            current_row.append(current_basin)
        prev_row = current_row

A, B, C = nlargest(3, filter(lambda x: isinstance(x, int), basins.values()))
print(A*B*C)
