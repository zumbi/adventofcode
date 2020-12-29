import sys
import cmath

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
        #angle = diff.real / diff.imag
        direct.add(cmath.phase(diff))
    if len(direct) > max_ast:
        max_ast = len(direct)

print(max_ast)
