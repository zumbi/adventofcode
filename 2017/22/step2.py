import sys

N = 1000

def debug(L, p):
    print("")
    L[p[0]][p[1]] +=10
    print('\n'.join([''.join(['{:3}'.format(item) for item in row])  for row in L]))
    L[p[0]][p[1]] -=10


inp = list()
for l in sys.stdin.readlines():
    l = list(l[:-1])
    r = [ (int(i=='#') * 2) for i in l ]
    inp += [r]

arr = [[0] * N for i in range(N)]
s = N / 2  - len(inp) / 2
for i in range(len(inp)):
    for j in range(len(inp)):
        arr[s+i][s+j] = inp[i][j]

pos = [N/2,N/2]
mov = [[-1,0],[0,-1],[1,0],[0,1]]
d = 0

c = 0
for a in range(10000000):
    if (a % 1000000) == 1:
        print a
    #debug(arr,pos)
    if arr[pos[0]][pos[1]] == 0:
        d = (d + 1) % 4
    elif arr[pos[0]][pos[1]] == 1:
        c += 1
    elif arr[pos[0]][pos[1]] == 2:
        d = (d + 3) % 4
    elif arr[pos[0]][pos[1]] == 3:
        d = (d + 2) % 4
    arr[pos[0]][pos[1]] = (arr[pos[0]][pos[1]]+1)%4
    pos[0] += mov[d][0]
    pos[1] += mov[d][1]

print c
