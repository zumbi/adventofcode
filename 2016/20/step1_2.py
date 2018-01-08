import sys


ranges = []

for l in sys.stdin.readlines():
    l = l.split("-")
    v = [int(l[0]),int(l[1])]
    if v[0] > v[1]:
        print v
    ranges += [v]

def compare(i1,i2):
    return i1[0] - i2[0]

ranges = sorted(ranges, cmp=compare)
merged = True
while merged:
    r2 = []
    i = 0
    merged = False
    while i < len(ranges):
        if (i != (len(ranges)-1)) and (ranges[i+1][0] <= (ranges[i][1]+1)):
            r2 += [[ranges[i][0],max(ranges[i][1],ranges[i+1][1])]]
            i+=2
            merged = True
            continue
        r2 += [ranges[i]]
        i+=1
    ranges = r2

print "step 1"
print ranges[0][1] + 1

total = 4294967295 + 1

print "step 2"
for i in ranges:
    total -= i[1] - i[0] + 1
print total
