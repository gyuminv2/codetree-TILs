n, m, t = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

goo = []
for i in range(m):
    goo.append(list(map(int, input().split())))
    goo[i][0], goo[i][1] = goo[i][0]-1, goo[i][1]-1

cnt = [[0 for _ in range(n)] for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
move_dir = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# n_goo = []
for _ in range(t): # t초
    move_dir = 0
    n_goo = []
    for i in range(len(goo)): # m개의 구슬
        move_dir = 0
        big = 0
        tmp_nx = 0
        tmp_ny = 0
        for _ in range(4): # 상하좌우 최대값
            nx, ny = goo[i][0] + dxs[move_dir], goo[i][1] + dys[move_dir]
            if not in_range(nx, ny):
                move_dir = (move_dir + 1) % 4
                continue
            if big < grid[nx][ny]:
                tmp_nx = nx
                tmp_ny = ny
                big = grid[nx][ny]
            move_dir = (move_dir + 1) % 4
        # print(big)
        if (tmp_nx, tmp_ny) in n_goo:
            n_goo.pop(n_goo.index((tmp_nx, tmp_ny)))
        else:
            n_goo.append((tmp_nx, tmp_ny))
        # print(n_goo)
        cnt[tmp_nx][tmp_ny] += 1
        if cnt[tmp_nx][tmp_ny] > 1:
            cnt[tmp_nx][tmp_ny] = 0
    goo = n_goo
    # print(goo)
print(len(goo))