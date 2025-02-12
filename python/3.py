'''if __name__ == "__main__":
    n = int(input("enter your value n:"))
    for i in range(0,n,1):
        k = 1
        for j in range(0,n,1):
            if j>=n-i-1:
                print (k,end = ' ')
                k = k+1
            else:
                print ('  ',end = '')
        print()'''

if __name__ == "__main__":
    itr = 1
    n = int(input("enter your value n:"))
    for i in range(0, n):
        for j in range(0, n):
            # print(f"i = {i} j = {j}  itr = {itr}")
            if j >= n-i-1:
                for k in range(0, itr):
                    print('*', end=' ')
                itr += 2
                break
            else:
                print(' ', end=' ')

        print()
