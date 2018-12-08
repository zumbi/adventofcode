import sys

val = sys.stdin.readline()
val = map(int,val.split())

idx = 0
i = 0

nodes = dict()
todo = [1]
meta = [0]
node_id = [i]
parent_id = [None]
while len(todo):
    if todo[-1] == 0:
        todo = todo[0:-1]
        metadata = []
        for _ in range(meta[-1]):
            metadata = metadata + [val[idx]]
            idx += 1
        aux = dict()
        aux["meta"] = metadata
        aux["parent"] = parent_id[-1]
        aux["childs"] = []
        if node_id[-1] in nodes:
            print "error"
        nodes[node_id[-1]] = aux
        node_id = node_id[0:-1]
        parent_id = parent_id[0:-1]
        meta = meta[0:-1]
        continue
    todo[-1] -= 1
    todo += [val[idx]]
    idx += 1
    meta += [val[idx]]
    idx += 1
    parent_id += [node_id[-1]]
    i += 1
    node_id += [i]

del nodes[0]

#Invert
for n in nodes:
    parent = nodes[n]["parent"]
    if parent == 0:
        continue
    nodes[parent]["childs"] += [n]
    nodes[parent]["childs"].sort()


def cal_val(n):
    if len(nodes[n]["childs"]) == 0:
        return sum(nodes[n]["meta"])
    s = 0
    for c in nodes[n]["meta"]:
        if c > len(nodes[n]["childs"]):
            continue
        s += cal_val(nodes[n]["childs"][c-1])
    return s

#Step 1 (again)
s = 0
for n in nodes:
    s+=sum(nodes[n]["meta"])
print(s)

print cal_val(1)

