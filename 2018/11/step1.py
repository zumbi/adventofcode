import sys
import numpy as np

LEN = 300
SQUARE = 3
serial = int(sys.argv[1])

def calc_table(serial):
    table = np.zeros((LEN, LEN),dtype=np.int)
    for line in range(LEN):
        for col in range(LEN):
            rack_id = line + 10
            power = rack_id * col
            power += serial
            power *= rack_id
            power //= 100
            power %= 10
            power -=5
            table[line,col] = power
    return table

table = calc_table(serial)

pos = None
val = 0

for line in range(LEN-SQUARE+1):
    for col in range(LEN-SQUARE+1):
        t0 = table[line:line+SQUARE,col:col+SQUARE]
        s = t0.sum()
        if pos == None or s > val:
            pos = [line , col]
            val = s

print(pos)
