from typing import DefaultDict
from aoc import get_puzzle
from heapq import heappush, heappop
from math import inf, asin, acos, atan2

test = "###############\n#.......#....E#\n#.#.###.#.###.#\n#.....#.#...#.#\n#.###.#####.#.#\n#.#.#.......#.#\n#.#.#####.###.#\n#...........#.#\n###.#.#####.#.#\n#...#.....#.#.#\n#.#.#.###.#.#.#\n#.....#...#.#.#\n#.###.#.#.#.#.#\n#S..#.....#...#\n###############"

REINDEER = 'S'
WALL = '#'
GOAL = 'E'


def print_maze(maze, path=None):
    if path is not None:
        for x, y in path:
            maze[y][x] = 'O'

    for row in maze:
        print("".join(row))


def get_input():
    return [list(row) for row in get_puzzle(16).splitlines()]


def get_reindeer(maze):
    return next(
        ((x, y) for y, row in enumerate(maze) for x, v in enumerate(row) if v == REINDEER)
    )


def get_goal(maze):
    return next(
        ((x, y) for y, row in enumerate(maze) for x, v in enumerate(row) if v == GOAL)
    )


def neighbours(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


def get_path(maze):
    W = len(maze[0])
    H = len(maze)
    queue = []
    costs = [[inf for _ in range(W)] for _ in range(H)]
    prev = DefaultDict(list)

    reindeer = get_reindeer(maze)
    goal = get_goal(maze)

    heappush(queue, (0, reindeer, (1, 0)))
    costs[reindeer[1]][reindeer[0]] = 0

    while queue:
        cost, (cx, cy), dir = heappop(queue)

        for nx, ny in neighbours(cx, cy):
            if maze[ny][nx] == WALL:
                continue

            new_dir = (nx - cx, ny - cy)
            new_cost = cost + 1 + 1000 * (dir != new_dir)

            if new_cost < costs[ny][nx]:
                costs[ny][nx] = new_cost
                prev[(nx, ny)] += [(cx, cy)]
                heappush(queue, (new_cost, (nx, ny), new_dir))
            elif new_cost == costs[ny][nx]:
                prev[(nx, ny)] += [(cx, cy)]

    all_paths = []

    def backtrack(node, path):
        if node == reindeer:
            all_paths.append(path[::-1])
            return
        for prev_node in prev.get(node, []):
            backtrack(prev_node, path + [node])

    backtrack(goal, [])
    
    return all_paths, costs[goal[1]][goal[0]]


def part1():
    maze = get_input()
    _, cost = get_path(maze)
    return cost


def part2():
    maze = get_input()
    paths, _ = get_path(maze)

    unique_nodes = set()
    for p in paths:
        for node in p:
            unique_nodes.add(node)

    return len(unique_nodes) + 1


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

