n, t = map(int, input().split())

arr = []
arr.append(list(map(int, input().split())))

ret = []
cnt = 0
for i in range(n-1):
    nxt = arr[0][i+1]
    if i == 0:
        continue
    if arr[0][i]+1 == nxt:
        cnt += 1
    else:
        ret.append(cnt)
        cnt = 0
    ret.append(cnt)

print(max(ret)+1)