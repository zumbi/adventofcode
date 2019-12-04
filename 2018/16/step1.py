import sys

def step(ins, regs_in):
    regs = regs_in[:]

    op = ins[0]

    #addr
    if op == 0:
        regs[ins[3]] = regs[ins[1]] + regs[ins[2]]
    #addi
    elif op == 1:
        regs[ins[3]] = regs[ins[1]] + ins[2]
    #mulr
    elif op == 2:
        regs[ins[3]] = regs[ins[1]] * regs[ins[2]]
    #mulr
    elif op == 3:
        regs[ins[3]] = regs[ins[1]] * ins[2]
    #banr
    elif op == 4:
        regs[ins[3]] = regs[ins[1]] & regs[ins[2]]
    #bani
    elif op == 5:
        regs[ins[3]] = regs[ins[1]] & ins[2]
    #borr
    elif op == 6:
        regs[ins[3]] = regs[ins[1]] | regs[ins[2]]
    #bori
    elif op == 7:
        regs[ins[3]] = regs[ins[1]] | ins[2]
    #setr
    elif op == 8:
        regs[ins[3]] = regs[ins[1]]
    #seti
    elif op == 9:
        regs[ins[3]] = ins[1]
    #gtir
    elif op == 10:
        if ins[1] > regs[ins[2]]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0
    #gtri
    elif op == 11:
        if regs[ins[1]] > ins[2]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0
    #gtrr
    elif op == 12:
        if regs[ins[1]] > regs[ins[2]]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0
    #eqri
    elif op == 13:
        if regs[ins[1]] == ins[2]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0
    #eqir
    elif op == 14:
        if ins[1] == regs[ins[2]]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0
    #eqrr
    elif op == 15:
        if regs[ins[1]] == regs[ins[2]]:
            regs[ins[3]] = 1
        else:
            regs[ins[3]] = 0

    return regs

def count_eq(ins,regs_in,regs_out):
    count = 0;
    for a in range(16):
        ins[0] = a
        r = step(ins,regs_in)
        if r == regs_out:
            count += 1
    return count

count = 0
lines = sys.stdin.readlines()
for i in range(len(lines)//4):
    regs_in = [int (x) for x in lines[i*4+0].split("[")[1][:-2].split(", ")]
    ins = [int (x)  for x in lines[i*4+1][:-1].split(" ")]
    regs_out = [int (x) for x in lines[i*4+2].split("[")[1][:-2].split(", ")]
    if count_eq(ins,regs_in, regs_out) >= 3:
        count += 1

print(count)
