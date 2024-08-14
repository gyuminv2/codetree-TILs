n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

ans = []

def Cal(ans):
    rtn = 0
    for i in range(n):
            rtn += arr[i][ans[i]]
    return rtn

large = 0
visited = [0] * (n+1)

def per(k):
    global large
    global visited
    if k == n+1:
        if large < Cal(ans):
            large = Cal(ans)
        return
    
    for i in range(n):
        if visited[i] == True:
            continue
        visited[i] = True
        ans.append(i)
        per(k + 1)
        ans.pop()
        visited[i] = False

per(1)
print(large)