n = int(input())
s = 0
i = 0
while 1:
    s += n
    i += 1
    n = int(input())
    if n >= 30:
        break
print(f'{s/i:.2f}')