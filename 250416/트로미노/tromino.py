# 4개 + 2개 => 6개 검사

n, m = map(int, input().split())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def in_range(x, y):
    return 0<=x<n and 0<=y<m

mx_sum = -1
for i in range(n):
    for j in range(n):
        # --- 모양
        if in_range(i, j+2):
            mx_sum = max(mx_sum, arr[i][j] + arr[i][j+1] + arr[i][j+2])
        # |
        # |
        # | 모양
        if in_range(i+2, j):
            mx_sum = max(mx_sum, arr[i][j] + arr[i+1][j] + arr[i+2][j])
        # ㄱ 모양
        if in_range(i+1, j+1):
            mx_sum = max(mx_sum, arr[i][j] + arr[i][j+1] + arr[i+1][j+1])
        # _| 모양
        if in_range(i+1, j+1):
            mx_sum = max(mx_sum, arr[i][j+1] + arr[i+1][j+1] + arr[i+1][j])
        # ㄴ 모양
        if in_range(i+1, j+1):
            mx_sum = max(mx_sum, arr[i][j] + arr[i+1][j] + arr[i+1][j+1])
        # |- 모양
        if in_range(i+1, j+1):
            mx_sum = max(mx_sum, arr[i][j] + arr[i][j+1] + arr[i+1][j])
print(mx_sum)            