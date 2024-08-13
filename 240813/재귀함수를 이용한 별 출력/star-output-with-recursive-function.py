n = int(input())

def 카우닝ssTar(n, t):
    if n == t:
        return 0
    print('*' * (t+1))
    return 카우닝ssTar(n, t+1)

카우닝ssTar(n, 0)