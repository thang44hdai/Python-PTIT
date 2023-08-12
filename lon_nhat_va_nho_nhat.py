for _ in range(int(input())):
    l = []
    st = set()
    for i in range(int(input())):
        n = input()
        l.append(n)
        st.add(n)
    l.sort()
    l.sort(key = lambda x: len(x))
    if len(st)==1:
        print("BANG NHAU")
    else:
        print(*l)