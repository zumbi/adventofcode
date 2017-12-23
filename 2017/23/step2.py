import sys

print "#include <stdio.h>"
print "int main() {"
for a in range(ord('a'), ord('h')+1):
    print "int %s = 0;" % chr(a)

print "a = 1;"
idx = -1
for l in sys.stdin.readlines():
    idx +=1;
    print "s%d:" % idx
    if idx == 32:
        print 'printf("a=%d b=%d c=%d d=%d e=%d f=%d g=%d h=%d\\n",a,b,c,d,e,f,g,h);'
    l = l[:-1].split(" ")
    if l[0] == "set":
        print "%s = %s;" % (l[1],l[2])
    elif l[0] == "sub":
        print "%s -= %s;" % (l[1],l[2])
    elif l[0] == "mul":
        print "%s *= %s;" % (l[1],l[2])
    elif l[0] == "jnz":
        #print 'printf("step = %d\\n");' % idx
        #print 'printf("a=%d b=%d c=%d d=%d e=%d f=%d g=%d h=%d\\n",a,b,c,d,e,f,g,h);'
        print "if (%s)" % l[1]
        print "  goto s%d;" % (idx + int(l[2]))

print "s32:"
print "s33:"
print 'printf("%d\\n", h);'
print "return 0;"
print "}"

