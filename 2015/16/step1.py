import sys

props = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
        }

for l in sys.stdin.readlines():
    l = l[:-1].split(", ")
    l0 = l[0].split(" ")
    l[0] = " ".join(l0[2:])

    aunt = True
    for p in l:
        p = p.split(": ")
        if props[p[0]] != int(p[1]):
            aunt = False
            break
    if aunt:
        print int(l0[1][:-1])
        break
