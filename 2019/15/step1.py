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
    return prog


def to_xy(visited):
    pos = 0j
    for v in visited:
        if v == 1:
            pos += 1
        if v == 2:
            pos -= 1
        if v == 3:
            pos += 1j
        if v == 4:
            pos -= 1j
    return pos


def visit(reach, visited, din):
    # print(reach)
    pos = to_xy(visited)
    l = len(visited)
    if pos in reach and l >= reach[pos]:
        return None
    reach[pos] = l
    # print(visited)
    ret = exec(din)
    if ret:
        print("Error")
        return None

    if din["outp"][0] == 2:
        print(pos)
        return visited
    if din["outp"][0] == 0:
        return None
    if din["outp"][0] != 1:
        print("Error")
        return None

    ret = None
    for i in range(1, 5):
        d = copy.deepcopy(din)
        d["outp"] = []
        d["inp"] = [i]
        r = visit(reach, visited+[i], d)
        if r != None:
            if ret == None:
                ret = r
            if len(r) < len(ret):
                ret = r
    return ret


d = dict()
line = sys.stdin.readline()

d["p"] = parse_prog(line)
d["pc"] = 0
d["rel"] = 0
d["inp"] = []
d["outp"] = [1]

reach = dict()
v = visit(reach, [], d)
print(len(v))
