import sys

N = int(sys.argv[1])

l = list()
for i in range(N):
    l += chr(i + ord('a'))

O = sys.stdin.readline()
O = O[:-1].split(",")

for o in O:
    if o[0] == 's':
        l2 = list()
        n = int(o[1:])
        for i in range(N):
            a = (N - n + i) % N
            l2 += l[a]
        l = l2
        continue
    if o[0] == 'x':
        o = o[1:].split('/')
        a = int(o[0])
        b = int(o[1])
        l[a] , l[b] = l[b], l[a]
        continue
    if o[0] == 'p':
        o = o[1:].split('/')
        a = l.index(o[0])
        b = l.index(o[1])
        l[a] , l[b] = l[b], l[a]
        continue
print ''.join(l)
