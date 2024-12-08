from aoc import get_puzzle

def is_valid1(target, value, numbers):
    if not numbers:
        return target == value

    value1 = value + numbers[0]
    value2 = value * numbers[0]
    return is_valid1(target, value1, numbers[1:]) or is_valid1(
        target, value2, numbers[1:]
    )


def is_valid2(target, value, numbers):
    if not numbers:
        return target == value

    value1 = value + numbers[0]
    value2 = value * numbers[0]
    value3 = int(str(value) + str(numbers[0]))
    return (
        is_valid2(target, value1, numbers[1:])
        or is_valid2(target, value2, numbers[1:])
        or is_valid2(target, value3, numbers[1:])
    )


def solve(data: list[str]) -> tuple[int, int]:
    part1 = 0
    part2 = 0

    for line in data:
        line = line.split(":")
        target = int(line[0])
        numbers = [int(i.strip()) for i in line[1].split()]

        value = numbers[0]

        if is_valid1(target, value, numbers[1:]):
            part1 += target
        if is_valid2(target, value, numbers[1:]):
            part2 += target

    return part1, part2


def main():
    data = get_puzzle(7).splitlines()

    res = solve(data)
    print(f"Part1: {res[0]}")
    print(f"Part2: {res[1]}")


main()
