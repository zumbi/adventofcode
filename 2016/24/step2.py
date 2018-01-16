import sys
import copy

def is_visited(v,tra):
    return v in tra

m = []

for l in sys.stdin.readlines():
    m += [list(l[:-1])]

travel = []
total_v = 0
for i in range(len(m)):
    t0 = []
    for j in range(len(m[i])):
        t0 += [list()]
        if m[i][j].isdigit():
            total_v+=1
        if m[i][j] == '0':
            p = [i,j]
    travel += [t0]

v = []
steps = 0
s = [p,v,steps]
todo = [s]

while len(todo) > 0:
    s = todo[0]
    todo = todo[1:]
    [p,v,steps] = s

    if is_visited(v,travel[p[0]][p[1]]):
        continue
    travel[p[0]][p[1]] += [v[:]]

    if len(v) == total_v and  m[p[0]][p[1]] == "0":
        print steps
        break

    if m[p[0]][p[1]].isdigit() and not int(m[p[0]][p[1]]) in v:
        v += [int(m[p[0]][p[1]])]
        v = sorted(v)
        print v

    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    for a in pos:
        p0=[0,0]
        for i in range(2):
            p0[i] = a[i] + p[i]
        if p0[0] >= len(m) or p0[0]<0:
            continue
        if p0[1] >= len(m[0]) or p0[1]<0:
            continue
        content =  m[p0[0]][p0[1]]
        if content == '#':
            continue

        if is_visited(v,travel[p0[0]][p0[1]]):
            continue

        s0 = [p0,v[:],steps+1]
        todo += [s0]

