import sys

def defrag(l):
    m = max(l)
    s = l.index(m)
    inc = m // len(l)
    rest = m%len(l)
    l[s] = 0

    for i in range(len(l)):
        p = (i + s + 1) % len(l)
        l[p] += inc
        if rest > 0:
            l[p] +=1
            rest -=1

    return l

mem = sys.stdin.readline()
mem = mem.split()
mem = list(map(int, mem))

h = list()

step = 0
while not mem in h:
    h.append(mem)
    step +=1
    mem = defrag(mem[:])


print(step)

l = h.index(mem)
print(step - l)

