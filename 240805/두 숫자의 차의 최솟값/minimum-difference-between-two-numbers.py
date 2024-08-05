n = int(input())
arr = list(map(int, input().split()))
mini = 99999999

for i in range(n):
    for j in range(i+1, n-1):
        mini = min(mini, arr[j]-arr[i])
print(mini)