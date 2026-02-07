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


# Arithmetics
x = 40
y = 10

print(x/y) # division (returns a float even if number is whole - 4.0)
print(x // y) # floor division (returns a whole number rounded down  4)
print(x % y) #modulo - returns remainder
print (2 * 3) # multiply
print(2 **3 ) # exponent 

first_name = "Tupay"
last_name = "Felkin"

# concatenation
full_name = first_name + last_name
print(full_name)
print(first_name + " " + last_name)


# operands +-/* / operators
print(first_name * 10) #returns first name 10 times
print(5 * 6)


x,y,z =  1,3,7 # multiple assignments of variables

#f-string
print(f"My full name is {first_name} {last_name}")