import sys

#s = "abcde"
s = "abcdefgh"
n = "01234567"

n = list(n)
s = list(s)

for l in sys.stdin.readlines():
    #print l[:-1]
    #print n
    #print s
    l = l[:-1].split(" ")
    if l[0] == "swap":
        if l[1] == "position" :
            p0 = int(l[2])
            p1 = int(l[5])
        else :
            p0 = s.index(l[2])
            p1 = s.index(l[5])
        aux = s[p0]
        s[p0] = s[p1]
        s[p1] = aux
    if l[0] == "rotate" and l[1] != "based":
        idx = int(l[2])
        idx %= len(s)
        if l[1] == "right":
            idx *= -1
        s = s[idx:] + s[:idx]
    if l[0] == "rotate" and l[1] == "based":
        idx = s.index(l[6])
        if idx >=4:
            idx += 2
        else:
            idx += 1
        idx %= len(s)
        idx *= -1
        s = s[idx:] + s[:idx]
    if l[0] == "reverse":
        p0 = min(int(l[2]),int(l[4]))
        p1 = max(int(l[2]),int(l[4]))
        inv = -(len(s) - p0) -1
        #print inv
        s = s[0:p0] + s[p1:inv:-1] + s[p1+1:]
    if l[0] == "move":
        p0 = int(l[2])
        p1 = int(l[5])
        aux = s.pop(p0)
        s.insert(p1,aux)
    #print s

print ''.join(s)



