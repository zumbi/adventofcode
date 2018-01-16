import sys
import numpy as np
from scipy import ndimage

N = 100

def s2i(v):
    if v == '#':
        return 1
    return 0

def corners(s):
    s[0,0] = 1
    s[0,-1] = 1
    s[-1,0] = 1
    s[-1,-1] = 1
    return s

def step(s):
    cv = np.zeros([N+2,N+2], dtype=int)
    cv[2:N+2,2:N+2] = s
    k = np.array([[1, 1, 1],
                    [1, 0, 1],
                    [1, 1, 1],],
                   dtype='int')
    cv = ndimage.convolve(cv, k, mode='constant', cval=0.0)
    cv =cv[2:N+2,2:N+2]

    s2 = s.copy()
    s[(s2==1) & ((cv!=2) & (cv!=3))] = 0
    s[(s2==0) & (cv==3)] = 1
    return s



s = np.zeros([N,N], dtype=int)
i = 0
for l in sys.stdin.readlines():
    l=map(s2i,list(l[:-1]))
    s[i] = l
    i+=1

s=corners(s)

for i in range(100):
    s = step(s)
    s = corners(s)

print np.sum(s)

