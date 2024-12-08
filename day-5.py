from aoc import get_puzzle
from functools import cmp_to_key


def parse_input():
    inp = get_puzzle(5).split("\n\n")
    inp_rules = inp[0].splitlines()
    pages = [list(map(int, r.split(","))) for r in inp[1].splitlines()]

    rules = [[] for _ in range(100)]
    for r in inp_rules:
        i = r.split("|")
        rules[int(i[0])] += [int(i[1])]

    return pages, rules


def is_right(pages, rules):
    for check, ps in zip(pages, [pages[i + 1 :] for i in range(len(pages))]):
        if any(rules[p] and check in rules[p] for p in ps):
            return False
    return True


def part1():
    pages, rules = parse_input()
    return sum(r[len(r) // 2] for r in filter(lambda p: is_right(p, rules), pages))


def part2():
    pages, rules = parse_input()

    def compare(p1, p2):
        return -1 if p1 not in rules[p2] else 0

    pages_updated = map(lambda p: sorted(p, key=cmp_to_key(compare)), pages)
    pages_correct = filter(lambda p: p not in pages, pages_updated)
    
    return sum(r[len(r) // 2] for r in pages_correct)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
