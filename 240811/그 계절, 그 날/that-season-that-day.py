Y, M, D = map(int, input().split())

def check_yoon(Y):
    if Y % 4 == 0:
        return 1
    elif Y % 4 == 0 and Y % 100 == 0and Y % 400 == 0:
        return 1
    elif Y % 4 == 0 and Y % 100 == 0:
        return 0
    return 0

yoon = check_yoon(Y)

def check_season(M, D):
    if 3 <= M and M <= 5:
        if 4 == M and D == 31:
            return -1
        return 'Spring'
    if 6 <= M and M <= 8:
        if 6 == M and D == 31:
            return -1
        return 'Summer'
    if 9 <= M and M <= 11:
        if (9 == M or 11 == M) and D == 31:
            return -1
        return 'Fall'
    if 12 == M or 1 == M:
        if 1 == M and D == 31:
            return -1
        return 'Winter'
    if 2 == M:
        if yoon == 1 and D >= 30:
            return -1
        elif yoon == 0 and D == 31:
            return -1
        else:
            return 'Winter'
    
season = check_season(M, D)
print(season)