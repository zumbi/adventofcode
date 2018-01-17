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
    added = True
    out = [[[s],0]]
    process = []

    while added:
        added = False
        out2 = []
        l2 = []
        for o in out:
            if o[0] not in l2:
                l2 += [o[0]]
                out2 += [o]
            if o[0][0] not in changes:
                continue
            if o[0][0] not in process:
                process += [o[0][0]]
                added = True
            for c in changes[o[0][0]]:
                s2 = c + o[0][1:]
                if s2 not in l2:
                    l2 += [s2]
                    out2 += [[s2,o[1]+1]]
        out = out2

    print out[1:]
    return out[1:]


T = dict()
for p in changes:
    T[p] = trans(p)

print T
print end



st = [[e2n("e")],0,0]
wq = [st]
min_n = None
while len(wq) > 0:
    [s,i,n] = wq[0]
    wq = wq[1:]

    if len(s) > len(end):
        continue

    if s == end:
        if min_n == None or n<min_n:
            min_n = n
            print s
            print n

    w = []
    for t in T[s[0]]:
        s1 = s[:i] + t[0] + s[i+1:]
        for i0 in range(i,min(len(s1),len(end))-1):
            if s1[i0] != end[i0]:
                break
            w += [[s1[:],i0+1,n+t[1]]]
    wq += w

print min_n


