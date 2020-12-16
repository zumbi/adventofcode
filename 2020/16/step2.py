import sys


def in_fields(fields, val):
    for f in fields:
        if val in fields[f]:
            return True
    return False


fields = dict()
l = sys.stdin.readline()
while l != "\n":
    [name, data] = l.split(": ")

    d = set()
    for k in data.split(" or "):
        [start, end] = k.split("-")
        d |= set(range(int(start), int(end)+1))

    fields[name] = d
    l = sys.stdin.readline()

sys.stdin.readline()  # your ticket:
your_ticket = list(map(int, sys.stdin.readline().split(",")))

sys.stdin.readline()  # \n
sys.stdin.readline()  # nearby tickets:

nearby = list()
for l in sys.stdin.readlines():
    nearby.append(list(map(int, l.split(","))))


# cleanup
nearby_clean = list()
s = 0
for ticket in nearby:
    valid = True
    for t in ticket:
        if not in_fields(fields, t):
            valid = False
            break
    if valid:
        nearby_clean.append(ticket)

field_pos = ["unknown"] * len(your_ticket)
while "unknown" in field_pos:
    for f in fields:
        if f in field_pos:
            continue
        valid_pos = -1
        for idx in range(len(your_ticket)):
            if field_pos[idx] != "unknown":
                continue
            valid = True
            for ticket in nearby_clean:
                if ticket[idx] not in fields[f]:
                    valid = False
                    break
            if valid and valid_pos != -1:
                valid_pos = -1
                break
            if valid:
                valid_pos = idx

        if valid_pos != -1:
            # print(f,valid_pos)
            field_pos[valid_pos] = f

mval = 1
# print(field_pos)
for i in range(len(your_ticket)):
    if field_pos[i].startswith("departure"):
        mval *= your_ticket[i]

print(mval)
