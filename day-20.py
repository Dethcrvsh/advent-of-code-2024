from typing import DefaultDict
from aoc import get_puzzle
from math import inf
from heapq import heappush, heappop


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


def get_path(grid):
    width = len(grid[0])
    height = len(grid)
    q = []
    costs = [[inf for _ in range(width)] for _ in range(height)]
    prev = {}

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

    path = set()
    cx, cy = goal

    while (cx, cy) != (-1, -1):
        path.add((cx, cy))
        cx, cy = prev.get((cx, cy), (-1, -1))

    return path, costs


def get_manhattan(dist, pos, grid):
    def in_bounds(x, y):
        width = len(grid[0])
        height = len(grid)
        return 0 <= x < width and 0 <= y < height

    def add_row(dx, dy):
        for i in range(-dx, dx + 1):
            npx, npy = (px + i, py + dy) 
            if in_bounds(npx, npy):
                manhattan.add((npx, npy))

    px, py = pos
    manhattan = set()

    for dy in range(-dist, 1):
        add_row(dy + dist, dy)
    for dy in range(dist, 0, -1):
        add_row(dist - dy, dy)

    return manhattan


def get_shortcuts(grid, seconds):
    path, costs = get_path(grid)
    shortcuts = set()

    for cx, cy in path:
        for mx, my in get_manhattan(seconds, (cx, cy), grid):
            old_cost = costs[cy][cx]
            new_cost = costs[my][mx]
            dist = (abs(cx - mx) + abs(cy - my))

            if new_cost < old_cost - dist - 100 + 1:
                shortcuts.add(((cx, cy), (mx, my)))
        
    return shortcuts


def part1():
    grid = get_input()
    return len(get_shortcuts(grid, 2))

def part2():
    grid = get_input()
    return len(get_shortcuts(grid, 20))


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

