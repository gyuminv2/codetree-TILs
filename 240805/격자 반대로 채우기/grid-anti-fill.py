n = int(input())

dx = -1

arr = [[0 for _ in range(n)] for _ in range(n)]
k = 1

for i in range(n-1, -1, -1):
    dx *= -1
    if dx > 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = k
            k += 1
    else:
        for j in range(n):
            arr[j][i] = k
            k += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print(' ')