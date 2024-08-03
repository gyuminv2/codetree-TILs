n = int(input())
s = 0
i = 0
while n < 30:
    s += n
    i += 1
    n = int(input())
print(f'{s/i:.2f}')