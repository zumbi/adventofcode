import sys

s = sys.stdin.readlines()
s = map(int, s)
pos = 0
step = 0


while pos>=0 and pos<len(s):
    step +=1
    jmp = s[pos]
    if jmp >=3:
        s[pos] -=1
    else:
        s[pos] +=1
    pos += jmp

print step
