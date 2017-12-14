import sys

nodes = dict()

def validate(l):
    if len(l) < 2:
        return
    for i in range(len(l)):
        pre = l[i - 1]
        nex = l[(i+1) % len(l)]
        if l[i] != pre and l[i] != nex:
            print(l[i],pre)
            return i
    return -1



def val(elem):
    v = 0
    n = nodes[elem]
    if len(n["sons"]) == 0:
        return n["val"]

    l = list()
    for a in n["sons"]:
        l.append(val(a))
        v += val(a)

    i = validate(l)
    if (i>0):
        print(nodes[n["sons"][i]])

    v += n["val"]
    return v


for l in sys.stdin.readlines():
    l = l[:-1]
    l = l.split(" ")
    n = dict()
    n["val"] = int(l[1][1:-1])

    s = list()
    for i in range(3, len(l)):
        v = l[i]
        if i != len(l)-1:
            v=v[:-1]
        s.append(v)

    n["sons"] = s
    nodes[l[0]] = n

copy = nodes.copy()
for i in nodes:
    n=nodes[i]
    for s in n["sons"]:
            del copy[s]

for i in copy:
    dad = i
print(dad)

val(dad)
