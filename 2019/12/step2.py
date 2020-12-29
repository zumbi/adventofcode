import sys
import math

pos = list()
speed = list()


def parse_pos(v):
    return int(v[2:])


def pot(v):
    p = 0
    for i in v:
        p += abs(i)
    return p


def get_i(lin,idx):
    lo = list()
    for l in lin:
        lo.append(l[idx])
    return lo

def to_str(pos,speed,idx):
    return str([get_i(pos,idx),get_i(speed,idx)])


def step(pos, speed):
    for i in range(len(pos)):
        for j in range(len(pos)):
            if j == i:
                continue
            for k in range(len(pos[i])):
                if pos[i][k] > pos[j][k]:
                    speed[i][k] -= 1
                elif pos[i][k] < pos[j][k]:
                    speed[i][k] += 1

    for i in range(len(pos)):
        for k in range(len(pos[i])):
            pos[i][k] += speed[i][k]

def calc_turns(pos,speed,idx):
    i = 0
    visited = dict()
    while True:    
        step(pos,speed)
        s = to_str(pos,speed,idx)
        if s in visited:
            return i 
            
        visited[s] = i
        i +=1

for l in sys.stdin.readlines():
    l = l.strip()
    l = l[1:-1]
    l = l.split(", ")
    l = list(map(parse_pos, l))
    pos.append(l)
    speed.append([0]*len(l))

out = 1
for i in range(len(pos[0])):
    r = calc_turns(pos[:],speed[:],i)    
    out = math.lcm(out,r)

print(out)
