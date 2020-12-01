import sys

TOTAL = 2020

numbers = sys.stdin.readlines()
numbers = list(map(int, numbers))
numbers_hash = dict()
for n in numbers:
    numbers_hash[n] = True

for n in numbers:
    total = TOTAL - n

    for n2 in numbers:
        if n2 == n:
            continue
        n3 = total - n2
        if n3 == n2:
            continue
        if n3 in numbers_hash:
            print(n*n2*n3)
            sys.exit(0)
