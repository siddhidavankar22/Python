'''if __name__ == "__main__":
    #this is how to write main
   
   grade = int (input("enter a grade"))
    if grade < 50 :
        print("fail")
    else:
        print("pass")

    marks = int (input("enter your marks"))
    if marks > 150:
        print("fuck",end='')
        #to print output of two different statements use the above syntax with end
    else:
        print("dengey",end='')

    a=1
    print(a)
    '''

if __name__ == "__main__":
    n = int(input("enter your value n"))+1
    for i in range(0, n, 1):
        print(i, end=' ')
