from math import sqrt

n = int(input())
a = list(map(int, input().split()))
b = []
st = {}
for i in a:
    if st.get(i) == None:
        b.append(i)
        st[i]=1
a = b
n = len(a)
def check(n):
    if n<=1:
        return 0
    for i in range(2, int(sqrt(n))):
        if n%i==0:
            return 0
    return 1
total = sum(a)
left = 0
flag = 0
for i in range(n):
    left += a[i]
    if check(left) == 1 and check(total-left)==1:
        print(i)
        flag = 1
        break
if flag == 0:
    print("NOT FOUND")