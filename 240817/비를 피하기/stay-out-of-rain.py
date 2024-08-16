from collections import deque

n, h, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

point = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 3:
            point.append((x, y))


ans = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 1:
        return False
    return True

def push(x, y, s):
    visited[x][y] = 1
    step[x][y] = s
    q.append((x, y))

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

for e_x, e_y in point:
    push(e_x, e_y, 0)
bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] != 2:
            print(0, end=" ")
        else:
            if not visited[i][j]:
                print(-1, end=" ")
            else:
                print(step[i][j], end=" ")
    print()