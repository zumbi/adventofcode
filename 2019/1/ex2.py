import sys

fuel_cache = dict()
def fuel(in_n):
    if in_n in fuel_cache:
        return fuel_cache[in_n]
    n = in_n // 3
    n = max(0, n - 2)
    if n == 0:
        fuel_cache[in_n] = 0
    else:
        fuel_cache[in_n] = n + fuel(n)
    return fuel_cache[in_n]


s = 0
for n in sys.stdin.readlines():
    s = s + fuel(int(n))


print(s)
