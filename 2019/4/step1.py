
n = 0
for i in range(246515, 739105):
    s = list(map(int, str(i)))
    isValidDouble = False
    isValidIncrease = True
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            isValidDouble = True
        if s[i] < s[i-1]:
            isValidIncrease = False

    if isValidDouble and isValidIncrease:
        n += 1

print(n)
