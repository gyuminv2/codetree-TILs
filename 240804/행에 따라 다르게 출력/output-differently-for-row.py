n = int(input())

o = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(o, end=' ')
        if i % 2 != 0:
            print(o, end=' ')
            o += 1
        o += 1
    if i % 2 == 0:
        o += 1
    if i % 2 != 0:
        o -= 1
    print()