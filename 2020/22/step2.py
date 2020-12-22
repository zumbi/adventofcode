import sys
import copy

blocks = sys.stdin.read()[:-1].split("\n\n")


def winner(players):
    if players[0][1][0] < len(players[0][1]) and players[1][1][0] < len(players[1][1]):
        players_copy = []
        for p in players:
            pc = copy.deepcopy(p)
            pc[1] = pc[1][1:pc[1][0]+1]
            players_copy.append(pc)
        return playcards(players_copy)[0][0]
    if players[0][1][0] > players[1][1][0]:
        return players[0][0]
    return players[1][0]


def playcards(players):
    history = []
    while (len(players[1][1]) > 0):
        # print(len(players[0][1])+len(players[1][1]))
        # for p in players:
        #    print(p)
        if (players[0][1] in history) or (players[1][1] in history):
            if players[1][0] == 1:
                return [players[1], players[0]]
            return [players[0], players[1]]

        if winner(players) != players[0][0]:
            players = players[::-1]
        history += [players[0][1], players[1][1]]
        cards = [players[0][1][0], players[1][1][0]]
        players[0][1] = players[0][1][1:] + cards
        players[1][1] = players[1][1][1:]
    return players


players = list()
for b in blocks:
    lines = b.split("\n")
    n = int(lines[0][:-1].split()[1])
    cards = list(map(int, lines[1:]))
    players.append([n, cards])

players = playcards(players)

res = 0
idx = 1
for p in players[0][1][::-1]:
    res += idx * p
    idx += 1

print(res)
