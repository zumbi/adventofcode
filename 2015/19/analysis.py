import sys


convert = dict()
def e2n(h):
    if h not in convert:
        convert[h] = len(convert)
    return convert[h]

def string2n(s):
    o = []
    i = 0
    while i<len(s):
        if (i+1)<len(s) and s[i+1].islower():
            o+=[e2n(s[i:i+2])]
            i+=2
        else:
            o+=[e2n(s[i:i+1])]
            i+=1
    return o


lines = sys.stdin.readlines()
start = string2n(lines[-1][:-1])

print "len"
print len(start)
print "Rn"
print start.count(e2n("Rn"))
print "Ar"
print start.count(e2n("Ar"))
print "Y"
print start.count(e2n("Y"))

print len(start)-start.count(e2n("Rn"))-start.count(e2n("Ar"))-2*start.count(e2n("Y"))-1


