def in_range(x, y):
    return 0<=x<L and 0<=y<L

# 고려해야 할 것
# 1. 벽에 걸리는지, 맵 밖으로 나가는지 -> 바로 return (아무일도 일어나지 않음)
# 2. 움직일 곳에 다른 좌표가 존재할 때 -> nq에 저장 : while로 처리 (연쇄처리)
def knight_move(idx, dr):
    q = [] # queue.
    nset = set()
    attack = [0] * (N+1)
    q.append(idx)
    nset.add(idx)

    while q:
        nidx = q.pop(0)
        ci, cj, h, w, _ = knight[nidx]
        ni, nj = ci + dis[dr], cj + djs[dr]

        # 맵 선회하며 벽, 맵 check와 공격 check
        for i in range(ni, ni+h):
            for j in range(nj, nj+w):
                if not in_range(i, j) or grid[i][j] == 2:
                    return
                if grid[i][j] == 1 and nidx != idx:
                    attack[nidx] += 1

        # 겹치는 기사가 있다면 q에 추가 (모든 기사 탐색)
        for sidx in knight:
            # 이미 움직일 대상 체크 X
            if sidx in nset: continue
            
            ti, tj, th, tw, _ = knight[sidx]
            if ni <= ti+th-1 and ni+h-1 >= ti and nj+w-1 >= tj and nj <= tj+tw-1:
                q.append(sidx)
                nset.add(sidx)
    # attack[idx] = 0
    # 움직임
    for idx in nset:
        si, sj, h, w, k = knight[idx]
        if k <= attack[idx]:
            knight.pop(idx)
        else:
            ni, nj = si + dis[dr], sj + djs[dr]
            knight[idx] = [ni, nj, h, w, k - attack[idx]]

####################
####################
L, N, Q = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(L)
]
knight = {}
init_damage = [0] * (N+1)
for i in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    knight[i] = [r-1, c-1, h, w, k]
    init_damage[i] = k
cmd = []
for _ in range(Q):
    cmd.append(list(map(int, input().split())))
# 위 오 아 왼
dis = [-1, 0, 1, 0]
djs = [0, 1, 0, -1]

# 메인 로직
for idx, dr in cmd:
    # 죽은 기사 건너뛰기
    if idx in knight:
        knight_move(idx, dr)
        
ans = 0
for i in knight:
    ans += init_damage[i] - knight[i][4]
print(ans)