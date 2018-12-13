import sys

line = sys.stdin.readline()
sys.stdin.readline()

def to_pots(init):
    pots = [0] * len(init)
    for i in range(len(init)):
        if init[i] == '#':
            pots[i] = 1
    return pots

init = line[:-1].split(": ")[1]
pots = to_pots(init)

def enlarge(p):
    if sum(p[0:5])!=0:
        p = 5 * [0] + p
    if sum(p[-5:])!=0:
        p = p + 5 * [0]
    return p


def calc(p):
    v = 0
    for i in range(len(p)):
        v *= 2
        v += p[i]
    return v

def calc_uniq(val):
    while (val & 1) == 0:
        val /=2
    return val

def first_one(pots):
    for i in range(len(pots)):
        if pots[i] != 0:
            return i


transfers = [0] * 32
for l in sys.stdin.readlines():
    l = l[:-1].split(" => ")
    if  l[1] == "#" :
        v = 1
    else: 
        v = 0
    transfers[calc(to_pots(l[0]))] =v

def exec_step(p):
    l = len(p)
    p2 = [0] * l
    for i in range(3,l-3):
        p2[i] = transfers[calc(p[i-2:i+3])]
    return p2

def calc_sm(j,pots):
    sm = 0
    for i in range(len(pots)):
        sm += (i - j) * pots[i]
    return sm

i = 0
idx = 0
old_pots = pots
NUM = 50000000000
while i<NUM:
    if sum(pots[0:5])!=0:
        idx += 5
    pots = enlarge(old_pots)
    pots = exec_step(pots)
    i += 1

    if calc_uniq(calc(pots))!=calc_uniq(calc(old_pots)):
        old_pots = pots
        continue

    #System is stable
    left = first_one(pots) - first_one(old_pots)
    idx -= (NUM-i)
    break

print(calc_sm(idx, pots))
