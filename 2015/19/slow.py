import sys

lines = sys.stdin.readlines()
changes = []
for l in lines[:-2]:
    l = l[:-1].split(" => ")
    changes += [l]
end = lines[-1][:-1]

def apply_change(s, change):
    s0 = s
    i = 0
    out = []
    l = len(change[0])
    while True:
        i2 = s[i:].find(change[0])
        if i2<0:
            break
        i2 = i+i2
        s2 = s[0:i2] + change[1] + s[i2+l:]
        out += [s2]
        i = i2 + l
    return out

def next_step(s):
    out = []
    for c in changes:
        out += apply_change(s, c)
    out = list(set(out))
    return out

visited = dict()
state = ["e",0]
wq = [state]

maxi = 0
while len(wq) > 0:
    [s,n] = wq[0]
    wq = wq[1:]
    if s == end:
        print n
        break
    if s in visited:
        continue
    if n>maxi:
        maxi = n
        print s
    visited[s] = n
    li = next_step(s)
    for l in li:
        if l in visited:
            continue
        wq += [[l,n+1]]

