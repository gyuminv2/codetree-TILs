n = int(input())
a = []
rtn = 0

# 북 동 남 서
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and a[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            rtn += 1

print(rtn)