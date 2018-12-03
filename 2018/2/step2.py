import sys

def common(wordA,wordB):
    st = ""
    for i in range(len(wordA)):
        if wordA[i] == wordB[i]:
            st = st + wordA[i]

    return st

def n_diff(wordA,wordB):
    diff = 0
    for i in range(len(wordA)):
        if wordA[i] != wordB[i]:
            diff += 1;
        if diff >= 2:
            break;
    if diff == 1:
        return True
    return False

lines =  sys.stdin.readlines()
n_lines = len(lines)

for i in range(len(lines)):
    for j in range(i + 1,n_lines):
        if n_diff(lines[i],lines[j]):
            print(common(lines[i],lines[j]))
