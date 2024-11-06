n = int(input())
arr = list(map(int, input().split()))
tmp = []
mid = []

for i in range(n):
    tmp.append(arr[i])
    if i % 2 == 0:
        tmp.sort()
        mid.append(tmp[i//2])
print(*mid)