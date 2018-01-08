import sys

lines = sys.stdin.readlines()
pc =0

regs = [0]*4
regs[0] = 7

def rn(v):
    return ord(v[0]) - ord('a')

def rv(v):
    try:
        return int(v)
    except ValueError:
        return regs[rn(v)]

def tgl(idx):
    if idx <0 or idx>=len(lines):
        return
    line = lines[idx].split(" ")
    if len(line) == 2:
        if line[0] == "inc":
            line[0] = "dec"
        else:
            line[0] = "inc"
    else:
        if line[0] == "jnz":
            line[0] = "cpy"
        else:
            line[0] = "jnz"
    lines[idx] =  " ".join(line)

def process(line,pc):
    line = line.split(" ")
    if line[0] == "cpy":
        regs[rn(line[2])] = rv(line[1])
    elif line[0] == "inc":
        regs[rn(line[1])] += 1
    elif line[0] == "dec":
        regs[rn(line[1])] -= 1
    elif line[0] == "jnz":
        if rv(line[1]) != 0:
            return rv(line[2])
    elif line[0] == "tgl":
        tgl(rv(line[1])+pc)

    return 1

while pc <len(lines):
    pc += process(lines[pc],pc)
print regs[0]
