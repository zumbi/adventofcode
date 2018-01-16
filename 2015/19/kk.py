import sys
import string

lines = sys.stdin.readlines()
changes = dict()
for l in lines[:-2]:
    l = l[:-1].split(" => ")
    if l[0] not in changes:
        changes[l[0]] = []
    changes[l[0]] += [l[1]]

end = lines[-1][:-1]

def trans(s):
    todo = [[s,0]]
    progress = []
    out = []

    while len(todo) >0:
        [s,n] = todo[0]
        todo = todo[1:]
        for p in changes:
            if s.find(p) != 0:
                continue
            if p not in progress:
                progress += [p]
            for c in changes[p]:
                s0 = c + s[len(p):]
                out += [[s0,n+1]]
                for i in changes:
                    if s0.find(i) == 0 and i not in progress:
                        todo += [[s0,n+1]]
    return out

T = dict()
for p in changes:
    T[p] = trans(p)

s = ["e",0,0]
wq = [s]

min_n = None
max_i = 0

visi = dict()

while len(wq) > 0:
    [s,i,n] = wq[0]
    wq = wq[1:]
    #print ["start",s,i,n]

    if s in visi and visi[s] < n:
        continue

    visi[s] = n

    if i > max_i:
        print [i, s]
        max_i = i

    if len(s) > len(end):
        continue

    if i == len(end):
        if n == None or n<min_n:
            print n
            n = min_n
        break

    for p in T:
        if s[i:].find(p) != 0:
            continue
        w = []
        for t in T[p]:
            if end[i:].find(t[0][0]) != 0:
                continue
            s1 = end[0:i] + t[0] + s[i+len(p):]
            if len(s1)>len(end):
                continue
            i0 = i
            #while (i0<min(len(s1),len(end))) and s1[i0] == end[i0]:
            #    i0+=1
            #w += [[s1[:],i0,n+t[1]]]
            w += [[s1[:],i+len(p),n+t[1]]]
            i0 = i+len(p) +1
            while (i0<min(len(s1),len(end))) and s1[i0] == end[i0]:
                if (i0+1)==len(s1) or  not s1[i0+1].islower():
                    w += [[s1[:],i0+1,n+t[1]]]
                i0 += 1
        #print ["new work",w]
        wq += w

print min_n


