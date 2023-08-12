def mul(n):
    n = str(n)
    res = 1
    for i in n:
        res *= int(i)
    return res

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l.sort(key = lambda x: mul(x))
    print(*l)
