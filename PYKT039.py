def sol(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    print(sol(a, b, n))
