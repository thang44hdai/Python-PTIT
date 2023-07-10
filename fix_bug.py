def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    print(a)

x, y = map(int, input().split())
gcd(x, y)
