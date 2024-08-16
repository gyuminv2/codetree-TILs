from collections import deque

n, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

loc = []
for _ in range(k):
    loc.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 1:
        return False
    return True

def push(x, y):
    visited[x][y] = 1
    q.append((x, y))

rtn = 0

def bfs():
    global rtn
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny)
                rtn += 1

push(0, 0)
rtn += 1
bfs()
print(rtn)