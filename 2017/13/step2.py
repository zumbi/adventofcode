import sys

rob = list()
res = 0
for l in sys.stdin.readlines():
    l = l.split(": ")
    ran = int(l[0])
    dep = int(l[1])
    rob += [(ran,dep)]


def crash(rob, i):
 for a in rob:
    ran = a[0]
    dep = a[1]

    if dep == 1:
        return True

    dep2 = (dep - 1) * 2
    if ((ran + i) % dep2) == 0:
        return True
 return False

print rob

i=0
while crash(rob, i):
    i+=1

print(i)
