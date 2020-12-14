import sys
import re

mem = dict()

ormask = 0
xmask = 0

for line in sys.stdin.readlines():
    if line[0:4] == "mask":
        line = line.split(" = ")
        mask = line[1]
        ormask = int(mask.replace("X", "0"), 2)
        xmask = mask.replace("1", "0")
        continue

    m = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)
    val = int(m.group(2))
    pos = int(m.group(1)) | ormask

    xs = [(35 - i.start()) for i in re.finditer('X', xmask)]
    if len(xs) == 0:
        mem[pos] = val
        continue
    xs.reverse()

    for i in range(1 << len(xs)):
        posX = pos
        for j in range(len(xs)):
            if i & (1 << j):
                posX |= (1 << xs[j])
            else:
                posX &= ~(1 << xs[j])
        mem[posX] = val
        # print(posX,val)

    continue

sum = 0
for k in mem:
    sum += mem[k]
print(sum)
