from math import*
def main():
    n = input()
    cnt=0
    for i in n:
        if(i>='a' and i<='z'):
            cnt+=1
    if(cnt>=len(n)-cnt):
        print(n.lower())
    else:
        print(n.upper())
if __name__ == "__main__":
    main()
    
