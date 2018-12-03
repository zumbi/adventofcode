import sys

out = dict()

lines =  sys.stdin.readlines()

for l in lines:
    l = l.split()
    l_c = l[2][:-1].split(",")
    a_b = l[3].split("x")
    c0 = int(l_c[0])
    l0 = int(l_c[1])
    b = int(a_b[0])
    a = int(a_b[1])
    for l in range(l0,l0+a):
        for c in range(c0, c0+b):
            p = (l << 16) + c
            if p not in out:
                out[p] = 0
            out[p] += 1;

for l in lines:
    l = l.split()
    i = int(l[0][1:])
    l_c = l[2][:-1].split(",")
    a_b = l[3].split("x")
    c0 = int(l_c[0])
    l0 = int(l_c[1])
    b = int(a_b[0])
    a = int(a_b[1])

    is_ok = True
    for l in range(l0,l0+a):
        for c in range(c0, c0+b):
            p = (l << 16) + c
            if out[p] != 1:
                is_ok = False
                break
    if is_ok:
        print(i)
        break
