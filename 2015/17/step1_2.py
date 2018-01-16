import sys

b = sys.stdin.readlines()
b = sorted(map(int,b))

total = 150

def su(v):
    s = 0
    for i in range(len(v)):
        s += v[i] * b[i]
    return s

def inc(v):
    v[-1] +=1
    for i in range(len(v)-1,-1,-1):
        #if v[i] * b[i] > total:
        if v[i] > 1:
            if i == 0:
                return None
            v[i-1] += 1
            v[i] = 0
    return v

v = [0] * len(b)

mini = len(b)
n_mini = 0
n = 0
while (v!=None):
    if su(v) == total:
        n+=1
        s = sum(v)
        if s < mini:
            n_mini = 1
            mini = s
        elif s == mini:
            n_mini += 1

    v = inc(v)

print "Step 1"
print n
print "Step 2"
print n_mini
