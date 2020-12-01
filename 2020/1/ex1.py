import sys

TOTAL = 2020
numbers = dict()

while True:
    n = int(sys.stdin.readline())
    if (TOTAL - n) in numbers:
        print(n * (TOTAL - n))
        sys.exit(0)
    numbers[n] = True
