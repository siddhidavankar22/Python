if __name__ == "__main__":
    n = int(input("enter your value n:"))
    for i in range(0,n,1):
        for j in range(0,i+1,1):
            print(j+1,end = ' ')
        print()