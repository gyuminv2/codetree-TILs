n = int(input())


arr = [[i for i in range(n, 0, -1)] for j in range(n)]

k = 1
for i in range(n):
    for j in range(n):
        print(arr[i][j] * k, end=' ')
    k += 1
    print()