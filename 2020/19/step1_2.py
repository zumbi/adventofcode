import sys


def can_match(rule, matches):
    for m in matches:
        if len(rule) > len(m):
            continue
        are_same = True
        for i in range(len(rule)):
            if rule[i] != "a" and rule[i] != "b":
                return True
            if rule[i] != m[i]:
                are_same = False
                break
        if are_same:
            return True
    return False


def n_valid_strings(rules, r, matches):
    matches = matches[:]
    n_matches_in = len(matches)
    todo = r
    done = []
    while len(todo) > 0:
        t = todo[0]
        todo = todo[1:]
        if not can_match(t, matches):
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
            s_out = "".join(t)
            done.append(s_out)
            if s_out in matches:
                matches.remove(s_out)

    return n_matches_in - len(matches)


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


nmatch = 0
matches = list()
for l in sys.stdin.readlines():
    matches.append(l.strip())

print("res_step1", n_valid_strings(rules, rules[0], matches))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print("res_step2", n_valid_strings(rules, rules[0], matches))
