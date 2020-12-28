import sys


def execute_prog(p, inp, outp):
    pc = 0

    while True:
        opcode = p[pc]
        op = opcode % 100
        mode1 = (opcode // 100) % 2
        mode2 = (opcode // 1000) % 2
        mode3 = (opcode // 10000) % 2
        # print(pc,p[pc:pc+4],mode1,mode2,mode3)
        # print(pc,p)

        if opcode == 99:
            return

        if op == 1 or op == 2 or op == 4:
            if mode1 == 1:
                arg1 = p[pc+1]
            else:
                arg1 = p[p[pc+1]]
        if op == 1 or op == 2:
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


for line in sys.stdin.readlines():
    line = list(map(int, line.split(",")))
    out = list()
    execute_prog(line, [1], out)
    print(out[-1])
