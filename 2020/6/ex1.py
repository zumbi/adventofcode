import sys

count = 0
letters = set()
for line in sys.stdin.readlines():
    line = line.strip()

    if len(line) == 0:
        count += len(letters)
        letters = set()
        continue
    letters |= set(line)


print(count)
