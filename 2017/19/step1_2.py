import sys

dirs = [[1,0],[-1,0],[0,1],[0,-1]]
lines = sys.stdin.readlines()
letters = []

for i in range(len(lines)):
    lines[i] = list(lines[i][:-1])


def find_start():
    for i in range(len(lines[0])):
        if lines[0][i] == '|':
            return [0,i]

def move(pos, d):
    steps = 0

    while (True):
        if (pos[0] < 0) or (pos[0] >= len(lines)):
            break;

        if (pos[1] < 0 or pos[0]) >= (len(lines[0])):
            break;

        if lines[pos[0]][pos[1]] == ' ':
            break

        if lines[pos[0]][pos[1]] == '+':
            if dirs[d][0] == 0:
                nd = dirs[0:2]
                d2 =0
            else:
                nd = dirs[2:]
                d2 =2
            steps += 1
            for i in range(len(nd)):
                steps += move( [pos[0] + nd[i][0], pos[1] + nd[i][1]], i+d2)
            break


        if lines[pos[0]][pos[1]].isalpha():
            letters.append (lines[pos[0]][pos[1]])

        pos[0] += dirs[d][0]
        pos[1] += dirs[d][1]
        steps +=1
    return steps



pos = find_start()
s = move(pos,0)
print ''.join(letters)
print s
