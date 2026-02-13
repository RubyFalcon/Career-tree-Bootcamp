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

# 02:
numbers = [1,3,5,7,8]

for num in numbers:
    if num % 2 == 0:
        print(f"Found it: {num}")
        break
    print(f"{num} is odd, contunuing...")

my_fruits = ["apple", "banana", "mango", "strawberry", "guava"]

search = "cherry"
for index, fruit in enumerate(fruits):
    if fruits == search:
        print(f"Found {fruit} at index {index}")
else:
    print(f"{search} not found")


# 02: password catcher

def password_catcher(password, max_attemps):
    for attempt in range(1, max_attempts+1):
        input_pass = input(f"Attempt {attempt}/ 3 - Type password: ")
        if(input_pass == password):
            print("Correct pass! Logged in.")
            break
        else: 
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Inccorect  password you have {remaining} attempts remaining.")
    else:
        print("Max attempts reached")

# password_catcher(max_attempts = 3,password = "password1234")
 
# While loops:

# While vs for

# When number of iterations is KNOWN - for or while
# When number of iterations UNKNOWN - use While only
# When u dont know no. iterations, u cannot use for loop, u have to use while

responses = ['hello','quit', 'more','less']

index = 0
while index < len(responses):
    user_input = responses[index]
    if user_input == 'quit':
        print("Exiting...")
        break
    index += 1
