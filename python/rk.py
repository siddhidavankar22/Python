x = int(input("enter your first number: "))
y = int(input("enter your second number: "))
z = int(input("enter your third number: "))
maximum = 'the number which is max is'
if x > y:
    if x > z:
        maximum = x
        print(maximum)
elif y > x:
    if y > z:
        maximum = y
        print(maximum)
else:
    maximum = z
    print(maximum)
