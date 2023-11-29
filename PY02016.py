def sol(n, a):
    for i in a:
        if a.get(i)> n//2:
            return i
    return "NO"
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    dd = {}
    for i in a:
        if dd.get(i)== None:
            dd[i] =1
        else:
            dd[i]+= 1
    print(sol(n, dd))