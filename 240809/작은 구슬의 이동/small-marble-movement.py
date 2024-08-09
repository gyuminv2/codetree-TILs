n, t = map(int, input().split())

r, c, d = input().split()
r = int(r)
c = int(c)

dxs = [1, 0, 0, -1]
dys = [0, 1, -1, 0]

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

def in_range(x):
    return 0 < x and x <= n

move_dir = mapper[d]
for i in range(t):
    if move_dir == mapper['R'] or move_dir == mapper['L']:
        nx = c + dxs[move_dir]
        if not in_range(nx):
            move_dir = 3 - move_dir
            continue
        c += dxs[move_dir]
    else:
        ny = r + dys[move_dir]
        if not in_range(ny):
            move_dir = 3 - move_dir
            continue
        r += dys[move_dir]

print(r, c)