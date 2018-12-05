import sys
import string

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

def react(letters):
    while True:
        dup = find_dup(letters)

        if len(dup) == 0:
            return letters

        for i in sorted(dup, reverse=True):
            del letters[i]


line = sys.stdin.readline()[:-1]
res = dict()
for l in list(string.ascii_lowercase):
    letters = list(line)
    letters = [i for i in letters if str.lower(i) != l]
    letters = react(letters)
    res[l] = len(letters)

print(min(res.values()))
