#!/usr/bin/python3
from itertools import chain

with open('input.txt') as file:
    print(sum(chain.from_iterable(
        (2 <= len(digit) <= 4 or len(digit) == 7
         for digit in line.split('|')[1].split()) for line in file)))
