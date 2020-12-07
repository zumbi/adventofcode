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
        bag[name].append([m.group(2), m.group(1)])


visited = set()
todo = ['shiny gold']

while len(todo) > 0:
    t = todo[0]
    todo = todo[1:]
    if t in visited:
        continue
    visited.add(t)
    for k in bag.keys():
        b = bag[k]
        for c in b:
            if c[0] == t and k not in visited:
                todo.append(k)

print(len(visited)-1)
