n = int(input())

alpha = [chr(i) for i in range(65, 91)]

x = 0
for i in range(n):
    for j in range(n):
        if alpha[x] == 'Z':
            x = 0
        if j < i:
            print(' ', end=' ')
        else:
            print(alpha[x], end=' ')
            x += 1
    print()