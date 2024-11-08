# 입력 받기
n, t = map(int, input().split())
cmd = input()
grid = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (북, 동, 남, 서)
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

# 시작 위치 (격자 중앙) 및 초기 방향 (북쪽)
x, y = n // 2, n // 2
direction = 0  # 북쪽: 0, 동쪽: 1, 남쪽: 2, 서쪽: 3

# 방문 위치와 누적합 초기화
visited = set()
visited.add((x, y))
total_sum = grid[y][x]  # 시작 위치 값 포함

# 범위 검사 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 명령어 처리
for i in range(t):
    if cmd[i] == 'L':
        direction = (direction - 1) % 4  # 왼쪽으로 90도 회전
    elif cmd[i] == 'R':
        direction = (direction + 1) % 4  # 오른쪽으로 90도 회전
    elif cmd[i] == 'F':
        # 현재 방향으로 이동
        nx, ny = x + dxs[direction], y + dys[direction]
        # 격자 범위 내인지 확인
        if in_range(nx, ny):
            x, y = nx, ny
            # 새로운 위치의 값을 누적합에 추가 (처음 방문할 때만)
            if (x, y) not in visited:
                visited.add((x, y))
                total_sum += grid[y][x]

# 결과 출력
print(total_sum)