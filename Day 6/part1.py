#!/usr/bin/python3
from functools import cache


@cache
def fish_count(timer: int, days_left: int) -> int:
    if timer >= days_left:
        return 1
    skipped_days_left = days_left - timer - 1
    return fish_count(8, skipped_days_left) + fish_count(6, skipped_days_left)


with open("input.txt") as file:
    state = map(int, next(file).split(','))

print(sum(fish_count(n, 80) for n in state))
