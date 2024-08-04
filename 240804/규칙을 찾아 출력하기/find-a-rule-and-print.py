n = int(input())

k = n - 2
l = 1
print('* ' * n)
for i in range(2, n):
    print('* ' * l + '  ' * k + '* ' * 1)
    k -= 1
    l += 1
if n != 1:
    print('* ' * n)