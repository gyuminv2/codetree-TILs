# import sys
# sys.setrecursionlimit(10**5)

n = int(input())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(n)]
village = 0
order = 0
order_l = []

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global order

    visited[x][y] = 1
    order += 1
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)


for x in range(n):
    for y in range(n):
        order = 0
        if grid[x][y] == 1 and visited[x][y] == 0:
            dfs(x, y)
            village += 1
            order_l.append(order)

# for x in range(n):
#     for y in range(n):
#         print(visited[x][y], end=' ')
#     print('')
print(village)
order_l.sort()
for i in order_l:
    print(i)