def fizz_buzz(number):
    # while number != 0:
    if (number % 3 == 0) and (number % 5 == 0):
        return 'Fizz_buzz'
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return 'Buzz'
    if number == 7:
        return number

    return 'improper input'
    # break


print(fizz_buzz(30))
