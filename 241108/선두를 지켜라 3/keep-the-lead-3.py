n, m = map(int, input().split())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

totalTime = 0
for i in range(len(A)):
    totalTime += A[i][1]

curA = []
curB = []
momA = 0
momB = 0

for i in range(n):
    for _ in range(1, int(A[i][1])+1):
        momA += int(A[i][0])
        curA.append(momA)

for i in range(m):
    for _ in range(1, int(B[i][1])+1):
        momB += int(B[i][0])
        curB.append(momB)

top = []
for i in range(totalTime):
    if i == 0:
        if curA[i] > curB[i]:
            top.append('A')
        else:
            top.append('B')
        continue
    if curA[i] > curB[i]:
        top.append('A')
    elif curA[i] < curB[i]:
        top.append('B')
    else:
        top.append('S')

cnt = 1
for i in range(totalTime-1):
    nxt = top[i+1]
    if nxt != top[i]:
        cnt += 1
        
print(cnt)