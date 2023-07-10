n = int(input())
l = list(map(int, input().split()))

ans = []
for i in range(len(l)):
    ans.append(l[i])
    if (len(ans) >= 2 and (ans[-1]+ans[-2]) % 2 == 0):
        ans.pop()
        ans.pop()
print(len(ans))
