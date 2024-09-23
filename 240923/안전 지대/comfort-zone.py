n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == True:
        return False
    if graph[x][y] <= k:
        return False
    return True

def dfs(x, y):
    global home_cnt
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if can_go(nx, ny):
            dfs(nx, ny)

safe_area = []

for k in range(1, 101):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    home_cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] <= k:
                visited[i][j] = 1
                continue
            elif visited[i][j] == 0:
                dfs(i, j)
                home_cnt += 1
    safe_area.append((k, home_cnt))

tmp = [0, 0]
for i in safe_area:
    if tmp[1] < i[1]:
        tmp[0] = i[0]
        tmp[1] = i[1]

print(tmp[0], tmp[1])