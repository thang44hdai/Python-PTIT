for _ in range(int(input())):
    n = input()
    total = 0
    mutil = 1
    cnt0 = 0
    cnt_le = 0
    for i in range(len(n)):
        if i % 2 == 0:
            total += int(n[i])
        else:
            cnt_le += 1
            if int(n[i]) == 0:
                cnt0 += 1
            else:
                mutil *= int(n[i])
    print(total, end=" ")
    if cnt0 == cnt_le:
        print(0)
    else:
        print(mutil)
