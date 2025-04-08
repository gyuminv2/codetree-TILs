from collections import deque

def bfs(arr, v, i, j, flg):
    sset = set()
    q = deque([(i, j)])
    v[i][j] = 1
    sset.add((i, j))
    cnt = 1

    while q:
        i, j = q.popleft()
        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj] == 0 and arr[i][j] == arr[ni][nj]:
                v[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
                sset.add((ni, nj))
        
    if cnt >= 3:
        if flg == 1:
            for x, y in sset:
                arr[x][y] = 0
        return cnt
    else:
        return 0


def count_clear(arr, flg):          # flg == 1일 때 3개 이상 값을 0으로 clear
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                cnt += bfs(arr, v, i, j, flg)
    return cnt

def rotate(arr, si, sj):
    n_arr = [a[:] for a in arr]
    for i in range(3):
        for j in range(3):
            n_arr[si+i][sj+j] = arr[si+3-j-1][sj+i]
    return n_arr

######################
######################
k, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(5)
]
gold = list(map(int, input().split()))
ans = []
dis = [-1, 1, 0, 0]
djs = [0, 0, -1, 1]

# FOR : k, rotate(1, 2, 3), (열, 행)(0~3), 원소(0~5), bfs
for _ in range(k):
    # [1] 탐사 진행
    mx_cnt = 0
    for r in [1, 2, 3]:                         # 90, 180, 270 회전
        for j in range(3):                      # 열 좌표
            for i in range(3):                  # 행 좌표
                n_grid = [x[:] for x in grid]     # 복사
                print(n_grid)
                for _ in range(r):
                    n_grid = rotate(n_grid, i, j)
                
                t_cnt = count_clear(n_grid, 0)
                if t_cnt > mx_cnt:
                    mx_cnt = t_cnt
                    m_grid = n_grid
    
    if mx_cnt == 0:
        break
    
    # [2] 연쇄 획득
    cnt = 0
    grid = m_grid
    while 1:
        t_cnt = count_clear(grid, 1)
        if t_cnt == 0:
            break
        cnt += t_cnt

        for j in range(5):
            for i in range(4, -1, -1):
                if grid[i][j] == 0:
                    grid[i][j] = gold.pop(0)

    ans.append(cnt)
print(*ans)