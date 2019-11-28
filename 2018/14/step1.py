import sys

r =  [3,7]
elf = [0,1]
dest = int(sys.argv[1])
while (len(r) < (9+dest+1)):
    s = r[elf[0]] + r[elf[1]]
    if s >= 10:
        r += [1]
        r += [s - 10]
    else:
        r += [s]
    for i,e in enumerate(elf):
        elf[i] = (1 + r[e] + e) % len(r)

for i in r[dest:dest+9+1]:
    print(i, end="")
print()
