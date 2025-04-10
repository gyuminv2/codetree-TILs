def repair(route, ai, aj):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            elif (i, j) == (ai, aj):
                continue
            elif (i, j) not in route:
                grid[i][j] += 1

def boomb(a, t, damage):
    ai, aj = a[0], a[1]
    ti, tj = t[0], t[1]
    half = damage//2
    route = [(ti, tj)]

    for dr in [0, 1, 2, 3, 4, 5, 6, 7]:
        ni, nj = ti + dis[dr], tj + djs[dr]
        ni, nj = is_nxt_go(ni, nj)
        if grid[ni][nj] != 0 and (ni, nj) != (ai, aj):
            grid[ni][nj] = max(grid[ni][nj] - half, 0)
            route.append((ni, nj))
    grid[ti][tj] = max(grid[ti][tj] - damage, 0)
    return route

def lazer(route, ti, tj, damage):
    half = damage//2
    for i, j in route:
        if (i, j) == (ti, tj):
            grid[i][j] = max(grid[i][j] - damage, 0)
        else:
            grid[i][j] = max(grid[i][j] - half, 0)

def is_nxt_go(x, y):
    if y < 0:           # 왼쪽 -> 오른쪽
        y = y + M
    if y >= M:          # 오른쪽 -> 왼쪽
        y = y - M
    if x < 0:
        x = x + N       # 위 -> 아래
    if x >= N:
        x = x - N       # 아래 -> 위
    return x, y

def in_range(x, y):
    return 0<=x<N and 0<=y<M

from collections import deque
def find_route(a, t):
    route = []
    v = [[0] * M for _ in range(N)]
    q = deque([(a[0], a[1], route)])
    v[a[0]][a[1]] = 1

    while q:
        ci, cj, route = q.popleft()

        if (ci, cj) == (t[0], t[1]):
            return route

        for dr in [0, 2, 4, 6]:
            ni, nj = ci + dis[dr], cj + djs[dr]
            ni, nj = is_nxt_go(ni, nj)
            if v[ni][nj] == 0 and grid[ni][nj] != 0:
                q.append((ni, nj, route+[(ni, nj)]))
                v[ni][nj] = (ci, cj)
    return []


def find_attacker(sequence):
    candidate = []
    mn_a = 987654321
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            # attacker 후보 찾기
            if mn_a >= grid[i][j]:
                mn_a = grid[i][j]
                candidate.append([i, j, grid[i][j]])
    seq = sequence[::-1]
    if len(candidate) > 1:
        can = []
        for i in range(len(candidate)):
            if mn_a == candidate[i][2]:
                can.append(candidate[i])
        # 중복 처리
        for si, sj in seq:
            for i in range(len(can)):
                ci, cj = can[i][0], can[i][1]
                if (si, sj) == (ci, cj):
                    return can[i]
        # 여기까지 왔다는 건, 최근 공격 포탑도 동일
        can.sort(key = lambda x : (x[2], -(x[0]+x[1]), -x[1]))
        return can[0]
    else:
        return candidate[0]

def find_target(attacker, old):
    candidate = []
    ai, aj = attacker[0], attacker[1]
    mn_t = -1
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                continue
            # 공격자 제외
            if (ai, aj) == (i, j):
                continue
            # target 후보 찾기
            if mn_t <= grid[i][j]:
                mn_t = grid[i][j]
                candidate.append([i, j, grid[i][j]])
    if len(candidate) > 1:
        can = []
        for i in range(len(candidate)):
            if mn_t == candidate[i][2]:
                can.append(candidate[i])
        # 중복 처리
        for oi, oj in old:
            for i in range(len(can)):
                ci, cj = can[i][0], can[i][1]
                if (oi, oj) == (ci, cj):
                    return can[i]
        # 여기까지 왔다는 건, 최근 공격 포탑도 동일
        can.sort(key = lambda x : (-x[2], x[0]+x[1], x[1]))
        return can[0]
    else:
        return candidate[0]

def left_one():
    one = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 0:
                one += 1
            if one > 1:
                return 0
    return 1

####################
####################
N, M, K = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]
# 우 하우 하 하좌 좌 상좌 상 상우
dis = [0, 1, 1, 1, 0, -1, -1, -1]
djs = [1, 1, 0, -1, -1, -1, 0, 1]
handicap = N+M

# 공격 순서 저장
sequence = []
old = []
for i in range(N):
    for j in range(M):
        old.append((i, j))
old.sort(key = lambda x : (x[0]+x[1], x[1]))
for _ in range(K):
    if left_one():
        break

    a = find_attacker(sequence)

    old.pop(old.index((a[0], a[1])))
    old.append((a[0], a[1]))
    sequence.append((a[0], a[1]))
    grid[a[0]][a[1]] += handicap
    a[2] += handicap

    t = find_target(a, old)
    route = find_route(a, t)
    if route:
        lazer(route, t[0], t[1], a[2])
        repair(route, a[0], a[1])
    else:
        route = boomb(a, t, a[2])
        repair(route, a[0], a[1])

rtn = 0
for i in range(N):
    for j in range(M):
        rtn = max(rtn, grid[i][j])
print(rtn)