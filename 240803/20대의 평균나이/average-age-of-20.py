s = 0
i = 0
while 1:
    try:
        n = int(input())
    except EOFError:
        break
    if n >= 30:
        break
    s += n
    i += 1
if i != 0:
    print(f'{s/i:.2f}')