#!/usr/bin/python3
from typing import Optional, Callable
from dataclasses import dataclass


# Store all inputs in a huffman tree
@dataclass
class HuffmanNode:
    one: Optional['HuffmanNode'] = None
    zero: Optional['HuffmanNode'] = None

    one_count: int = 0
    zero_count: int = 0


root = HuffmanNode()


def rating(comparison: Callable[[int, int], bool]) -> int:
    rating_node = root
    result = 0

    for j in range(12):
        if comparison(rating_node.one_count, rating_node.zero_count):
            if rating_node.one_count == 0:
                break
            else:
                result |= 1 << (11 - j)
                rating_node = rating_node.one
        elif rating_node.zero_count == 0:
            print(j, rating_node)
            break
        else:
            rating_node = rating_node.zero

    for k in range(j, 12):
        if rating_node.one_count == 0:
            rating_node = rating_node.zero
        else:
            rating_node = rating_node.one
            result |= 1 << (11 - k)

    return result


with open("input.txt") as lines:
    for line in lines:
        node = root
        for i in range(12):
            if line[i] == '1':
                if node.one_count == 0:
                    node.one = HuffmanNode()
                node.one_count += 1
                node = node.one
            else:
                if node.zero_count == 0:
                    node.zero = HuffmanNode()
                node.zero_count += 1
                node = node.zero

    oxygen_rating = rating(lambda x, y: x >= y)
    scrubber_rating = rating(lambda x, y: x < y)

    print(oxygen_rating*scrubber_rating)


