import re
from typing import DefaultDict
from aoc import get_puzzle


def get_input():
    inp = get_puzzle(19).splitlines()
    patterns = DefaultDict(list)

    for p in inp[0].split(", "):
        patterns[p[0]].append(p)

    designs = inp[2:]

    return patterns, designs


def count_designs(patterns, design, memo):
    if not design:
        return 1

    if design in memo:
        return memo[design]

    possible = 0
    for p in patterns[design[0]]:
        m = re.search(p, design)
        span = m.span() if m else (-1, -1)

        if span[0] == 0:
            possible += count_designs(patterns, design[span[1]:], memo)

    memo[design] = possible
    return possible
            


def part1():
    patterns, designs = get_input()
    return sum(count_designs(patterns, d, {}) > 0 for d in designs)


def part2():
    patterns, designs = get_input()
    return sum(count_designs(patterns, d, {}) for d in designs)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

