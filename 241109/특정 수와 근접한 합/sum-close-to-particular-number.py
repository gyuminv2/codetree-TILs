n, s = map(int, input().split())
arr = list(map(int, input().split()))

ret = []
for i in range(n-1):
    a = arr[i]
    for j in range(i+1, n):
        b = arr[j]
        tp = sum(arr) - (a+b)
        ret.append(tp)

ret.sort()
mins = 100
for i in ret:
    if s - i < mins:
        mins = s - i
print(mins)