import sys

lines = sys.stdin.readlines()

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


changes = []
for l in lines[:-2]:
    l = l[:-1].split(" => ")
    changes += [l]

inp = lines[-1][:-1]

out = []
for c in changes:
    out += apply_change(inp, c)

out = list(set(out))
print len(out)
