n, r, c = map(int, input().split())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

move_dir = 0 # 상, 하, 좌, 우

x, y = r-1, c-1

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

print(grid[x][y], end = ' ')
for i in range(n * n - 1):
    for k in range(4):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if in_range(nx, ny):
            if grid[x][y] < grid[nx][ny]:
                x, y = x + dxs[move_dir], y + dys[move_dir]
                print(grid[x][y], end = ' ')
        move_dir = (move_dir + 1) % 4