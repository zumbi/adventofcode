
inp = "10111011111001111"
length = 272

def step(s):
    a = s
    b = a[::-1]
    b= b.replace("0","a").replace("1","0").replace("a","1")
    return a + "0" + b

def csum_s(s):
    out = ""
    for i in range(0,len(s),2):
        if s[i]==s[i+1]:
            out += "1"
        else:
            out += "0"
    return out


while len(inp)<length:
    inp = step(inp)

inp = inp[:length]

while (len(inp) % 2) ==0:
    inp = csum_s(inp)

print inp
