k, n = map(int, input().split())

ans = []

f = k
g = n
def gang(n):
    if n == 0:
        return
    for i in range(f):
        ans.append(i+1)
        if len(ans) == g:
            print(*ans)
        gang(n-1)
        ans.pop()

gang(n)