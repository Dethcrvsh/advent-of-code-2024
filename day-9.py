from aoc import get_puzzle
from typing import DefaultDict


def parse_input():
    inp = get_puzzle(9)
    disk = []
    for i, (b, s) in enumerate(zip(inp[::2], inp[1::2] + "0")):
        disk += [str(i)] * int(b)
        disk += ["."] * int(s)
    return disk


def sort_disk(disk):
    s = 0
    e = len(disk) - 1

    while True:
        if s >= e:
            break

        if not disk[s] == ".":
            s += 1
            continue

        if disk[e] == ".":
            e -= 1
            continue

        disk[s] = disk[e]
        disk[e] = "."


def get_free_memory(disk):
    mem = DefaultDict(int)
    index = 0
    free = 0
    for i, c in enumerate(disk):
        if c == ".":
            if free == 0:
                index = i
            free += 1
            continue
        if free > 0:
            mem[index] = free
        free = 0
    return mem


def get_file_sizes(disk):
    files = list(filter(lambda x: x != ".", disk))
    sizes = [0] * (int(files[-1]) + 1)
    for f in files:
        sizes[int(f)] += 1
    return sizes


def sort_disk_nofrag(disk):
    free_mem = get_free_memory(disk)
    file_sizes = get_file_sizes(disk)

    p = len(disk) - 1

    while True:
        if p < 0:
            break

        c = disk[p]

        if c == ".":
            p -= 1
            continue

        size = file_sizes[int(c)]

        # Get a free memory section
        sections = [i for i, v in free_mem.items() if v >= size and i < p]
        if not sections:  # No free memory sections
            p -= 1
            continue
        mem_p = min(sections)

        # Update to reflect the available memory
        free_mem[mem_p + size] = free_mem[mem_p] - size
        del free_mem[mem_p]

        # Move the data
        disk[mem_p : mem_p + size] = [c] * size
        disk[p - size + 1 : p + 1] = ["."] * size

        p -= size


def compute_checksum(disk):
    return sum(i * int(b) if not b == "." else 0 for i, b in enumerate(disk))


def part1():
    disk = parse_input()
    sort_disk(disk)
    return compute_checksum(disk)


def part2():
    disk = parse_input()
    sort_disk_nofrag(disk)
    return compute_checksum(disk)


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
