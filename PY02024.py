def mul(x):
    tich = 1
    for i in x:
        tich *= int(i)
    return tich


for _ in range(int(input())):
    n = int(input())
    a = [i for i in input().split()]
    a.sort(key=lambda x: (mul(x), int(x)))
    print(*a)