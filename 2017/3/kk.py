import sys

inp = int(sys.argv[1])
MAX = 11
C = MAX / 2

a = [[0 for _ in range(MAX)] for _ in range(MAX)]

a[C][C] = 1
dirs = ((0,1),(-1,0),(0,-1),(1,0))

d1 = 0
count = 1
p = [C,C]
n = 0

def p_a(a):
    print("")
    print('\n'.join([''.join(['{:7}'.format(item) for item in row])  for row in a]))
    print("")

while True:
    for d in range(len(dirs)):
        print count
        for c in range(count):
            p[0] += dirs[d][0]
            p[1] += dirs[d][1]
            v = 0;
            for x in range(3):
                for y in range(3):
                    v += a[p[0]+x-1][p[1]+y-1]
            print p
            a[p[0]][p[1]] = v
            p_a(a)
            if (v > inp):
                print(v)
                sys.exit(0)
        if d % 2 == 1:
            count += 1

