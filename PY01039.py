def sol(n):
    l = len(n)
    st = set()
    for i in range(l):
        st.add(n[i])
        if len(st) > 2:
            return "NO"
    i = 0
    while i+2 < l:
        if n[i] != n[i+2]:
            return "NO"
        else:
            i += 2
    i = 1
    while i+2 < l:
        if n[i] != n[i+2]:
            return "NO"
        else:
            i += 2
    return "YES"


for _ in range(int(input())):
    n = input()
    print(sol(n))
