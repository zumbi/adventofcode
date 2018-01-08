import sys

node = dict()

def h(x,y):
    return (x << 8) + y

for l in sys.stdin.readlines()[2:]:
    l = l.split()
    used = int(l[2][:-1])
    size = int(l[1][:-1])
    name = l[0].split("-")
    x = int(name[1][1:])
    y = int(name[2][1:])
    node[h(x,y)] = [used,size]

viable = 0
for i in node:
    for j in node:
        if j == i:
            continue
        n1 = node[i]
        n2 = node[j]
        if n1 is n2:
            continue
        if n1[0] == 0:
            continue
        if n1[0] + n2[0] <= n2[1]:
            viable += 1

print viable

