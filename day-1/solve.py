from collections import Counter


def part1():
    l1, l2 = zip(*[line.split() for line in open("input").readlines()])
    l1 = sorted(l1)
    l2 = sorted(l2)
    return sum(abs(int(n1)-int(n2)) for n1, n2 in zip(l1, l2))

def part2():
    l1, l2 = zip(*[[int(n) for n in line.split()] for line in open("input").readlines()])
    s = Counter(l2)
    return sum(map(lambda n: n*s[n], l1))

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
