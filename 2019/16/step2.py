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
        a = mulp(l, p)
        # print(float(i)/len(l),i,a)
        out.append(a)
    return out


def fast_conv(l):
    out = list()
    s = 0
    for v in l:
        s += v
    #s = to_one(s)
    out.append(s)
    for i in range(len(l)-1):
        s -= l[i]
        #s = to_one(s)
        out.append(s)
    out = list(map(to_one, out))
    return out


def getn(l, idx, size):
    n = l[idx:idx+size]
    n = list(map(str, n))
    n = "0"+"".join(n)
    n = int(n)
    return n


l = sys.stdin.readline().strip()
l = list(map(int, list(l)))
l = l * 10000
idx = getn(l, 0, 7)
# print(idx)
l = l[idx:]
for i in range(100):
    l = fast_conv(l)
    # print(i,getn(l,0,8))

n = getn(l, 0, 8)
print(n)
