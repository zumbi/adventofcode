import sys


def process_list(l, idx):
    acc = 0
    op = "+"
    while idx < len(l):
        if l[idx] == ")":
            return acc, idx

        if l[idx] in "+*":
            op = l[idx]
            idx += 1
            continue

        if l[idx] == "(":
            val, idx = process_list(l, idx+1)
        else:
            val = int(l[idx])
        if op == '+':
            acc += val
        else:
            acc *= val
        idx += 1
    return acc, idx


def process_string(st):
    s2 = ""
    for s in st:
        if s in "()":
            s2 += " "
        s2 += s
        if s in "()":
            s2 += " "

    s2 = s2.split()
    a, b = process_list(s2, 0)
    print(a)
    return(a)


s = 0
for l in sys.stdin.readlines():
    s += process_string(l)
print(s)
