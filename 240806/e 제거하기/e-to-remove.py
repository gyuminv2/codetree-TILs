s = input()
flag = 0

for i in s:
    if i == 'e' and flag == 0:
        flag = 1
        continue
    else:
        print(i, end='')