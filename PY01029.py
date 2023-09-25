from math import gcd


for _ in range(int(input())):
    n = input()
    n_re = n[::-1]
    if gcd(int(n), int(n_re)) == 1:
        print("YES")
    else:
        print("NO")
