from aoc import get_puzzle
from functools import cache
import time
import math


@cache
def get_stones(stone, blinks):
    if blinks == 0:
        return 1

    blinks -= 1

    if stone == 0:
        return get_stones(stone + 1, blinks)

    digits = int(math.log10(stone)) + 1

    if digits % 2 == 0:
        s1 = stone // (10 ** (digits / 2))
        s2 = stone % (10 ** (digits / 2))

        return get_stones(s1, blinks) + get_stones(s2, blinks)

    return get_stones(stone * 2024, blinks)


def part1():
    stones = map(int, get_puzzle(11).split(" "))
    return sum(get_stones(s, 25) for s in stones)


def part2():
    stones = map(int, get_puzzle(11).split(" "))
    return sum(get_stones(s, 75) for s in stones)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
