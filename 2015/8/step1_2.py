import sys

def ishexa(s):
    try:
        x = int(s, 16)
        return True
    except:
        return False

def escape(s):
    r = 2
    m = len(s) - 2
    i = 1
    while i < m:
        if s[i] != '\\':
            i+=1
            continue
        if s[i+1] == '\\' or s[i+1] == '"':
            r+=1
            i+=2
            continue
        if ((i+2) < m) and ishexa(s[i+2:i+4]):
            r+=3
            i+=4
            continue
        i +=1
    return r

def enter(s):
    return 2 + s.count('"') + s.count('\\')


e = 0
s = 0
for l in sys.stdin.readlines():
    s += escape(l[:-1])
    e += enter(l[:-1])

print "Step 1"
print s

print "Step 2"
print e
