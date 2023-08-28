for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        l = i+1
        r = n-1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                cnt += 1
                break
            elif a[i]+a[l]+a[r] > 0:
                r -= 1
            else:
                l += 1
    print(cnt)
