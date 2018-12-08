import sys

WORKERS = 10
TIME = 60

def get_min(step,work):
    m = None
    for s in step:
        if len(step[s]) != 0:
            continue
        if (m == None or s < m) and not s in work:
            m = s
    return m

def del_val(step, val):
    m = val
    del step[m]
    for s in step:
        if m in step[s]:
            del step[s][m]

step = dict()
for l in sys.stdin.readlines():
    l = l.split()
    a = l[1]
    b = l[7]
    for k in [a, b]:
        if k not in step:
            step[k] = dict()
    step[b][a] = None

workers = WORKERS * [0]
work = WORKERS * ['*']
wall = 0
while (len(step) > 0) or sum(workers)!=0:
    for w in range(len(workers)):
        if workers[w] != 0:
            workers[w] -= 1
            continue
        m = get_min(step,work)
        if m == None:
            continue
        workers[w] += ord(m) - ord('A') + TIME
        work[w] = m
    #Delete finished workers
    for w in range(len(workers)):
        if workers[w] == 0 and work[w] != "*":
            del_val(step, work[w])
            work[w] = "*"
    wall += 1

print(wall)
