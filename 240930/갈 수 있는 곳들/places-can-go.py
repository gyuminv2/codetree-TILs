from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]

loc = []
for _ in range(k):
    loc.append(list(map(int, input().split())))

q = deque()

total = 0

def push(x, y):
    global total
    if visited[x][y] == False:
        visited[x][y] = True
        q.append((x, y))
        total += 1
        
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if graph[x][y] == 1:
        return False
    if visited[x][y] == 1:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                push(nx, ny)

for i in range(k):
    push(loc[i][0]-1, loc[i][1]-1)
    bfs()

print(total)