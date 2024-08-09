n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = 0

x, y = 0, 0

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < m:
        if arr[x][y] == 0:
            return True
    return False

arr[0][0] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny):
        dir_num = (dir_num + 1) % 4
    x += dxs[dir_num]
    y += dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()