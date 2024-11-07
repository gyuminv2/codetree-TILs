n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def diff(arr, i):
    a = arr[i][0]
    b = arr[i][2]
    c = arr[i][1]
    d = arr[i][3]
    
    if a < arr[i-1][0]:
        a = arr[i-1][0]
    elif a > arr[i-1][2]:
        a = arr[i-1][2]
    
    # if b < arr[i-1][0]:
    #     b = arr[i-1][0]
    # elif b > arr[i-1][2]:
    #     b = arr[i-1][2]

    if c < arr[i-1][1]:
        c = arr[i-1][1]
    elif c > arr[i-1][3]:
        c = arr[i-1][3]

    # if d < arr[i-1][1]:
    #     d = arr[i-1][1]
    # elif d > arr[i-1][3]:
    #     d = arr[i-1][3]

    return(abs(b-a)*abs(d-c))

blue = 0
for i in range(len(arr)):
    if i == 0 :
        continue
    if i % 2 == 0:
        blue -= diff(arr, i)
    else:
        blue += abs(arr[i][2] - arr[i][0]) * abs(arr[i][3] - arr[i][1])

print(blue)