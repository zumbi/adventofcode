import sys


def get_min(step):
    m = None
    for s in step:
        if len(step[s]) != 0:
            continue
        if m == None or s < m:
            m = s
    return m


step = dict()
for l in sys.stdin.readlines():
    l = l.split()
    a = l[1]
    b = l[7]
    for k in [a, b]:
        if k not in step:
            step[k] = dict()
    step[b][a] = None

res = []
while (len(step) > 0):
    m = get_min(step)
    res += m
    del step[m]
    for s in step:
        if m in step[s]:
            del step[s][m]

print(''.join(res))
