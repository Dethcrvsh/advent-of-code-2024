from aoc import get_puzzle
import re


def diagonalize(string):
    strings = string.splitlines()
    n = len(strings)
    m = len(strings[0])
    diagonals = [""] * (n + m - 1)

    for y, row in enumerate(strings):
        for x, char in enumerate(row):
            diagonals[y + x] += char
    return "\n".join(diagonals)


def part1():
    x = get_puzzle(4)
    y = "\n".join("".join(r) for r in zip(*x.splitlines())) # transpose string
    d1 = diagonalize(x)
    d2 = diagonalize("\n".join(r[::-1] for r in x.splitlines()))

    return len(re.findall(r"(?=(XMAS|SAMX))", x + y + d1 + d2))


def part2():
    inp = get_puzzle(4).splitlines()

    diags = []
    for y, row in enumerate(inp[1:-1]):
        for x, c in enumerate(row[1:-1]):
            if c == "A":
                # Get the words on the diagonals
                diags += [((inp[y][x] + c + inp[y+2][x+2]), (inp[y][x+2] + c + inp[y+2][x]))]
            
    return sum(1 for d in diags if all(w in ["MAS", "SAM"] for w in d))


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
