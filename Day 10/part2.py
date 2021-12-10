#!/usr/bin/python3
from heapq import heappush, heappop

closer = {
    '(' : ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

scores = []
with open('input.txt') as file:
    for line in file:
        stack = []
        valid = True
        for character in line[:-1]:
            if character in closer:
                stack.append(character)
            elif character != closer[stack.pop()]:
                valid = False
                break
        if valid:
            line_points = 0
            for character in reversed(stack):
                line_points = line_points*5 + points[character]
            heappush(scores, line_points)

result = None
for i in range(len(scores)//2+1):
    result = heappop(scores)

print(result)
