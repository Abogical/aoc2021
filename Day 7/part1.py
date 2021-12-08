#!/usr/bin/python3

with open('input.txt') as file:
    positions = list(map(int, next(file).split(',')))

median_position = sorted(positions)[len(positions)//2]

print(sum(abs(position-median_position) for position in positions))
