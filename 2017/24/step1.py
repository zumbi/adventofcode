import sys

chains = list()
for c in sys.stdin.readlines():
    c = c.split("/")
    chains += [[int(c[0]), int(c[1])]]

def lenc(v, s, ch):
    mv = 0
    for i in range(len(ch)):
        v2 = -1
        if ch[i][0] == v:
            v2 = ch[i][1]
        if ch[i][1] == v:
            v2 = ch[i][0]
        if v2 != -1:
            ch2 = ch[:]
            r = ch2.pop(i)
            mv2 = lenc(v2, s, ch2) + r[0] + r[1]
            if mv2 > mv:
                mv = mv2
    return s+mv

print lenc(0,0,chains)
