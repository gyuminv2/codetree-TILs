# 최소 크기 : 1
# 최대 크기 : n(5)
# 횟수 (예시 기준) : 3
# 그렇다면 1 3 5 (for) 만큼만 하면 됨
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

mx_gold = -1
for k in range(n//2+1):
    for i in range(n):
        for j in range(n):
            cur_gold = 0
            payment = 0
            if k != 0:
            # 주위 4방향
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = (di + i) * k, (dj + j) * k
                    if 0<=ni<n and 0<=nj<n:
                        if grid[ni][nj] == 1:
                            payment += 1
                            cur_gold += m
            # 사각형
            for ni in range(i-(k-1), i+(k-1)+1):
                for nj in range(j-(k-1), j+(k-1)+1):
                    if 0<=ni<n and 0<=nj<n:
                        if grid[ni][nj] == 1:
                            payment += 1
                            cur_gold += m
            # 체굴한 금 검사
            if cur_gold >= payment:
                mx_gold = max(mx_gold, cur_gold)
    
print(mx_gold//m)