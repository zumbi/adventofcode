import sys

def move(cups):
    first = cups[0]
    three = cups[1:4]    
    cups = cups[4:]    
    
    start = first
    while start not in cups:        
        start = ((start - 2) % 10) + 1
    p = cups.index(start)
    cups = cups[:p+1] + three + cups[p+1:] + [first]
    return cups

def print_res(cups):
    one = cups.index(1)
    out = cups[one+1:] + cups[:one]
    out = list(map(str,out))
    print("".join(out))
        

cups = list(map(int,list(sys.stdin.readline().strip())))
#print(cups)

for i in range(100):
    cups = move(cups)
    #print(cups)

print_res(cups)