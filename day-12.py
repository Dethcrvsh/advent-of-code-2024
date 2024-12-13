from aoc import get_puzzle
from random import randint, uniform
from threading import Thread
from time import sleep
import pygame


test = "RRRRIICCFF\nRRRRIICCCF\nVVRRRCCFFF\nVVRCCCJFFF\nVVVVCJJCFE\nVVIVCCJJEE\nVVIIICJJEE\nMIIIIIJJEE\nMIIISIJEEE\nMMMISSJEEE"
screen = None


# Generate pastel colors
def generate_pastel_color():
    r = randint(103, 230)  # Keep colors light
    g = randint(103, 230)  # Keep colors light
    b = randint(103, 230)  # Keep colors light
    return (r, g, b)


# Assign a pastel color to each letter in the alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
colors = {letter: generate_pastel_color() for letter in alphabet}


def draw(x, y, p):
    if screen:
        pygame.draw.rect(screen, colors[p], (x * 50, y * 50, 50, 50))


def visualize(width, height):
    global screen

    screen = pygame.display.set_mode((width * 50 + 50, height * 50 + 50))
    screen.fill((30, 20, 10))

    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Close button
                running = False

        # Draw everything

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)


def is_corner(x, y, plants):
    p = plants[y][x]
    neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    shared_n = sum(plants[ny][nx] == p for nx, ny in neighbours)

    if shared_n == 4:
        return False
    if shared_n == 3:
        return True
    if shared_n == 2:
        is_opposing_x = plants[y][x-1] == p and plants[y][x+1]
        is_opposing_y = plants[y-1][x] == p and plants[y+1][x]
        return not is_opposing_x and not is_opposing_y 
    if shared_n <= 1:
        return True

    return False


def get_area(x, y, plants, visited):
    visited.add((x, y))
    area = 1
    fence = 0

    corners = int(is_corner(x, y, plants))

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy

        if plants[y][x] != plants[ny][nx]:
            fence += 1
            continue
        if (nx, ny) in visited:
            continue

        rest_area, rest_fence, rest_corners = get_area(nx, ny, plants, visited)
        area += rest_area
        fence += rest_fence
        corners += rest_corners

    return area, fence, corners


def get_input():
    # world = get_puzzle(12).splitlines()
    world = test.splitlines()
    # Pad to dodge those pesky bounds checks
    world = ["." + r + "." for r in world]
    world.insert(0, "." * (len(world[0])))
    world.append("." * (len(world[0])))
    return world


def part1():
    world = get_input()
    W = len(world[0])
    H = len(world)

    price = 0
    visited = set()

    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if (x, y) in visited:
                continue
            area, fence, corners = get_area(x, y, world, visited)
            print(corners)
            price += area * fence
    return price


def part2():
    pass
    # world = get_input()
    # W = len(world[0])
    # H = len(world)

    # price = 0
    # visited = set()

    # for y in range(1, H - 1):
    #     for x in range(1, W - 1):
    #         if (x, y) in visited:
    #             continue
    #         area, fence = get_area(x, y, world, visited)
    #         price += area * fence
    # return price


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
