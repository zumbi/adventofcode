import sys

pos = list()
speed = list()


def parse_pos(v):
    return int(v[2:])


def pot(v):
    p = 0
    for i in v:
        p += abs(i)
    return p


def step(pos, speed):
    for i in range(len(pos)):
        for j in range(len(pos)):
            if j == i:
                continue
            for k in range(len(pos[i])):
                if pos[i][k] > pos[j][k]:
                    speed[i][k] -= 1
                elif pos[i][k] < pos[j][k]:
                    speed[i][k] += 1

    for i in range(len(pos)):
        for k in range(len(pos[i])):
            pos[i][k] += speed[i][k]


for l in sys.stdin.readlines():
    l = l.strip()
    l = l[1:-1]
    l = l.split(", ")
    l = list(map(parse_pos, l))
    pos.append(l)
    speed.append([0]*len(l))

for i in range(1000):
    step(pos, speed)

power = 0
for i in range(len(pos)):
    power += pot(pos[i]) * pot(speed[i])


print(power)
