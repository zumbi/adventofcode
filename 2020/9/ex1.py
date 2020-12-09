import sys

N_ELEM = 25
#N_ELEM = 5


def validate(num, nlist):
    inlist = dict()
    for v in nlist:
        if v in inlist:
            return False
        inlist[v] = True
        if (num - v) in inlist:
            return True
    return False


numbers = sys.stdin.readlines()
numbers = list(map(int, numbers))

for i in range(N_ELEM, len(numbers)):
    if not validate(numbers[i], numbers[i-N_ELEM:i]):
        print(numbers[i])
        sys.exit(0)
