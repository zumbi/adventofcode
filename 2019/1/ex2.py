import sys


def fuel(n):
    n = n // 3
    n = max(0, n - 2)
    if n == 0:
        return 0
    return n + fuel(n)


s = 0
for n in sys.stdin.readlines():
    s = s + fuel(int(n))


print(s)
