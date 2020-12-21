import sys

alergens = dict()
products = list()


for l in sys.stdin.readlines():
    [p, al] = l.split("(contains ")
    al = al[:-2]
    al = al.split(", ")
    p = p.split()

    products += p
    for a in al:
        if a not in alergens:
            alergens[a] = set(p)
        else:
            alergens[a] &= set(p)

# print(alergens)
# print(products)

p_empty = products[:]
for a in alergens:
    for p in alergens[a]:
        p_empty[:] = (value for value in p_empty if value != p)
print("step1:", len(p_empty))


alergens_ready = dict()
while len(alergens) > 0:
    for a in list(alergens.keys()):
        if len(alergens[a]) != 1:
            continue
        p = alergens[a].pop()
        alergens_ready[a] = p
        del alergens[a]
        for aa in alergens:
            alergens[aa] -= set([p])

res = []
for a in sorted(alergens_ready.keys()):
    res += [alergens_ready[a]]

print("step2:", ",".join(res))
