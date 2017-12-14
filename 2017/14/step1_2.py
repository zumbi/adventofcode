
def khash(inp):
    inp = list(inp)
    inp = map(ord, inp)
    inp += [17, 31, 73, 47, 23]
    l = range(256)
    ll = 256
    skip = 0
    pos = 0
    for a in range(64):
     for i in inp:
        l2 = l[:]
        for j in range(i):
            p1 = (pos + j) % ll
            p2 = (pos + ll + i - 1 - j) % ll
            l2[p2] = l[p1]
        l = l2
        pos = (pos + i + skip) % ll
        skip += 1

    h = list()

    for i in range(16):
        x = 0
        for j in range(16):
            x ^= l[i*16 +j]
        h += [x]
    return h

def khash128(inp):
    a = list()
    for i in range(128):
        h = khash(inp+"-"+str(i))
        o = ""
        for i in h:
            o+=format(i, '08b')

        o = list(o)
        o = map(int, o)
        a.append(o)

    return a

def color(h,val, i, j):
    if i < 0:
        return False
    if j < 0:
        return False
    if i == 128:
        return False
    if j == 128:
        return False
    if h[i][j] != 1:
        return False
    h[i][j] = val
    color(h, val, i+1, j)
    color(h, val, i, j+1)
    color(h, val, i-1, j)
    color(h, val, i, j-1)
    return True

def n_1(h):
    n = 0
    for i in range(128):
        for j in range(128):
            n += h[i][j]
    return n

def n_e(h):
    n_e = 0
    for i in range(128):
        for j in range(128):
            if color(h, n_e+2, i, j):
                n_e += 1
    return n_e



#i = "flqrgnkx"
i = "hxtvlmkl"
h = khash128(i)
n = n_1(h)
print(n)
n = n_e(h)
for i in range(8):
    print h[i][0:8]
print(n)

