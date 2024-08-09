n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def check(x, y):
    rtn = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
           if arr[i][j] == 1:
            rtn += 1 
    return rtn

rtn = 0
for i in range(n):
    for j in range(n):
        di, dj = i + 2, j + 2
        if not in_range(di, dj):
            break
        rtn = max(rtn, check(i, j))

print(rtn)