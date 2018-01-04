import sys

def isana(s):
    if s[0] != s[1] and s[0] == s[3] and s[1] == s[2]:
        return True
    return False

tsl = 0
for l in sys.stdin.readlines():
    n = 0
    skip = False
    istsl=False
    for i in range(len(l)):
        if l[i] == '[':
            skip = True
            n = 0
            continue
        if l[i] == ']':
            skip = False
            n = 0
            continue
        n += 1
        if n>=4 and isana(l[i-3:i+1]):
            if skip:
                istsl=False
                break
            else :
                istsl=True
    if istsl:
        tsl +=1
print tsl

