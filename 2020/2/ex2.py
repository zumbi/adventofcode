import sys


def validate(char_min, char_max, char, pwd):
    pwd = list(pwd)
    if pwd[char_min - 1] == char and not pwd[char_max - 1] == char:
        return True
    if not pwd[char_min - 1] == char and pwd[char_max - 1] == char:
        return True
    return False


count = 0
for line in sys.stdin.readlines():
    [header, tail] = line[:-1].split(": ")
    [min_max, char] = header.split(" ")
    [char_min, char_max] = min_max.split("-")
    char_min = int(char_min)
    char_max = int(char_max)

    if validate(char_min, char_max, char, tail):
        count = count + 1

print(count)