import sys

L = 1000 * 1000

cups = list(map(int, list(sys.stdin.readline().strip())))
for i in range(len(cups) + 1, L + 1):
    cups.append(i)

next = dict()
for i in range(len(cups)):
    next[cups[i]] = cups[(i + 1) % L]


start = cups[0]
for i in range(10*1000*1000):
    a = next[start]
    b = next[a]
    c = next[b]
    next[start] = next[c]

    pos = start
    while pos in [start, a, b, c]:
        pos = ((pos - 2) % L) + 1

    next[c] = next[pos]
    next[pos] = a
    start = next[start]

print(next[1]*next[next[1]])
