import sys


def calc_distance(distance, planets, orig, n):
    distance[orig] = n
    if orig not in planets:
        return
    for p in planets[orig]:
        calc_distance(distance, planets, p, n+1)


planets = dict()
for l in sys.stdin.readlines():
    l = l.strip()
    [fr, to] = l.split(")")
    if fr not in planets:
        planets[fr] = []
    planets[fr].append(to)

distance = dict()
calc_distance(distance, planets, "COM", 0)
# print(distance)

dist = 0
for d in distance:
    dist += distance[d]

print(dist)
