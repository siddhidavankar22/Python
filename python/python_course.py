# functions
def eligiblity():
    age = int(input("enter your age: "))
    message = 'eligble to drink' if age > 18 else 'not eligble to drink'
    print(message)


def greet(name):
    print(f'hi {name}')


greet('Ashish')
eligiblity()
# lists
letters = ['s', 'b', 'd']
matrix = [[0, 1], [2.3]]
zeros = [0]*5
combined = zeros+letters
print(combined)


letter = ['a', 'b', 'c']
letter.append('d')
letter.insert(2, 'f')
del letter[0:3]
print(letter)

letters.pop()
print(letters)

numbers = [20, 30, 50, 84, 12, 8, 6, 5, 4, 7]
numbers.sort()
print(numbers)

items = [
    ('product1', 20),
    ('product2', 15),
    ('product3', 5)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

products = [
    ('pro1', 25),
    ('pro2', 5),
    ('pro', 15)
]

# this is how to map a list or tuple
# map function syntax
x = map(lambda ite: ite[1], products)
for ite in x:
    print(ite)


i = [
    ('product1', 20),
    ('product2', 15),
    ('product3', 5)
]

# filter function
b = list(filter(lambda a: a[1] >= 10, i))
print(b)

list1 = [10, 20, 30]
list2 = [100, 200, 300]
print(list(zip('abc', list1, list2)))


def Dictionary(**kwargs):
    for n, a in kwargs.items():
        print(f"{n} : {a} ")


Dictionary(n=2, a=3)
