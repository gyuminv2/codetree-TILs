n = int(input())
i = 1
while n > 1:
    n //= i
    i += 1
print(i-1)