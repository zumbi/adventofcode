import sys

regs = dict()
mv = 0

for line in sys.stdin.readlines():
    l = line.split(" ")
    if not l[4] in regs:
        regs[l[4]] = 0;
    comp = False
    v1 = regs[l[4]]
    v2 = int(l[6])

    if l[5] == ">":
        comp = v1 > v2
    elif l[5] == ">=":
        comp = v1 >= v2
    elif l[5] == "<":
        comp = v1 < v2
    elif l[5] == "<=":
        comp = v1 <= v2
    elif l[5] == "==":
        comp = v1 == v2
    elif l[5] == "!=":
        comp = v1 != v2
    else :
        print("Unknown " + l[5])

    if not comp:
        continue

    if not l[0] in regs:
        regs[l[0]] = 0

    if l[1] == "inc":
        regs[l[0]] += int(l[2])
    elif l[1] == "dec":
        regs[l[0]] -= int(l[2])
    else :
        print("Unknown "+l[1])

    if regs[l[0]] > mv:
        mv = regs[l[0]]


m = max(regs, key=regs.get)
print(regs[m])
print(mv)
