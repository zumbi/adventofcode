import sys

def compare(i1,i2):
    if i1[1] == i2[1]:
        return ord(i1[0]) - ord(i2[0])
    return i2[1] - i1[1]

def histogram(s):

    if len(s) == 0:
        return ""

    d = dict()
    for i in s:
        for j in i:
            if j in d:
                d[j] +=1
            else:
                d[j] =1
    l = list()
    for key, value  in d.iteritems():
        l += [[key,value]]
    return sorted(l, cmp=compare)


cols = [""] * 64

for l in sys.stdin.readlines():
    for i in range(len(l)-1):
        cols[i] += l[i]

most = ""
less = ""
for c in cols:
    if len(c) == 0:
        break;
    h = histogram(c)
    most += h[0][0]
    less += h[-1][0]

print most
print less


