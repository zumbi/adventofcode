import sys

def visit(d,p):
    v = str(p)
    if v in d:
        d[v]+=1
    else:
        d[v] = 1

for l in sys.stdin.readlines():
    d=dict()
    p = [0,0]
    visit(d,p)
    for c in l:
        if c == '^':
            p[1] +=1
        elif c == 'v':
            p[1] -=1
        elif c == '>':
            p[0] +=1
        elif c == '<':
            p[0] -=1
        else:
            print c
            continue
        visit(d,p)
    print len(d.keys())
