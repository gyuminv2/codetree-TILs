n = int(input())

sq = 9
for i in range(n):
    for j in range(n):
        if sq == 0:
            sq = 9
        print(sq, end='')
        sq -= 1
    print()