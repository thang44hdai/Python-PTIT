ans = []
a = []


def Try(i, n, sum):
    if sum > n:
        return
    if sum == n:
        ans.append([i for i in a])
    for j in range(i, 0, -1):
        a.append(j)
        Try(j, n, sum+j)
        a.pop()


for t in range(int(input())):
    ans = []
    a = []
    n = int(input())
    Try(n, n, 0)
    print(len(ans))
    for i in ans:
        print("(", end="")
        print(*i, end="")
        print(")", end=" ")
    print()
