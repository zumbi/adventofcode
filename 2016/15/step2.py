#Disc #1 has 17 positions; at time=0, it is at position 1.
#Disc #2 has 7 positions; at time=0, it is at position 0.
#Disc #3 has 19 positions; at time=0, it is at position 2.
#Disc #4 has 5 positions; at time=0, it is at position 0.
#Disc #5 has 3 positions; at time=0, it is at position 0.
#Disc #6 has 13 positions; at time=0, it is at position 5.

mod = [17,7,19,5,3,13,11]
s = [1,0,2,0,0,5,0]

t = 0
while True:
    fail = False
    for i in range(len(mod)):
        if (s[i]+t+i+1) % mod[i] != 0:
            fail = True
            break
    if not fail:
        print t
        break
    t +=1
