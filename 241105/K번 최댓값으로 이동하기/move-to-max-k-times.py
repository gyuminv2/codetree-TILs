from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

x, y = map(int, input().split())

pivot = graph[x-1][y-1]

q = deque()

def push(x, y):
    visited[x][y] = graph[x][y]
    q.append((x, y))

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    global ch
    if not in_range(x, y):
        return False
    if graph[x][y] >= pivot:
        return False
    if visited[x][y] == graph[x][y]:
        return False
    return True

def bfs():
    global cp
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if can_go(nx, ny):
                push(nx, ny)
                cp = 1

def find_next_loc(visited):
    tmp = 0
    nx, ny = 0, 0
    stand = 0
    for i in range(n):
        for j in range(n):
            tmp = visited[i][j]
            if tmp < pivot and tmp > stand:
                stand = tmp
                nx, ny = i, j
    return nx, ny

result = []
visited = [[0 for _ in range(n)] for _ in range(n)]
push(x-1, y-1)
bfs()
result.append((x-1, y-1))
for _ in range(k):
    x, y = find_next_loc(visited)
    # print(x, y, pivot, graph[x][y])
    if graph[x][y] == pivot:
        break
    pivot = graph[x][y]
    cp = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    push(x, y)
    bfs()
    if cp == 1:
        result.append((x, y))
    else:
        result.append((x, y))
        break

x, y = result[-1][0], result[-1][1]
print(x+1, y+1)