import sys

N = 1000

def debug(L, p):
    L[p[0]][p[1]] +=10
    print('\n'.join([''.join(['{:3}'.format(item) for item in row])  for row in L]))
    L[p[0]][p[1]] -=10


inp = list()
for l in sys.stdin.readlines():
    l = list(l[:-1])
    r = [ int(i=='#') for i in l ]
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
for a in range(10000):
    #debug(arr,pos)
    if arr[pos[0]][pos[1]] == 1:
        #print "clean"
        d = (d + 3) % 4
        arr[pos[0]][pos[1]] = 0
    else:
        #print "infect"
        c += 1
        d = (d + 1) % 4
        arr[pos[0]][pos[1]] = 1
    pos[0] += mov[d][0]
    pos[1] += mov[d][1]

print c
