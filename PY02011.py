n = int(input())
a = list(map(int, input().split()))
idx = 0 
ans = int(1e9)
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(a[i]-a[j])
    if sum < ans:
        ans = sum
        idx = i
print(ans, a[idx])