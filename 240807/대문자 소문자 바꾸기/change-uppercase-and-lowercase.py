a = input()

for i in a:
    if i >= 'A' and i <= 'Z':
        print(chr(ord(i) + 32),end='')
    else:
        print(chr(ord(i) - 32),end='')