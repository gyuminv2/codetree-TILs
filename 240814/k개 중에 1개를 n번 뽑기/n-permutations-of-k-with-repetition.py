k, n = map(int, input().split())

ans = []

def rc(i):
    if i == 0:
        return

    for j in range(k):
        ans.append(j+1)
        if len(ans) == n:
            print(*ans)
        rc(i-1)
        ans.pop()

rc(n)