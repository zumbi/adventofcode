import sys

horses = dict()

#speed, time, rest
for l in sys.stdin.readlines():
    l = l.split()
    v = map(int,[l[3],l[6],l[-2]])
    horses[l[0]] = v

points = [0] * len(horses)

time = 2503

def distance(time, horse):
    d = 0
    cycles = time / (horse[1] + horse[2])
    d += cycles * (horse[1]  * horse[0])
    steps = time % (horse[1] + horse[2])
    if steps > horse[1]:
        steps = horse[1]
    d += steps * horse[0]
    return d

for i in range(1,time+1):
    d = []
    for h in horses:
        d += [distance(i, horses[h])]
    m = max(d)
    for i in range(len(d)):
        if d[i] == m:
            points[i] +=1

print max(points)

