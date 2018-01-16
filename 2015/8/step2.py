import sys

def ishexa(s):
    try:
        x = int(s, 16)
        return True
    except:
        return False

def enter(s):
    r = 2
    m = len(s)
    i = 0
    while i < m:
        if s[i] == '"':
            r+=1
        elif s[i] == '\\':
            r+=1
        i +=1
    return r


s = 0
for l in sys.stdin.readlines():
    s += enter(l[:-1])

print s
