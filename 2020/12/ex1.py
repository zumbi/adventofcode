import sys

facing = [1+0j, 0-1j, -1+0j, 0+1j]
f = 0
pos = 0 + 0j

for order in sys.stdin.readlines():

    count = int(order[1:])
    ins = order[0]

    if ins == "L" or ins == "R":
        if count % 90:
            print("not integer move")
        count = count // 90

    if ins == "N":
        pos += count * (0+1j)
    elif ins == "S":
        pos += count * (0-1j)
    elif ins == "E":
        pos += count * (1+0j)
    elif ins == "W":
        pos += count * (-1+0j)
    elif ins == "F":
        pos += count * facing[f]
    elif ins == "L":
        f = (f - count) % len(facing)
    elif ins == "R":
        f = (f + count) % len(facing)
    #print(f, pos)

print(int(abs(pos.real) + abs(pos.imag)))
