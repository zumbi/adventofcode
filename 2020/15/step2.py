import sys


def sim(ns):
    backlog = dict()
    idx = 0
    for i in ns:
        backlog[i] = [idx]
        idx += 1
        last = i

    while idx < 30000000:
        if len(backlog[last]) < 2:
            new_val = 0
        else:
            new_val = backlog[last][0] - backlog[last][1]
        if new_val in backlog:
            backlog[new_val] = [idx, backlog[new_val][0]]
        else:
            backlog[new_val] = [idx]
        last = new_val
        idx += 1
    return(last)


for l in sys.stdin.readlines():
    l = list(map(int, l.split(",")))
    print(sim(l))
