import hashlib
import sys

n = 0
i = 0
out = ['_'] * 8
done = [0] * 8
while 0 in done:
    txt = "%s%05d" % (sys.argv[1], i)
    i +=1
    m = hashlib.md5()
    m.update(txt)
    dig = m.hexdigest()
    if dig[:5] == '00000':
        if not dig[5].isdigit():
            continue
        pos = int(dig[5])
        if pos > 7:
            continue
        if done[pos] != 0:
            continue
        out[pos]= dig[6]
        done[pos]= 1
        print(out)
print(''.join(out))

