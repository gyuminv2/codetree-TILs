# N x N : 격자
# M : 게임 턴 수
# P : 산타 수
# 거리는 피타고라스

# [0] M만큼 진행

# [1] 루돌프의 움직임
# 가장 가까운 산타를 향해 1칸 돌진
# 동일한 거리의 산타라면 r, c 순
# 8방향 (가까운 방향)

# [2] 산타의 움직임
# 1~P 까지 move
# 탈락, 기절 산타는 움직일 수 없음
# 루돌프와 가장 가까운 방향으로 1칸 이동
# 가까워질 방법이 없다면 움직일 수 없음
# 4방향 (상우하좌)

# [3] 충돌
# 루돌프 -> 산타 : 산타(C획득, 루돌프 방향 반대로 C칸 밀려남)
# 산타 -> 루돌프 : 산타(D획득, 산타 방향 반대로 D칸 밀려남)
# 밀려난 위치(1개)가
# - 격자 밖이면 탈락
# - 다른 산타 있을 경우 상호작용

# [4] 상호작용
# 부딪힌 산타는 부딪힌 방향 반대인 1칸 뒤로 밀려남 (반복)
# 격자 밖이면 탈락

# [5] 기절
# 루돌프와 충돌한 산타는 기절(2턴) : 움직일 수 없지만, 상호작용은 가능
# 루돌프는 기절한 산타를 대사응로 선택 가능

# [6] 종료
# P명의 산타가 모두 탈락이면 게임 종료
# 매 턴 이후 탈락하지 않은 산타는 점수 += 1점
# 종료 후 각 산타가 얻은 최종 점수 구함

# for _ in range(m):
#     r_move() -> 충돌 -> 상호작용 -> 기절
#     종료 체크
#     s_move() -> 충돌 -> 상호작용 -> 기절
#     종료 체크

def get_score():
    for i in range(1, p+1):
        print(santa[i][3], end=' ')

def ending_check():
    for i in range(1, p+1):
        if santa[i][2] == 0:
            return 0
    return 1                # 종료

def distance(r1, c1, r2, c2):
    return (r1-r2)**2 + (c1-c2)**2

def in_range(x, y):
    return 0<=x<n and 0<=y<n

# boom(산타_idx, 루돌프 충돌 방향) , 항상 산타 존재
def boom(idx, dr, flg, flow):
    if santa[idx][2] == 1:
        return
    s_f = 0
    cnt = 0
    if flg == 'r':
        flg = c
        cnt = c
        dr = (dr+4)%8
    elif flg == 's':
        flg = d
        cnt = d-1
    elif flg == 'a':
        flg = 1
        cnt = 1
        s_f = 1
    # 반대 방향
    if s_f == 0:
        dr = (dr+4)%8
    # 충돌 (다른 산타 존재 여부)
    if s_f == 0:
        santa[idx][1] = 2
    # 3, 2
    x, y = santa[idx][0][0], santa[idx][0][1]
    nx, ny = x + (cnt*dis[dr]), y + (cnt*djs[dr])
    # print('방향 :', dr, s_f)
    # 범위 체크
    # print('산타 좌표 :', x, y)
    # print('밀려난 좌표 :', nx, ny)
    if in_range(nx, ny):
        # 다른 산타가 있을 경우
        if grid[nx][ny] != 0 and (x, y) != (nx, ny):
            # print(grid[nx][ny], ' 산타 좌표(다음) :', nx, ny)
            boom(grid[nx][ny], dr, 'a', 1)
        grid[nx][ny] = grid[x][y]
        santa[idx][0][0], santa[idx][0][1] = nx, ny
        if (x, y) != (nx, ny):
            grid[x][y] = 0
    else:   # 종료
        santa[idx][2] = 1
        grid[x][y] = 0
    # 점수
    if s_f == 0:
        santa[idx][3] += flg

def r_move(ri, rj):
    min_dist = 987654321
    direct = 0
    sidx = -1
    for i in range(1, p+1):
        # 종료 산타 넘기기
        if santa[i][2] == 1:
            continue
        # x : santa[i][0][0], y : santa[i][0][1]
        dist = distance(ri, rj, santa[i][0][0], santa[i][0][1])
        if min_dist > dist:
            min_dist = dist
            sidx = i
        elif min_dist == dist:
            if santa[sidx][0][0] < santa[i][0][0]:
                sidx = i
            elif santa[sidx][0][0] == santa[i][0][0]:
                if santa[sidx][0][1] < santa[i][0][1]:
                    sidx = i
    # print('다음 산타 :', sidx)
    # print('루돌프 위치 :', (ri, rj))
    # 산타 향해 돌진 (산타 번호 : sidx, 거리 : min_dist)
    # 충돌, 상호작용, 기절
    move = 0
    for dr in [0, 1, 2, 3, 4, 5, 6, 7]:
        ni, nj = ri + dis[dr], rj + djs[dr]
        nxt_dist = distance(ni, nj, santa[sidx][0][0], santa[sidx][0][1])
        if in_range(ni, nj) and nxt_dist < min_dist:
            min_dist = nxt_dist
            nri, nrj = ni, nj
            direct = dr
            move = 1
    if move == 1:
        # 루돌프 위치 : nri, nrj
        if grid[nri][nrj] != 0:     # 산타가 있으면 충돌
            boom(sidx, direct, 'r', 0)
        grid[nri][nrj] = -1
        grid[ri][rj] = 0
        ri, rj = nri, nrj
    return ri, rj

def s_move(ri, rj):
    # 각각 산타마다<->루돌프 거리 체크
    # print('루돌프 위치 :', ri, rj)
    for i in range(1, p+1):
        if santa[i][2] == 1:
            continue
        if santa[i][1] != 0:
            continue
        direct = 0
        si, sj = santa[i][0][0], santa[i][0][1]
        dist = distance(ri, rj, si, sj)
        # 1칸 이동 (최소거리, 상우하좌)
        move = 0
        for dr in [0, 2, 4, 6]:
            ni, nj = si + dis[dr], sj + djs[dr]
            # 움직인 곳이 루돌프, 다른 산타가 아니라면
            ndist = distance(ri, rj, ni, nj)
            if in_range(ni, nj) and grid[ni][nj] <= 0 and ndist < dist:
                dist = ndist
                nsi, nsj = ni, nj
                direct = dr
                move = 1
        if move == 1:
            # 루돌프와 충돌
            # nsi, nsj : 다음 산타 좌표
            if grid[nsi][nsj] == -1:
                boom(i, direct, 's', 0)
            else:               # 빈칸이면
                grid[nsi][nsj] = i
                grid[si][sj] = 0
                santa[i][0][0], santa[i][0][1] = nsi, nsj

####################
####################

# 산타 : p
# 루돌프 : -1
n, m, p, c, d = map(int, input().split())
grid = [
    [0] * n
    for _ in range(n)
]
ri, rj = map(int, input().split())
# 루돌프 위치 표시
grid[ri-1][rj-1] = -1
santa = dict()
for _ in range(p):
    num, si, sj = map(int, input().split())
    # 산타[번호] = [0: 좌표, 1: 기절 턴, 2: 종료, 3: 점수]
    santa[num] = [[si-1, sj-1], 0, 0, 0]
    grid[si-1][sj-1] = num

# 상 우상 우 우하 하 좌하 좌 좌상
# 산타 : 0, 2, 4, 6 (우선순위)
dis = [-1, -1, 0, 1, 1, 1, 0, -1]
djs = [0, 1, 1, 1, 0, -1, -1, -1]

ri, rj = ri-1, rj-1
for k in range(m):
    ri, rj = r_move(ri, rj)
    # print(k, ': 루돌프 이동 ################')
    # for v in grid:
    #     print(v)
    if ending_check():
        break
    s_move(ri, rj)
    # print(k, ': 산타 이동 ################')
    # for v in grid:
    #     print(v)
    if ending_check():
        break
    # 기절 감소, 총점 올려 (탈락 산타 제외)
    for i in range(1, p+1):
        # print(i, ': 산타 출력 =', santa[i])
        if santa[i][2] == 1:
            continue
        if santa[i][1] != 0:
            santa[i][1] -= 1
        santa[i][3] += 1
get_score()