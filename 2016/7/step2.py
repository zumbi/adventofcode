import sys

ssl = 0
for l in sys.stdin.readlines():
    l = l[:-1]
    l = l.replace("["," ")
    l = l.replace("]"," ")
    l = l.split()
    even = l[::2]
    odd = l[1::2]

    isssl = False
    for word in even:
        for i in range(len(word)-2):
            w = word[i:i+3]
            if w[0] == w[1]:
                continue
            if w[0] != w[2]:
                continue
            w = w[1]+w[0]+w[1]
            for k in odd:
                if w in k:
                    isssl = True
                    break
            if isssl:
                break
    if isssl:
        ssl += 1

print ssl

