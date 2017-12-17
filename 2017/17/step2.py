
inc = 376
pos = 1
steps = 50000000 -1

pos0 = 0
valadd = 1
for i in xrange(steps):
    curr_len = i + 2
    pos = (pos + inc + 1) % curr_len
    if pos <= pos0:
        pos0 = (pos0+1) % curr_len
    if pos == ((pos0+1) % curr_len):
        valadd = curr_len

print valadd

