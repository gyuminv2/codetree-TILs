n, t = map(int, input().split())

arr = []
arr.append(list(map(int, input().split())))

ret = []
cnt = 0
for i in range(n):
    if arr[0][i] > t:
        cnt += 1
    else:
        ret.append(cnt)
        cnt = 0
    ret.append(cnt)

if not ret:
    print(1)
else:
    print(max(ret))