from aoc import get_puzzle
from dataclasses import dataclass
import numpy as np
import re
import time


@dataclass
class Data:
    ax: int
    ay: int
    bx: int
    by: int
    x: int
    y: int


def get_input():
    RE_STR = re.compile(r".*X\+(\d+)\, Y\+(\d+)\n.*X\+(\d+)\, Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)")
    g = RE_STR.findall(get_puzzle(13))
    return [Data(*(int(d) for d in m)) for m in g]


def get_cost(data):
    cost = 0

    for d in data:
        A = np.array([[d.ax, d.bx], [d.ay, d.by]])
        B = np.array([d.x, d.y])

        ba, bb = np.linalg.solve(A, B)

        if round(ba, 3).is_integer() and round(bb, 3).is_integer():
            cost += 3 * ba + bb

    return int(cost)


def part1():
    data = get_input()
    return get_cost(data)


def part2():
    data = get_input()
    for d in data:
        d.x += 10000000000000
        d.y += 10000000000000
    return get_cost(data)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    s = time.time()
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
    print(f"    Processing time: {round((time.time() - s) * 1000, 2)} ms")
