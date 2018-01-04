import sys

#C = 7
#L = 3
C = 50
L = 6
screen = []
for i in range(L):
    screen +=  [[0] * C]

for l in sys.stdin.readlines():

    for i in screen:
        print i
    print l

    l = l.split(" ")
    if l[0] == "rect":
        coord =  l[1].split('x')
        c = int(coord[0])
        l = int(coord[1])
        for i in range(l):
            for j in range(c):
                screen[i][j] = 1
        continue

    if l[1] == "row":
        row = int(l[2].split("=")[1])
        n = int(l[4])
        screen[row] = screen[row][-n:] + screen[row][0:-n]
        continue

    if l[1] == "column":
        s = [row[:] for row in screen]
        col = int(l[2].split("=")[1])
        n = int(l[4])
        for i in range(L):
            screen[(i+n)%L][col] = s[i][col]
        continue



for i in screen:
    print i

on = 0
for i in screen:
    for j in i:
        on +=j
print on

