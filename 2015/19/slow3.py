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
#print convert

def addt(t,out):
    for o in range(len(out)):
        if out[o][0] == t[0]:
            if t[1] < out[o][0]:
                out[o][1] = t[1]
            return out
    return out + [t]

def pst(s):
    out = []
    for i in s:
        for j in convert:
            if convert[j] == i:
                out +=[j]
                break
    return ''.join(out)

def trans(s):
    added = True
    out = [[[s],0]]
    process = []

    while added:
        added = False
        out2 = []
        for o in out:
            out2 = addt(o,out2)
            if o[0][0] not in process:
                process += [o[0][0]]
                added = True
            if o[0][0] not in changes:
                continue
            for c in changes[o[0][0]]:
                s2 = c + o[0][1:]
                out2 = addt([s2,o[1]+1],out2)
        out = out2

    print pst([s])
    print "=>"
    for o in out[1:]:
        print [pst(o[0]),o[1]]

    return out[1:]


T = dict()
for p in changes:
    T[p] = trans(p)

#print T
#print end

def compare(i1,i2):
    return len(i2[0]) - len(i1[0])

visited = dict()

st = [[e2n("e")],0,0]
wq = [st]
min_n = None
max_i = 0
while len(wq) > 0:
    #print wq
    wq = sorted(wq, cmp=compare)
    #print wq
    [s,i,n] = wq[0]
    #print "Process " + pst(s)
    #print [s,i]
    wq = wq[1:]


    if len(s) > len(end):
        continue
    if n >= 250:
        continue

    if min_n and n>=n:
        continue

    if i > max_i:
        max_i = i
        print i
        print pst(s[:i])
        print pst(s)

    if s == end:
        if min_n == None or n<min_n:
            min_n = n
            print pst(s)
            print n

    if s[0] not in T:
        continue

    w = []
    for t in T[s[0]]:
        s1 = s[:i] + t[0] + s[i+1:]

        if s1[i] == end[i]:
            h = str([s1,i])
            if not( h in visited and n>= visited[h]):
                w += [[s1[:],i,n+t[1]]]
        #print "Add "+ pst(s1)
        #print [s1,i]

        for i0 in range(i,min(len(s1),len(end))-1):
            if s1[i0] != end[i0]:
                break
            #print "Add "+ pst(s1)
            #print [s1,i0+1]
            h = str([s1,i0+1])
            if not( h in visited and n+t[1]>= visited[h]):
                w += [[s1[:],i0+1,n+t[1]]]
                visited[h] = n+t[1]
    wq += w

print min_n


