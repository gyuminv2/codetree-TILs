n = int(input())

jenga = []
for _ in range(n):
    jenga.append(int(input()))

n1, m1 = map(int, input().split())
n2, m2 = map(int, input().split())

tmp = []
rtn = []

for i in range(n):
    if n1 - 1 <= i and i <= m1 - 1:
        continue
    else:
        tmp.append(jenga[i])

for i in range(len(tmp)):
    if n2 - 1 <= i and i <= m2 - 1:
        continue
    else:
        rtn.append(tmp[i])

print(len(rtn))
if len(rtn) != 0:
    for i in range(len(rtn)):
        print(rtn[i])