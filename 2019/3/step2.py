import sys


def text2complex(D):
    if D == 'U':
        return 1j
    elif D == 'D':
        return -1j
    elif D == 'L':
        return -1 + 0j
    elif D == 'R':
        return 1 + 0j


def wire2set(wire):
    distance = dict()
    visited = set()
    p = 0j
    d0 = 0
    for w in wire:
        D = w[0]
        n = int(w[1:])
        d = text2complex(D)
        while n:
            p += d
            n -= 1
            d0 += 1
            if p not in distance:
                distance[p] = d0
            visited.add(p)
    return [distance, visited]


visited = set()
p = 0j

wire0 = sys.stdin.readline()
wire0 = wire0.split(",")
[d0, w0] = wire2set(wire0)

wire1 = sys.stdin.readline()
wire1 = wire1.split(",")
[d1, w1] = wire2set(wire1)

shorts = w0 & w1
dist = 1000000000
for s in shorts:
    d = d0[s]
    d += d1[s]
    if d < dist:
        dist = d
print(dist)
