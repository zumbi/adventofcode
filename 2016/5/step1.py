import hashlib
import sys

n = 0
i = 0
out = ""
while (n<8):
    txt = "%s%05d" % (sys.argv[1], i)
    i +=1
    m = hashlib.md5()
    m.update(txt)
    dig = m.hexdigest()
    if dig[:5] == '00000':
        out += dig[5]
        n+=1
        print(out)
print(out)

