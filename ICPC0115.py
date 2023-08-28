import math

for _ in range(int(input())):
    n = input()
    if int(n) == sum(math.factorial(int(i)) for i in n):
        print("Yes")
    else:
        print("No")
    