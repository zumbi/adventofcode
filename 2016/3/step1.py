import sys

def is_tri(p):
    for i in range(3):
        if p[i] + p[(i+1)%3] <= p[(i+2)%3]:
            return False
    return True

n = 0
for l in sys.stdin.readlines():
    l = l.split()
    l = [ int(x) for x in l ]
    if is_tri(l):
        n+=1

print(n)
