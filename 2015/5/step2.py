import sys

def nice(s):

    bwin = False
    pair = False
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            bwin = True
        if pair and bwin:
            return True
        for j in range(i+2,len(s)-1):
            if s[i] == s[j] and s[i+1] == s[j+1]:
                pair = True
                break
        if pair and bwin:
            return True

    return False

c = 0
for l in sys.stdin.readlines():
    if nice(l):
        c += 1

print c
