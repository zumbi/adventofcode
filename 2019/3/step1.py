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
    visited = set()
    p = 0j
    for w in wire:
        D = w[0]
        n = int(w[1:])
        d = text2complex(D)
        while n:
            p += d
            n -= 1
            visited.add(p)
    return visited


visited = set()
p = 0j

wire0 = sys.stdin.readline()
wire0 = wire0.split(",")
w0 = wire2set(wire0)

wire1 = sys.stdin.readline()
wire1 = wire1.split(",")
w1 = wire2set(wire1)

shorts = w0 & w1
dist = 10000000
for s in shorts:
    d = abs(s.imag) + abs(s.real)
    if d < dist:
        dist = d

print(int(dist))
