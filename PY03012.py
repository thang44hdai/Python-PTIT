def cmp(a, b):
    if a[0] != b[0]:
        return a[0] > b[0]
    return a[1] < b[1]


l = []
for _ in range(int(input())):
    name = input()
    c, t = [int(i) for i in input().split()]
    l.append([name, c, t])
l = sorted(l, key=lambda x: (-x[1], x[2], x[0]))
for i in l:
    print(i[0], i[1], i[2], sep=" ")
