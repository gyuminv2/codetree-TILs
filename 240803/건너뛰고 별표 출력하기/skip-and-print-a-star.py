n = int(input())
j = 1
for i in range(1, n):
    for _ in range(i%(n+1)):
        print('*', end='')
    print()
    print()
for i in range(n, 0, -1):
    for _ in range(i):
        print('*', end='')
    print()
    print()