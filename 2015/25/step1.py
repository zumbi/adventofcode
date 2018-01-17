line = 3010
column = 3019

def position(line,column):
    p = [0,0]
    i = 0
    while  p != [line,column]:
        if p[0] == 0:
            p = [p[1]+1,0]
        else:
            p[0] -=1
            p[1] +=1
        i += 1
    return i

n = position(line-1,column-1)
print n
p = 20151125
i = 0

while i<n:
    p *= 252533
    p %= 33554393
    i+=1

print p
