n = int(input())

f_dir = [0, 0]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    dist, jump = input().split()
    jump = int(jump)
    if dist == 'N':
        f_dir[1] += jump * dy[1]
    elif dist == 'E':
        f_dir[0] += jump * dx[2]
    elif dist == 'S':
        f_dir[1] += jump * dy[3]
    else:
        f_dir[0] += jump * dx[0]

print(f_dir[0], f_dir[1])