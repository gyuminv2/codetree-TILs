# [1] 미지의 공간 평면도 : 전체 맵 (위에서 내려다 본)
# [2] 시간의 벽 단면도 : 동, 서, 남, 북, 윗면

# 0 : 빈 공간, 1 : 장애물
# 단면도( [2] 윗면 어딘가 ) | [2] 타임머신(2)
# 평면도 | [1] 위치(3) | [1] 탈출구(4)(미지의 공간 바닥)

# 시간의 벽 <-> 미지의 공간 바닥 출구는 단 하나

# 미지의 공간 바닥에 F개의 시간 이상 현상
# 바닥의 빈 공간 (r, c)에서 시작해서 매 v의 배수 턴마다 d 방향으로 한 칸씩 확산
# 확산 후에도 기존 위치의 시간 이상 현상은 남음
# 시간 이상 현상은 장애물과 탈출구가 없는 빈 공간으로 확산, 더 이상 확산할 수 없을 경우 멈춤
# 모든 시간 이상 현상은 서로 독립적, 동시 확산
# d : 0, 1, 2, 3 (동 서 남 북)

# 타임머신은 매 턴마다 상하좌우로 한 칸씩 이동
# 장애물, 시간 이상 현상을 피해 "탈출구"까지 도달해야 함
# "탈출구"까지의 최소 시간 출력 (fail : -1)
# 시간 이상 현상 확산 -> 타임머신 이동

# 이상 현상 배열
# visited 배열

from collections import deque

n, m, f = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
grid_3d = [
    [
        list(map(int, input().split()))
        for _ in range(m)
    ]
    for _ in range(5)
]
warn = [
    list(map(int, input().split()))
    for _ in range(f)
]

# 동 서 남 북
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

def find_3d_start():
    for i in range(m):
        for j in range(m):
            if grid_3d[4][i][j] == 2:
                return i, j

def find_3d_base():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                return i, j

def find_2d_end():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 4:
                grid[i][j] = 0
                return i, j

# find_3d_end_2d_start(sx_3d, sy_3d, ex_2d, ey_2d)
def find_3d_end_2d_start(sx_3d, sy_3d, ex_2d, ey_2d):
    bi, bj = find_3d_base()

    for i in range(bi, bi+m):
        for j in range(bj, bj+m):
            if grid[i][j] != 3:
                print('아닐 수가 있나?')
                continue
            if grid[i][j+1] == 0:   # 우측에 0 위치
                return 0, m-1, (m-1)-(i-bi), i, j+1
            if grid[i][j-1] == 0:   # 좌측에 0 위치
                return 1, m-1, i-bi, i, j-1
            if grid[i+1][j] == 0:   # 남측에 0 위치
                return 2, m-1, j-bj, i+1, j
            if grid[i-1][j] == 0:
                return 3, m-1, (m-1)-(j-bj), i-1, j
    return -1

left_nxt = {0:2, 1:3, 2:1, 3:0}
right_nxt = {0:3, 1:2, 2:0, 3:1}
def bfs_3d(dr, sx, sy, ex, ey):
    v = [[[0] * m for _ in range(m)] for _ in range(5)]
    q = deque([(4, sx, sy)])
    v[4][sx][sy] = 1

    while q:
        r, x, y = q.popleft()

        if (r, x, y) == (dr, ex, ey):
            return v[r][x][y]

        for ddr in [0, 1, 2, 3]:
            nx, ny = x + dxs[ddr], y + dys[ddr]
            if nx < 0:                      # 위쪽 범위 이탈
                if r == 0:
                    nk, nx, ny = 4, (m-1)-y, m-1
                elif r == 1:
                    nk, nx, ny = 4, y, 0
                elif r == 2:
                    nk, nx, ny = 4, m-1, y
                elif r == 3:
                    nk, nx, ny = 4, 0, (m-1)-y
                elif r == 4:
                    nk, nx, ny = 3, 0, (m-1)-y
            elif nx >= m:                   # 아래쪽 범위 이탈
                if r == 4:
                    nk, nx, ny = 2, 0, y
                else:
                    continue
            elif ny < 0:                    # 왼쪽 범위 이탈
                if r == 4:
                    nk, nx, ny = 1, 0, x
                else:
                    nk, nx, ny = left_nxt[r], x, m-1
            elif ny >= m:
                if r == 4:
                    nk, nx, ny = 0, 0, (m-1)-x # x->(m-1)-x
                else:
                    nk, nx, ny = right_nxt[r], x, 0
            else:
                nk = r
            
            if v[nk][nx][ny] == 0 and grid_3d[nk][nx][ny] == 0:
                v[nk][nx][ny] = v[r][x][y] + 1
                q.append((nk, nx, ny))

    return -1

def bfs_2d(v, d, si, sj, ei, ej):
    q = deque([(si, sj)])
    v[si][sj] = d

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return v[ci][cj]

        for dr in [0, 1, 2, 3]:
            ni, nj = ci + dxs[dr], cj + dys[dr]
            if 0<=ni<n and 0<=nj<n and grid[ni][nj] == 0 and (v[ci][cj]+1) < v[ni][nj]:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
    return -1

sx_3d, sy_3d = find_3d_start()
ex_2d, ey_2d = find_2d_end()

dr, ex_3d, ey_3d, sx_2d, sy_2d = find_3d_end_2d_start(sx_3d, sy_3d, ex_2d, ey_2d)

dist = bfs_3d(dr, sx_3d, sy_3d, ex_3d, ey_3d)

if dist != -1:
    v = [[401]*n for _ in range(n)]
    for wi, wj, wd, wv in warn:
        v[wi][wj] = 1
        for i in range(1, n+1):
            wi, wj = wi + dxs[wd], wj + dys[wd]
            if 0<=wi<n and 0<=wj<n and grid[wi][wj] == 0 and (wi, wj) != (ex_2d, ey_2d):
                v[wi][wj] = wv*i
            else:
                break
    dist = bfs_2d(v, dist, sx_2d, sy_2d, ex_2d, ey_2d)

print(dist)