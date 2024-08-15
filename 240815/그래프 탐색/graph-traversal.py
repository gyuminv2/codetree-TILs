n, m = map(int, input().split())

graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

visited = [0] * (n+1)
cnt = 0

def dfs(vertex):
    global cnt
    for curr_v in range(1, n+1):
        if graph[vertex][curr_v] == True and not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)

for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(cnt)