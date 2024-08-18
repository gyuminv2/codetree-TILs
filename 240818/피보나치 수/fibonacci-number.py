# 2, 3, 5, 8

n = int(input())

a = []
a.append(1)
a.append(1)

def f(n):
    for i in range(2, n+1):
        a.append(a[i-2] + a[i-1])
f(n)
print(a[n-1])