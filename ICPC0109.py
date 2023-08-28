for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min1, min2, min3 = 1e8, 1e8, 1e8
    for i in range(n):
        if a[i] < min1:
            min1, min2, min3 = a[i], min1, min2
        elif a[i] < min2:
            min1, min2, min3 = min1, a[i], min2
        elif a[i] < min3:
            min3 = a[i]
    print(min1 + min2 + min3)
