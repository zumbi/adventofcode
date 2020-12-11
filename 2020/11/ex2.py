import sys
import copy


def pseats(seats):
    for se in seats:
        print(se)


def cycle(seats):
    oldseats = copy.deepcopy(seats)
    changed = False
    for i in range(0, len(oldseats)):
        for j in range(0, len(oldseats[i])):
            if oldseats[i][j] == ".":
                continue
            n_L = 0
            n_H = 0
            for vect in [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (-1, 0), (1, 0)]:
                lenght = 0
                while(True):
                    lenght += 1
                    ni = i + lenght * vect[0]
                    nj = j + lenght * vect[1]
                    if ni < 0 or ni >= len(oldseats) or nj < 0 or nj >= len(oldseats[i]):
                        break
                    if oldseats[ni][nj] == ".":
                        continue
                    if oldseats[ni][nj] == "#":
                        n_H += 1
                    if oldseats[nj][nj] == "L":
                        n_L += 1
                    break
            if oldseats[i][j] == "L":
                if n_H == 0:
                    seats[i][j] = "#"
                    changed = True
            if oldseats[i][j] == "#":
                if n_H >= 5:
                    seats[i][j] = "L"
                    changed = True
    return changed


seats = list()
for l in sys.stdin.readlines():
    seats.append(list(l.strip()))


# pseats(seats)
while (cycle(seats)):
    # pseats(seats)
    pass

occupied = 0
for i in seats:
    for j in i:
        if j == "#":
            occupied += 1
pseats(seats)
print(occupied)
