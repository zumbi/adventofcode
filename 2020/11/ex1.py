import sys
import copy


def cycle(seats):
    oldseats = copy.deepcopy(seats)
    changed = False
    for i in range(1, len(oldseats)-1):
        for j in range(1, len(oldseats[i])-1):
            n_L = 0
            n_H = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if ii == 0 and jj == 0:
                        continue
                    if oldseats[i+ii][j+jj] == "#":
                        n_H += 1
                    if oldseats[i+ii][j+jj] == "L":
                        n_L += 1
            if oldseats[i][j] == "L":
                if n_H == 0:
                    seats[i][j] = "#"
                    changed = True
            if oldseats[i][j] == "#":
                if n_H >= 4:
                    seats[i][j] = "L"
                    changed = True
    return changed


seats = list()
for l in sys.stdin.readlines():
    seats.append(["."] + list(l.strip()) + ["."])

border = ["."] * len(seats[0])
seats = [border] + seats + [border]

while (cycle(seats)):
    pass

occupied = 0
for i in seats:
    for j in i:
        if j == "#":
            occupied += 1

print(occupied)
