import sys


def neighbour(address):
    n = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    n.add((address[0]+i, address[1]+j,
                           address[2]+k, address[3]+l))
    n.remove(address)
    return(n)


def cycle(actives):
    inactives = set()
    for a in actives:
        inactives |= neighbour(a)
    inactives -= actives

    output = set()
    for a in actives:
        n_a = neighbour(a) & actives
        if len(n_a) in [2, 3]:
            output.add(a)

    for i in inactives:
        n_i = neighbour(i) & actives
        if len(n_i) == 3:
            output.add(i)

    return output


actives = set()
idx = 0
for line in sys.stdin.readlines():
    for l in range(len(line)):
        if line[l] == "#":
            actives.add(tuple([idx, l, 0, 0]))
    idx += 1

# print(actives)
for i in range(6):
    actives = cycle(actives)
    # print(len(actives),actives)
print(len(actives))
