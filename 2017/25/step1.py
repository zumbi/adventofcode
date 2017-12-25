


def step(state):
    st = state[0]
    pos = state[1]
    lis = state[2]

    cur = lis[pos]

    if st == 'A':
        if cur == 0:
            lis[pos] = 1
            pos+=1
            st = 'B'
        else :
            lis[pos] = 0
            pos+=1
            st = 'C'
    elif st == 'B':
        if cur == 0:
            lis[pos] = 0
            pos-=1
            st = 'A'
        else :
            lis[pos] = 0
            pos+=1
            st = 'D'
    elif st == 'C':
        if cur == 0:
            lis[pos] = 1
            pos+=1
            st = 'D'
        else :
            lis[pos] = 1
            pos+=1
            st = 'A'
    elif st == 'D':
        if cur == 0:
            lis[pos] = 1
            pos-=1
            st = 'E'
        else :
            lis[pos] = 0
            pos-=1
            st = 'D'
    elif st == 'E':
        if cur == 0:
            lis[pos] = 1
            pos+=1
            st = 'F'
        else :
            lis[pos] = 1
            pos-=1
            st = 'B'
    elif st == 'F':
        if cur == 0:
            lis[pos] = 1
            pos+=1
            st = 'A'
        else :
            lis[pos] = 1
            pos+=1
            st = 'E'

    if pos == -1:
        lis = [0] + lis
        pos = 0
    elif pos == len(lis):
        lis = lis + [0]
    return [st, pos, lis]

st = 'A'
pos = 0
lis = [0]
state = [st, pos, lis]
for i in xrange(12368930):
    state = step(state)

print state

print sum(state[2])
