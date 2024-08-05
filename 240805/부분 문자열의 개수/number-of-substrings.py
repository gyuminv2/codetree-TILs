a = input()
b = input()
rtn = 0
for i in range(len(a)):
    if a[i:len(b)+i] == b:
        rtn += 1
print(rtn)