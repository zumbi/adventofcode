
N=3012210
#31682 is too low
#N=5
#N=20
elves = [(i+1) for i in range(N)]

i = 0
while len(elves)>1:
    l = len(elves)
    if l%1000 == 0:
        print l
    d = (i + l//2) % l
    elves.pop(d)
    if (d>i):
        i += 1
    if i >= (l-1):
        i = 0
print(elves)





