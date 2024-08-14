n = int(input())
visited = [0] * (n+1)
arr = []

def permu(k):
    if k == 0:
        print(*arr)
        return

    for i in range(n, 0, -1):
        if visited[i] == True:
            continue

        visited[i] = True
        arr.append(i)

        permu(k - 1)

        arr.pop()
        visited[i] = False

permu(n)