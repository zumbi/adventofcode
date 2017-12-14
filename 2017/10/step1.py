import sys

l = range(int(sys.argv[1]))
ll = len(l)

inp = sys.stdin.readline().split(",")
inp = map(int, inp)

skip = 0
pos = 0
for i in inp:
    l2 = l[:]
    for j in range(i):
        p1 = (pos + j) % ll
        p2 = (pos + ll + i - 1 - j) % ll
        l2[p2] = l[p1]
    l = l2
    print l
    pos = (pos + i + skip) % ll
    skip += 1

#print l[pos] * l[(pos+1) % ll]
print l[0] * l[1]

