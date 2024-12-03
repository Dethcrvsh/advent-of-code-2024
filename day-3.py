from aoc import get_puzzle
import re


def part1():
    input = get_puzzle(3)
    n = re.findall(r"mul\((\d+)\,(\d+)\)", input)
    return sum(int(i) * int(j) for i, j in n)


def part2():
    input = get_puzzle(3)

    # dollarstore state machine
    mem = ""
    state = True
    out = ""

    for c in input:
        mem += c

        if state and re.search(r"don't\(\)", mem):
            out += mem
            mem = ""
            state = False

        elif not state and re.search(r"do\(\)", mem):
            mem = ""
            state = True
    if state:
        out += mem

    n = re.findall(r"mul\((\d+)\,(\d+)\)", out)
    return sum(int(i) * int(j) for i, j in n)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
