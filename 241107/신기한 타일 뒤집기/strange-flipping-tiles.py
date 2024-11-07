n = int(input())

tile = [-1 for _ in range(1000)]
arr = []
for i in range(n):
    arr.append(input().split())

for i in range(n):
    dirs = arr[i][1]
    for j in range(int(arr[i][0])):
        if dirs == 'L':
            tile[j] = 1
        else :
            tile[j] = 0

print(tile.count(1), tile.count(0))