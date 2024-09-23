n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

cnt = 0

def dfs(v):
    global cnt

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            visited[i] = True
            dfs(i)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = True
dfs(1)

print(cnt)