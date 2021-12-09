#!/usr/bin/python3

signal_placements = frozenset(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

digit_to_patterns = [
    frozenset(['a', 'b', 'c', 'e', 'f', 'g']),
    frozenset(['c', 'f']),
    frozenset(['a', 'c', 'd', 'e', 'g']),
    frozenset(['a', 'c', 'd', 'f', 'g']),
    frozenset(['b', 'c', 'd', 'f']),
    frozenset(['a', 'b', 'd', 'f', 'g']),
    frozenset(['a', 'b', 'd', 'e', 'f', 'g']),
    frozenset(['a', 'c', 'f']),
    signal_placements,
    frozenset(['a', 'b', 'c', 'd', 'f', 'g'])
]

result = 0
with open('input.txt') as file:
    for line in file:
        patterns, to_deduce = (segment.split() for segment in line.split('|'))
        possibilities = dict((signal, set(signal_placements)) for signal in signal_placements)

        def refine_possibilities(pattern_set, replacement_set):
            for signal in signal_placements:
                if signal in pattern_set:
                    possibilities[signal] &= replacement_set
                else:
                    possibilities[signal] -= replacement_set

        five_signals_common = signal_placements.copy()
        six_signals_common = signal_placements.copy()

        two_signal_pattern = None
        three_signal_pattern = None
        four_signal_pattern = None

        for pattern in patterns:
            if len(pattern) == 2:
                two_signal_pattern = set(pattern)
            elif len(pattern) == 3:
                three_signal_pattern = set(pattern)
            elif len(pattern) == 4:
                four_signal_pattern = set(pattern)
            elif len(pattern) == 5:
                five_signals_common &= set(pattern)
            elif len(pattern) == 6:
                six_signals_common &= set(pattern)

        if two_signal_pattern is not None:
            refine_possibilities(two_signal_pattern, digit_to_patterns[1])

        if three_signal_pattern is not None:
            refine_possibilities(three_signal_pattern, digit_to_patterns[7])

        if four_signal_pattern is not None:
            refine_possibilities(four_signal_pattern, digit_to_patterns[4])

        if len(five_signals_common) == 3:
            refine_possibilities(
                five_signals_common, digit_to_patterns[2] & digit_to_patterns[3] & digit_to_patterns[5]
            )

        if len(six_signals_common) == 4:
            refine_possibilities(six_signals_common, digit_to_patterns[0] & digit_to_patterns[6] & digit_to_patterns[9])

        assert all(len(possibility) == 1 for possibility in possibilities.values())

        number = 0
        for pattern in to_deduce:
            number = number*10 + digit_to_patterns.index(frozenset().union(*(
                possibilities[signal] for signal in pattern
            )))

        result += number

print(result)
