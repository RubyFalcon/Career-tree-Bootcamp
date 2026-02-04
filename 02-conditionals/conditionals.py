# Conditionals: Logical conditions which helps us to make decisions
age = 10

if age >= 18:
    print("You are an adult")
elif age < 18 and age >= 0:
    print("You are too young to drink")
else:
    print("Logical error")

score = 60
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Fail")


age = 30
can_drive = False

if age >= 25 and not can_drive: # with or, only 1 needs to be True, with and, all need to be True
    print("Welcome")

# Type conversion:
# number_str = input("Enter a number") #input function returns a str
# print(type(number_str))
number = int(input("Enter a number: ") )

if number %2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
   
