import sys

def special(s):
    for c in range(len(s)):
        if s[c] == ')':
            break
    mod = s[1:c]
    mod = mod.split('x')
    s = s[c+1:]
    out = ""
    for k in range(int(mod[1])):
        for j in range(int(mod[0])):
            out += s[j]
    n = c+1+int(mod[0])
    return (out,n)

def deco(s):
    o = ""
    p = 0;
    while p < len(s):
        if s[p]== '(':
            (out,n) = special(s[p:])
            p += n
            o += out
            continue
        o += s[p]
        p +=1

    return o

for a in sys.stdin.readlines():
    a = a[:-1]
    print a
    d = deco(a)
    print d
    print len(d)
