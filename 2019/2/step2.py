import sys


def execute_prog(p):
    pc = 0
    while p[pc] != 99:
        if p[pc] == 1:
            p[p[pc+3]] = p[p[pc+1]] + p[p[pc+2]]
            pc += 4
        elif p[pc] == 2:
            p[p[pc+3]] = p[p[pc+1]] * p[p[pc+2]]
            pc += 4


def find_noun_verb(prog, res):
    for noun in range(100):
        for verb in range(100):
            p = prog[:]
            p[1] = noun
            p[2] = verb
            execute_prog(p)
            # print(noun,verb)
            if p[0] == res:
                return(noun*100+verb)


for line in sys.stdin.readlines():
    line = list(map(int, line.split(",")))
    print(find_noun_verb(line, 19690720))
