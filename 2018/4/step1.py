import sys

def date_num(a):
    a = a.split('] ')
    a = a[0]
    a = a.replace(" ","")
    a = a.replace("[","")
    a = a.replace(":","")
    a = a.replace("-","")
    return int(a)

def date_cmp(a,b):
    return date_num(a) - date_num(b)

#Sort lines
lines = sys.stdin.readlines()
lines = sorted(lines, cmp=date_cmp)


for l in lines:
    print l
