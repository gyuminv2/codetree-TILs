k, n = map(int, input().split())

ans = []

def gang(k, n):
    if k == 0:
        return
    for i in range(1, n+1):
        ans.append(i)
        gang(k-1, n)
        if len(ans) == 3:
            print(*ans)
        ans.pop()

def __for(ans):
    for i in range(len(ans)):
        print(ans[i])

gang(k, n)
__for(ans)