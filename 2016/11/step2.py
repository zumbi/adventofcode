import copy
import sys
import pickle

#tot = 10
#i = [[0,10],[1,2,3,4],[11,12,13,14],[]]
#tot = 4
#i = [[10,11],[0],[1],[]]
tot = 14
i = [[0,10,5,15,6,16],[1,2,3,4],[11,12,13,14],[]]
e = 0
n = 0

state = [i,e,n]
todo = [state]

def fc(inp,v):
    for i in range(len(inp)):
        for j in inp[i]:
            if j == v:
                continue
            if (j % 10) ==  (v % 10):
                return i

def hash(inp,e):
    i2 = copy.deepcopy(inp)
    for i in range(len(inp)):
        for j in range(len(inp[i])):
            i2[i][j] = i-fc(inp,inp[i][j])
            if inp[i][j] >= 10:
                i2[i][j] += 100
    for i in range(len(inp)):
        i2[i] = sorted(i2[i])
    return pickle.dumps([e,i2])


def explotion(l):
    hot = False
    for i in l:
        if i // 10 == 0:
            hot = True
            break
    if not hot:
        return False

    for i in l:
        if i // 10 == 0:
            continue
        if not i%10 in l:
            return True

    return False

def valid_state(s):
    for i in s[0]:
        if explotion(i):
            return False
    return True


def valid_pairs(l):
    out = []
    for i in range(len(l)):
        out += [[l[i]]]
        for j in range(i+1, len(l)):
            p = [l[i],l[j]]
            out += [[l[i],l[j]]]
    return out

vi = dict()

max_n = 0
while len(todo)>0:
    s = todo[0]
    todo = todo[1:]
    i = s[0]
    e = s[1]
    n = s[2]
    h = hash(i,e)
    if h in vi:
        continue
    vi[h] = True
    if n > max_n:
        max_n = n
        print max_n
        print len(todo)
        print i
    if len(i[3]) == tot:
        print s
        print n
        sys.exit(0)
    vp = valid_pairs(i[e])
    for p in vp:
        for shift in [-1,+1]:
            e2 = e+shift
            if (e2 < 0) or (e2 > 3):
                continue
            s2 = copy.deepcopy(s)
            s2[1] = e2
            s2[2] += 1
            for v in p:
                s2[0][e].remove(v)
            s2[0][e2] = s2[0][e2] + p
            if not valid_state(s2):
                continue
            if hash(s2[0],e2) in vi:
                continue
            todo += [s2]


