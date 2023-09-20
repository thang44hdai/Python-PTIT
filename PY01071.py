n = input()
if len(n)>=4:
    if n[-1].lower()=='y' and n[-2].lower()=='p' and n[-3]=='.':
        print('yes')
    else:
        print("no")
else: 
    print("no")