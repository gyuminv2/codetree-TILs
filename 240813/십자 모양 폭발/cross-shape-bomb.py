n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int, input().split())))

r, c = map(int, input().split())
x, y = r-1, c-1
tmp_x, tmp_y = x, y
ran = grid[x][y] - 1

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
move_dir = -1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(4):
    move_dir = (move_dir + 1) % 4
    tmp_x, tmp_y = x, y
    for j in range(ran):
        nx, ny = tmp_x + dxs[move_dir], tmp_y + dys[move_dir]
        if not in_range(nx, ny):
            break
        grid[nx][ny] = 0
        tmp_x += dxs[move_dir]
        tmp_y += dys[move_dir]
grid[x][y] = 0

rtn_grid = []
for j in range(n-1, -1, -1):
    n_grid = []
    cnt = 0
    for i in range(n-1, -1, -1):
        if grid[i][j] != 0:
            n_grid.append(grid[i][j])
        else:
            cnt += 1
    for i in range(cnt):
        n_grid.append(0)
    rtn_grid.append(n_grid)

for j in range(n-1, -1, -1):
    for i in range(n-1, -1, -1):
        print(rtn_grid[i][j], end=' ')
    print('')