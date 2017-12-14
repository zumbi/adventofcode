import sys

def calc(l):
    n = 0
    e = 0
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
    r = 0
    print(n,e)
    n = abs(n)
    e = abs(e)

    m = min(n,e)
    r += m

    n-=m
    e-=m
    print(n,e)

    r += n//2
    r += e
    print r
    return r

for a in sys.stdin.readlines():
    a = a[:-1].split(",")
    calc(a)

