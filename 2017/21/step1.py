import sys
import numpy as np

IN_M = list()
OUT_M = list()

def convert(s):
    #print "s"
    #print s
    for i in range(len(IN_M)):
        #print "i"
        #print IN_M[i]
        if np.array_equal(s, IN_M[i]):
            return OUT_M[i]

def s_to_np(s):
    s = s.split('/')
    arr = np.zeros((len(s),len(s)),dtype=int)
    idx = 0
    for l in s:
        l = list(l)
        r = [ int(i=='#') for i in l ]
        arr[:,idx] = np.array(r)
        idx += 1
    return arr

for l in sys.stdin.readlines():
    l = l[:-1].split(" => ")
    i = s_to_np(l[0])
    o = s_to_np(l[1])
    for k in range(4):
        i = np.rot90(i)
        IN_M += [i.copy()]
        OUT_M += [o]

        a = i.copy()
        i = np.flipud(a)
        IN_M += [a.copy()]
        OUT_M += [o]

        a = i.copy()
        i = np.fliplr(a)
        IN_M += [a.copy()]
        OUT_M += [o]

array = np.array([[0,1,0],[0,0,1],[1,1,1]])

for itera in range(5):
    print itera
    l = array.shape[0]
    if (l % 2) == 0:
        l2 = (l//2) * 3
        step = 2
    else :
        l2 = (l//3) * 4
        step = 3
    new_array = np.zeros((l2,l2), dtype=int)

    for i in range(l/step):
        for j in range(l/step):
            a = array[i*step:(i+1)*step,j*step:(j+1)*step]
            na = convert(a)
            new_array[i*(step+1):(i+1)*(step+1),j*(step+1):(j+1)*(step+1)] = na

    array = new_array

print array
print np.sum(array)

