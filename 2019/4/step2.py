
n = 0
for number in range(246515, 739105):
    s = list(map(int, str(number)))
    isValidDouble = False
    isValidIncrease = True
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            isValidIncrease = False
        if s[i] != s[i-1]:
            continue
        if i > 1 and s[i] == s[i-2]:
            continue
        if i < (len(s) - 1) and s[i] == s[i+1]:
            continue
        isValidDouble = True

    if isValidDouble and isValidIncrease:
        # print(number)
        n += 1

print(n)
