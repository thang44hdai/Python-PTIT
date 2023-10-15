n, m = map(int, input().split())
a = []
ans_max = -1
ans_min = int(1e9)
for i in range(n):
    vt = [int(j) for j in input().split()]
    a.append(vt)
    ans_max = max(ans_max,  max(j for j in vt))
    ans_min = min(ans_min, min(j for j in vt))

ans = []
for i in range(n):
    for j in range(m):
        if a[i][j] == ans_max-ans_min:
            ans.append([i, j])
if len(ans) == 0:
    print("NOT FOUND")
else:
    print(ans_max-ans_min)
    for i in ans:
        print(f"Vi tri [{i[0]}][{i[1]}]")
