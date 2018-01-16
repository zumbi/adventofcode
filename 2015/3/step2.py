import sys

def visit(d,p):
    v = str(p)
    if v in d:
        d[v]+=1
    else:
        d[v] = 1

for l in sys.stdin.readlines():
    n = 0
    d=dict()
    p = [[0,0],[0,0]]
    visit(d,p[0])
    visit(d,p[1])
    for c in l:
        n +=1
        idx = n & 1
        if c == '^':
            p[idx][1] +=1
        elif c == 'v':
            p[idx][1] -=1
        elif c == '>':
            p[idx][0] +=1
        elif c == '<':
            p[idx][0] -=1
        else:
            print c
            continue
        visit(d,p[idx])
    print len(d.keys())

