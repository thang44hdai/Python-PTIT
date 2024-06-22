
for _ in range(int(input())):
    n = int(input())
    a = [0]
    for i in range(1, n+1):
        a.append(i)
    ans = []
    while True:
        ans.append(a[1:])
        i = n-1
        while i > 0 and a[i] >= a[i+1]:
            i -= 1
        if i == 0:
            break
        k = n
        while a[k] <= a[i]:
            k -= 1
        a[i], a[k] = a[k], a[i]
        l, r = i+1, n
        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    print(len(ans))
    ans = reversed(ans)
    for i in ans:
        for j in i:
            print(j, end="")
        print(end=' ')
    print()
