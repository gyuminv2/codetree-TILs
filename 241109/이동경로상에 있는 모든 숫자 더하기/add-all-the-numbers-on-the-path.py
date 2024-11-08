n, t = map(int, input().split())
cmd = input()
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 위 오 아 왼
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

dirs = [0, 1, 2, 3]

s = n // 2
ret = []
ret.append(grid[s][s])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def letsGo():
    cur = [s, s, 0]
    for i in range(t):
        if cmd[i] == 'R':
            cur[2] = (cur[2]+1)%4
        elif cmd[i] == 'L':
            cur[2] = (cur[2]+3)%4
        else :
            nx = cur[0] + dxs[dirs[cur[2]]]
            ny = cur[1] + dys[dirs[cur[2]]]
            if in_range(nx, ny):
                cur[0], cur[1] = nx, ny
                ret.append(grid[ny][nx])
letsGo()
print(sum(ret))