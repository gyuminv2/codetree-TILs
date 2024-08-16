from collections import deque

n = int(input())

x1, y1, x2, y2 = list(map(int, input().split()))
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1:
        return False
    return True

def push(x, y, s):
    step[x][y] = s
    visited[x][y] = 1
    q.append((x, y))

def bfs():
    dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
    dys = [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

if x1 == x2 and y1 == y2:
    print(0)
    exit()
else:
    push(x1, y1, step[x1][y1])
    bfs()

if step[x2][y2] == 0:
    print(-1)
else:
    print(step[x2][y2])