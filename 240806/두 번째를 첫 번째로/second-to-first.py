s = input()

tar = s[1]
des = s[0]

for i in s:
    if i == tar:
        print(des, end='')
    else:
        print(i, end='')