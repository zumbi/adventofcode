import sys

move = [[1,0], [0,1], [-1,0], [0, -1]]

pos = [0,0]
d = 0

steps = sys.stdin.readline()[:-1].split(', ')
visited = []

for s in steps:
    if s[0] == 'L':
        d +=1
    else :
        d +=3
    d %= 4
    n = int(s[1:])

    for i in range(n):
        pos[0] += move[d][0]
        pos[1] += move[d][1]
        if pos in visited:
            print "already visited:"
            print (abs(pos[0]) + abs(pos[1]))
            sys.exit(0)
        visited += [pos[:]]

print "end"
print (abs(pos[0]) + abs(pos[1]))

