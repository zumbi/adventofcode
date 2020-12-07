import sys
import re

bag = dict()
for line in sys.stdin.readlines():
    line = line.strip()[:-1]
    [name, content] = line.split(" bags contain ")
    bag[name] = []
    if content == "no other bags":
        continue
    for c in content.split(","):
        m = re.search(r'([0-9]+)\s(.*)\sbag[s]*$', c)
        bag[name].append([m.group(2), int(m.group(1))])


def visit(name):
    n_bags = 1
    for b in bag[name]:
        n_bags += b[1] * visit(b[0])
    return n_bags


print(visit("shiny gold")-1)
