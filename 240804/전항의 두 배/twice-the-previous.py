a, b = map(int, input().split())

print(a, end=' ')
print(b, end=' ')
for i in range(8):
    c = b + 2 * a
    a, b = b, c
    print(c, end=' ')