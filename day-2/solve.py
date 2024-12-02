def is_safe(report: list[int]) -> bool:
    s = report[0] - report[1]
    sign = s // abs(s) if s != 0 else 0
    for l1, l2 in zip(report[:-1], report[1:]):
        r: int = l1 - l2
        r_abs: int = abs(r)

        if r_abs < 1 or 3 < r_abs:
            return False
        if (r // r_abs if r != 0 else 0) != sign:
            return False

    return True


def part1():
    reports = [list(map(lambda x: int(x), ln.strip().split())) for ln in open("input").readlines()]
    return list(map(is_safe, reports)).count(True)


def part2():
    reports = [list(map(lambda x: int(x), ln.strip().split())) for ln in open("input").readlines()]
    # brute force go brr
    reports = list(map(lambda rep: [rep[:i] + rep[i+1:] for i, _ in enumerate(rep)] + [rep], reports))
    return sum(map(lambda reps: sum(is_safe(r) for r in reps) > 0, reports))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
