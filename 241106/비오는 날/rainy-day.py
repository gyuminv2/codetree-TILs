n = int(input())

arr = []
for _ in range(n):
    tmp = input().split()
    if tmp[2] == 'Rain':
        arr.append(tmp)

small = 21001231
j = 0
for i in range(len(arr)):
    tmp = ''.join(arr[i][0].split('-'))
    if small > int(tmp):
        small = int(tmp)
        j = i

print(arr[j][0], arr[j][1], arr[j][2])