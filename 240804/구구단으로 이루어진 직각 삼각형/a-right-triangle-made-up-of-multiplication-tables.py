n = int(input())

for i in range(1, n+1):
    x = 1
    for j in range(i, n+1):
        if j != n:
            print(f'{i} * {x} = {i*x} ', end='/ ')
        else:
            print(f'{i} * {x} = {i*x} ', end='')
        x += 1
    print()