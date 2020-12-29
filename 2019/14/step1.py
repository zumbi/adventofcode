import sys
import math

recipes = dict()

for l in sys.stdin.readlines():
    l = l.strip()
    [fro, to] = l.split(" => ")
    to = to.split()
    to[0] = int(to[0])
    fro = fro.split(", ")
    for i in range(len(fro)):
        fro[i] = fro[i].split()
        fro[i][0] = int(fro[i][0])
    fr = dict()
    for f in fro:
        fr[f[1]] = f[0]

    recipes[to[1]] = [to[0], fr]

start = recipes["FUEL"][1]
leftover = dict()

while(len(start) > 1 or "ORE" not in start):
    for s in start:
        # print(start,leftover)
        if s == "ORE":
            continue
        if s in leftover:
            if leftover[s] >= start[s]:
                leftover[s] -= start[s]
                del start[s]
                break
            else:
                start[s] -= leftover[s]
                del leftover[s]
        n = (start[s] + recipes[s][0] - 1) // recipes[s][0]
        leftover[s] = (-1 * (start[s] % recipes[s][0])) % recipes[s][0]
        del start[s]
        for i in recipes[s][1]:
            if i not in start:
                start[i] = 0
            start[i] += n * recipes[s][1][i]
        break

print(start)
