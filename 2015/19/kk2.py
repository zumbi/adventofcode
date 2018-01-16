import sys


convert = dict()
def e2n(h):
    if h not in convert:
        convert[h] = len(convert)
    return convert[h]

def string2n(s):
    o = []
    i = 0
    while i<len(s):
        if (i+1)<len(s) and s[i+1].islower():
            o+=[e2n(s[i:i+2])]
            i+=2
        else:
            o+=[e2n(s[i:i+1])]
            i+=1
    return o


lines = sys.stdin.readlines()
changes = dict()
for l in lines[:-2]:
    l = l[:-1].split(" => ")
    if e2n(l[0]) not in changes:
        changes[e2n(l[0])] = []
    changes[e2n(l[0])] += [string2n(l[1])]

end = string2n(lines[-1][:-1])


def trans(s):
    todo= [[[s],0]]
    done = []
    out = []
    while len(todo) > 0:
        [s,n] = todo[0]
        todo = todo[1:]

        if s[0] not in done:
            done += [s[0]]

        if s[0] not in changes:
            continue

        for c in changes[s[0]]:
            s0 = c + s[1:]
            out += [[s0,n+1]]
            if s0[0] in done:
                continue
            todo += [[s0,n+1]]
    return out

T = dict()
for p in changes:
    T[p] = trans(p)


#print convert
#print T[11]
#print end

print end

st = [[e2n("e")],0,0]
wq = [st]
min_n = None
while len(wq) > 0:
    [s,i,n] = wq[0]
    wq = wq[1:]

    print [s,i]
    if len(s) > len(end):
        continue

    if s == end:
        if min_n == None or n<min_n:
            min_n = n
            print n

    w = []
    for t in T[s[0]]:
        s1 = s[:i] + t[0] + s[i+1:]
        for i0 in range(i,min(len(s1),len(end))-1):
            if s1[i0] != end[i0]:
                break
            w += [[s1[:],i0+1,n+t[1]]]
    wq += w



