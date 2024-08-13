n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

dxs = [-1, -1, 0, 1, 1, 1, 0 , -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]
move_dir = 0

def find_idx(k):
    for i in range(n):
        for j in range(n):
            if k == grid[i][j]:
                return i, j

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for k in range(1, n * n + 1):
    x, y = find_idx(k)
    move_dir = 0
    big = 0
    tmp_nx, tmp_ny = 0, 0
    for _ in range(8):
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if not in_range(nx, ny):
            move_dir = (move_dir + 1) % 8
            continue
        if big < grid[nx][ny]:
            big = grid[nx][ny]
            tmp_nx, tmp_ny = nx, ny
        move_dir = (move_dir + 1) % 8
    grid[x][y], grid[tmp_nx][tmp_ny] = grid[tmp_nx][tmp_ny], grid[x][y]

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print('')