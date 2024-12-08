from typing import DefaultDict
from itertools import combinations
from aoc import get_puzzle


test = "............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"
test2 = "T.........\n...T......\n.T........\n..........\n..........\n..........\n..........\n..........\n..........\n.........."


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x}, {self.y})"


def get_antennas(world):
    antennas = DefaultDict(set)
    for y, row in enumerate(world):
        for x, c in enumerate(row):
            if not c == ".":
                antennas[c].add(Vec2(x, y))
    return antennas


def get_antinodes(antennas, world, harmonics=False):
    W = len(world[0])
    H = len(world)
    nodes = set()

    def in_bounds(p):
        return 0 <= p.x < W and 0 <= p.y < H

    for key in antennas:
        for a1, a2 in combinations(antennas[key], 2):
            node1 = 2 * a1 - a2 if not harmonics else a1
            node2 = 2 * a2 - a1 if not harmonics else a2

            while True:
                b1, b2 = in_bounds(node1), in_bounds(node2)

                if b1:
                    nodes.add(node1)
                    node1 += a1 - a2
                if b2:
                    nodes.add(node2)
                    node2 += a2 - a1

                if not harmonics or not b1 and not b2:
                    break

    return nodes


def part1():
    world = get_puzzle(8).splitlines()
    antennas = get_antennas(world)
    return len(get_antinodes(antennas, world, harmonics=False))


def part2():
    world = get_puzzle(8).splitlines()
    antennas = get_antennas(world)
    nodes = get_antinodes(antennas, world, harmonics=True)
    return len(nodes)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
