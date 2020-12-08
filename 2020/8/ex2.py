import sys


def run_prog(code):
    acc = 0
    ip = 0
    visited = dict()
    n_lines = len(code)

    while ip not in visited and ip < n_lines:
        visited[ip] = True
        [ins, count] = code[ip].split()
        count = int(count)
        if ins == "nop":
            ip += 1
            continue
        elif ins == "acc":
            acc += count
            ip += 1
            continue
        elif ins == "jmp":
            ip += count
            continue
        else:
            print(code[ip])

    if ip == n_lines:
        return [True, acc]

    return [False, acc]


code = sys.stdin.readlines()

for i in range(len(code)):
    [ins, count] = code[i].split()
    old_code = code[i]
    if ins == "acc":
        continue
    if ins == "jmp":
        code[i] = code[i].replace("jmp", "nop")
    else:
        code[i] = code[i].replace("nop", "jmp")

    ret, acc = run_prog(code)
    if ret:        
        print(acc)
        sys.exit(0)

    code[i] = old_code
