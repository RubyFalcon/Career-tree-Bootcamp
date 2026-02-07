# Tuples :  immutable lists - can't mutate or change
numbers = (1,2,3)
# Methods :  count and index
# Use case : when we dont want to change something later
# numbers[0] = 10 #error: cannot mutate

# Unpacking: powerful python feature
coordinates = (1,2,3) #x,y,z

# We want these values for complex expressions/ formulas
# coordinates[0] * coordinates [1] *coordinates[2] #really long and unreadable

# Classical approach:
x,y,z = coordinates[0],coordinates[1], coordinates[2]

# Better approach
x,y,z = coordinates #shorthand to achieve same 
# python will get first item then assign to the 1st variable, and continue
# called Unpacking
print(x)
print(y)
print(z)


