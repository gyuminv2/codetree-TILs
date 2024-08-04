n = int(input())

a = list(map(int, input().split()))
a.reverse()
for i in a:
    if i % 2 == 0:
        print(i, end=' ')