import sys

def deco(s):
    out = 0
    p = 0
    while p < len(s):
        if s[p]== '(':
            j = p
            while s[j] != ')':
                j +=1
            mod = s[p+1:j]
            mod = mod.split('x')

            out += int(mod[1]) * deco(s[j+1:j+1+int(mod[0])])
            p = j + int(mod[0]) + 1
            continue
        out +=1
        p +=1

    return out

for a in sys.stdin.readlines():
    a = a[:-1]
    print deco(a)
