a = input()
b = input()
cnt = 0

for i in range(len(a)):
    a = a[-1] + a[0:-1]
    cnt += 1
    if a == b:
        print(cnt)
        exit()
print(-1)