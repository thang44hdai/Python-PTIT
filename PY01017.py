for _ in range(int(input())):
    n = input()
    st = []
    for i in n:
        if len(st) == 0:
            st.append(i)
        else:
            if st[-1] == i:
                st.append(i)
            else:
                print(len(st), st[-1], sep="", end="")
                st.clear()
                st.append(i)
    if len(st) > 0:
        print(len(st), st[-1], sep="", end="")
    print()
