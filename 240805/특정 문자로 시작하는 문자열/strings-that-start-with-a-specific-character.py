n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
c = input()
rtn = 0
tmp = []
for i in range(n):
    if arr[i][0] != c:
        continue
    else:
        tmp.append(arr[i])
        rtn += len(arr[i])
print(f'{len(tmp)} {rtn/len(tmp):.2f}')