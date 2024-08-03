n = int(input())
j = 1
for i in range(n):
    for _ in range(j * 2 - 1):
        print('*', end='')
    j += 1
    print()