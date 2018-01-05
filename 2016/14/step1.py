import hashlib


h = dict()
def hash(n):

    if n in h:
        return h[n]

    #inp = "zpqevtbw"
    inp = "abc"
    m = hashlib.md5()
    m.update(inp+str(n))
    dig = m.hexdigest()
    h[n] = dig
    return dig

def n_in_h(n,rep):
    h = hash(n)
    out = []
    for i in h:
        s = i*rep
        if s in h:
            out += i
            if rep == 3:
                return out
    return list(set(out))

def trih(n):
    return n_in_h(n,3)

def quih(n):
    return n_in_h(n,5)

n = 0
keys =0

while keys < 65:
    tri = trih(n)
    iskey = False
    for t in tri:
        for i in range(1000):
            if t in quih(n+i+1):
                iskey = True
                #print (hash(n), hash(n+i+1))
                #print i
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
