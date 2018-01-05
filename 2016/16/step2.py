
inp = "10111011111001111"
length = 35651584

def step(s):
    a = s
    b = a[::-1]
    b= b.replace("0","a").replace("1","0").replace("a","1")
    return a + "0" + b

def csum_s(s):
    print len(s)
    out = ["0"] * (len(s)/2)
    for i in range(0,len(s),2):
        if s[i]==s[i+1]:
            out[i/2] = "1"
    return ''.join(out)

while len(inp)<length:
    print len(inp)
    inp = step(inp)

inp = inp[:length]

while (len(inp) % 2) ==0:
    print len(inp)
    inp = csum_s(inp)

print inp
