from math import *
def prime(n):
    if n<=1:
        return 0
    for i in range(2, isqrt(n)+1, 1):
        if n%i==0:
            return 0
    return 1
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        cnt = 0
        for i in range(1, n, 1):
            if gcd(i, n)==1:
                cnt+=1
        if prime(cnt):
            print("YES")
        else:
            print("NO")