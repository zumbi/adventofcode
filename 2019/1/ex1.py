import sys

s = 0
for n in sys.stdin.readlines():
    n = int(n) // 3
    n = max(0, n - 2)
    s += n

print(s)
