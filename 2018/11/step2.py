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

def calc_max(serial, square):
    table = calc_table(serial)

    pos = None
    val = 0
    for line in range(LEN-square+1):
        for col in range(LEN-square+1):
            t0 = table[line:line+square,col:col+square]
            s = t0.sum()
            if pos == None or s > val:
                pos = [line , col]
                val = s
    return [pos, val]


res_max = calc_max(serial, LEN)
id_max = LEN
for i in range(1,LEN-1):
    print(i)
    resN = calc_max(serial, i)
    if resN[1] > res_max[1]:
        id_max = i
        res_max = resN
        print(res_max)

print(res_max[0] + [id_max])


