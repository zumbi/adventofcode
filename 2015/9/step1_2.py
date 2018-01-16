import sys
import itertools

dist = dict()
cities = []

def h(a,b):
    return a+b

for l in sys.stdin.readlines():
    l = l.split()
    dist[h(l[0],l[2])]= int(l[-1])
    dist[h(l[2],l[0])]= int(l[-1])
    cities += [l[0], l[2]]

perm = list(itertools.permutations(list(set(cities))))

mini = 0xffffffff
maxi = 0
for p in perm:
    d = 0
    valid = True
    for i in range(len(p)-1):
        if not h(p[i],p[i+1]) in dist:
            valid = False
            break
        d += dist[h(p[i],p[i+1])]
    if not valid:
        continue
    if d<mini:
        mini = d
    if d>maxi:
        maxi = d

print "Step 1"
print mini

print "Step 2"
print maxi
