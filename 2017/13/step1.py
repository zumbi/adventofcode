import sys

res = 0
for l in sys.stdin.readlines():
    l = l.split(": ")
    ran = int(l[0])
    dep = int(l[1])
    if ran == 0:
        continue

    if dep == 1:
        res += ran * dep

    dep2 = (dep - 1) * 2
    if (ran % dep2) == 0:
        res += ran * dep


print (res)
