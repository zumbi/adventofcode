import sys
from collections import defaultdict
import copy


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


def exec(d):
    d["pc"], d["rel"], ret = execute_prog(
        d["p"], d["pc"], d["rel"], d["inp"], d["outp"])
    return ret


def def_value():
    return 0


def parse_prog(line):
    prog_in = list(map(int, line.split(",")))
    prog = defaultdict(def_value)
    for i in range(len(prog_in)):
        prog[i] = prog_in[i]
    d = dict()
    d["p"] = prog
    d["pc"] = 0
    d["rel"] = 0
    d["inp"] = []
    d["outp"] = []
    return d


def outp2txt(map):
    out = ""
    for p in map:
        out += chr(p)
    return out


def txt2map(txt):
    txt = txt.split("\n")
    txt = list(map(list, txt))
    return txt


def map2dict(map):
    d = dict()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != ".":
                pos = (j * 1j) + i
                d[pos] = map[i][j]
    return d


d = dict()
line = sys.stdin.readline()

d = parse_prog(line)
ret = exec(d)
if not ret:
    print("error")
    sys.exit(0)

txt = outp2txt(d["outp"])
mapa = txt2map(txt)
di = map2dict(mapa)
# print(di)

s = 0
for d in di:
    n = 0
    for k in [1, -1, -1j, +1j]:
        if d+k in di and di[d+k] == "#":
            n += 1
    if n == 4:
        s += int(d.real * d.imag)
print(s)
