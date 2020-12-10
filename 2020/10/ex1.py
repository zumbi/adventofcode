import sys

numbers = sys.stdin.readlines()
numbers = list(map(int, numbers))

numbers.append(0)
numbers.sort()
numbers.append(numbers[-1]+3)

diff_1 = 0
diff_3 = 0

for i in range(1, len(numbers)):
    diff = numbers[i] - numbers[i-1]
    if diff == 1:
        diff_1 += 1
    if diff == 3:
        diff_3 += 1

print(diff_1*diff_3)
