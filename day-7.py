from itertools import product
from aoc import get_puzzle


class cint(int):
    def __add__(self, other):
        return cint(super().__add__(other))

    def __mul__(self, other):
        return cint(super().__mul__(other))

    def __or__(self, other):
        return cint(str(self) + str(other))


def get_operators(nums, ops):
    operators = product(ops, repeat=len(nums)-1)
    exps = []

    for ops in operators:
        exp = f"{'(' * (len(nums)-1)} cint({str(nums[0])})"
        for op, n in zip(ops, nums[1:]):
            exp += f"{op} cint({str(n)}))"
        exps.append(exp)

    return exps


def get_input():
    return [
        [int(n) for n in ln.replace(":", "").split(" ")]
        for ln in get_puzzle(7).splitlines()
    ]


def part1():
    eqs = get_input()
    s = 0

    for sum, *nums in eqs:
        if any(eval(eq) == sum for eq in get_operators(nums, "+*")):
            s += sum
    return s


def part2():
    eqs = get_input()
    s = 0

    for sum, *nums in eqs:
        if any(eval(eq) == sum for eq in get_operators(nums, "+*|")):
            s += sum
    return s


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
