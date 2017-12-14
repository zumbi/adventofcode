import sys

line = sys.stdin.read()
line = line[:-1]

s = 0
l = len(line)
l2 = l /2

for a in range(l):
    if line[a] == line [(a+l2)%l]:
        s += int(line[a])

print line[-1]
print s
