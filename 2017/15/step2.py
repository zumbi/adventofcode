

#A = 65
#B = 8921
A = 679
B = 771
A_mul = 16807
B_mul = 48271
mod = 2147483647

res = 0
for i in xrange(5000000):
    A *= A_mul
    A %= mod
    while (A & 0x3):
        A *= A_mul
        A %= mod
    B *= B_mul
    B %= mod
    while (B & 0x7):
        B *= B_mul
        B %= mod

    if (A & 0xffff) == (B & 0xffff):
        res +=1

print res
