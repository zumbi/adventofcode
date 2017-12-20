import sys


lines = sys.stdin.readlines()

def dist(a):
    return abs(a[0]) +  abs(a[1]) + abs(a[2])

n = 0
p = list()
for l in lines:
    l =l[:-1].split(", ")
    a = dict()
    a["n"] = n
    a["p"] = map(int,l[0][3:-1].split(","))
    a["v"] = map(int,l[1][3:-1].split(","))
    a["a"] = map(int,l[2][3:-1].split(","))
    a["d1"] = dist(a["p"])
    a["d0"] = a["d1"] + 1 #Fake going towards the center
    p.append(a)
    n+=1

def step(p):
    p["v"][0] += p["a"][0]
    p["v"][1] += p["a"][1]
    p["v"][2] += p["a"][2]

    p["p"][0] += p["v"][0]
    p["p"][1] += p["v"][1]
    p["p"][2] += p["v"][2]

    p["d0"] = p["d1"]
    p["d1"] = dist(p["p"])
    if p["d1"] >= p["d0"] :
        return 1
    return 0

n_away = 0
while (n_away != len(p)):
    n_away =0
    for i in p:
        n_away += step(i)

    for i in range(len(p)):
        dels = [1] #dummy
        while i < (len(p)-1):
            dels = list()
            p_i = p[i]["p"]
            for j in range(i+1, len(p)):
                if p[j]["p"] == p_i:
                    dels += [i,j]
            if len(dels) == 0:
                break
            dels=list(set(dels))
            dels.sort(reverse=True)
            for a in dels:
                del p[a]

print len(p)
