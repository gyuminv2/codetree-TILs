a, b = map(int, input().split())
rtn = 1
for i in range(1, b+1):
    if i % a == 0:
        rtn *= i
print(rtn)