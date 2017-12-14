import sys

def visit(nod,n,v):
    v += [nod]
    for a in n[nod]:
        if not a in v:
            visit(a,n,v)

    return v

def visit_nr(nod,n):
    nv = [nod]
    v = list()

    while (len(nv) > 0):
        nod = nv.pop(0)
        if nod in v:
            continue
        v += [nod]
        for a in n[nod]:
            if not a in v:
                nv += [a]

    return v

#Create node
t = set()
n = dict()
for a in sys.stdin.readlines():
    a = a[:-1].split(" <-> ")
    n[a[0]] = a[1].split(", ")
    t.add(a[0])

tot = t.copy()
res = 0
while (len(tot) > 0):
    res +=1
    v = visit(tot.pop(),n,list())
    tot -= set(v)
print(res)

tot = t.copy()
res = 0
while (len(tot) > 0):
    res +=1
    v = visit_nr(tot.pop(),n)
    tot -= set(v)
print(res)
