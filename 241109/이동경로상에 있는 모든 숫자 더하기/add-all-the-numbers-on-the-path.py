n, t = map(int, input().split())
cmd = input()
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 상, 우, 하, 좌 방향 이동
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

dirs = [0, 1, 2, 3]

# 중앙 시작
s = n // 2
ret = []
ret.append(grid[s][s])

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def letsGo():
    cur = [s, s, 0]  # x, y, 방향
    for i in range(t):
        if cmd[i] == 'R':
            cur[2] = (cur[2] + 1) % 4  # 오른쪽으로 회전
        elif cmd[i] == 'L':
            cur[2] = (cur[2] - 1) % 4  # 왼쪽으로 회전
        else:
            # 전진할 위치 계산
            dx = cur[0] + dxs[cur[2]]
            dy = cur[1] + dys[cur[2]]
            if in_range(dx, dy):
                cur[0] = dx
                cur[1] = dy
                # 새 위치에 있는 값을 ret에 추가 (마지막 값과 다른 경우에만)
                if ret[-1] != grid[dy][dx]:  # y, x 순서 주의
                    ret.append(grid[dy][dx])

letsGo()
print(sum(ret))