import sys


def pos2int(p):
    p = p.translate(str.maketrans("FBLR", "0101"))
    p = int(p,2)
    return p


pos = list()
for line in sys.stdin.readlines():
    pos.append(pos2int(line))

pos.sort()

for i in range(1,len(pos)-1):
    if pos[i+1] == pos[i] + 2:
        print(pos[i]+1)
        sys.exit(0)
