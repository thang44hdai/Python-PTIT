def check(n):
    for i in range(len(n)-1):
        if(n[i]>n[i+1]):
            return "NO"
    return "YES"
for i in range(int(input())):
    n = input()
    print(check(n))