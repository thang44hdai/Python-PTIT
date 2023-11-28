n = int(input())
a= []
while len(a)<n:
    a += [int(i) for i in input().split()]

dd = []
for i in a:
    if i % 2 == 0:
        dd.append(0)
    else:
        dd.append(1)
c = [i for i in a if i % 2 == 0]
l = [i for i in a if i % 2 == 1]
c.sort()
l = sorted(l, key=lambda x: -x)
i1 = 0
i2 = 0
for i in dd:
    if i == 0:
        print(c[i1], end=" ")
        i1 += 1
    else:
        print(l[i2], end=" ")
        i2 += 1
