import sys

sub =0
for l in sys.stdin.readlines():
    if (int(l) % 17) == (105700 % 17):
        sub +=1
        print int(l)

print 1001-sub
