import sys

start = [0, 0]
slope = []
for line in sys.stdin.readlines():
    slope.append(list(line[:-1]))

n_trees = 0
n_cols = len(slope[0])
n_lines = len(slope)
while start[0] != n_lines:
    if slope[start[0]][start[1]] == '#':
        n_trees += 1
    start[0] += 1
    start[1] = (start[1] + 3) % n_cols
print(n_trees)
