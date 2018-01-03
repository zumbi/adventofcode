import sys

def compare(i1,i2):
    if i1[1] == i2[1]:
        return ord(i1[0]) - ord(i2[0])
    return i2[1] - i1[1]

def most_common(s):

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
    l = sorted(l, cmp=compare)
    return l[0][0]


cols = [""] * 64

for l in sys.stdin.readlines():
    for i in range(len(l)-1):
        cols[i] += l[i]

out = ""
for c in cols:
    out += most_common(c)

print out


