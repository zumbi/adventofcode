import sys
from collections import deque

def calc_max(max_players, last_marble):
    scores = dict()
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            p = marble % max_players
            if p not in scores:
                scores[p] = 0
            scores[p] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values())

for line in sys.stdin.readlines():
    line = line.split()
    players = int(line[0])
    marbles = int(line[6])
    print(calc_max(players,marbles*100))
