n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]
dxs = [0, 1]
dys = [1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    return True

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)

print(visited[n-1][m-1])