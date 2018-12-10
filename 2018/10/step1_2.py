import sys

signals = list()
speeds = list()

pos = []
for l in sys.stdin.readlines():
    l  = l.split(">")
    l0 = map(int, l[0].split("=<")[1].split(", "))
    l1 = map(int, l[1].split("=<")[1].split(", "))
    signals += [l0]
    speeds += [l1]
    pos += l0

def get_area(signals):
    lines = [item[0] for item in signals]
    cols = [item[1] for item in signals]
    return abs(max(lines)-min(lines)) * abs(max(cols)-min(cols))

def step_area(signals,speeds,count):
    moves = list()
    for s in range(len(signals)):
        x = signals[s][0] + count * speeds[s][0]
        y = signals[s][1] + count * speeds[s][1]
        moves += [[x,y]]
    return moves

def print_area(signals):
    cols = [item[0] for item in signals]
    lines = [item[1] for item in signals]

    min_lines = min(lines)
    lines = [l - min_lines  for l in lines]
    min_cols = min(cols)
    cols = [c - min_cols  for c in cols]

    data = [["." for x in range(max(cols)+1)] for y in range(max(lines)+1)]

    for s in range(len(cols)):
        data[lines[s]][cols[s]] = "#"

    for d in data:
        print(d)


old_a = get_area(signals)
i = 1
while True:
    m = step_area(signals,speeds, i)
    a = get_area(m)
    if a>old_a:
        break
    old_a = a
    i += 1

m = step_area(signals,speeds, i-1)
print_area(m)
print(i-1)

