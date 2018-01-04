#61 and 17
import sys


bots= []
vals= []
done = []
for i in range(1256):
    bots += [[-1,-1]]
    vals += [[]]
    done += [False]


for l in sys.stdin.readlines():
    l = l.split(" ")
    if l[0] ==  'bot':
        v0 = int(l[6])
        if l[5] == "output":
            v0 += 1000
        v1 = int(l[11])
        if l[10] == "output":
            v1 += 1000
        bots[int(l[1])] = [v0,v1]
    if l[0] == 'value':
        vals[int(l[5])] = sorted(vals[int(l[5])] + [int(l[1])])

move = True
while(move):
    move = False
    for i in range(256):
        if len(vals[i]) == 2 and not done[i]:
            for j in range(2):
                vals[bots[i][j]] = sorted(vals[bots[i][j]] + [vals[i][j]])
            done[i] = True
            move = True

print "step 1"
print vals.index([17,61])
print "step 2"
o = 1
for a in vals[1000:1003]:
    o*=a[0]
print o
