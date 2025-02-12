if __name__ == "__main__":
    x = 0
    y = 1
    n = int(input("enter vale of n:"))
    print(x, y, end=' ')
    for i in range(0, n-2):
        nxt = x+y
        x = y
        y = nxt
        print(nxt, end=' ')
