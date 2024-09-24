from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x and x < m and 0 <= y and y < n 

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == True:
        return False
    if graph[x][y] == 0:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                push(nx, ny)

def push(x, y):
    visited[x][y] = True
    q.append((x, y))
    
push(0, 0)
bfs()

if visited[n-1][n-1] == 1:
    print(1)
else:
    print(0)