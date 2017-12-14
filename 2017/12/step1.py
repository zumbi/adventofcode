import sys

def visit(nod,n,v):
    r = 1
    v += [nod]
    for a in n[nod]:
        if not a in v:
            r += visit(a,n,v)

    return r

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

    return len(v)

n = dict()
for a in sys.stdin.readlines():
    a = a[:-1].split(" <-> ")
    n[a[0]] = a[1].split(", ")


print(visit("0",n,list()))
print(visit_nr("0",n))
