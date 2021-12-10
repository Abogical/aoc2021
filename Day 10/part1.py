#!/usr/bin/python3

closer = {
    '(' : ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

result = 0
with open('input.txt') as file:
    for line in file:
        stack = []
        for character in line[:-1]:
            if character in closer:
                stack.append(character)
            elif character != closer[stack.pop()]:
                result += points[character]

print(result)
