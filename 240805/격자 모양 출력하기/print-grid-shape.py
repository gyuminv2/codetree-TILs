n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    k, l = map(int, input().split())
    arr[k-1][l-1] = k*l

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()