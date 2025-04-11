# M : 참가자 수
# N X N : 미로
# 1 : 빈칸
# - 이동 가능
# 2 : 벽
# - 이동 불가
# - 내구도 => 1 ~ 9
# - 회전 시 => 내구도 1 감소
# - (내구도 == 0) => 빈 칸
# 3 : 출구
# - 도달 시 즉시 탈출

# [1] 움직임
# 최단거리 : |x1 - x2| + |y1 - y2| , (x1, y1) (x2, y2)
# 모든 참가자는 동시에 움직임...?
# 상하좌우
# 출구까지 최단거리로 이동
# 움직일 수 있는 칸 2개 이상 => 상하 우선
# 움직일 수 없음 => 안 움직임
# 한 칸에 2명 이상 => 가능

# [2] 미로 회전
# 움직임 종료 시 회전
# 1명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 : 범위
# 가장 작은 크기 정사각형 2개 이상 => r 좌표 작음 => c 좌표 작음
# 선택한 정사각형 90도 회전 후 내구도 1 감소

# [3] 종료
# K번 반복, 참가자 전원 탈출 시 게임 종료.
# 모든 참가자들의 이동거리 합, 출구 좌표 출력

def find_exit(f):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == -1:
                if not f:
                    return i, j
                else:
                    return i+1, j+1

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def rotate(arr, si, sj, n):
    n_arr = [a[:] for a in arr]
    for i in range(n):
        for j in range(n):
            n_arr[si+i][sj+j] = arr[si+n-j-1][sj+i]
            if n_arr[si+i][sj+j] != 0 and n_arr[si+i][sj+j] != -1:
                n_arr[si+i][sj+j] -= 1

            # for k in range(1, M+1):
            #     ri, rj, d, e = runner[k]
            #     if e == 1:
            #         continue
            #     if (si+i, sj+j) == (ri, rj):
            #         runner[k] = [si+n-j-1, sj+i, d, e]

        # runner 좌표 회전
    for k in range(1, M+1):
        ri, rj, d, e = runner[k]
        if e == 1:
            continue
        if si <= ri < si + n and sj <= rj < sj + n:
            # 회전 공식: (x, y) → (y', x') = (n - 1 - (y - sj), x - si) + (si, sj)
            ni = si + (rj - sj)
            nj = sj + (n - 1 - (ri - si))
            runner[k] = [ni, nj, d, e]
            # print(k, 'RUNNER:', runner[k])
            
    return n_arr

######################
######################
N, M, K = map(int, input().split())
maze = [
    list(map(int, input().split()))
    for _ in range(N)
]
# 0 : 빈 칸
# (1~9) : 벽(내구도)
# -1 : 출구
runner = dict()
for i in range(1, M+1):
    x, y = map(int, input().split())
    # x, y, 움직인 거리, 탈출 여부
    runner[i] = [x-1, y-1, 0, 0]
a,b = map(int, input().split())
maze[a-1][b-1] = -1
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

for cake in range(1, K+1):
    # [1] : 움직임
    # print("#######", cake, "초 #######")
    # print('움직임')
    # for g in maze:
    #     print(*g)
    # print()

    ei, ej = find_exit(0)
    for idx in range(1, M+1):
        i, j, d, e = runner[idx]
        # print(idx, '번째 러너(before):', runner[idx])
        if e == 1:
            continue
        # 출구 - 현재 위치
        mn_dist = abs(i-ei) + abs(j-ej)
        ci, cj = i, j
        for dr in [0, 1, 2, 3]:
            ni, nj = i + dis[dr], j + djs[dr]
            if in_range(ni, nj) and maze[ni][nj] <= 0:
                dist = abs(ni-ei) + abs(nj-ej)
                if mn_dist > dist:
                    mn_dist = dist
                    ci, cj = ni, nj
        # ci, cj = 새롭게 가까워진 위치
        # print('NEW WHERE', ci, cj, ei, ej)
        if (ci, cj) == (ei, ej):
            runner[idx] = [ci, cj, d+1, 1]
            continue
        elif (ci, cj) != (i, j):
            # print('뭐여', ci, cj, d+1)
            runner[idx] = [ci, cj, d+1, 0]
    
    # for i in range(1, M+1):
    #     print(i, '번째 러너:', runner[i])
    # print()

    # 전원 탈출 check
    exit_num = 0
    for idx in range(1, M+1):
        _, _, _, e = runner[idx]
        if e == 1:
            exit_num += 1
    if exit_num == M:
        break

    # [2] 미로 회전
    # 출구와 가까운 runner 찾기
    # mn_dist = 987654321
    # si, sj = -1, -1
    # for idx in range(1, M+1):
    #     i, j, d, e = runner[idx]
    #     if e == 1:
    #         continue
    #     dist = abs(i-ei) + abs(j-ej)
    #     if mn_dist > dist:
    #         mn_dist = dist
    #         si, sj = i, j
    #     elif mn_dist == dist:
    #         if si > i:
    #             si, sj = i, j
    #         elif si == i:
    #             if sj > j:
    #                 si, sj = i, j

    # 정사각형 만들기 (인당 최대 2개)
    # x, y, n(크기)
    squere = []
    for idx in range(1, M+1):
        i, j, d, e = runner[idx]
        if e == 1:
            continue
        # 동일 선상 == 2개, 대각선 1개
        if i - ei == 0:                                # x축 동일 (위, 아래 정사각형)
            dist = abs(j-ej)
            for ti in range(i-dist, i+1):
                if in_range(ti, min(j, ej)):
                    squere.append([ti, min(j, ej), dist+1])
        if j - ej == 0:                              # y축 동일 (왼쪽, 오른쪽 정사각형)
            dist = abs(i-ei)
            for tj in range(j-dist, j+1):
                if in_range(min(i, ei), tj):
                    squere.append([min(i, ei), tj, dist+1])
        if abs(i-ei) == abs(j-ej):               # 대각선 (왼아, 오위, 왼위, 오아)
            if in_range(min(i, ei), min(j, ej)):
                squere.append([min(i, ei), min(j, ej), abs(i-ei)+1])

    if not squere:
        continue
    squere.sort(key = lambda x : (x[2], x[0], x[1]))
    # print(squere)
    si, sj, n = squere[0][0], squere[0][1], squere[0][2]
    # print(si, sj, n)

    # 정사각형 크기
    # 90도 회전
    n_maze = [a[:] for a in maze]
    # print('회전')
    maze = rotate(n_maze, si, sj, n)
    # for g in maze:
    #     print(*g)
    # print()
    # for i in range(1, M+1):
    #     print(i, '번째 러너(rotate_after):', runner[i])
    # print()

ans = 0
for i in range(1, M+1):
    ans += runner[i][2]
print(ans)
print(*find_exit(1))