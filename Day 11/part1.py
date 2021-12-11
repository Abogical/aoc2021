#!/usr/bin/python3

import numpy as np

with open('input.txt') as file:
    array = np.array([[int(character) for character in line[:-1]] for line in file])

flash_count = 0
for step in range(100):
    array += 1
    flashes = np.zeros(array.shape, dtype=bool)
    new_flashes = array >= 10
    while np.any(new_flashes):
        flashes_padded = np.pad(new_flashes, 1).astype(int)
        array += (
            flashes_padded[0:-2, 0:-2] + flashes_padded[0:-2, 1:-1] + flashes_padded[0:-2, 2:] +
            flashes_padded[1:-1, 0:-2] + flashes_padded[1:-1, 2:] +
            flashes_padded[2:, 0:-2] + flashes_padded[2:, 1:-1] + flashes_padded[2:, 2:]
        )
        flashes |= new_flashes
        new_flashes = (array >= 10) & ~flashes

    flash_count += np.sum(flashes)
    array[flashes] = 0

print(flash_count)
