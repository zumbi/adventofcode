
N=3012210
#N=5
elves = [(i+1) for i in range(N)]

i = 0
while len(elves)>1:
    if (len(elves) % 2) == 0:
        elves = elves[::2]
    else:
        elves = elves[2::2]
print elves





