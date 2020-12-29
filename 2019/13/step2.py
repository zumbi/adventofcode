import sys
from collections import defaultdict


def get_arg(mode, arg, p, rel):
    if mode == 0:
        return p[arg]
    elif mode == 1:
        return arg
    elif mode == 2:
        return p[arg+rel]
    else:
        raise NameError(int(mode))


def get_dest(mode, arg, p, rel):
    # print(mode)
    if mode == 0:
        return arg
    elif mode == 2:
        return arg+rel
    else:
        raise NameError(int(mode))


def execute_prog(p, pc, rel, inp, outp):

    while True:
        # print(pc,rel,p[pc],p[pc+1],p[pc+2],p[pc+3])
        # print(outp)
        opcode = p[pc]
        op = opcode % 100
        mode1 = (opcode // 100) % 10
        mode2 = (opcode // 1000) % 10
        mode3 = (opcode // 10000) % 10

        if opcode == 99:
            return [pc, rel, True]

        if op == 1:
            # print("sum")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            dest = get_dest(mode3, p[pc+3], p, rel)
            p[dest] = arg1 + arg2
            pc += 4
        elif op == 2:
            # print("mul")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            dest = get_dest(mode3, p[pc+3], p, rel)
            p[dest] = arg1 * arg2
            pc += 4
        elif op == 3:
            # print("in")
            if len(inp) < 1:
                return [pc, rel, False]
            dest = get_dest(mode1, p[pc+1], p, rel)
            p[dest] = inp[0]
            inp.pop(0)
            pc += 2
        elif op == 4:
            # print("out")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            outp.append(arg1)
            pc += 2
        elif op == 5:
            #print("jnz", arg1)
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            if arg1 != 0:
                pc = arg2
            else:
                pc += 3
        elif op == 6:
            #print("jz", arg1)
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            if arg1 == 0:
                pc = arg2
            else:
                pc += 3
        elif op == 7:
            #print("cmp less")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            dest = get_dest(mode3, p[pc+3], p, rel)
            if arg1 < arg2:
                p[dest] = 1
            else:
                p[dest] = 0
            pc += 4
        elif op == 8:
            #print("cmp eq")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            arg2 = get_arg(mode2, p[pc+2], p, rel)
            dest = get_dest(mode3, p[pc+3], p, rel)
            if arg1 == arg2:
                p[dest] = 1
            else:
                p[dest] = 0
            pc += 4
        elif op == 9:
            #print("rel +")
            arg1 = get_arg(mode1, p[pc+1], p, rel)
            rel += arg1
            pc += 2
        else:
            raise NameError(int(op))
        # print()


def def_value():
    return 0


def n_block(game):
    n = 0
    for g in game:
        n += g.count(1)
    return n


def run(prog_in):
    prog = defaultdict(def_value)
    for i in range(len(prog_in)):
        prog[i] = prog_in[i]

    pc = 0
    rel = 0

    game = list()
    line = [0] * (43)
    for i in range(23):
        game.append(line[:])

    n_b = 1
    inp = []
    ret = False
    while n_b > 0 and not ret:
        out = []
        [pc, rel, ret] = execute_prog(prog, pc, rel, inp, out)

        p_b = 0
        p_p = 0
        score = -1
        for i in range(0, len(out), 3):
            col, line, val = out[i], out[i+1], out[i+2]
            if col == -1:
                score = val
            elif val == 0:
                game[line][col] = 0
            elif val == 2:
                game[line][col] = 1

            elif val == 4:
                p_b = col

            elif val == 3:
                p_p = col
        if p_p < p_b:
            inp.append(1)
        elif p_p > p_b:
            inp.append(-1)
        elif p_p == p_b:
            inp.append(0)
        n_b = n_block(game)
        # print(ret,n_b,score)

    return score


line = sys.stdin.readline()
prog = list(map(int, line.split(",")))
prog[0] = 2
print(run(prog))
