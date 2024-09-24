n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

num_block = 0 # 터지게 되는 블럭의 수
max_block = 0 # 최대 블럭의 크기
tmp_block = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == True:
        return False
    return True

def dfs(x, y):
    global tmp_block
    visited[x][y] = True
    tmp_block += 1

    for dx, dy in zip(dxs, dys):
        nx, ny = dx + x, dy + y
        if can_go(nx, ny):
            if graph[x][y] == graph[nx][ny]:
                dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            if tmp_block >= 4:
                num_block += 1
            if tmp_block > max_block:
                max_block = tmp_block
            tmp_block = 0

print(num_block, max_block)