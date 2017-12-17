import sys

N = int(sys.argv[1])
times = int(sys.argv[2])

l0 = range(N)
l = range(N)

O = sys.stdin.readline()
O = O[:-1].split(",")

count = 0
while count < times:
 ##found a cycle!
 if (count and l == l0):
     times = times % count
     count = 0

 count += 1
 for o in O:
    if o[0] == 's':
        l2 = list()
        n = int(o[1:])
        for i in range(N):
            a = (N - n + i) % N
            l2 += [l[a]]
        l = l2
        continue
    if o[0] == 'x':
        o = o[1:].split('/')
        a = int(o[0])
        b = int(o[1])
        l[a] , l[b] = l[b], l[a]
    if o[0] == 'p':
        o = o[1:].split('/')
        a = l.index(ord(o[0])-ord('a'))
        b = l.index(ord(o[1])-ord('a'))
        l[a] , l[b] = l[b], l[a]
        continue


X = list()
for i in range(N):
    X += chr(l[i]+ord('a'))

print ''.join(X)
