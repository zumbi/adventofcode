import sys

val = sys.stdin.readline()
val = map(int,val.split())

idx = 0

s = 0
todo = [1]
meta = [0]
while len(todo):
    if todo[-1] == 0:
        todo = todo[0:-1]
        for i in range(meta[-1]):
            s += val[idx]
            idx += 1
        meta = meta[0:-1]
        continue
    todo[-1] -= 1
    todo += [val[idx]]
    idx += 1
    meta += [val[idx]]
    idx += 1

print(s)
