a, b = map(int, input().split())
n = input()

code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cn = int(n)
base_10 = 0
for i in range(len(n)):
    tr = cn % 10
    cn //= 10
    base_10 += tr * a**i

base_b = ''
while base_10 != 0:
    base_b += str(base_10%b)
    base_10 //= b

print(base_b[::-1])