n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0

def in_range(x, y):
    if 0 <= x and x < n and 0 <= y and y < m:
        if arr[x][y] == 0:
            return True
    return False

move_dir = 0
arr[x][y] = 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if not in_range(nx, ny):
        move_dir = (move_dir + 1) % 4
    x, y = x + dxs[move_dir], y + dys[move_dir]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()