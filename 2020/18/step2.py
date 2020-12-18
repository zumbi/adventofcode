import sys


def reduce_p(l):
    ol = []
    idx = 0
    while(idx < len(l)):
        if l[idx] != ")":
            ol.append(l[idx])
            idx += 1
            continue
        i = -2
        while ol[i] != "(":
            i -= 1
        val = process_list(ol[i+1:])
        ol = ol[:i]
        ol.append(val)

        idx += 1

    return ol


def reduce_op(l, op):
    ol = []
    idx = 0
    while idx < len(l):
        if l[idx] == op:
            if op == "+":
                val = int(ol[-1])+int(l[idx+1])
            else:
                val = int(ol[-1])*int(l[idx+1])
            ol[-1] = val
            idx += 2
            continue
        ol.append(l[idx])
        idx += 1

    return ol


def process_list(l):
    # print(l)
    l = reduce_p(l)
    l = reduce_op(l, "+")
    l = reduce_op(l, "*")

    return(l[0])


def process_string(st):
    s2 = ""
    for s in st:
        if s in "()":
            s2 += " "
        s2 += s
        if s in "()":
            s2 += " "

    s2 = s2.split()
    a = process_list(s2)
    print(a)
    return(a)


s = 0
for l in sys.stdin.readlines():
    s += process_string(l)
print(s)
