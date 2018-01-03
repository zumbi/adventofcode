import sys
import re

def compare(i1,i2):
    if i1[1] == i2[1]:
        return ord(i1[0]) - ord(i2[0])
    return i2[1] - i1[1]

def fivemore(d):
    l = list()
    for key, value  in d.iteritems():
        l += [[key,value]]

    l = sorted(l, cmp=compare)
    out = ""
    for i in range(5):
        out += l[i][0]
    return out

def csum(inp):
    s = inp.split('[')[-1][:-2]
    return s

def validate(inp):
    d = dict()
    s = inp.split('-')[:-1]
    for i in s:
        for j in i:
            if j in d:
                d[j] +=1
            else:
                d[j] =1
    return fivemore(d) == csum(inp)

def id(s):
    s = s.split('-')[-1]
    s = s.split('[')[0]
    return int(s)

def decode(inp, inc):
    s = inp.split('-')[:-1]
    out = ""
    for i in s:
        for j in i:
            v = ord(j)
            v -= ord('a')
            v += inc
            v %= (ord('z') - ord('a') + 1)
            v += ord('a')
            v = chr(v)
            out += v
        out += " "
    return out


for s in sys.stdin.readlines():
    if validate(s):
        i = id(s)
        plain = decode(s,i)
        if re.search('northpole', plain):
            print (plain, i)

