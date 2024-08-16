from collections import deque

n, h, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

human_x = []
human_y = []
point_x = []
point_y = []
for x in range(n):
    for y in range(n):
        if grid[x][y] == 2:
            human_x.append(x)
            human_y.append(y)
        if grid[x][y] == 3:
            point_x.append(x)
            point_y.append(y)

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
    if step[x][y] < s:
        step[x][y] = s
    q.append((x, y))

def bfs(end_x, end_y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                push(nx, ny, step[x][y] + 1)

ans = [[0 for _ in range(n)] for _ in range(n)]
for s_x, s_y in zip(human_x, human_y):
    for e_x, e_y in zip(point_x, point_y):
        visited = [[0 for _ in range(n)] for _ in range(n)]
        step = [[0 for _ in range(n)] for _ in range(n)]

        push(s_x, s_y, step[s_x][s_y])
        bfs(e_x, e_y)
        time = step[e_x][e_y]
        if time == 0:
            continue

        if ans[s_x][s_y] != 0:
            tmp = ans[s_x][s_y]
            if tmp > time:
                ans[s_x][s_y] = time
        else:
            ans[s_x][s_y] = time

    if ans[s_x][s_y] == 0:
        ans[s_x][s_y] = -1

for x in range(n):
    for y in range(n):
        print(ans[x][y], end=' ')
    print('')