from math import ceil, floor
from utils import print_matrix
# Loops
fruits = ["apple", "banana", "mango", "strawberry", "guava"]

# Print fruits
my_it = iter(fruits)
# print(next(my_it))
# print(next(my_it))
# print(*fruits)

for fruit in fruits:
    pass
    # print(type(fruit))
    # print(fruit)

colors = ("Orange", "Blue", "White")

for color in colors:
    pass
    # print(color)

student = {"name":"Alice", "age": 20, "grade": "A"}

for key in student:
    print(f"{key}: {student[key]}")

# Enumerate
print("Without Enumerate")

# Index, fruit name
for i in range(len(fruits)):

    print(f"At index {i} we have: {fruits[i]}")

# or
for fruit in fruits:
    print(f"At index {fruits.index(fruit)} we have: {fruit}")
# with enumerate:
for index, fruit in enumerate(fruits):
    print(f"at index {index} we have {fruit}")


# What if we want to start at a later number:
for greaterindex, fruit in enumerate(fruits, start=15):
    print(f"{index}: {fruit}")

# using 2 variables for loop dict:

products = {
    "Laptop": 99.9,
    "Mouse": 45.5,
    "Keyboard":120.5,
    "Headphones": 200.0
    }

for product, price in products.items():
    pass
    # print(f"{product:<15} :${price:0.2f}") #products:<15  left allignspace in betweem, 0.2f 2 decimal places

print(f"{'Total':<15} ${sum(products.values()):>8.2f}") #< - left align, > right align

x = 78.18
print(floor(x))
print(ceil(x))
print(round(x))



print_matrix(1,5)


# 1: 
classes = {
    "Monday" : ["Maths", "Science", "English"],
    "Tueday": ["History", "Maths", "Pe"],
    "Wednesday ": ["Science", "English", "Art"]
    }

for day,subjects in classes.items():
    print(f"\n{day}:")
    for period, subject in enumerate(subjects, start=1):
        print(f"Period {period} : {classes[day]}")