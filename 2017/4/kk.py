import sys

n_val = 0
for line in sys.stdin:
    d = dict()
    valid = True
    for a in line.split():
        a = ''.join(sorted(a))
        if a in d:
            valid = False
            break
        d[a] = 1
    if (valid):
        n_val += 1

print n_val
