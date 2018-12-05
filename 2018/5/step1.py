import sys

def find_dup(s):
    l = list()
    erased = False
    for i in range(len(s)-1):
        if erased:
            erased = False
            continue
        if (str.lower(s[i]) == str.lower(s[i + 1])) and (str.islower(s[i]) != str.islower(s[i + 1])):
            l += [i, i+1]
            erased = True

    return l

line = sys.stdin.readline()[:-1]
letters = list(line)

while True:
    dup = find_dup(letters)

    if len(dup) == 0:
        break

    for i in sorted(dup, reverse=True):
        del letters[i]

line = ''.join(letters)


print(len(line))
