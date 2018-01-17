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

def pst(s):
    out = []
    for i in s:
        for j in convert:
            if convert[j] == i:
                out +=[j]
                break
    return ''.join(out)


lines = sys.stdin.readlines()
changes = dict()
invert = list()
for l in lines[:-2]:
    l = l[:-1].split(" => ")
    fr = e2n(l[0])
    to = string2n(l[1])
    if fr not in changes:
        changes[fr] = []
    changes[fr] += [to]
    invert += [[string2n(l[1]), [e2n(l[0])]]]

start = string2n(lines[-1][:-1])
end = [e2n("e")]

st = [start,0]

def find_sub(big,small):
    out = []
    for i in range(len(big)-len(small)+1):
        found = True
        for j in range(len(small)):
            if big[i+j]!=small[j]:
                found = False
                break;
        if found:
            out += [i]
    return out


def applyc(change,s):
    i = 0
    out = []
    pos = find_sub(s,change[0])
    l = len(change[0])
    for p in pos:
        s1 = s[0:p] + change[1] + s[p+l:]
        if change[1] == end and len(s1)!=1:
            continue
        out += [s1]
    return out

def compare(i1,i2):
    return len(i1[0]) - len(i2[0])

visited = dict()
last_len = len(start)
wq = [st]
while len(wq) > 0:
    wq = sorted(wq, cmp=compare)

    [s,n] = wq[0]
    wq = wq[1:]

    if len(s) < last_len:
        print [pst(s),n]
        print len(s)
        last_len = len(s)

    if s == end:
        print s
        print n
        break

    new = []
    for i in invert:
        new += applyc(i,s)
    for c in new:
        h = str(c)
        if n+1 >=250:
            continue
        if h in visited and visited[h] <= n+1:
            continue
        visited[h] = n+1
        wq += [[c,n+1]]



