s = input()

dir_num = 3 
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

cur_dir = 3

for i in s:
    if i == 'L':
        cur_dir = (cur_dir + 3) % 4
    elif i == 'R':
        cur_dir = (cur_dir + 1) % 4
    elif i == 'F':
        x += dx[cur_dir]
        y += dy[cur_dir]
print(x, y)