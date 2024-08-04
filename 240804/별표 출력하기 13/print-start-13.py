n = int(input())

a = n
b = 1

for i in range(1, n+1):
    if i % 2 != 0:
        for j in range(a):
            print('*', '', end='')
        a -= 1
    else:
        for j in range(b):
            print('*', '', end='')
        b += 1
    print()
for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(a):
            print('*', '', end='')
        a -= 1
    else:
        for j in range(b):
            print('*', '', end='')
        b += 1
    print()