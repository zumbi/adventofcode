import sys

def clean_line(l):
    mode = 0

    l = list(l)

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
        if mode > 0:
            l[a] = " "

    return ''.join(l)



def ev_line(l):
    dep = 0
    val = 0

    for a in l:
        if a == '{':
            dep +=1
        if a == '}':
            val += dep
            dep -=1
    return val


for a in sys.stdin.readlines():
    a = clean_line(a)
    v = ev_line(a)
    print v
