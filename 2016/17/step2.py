import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return  m.hexdigest()

pos = [[-1,0],[1,0],[0,-1],[0,1]]
names = "UDLR"
p = [0,0]
start = "qzthpkfp"
n = start

s = [n,p]
jobs = [s]

maxl = 0
while len(jobs):
    s = jobs[0]
    jobs = jobs[1:]

    n = s[0]
    p = s[1]
    if p == [3,3]:
        path = n[len(start):]
        maxl= len(path)
        continue

    h = md5(n)
    for i in range(4):
        if h[i].isdigit() or h[i] == 'a':
            continue
        isout = False
        p2 = p[:]
        for j in range(2):
            p2[j]= p[j] + pos[i][j]
            if p2[j]<0 or p2[j]>3:
                isout = True
                break
        if isout:
            continue
        s2 = [n+names[i],p2]
        jobs = jobs + [s2]

print maxl
