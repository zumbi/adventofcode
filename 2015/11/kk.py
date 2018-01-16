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
            if i == 0:
                return None
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
    if s == None:
        return None
    while not valid(s):
        s = inc(s)
        if s == None:
            return None
    return s

n = 0
s0 = "aaaaaaaa"
s = s0
while True:
    s = nextp(s)
    if s == None:
        break
    n += 1
    print[n,s]

valid = n / float ((ord('z') - ord('a') + 1)**len(s0))
print valid

