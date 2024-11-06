n = int(input())

phy = []
for i in range(1, n+1):
    # for j in range(len(phy)):
    #     if 
    phy.append(list(map(int, input().split())) + [i])

# print(sorted(phy, key=lambda x : (x[0], -x[1])))
phy.sort(key=lambda x : (x[0], -x[1]))

for i in range(n):
    for j in range(3):
        print(phy[i][j], end=' ')
    print('')