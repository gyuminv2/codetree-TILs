n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]

dxs = [1, 0]
dys = [0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 0:
        return False
    if visited[x][y] == 1:
        return False
    return True

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    
    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy +y
        if can_go(nx, ny):
            dfs(nx, ny)

vlg_cnt = 0
vlg = []
cnt = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            vlg.append(cnt)
            cnt = 0
            vlg_cnt += 1

print(vlg_cnt)
for p in sorted(vlg):
    print(p)