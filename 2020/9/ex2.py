import sys

TARGET = 41682220
#TARGET = 127

numbers = sys.stdin.readlines()
numbers = list(map(int, numbers))

for i in range(len(numbers)):
    sum = numbers[i]
    for j in range(i+1, len(numbers)):
        sum += numbers[j]
        if sum == TARGET:
            print(min(numbers[i:j+1])+max(numbers[i:j+1]))
            sys.exit(0)
        if sum > TARGET:
            break
