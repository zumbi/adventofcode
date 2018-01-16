import sys

lines = sys.stdin.readlines()
pc =0

regs = [0]*5

def rn(v):
    return ord(v[0]) - ord('a')

def rv(v):
    try:
        return int(v)
    except ValueError:
        return regs[rn(v)]


def process(line):
    error = False
    line = line.split(" ")
    if line[0] == "cpy":
        regs[rn(line[2])] = rv(line[1])
    elif line[0] == "inc":
        regs[rn(line[1])] += 1
    elif line[0] == "dec":
        regs[rn(line[1])] -= 1
    elif line[0] == "jnz":
        if rv(line[1]) != 0:
            return [rv(line[2]),error]
    elif line[0] == "out":
        o =  rv(line[1])
        if o == regs[4]:
            error = True
        regs[4] = o
    else :
        print line
    return [1,error]

av = 0
regs[4] = -1
while pc <len(lines):
    [inc,error] = process(lines[pc])
    pc += inc
    if (error):
        av +=1
        print av
        regs = [0]*5
        regs[4] = -1
        regs[0] = av
        pc = 0

