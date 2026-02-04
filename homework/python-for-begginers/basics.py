# This covers variables, inputs, type conversion and string

# variables
full_name,age, new_patient = "John Smith", 22, True
# can be declared on one line using ,

# print(full_name) -> print displays our variable values
# print(age)
# print(new_patient)


#receiving input
# name = input("Tell me your name: ")
# print(f"Hello {name}") -> formatted string

# birth_year = input('Birth year: ')
# age = 2026 - int(birth_year) -> using type conversion t
# to turn our str into an int
# we have int(), str(), float(), bool()
# print(f"your age is {age}")

# Exercise 01: Ask user weight in lbs, convert to kg and print

weight_lbs = input("Weight in lbs: ")
weight_kg = int(weight_lbs) * 0.453

print(weight_kg)

# Strings
user = "Tupay"
user[0] # returns the character at index 0
user[0:4] # returns char at 0 but not including 4
user[:-1] #returns chars from 0 up until last character excl
user[1:] # returns chars from 1 up and including last
# Exercise 02: what will be printed?
name = "Jennifer"
print(name[1:-1])

#String methods:
# Q: What is a method?
# A: a method is a function belonging to an object or class

# len: returns length of a string -> len is a function
course = "Python for Beginners"
print(len(course)) #output: 20
# important we can use this to set limits 
# e.g password max.min

# upper: a method which uppercases the string
print(course.upper()) #upper doesnt modify our string, 
# it creates a new string and returns it
print(course)

# lower: lowercases a string
print(course.lower())

# find : returns the index of a character
course.find('o') # returns 4

course.find('O') #returns -1 if character is not found

course.find('Beginners') #returns 11 , 
# returns the index of the 1st letter that it matches

# replace: returns a new string with the string literal replaced
print(course.replace("Beginners", "Absolute Beginners"))
print(course)

# check existense of characters using 'in':

print('Python' in course ) # True
# this expression produces a bool value, so its a 
# Boolean expression

print("python" in course) #Q: why is it false?
# A: case sensitive

