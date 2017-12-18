import sys

lines = sys.stdin.readlines()

regs = dict()
for a in range(ord('a'), ord('z')+1):
    regs[chr(a)] = 0

pc = 0
lastpc = len(lines)
snd = 0

while (pc < lastpc):
    l = lines[pc][:-1].split(" ")
    #print regs['a']
    #print (pc, l)
    #v2 decoding
    if (len(l) > 2):
        if l[2].lstrip('-').isdigit():
            v2 = int(l[2])
        else:
            v2 = regs[l[2]]
    pc +=1

    if l[0] == "snd":
        snd = regs[l[1]]
    elif l[0] == "set":
        regs[l[1]] = v2
    elif l[0] == "add":
        regs[l[1]] += v2
    elif l[0] == "mul":
        regs[l[1]] *= v2
    elif l[0] == "mod":
        regs[l[1]] %= v2
    elif l[0] == "rcv":
        if regs[l[1]] != 0:
            regs[l[1]] = snd
            break
    elif l[0] == "jgz":
        if regs[l[1]] > 0:
            pc -= 1
            pc += v2



print snd

