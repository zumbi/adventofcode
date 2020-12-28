import sys


def find_dest(planets,vin, tr):
    #print(vin,tr)
    v = vin[:]
    fr = v[-1]
    if fr == tr:
        return v
    if fr not in planets:
        return None
    for p in planets[fr]:        
        v2 = find_dest(planets,v + [p],tr)
        if v2:
             return v2
    return None
        

planets = dict()
for l in sys.stdin.readlines():
    l = l.strip()
    [fr, to] = l.split(")")
    if fr not in planets:
        planets[fr] = []
    planets[fr].append(to)

you = set(find_dest(planets,["COM"], "YOU"))
san = set(find_dest(planets,["COM"], "SAN"))
unique = (you | san) - (you & san)
print(len(unique)-2)
