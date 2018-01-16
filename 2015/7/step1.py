import sys

lines = sys.stdin.readlines()
regs = dict()

def get_op(op):
    if op[-1].isdigit():
        return int(op)
    if op not in regs:
        return None
    return regs[op]

def do_line(line):
    l = line.split()
    if l[0] == "NOT":
        op0 = get_op(l[1])
        if op0 == None:
            return False
        regs[l[-1]] = (~op0) & 0xffff
        return True
    if l[1] == "->":
        op0 = get_op(l[0])
        if op0 == None:
            return False
        regs[l[-1]] = op0 & 0xffff
        return True

    op1  = get_op(l[0])
    op2  = get_op(l[2])
    if op1 == None or op2 == None:
       return False
    if l[1] == "AND":
        regs[l[-1]] = (op1 & op2) & 0xffff
    elif l[1] == "OR":
        regs[l[-1]] = (op1 | op2) & 0xffff
    elif l[1] == "RSHIFT":
        regs[l[-1]] = (op1 >> op2) & 0xffff
    elif l[1] == "LSHIFT":
        regs[l[-1]] = (op1 << op2) & 0xffff
    else:
        print l[1]
    return True


while len(lines) > 0 :
    for i in range(len(lines)-1,-1,-1):
        #print lines[i][:-1]
        if do_line(lines[i][:-1]):
            lines.pop(i)
        #print regs

print regs
print regs["a"]
