m1, d1, m2, d2 = map(int, input().split())

A = input()

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ["Mon", 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
diff = sum(num_of_days[1:m2]) + d2 - (sum(num_of_days[1:m1]) + d1)

cnt = 0
number = diff - day.index(A)

cnt = (number + 7) // 7

print(cnt)