n = int(input())
l= [] 
for i in range(n):
    #l.append(list(map(int, input().split())))
    l.append([int(i) for i in input().split()])
    #l[i] = [int(x) for x in input().split()]
k = int(input())
sum = 0
for i in range(n):
    for j in range(n):
        if i > j:
            sum = sum + l[i][j]
        elif i < j:
            sum = sum - l[i][j]
if abs(sum) <= k:
    print("YES", abs(sum), sep="\n")
else:
    print("NO", abs(sum), sep="\n")
