import re
from aoc import get_puzzle

ROBOT = '@'
GROUND = '.'
WALL = '#'
BOX = 'O'
BOX_LEFT = '['
BOX_RIGHT = ']'


def get_input():
    RE_STR = re.compile(r"(#+\n(?:#.*#\n)+#+)\n\n([\s\S]+)") 
    m = RE_STR.match(get_puzzle(15))

    if m is None:
        return [], []

    g, d = m.groups()

    grid = [[c for c in line] for line in g.splitlines()]
    dir_map = {'>': (1, 0), '<': (-1, 0), 'v': (0, 1), '^': (0, -1)}
    dirs = [dir_map[c] for c in d.replace('\n', '')]

    return grid, dirs


def get_expanded_input():
    grid, dirs = get_input()
    W = len(grid[0])
    H = len(grid)
    exp_grid = [['' for _ in range(W * 2)] for _ in range(H)]

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ROBOT:
                exp_grid[y][x*2] = ROBOT
                exp_grid[y][x*2 + 1] = GROUND
            elif c == 'O':
                exp_grid[y][x*2] = BOX_LEFT 
                exp_grid[y][x*2 + 1] = BOX_RIGHT
            else:
                exp_grid[y][x*2] =  c
                exp_grid[y][x*2 + 1] = c

    return exp_grid, dirs
    

def move(grid, agent, dir):
    ax, ay = agent[0], agent[1]
    dx, dy = dir[0], dir[1]
    nx, ny = ax + dx, ay + dy

    tile = grid[ay][ax]

    if grid[ny][nx] == BOX:
        move(grid, (nx, ny), dir)

    if grid[ny][nx] == GROUND:
        grid[ay][ax] = GROUND
        grid[ny][nx] = tile
        return nx, ny

    return ax, ay


def can_move(grid, agent, dir):
    org_x, org_y = agent[0], agent[1]
    dy = dir[1]

    org_tile = grid[org_y][org_x]

    if org_tile == WALL:
        return False
    if org_tile == GROUND:
        return True

    left_x, left_y = (org_x, org_y) if org_tile == BOX_LEFT else (org_x - 1, org_y)
    right_x, right_y = (org_x, org_y) if org_tile == BOX_RIGHT else (org_x + 1, org_y)

    return can_move(grid, (left_x, left_y + dy), dir) and can_move(grid, (right_x, right_y + dy), dir)


def move_expanded(grid, agent, dir):
    org_x, org_y = agent[0], agent[1]
    dx, dy = dir[0], dir[1]
    new_x, new_y = org_x + dx, org_y + dy

    org_tile = grid[org_y][org_x]

    if org_tile in (GROUND, WALL):
        return org_x, org_y

    do_double = dy != 0 and org_tile in (BOX_LEFT, BOX_RIGHT)

    if do_double:
        left_x, left_y = (org_x, org_y) if org_tile == BOX_LEFT else (org_x - 1, org_y)
        right_x, right_y = (org_x, org_y) if org_tile == BOX_RIGHT else (org_x + 1, org_y)

        if not can_move(grid, (left_x, left_y + dy), dir) or not can_move(grid, (right_x, right_y + dy), dir):
            return org_x, org_y

        move_expanded(grid, (left_x, left_y + dy), dir)
        move_expanded(grid, (right_x, right_y + dy), dir)

        if grid[left_y + dy][left_x] == GROUND and grid[right_y + dy][right_x] == GROUND:
            grid[left_y + dy][left_x] = BOX_LEFT
            grid[right_y + dy][right_x] = BOX_RIGHT
            grid[left_y][left_x] = GROUND
            grid[right_y][right_x] = GROUND
            return new_x, new_y

    else:
        move_expanded(grid, (new_x, new_y), dir)

        if grid[new_y][new_x] == GROUND:
            grid[new_y][new_x] = org_tile
            grid[org_y][org_x] = GROUND
            return new_x, new_y

    return org_x, org_y


def simulate(grid, dirs, move_func):
    robot = next(
        ((x, y) for y, row in enumerate(grid) for x, v in enumerate(row) if v == ROBOT)
    )
    for dir in dirs:
        robot = move_func(grid, robot, dir)


def get_cost(grid, t=BOX):
    cost = 0

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == t:
                cost += x + y * 100

    return cost


def part1():
    grid, dirs = get_input()
    simulate(grid, dirs, move)
    return get_cost(grid)


def part2():
    grid, dirs = get_expanded_input()
    simulate(grid, dirs, move_expanded)
    return get_cost(grid, '[')


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")

