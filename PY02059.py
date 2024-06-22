import math
n, m = map(int, input().split())


def check(n):
    if n <= 1:
        return 0
    for i in range(2, int(math.sqrt(n))+1, 1):
        if n % i == 0:
            return 0
    return 1


a = []
for i in range(n):
    a.append([int(i) for i in input().split()])
ans_max = -1
for i in a:
    for j in i:
        if check(j) == 1:
            ans_max = max(ans_max, j)
if ans_max == -1:
    print("NOT FOUND")
else:
    print(ans_max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == ans_max:
                print(f"Vi tri [{i}][{j}]")
