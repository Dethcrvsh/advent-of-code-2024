import re
from aoc import get_puzzle


class Computer:
    def __init__(self, ra, rb, rc, mem):
        self.ra = ra
        self.rb = rb
        self.rc = rc
        self.ip = 0
        self.mem = mem
        self.buf = []

    def run(self):
        while self.ip + 1 < len(self.mem):
            self.cycle()

        return ",".join(map(str, self.buf))

    def reset(self):
        self.ra = 0
        self.rb = 0
        self.rc = 0
        self.ip = 0
        self.buf = []

    def cycle(self):
        instr = self.mem[self.ip]
        op = self.mem[self.ip + 1]

        match instr:
            case 0:
                self.adv(op)
            case 1:
                self.bxl(op)
            case 2:
                self.bst(op)
            case 3:
                self.jnz(op)
            case 4:
                self.bxc(op)
            case 5:
                self.out(op)
            case 6:
                self.bdv(op)
            case 7:
                self.cdv(op)

    def combo(self, op):
        if 0 <= op <= 3:
            return op
        if op == 4:
            return self.ra
        if op == 5:
            return self.rb
        if op == 6:
            return self.rc
        else:
            raise ValueError("oopsie")

    # OP codes
    def adv(self, op):
        self.ra = int(self.ra / (2 ** self.combo(op)))
        self.ip += 2

    def bxl(self, op):
        self.rb ^= op
        self.ip += 2

    def bst(self, op):
        self.rb = self.combo(op) % 8
        self.ip += 2

    def jnz(self, op):
        if self.ra != 0:
            self.ip = op
        else:
            self.ip += 2

    def bxc(self, _):
        self.rb ^= self.rc
        self.ip += 2

    def out(self, op):
        self.buf.append(self.combo(op) % 8)
        self.ip += 2

    def bdv(self, op):
        self.rb = int(self.ra / (2 ** self.combo(op)))
        self.ip += 2

    def cdv(self, op):
        self.rc = int(self.ra / (2 ** self.combo(op)))
        self.ip += 2


def get_input():
    RE_STR = re.compile(r"(?:Register \S: (\d+))|Program: (.+)")
    m = RE_STR.findall(get_puzzle(17))
    seq = [int(i) for i in m[3][1].split(",")]
    return Computer(int(m[0][0]), int(m[1][0]), int(m[2][0]), seq), seq


def get_reg(pc, seq):
    if not seq:
        return [0]

    rest = get_reg(pc, seq[1:])

    vals = []
    for r in rest:
        for k in range(8):
            pc.reset()
            pc.ra = r * 8 + k
            out = int(pc.run()[0])

            if out == seq[0]:
                vals.append(r * 8 + k)
    if vals:
        return vals

    return []


def part1():
    pc, _ = get_input()
    return pc.run()


def part2():
    pc, seq = get_input()
    return min(get_reg(pc, seq))


if __name__ == "__main__":
    print("⋆꙳•̩̩͙❅*̩̩͙‧͙   Advent of Code 2024  ‧͙*̩̩͙❆ ͙͛ ˚₊⋆\n")
    print(f"  ❆ Part 1: {part1()}")
    print(f"  ❆ Part 2: {part2()}")
