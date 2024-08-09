n = int(input())

mapper = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3,
}
in_di = []
in_it = []
x, y = 0, 0
dir_num = 0

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

for i in range(n):
    di, it = input().split()
    in_di.append(di)
    in_it.append(int(it))

rtn = 0
for i in range(n):
    dir_num = mapper[in_di[i]]
    for j in range(in_it[i]):
        x, y = x + dxs[dir_num], y + dys[dir_num]
        rtn += 1
        if x == 0 and y == 0:
            print(rtn)
            exit()
print(-1)