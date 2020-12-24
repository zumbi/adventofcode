import sys


def s2complex(s):
    if s == "e":
        return +2+0j
    elif s == "se":
        return 1-1j
    elif s == "ne":
        return 1+1j
    elif s == "w":
        return -2+0j
    elif s == "sw":
        return -1-1j
    elif s == "nw":
        return -1+1j


def line2steps(l):
    steps = list()
    i = 0
    s = ""
    while i < len(l):
        s += l[i]
        if l[i] in ["e", "w"]:
            steps.append(s2complex(s))
            s = ""
        i += 1
    return steps


def n_blacks(tiles):
    n_black = 0
    for t in tiles:
        if (tiles[t] % 2) != 0:
            n_black += 1
    return n_black


def neighbours():
    return [+2+0j, 1-1j, 1+1j, -2+0j, -1-1j, -1+1j]


def black_neighbours(tiles, t0):
    n_black = 0
    for n in neighbours():
        t = t0 + n
        if t in tiles:
            n_black += 1
    return n_black


def cycle(tiles):
    new = dict()

    for t in tiles:
        nb = black_neighbours(tiles, t)
        if not(nb == 0 or nb > 2):
            new[t] = True
        for n in neighbours():
            t1 = t + n
            if t1 in tiles:
                continue
            if black_neighbours(tiles, t1) == 2:
                new[t1] = True

    return new


path = list()
for l in sys.stdin.readlines():
    path.append(line2steps(l))
# print(path)

tiles = dict()
for p in path:
    pos = 0j
    for s in p:
        pos += s
    if pos not in tiles:
        tiles[pos] = True
    else:
        del tiles[pos]

print("step1", n_blacks(tiles))

for i in range(100):
    tiles = cycle(tiles)
    # print(n_blacks(tiles))

print("step2", n_blacks(tiles))
