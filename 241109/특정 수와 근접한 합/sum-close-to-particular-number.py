n, s = map(int, input().split())
arr = list(map(int, input().split()))

ret = []
for i in range(n-1):
    a = arr[i]
    for j in range(i+1, n):
        b = arr[j]
        tp = sum(arr) - (a+b)
        if tp - s < 0:
            ret.append(s-tp)
        else:
            ret.append(tp-s)

ret.sort()
print(ret[0])