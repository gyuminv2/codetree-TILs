
def golem_move(ci, di, p):
    # 남쪽 (아아, 아왼, 아오)
    i = 0
    while (grid[i+2][ci] + grid[i+1][ci-1] + grid[i+1][ci+1]) == 0:
        i += 1
    # 서쪽 (왼왼, 아왼, 아왼왼, 아아왼) (출구 반시계방향)
    while (grid[i][ci-2] + grid[i+1][ci-1] + grid[i+1][ci-2] + grid[i+2][ci-1]) == 0:
        ci -= 1
        di = (di-1)%4
        i += 1
    while (grid[i+2][ci] + grid[i+1][ci-1] + grid[i+1][ci+1]) == 0:
        i += 1
    # 동쪽 (오오, 아오, 아오오, 아아오) (출구 시계)
    while (grid[i][ci+2] + grid[i+1][ci+1] + grid[i+1][ci+2] + grid[i+2][ci+1]) == 0:
        ci += 1
        di = (di+1)%4
        i +=1
    while (grid[i+2][ci] + grid[i+1][ci-1] + grid[i+1][ci+1]) == 0:
        i += 1
    # 초기화
    if (i-1) <= 2:
        end_points = []
        return [
            [-1] + [0] * c + [-1]
            for _ in range(r+3)
        ] + [[-1]*(c+2)], 0, 0, 0
    else:
        # R에 닿았는지 확인
        if (i+1) == (r+3):
            end_points.append((i))
        # 배열 채우기
        # 북 동 남 서
        grid[i][ci] = p
        grid[i-1][ci] = p
        grid[i][ci+1] = p
        grid[i+1][ci] = p
        grid[i][ci-1] = p
        if di == 0:
            grid[i-1][ci] = -p
        elif di == 1:
            grid[i][ci+1] = -p
        elif di == 2:
            grid[i+1][ci] = -p
        else:
            grid[i][ci-1] = -p
    return grid, i, ci, 1

from collections import deque
def tinkerbell_move(grid, si, sj, p):
    # v는 1마리가 이동할 때마다 초기화
    v = [[0]*(c+2) for _ in range(r+4)]
    q = deque([(si, sj)])
    v[si][sj] = 1
    grid[si][sj] = p
    mx_ci = 0

    while q:
        ci, cj = q.popleft()
        mx_ci = max(mx_ci, ci)

        for di, dj in zip(dis, djs):
            ni, nj = ci + di, cj + dj
            if 0<=ni<(r+4) and 0<=nj<(c+2) and v[ni][nj] == 0 and grid[ni][nj] != -1 and grid[ni][nj] != 0:
                if (grid[ci][cj] == grid[ni][nj]) or (grid[ci][cj] < 0) or (grid[ci][cj] == -grid[ni][nj]):
                    v[ni][nj] = 1
                    q.append((ni, nj))
    # for q in v:
    #     print(*q)
    # print (mx_ci-2)
    return mx_ci-2

####################
####################
# 골렘 : 
# 정령 : 
# 출구 : -2
r, c, k = map(int, input().split())
golem = [
    list(map(int, input().split()))
    for _ in range(k)
]
grid = [
    [-1] + [0] * c + [-1]
    for _ in range(r+3)
]+ [[-1]*(c+2)]
# 남 동 서 북
dis = [1, 0, 0, -1]
djs = [0, 1, -1, 0]
end_points = []

ans = 0
p = 2
for ci, di in golem:
    grid, si, sj, f = golem_move(ci, di, p)
    if f != 0:
        ans += tinkerbell_move(grid, si, sj, p)
    p += 1
    # for g in grid:
    #     print(g)
print(ans)