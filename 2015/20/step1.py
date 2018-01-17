inp = 34000000

max_h = 1000000

house = [0] * max_h

for i in xrange(1,max_h):
    h = i
    while h<max_h:
        house[h] += 10*i
        h += i

for i in xrange(len(house)):
    if house[i] >= inp:
        print i
        break

