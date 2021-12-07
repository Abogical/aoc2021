#!/usr/bin/python3
from dataclasses import dataclass, field
from typing import Dict, Tuple


@dataclass
class Board:
    row_sums: list[int] = field(default_factory=lambda: [0] * 5)
    column_sums: list[int] = field(default_factory=lambda: [0] * 5)


with open("input.txt") as file:
    draws = map(int, next(file).split(','))

    draw_to_board_position: Dict[int, list[Tuple[int, int, int]]] = {}
    boards: list[Board] = []

    board_index = 0
    # Skip empty lines while looping
    while next(file, None) is not None:
        board = Board()
        for row in range(5):
            for column, number in enumerate(map(int, next(file).split())):
                board.row_sums[row] += number
                board.column_sums[column] += number

                position = (board_index, row, column)
                if number in draw_to_board_position:
                    draw_to_board_position[number].append(position)
                else:
                    draw_to_board_position[number] = [position]

        boards.append(board)
        board_index += 1

    for draw in draws:
        if draw in draw_to_board_position:
            for board_index, row, column in draw_to_board_position.pop(draw):
                board = boards[board_index]
                board.row_sums[row] -= draw
                board.column_sums[column] -= draw
                if board.row_sums[row] == 0 or board.column_sums[column] == 0:
                    print(sum(board.row_sums)*draw)
                    exit()


