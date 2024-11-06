n = int(input())
arr = list(map(int, input().split()))
mid = []

for i in range(n):
    if i % 2 == 0:
        mid.append(arr[i//2])
print(*mid)