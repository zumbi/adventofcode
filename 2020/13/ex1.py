import sys

target = int(sys.stdin.readline())
all_buses = sys.stdin.readline()
all_buses = all_buses.split(",")
buses = list()
for b in all_buses:
    if b != "x":
        buses.append(int(b))

min_t = target

for b in buses:
    t = (-1 * target) % b
    if t < min_t:
        min_t = t
        retv = b * t


print(retv)
