from aoc import get_puzzle
from collections import Counter


def part1():
    l1, l2 = zip(*[line.split() for line in get_puzzle(1).splitlines()])
    l1 = sorted(l1)
    l2 = sorted(l2)
    return sum(abs(int(n1)-int(n2)) for n1, n2 in zip(l1, l2))

def part2():
    l1, l2 = zip(*[line.split() for line in get_puzzle(1).splitlines()])
    s = Counter(l2)
    return sum(map(lambda n: int(n)*s[n], l1))

if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
