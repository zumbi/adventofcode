import sys

p = 0
r = 0
for l in sys.stdin.readlines():
    l = l.split('x')
    l = map(int, l)
    l = sorted(l)
    p += 3 * (l[0] * l[1])
    p += 2 * (l[1] * l[2])
    p += 2 * (l[2] * l[0])

    r+= 2*(l[0] + l[1])
    r+= l[0] * l[1] * l[2]


print "Step 1"
print(p)

print "Step 2"
print(r)
