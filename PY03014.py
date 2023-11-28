for _ in range(int(input())):
    n = input()
    st = []
    idx = 1
    ans = []
    for i in range(len(n)):
        if n[i] == "(":
            st.append(idx)
            ans.append(idx)
            idx += 1
        elif n[i] == ")":
            ans.append(st[-1])
            st.pop()
    print(*ans)
