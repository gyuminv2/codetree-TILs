n = int(input())

arr = []
cnt = 0
cnt_arr = []
for i in range(n):
    arr.append(int(input()))
    if i == 0:
        continue
    elif arr[i] == arr[i-1]:
        cnt += 1
    else:
        cnt_arr.append(cnt)
        cnt = 0

print(max(cnt_arr)+1)