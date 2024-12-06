from aoc import get_puzzle
test = "47|53\n97|13\n97|61\n97|47\n75|29\n61|13\n75|53\n29|13\n97|29\n53|29\n61|53\n97|53\n61|29\n47|13\n75|47\n97|75\n47|61\n75|61\n47|29\n75|13\n53|13\n\n75,47,61,53,29\n97,61,53,29,13\n75,29,13\n75,97,47,61,53\n61,13,29\n97,13,75,29,47"


def is_right(pages, rules):
    for check, ps in zip(pages, [pages[i+1:] for i in range(len(pages))]):
        if any(rules[p] and check in rules[p] for p in ps):
            return False
    return True


def part1():
    inp = get_puzzle(5).split("\n\n")
    inp_rules = inp[0].splitlines()
    pages = [list(map(int, r.split(","))) for r in inp[1].splitlines()]

    rules = [[] for _ in range(100)]
    for r in inp_rules:
        i = r.split("|")
        rules[int(i[0])] += [int(i[1])]

    return sum(r[len(r)//2] for r in filter(lambda p: is_right(p, rules), pages))


def part2():
    pass


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
