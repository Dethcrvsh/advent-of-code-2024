from aoc import get_puzzle
from typing import DefaultDict
from heapq import heappush, heappop
from math import inf


test = "5,4\n4,2\n4,5\n3,0\n2,1\n6,3\n2,4\n1,5\n0,6\n3,3\n2,6\n5,1\n1,2\n5,5\n2,5\n6,5\n1,4\n0,4\n6,4\n1,1\n6,1\n1,0\n0,5\n1,6\n2,0"


def get_input():
    return [tuple(int(i) for i in r.split(',')) for r in get_puzzle(18).splitlines()]


def neighbours(x, y, width, height):
    if x > 0:
        yield x - 1, y
    if x < width - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < height - 1:
        yield x, y + 1


def get_cost(obst, width, height):
    q = []
    costs = [[inf for _ in range(width)] for _ in range(height)]
    obst = set(obst)

    c = (0, 0)
    goal = (width - 1, height - 1)
    heappush(q, (0, c))
    costs[c[1]][c[0]] = 0

    while q:
        cost, (cx, cy) = heappop(q)

        if (cx, cy) == goal:
            break

        for nx, ny in neighbours(cx, cy, width, height):
            if (nx, ny) in obst:
                continue

            new_cost = cost + 1
            if new_cost < costs[ny][nx]:
                costs[ny][nx] = new_cost
                heappush(q, (new_cost, (nx, ny)))

    return costs[goal[1]][goal[0]]


def part1():
    w = get_input()[:1024]
    width = max(w, key=lambda x: x[0])[0] + 1
    height = max(w, key=lambda x: x[1])[1] + 1
    return get_cost(w, width, height)


def part2():
    w = get_input()
    width = max(w, key=lambda x: x[0])[0] + 1
    height = max(w, key=lambda x: x[1])[1] + 1

    for i in range(1024, len(w)):
        cost = get_cost(w[:i], width, height)
        if cost == inf:
            return w[i-1]


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

