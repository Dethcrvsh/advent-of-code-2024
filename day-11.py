from aoc import get_puzzle
from functools import cache
import math
import time

POWER = [10**i for i in range(25)]


@cache
def get_stones(stone, blinks):
    if blinks == 0:
        return 1

    blinks -= 1

    if stone == 0:
        return get_stones(stone + 1, blinks)

    digits = int(math.log10(stone)) + 1

    if digits % 2 == 0:
        p = POWER[digits//2]
        s1 = stone // p
        s2 = stone % p

        return get_stones(s1, blinks) + get_stones(s2, blinks)

    return get_stones(stone * 2024, blinks)


def part1():
    stones = map(int, get_puzzle(11).split(" "))
    return sum(get_stones(s, 25) for s in stones)


def part2():
    stones = map(int, get_puzzle(11).split(" "))
    return sum(get_stones(s, 75) for s in stones)


if __name__ == "__main__":
    print("\n⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    s = time.time()
    print(f"  ❆ Part 2: {part2()}\n")
    print(time.time() - s)
