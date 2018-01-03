import sys

move = [[1,0], [0,1], [-1,0], [0, -1]]

pos = [0,0]
d = 0

steps = sys.stdin.readline()[:-1].split(', ')

for s in steps:
    if s[0] == 'L':
        d +=1
    else :
        d +=3
    d %= 4
    n = int(s[1:])

    pos[0] += n * move[d][0]
    pos[1] += n * move[d][1]

print (abs(pos[0]) + abs(pos[1]))

