k, n = map(int, input().split())

ans = []

f = k
def gang(k, n):
    if k == 0:
        return
    for i in range(f):
        ans.append(i+1)
        if len(ans) == n:
            print(*ans)
        gang(k-1, n)
        ans.pop()

if k != 1:
    gang(k, n)
else:
    gang(k+1, n)