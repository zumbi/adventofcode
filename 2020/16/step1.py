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


s = 0
for ticket in nearby:
    for t in ticket:
        if not in_fields(fields, t):
            s += t

print(s)
