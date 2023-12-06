from math import sqrt


n = int(input())
a = [int(i) for i in input().split()]
b = []
dd = {}
for i in a:
    try:
        dd[i] += 1
    except:
        dd[i] = 1
        b.append(i)
sum = sum(b)
check = False


def nt(n):
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return 0
    return 1


l = 0
for i in range(len(b)):
    l += b[i]
    if nt(l) == 1 and nt(sum-l) == 1:
        print(i)
        check = True
        break
if check == False:
    print("NOT FOUND")
