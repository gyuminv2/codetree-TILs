# move_man, TARGET : CU
def move_man(idx):
    # print(idx, 'move_man')
    flg = 0
    mi, mj = find_man(idx)
    if (mi, mj) == (-1, -1):
        for i, j, x in save_man:
            if idx == x:
                # print('여기다!')
                mi, mj = i, j
                flg = 2
                break

    # print(grid[mi][mj])
    ci, cj = find_cu(-idx)
    ri, rj = mi, mj
    # man의 초기 이동일 경우 -> (현재 위치 값 : idx => 999로 변경 (원래 베이스캠프 위치로..))
    if [mi, mj] in base_camp:
        flg = 1
        base_camp.pop(base_camp.index([mi, mj]))
    
    mn_dist = abs(mi-ci) + abs(mj-cj)
    for dr in [0, 1, 2, 3]:
        ni, nj = mi + dis[dr], mj + djs[dr]
        dist = abs(ni-ci) + abs(nj-cj)
        # 격자 체크 (0보다 크면 안됨)
        if 0<=ni<n and 0<=nj<n and grid[ni][nj] <= 0:
            # 편의점 도착
            if (ni, nj) == (ci, cj):
                if flg == 1:
                    grid[mi][mj] = 999
                elif flg != 2:
                    grid[mi][mj] = 0
                grid[ni][nj] = idx
                return 1
            if mn_dist > dist:
                mn_dist = dist
                ri, rj = ni, nj
        if flg == 1:
            grid[mi][mj] = 999
        elif flg != 2:
            grid[mi][mj] = 0
        if grid[ri][rj] not in test_arr:
            grid[ri][rj] = idx
        else:
            save_man.append((ri, rj, idx))
    # for v in grid:
    #     print(*v)
    return 0


# bfs : return [i, j, d]
from collections import deque
def bfs(si, sj, ei, ej):
    v = [[0] * n for _ in range(n)]
    q = deque([(si, sj, 0)])
    v[si][sj] = 1
    d = 0
    
    while q:
        si, sj, d = q.popleft()
        if (si, sj) == (ei, ej):
            return [si, sj, d]

        for dr in [0, 1, 2, 3]:
            ni, nj = si + dis[dr], sj + djs[dr]
            # 안되면 grid 조건 제외하고 해보삼
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and grid[ni][nj] <= 0:    # or [ni, nj, _] in save_man):
                v[ni][nj] = 1
                q.append((ni, nj, d+1))
    
    return [999, 999, 999]

# idx번 Man 찾기
def find_man(idx):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == idx:
                return i, j
    return -1, -1

# t번 편의점 찾기
def find_cu(t):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == t:
                return i, j

def find_base():
    valid_base = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -999:
                valid_base.append((i, j))
    return valid_base

####################
####################
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 베이스 캠프 -999 로 변경
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            grid[i][j] = -999


man = dict()
# 편의점, 사람 추가
for num in range(1, m+1):
    i, j = map(int, input().split())
    grid[i-1][j-1] = -num
    # 격자 안에 들어간 정보, 도착 정보
    man[num] = [0, 0]

dis = [-1, 0, 0, 1]
djs = [0, -1, 1, 0]
# 격자 출력 test
# for v in grid:
#     print(*v)

# 베이스 캠프 : -999 였다가, 사람이 발견하면 사람이 들어갔다가, 출발하면 999로 변경
# 사람 : 1 ~ 15
# 편의점 : -(1 ~ 30)
save_man = []
test_arr = [i for i in range(-15, 0)]

# 도착하면 1로 변경 (베이스 캠프 속에 사람 = (-1 => 1)) -> 1 찾으러 감
base_camp = []
t = 1
while 1:
    # 종료 조건 (모두 도착)
    end = 0
    for idx in range(1, m+1):
        _, e = man[idx]
        if e == 1:
            end += 1
    if end == m:
        break
    
    for idx in range(1, m+1):
        # 격자 포함, 종료 여부
        g, e = man[idx]
        if e == 1 or g == 0:
            continue
        
        # [1] : 1칸 이동 (idx번째 man이 -idx번째 편의점을 향해..)
        if move_man(idx) == 1:
            man[idx] = [1, 1]
    
    # 격자에 사람 추가
    if t <= m:
        # t번 편의점 찾기
        # print(t, '번째')
        # for v in grid:
        #     print(*v)
        # print()
        ci, cj = find_cu(-t)

        # t번 편의점과 가장 가까운 베이스캠프 찾기
        # i, j, d (좌표, 거리) (i와 j는 !무조건! 베이스 캠프 위치)
        can_base = []
        base = find_base()
        for bi, bj in base:
            can_base.append(bfs(ci, cj, bi, bj))
        # print(*can_base)
        can_base.sort(key = lambda x : (x[2], x[0], x[1]))
        # print(*can_base)
        # si, sj == 선택된 베이스캠프
        si, sj = can_base[0][0], can_base[0][1]
        # grid에 정보 최신화 (베이스캠프 -> 사람(t))
        base_camp.append([si, sj])
        grid[si][sj] = t
        man[t] = [1, 0]
    # 1번
    # 2번


    t += 1
    # print(t-1, '초')
    # for v in grid:
    #     print(*v)
    # print()
    # if t == 7:
    #     break
print(t-1)