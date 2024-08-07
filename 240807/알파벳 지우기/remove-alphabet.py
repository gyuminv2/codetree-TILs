a = list(input())
b = input()
tmp = []
num1 = 0
num2 = 0

for i in a:
    if i.isdigit():
        tmp.append(i)
num1 += int(''.join(tmp))

tmp.clear()

for i in b:
    if i.isdigit():
        tmp.append(i)
num2 += int(''.join(tmp))

print(num1 + num2)