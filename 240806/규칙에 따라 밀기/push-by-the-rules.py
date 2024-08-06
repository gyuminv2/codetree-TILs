s1 = input()
s2 = input()

for i in s2:
    if i == 'L':
        s1 = s1[1:] + s1[0]
    else:
        s1 = s1[-1] + s1[0:-1]
print(s1)