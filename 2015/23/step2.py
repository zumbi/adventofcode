import sys

lines = sys.stdin.readlines()

pc = 0
reg = [0] * 2

reg[0] = 1

def r2n(r):
    return ord(r)-ord('a')

while (pc < len(lines) and pc >=0):
    l = lines[pc]
    #print [pc,reg]
    #print l[:-1]
    l = l.split()


    if l[0] == "hlf":
        reg[r2n(l[1])] /=2
        pc +=1
        continue
    if l[0] == "tpl":
        reg[r2n(l[1])] *=3
        pc +=1
        continue
    if l[0] == "inc":
        reg[r2n(l[1])] +=1
        pc +=1
        continue
    if l[0] == "jmp":
        pc += int(l[1])
        continue
    if l[0] == "jie":
        if reg[r2n(l[1][:-1])]%2==0:
            pc += int(l[2])
        else :
            pc += 1
        continue
    if l[0] == "jio":
        if reg[r2n(l[1][:-1])]==1:
            pc += int(l[2])
        else :
            pc += 1
        continue

print reg[1]




