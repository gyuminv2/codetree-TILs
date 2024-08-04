n = int(input())
a = list(map(int, input().split()))

s = 0
for i in range(len(a)):
    if a[i] == 2:
        s += 1
    if s == 3:
        s = i+1
        break
print(s)