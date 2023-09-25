n = int(input())
l = [int(i) for i in input().split()]
l.sort()
check = True
for i in range(len(l)-1):
    if l[i+1]-l[i] != 1:
        print(l[i]+1)
        check = False
        break
if check == True:
    print(n+1)
