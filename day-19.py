import re
from aoc import get_puzzle
from functools import cache


def get_input():
    inp = get_puzzle(19).splitlines()
    patterns = tuple(re.compile(p) for p in inp[0].split(", "))
    designs = inp[2:]

    return patterns, designs


@cache
def count_designs(patterns, design):
    if not design:
        return 1

    possible = 0
    for p in patterns:
        m = p.search(design)
        span = m.span() if m else (-1, -1)

        if span[0] == 0:
            possible += count_designs(patterns, design[span[1]:])

    return possible


def part1():
    patterns, designs = get_input()
    return sum(count_designs(patterns, d) > 0 for d in designs)


def part2():
    patterns, designs = get_input()
    return sum(count_designs(patterns, d) for d in designs)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
