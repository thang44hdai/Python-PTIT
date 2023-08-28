for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k, n):
        print(a[i], end=" ")
    for i in range(k):
        print(a[i], end=" ")
    print()
