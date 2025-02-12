numbers = [1, 2, 3, 3, 4, 5]
# this is how to convert a list into a set
first = set(numbers)
# this is how to define a set
second = {2, 6, 7}

# '|' concatinates both the sets with the same elements
print(first | second)
# '&' finds similar elements in both the sets
print(first & second)
# '-' removes the similar elements in both the sets
print(first-second)
# '^' adds only the unique elements
print(first ^ second)
