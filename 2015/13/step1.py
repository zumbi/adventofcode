import sys
import itertools

happy = dict()
people = []

def h(a,b):
    return a+b

for l in sys.stdin.readlines():
    l = l[:-2].split()
    v = int(l[3])
    if l[2] == "lose":
        v *= -1
    happy[h(l[0],l[-1])] = v
    people += [l[0], l[-1]]

people = list(set(people))

perm = list(itertools.permutations(people))

maxi = None

n = len(people)
for p in perm:
    v = 0
    for i in range(len(p)):
        v += happy[h(p[i],p[(i+1)%n])]
        v += happy[h(p[i],p[i-1])]

    if maxi==None or v > maxi:
        maxi = v

print maxi



