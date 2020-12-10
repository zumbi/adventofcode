import sys

cache = dict()

def n_ways(numbers):

    if len(numbers) == 1:
        return 1
    if len(numbers) in cache:
        return cache[len(numbers)]
    ret = 0
    val = numbers[0]
    for i in range(1, 4):
        if (i >= len(numbers)):
            break
        if numbers[i] > (val + 3):
            break
        ret += n_ways(numbers[i:])
    cache[len(numbers)] = ret
    return ret


numbers = sys.stdin.readlines()
numbers = list(map(int, numbers))

numbers.append(0)
numbers.sort()
numbers.append(numbers[-1]+3)


print(n_ways(numbers))
