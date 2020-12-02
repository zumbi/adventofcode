import sys


def validate(char_min, char_max, char, pwd):
    pwd = list(pwd)
    count = pwd.count(char)
    if count >= char_min and count <= char_max:
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