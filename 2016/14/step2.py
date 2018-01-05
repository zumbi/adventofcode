import hashlib

h = dict()

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return  m.hexdigest()

def hash(n):

    if n in h:
        return h[n]

    inp = "zpqevtbw"+str(n)
    #inp = "abc"+str(n)

    for i in range(2017):
        inp = md5(inp)
    h[n] = inp
    return inp

def n_in_h(n,rep):
    h = hash(n)
    out = []
    for i in h:
        s = ""
        for j in range(rep):
            s += i
        if s in h:
            out += i
            if rep == 3:
                return out
    return list(set(out))

def trih(n):
    return n_in_h(n,3)

qu = dict()
def quih(n):
    if n in qu:
        return qu[n]
    q = n_in_h(n,5)
    qu[n] = q
    return q

n = 0
keys =0

while keys < 64:
    tri = trih(n)
    iskey = False
    for t in tri:
        for i in range(1000):
            if t in quih(n+i+1):
                iskey = True
                #print (hash(n), hash(n+i+1))
                break
            if iskey:
                break
        if iskey:
            break
    if iskey:
        keys +=1
        print (keys, n)

    n+=1

print n-1
