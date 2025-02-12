if __name__ == "__main__":

    arr = [1,2,3,4,5]
    for i in range(0,len(arr),1):
        print (arr[i], end = " ")
   
    arr = [i.split() for i in input().split(',')]
   #this is how to input an array
    print (arr)
