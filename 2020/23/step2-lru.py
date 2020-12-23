import sys
from collections import deque
import pickle


L = 1000000

def add_offset(val,offsets):
    val %= L - 4
    if val in offsets:
        #print("hit",val)
        offsets.remove(val)
    else:
        #print("miss",val)
        pass
    offsets = [val] + offsets
    return offsets[:32]    

def find_val(last_offsets, last_index, val, cups): 
    for j in last_offsets:
        r = last_index + j
        r %= L - 4       
        if cups[r]==val:
            return [add_offset(r-last_index,last_offsets),r]
    
    r = list(cups).index(val)
    return [add_offset(r-last_index,last_offsets),r]    

def move(cups, last_index, last_offset):
    first = cups.popleft()
    three = [cups.popleft(), cups.popleft(), cups.popleft()]    
    p = -1
    
    start = first    
    while start in three + [first]:       
        start = ((start - 2) % L) + 1 
    [last_offset,p] = find_val(last_offset, last_index,start,cups)

    for i in range(len(three)):
        cups.insert(p+1+i, three[i])
    cups.append(first)
    
    return [cups,p,last_offset]

def calc_res(cups):    
    [one, _] = list(cups).index(1) 
    out = cups[(one + 1)%L]
    out *= cups[(one + 2)%L]    
    return (out)

def launch(step, cups):
    last_index = 0
    last_offset = []
    while(step<10000000):
        if (step%10000 ==0):
            print(step)        
            f = open("kkk-lru",'wb')
            pickle.dump([step,cups], f)
        [cups, last_index, last_offset] = move(cups,last_index,last_offset)
        step += 1
    print(calc_res(cups))
    return
    

if (len(sys.argv) == 2):
    f = open(sys.argv[1],'rb')
    step,cups = pickle.load(f)
    launch(step, cups)    
    sys.exit(0)


cups = list(map(int,list(sys.stdin.readline().strip())))
for i in range(len(cups) + 1,1000000 + 1):
    cups.append(i)
cups = deque(cups)
launch(0,cups)
sys.exit(0)

#if len(sys.argv) > 1:
    