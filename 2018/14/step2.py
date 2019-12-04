import sys

def to_str(l):
    return str(l)[1:-1]

r =  [3,7]
elf = [0,1]
dest = list(sys.argv[1])
dest = to_str([int(i) for i in dest])
count = 0
while True:
    count += 1
    s = r[elf[0]] + r[elf[1]]
    if s >= 10:
        r += [1]
        r += [s - 10]
    else:
        r += [s]
    for i,e in enumerate(elf):
        elf[i] = (1 + r[e] + e) % len(r)
    if (count%100000 == 0):
        print(count)
        if dest in to_str(r):
            break

print(to_str(r).find(dest)//3)
