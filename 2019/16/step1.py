import sys


def get_pattern(n):
    out = list()
    pbase = [0, 1, 0, -1]
    for p in pbase:
        for _ in range(n):
            out.append(p)
    k = out.pop(0)
    out.append(k)
    return out


def to_one(i):
    return abs(i) % 10


def mulp(l, p):
    # print("mulp",l,p)
    out = 0
    N = len(p)
    for i in range(len(l)):
        out += l[i] * p[i % N]

    return to_one(out)


def conv(l):
    out = list()
    for i in range(len(l)):
        p = get_pattern(i+1)
        out.append(mulp(l, p))
    return out


l = sys.stdin.readline().strip()
l = list(map(int, list(l)))
for i in range(100):
    l = conv(l)
    # print(l)


f8 = l[:8]
f8 = list(map(str, f8))

print("".join(f8))
