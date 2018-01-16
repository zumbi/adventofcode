import sys
import numpy as np

s = np.zeros([1000,1000], dtype=bool)


for l in sys.stdin.readlines():
    l2 = l
    l = l.split()
    v1 = map(int,l[-3].split(","))
    v2 = map(int,l[-1].split(","))
    c = sorted([v1[0],v2[0]])
    li = sorted([v1[1],v2[1]])

    a = s[li[0]:li[1]+1, c[0]:c[1]+1]
    if l[1] == "on":
        a[:,:] = True
    elif l[1] == "off":
        a[:,:] = False
    elif l[0] == "toggle":
        a[:,:] ^= True
    else:
        print "error"

print s.sum()


