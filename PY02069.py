n, m = [int(i) for i in input().split()]
a = [] * m
for i in range(n):
    a.append(input().split())
Max = 0
for i in range(n):
    for j in range(m):
        x = a[i][j]
        if len(x)>1 and x == x[::-1] and int(x)>Max:
            Max = int(x)
if Max == 0:
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == str(Max):
                print('Vi tri [', i, '][', j, ']', sep = '')
