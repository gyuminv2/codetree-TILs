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

def in_range(dx, dy):
    if dx >= n or dy >= n:
        return 0
    return 1

def letsGo():
    cur = [s, s, 0]
    for i in range(t):
        if cmd[i] == 'R':
            if cur[2] + 1 == 4:
                cur[2] = dirs[0]
            else :
                cur[2] = dirs[cur[2]+1]
        elif cmd[i] == 'L':
            cur[2] = dirs[cur[2]-1]
        else :
            dx = cur[0] + dys[dirs[cur[2]]]
            dy = cur[1] + dxs[dirs[cur[2]]]
            if in_range(dx, dy):
                cur[0] = dx
                cur[1] = dy
            if ret[-1:] == grid[cur[0]][cur[1]]:
                continue
            else:
                ret.append(grid[cur[0]][cur[1]])
letsGo()
print(sum(ret))