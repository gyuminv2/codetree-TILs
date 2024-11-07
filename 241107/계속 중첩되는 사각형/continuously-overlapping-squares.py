# 좌표 평면의 크기 정의 (-100 <= x, y <= 100 이므로 200x200 크기의 배열을 사용)
OFFSET = 100  # 좌표의 범위가 -100 ~ 100이므로, 0 ~ 200 인덱스를 사용하기 위해 오프셋 적용
plane = [[0] * 201 for _ in range(201)]  # 0: 없음, 1: 빨간색, 2: 파란색

def calculate_blue_area(rectangles):
    for i, (x1, y1, x2, y2) in enumerate(rectangles):
        color = 1 if i % 2 == 0 else 2  # 짝수 인덱스 -> 빨간색(1), 홀수 인덱스 -> 파란색(2)
        for x in range(x1 + OFFSET, x2 + OFFSET):
            for y in range(y1 + OFFSET, y2 + OFFSET):
                plane[x][y] = color  # 현재 색상으로 덮음

    # 파란색 영역의 넓이 계산
    blue_area = sum(1 for x in range(201) for y in range(201) if plane[x][y] == 2)
    return blue_area

# 입력 받기
n = int(input())
rectangles = [tuple(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(calculate_blue_area(rectangles))