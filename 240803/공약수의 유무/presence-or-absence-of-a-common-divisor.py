a, b = map(int, input().split())
cd = []
for i in range(1, 1920):
    if 1920 % i == 0 and 2880 % i == 0:
        cd.append(i)
for i in range(a, b+1):
    if i in cd:
        print(1)
        exit()
print(0)