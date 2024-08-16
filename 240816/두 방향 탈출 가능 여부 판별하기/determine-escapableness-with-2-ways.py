n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if grid[x][y] == 0 or visited[x][y] == 1:
        return False
    return True

def dfs(x, y):
    global result

    if x == n-1 and y == n-1:
        result = 1
    
    visited[x][y] = 1
    dxs = [1, 0]
    dys = [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        
        if can_go(nx, ny):
            dfs(nx, ny)

dfs(0, 0)
print(*visited)
if result == 1:
    print(1)
else:
    print(0)