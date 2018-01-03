import sys


pos = [1,1]
keyb = [[1,2,3],[4,5,6],[7,8,9]]

mov = dict()
mov['U'] = [-1,0]
mov['D'] = [1,0]
mov['L'] = [0,-1]
mov['R'] = [0,1]

s = ""

for line in sys.stdin.readlines():
    for a in line[:-1]:
        m = mov[a]
        for i in range(2):
            pos[i] += m[i]
        for i in range(2):
            pos[i] = max(0,pos[i])
            pos[i] = min(2,pos[i])
    s += str(keyb[pos[0]][pos[1]])

print s

