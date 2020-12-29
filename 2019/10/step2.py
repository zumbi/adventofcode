import sys
import cmath
import functools

ast = list()
lines = sys.stdin.readlines()
for i in range(len(lines)):
    for k in range(len(lines[i])):
        if lines[i][k] == "#":
            a = complex(i, k)
            ast.append(a)

max_ast = 0
for i in range(len(ast)):
    direct = set()
    for j in range(len(ast)):
        if i == j:
            continue
        diff = ast[i]-ast[j]
        direct.add(cmath.phase(diff))
    if len(direct) > max_ast:
        max_ast = len(direct)
        zero = ast[i]


killlist = list()
for a in ast:
    if a == zero:
        continue
    a = a - zero
    [dist, angle] = cmath.polar(a)
    killlist.append([angle, dist])


def aux(x):
    x += cmath.pi
    x %= 2*cmath.pi
    return x


def to_zero(x):
    x = aux(cmath.phase(-1)) - aux(x)
    return x % (2*cmath.pi)


def compare_list(x, y):
    a = to_zero(x[0])
    b = to_zero(y[0])

    if a == b:
        return x[1] - y[1]
    return a - b


killlist = sorted(killlist, key=functools.cmp_to_key(compare_list))

done = False
while not done:
    done = True
    for i in range(len(killlist)-1):
        if killlist[i][0] == killlist[i+1][0] and killlist[i][0] != killlist[-1][0]:
            done = False
            a = killlist.pop(i+1)
            killlist.append(a)
            break


def restore_ast(diff, zero):
    ast = cmath.rect(diff[1], diff[0])
    ast += zero
    ast = complex(round(ast.real), round(ast.imag))
    return ast


r = restore_ast(killlist[199], zero)
print(int(r.imag * 100 + r.real))
