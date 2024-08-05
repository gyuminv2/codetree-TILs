arr = []
rtn = 0
for i in range(4):
    arr.append(list(map(int, input().split())))
    for j in range(0, i+1):
        rtn += arr[i][j]
print(rtn)