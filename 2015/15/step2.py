import sys

ing = []

for l in sys.stdin.readlines():
    l = l.split()
    ing += [[l[0], int(l[2][:-1]), int(l[4][:-1]), int(l[6][:-1]), int(l[8][:-1]),int(l[10])]]

prop = 4
ingredients = 4

def combinations(n):
    l = []
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                i0 = i
                i1 = j - i
                i2 = k - j
                i3 = 100 - k
                l +=[[i0,i1,i2,i3]]
    return l

maxi = 0
for c in combinations(100):
    cal = 0
    for i in range(ingredients):
        cal += c[i] * ing[i][-1]
    if cal != 500:
        continue

    val = 1
    for pr in range(prop):
        p = 0
        for i in range(ingredients):
            p += c[i] * ing[i][1+pr]
        val *= max(0,p)
        if val == 0:
            break
    maxi = max(val,maxi)

print maxi
