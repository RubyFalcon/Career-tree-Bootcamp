for item in  "Python": #for loops iterate over a collection
    # item is a loop variable - each iteration item will hold one item
    # in goes over a collection, in this case a string, which is a sequence of characters
    print(item)

# Create a list:
for item in ['Mosh','John', 'Sarah']:
    print(item)
    #  list - list of items

for item in [1,2,3,4]:
    print(item * 2) #we can manipulate each item as we want

# What if we want a large list of numbers? Typing to would be tedious
for item in range(10):
    print(item) # prints 0-9, not 10

for item in range(5, 10,2): #(start,stop, step)
    print(item) # prints 0-9, not including 10


# Exercise : create a program to get total cost of shopping cart

prices = [10,20,30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested loops:
    # can be used for coordinate values

for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

# Challenge: Print F with X's as a 2d array

numbers = [5,2,5,2,2]

for number in numbers:
    for x in range(number):
        print("X")
    print("\n")