a, b = map(int, input().split())
arr = []
rtn = 0
tmp = 1

while a > 0:
    arr.append(a%b)
    a //= b

for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        tmp += 1
    else:
        rtn += tmp ** 2
        tmp = 1
rtn += tmp ** 2
print(rtn)