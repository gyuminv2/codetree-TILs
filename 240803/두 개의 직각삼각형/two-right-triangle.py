n = int(input())

for i in range(n, 0, -1):
    for j in range(n):
        if i > j:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(n, 0, -1):
        if i >= j:
            print('*', end='')
        else:
            print(' ', end='')
    print()