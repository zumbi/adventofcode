import sys

l = range(256)
ll = 256

inp = sys.stdin.readline()
inp = inp[:-1]
inp = list(inp)
#inp[:] = (value for value in inp if value != " ")
inp = map(ord, inp)
inp += [17, 31, 73, 47, 23]

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

print(h)
o = ""
for i in h:
    o+=format(i, '02x')
print(o)


