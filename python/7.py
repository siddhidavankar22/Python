if __name__ == "__main__":
    x = int(input("enter your value x:"))
    y = int(input("enter your value y:"))
    z = int(input("enter your value z:"))
    if (x+y+z)/3 < 50:
        print("inka ekkuva enter chey bey")
    elif (x+y+z)/3 < 75:
        print("parledu")
    else:
        print("avatalaki dengey")

    x = int(input("enter your value x:"))
    y = int(input("enter your value y:"))
    z = int(input("enter your value z:"))

    sums = x+y+z
    avg = sum/3
    if avg < 50 and sums > 100:
        print("inka ekkuva enter chey bey")
    elif avg < 75 and sums > 200:
        print("parledu")
    else:
        print("avatalaki dengey")

    b = avg
    print(b)
