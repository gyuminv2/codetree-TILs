arr = []
for i in range(3):
    arr.append(len(input()))
print(max(arr) - min(arr))