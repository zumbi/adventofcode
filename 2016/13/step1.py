import copy

walls = dict()

def hash(x,y):
    return (x<<32) | y

def wall(x,y):
    if (x < 0) or (y < 0):
        return True
    I = 1352
    res = x*x + 3*x + 2*x*y + y + y*y
    res += I
    res = bin(res).count("1")
    return (res&1) == 1

def iswall(x,y):
    h = hash(x,y)
    if h in walls:
        return walls[h]

    walls[h] = wall(x,y)
    return walls[h]


pos = [1,1]
visited = dict()
count = 0
state = [pos,visited,count]
trip = [state]

while len(trip) > 0:
    state = trip[0]
    trip = trip[1:]

    pos = state[0]
    visited = state[1]
    count = state[2]

    if pos == [31,39]:
        print count
        break

    if iswall(pos[0], pos[1]):
        continue

    if hash(pos[0], pos[1]) in visited:
        continue

    visited[hash(pos[0],pos[1])] = True
    for i in [[0,1],[0,-1],[1,0],[-1,0]]:
       s2 = copy.deepcopy(state)
       s2[0][0] += i[0]
       s2[0][1] += i[1]
       s2[2] +=1
       trip += [s2]

