n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i][j-1] + arr[i-1][j]

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()