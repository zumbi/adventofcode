import sys

DISTANCE = int(sys.argv[1])

coords = dict()

get_m = list()
idx = 0
for l in sys.stdin.readlines():
    l = l.split(", ")
    coords[idx] = [int(l[0]), int(l[1])]
    get_m +=[int(l[0]), int(l[1])]
    idx += 1

MAX = max(get_m) + 1

def sum_distances(point, coords):
    s_d = 0
    for c in coords:
        s_d += abs(coords[c][0] - point[0]) + abs(coords[c][1] - point[1])
        #Optiminzation
        if s_d >= DISTANCE:
            break
    return s_d

n_val = 0
for line in range(MAX):
    for col in range(MAX):
        if sum_distances([line,col], coords) < DISTANCE:
            n_val +=1

print(n_val)
