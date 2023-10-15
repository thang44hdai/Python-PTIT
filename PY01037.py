import math


def dem_uoc(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            cnt += 2
        if i*i == n:
            cnt -= 1
    return cnt


def sol(n):
    cnt = dem_uoc(n)
    for i in range(1, n):
        cnt -= dem_uoc(i)
        if cnt < 0:
            return False
    return cnt >= 0


for _ in range(int(input())):
    n = int(input())
    print(sol(n))
    # while True:
    #     if sol(n) == True:
    #         print(n)
    #         break
    #     n += 1
