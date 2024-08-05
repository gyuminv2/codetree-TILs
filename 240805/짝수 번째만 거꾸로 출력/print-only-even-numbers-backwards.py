s = list(input())
s.reverse()

for i in range(len(s)):
    if len(s) % 2 == 0:
        if i % 2 == 0:
            print(s[i], end='')
    else:
        if i % 2 != 0:
            print(s[i], end='')