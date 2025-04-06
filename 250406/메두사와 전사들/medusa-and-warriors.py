from collections import deque

def find_route(x, y):
    visited = [[0]*n for _ in range(n)]
    q = deque([(x, y)])
    visited[x][y] = ((x, y))

    while q:
        x, y = q.popleft()

        if (x, y) == (park_x, park_y):
            route = []
            x, y = visited[x][y]
            while (x, y) != (home_x, home_y):
                route.append((x, y))
                x, y = visited[x][y]
            return route[::-1]

        for dx, dy in zip(dxs, dys):
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = ((x, y))
                q.append((nx, ny))
    return -1

def rm_warrier(x, y):
    for i in range(len(warrier)-1, -1, -1):
        if [warrier[i][0], warrier[i][1]] == [x, y]:
            warrier.pop(i)

def mark_line(v, ci, cj, dr):
    while 0<=ci<n and 0<=cj<n:
        v[ci][cj] = 2
        ci, cj = ci + ddxs[dr], cj + ddys[dr]

def mark_safe(v, si, sj, dr, ddr):
    # [1] 직선 방향 표시
    ci, cj = si + ddxs[dr], sj + ddys[dr]
    mark_line(v, ci, cj, dr)

    # [2] 바라보는 방향으로 한줄씩 표시
    ci, cj = si + ddxs[ddr], sj + ddys[ddr]
    while 0<=ci<n and 0<=cj<n:
        mark_line(v, ci, cj, dr)
        ci, cj = ci + ddxs[ddr], cj + ddys[ddr]

# tmp_visited, tmp_stone = make_stone(w_arr, mi, mj, dr)
def make_stone(w_arr, mi, mj, dr):
    visited = [[0]*n for _ in range(n)]
    stone_cnt = 0
    # [1] : dr 방향으로 만날때까지 1표시, 그 후 2표시
    ni, nj = mi + ddxs[dr], mj + ddys[dr]
    while 0<=ni<n and 0<=nj<n:
        visited[ni][nj] = 1
        if w_arr[ni][nj] > 0:
            stone_cnt += w_arr[ni][nj]
            ni, nj = ni + ddxs[dr], nj + ddys[dr]
            mark_line(visited, ni, nj, dr)
            break
        ni, nj = ni + ddxs[dr], nj + ddys[dr]

    # [2] : dr-1, dr+1 방향으로 동일처리, 대각선 원점 잡고 dr 방향 처리 (50:30)
    for ddr in [((dr-1)%8), ((dr+1)%8)]:
        si, sj = mi + ddxs[ddr], mj + ddys[ddr]
        while 0<=si<n and 0<=sj<n:
            if visited[si][sj] == 0 and w_arr[si][sj] > 0:
                visited[si][sj] = 1
                stone_cnt += w_arr[si][sj]
                mark_safe(visited, si, sj, dr, ddr)
                break

            ci, cj = si, sj
            while 0<=ci<n and 0<=cj<n:
                if visited[ci][cj] == 0:
                    visited[ci][cj] = 1
                    if w_arr[ci][cj] > 0:
                        stone_cnt += w_arr[ci][cj]
                        mark_safe(visited, ci, cj, dr, ddr)
                        break
                else:
                    break
                ci, cj = ci + ddxs[dr], cj + ddys[dr]
            si, sj = si + ddxs[ddr], sj + ddys[ddr]
    
    return visited, stone_cnt

# total_move, attk_cnt = move_warrier(visited, mi, mj)
def move_warrier(visited, mi, mj):
    move, attk = 0, 0

    # 상하좌우, 좌우상하 | 메두사 시야 = 1 피해서
    for dr in ([0, 1, 2, 3], [2, 3, 0, 1]):
        for idx in range(len(warrier)-1, -1, -1):
            ci, cj = warrier[idx]
            if visited[ci][cj] == 1:    # 메두사 시야면 얼음
                continue
            
            dist = abs(mi-ci) + abs(mj-cj)
            for ddr in dr:
                ni, nj = ci + dxs[ddr], cj + dys[ddr]
                if 0<=ni<n and 0<=nj<n and visited[ni][nj] != 1 and dist > abs(mi-ni) + abs(mj-nj):
                    if (ni, nj) == (mi, mj):
                        attk += 1
                        warrier.pop(idx)
                    else:
                        warrier[idx] = [ni, nj]
                    move += 1
                    break
    return move, attk
        
# ===============================================================
# ===============================================================

n, m = map(int, input().split())
home_x, home_y, park_x, park_y = map(int, input().split())
w_pos = list(map(int, input().split()))
warrier = []
for i in range(0, m*2, 2):
    warrier.append(w_pos[i:i+2])
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
# 0: 좌상, 1: 상, 2: 우상, 3: 우, 4: 우하, 5: 하, 6: 좌하, 7: 좌
ddxs = [-1, -1, -1, 0, 1, 1, 1, 0]
ddys = [-1, 0, 1, 1, 1, 0, -1, -1]

# 집 -> 공원 경로
route = find_route(home_x, home_y)
if route == -1:
    print(-1)
else:
    for mi, mj in route:
        # 출력 (전사 이동 거리 합, 돌 수, 공격 수)
        total_move, attk_cnt = 0, 0

        # [1] 메두사의 이동 : 지정된 최단거기로 한 칸 이동 (전사 만날 시 pop)
        if [mi, mj] in warrier:       # 역순으로 삭제
            rm_warrier(mi, mj)

        # [2] 메두사의 시선 : 상하좌우 네 방향 가장 많이 돌로 만든 
        # => v[]에 표시해서 이동시 참조(메두사 시선 == 1, 전사에 가려짐 == 2)
        # w_arr[][] : 지도에 있는 전사 수 표시
        w_arr = [[0]*n for _ in range(n)]
        for wi, wj in warrier:
            w_arr[wi][wj] += 1

        mx_stone = -1
        visited = []
        for dr in [1, 5, 7, 3]:         # 상하좌우 순서로 처리
            tmp_visited, tmp_stone = make_stone(w_arr, mi, mj, dr)
            if mx_stone < tmp_stone:
                mx_stone = tmp_stone
                visited = tmp_visited
        
        # [3] 전사들의 이동 (한 칸씩 두번) : 메두사 있는 경우 공격 후 pop
        total_move, attk_cnt = move_warrier(visited, mi, mj)

        print(total_move, mx_stone, attk_cnt)
    print(0)