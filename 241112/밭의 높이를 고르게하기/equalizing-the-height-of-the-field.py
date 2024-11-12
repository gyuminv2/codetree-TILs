n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

ret = []
for i in range(n-t+1):
    comp = arr[i:i+t]
    cnt = 0
    for j in range(t):        
        while comp[j] != h:
            if comp[j] > h:
                comp[j] -= 1
            elif comp[j] < h:
                comp[j] += 1
            cnt += 1
    ret.append(cnt)
print(min(ret))