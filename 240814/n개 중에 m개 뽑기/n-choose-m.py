k, n = map(int, input().split())
ans = []

def sort(ans, n):
    for i in range(n-1):
        if ans[i] >= ans[i+1]:
            return False
    return True

def check_last(ans, j):
    if len(ans) >= 1:
            if j <= ans[len(ans)-1]:
                return True
    return False

def rc(i):
    if i == 0:
        return
    for j in range(1, k+1):
        if check_last(ans, j) == True:
            continue
        ans.append(j)
        if len(ans) == n:
            if sort(ans, n) == True:
                print(*ans)
        rc(i-1)
        ans.pop()

rc(n)