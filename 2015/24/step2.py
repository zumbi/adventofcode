import sys
import itertools

p = map(int,sys.stdin.readlines())

weight = sum(p) /4



print p
print len(p)
print weight

min_ew = None
for i in range(len(p)/4):
    com = list(itertools.combinations(p,i))

    Found = False
    for c in com:
        if sum(c) != weight:
            continue
        ew = 1
        for k in c:
            ew *=k
        if not min_ew or ew<min_ew:
            min_ew = ew
            print min_ew
        Found = True
        print c
    if Found:
        break

print min_ew
