import hashlib

def md5(s):
    m = hashlib.md5()
    m.update(s)
    return  m.hexdigest()

found5 = False
n=-1
while True:
    n +=1
    s = "yzbqklnj" + str(n)
    h = md5(s)
    if h[0:5] == "00000" and not found5:
        print(n)
        found5 = True
    if h[0:6] == "000000":
        print(n)
        break
