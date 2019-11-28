import sys

lines_read = sys.stdin.readlines()
lines = len(lines_read)
cols = len(lines_read[0])

roads = [['*'  for x in range(cols)] for y in range(lines)]

# > < ^ v
# L S R
direction = dict()
direction['>']  = [ '^', '>', 'v']
direction['<']  = [ 'v', '<', '^']
direction['^']  = [ '<', '^', '>']
direction['v']  = [ '>', 'v', '<']


movement = dict()
movement['>']  = [ 0, 1]
movement['<']  = [ 0,-1]
movement['^']  = [-1,0]
movement['v']  = [ 1,0]

transfers = dict()

t = dict()
t['>'] = 2
t['<'] = 2
t['^'] = 0
t['v'] = 0
transfers['\\'] = t

t = dict()
t['>'] = 0
t['<'] = 0
t['^'] = 2
t['v'] = 2
transfers['/'] = t

carts = list()
for i,l in enumerate(lines_read):
    for j,r in enumerate(l[:-1]):
        if r == '<' or r == '>' or r == 'v' or r == '^':
            carts += [[[i,j],r,0,0]]

        if r == '<' or r == '>' or r == '-':
            r = '-'

        if r == 'v' or r == '^' or r == '|':
            r = '|'
        roads[i][j] = r

#carts = [carts[0]]
while True:
    #delete crashed
    carts2 = list()
    for i in carts:
        if i[3] == 0:
            carts2 += [i]
    carts = carts2
    #sort
    carts = sorted(carts, key=lambda s: s[0][0]*10000 + s[0][1])
    for i in range(len(carts)):
        print(carts[i][0][1],carts[i][0][0])

    n_del = 0
    for i,c in enumerate(carts):

        #stop condition
        if i == (len(carts) -1) and crashed == len(carts)-1:
            print(pos[1], ",", pos[0])
            sys.exit(0)

        #move
        pos = c[0].copy()
        for j in range(2):
            pos[j] += movement[c[1]][j]

        #crash
        crashed = carts[i][3]
        for j,crash in enumerate(carts):
            if pos == crash[0] and crash[3] == 0 and i != j:
                crashed = 1
                carts[i][3] = 1
                carts[j][3] = 1

        mov = 1
        cros = c[2]
        #new movement
        r = roads[pos[0]][pos[1]]
        if r in transfers:
            mov = transfers[r][c[1]]
        elif r == '+':
            mov = c[2]
            cros = (c[2] + 1) % 3

        mov = direction[c[1]][mov]
        carts[i] = [pos,mov,cros,crashed]
        n_del += crashed


print(roads)

