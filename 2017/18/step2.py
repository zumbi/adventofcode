import sys

def deco(val, regs):
    if val.lstrip('-').isdigit():
        return int(val)
    else:
        return regs[val]

def execu(state, fifo_in, fifo_out, d=0):
    if state[0] >= len(lines):
        return 0
    regs = state[1]
    l = lines[state[0]][:-1].split(" ")
    if (d):
        print(state[0], l)
    #v2 decoding
    if (len(l) > 2):
        v2 = deco(l[2], regs)
    if l[0] == "snd":
        v1 = deco(l[1], regs)
        fifo_out.append(v1)
        state[0] += 1
        state[2] += 1
    elif l[0] == "set":
        regs[l[1]] = v2
        state[0] += 1
    elif l[0] == "add":
        regs[l[1]] += v2
        state[0] += 1
    elif l[0] == "mul":
        regs[l[1]] *= v2
        state[0] += 1
    elif l[0] == "mod":
        regs[l[1]] %= v2
        state[0] += 1
    elif l[0] == "rcv":
        if len(fifo_in) == 0:
            return 0
        regs[l[1]] = fifo_in.pop(0)
        state[0] += 1
    elif l[0] == "jgz":
        v1 = deco(l[1], regs)
        if v1 > 0:
            state[0] += v2
        else:
            state[0] += 1
    return 1

lines = sys.stdin.readlines()

regs0 = dict()
regs1 = dict()
for a in range(ord('a'), ord('z')+1):
    regs0[chr(a)] = 0
    regs1[chr(a)] = 0
regs1['p'] = 1


state0 = [0,regs0,0]
state1 = [0,regs1,0]
fifo0 = list()
fifo1 = list()

e = 2
while e > 0:
    e = 0
    e += execu(state0, fifo0, fifo1, 0)
    e += execu(state1, fifo1, fifo0, 0)


print state1[2]

