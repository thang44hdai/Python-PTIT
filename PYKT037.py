def mod(a, b):
    n = a % b
    if n <= 9:
        return n
    return chr(ord('A')+n-10)


for _ in range(int(input())):
    n, b = map(int, input().split())
    ans = []
    while n > 0:
        ans.append(mod(n % b, b))
        n = n//b
    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end="")
    print()
