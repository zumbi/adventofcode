import sys


def count_trees(slope, movement):
    start = [0, 0]
    n_trees = 0
    n_cols = len(slope[0])
    n_lines = len(slope)
    while start[0] < n_lines:
        if slope[start[0]][start[1]] == '#':
            n_trees += 1
        start[0] += movement[0]
        start[1] = (start[1] + movement[1]) % n_cols
    return n_trees


slope = []
for line in sys.stdin.readlines():
    slope.append(list(line[:-1]))

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

total = 1
for mov in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
    total *= count_trees(slope, mov)
print(total)
