#print statement
print("Hello teachers")

#variables
my_name = "Tupay" # = is an assignemnt operator
my_name = 24 # python is a dynamically typed language, meaning we can re-assign a string data-type to an int
my_name = "Tupay"

#constants
BANKINTEREST = 15 #constants are used to tell someone we do not plan to change the value

#in python we use snake_case meaning my_name and not myName(camelCase)
print(my_name)

#functions
def write_name(name):
    print(f"hello {name}")


def square(num):
    return num * num

write_name("Tupay") 
print(square(2))

#data type in Python
# int - whole numbers,
# float - decimal numbers
# string -  seq. characters
# bool - logical values, True or False
# dictionaries - key/value pairs {'key':'value'}
# lists - Mutable  objects [1,2,3,4,6]
# tuples - Immutable objects (1,2,4,5)
# set - unique objects {1,2,3,4,5}