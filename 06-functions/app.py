# Recap: loops
names = ["Tupay", "john", "bob"]
for name in names:
    pass
    # print(name.capitalize())

index = 0

while index < len(names):
    pass
    # print(names[index])
    index +=1

# # While has to be used when we know how many iterations we would eneed
# while True:
#     user_input = input("Etner your name: ")
#     print(f"User entered {user_input}")
#     if user_input.lower() == "quit":
#         print("Exiting")
#         break

numbers = [10,23,45,86,67,99]
target = 67

for index, number in enumerate(numbers):
    if number == target:
        print(f"{number} Found!")
        break
else:
    print(f"{target} not fond")

data = [100,-200,-50,300, 150]

for val in data:
    if val < 0:
        print("Data is invalid")
        break
else:
    print("Data is valid")

text = "Hello world, how are you"
vowels = 'aeiou'
vowel_count = 0

for char in text:
    if char.lower() in vowels:
        vowel_count += 1
        print(f"Vowel {char} found")

print(f"Total Vowels: {vowel_count}")

def greet() -> None:
    """This is a simple greet Function""" #docstring - adds context to functions classes
    print("Hello world")

def welcome_message() -> None:
    """Displays a welcome message for all users"""
    print("="*70)
    print("Welcome to Python Programming")
    print("Let's learn about FUNCTIONS today!!")
    print("="*70)


def my_greet(name:str, age:int) -> None:
    """Greets a person with a name"""
    print(f"Hello  {name}, your age is {age}")

def add_nums(num1: int, num2:int):
    result:int = num1 + num2
    print(f"{num1} + {num2} =  {result}")

def sum_nums(*nums:int) -> int:
    total = 0
    for num in nums:
        total += num
    return total

print(sum_nums(1,2,3,6))
