n = int(input())
# 4

# 4
# 3 5
# 2 4 6
# 1 3 5 7

# 다이아몬드 위쪽 절반
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 다이아몬드 아래쪽 절반
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2 * (n - i - 1) - 1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()