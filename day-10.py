from aoc import get_puzzle


def get_score(world, x, y, unique, visited=None):
    if visited is None:
        visited = set()

    W = len(world[0])
    H = len(world)

    n = int(world[y][x])
    visited.add((x, y))

    if n == 9:
        return 1

    paths = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = (x + dx, y + dy)

        if not unique and (nx, ny) in visited:
            continue

        if not 0 <= nx < W or not 0 <= ny < H:
            continue

        if not int(world[ny][nx]) == n + 1:
            continue

        paths += get_score(world, nx, ny, unique, visited)

    return paths


def part1():
    world = get_puzzle(10).splitlines()

    paths = 0
    for y, row in enumerate(world):
        for x, n in enumerate(row):
            if n == "0":
                paths += get_score(world, x, y, False)
    return paths


def part2():
    world = get_puzzle(10).splitlines()

    paths = 0
    for y, row in enumerate(world):
        for x, n in enumerate(row):
            if n == "0":
                paths += get_score(world, x, y, True)
    return paths


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
