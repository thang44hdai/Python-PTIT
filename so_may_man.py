from math import*

def main():
    n = input()
    cnt= n.count("4")+n.count("7")
    if cnt==4 or cnt==7:
        print("YES")
    else:
        print("NO")
if __name__=="__main__":
    main()