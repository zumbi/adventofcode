import sys
from itertools import permutations


def execute_prog(p, pc, inp, outp):

    while True:
        opcode = p[pc]
        op = opcode % 100
        mode1 = (opcode // 100) % 2
        mode2 = (opcode // 1000) % 2
        mode3 = (opcode // 10000) % 2

        if opcode == 99:
            return [pc, True]

        if op in [1, 2, 4, 5, 6, 7, 8]:
            if mode1 == 1:
                arg1 = p[pc+1]
            else:
                arg1 = p[p[pc+1]]
        if op in [1, 2, 5, 6, 7, 8]:
            if mode2 == 1:
                arg2 = p[pc+2]
            else:
                arg2 = p[p[pc+2]]

        if op == 1:
            p[p[pc+3]] = arg1 + arg2
            pc += 4
        elif op == 2:
            p[p[pc+3]] = arg1 * arg2
            pc += 4
        elif op == 3:
            if len(inp) < 1:
                return [pc, False]
            p[p[pc+1]] = inp[0]
            inp.pop(0)
            pc += 2
        elif op == 4:
            outp.append(arg1)
            pc += 2
        elif op == 5:
            if arg1 != 0:
                pc = arg2
            else:
                pc += 3
        elif op == 6:
            if arg1 == 0:
                pc = arg2
            else:
                pc += 3
        elif op == 7:
            if arg1 < arg2:
                p[p[pc+3]] = 1
            else:
                p[p[pc+3]] = 0
            pc += 4
        elif op == 8:
            if arg1 == arg2:
                p[p[pc+3]] = 1
            else:
                p[p[pc+3]] = 0
            pc += 4
        else:
            raise NameError(int(pc))


def execute_thruster(prog, config):
    N = len(config)
    progs = list()
    ins = list()
    pcs = list()
    for i in range(N):
        ins.append([config[i]])
        progs.append(prog[:])
        pcs.append(0)
    ins[0].append(0)

    end = False
    while not end:
        for i in range(N):
            [pcs[i], end] = execute_prog(
                progs[i], pcs[i], ins[i], ins[(i+1) % N])
    return ins[0][0]


line = sys.stdin.readline()
prog = list(map(int, line.split(",")))

mval = 0
perm = permutations(range(5, 10))
for p in perm:
    m = execute_thruster(prog, p)
    # print(m)
    if m > mval:
        mval = m
print(mval)
