import sys

def execute_prog(p):
    pc = 0
    while p[pc] != 99:       
        if p[pc] == 1:
            p[p[pc+3]] = p[p[pc+1]] + p[p[pc+2]]
            pc +=4
        elif p[pc] == 2:
            p[p[pc+3]] = p[p[pc+1]] * p[p[pc+2]]
            pc +=4
        


for line in sys.stdin.readlines():
    line = list(map(int,line.split(",")))
    line[1] = 12
    line[2] = 2    
    execute_prog(line)    
    print(line[0])