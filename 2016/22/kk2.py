import sys
import copy
import cPickle as pickle

X = 38
Y = 28
#X = 3
#Y = 3

used = list()
for y0 in range(Y):
    x =[]
    for x0 in range(X):
        x += [0]
    used +=[x]

size = copy.deepcopy(used)

for l in sys.stdin.readlines()[2:]:
    l = l.split()
    us = int(l[2][:-1])
    si = int(l[1][:-1])
    name = l[0].split("-")
    x = int(name[1][1:])
    y = int(name[2][1:])
    used[y][x] = us
    size[y][x] = si

def h(a,b):
    return pickle.dumps([a,b])

def movements(used):
    movements = list()
    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    for y in range(Y):
        for x in range(X):
            for p in pos:
                y0 = y+p[0]
                x0 = x+p[1]
                if x0<0 or x0 >=X or y0<0 or y0 >=Y:
                    continue
                if (used[y][x] + used[y0][x0]) <= size[y0][x0]:
                    m = [[y,x] ,[y0,x0]]
                    movements += [m]

    return movements

data = [0,X-1]
state = [data,used,0]

work =[state]

visited = dict()
last_step = 0
while len(work) > 0:
    s =work[0]
    work = work[1:]

    [data,used,steps] = s
    ha = h(used,data)
    if ha in visited:
        continue
    visited[ha] = True

    if steps > last_step:
        last_step = steps
        print (steps, len(work))
    #print s

    if data == [0,0]:
        print steps
        break

    mov = movements(used)
    for m in mov:
        #print m
        s2 = copy.deepcopy(s)
        [data,used,steps] = s2
        used[m[1][0]][m[1][1]] += used[m[0][0]][m[0][1]]
        used[m[0][0]][m[0][1]] = 0
        if [m[0][0],m[0][1]] == data:
            data = [m[1][0],m[1][1]]
        ha = h(used,data)
        if ha in visited:
            continue
        s2 = [data,used,steps+1]
        work += [s2]



