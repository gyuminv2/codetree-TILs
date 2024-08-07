n = int(input())
n_lst = []
rtn = 0

for i in range(n):
    n_lst.append(input())
    rtn += int(n_lst[i])
rtn = str(rtn)
print(rtn[1:] + rtn[0])