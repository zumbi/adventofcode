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


def ch2dir(ch):
    if ch == "^":
        return -1 + 0j
    if ch == "v":
        return 1 + 0j
    if ch == ">":
        return 0 + 1j
    if ch == "<":
        return 0 - 1j


def find_robot(di):
    for d in di:
        if di[d] != "#":
            p = d
            dir = ch2dir(di[d])
            di[d] = 1
        else:
            di[d] = 0

    return p, dir


def not_visited(di):
    s = 0
    for d in di:
        if di[d] == 0:
            s += 1
    return s


def visit(di, path, pos, dir):
    # print(not_visited(di),path)
    if not_visited(di) == 0:
        return path
    ret = None
    for i in ["L", "R", "1"]:

        if i in ["L", "R"]:
            avoid = True
            for k in [-1, 1, -1j, 1j]:
                if (pos + k) not in di:
                    avoid = False
                    break
            if avoid:
                continue

            if path[-1] in ["L", "R"]:
                continue
            if i == "L":
                dir1 = dir * 1j
            else:
                dir1 = dir * -1j
            pos1 = pos
            path1 = path[:] + [i]
            di1 = copy.deepcopy(di)
        else:
            pos1 = pos + dir
            if pos1 not in di:
                continue
            if di[pos1] > 2:
                continue
            dir1 = dir
            di1 = copy.deepcopy(di)
            di1[pos1] += 1
            path1 = path[:]
            if not isinstance(path[-1], int):
                path1 += [0]
            path1[-1] += 1
        r = visit(di1, path1, pos1, dir1)
        if r == None:
            continue
        if ret == None:
            ret = r
        if len(r) < len(ret):
            ret = r

    return ret


def _visit(di, pos, dir):
    r = visit(di, [0], pos, dir)
    if r != None and r[0] == 0:
        r = r[1:]
    return r


def n_substrings(trip, s):
    trip0 = ""
    for t in trip:
        trip0 += str(t)
    s0 = ""
    for t in s:
        s0 += str(t)

    return trip0.count(s0)


def findC(txt):
    s = None
    for i in range(len(txt)):
        if s == None:
            if txt[i] in ["A", "B", ","]:
                continue
            s = i
            continue
        if txt[i] in ["A", "B"]:
            out = txt[s:i]
            l = len(out)
            if l > 21:
                out = out[0:l//2]
            return out


def testABC(abc, txt):
    # print(abc)
    for i in [0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]:
        t1 = txt[:]
        t1 = t1.replace(abc[i[0]], "A,")
        t1 = t1.replace(abc[i[1]], "B,")
        t1 = t1.replace(abc[i[2]], "C,")
        found = True
        for t in t1:
            if t not in ["A", "B", "C", ","]:
                found = False
        if found:
            return t1
    return None


def find_part(txt):
    for i in range(1, 22):
        if txt[i] != ",":
            continue
        a = txt[:i+1]
        for j in range(-22, 0):
            if txt[j-1] != ",":
                continue
            b = txt[j:]

            t1 = txt[:]
            t1 = t1.replace(a, "A,")
            t1 = t1.replace(b, "B,")
            c = findC(t1)
            t = testABC([a, b, c], txt)
            if t != None:
                return(t, [a, b, c])


line = sys.stdin.readline()

din = parse_prog(line)
d = copy.deepcopy(din)
ret = exec(d)
if not ret:
    print("error")
    sys.exit(0)

txt = outp2txt(d["outp"])
mapa = txt2map(txt)
di = map2dict(mapa)


p, dir = find_robot(di)


trip = _visit(di, p, dir)
txt_trip = ",".join(list(map(str, trip)))
txt_trip += ","


print(txt_trip)
[main, [a, b, c]] = find_part(txt_trip)

out = str(main[:-1]) + "\n"
out += str(a[:-1]) + "\n"
out += str(b[:-1]) + "\n"
out += str(c[:-1]) + "\n"
out += "n\n"


out = list(map(ord, list(out)))


d = copy.deepcopy(din)
d["p"][0] = 2
d["inp"] = out
ret = exec(d)
if not ret:
    print("error")
    sys.exit(0)


txt = outp2txt(d["outp"][:-1])
# print(txt)
print(d["outp"][-1])
