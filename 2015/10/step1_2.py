v0 = map(int,list("3113322113"))
#v0 = map(int,list("1"))

def dh(s):
    s = map(int,list(s))
    s2 = []
    i = 0
    while i<len(s):
        n = 0
        v = s[i]
        while i<len(s) and s[i] == v:
            n += 1
            i += 1
        s2 += [n,v]
    return ''.join(map(str,s2))

for i in range(40):
    v0 = dh(v0)

print "Step 1"
print len(v0)

for i in range(10):
    v0 = dh(v0)

print "Step 2"
print len(v0)
