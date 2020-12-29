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


def run(prog_in):
    prog = defaultdict(def_value)
    for i in range(len(prog_in)):
        prog[i] = prog_in[i]

    pc = 0
    rel = 0

    out = []
    [pc, rel, ret] = execute_prog(prog, pc, rel, [], out)

    if not ret:
        print("error")
    return out


def print_game(game):
    for g in game:
        print(g)


def get_game(prog):
    game = run(prog)

    colmax = 0
    linemax = 0

    tiles = defaultdict(def_value)
    for i in range(0, len(game), 3):
        pos = complex(game[i], game[i+1])
        val = game[i+2]
        tiles[pos] = val
        if pos.real > colmax:
            colmax = int(pos.real)
        if pos.imag > linemax:
            linemax = int(pos.real)

    game = list()
    line = [0] * (colmax + 1)
    for i in range(linemax+1):
        game.append(line[:])

    for t in tiles:
        game[int(t.imag)][int(t.real)] = tiles[t]

    return game


line = sys.stdin.readline()
prog = list(map(int, line.split(",")))

game = get_game(prog)
print_game(game)
n_2 = 0
for g in game:
    n_2 += g.count(2)
print(n_2)
