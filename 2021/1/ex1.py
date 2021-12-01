import sys

lines = sys.stdin.readlines()
numbers = list(map(int, lines))

n_bigger = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        n_bigger += 1

print(n_bigger)
