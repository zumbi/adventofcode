import sys

coords = dict()

get_m = list()
idx = 0
for l in sys.stdin.readlines():
    l = l.split(", ")
    coords[idx] = [int(l[0]), int(l[1])]
    get_m +=[int(l[0]), int(l[1])]
    idx += 1

MAX = max(get_m) + 1

def get_distances(point, coords):
    dists = dict()
    for c in coords:
        dists[c] = abs(coords[c][0] - point[0]) + abs(coords[c][1] - point[1])
    return dists

#get distances for all points
distances = dict()
for line in range(MAX):
    for col in range(MAX):
        distances[line*MAX + col] = get_distances([line,col], coords)

def get_min(distance):
    vals = list(distance.values())
    maxs = vals[:]
    maxs.sort()
    if maxs[0] == maxs[1]:
        return None
    keys = list(distances[d].keys())
    return keys[vals.index(maxs[0])]

#get sum of winners
win = dict()
for c in coords:
    win[c] = 0
for d in distances:
    m = get_min(distances[d])
    if m != None:
        win[m] += 1

#remove points in the border
for line in range(MAX):
    for col in [0, MAX-1]:
        m = get_min(distances[line * MAX + col])
        if m != None and m in win:
            del win[m]
for col in range(MAX):
    for line in [0, MAX-1]:
        m = get_min(distances[line * MAX + col])
        if m != None and m in win:
            del win[m]

print(max(win.values()))
