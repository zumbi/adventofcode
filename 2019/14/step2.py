import sys
import math
import copy

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


def to_ore(start, leftover):
    #print(start, leftover)
    while(len(start) > 1 or "ORE" not in start):
        for s in start:
            # print(start,leftover)
            if s == "ORE":
                continue
            if s in leftover:
                if leftover[s] >= start[s]:
                    leftover[s] -= start[s]
                    del start[s]
                    if leftover[s] == 0:
                        del leftover[s]
                    break
                else:
                    start[s] -= leftover[s]
                    del leftover[s]
            n = (start[s] + recipes[s][0] - 1) // recipes[s][0]
            l = (-1 * (start[s] % recipes[s][0])) % recipes[s][0]
            if l > 0:
                leftover[s] = l

            del start[s]
            for i in recipes[s][1]:
                if i not in start:
                    start[i] = 0
                start[i] += n * recipes[s][1][i]
            break

    return start["ORE"], leftover


n_ore = 0
leftover = dict()
i = 0
while n_ore < 1000000000000:
    n, leftover = to_ore(copy.deepcopy(recipes["FUEL"][1]), leftover)
    n_ore += n
    i += 1
    if (i % 10000) == 0:
        print(i, float(n_ore)/1000000000000)


print(i-1)

# 4935420 too low
# 19604563
