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