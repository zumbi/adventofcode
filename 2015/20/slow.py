inp = 34000000

def pre(h):
    i = 1
    n = 0
    while i <= h:
        if (h%i)==0:
            n += 10*i
        i+=1
    return n

def min_h(n):
    i =1
    while n>0:
        n-=10*i
        i+=1
    return i


n = min_h(inp)
v = 1
while v < inp:
    n +=1
    v = pre(n)
    print [n,v]
