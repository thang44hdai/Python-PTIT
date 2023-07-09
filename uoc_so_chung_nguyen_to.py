from math import*

def check_nguyen_to(n):
    if n<=1:
        return "NO"
    for i in range(2, int(sqrt(n))+1):
        if(n%i==0):
            return "NO"
    return "YES"

for i in range(int(input())):
    a, b = map(int, input().split())
    n = gcd(a, b)
    sum = 0
    while n>0:
        sum+=n%10
        n = int(n/10)
    print(check_nguyen_to(sum))