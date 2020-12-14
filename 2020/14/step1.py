import sys
import re

mem = dict()

ormask = 0
andmask = 0

for line in sys.stdin.readlines():
    if line[0:4] == "mask":
        line = line.split(" = ")
        mask = line[1]
        ormask = int(mask.replace("X", "0"), 2)
        andmask = ~int(mask.translate(str.maketrans('0X1', '100')), 2)
        continue

    m = re.match(r'mem\[([0-9]+)\] = ([0-9]+)', line)
    pos = int(m.group(1))
    val = (int(m.group(2)) & andmask) | ormask
    mem[pos] = val

sum = 0
for k in mem:
    sum += mem[k]
print(sum)
