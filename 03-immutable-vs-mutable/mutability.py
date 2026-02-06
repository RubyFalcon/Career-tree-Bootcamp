# How can you prove string is immutable? In python

name = "Tupay"
print(id(name)) #this id is the objects memory address
name = "John"
print(id(name)) #this id changes , so we know that the memory address has changed,

age = 2
age = 20
# we can also see that by trying to change a char in the string it will result in an error.

name =  "Tupay"
new_name = name.replace("u", "o") #creates a new string replacing a said character or string
print(new_name) 

fruits = ["apple", "banana", "cherry"]
fruits[0] = "pineapple"
print(fruits) # ['pineapple', 'banana', 'cherry']
# we can see that list are mutable
fruits[0:2] = ["apricot", "guava"]
print(fruits) # ['apricot', 'guava', 'cherry']
# How many bytes for python list: 

my_nums = [1,2,3,4,5]
print(id(my_nums)) #4374697216
my_nums[2] = 300
print(id(my_nums)) #4374697216
# we can see the id stays the same, so we know both lists have the same memory allocation
