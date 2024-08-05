n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
c = input()
rtn = 0
for i in range(n):
    if arr[i][0] != c:
        arr.remove(arr[i])
    else:
        rtn += len(arr[i])
print(f'{len(arr)} {rtn/len(arr):.2f}')