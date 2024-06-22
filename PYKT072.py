n = int(input())
a = []


def check(a, b):
    l = len(a)
    if a == b:
        return 0
    for i in range(l):
        a = a[1:]+a[0]
        if a == b:
            return i+1
    return -1


for i in range(n):
    a.append(input())


def sol(a, n, ans):
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                k = check(a[j], a[i])
                if k == -1:
                    return -1
                else:
                    cnt += k
        ans = min(ans, cnt)
    return ans


print(sol(a, n, 1e9))
