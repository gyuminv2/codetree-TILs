n = int(input())
# visited = [[0] * (n+1)] * (n+1)
visited =[[0 for _ in range(n+1)] for _ in range(n+1)]
# print(*visited)
ans = []

def choose(c):
    if c == n+1:
        print(*ans)
        return

    for i in range(1, n+1):
        if visited[i] == True:
            continue

        visited[i] = True
        ans.append(i)

        choose(c + 1)

        ans.pop()
        visited[i] = False

choose(1)