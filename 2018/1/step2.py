import sys

s = 0
d = dict()
d[s] = True

lines = sys.stdin.readlines()

while True:
    for l in lines:
       s += int(l)
       if s in d:
           print(s)
           sys.exit(0)
       d[s] = True

