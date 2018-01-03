import sys

def is_tri(p):
    for i in range(3):
        if p[i] + p[(i+1)%3] <= p[(i+2)%3]:
            return False
    return True

tris = 0
t = [[0,0,0],[0,0,0],[0,0,0]]

n = 0
for l in sys.stdin.readlines():
    l = l.split()
    l = [ int(x) for x in l ]
    for i in range(3):
        t[i][n%3] = l[i]

    n += 1
    if (n % 3) != 0:
        continue

    for i in range(3):
        if is_tri(t[i]):
            tris+=1

print(tris)
