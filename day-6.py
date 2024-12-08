from aoc import get_puzzle
from math import pi, cos, sin

test = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."


def do_rounds(world, new_obstacle=None):
    W = len(world.split("\n")[0])
    world = world.replace("\n", "")
    L = len(world)

    guard_pos = world.find("^")
    guard_dir = pi / 2
    visited = set()
    visited.add((guard_pos, guard_dir))

    if new_obstacle is not None and not new_obstacle == guard_pos:
        world = world[:new_obstacle] + "#" + world[new_obstacle+1:]

    while True:
        next_pos = int(guard_pos + cos(guard_dir) - W * sin(guard_dir))

        # Check for bounds
        x_in_bounds = (
            (guard_pos % W) == (next_pos % W) or 
            (guard_pos // W) == (next_pos // W)
        )
        y_in_bounds = 0 <= next_pos < L
        if not x_in_bounds or not y_in_bounds:
            return visited, False

        # Turn right if faced with an obstacle
        if world[next_pos] == "#":
            guard_dir = (guard_dir - pi / 2) % (2 * pi)
        # Check for loops
        elif (next_pos, guard_dir) in visited:
            return visited, True
        else:
            visited.add((next_pos, guard_dir))
            guard_pos = next_pos


def part1():
    visited, _ = do_rounds(get_puzzle(6))
    return len(set(v[0] for v in visited))


def part2():
    w = get_puzzle(6)
    visited, _ = do_rounds(w)
    return sum(do_rounds(w, pos)[1] for pos in set(v[0] for v in visited))


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
