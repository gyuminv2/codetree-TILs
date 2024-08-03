s = 0
i = 0
while 1:
    n = int(input())
    if n >= 30 or n < 20:
        break
    s += n
    i += 1
if i != 0:
    print(f'{s/i:.2f}')