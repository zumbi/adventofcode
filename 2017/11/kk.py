import sys

def le(n,e):
    r = 0
    n = abs(n)
    e = abs(e)

    m = min(n,e)
    r += m

    n-=m
    e-=m

    r += n//2
    r += e
    return r

def calc(l):
    n = 0
    e = 0
    r = 0
    for a in l:
        if a == "n":
            n +=2
        elif a == "s":
            n -=2
        elif a == "ne":
            n +=1
            e +=1
        elif a == "nw":
            n +=1
            e -=1
        elif a == "se":
            n -=1
            e +=1
        elif a == "sw":
            n -=1
            e -=1
        r = max(le(n,e), r)
    return r

for a in sys.stdin.readlines():
    a = a[:-1].split(",")
    print calc(a)

