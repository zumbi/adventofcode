import sys

blocks = sys.stdin.read()[:-1].split("\n\n")


players = list()
for b in blocks:
    lines = b.split("\n")
    n = int(lines[0][:-1].split()[1])
    cards = list(map(int, lines[1:]))
    players.append(cards)

while (len(players[1]) > 0):
    if players[0][0] < players[1][0]:
        players = players[::-1]
    cards = [players[0][0], players[1][0]]
    players[0] = players[0][1:] + cards
    players[1] = players[1][1:]

res = 0
idx = 1
for p in players[0][::-1]:
    res += idx * p
    idx += 1

print(res)
