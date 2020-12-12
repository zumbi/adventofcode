import sys


pos = 0 + 0j
way = 10 + 1j

for order in sys.stdin.readlines():
    # print(order.strip())

    count = int(order[1:])
    ins = order[0]

    if ins == "L":
        count = -count
        count %= 360
        ins = "R"

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
    elif ins == "R":
        if count == 0:
            pass
        elif count == 90:
            way = complex(way.imag, way.real*-1)
        elif count == 180:
            way = complex(way.real*-1, way.imag*-1)
        elif count == 270:
            way = complex(way.imag*-1, way.real)

    #print(way, pos)

print(int(abs(pos.real) + abs(pos.imag)))
