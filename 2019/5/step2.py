import sys


def execute_prog(p, inp, outp):
    pc = 0

    while True:
        opcode = p[pc]
        op = opcode % 100
        mode1 = (opcode // 100) % 2
        mode2 = (opcode // 1000) % 2
        mode3 = (opcode // 10000) % 2
        # print(pc,p[pc:pc+4],op,mode1,mode2,mode3)
        # print(pc,p)

        if opcode == 99:
            return

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
            sys.exit(-1)


for line in sys.stdin.readlines():
    line = list(map(int, line.split(",")))
    out = list()
    execute_prog(line, [5], out)
    print(out[-1])
