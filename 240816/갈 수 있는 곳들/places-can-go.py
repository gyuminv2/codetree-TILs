from collections import deque

n, k = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

loc_x = []
loc_y = []
for _ in range(k):
    x, y = map(int, input().split())
    loc_x.append(x-1)
    loc_y.append(y-1)

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

for x, y in zip(loc_x, loc_y):
    push(x, y)
    bfs()
    rtn += 1
print(rtn)