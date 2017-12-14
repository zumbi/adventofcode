import sys

n_sum = 0
for line in sys.stdin:
    l = line.split()
    done = False
    for a in range(len(l)):
        if done:
            break
        v1 = int(l[a])
        for b in range(a + 1, len(l)):
            v2 = int(l[b])
            M = max(v1,v2)
            m = min(v1,v2)
            if (M % m) == 0:
                n_sum += M / m
                done = True
                break
print n_sum
