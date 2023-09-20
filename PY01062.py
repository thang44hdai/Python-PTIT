prime = [1] * 1000001
prime[0] = prime[1] = 0
for i in range(2, 1001):
    if prime[i] == 1:
        for j in range(i * i, 1000001, i):
            prime[j] = 0
for _ in range(int(input())):
    n = input()
    if prime[len(n)] == 0:
        print("NO")
        continue
    cnt = 0
    for i in n:
        if prime[int(i)] == 1:
            cnt += 1
    if cnt > len(n) - cnt:
        print("YES")
    else:
        print("NO")
