import sys


def valid_passport(p):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # , "cid"]

    for f in fields:
        if f not in p:
            return 0
        val = p[f]

        if f == "byr":
            val = int(val)
            if val < 1920 or val > 2002:
                return 0
            continue
        if f == "iyr":
            val = int(val)
            if val < 2010 or val > 2020:
                return 0
            continue
        if f == "eyr":
            val = int(val)
            if val < 2020 or val > 2030:
                return 0
            continue
        if f == "hgt":
            unit = val[-2:]
            val = val[:-2]
            if not val.isnumeric():
                return 0
            val = int(val)

            if unit == "cm":
                if val < 150 or val > 193:
                    return 0
            elif unit == "in":
                if val < 59 or val > 76:
                    return 0
            else:
                return 0

            continue
        if f == "hcl":
            if val[0] != '#':
                return 0
            val = val[1:]
            if len(val) != 6:
                return 0
            for v in val:
                if v not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    return 0
            continue

        if f == "ecl":
            if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return 0
            continue

        if f == "pid":
            if len(val) != 9:
                return 0
            for v in val:
                if v not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
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
