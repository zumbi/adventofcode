import sys

M = 20201227

def expon(s, p):
    r = p
    i = 1

    while i != s:
        r *= p
        r %= M
        i += 1
    return r


def invert(base, target):
    r = base
    n = 1
    while (r != target):
        r *= base
        r %= M
        n += 1

    return n


p0, p1 = list(map(int, sys.stdin.readlines()))
s0 = invert(7, p0)
s1 = invert(7, p1)

print(expon(s0, p1))
print(expon(s1, p0))

print((p1**s0) % M)
print((p0**s1) % M)
