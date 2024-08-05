n = int(input())
arr = list(map(int, input().split()))
mini = 99999999

for i in range(n-1):
    mini = min(mini, arr[i+1] - arr[i])
print(mini)