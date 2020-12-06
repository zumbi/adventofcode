import sys
import string

count = 0
letters = set(string.ascii_lowercase)
for line in sys.stdin.readlines():
    line = line.strip()

    if len(line) == 0:
        count += len(letters)
        letters = set(string.ascii_lowercase)
        continue
    letters &= set(line)


print(count)
