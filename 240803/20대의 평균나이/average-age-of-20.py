s = 0
i = 0
while 1:
    n = int(input())
    if n >= 30:
        break
    s += n
    i += 1
print(f'{s/i:.2f}')