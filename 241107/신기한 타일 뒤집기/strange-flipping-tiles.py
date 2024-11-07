n = int(input())

tile = [-1 for _ in range(1000)]
arr = []
for i in range(n):
    arr.append(input().split())

idx = -1
for i in range(n):
    move = int(arr[i][0])
    dirs = arr[i][1]
    if dirs == 'L':
        for j in range(move):
            tile[idx] = 1
            idx -= 1
        idx += 1
    else :
        for j in range(move):
            tile[idx] = 0
            idx += 1
        idx -= 1
    # print(*tile, idx)

print(tile.count(1), tile.count(0))