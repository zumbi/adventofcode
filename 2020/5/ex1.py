import sys


def pos2int(p):
    p = p.translate(str.maketrans("FBLR", "0101"))
    p = int(p,2)
    return p


max_n = 0
for line in sys.stdin.readlines():
    n = pos2int(line)
    print(n)
    if n > max_n:
        max_n = n

print(max_n)
