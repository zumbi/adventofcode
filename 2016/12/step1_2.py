import sys

lines = sys.stdin.readlines()
pc =0

regs = [0]*4

def rn(v):
    return ord(v[0]) - ord('a')

def rv(v):
    try:
        return int(v)
    except ValueError:
        return regs[rn(v)]

def process(line):
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
    return 1

while pc <len(lines):
    pc += process(lines[pc])
print "step1"
print regs[0]

regs = [0]*4
regs[2] = 1
pc = 0
while pc <len(lines):
    pc += process(lines[pc])
print "step2"
print regs[0]
