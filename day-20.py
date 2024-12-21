from aoc import get_puzzle
from math import inf
from heapq import heappush, heappop
from collections import Counter


test = "###############\n#...#...#.....#\n#.#.#.#.#.###.#\n#S#...#.#.#...#\n#######.#.#.###\n#######.#.#...#\n#######.#.###.#\n###..E#...#...#\n###.#######.###\n#...###...#...#\n#.#####.#.###.#\n#.#...#.#.#...#\n#.#.#.#.#.#.###\n#...#...#...###\n###############"


GROUND = '.'
WALL = '#'
START = "S"
GOAL = 'E'


def get_input():
    return [list(row) for row in get_puzzle(20).splitlines()]



def get_pos(c, grid):
    return next(
        ((x, y) for y, row in enumerate(grid) for x, v in enumerate(row) if v == c)
    )


def neighbours(x, y, width, height):
    if x > 0:
        yield x - 1, y
    if x < width - 1:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < height - 1:
        yield x, y + 1


def get_cost(grid, cheat=(-1, -1)):
    width = len(grid[0])
    height = len(grid)
    q = []
    costs = [[inf for _ in range(width)] for _ in range(height)]
    prev = {}
    # Active the cheat
    old_tile = grid[cheat[1]][cheat[0]]
    grid[cheat[1]][cheat[0]] = GROUND

    c = get_pos(START, grid)
    goal = get_pos(GOAL, grid)
    heappush(q, (0, c))
    costs[c[1]][c[0]] = 0

    while q:
        cost, (cx, cy) = heappop(q)

        if (cx, cy) == goal:
            break

        for nx, ny in neighbours(cx, cy, width, height):
            if grid[ny][nx] == WALL:
                continue

            new_cost = cost + 1
            if new_cost < costs[ny][nx]:
                costs[ny][nx] = new_cost
                prev[(nx, ny)] = (cx, cy)
                heappush(q, (new_cost, (nx, ny)))

    # This is cheaper than copying
    grid[cheat[1]][cheat[0]] = old_tile

    path = set()
    cx, cy = goal

    while (cx, cy) != (-1, -1):
        path.add((cx, cy))
        cx, cy = prev.get((cx, cy), (-1, -1))

    return path, costs[goal[1]][goal[0]]


def get_manhattan(dist, grid):
    width = len(grid[0])
    height = len(grid)

    for x in range(dist):
        for y in range(dist, 0, -1):
            print(x, y)




def get_cheats(path, grid):
    width = len(grid[0])
    height = len(grid)
    cheats = set()
    for px, py in path:
        for nx, ny in neighbours(px, py, width, height):
            if grid[ny][nx] == WALL:
                cheats.add((nx, ny))
    return cheats


def print_grid(grid, path):
    for y, row in enumerate(grid):
        r = ""
        for x, c in enumerate(row):
            if (x, y) in path and c not in (START, GOAL):
                r += '*'
            else:
                r += c
        print(r)


def part1():
    grid = get_input()
    path, cost = get_cost(grid)
    cheats = get_cheats(path, grid)
    s = 0

    for i, c in enumerate(cheats):
        print(i / len(cheats))
        if (cost - get_cost(grid, c)[1]) >= 100:
            s += 1
    return s
    # return sum((cost - get_cost(grid, c)[1]) >= 100 for c in cheats)


def part2():
    return 0


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

