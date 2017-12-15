

#A = 65
#B = 8921
A = 679
B = 771
A_mul = 16807
B_mul = 48271
mod = 2147483647

res = 0
for a in xrange(40000000):
    A *= A_mul
    A %= mod
    B *= B_mul
    B %= mod

    if (A & 0xffff) == (B & 0xffff):
        res +=1

print res
