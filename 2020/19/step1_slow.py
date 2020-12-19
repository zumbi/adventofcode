import sys


def valid_strings(rules, r):
    todo = r
    done = []
    len_t = 0
    while len(todo) > 0:
        if (len(todo) % 10000) == 0:
            print(len(todo))
        t = todo[0]
        todo = todo[1:]
        if len(t) > len_t:
            len_t = len(t)
            print(len_t)
        if len(t) > 96:
            print("TM")
            continue
        is_done = True
        for i in range(len(t)):
            if t[i] == "a" or t[i] == "b":
                continue
            for r in rules[t[i]]:
                nt = t[:i]+r+t[i+1:]
                todo.append(nt)
            is_done = False
            break
        if is_done:
            done.append(t)

    out = list()
    for d in done:
        out.append("".join(d))

    return list(set(out))


rules = dict()

l = sys.stdin.readline().strip()
while l != "":
    [name, data] = l.split(":")
    data = data.split("|")
    r = list()
    for d in data:
        d = d.split()
        ou = []
        for o in d:
            if o == '"a"':
                ou.append("a")
            elif o == '"b"':
                ou.append("b")
            else:
                ou.append(int(o))
        r.append(ou)

    rules[int(name)] = r

    l = sys.stdin.readline().strip()

valid_s = valid_strings(rules, rules[0])
# print(valid_s)

nmatch = 0
tests = list()
for l in sys.stdin.readlines():
    if l.strip() in valid_s:
        nmatch += 1
print("nvalid", len(valid_s))
print("res", nmatch)
