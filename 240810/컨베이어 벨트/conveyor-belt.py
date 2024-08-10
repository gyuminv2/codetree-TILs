n, t = map(int, input().split())

arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))

for i in range(t):
    tmpmp = arr[1][n-1]
    for j in range(1, -1, -1):
        tmp = arr[j][n-1]
        for k in range(n-2, -1, -1):
            arr[j][k+1] = arr[j][k]
        if j != 1:
            arr[j+1][0] = tmp
    arr[0][0] = tmpmp

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()