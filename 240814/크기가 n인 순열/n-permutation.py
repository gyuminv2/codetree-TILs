n = int(input())
visited = [0] * (n+1)
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