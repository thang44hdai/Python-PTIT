leng = int(1e6+5)
prime = [1]*leng

prime[0] = prime[1] = 0
for i in range(1001):
    if prime[i] == 1:
        for j in range(i*i, leng, i):
            prime[j] = 0


def check(n):
    n1 = n[::-1]
    if n1 == n:
        return False
    if prime[int(n)] == 0:
        return False
    if prime[int(n1)] == 0:
        return False

    return True


for _ in range(int(input())):
    n = int(input())
    for i in range(2, n):
        j = str(i)
        j = j[::-1]
        if int(j) < n:
            if check(str(i)) == True:
                if int(str(i)[::-1]) > i:
                    print(i, str(i)[::-1], sep=" ", end=" ")
    print()
