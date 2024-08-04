a, b = map(int, input().split())

x = 2
for i in range(4):
    for j in range(b, a-1, -1):
        if j != a:
            print(f'{j} * {x} = {j*x} ', end='/ ')
        else:
            print(f'{j} * {x} = {j*x} ', end='')
    x += 2
    print()