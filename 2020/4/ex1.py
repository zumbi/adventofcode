import sys


def valid_passport(p):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # , "cid"]
    for f in fields:
        if f not in p:
            return 0
    return 1


passport = dict()
n_valid = 0
for line in sys.stdin.readlines():
    line = line.strip()
    if len(line) == 0:
        n_valid += valid_passport(passport)
        passport = dict()
        continue
    line = line.split(" ")
    for item in line:
        item = item.split(":")
        passport[item[0]] = item[1]

if len(passport):
    n_valid += valid_passport(passport)

print(n_valid)
