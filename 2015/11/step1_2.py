s = "hxbxwxba"

def s2n(v):
    return ord(v) - ord('a')

def n2s(v):
    return chr(v + ord('a'))

def inc(s):
    s = map(s2n,list(s))
    s[-1] += 1
    zz = ord('z') - ord('a') + 1
    for i in reversed(range(len(s))):
        if s[i] >= zz:
            s[i-1] += s[i] / zz
            s[i] %= zz
    s = ''.join(map(n2s,s))
    return s

def valid(s):
    if "i" in s:
        return False
    if "o" in s:
        return False
    if "l" in s:
        return False

    c1 = False
    c3 = False
    pair = []

    s = map(s2n,list(s))

    for i in range(len(s)-1):
        if not c1 and s[i] == s[i+1]:
            if s[i] not in pair:
                pair += [s[i]]
            if len(pair) >=2 :
                c1 = True
        if i+2 >= len(s):
            continue
        if not c3 and s[i] + 1  == s[i+1] and s[i] + 2 == s[i+2]:
            c3 = True

    return c1 and c3

def nextp(s):
    s = inc(s)
    while not valid(s):
        s = inc(s)
    return s

print "Step 1"
s = nextp("hxbxwxba")
print s
print "Step 2"
s = nextp(s)
print s


