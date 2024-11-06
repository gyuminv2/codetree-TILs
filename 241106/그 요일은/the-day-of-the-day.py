m1, d1, m2, d2 = map(int, input().split())

# 2024년 m1월 d1일이 월요일 이었다면
# 2024년 m2월 d2까지 A 요일은 몇 번 등장하는지

A = input()

monthOfDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def calDay(m1, d1, m2, d2):
    firstDay = monthOfDay[m1-1] - d1 + 1
    # print('first :', firstDay)
    secondDay = d2
    # print('second :', secondDay)
    gapDay = 0
    for i in range(m1+1, m2):
        gapDay += monthOfDay[i]
    # print('gapDay :', gapDay)
    return firstDay + secondDay + gapDay

total = calDay(m1, d1, m2, d2) // 7
if day[total % 7] == A:
    print(total + 1)
else:
    print(total)