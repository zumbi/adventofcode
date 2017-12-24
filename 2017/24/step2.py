import sys

chains = list()
for c in sys.stdin.readlines():
    c = c.split("/")
    chains += [[int(c[0]), int(c[1])]]

def lenc(v, s, l, ch):
    mv = 0
    lv = 0
    for i in range(len(ch)):
        v2 = -1
        if ch[i][0] == v:
            v2 = ch[i][1]
        if ch[i][1] == v:
            v2 = ch[i][0]
        if v2 != -1:
            ch2 = ch[:]
            r = ch2.pop(i)
            (mv2 , lv2) = lenc(v2, s, l+1, ch2)
            mv2 += r[0] + r[1]
            if lv2 > lv:
                lv = lv2
                mv = mv2
            if lv2 == lv:
                mv = max(mv,mv2)
    return (s+mv, l+lv)

print lenc(0,0,0,chains)[0]
