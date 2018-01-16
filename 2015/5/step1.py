import sys

def nice(s):
    nv =0
    for v in [ 'a', 'e', 'i', 'o', 'u']:
        nv += s.count(v)
    if nv<3:
        return False

    rep = False
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            rep = True
            break

    if not rep:
        return False

    for a in ["ab", "cd", "pq", "xy"]:
       if a in s:
           return False

    return True

c = 0
for l in sys.stdin.readlines():
    if nice(l):
        c += 1

print c
