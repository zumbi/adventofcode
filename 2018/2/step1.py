import sys

def count_2_3(word):
    d = dict()
    n_2 = 0
    n_3 = 0
    for l in word:
        if l not in d:
            d[l] = 0;
        d[l] += 1
    for l in d:
        if d[l] == 2:
            n_2 += 1
        if d[l] == 3:
            n_3 += 1
    return (n_2, n_3)

n_2 = 0
n_3 = 0

#print(count_2_3("bababc"))
#sys.exit(0)

for l in sys.stdin.readlines():
    (a,b) = count_2_3(l)
    if (a >= 1):
        n_2 += 1;
    if (b >= 1):
        n_3 += 1;

print(n_2 * n_3)
