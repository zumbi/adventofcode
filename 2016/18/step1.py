import sys

lines = 40
is_trap = [[False,False,True],[True,False,False],[False,True,True],[True,True,False]]
line = sys.stdin.readline()[:-1]
safes = [i=="." for i in line]

s = sum(safes)
for lines in range(lines-1):
 safes2= [True] * len(safes)
 for i in range(len(safes)):
    tri = [True, True, True]
    if i != 0:
        tri[0] = safes[i-1]
    tri[1] = safes[i]
    if i != (len(safes)-1):
        tri[2] = safes[i+1]
    if tri in is_trap:
        safes2[i] = False
 safes = safes2
 s += sum(safes)

print s
