import sys
import cmath


pos = 0 + 0j
way = 10 + 1j

for order in sys.stdin.readlines():
    # print(order.strip())

    count = int(order[1:])
    ins = order[0]

    if ins == "N":
        way += count * (0+1j)
    elif ins == "S":
        way += count * (0-1j)
    elif ins == "E":
        way += count * (1+0j)
    elif ins == "W":
        way += count * (-1+0j)
    elif ins == "F":
        pos += count * way
    elif ins == "R" or ins == "L":
        if ins == "L":
            count = -count
        count %= 360
        count = (2 * cmath.pi * count) / 360
        (r, ang) = cmath.polar(way)
        ang -= count
        way = cmath.rect(r, ang)

    #print(way, pos)

print(round(abs(pos.real) + abs(pos.imag)))
