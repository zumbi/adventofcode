import sys

l = sys.stdin.readline()

print "Step 1"
print l.count('(') - l.count(')')

print "Step 2"
step = 0
pos = 0
for c in l:
    step +=1
    if c == '(':
        pos += 1
    if c == ')':
        pos -= 1

    if pos < 0:
        print step
        break
