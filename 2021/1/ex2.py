import sys

lines = sys.stdin.readlines()
numbers = list(map(int, lines))

n_bigger = 0
sum = 0
for i in range(len(numbers)):
    old_sum = sum
    if i > 2:
        sum -= numbers[i - 3]
    sum += numbers[i]
    if i > 2:
        if sum > old_sum:
            n_bigger += 1

print(n_bigger)
