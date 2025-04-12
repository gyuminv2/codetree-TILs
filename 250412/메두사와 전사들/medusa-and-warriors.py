# 유클리드 거리
def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2

# 격자 안
def in_range(x, y):
    return 0<=x<N and 0<=y<N

# route 찾기
from collections import deque
def find_route(si, sj, ei, ej):
    v = [[0]*N for _ in range(N)]
    route = []
    q = deque([(si, sj, route)])
    v[si][sj] = 1

    while q:
        i, j, r = q.popleft()
        if (i, j) == (ei, ej):
            return r
        mn_dist = distance(i, j, ei, ej)
        ci, cj = -1, -1
        for dr in [0, 4, 6, 2]:
            ni, nj = i + dis[dr], j + djs[dr]
            if in_range(ni, nj) and v[ni][nj] == 0 and grid[ni][nj] == 0:
                v[ni][nj] = 1
                q.append((ni, nj, r + [(ni, nj)]))
                dist = distance(ni, nj, ei, ej)
                if mn_dist > dist:
                    mn_dist = dist
                    ci, cj = ni, nj
    return -1

####################
####################
N, M = map(int, input().split())
msi, msj, mei, mej = map(int, input().split())
tmp_input = list(map(int, input().split()))
warrier = dict()
for i in range(0, M*2, 2):
    # [wi, wj, stone, attack, dead]
    warrier[(i+1)//2+1] = [tmp_input[i], tmp_input[i+1], 0, 0, 0]
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
# 0상 1상우 2우 3하우 4하 5하좌 6좌 7상좌
dis = [-1, -1, 0, 1, 1, 1, 0, -1]
djs = [0, 1, 1, 1, 0, -1, -1, -1]





route = find_route(msi, msj, mei, mej)
if route == -1:
    print(-1)
else:
    # [1] 메두사 이동
    # mi, mj : 다음 이동 장소 (i, j => mi, mj)
    # mi, mj 자리에 warrier가 존재하면 해당 w 사망
    for mi, mj in route:
        for w in warrier:
            i, j, s, a, d = warrier[w]
            if d == 1:
                continue
            if (mi, mj) == (i, j):
                warrier[w] = [i, j, s, a, 1]
        
        # [2] 메두사 시선 (상 하 좌 우)
        mx_stone = 0
        sdr = 0
        for dr in [0, 4, 6, 2]:
            t_stone = 0
            tv = [[0]*N for _ in range(N)]
            # 보이는 영역 : 1
            # 안보이는 영역 : 2 + 0
            # 용사는 따로 관리 (stone으로..)
            # 용사 만났는지 여부
            flg = 0
            # dr 방향
            # nmi, nmj : 다음 위치
            nmi, nmj = mi + dis[dr], mj + djs[dr]
            while in_range(nmi, nmj) and tv[nmi][nmj] == 0:
                # 전사랑 부딪히는지 check
                t_stone, flg = check_warrier(t_stone, flg)
                for w in warrier:
                    i, j, _, _, d = warrier[w]
                    if d == 1:
                        continue
                    if (nmi, nmj) == (i, j):
                        t_stone += 1
                        flg = 1
                tv[nmi][nmj] = 1
                # flg == 1 이라는 것은 그 이후 전부 2로 처리
                if flg == 1:
                    nnmi, nnmj = nmi + dis[dr], nmj + djs[dr]
                    while in_range(nnmi, nnmj) and tv[nnmi][nnmj] == 0:
                        tv[nnmi][nnmj] = 2
                        nnmi, nnmj = nnmi + dis[dr], nnmj + djs[dr]
                nmi, nmj = nmi + dis[dr], nmj + djs[dr]

            # (dr-1), (dr+1) 방향
            # (dr-1) = ndr 방향으로 1칸 이동 후 -> dr 방향으로 쭉 (반복)
            flg = 0
            # for ndr in (dr-1), (dr+1):





            if mx_stone < t_stone:
                mx_stone = t_stone
                sdr = dr
        print(mx_stone, sdr)
        for g in tv:
            print(*g)
        print()

                
            

# for i in range(1, M+1):
#     print(warrier[i])