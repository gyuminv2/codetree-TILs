import datetime

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
A = input()

# 요일을 문자열로 매핑
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 시작 날짜와 종료 날짜 생성
start_date = datetime.date(2024, m1, d1)
end_date = datetime.date(2024, m2, d2)

# 특정 요일의 개수 세기
count = 0
current_date = start_date

while current_date <= end_date:
    if days[current_date.weekday()] == A:
        count += 1
    current_date += datetime.timedelta(days=1)

# 결과 출력
print(count)