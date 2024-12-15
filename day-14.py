from aoc import get_puzzle
from dataclasses import dataclass
from collections import Counter
from functools import reduce
import numpy as np
import re
import math
import pygame


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int

    def move(self, s, w, h):
        self.px = (self.px + (self.vx * s)) % w
        self.py = (self.py + (self.vy * s)) % h

    def get_quadrant(self, w, h):
        qx = self.px // (w / 2) if self.px != w // 2 else -1
        qy = self.py // (h / 2) if self.py != h // 2 else -1
        return qx + qy * 2 if qx != -1 and qy != -1 else -1

    def __lt__(self, other):
        if self.py < other.py:
            return True
        if self.py == other.py and self.px < other.px:
            return True
        return False

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.px == other[0] and self.py == other[1]
        return False


def display_grid(grid):
    pygame.init()
    rows, cols = grid.shape
    WIDTH, HEIGHT = rows * 8, cols * 8
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for y in range(cols):
            for x in range(rows):
                c = grid[x, y]
                if c == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x * 8, y * 8, 8, 8), 0)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


def get_input():
    RE_STR = re.compile(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)")
    gs = RE_STR.findall(get_puzzle(14))
    return [Robot(*(int(d) for d in g)) for g in gs]


def gen_grid(robots, W, H):
    grid = [[0 for _ in range(W)] for _ in range(H)]
    for r in robots:
        grid[r.py][r.px] = 1
    return np.array(grid)


def get_entropy(grid):
    rows, cols = grid.shape
    b_size = 30
    entropy = []

    for y in range(0, cols, b_size):
        for x in range(0, rows, b_size):
            block = grid[x : x + b_size, y : y + b_size]
            total = block.size

            count_1 = np.sum(block)
            count_0 = total - count_1

            p_1 = count_1 / total if total > 0 else 0
            p_0 = count_0 / total if total > 0 else 0

            b_entropy = 0
            b_entropy -= p_1 * np.log2(p_1) if p_1 > 0 else 0
            b_entropy -= p_0 * np.log2(p_0) if p_0 > 0 else 0

            entropy.append(b_entropy)

    return np.mean(entropy)


def get_lowest_entropy(robots, width, height):
    min_entropy = math.inf
    saved_grid = None
    it = 0
    for i in range(10000):
        for r in robots:
            r.move(1, width, height)

        grid = gen_grid(robots, width, height)
        entropy = get_entropy(grid)

        if entropy < min_entropy:
            min_entropy = entropy
            saved_grid = grid
            it = i
    return saved_grid, it


def part1():
    W = 101
    H = 103
    robots = get_input()
    for r in robots:
        r.move(100, W, H)
    qs = Counter(r.get_quadrant(W, H) for r in robots)
    return reduce((lambda x, y: x * y), (v for k, v in qs.items() if k != -1))


def part2():
    W = 101
    H = 103
    robots = get_input()
    grid, iterations = get_lowest_entropy(robots, W, H)
    display_grid(grid)
    return iterations + 1


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
