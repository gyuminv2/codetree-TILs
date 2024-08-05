s = list(input())
s.reverse()

for i in range(len(s)):
    if i % 2 == 0:
        print(s[i], end='')