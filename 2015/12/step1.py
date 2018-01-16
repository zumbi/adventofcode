import sys

l = sys.stdin.readline()

su = 0
i=0
while i < len(l):
    if l[i].isdigit():
        j = i
        while j<len(l) and l[j].isdigit():
            j+=1
        n = int(l[i:j])
        if l[i-1] == '-':
            n *= -1
        su += n
        i = j-1
    i +=1

print su
