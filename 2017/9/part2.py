import sys

def clean_line(l):
    mode = 0

    l = list(l)
    v =0

    for a in range(len(l)):
        if l[a] == "<" and mode == 0:
            mode = 1
            l[a] = " "
            continue
        if l[a] == ">" and mode == 1:
            mode = 0
            l[a] = " "
            continue
        if l[a] == "!" and mode == 1:
            mode = 2
            l[a] = " "
            continue
        if mode == 2:
            l[a] = " "
            mode = 1
            continue
        if mode > 0:
            l[a] = " "
            v+=1

    return v


for a in sys.stdin.readlines():
    a = clean_line(a)
    print a
