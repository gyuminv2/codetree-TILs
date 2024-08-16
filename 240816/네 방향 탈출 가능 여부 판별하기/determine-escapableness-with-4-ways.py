from collections import deque

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 0 or visited[x][y] == 1:
        return False
    return True

def push(x, y):
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny)

push(0, 0)
bfs()
if visited[n-1][m-1] == 1:
    print(1)
else:
    print(0)