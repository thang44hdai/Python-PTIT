n = int(input())
st = []
vt = ["C", "B", "A"]
ans = ""


def Try(a=0, b=0, c=0):
    global ans
    if len(ans) > n:
        return
    elif a > 0 and a <= b and b <= c:
        st.append(ans)
    for i in range(3):
        ans += vt[i]
        if i == 0:
            Try(a, b, c+1)
        elif i == 1:
            Try(a, b+1, c)
        elif i == 2:
            Try(a+1, b, c)
        ans = ans[:-1]


Try()
st = sorted(st, key=lambda x: (len(x), x))

for i in st:
    print(i)
