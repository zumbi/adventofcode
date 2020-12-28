import sys

lines = 6
cols = 25
l = sys.stdin.readline()
l = l.strip()
l = list(map(int, list(l)))

layers = list()
for i in range(0, len(l), lines*cols):
    layers.append(l[i:i+lines*cols])
layers.reverse()

top_layer = list()

print("P2", cols, lines, 2)
for i in range(lines * cols):
    v = 0
    for l in layers:
        if l[i] != 2:
            v = l[i]
    print(v)
