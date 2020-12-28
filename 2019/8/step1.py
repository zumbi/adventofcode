import sys

lines = 6
cols = 25
l = sys.stdin.readline()
l = l.strip()
l = list(map(int, list(l)))

layers = list()
for i in range(0, len(l), lines*cols):
    layers.append(l[i:i+lines*cols])

min_n0 = lines * cols
for l in layers:
    n0 = l.count(0)
    if (n0 < min_n0):
        min_n0 = n0
        mul_1_2 = l.count(2) * l.count(1)
print(mul_1_2)
