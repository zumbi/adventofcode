import sys

code = sys.stdin.readlines()

acc = 0
ip = 0
visited = dict()

while ip not in visited:
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

print(acc)
