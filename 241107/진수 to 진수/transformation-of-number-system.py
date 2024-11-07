a, b = map(int, input().split())
n = input()

code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cn = int(n)
base_10 = 0
for i in range(len(n)):
    tr = cn % 10
    cn //= 10
    base_10 += tr * a**i

base_2 = ''
while base_10 != 0:
    if base_10 % b != 0:
        base_2 += '1'
    else:
        base_2 += '0'
    base_10 //= b

print(base_2)