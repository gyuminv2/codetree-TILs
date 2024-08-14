k, n = map(int, input().split())
ans = []
tmp = ()

def re(ans, n):
    for i in range(n-2):
        if ans[i] != ans[i+1] and ans[i+1] != ans[i+2]:
            return True
    return False

def sort(ans, n):
    for i in range(n-1):
        if ans[i] >= ans[i+1]:
            return False
    return True

def rc(i):
    if i == 0:
        return
    for j in range(1, k+1):
        ans.append(j)
        if len(ans) == n:
            if sort(ans, n) == True:
                print(*ans)
        rc(i-1)
        ans.pop()

rc(n)