
inc = 376
pos = 1
steps = 2017 -1
l = [0,1]

for i in xrange(steps):
    curr_len = i + 2
    pos = (pos + inc + 1) % curr_len
    l = l[:pos] + [curr_len] + l[pos:]


#print l[pos-1:pos+2]
#print l.index(0)
#print  l[l.index(0)+1]
print l[(pos+1)%(i+3)]

