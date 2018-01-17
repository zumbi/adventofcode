inp = 34000000

max_h = 1000000

house = [0] * max_h

for i in xrange(1,max_h):
    h = i
    p = 0
    while h<max_h and p<50:
        house[h] += 11*i
        h += i
        p +=1

for i in xrange(len(house)):
    if house[i] >= inp:
        print i
        break

