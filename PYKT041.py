n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = 0


def C(n):
    return n*(n-1)/2


for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        if a[i][j] == "C":
            sum1 += 1
        if a[j][i] == "C":
            sum2 += 1
    ans += C(sum1) + C(sum2)
print(int(ans))
