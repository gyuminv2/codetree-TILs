k, n = map(int, input().split())

ans = []

def rc(cnt):
    if cnt == n+1:
        print(*ans)
        return

    for j in range(1, k+1):
        ans.append(j)
        rc(cnt+1)
        ans.pop()

rc(1)