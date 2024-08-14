k, n = map(int, input().split())

ans = []

def rc(i):
    if i == 0:
        return
    for j in range(1, k+1):
        ans.append(j)
        if len(ans) == n and (len(list(set(ans))) != 1 or i == 1):
            print(*ans)
        rc(i-1)
        ans.pop()

rc(n)