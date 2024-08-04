n = int(input())

arr = [i for i in range(n, 0, -1)]

for i in range(n):
    print(*arr)

# for i in range(n, 0, -1):
#     for j in range(n):
#         print(n-j, end=' ')
#     print()