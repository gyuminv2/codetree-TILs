n, m = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

row_arr = []
col_arr = []
ans = 0
# 행
for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(arr[i][j])
    row_arr.append(tmp)
# print(*row_arr)


for i in range(n):
    repeat = 1
    mx_repeat = 0
    for j in range(n-1):
        if row_arr[i][j] == row_arr[i][j+1]:
            repeat += 1
        else:
            mx_repeat = max(mx_repeat, repeat)
            repeat = 1
    mx_repeat = max(mx_repeat, repeat)
    if mx_repeat >= m:
        # print(mx_repeat)
        ans += 1

# 열
for i in range(n):
    col_arr.append([*arr[i]])
# print(*col_arr)

for i in range(n):
    repeat = 1
    mx_repeat = 0
    for j in range(n-1):
        if col_arr[i][j] == col_arr[i][j+1]:
            repeat += 1
        else:
            mx_repeat = max(mx_repeat, repeat)
            repeat = 1
    mx_repeat = max(mx_repeat, repeat)
    if mx_repeat >= m:
        # print(mx_repeat)
        ans += 1
print(ans)