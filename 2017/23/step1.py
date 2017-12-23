import sys

def deco(val, regs):
    if val.lstrip('-').isdigit():
        return int(val)
    else:
        return regs[val]

def execu(state, d=0):
    if state[0] >= len(lines):
        return 0
    regs = state[1]
    l = lines[state[0]][:-1].split(" ")
    if (d):
        print(state[0], l)
    #v2 decoding
    if (len(l) > 2):
        v2 = deco(l[2], regs)
    if l[0] == "set":
        regs[l[1]] = v2
        state[0] += 1
    elif l[0] == "sub":
        regs[l[1]] -= v2
        state[0] += 1
    elif l[0] == "mul":
        regs[l[1]] *= v2
        state[0] += 1
        state[2] += 1
    elif l[0] == "jnz":
        v1 = deco(l[1], regs)
        if v1 != 0:
            state[0] += v2
        else:
            state[0] += 1
    else:
        return 0
    return 1

lines = sys.stdin.readlines()

regs = dict()
for a in range(ord('a'), ord('h')+1):
    regs[chr(a)] = 0

state = [0,regs,0]

while True:
    if execu(state, 0) == 0:
        break;

print state[2]

