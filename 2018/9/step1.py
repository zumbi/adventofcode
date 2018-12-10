import sys

def pos_rot(table, pos):
    while (pos < 0):
        pos += len(table)
    return pos % len(table)

def insert(table, pos, value):
    pos = pos_rot(table, pos)
    return table[0:pos] + [value] + table [pos:]

def remove(table, pos):
    pos = pos_rot(table, pos)
    post = pos_rot(table, pos+1)
    v = table[pos]
    return table[0:pos] + table [post:]


def calc_max(players, marbles):
    score = [0] * players
    table = [0]
    pos = 0
    for i in range(1,marbles+1):
        if (i % 23) != 0:
            pos = pos + 2
            pos = pos_rot(table, pos)
            table = insert(table, pos, i)
        if (i % 23) == 0:
            pos = pos - 7
            pos = pos_rot(table, pos)
            v = table[pos]
            table =  remove(table, pos)
            p = (i - 1) % players
            score[p] += i + v
    #print [table[-1]] + table [0:-1]
    return max(score)
for line in sys.stdin.readlines():
    line = line.split()
    players = int(line[0])
    marbles = int(line[6])
    print(calc_max(players,marbles))
